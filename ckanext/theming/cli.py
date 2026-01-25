from __future__ import annotations

import contextlib
import inspect
import logging
import os
import pprint
import random
import re
import shutil
import string
from collections import Counter, defaultdict
from collections.abc import Callable, Collection
from typing import Any

import click
import flask.signals
from jinja2 import Environment, TemplateNotFound
from jinja2.exceptions import UndefinedError
from jinja2.runtime import Macro
from werkzeug.exceptions import NotFound
from werkzeug.routing import BuildError

import ckan.plugins.toolkit as tk
from ckan import model, types
from ckan.common import json
from ckan.plugins import plugin_loaded

from . import lib, reference

log = logging.getLogger(__name__)

__all__ = ["theme"]

RE_COMPONENT = re.compile(r"(?<!\.)ui\.(?!util\.)(?P<name>\w+)")

RE_EXTEND = re.compile(
    r"""
    \{%-?\s*		(?# tag start)
    extends\s+		(?# tag name)
    (?P<name>.+?)	(?# template name. Non-greedy match to exclude leading whitespace)
    \s*-?%\}		(?# tag end)
""",
    re.X,
)


RE_INCLUDE = re.compile(
    r"""
    \{%-?\s*		(?# tag start)
    include\s+		(?# tag name)
    (?P<name>.+?)	(?# template name)
    \s*-?%\}		(?# tag end)
    """,
    re.X,
)


@click.group(name="theme", short_help="Theme related commands.")
def theme():
    pass


def theme_callback(ctx: click.Context, param: click.Parameter, name: str | None):
    if not name:
        name = tk.config["ckan.ui.theme"]

    if not name:
        tk.error_shout("Theme is not configured")
        raise click.Abort

    try:
        return lib.get_theme(name)
    except KeyError as err:
        tk.error_shout(f"Theme {name} is not registered")
        raise click.Abort from err


theme_option = click.option("-t", "--theme", callback=theme_callback)


@contextlib.contextmanager
def _make_ui(ctx: click.Context, theme: lib.Theme):
    """Context manager to build the UI for a theme within a Flask app context."""
    with ctx.meta["flask_app"].app_context() as app_context:
        yield theme.build_ui(app_context.app)


@theme.command("list")
def list_themes():
    """List available themes."""
    themes = lib.collect_themes()
    for name, info in themes.items():
        click.echo(name)
        click.echo(f"  Path: {info.path}")

        lineage = []
        parent = info.parent
        while parent:
            if parent_info := themes.get(parent):
                lineage.append(parent)
                parent = parent_info.parent
            else:
                lineage.append(click.style(parent, fg="red"))

        if lineage:
            click.secho(f"  Extends: {' -> '.join(lineage)}")


@theme.command("create")
@click.argument("name")
@click.argument("location", required=False)
def theme_create(name: str, location: str):
    """Create a new theme with all required structure and templates."""
    if not location:
        location = os.getcwd()
        if not click.confirm(f"No location provided, theme will be created inside `{location}`"):
            raise click.Abort
    bare = lib.get_theme("bare")

    shutil.copytree(bare.path, os.path.join(location, name), ignore=lambda d, f: ["node_modules", "package-lock.json"])


@theme.group()
def component():
    """Component-level commands."""


@component.command("list")
@click.pass_context
@theme_option
def component_list(ctx: click.Context, theme: lib.Theme):
    """List available components."""
    with _make_ui(ctx, theme) as ui:
        for item in ui:
            click.echo(item)


@component.command("analyze")
@click.pass_context
@theme_option
@click.argument("components", nargs=-1)
def component_analyze(ctx: click.Context, components: Collection[str], theme: lib.Theme):  # noqa: C901
    """Analyze UI components and their implementations."""
    with _make_ui(ctx, theme) as ui:
        if not components:
            components = sorted(ui)
            click.secho(f"Available UI components({len(components)}):")

        for component in components:
            comp_func = getattr(ui, component, None)
            if not comp_func:
                tk.error_shout(f"Unknown component {component}")
                continue

            ref = reference.components[component]

            # Try to get the source or signature information
            if isinstance(comp_func, Macro):
                sig = ", ".join(comp_func.arguments)

                if comp_func.catch_varargs:
                    sig = ", ".join([sig, "*varargs"])

                if comp_func.catch_kwargs:
                    sig = ", ".join([sig, "**kwargs"])

                sig = f"({sig})"
                comp_type = "Callable macro" if comp_func.caller else "Macro"

            else:
                sig = str(inspect.signature(comp_func))
                comp_type = type(comp_func).__name__

            click.secho(f"{component}", bold=True)
            click.secho(click.style("Type: ", fg="yellow") + comp_type)
            click.secho(click.style("Category: ", fg="yellow") + ref.category.name)
            click.secho(click.style("Signature: ", fg="yellow") + sig)
            click.echo()


@component.command("check")
@theme_option
@click.pass_context
def component_check(ctx: click.Context, theme: lib.Theme):  # noqa: C901
    """Verify that a theme implements all required UI components."""
    categorized: dict[reference.Category, set[str]] = defaultdict(set)
    for name, info in reference.components.items():
        categorized[info.category].add(name)

    with _make_ui(ctx, theme) as ui:
        # Get all components from this theme
        theme_components = set(ui)
        missing_components = {name: sorted(items - theme_components) for name, items in categorized.items()}

        extra_components = sorted(theme_components.difference(reference.components))

        click.echo(f"Theme implements {len(theme_components)} components")

        for category, items in categorized.items():
            if missing_components[category]:
                click.secho(
                    f"  Missing {len(missing_components[category])} out of"
                    + f" {len(items)} in category {category.name}",
                    fg="yellow",
                )
                click.secho("    " + ", ".join(missing_components[category]), fg="red")

            else:
                click.secho(f"  All components in category {category.name} are implemented", fg="green")
        if extra_components:
            click.secho(f"  Extra components ({len(extra_components)})", fg="yellow")
            click.secho("    " + ", ".join(extra_components), fg="blue")

        with ctx.meta["flask_app"].test_request_context():
            args = {
                "".join(random.sample(string.ascii_letters, 10)): random.randint(0, 100),  # noqa: S311
            }
            rigid: dict[type, dict[str, Exception]] = defaultdict(dict)
            allow_rigid = {"user", "group", "package", "resource", "organization"}

            for name in sorted(theme_components):
                func = getattr(ui, name)
                try:
                    func(**args)
                except Exception as err:  # noqa: BLE001
                    if isinstance(err, UndefinedError) and name in allow_rigid:
                        continue
                    rigid[type(err)][name] = err

            if rigid:
                click.secho(
                    f"  {sum(map(len, rigid.values()))} components produced an error with random arguments",
                    fg="yellow",
                )
                for key, values in rigid.items():
                    click.secho(f"    {key.__name__}:", bold=False)
                    for name, err in values.items():
                        click.secho(f"      {click.style(name, bold=True)}: {err}")


@theme.group()
def template():
    """Template-level commands."""


@template.command("list")
@theme_option
def template_list(theme: lib.Theme):
    """List template files in the theme."""
    root = theme.template_path()
    for path, _, files in os.walk(root):
        relpath = os.path.relpath(path, root)
        if relpath == ".":
            relpath = ""

        for file in files:
            tpl_name = os.path.join(relpath, file)
            reference.templates[tpl_name]
            click.echo(tpl_name)


@template.command("check")
@theme_option
def template_check(theme: lib.Theme):
    """Verify that a theme contains all required templates."""
    categorized: dict[reference.Category, set[str]] = defaultdict(set)
    for name, info in reference.templates.items():
        categorized[info.category].add(name)

    root = theme.template_path()
    templates = {os.path.relpath(os.path.join(path, file), root) for path, _, files in os.walk(root) for file in files}

    click.echo(f"Theme contains {len(templates)} templates")

    missing = {name: sorted(items - templates) for name, items in categorized.items()}
    extra = sorted(templates.difference(reference.templates))

    for category, items in categorized.items():
        if missing[category]:
            click.secho(
                f"  Missing {len(missing[category])} out of" + f" {len(items)} in category {category.name}",
                fg="yellow",
            )
            click.secho("    " + ", ".join(missing[category]), fg="red")

        else:
            click.secho(f"  All templates in category {category.name} are present", fg="green")
    if extra:
        click.secho(f"  Extra templates ({len(extra)})", fg="yellow")
        click.secho("    " + "\n    ".join(extra), fg="blue")


@template.command("analyze")
@click.pass_context
@theme_option
@click.argument("templates", nargs=-1)
@click.option("--relative-filename", is_flag=True)
def template_analyze(  # noqa: C901
    ctx: click.Context, templates: Collection[str], theme: lib.Theme, relative_filename: bool
):
    """Analyze theme templates."""
    root = theme.template_path()
    if not templates:
        templates = {
            os.path.relpath(os.path.join(path, file), root) for path, _, files in os.walk(root) for file in files
        }
        click.secho(f"Available templates({len(templates)}):")

    get_template = ctx.meta["flask_app"].jinja_env.get_template
    for name in sorted(templates):
        try:
            tpl = get_template(name)
        except TemplateNotFound:
            tk.error_shout(f"Template {name} does not exist")
            continue

        ref = reference.templates[name]
        click.secho(f"{name}", bold=True)
        click.secho(click.style("Category: ", fg="yellow") + ref.category.name)
        click.secho(
            click.style("Filename: ", fg="yellow") + os.path.relpath(tpl.filename, os.getcwd())
            if relative_filename
            else tpl.filename
        )

        with open(tpl.filename) as src:
            content = src.read()

        if includes := RE_INCLUDE.findall(content):
            click.secho(click.style("Includes: ", fg="yellow") + ", ".join(i for i in sorted(set(includes))))

        all_blocks: set[str] = set(tpl.blocks)
        hierarchy = []
        hierarchy_break = None

        if extends := RE_EXTEND.search(content):
            parent_name = extends.group("name")
            click.secho(click.style("Extends: ", fg="yellow") + parent_name)

            while parent_name:
                try:
                    parent_tpl = get_template(parent_name.strip("\"'"))
                except TemplateNotFound:
                    hierarchy_break = parent_name
                    break
                hierarchy.append(parent_name)
                all_blocks.update(parent_tpl.blocks)

                with open(parent_tpl.filename) as src:
                    parent_content = src.read()

                extends = RE_EXTEND.search(parent_content)
                parent_name = extends.group("name") if extends else None

        if hierarchy:
            click.secho(click.style("Hierarchy: ", fg="yellow") + ", ".join(hierarchy))

        if hierarchy_break:
            click.secho(click.style("Hierarchy detection interrupted on: ", fg="red") + hierarchy_break)

        if tpl.blocks:
            click.secho(click.style("Explicit blocks: ", fg="yellow") + ", ".join(sorted(tpl.blocks)))

        implicit_blocks = all_blocks.difference(tpl.blocks)
        if implicit_blocks:
            click.secho(click.style("Implicit blocks: ", fg="yellow") + ", ".join(sorted(implicit_blocks)))

        click.echo()


@template.command("component-usage")
@theme_option
@click.pass_context
@click.option("--include-frequency", is_flag=True, help="Include component usage frequency.")
def template_component_usage(ctx: click.Context, theme: lib.Theme, include_frequency: bool):  # noqa: C901
    """Analyze component usage in templates."""
    env: Environment = ctx.meta["flask_app"].jinja_env
    used: dict[str, set[str]] = defaultdict(set)
    counter: Counter[str] = Counter()
    for name in env.list_templates():
        if not name.endswith(".html"):
            continue
        tpl = env.get_template(name)
        if not tpl.filename:
            continue

        with open(tpl.filename) as src:
            for component_name in RE_COMPONENT.findall(src.read()):
                used[component_name].add(tpl.filename)
                counter.update([component_name])

    with _make_ui(ctx, theme) as ui:
        existing = set(ui)

    unused = existing - set(used)
    unknown = set(used) - existing

    if unused:
        click.secho(click.style(f"Unused components({len(unused)}): ", fg="yellow") + ", ".join(sorted(unused)))
    else:
        click.secho("No unused components", fg="green")

    if unknown:
        click.secho(f"Unknown components({len(unknown)}): ", fg="yellow")
        for name in sorted(unknown):
            click.echo(f"  {name}:")
            for tpl_name in sorted(used[name]):
                click.echo(f"    {tpl_name}")

    else:
        click.secho("No unknown components", fg="green")

    if include_frequency:
        click.secho("Component frequency:", fg="yellow")
        for name, count in sorted(counter.items(), key=lambda pair: pair[::-1], reverse=True):
            click.echo(f"{count:> 5}: {name}")


@theme.group()
def endpoint():
    """Endpoint-level commands."""


@endpoint.command("list")
@click.pass_context
def endpoint_list(ctx: click.Context):
    """List registered Flask endpoints."""
    app = ctx.meta["flask_app"]
    for name in app.view_functions:
        click.echo(name)


@endpoint.command("variants")
@click.pass_context
@click.argument("endpoints", nargs=-1)
def endpoint_variants(ctx: click.Context, endpoints: Collection[str]):
    """List variants of Flask endpoints."""
    app = ctx.meta["flask_app"]
    grouped = app.url_map._rules_by_endpoint
    if not endpoints:
        endpoints = tuple(grouped)

    for name in endpoints:
        if name not in grouped:
            tk.error_shout(f"Endpoint {name} does not exist")
            continue

        click.secho(name, bold=True)
        for variant in grouped[name]:
            click.secho(click.style("Rule: ", fg="yellow") + variant.rule)
            click.secho(click.style("Methods: ", fg="yellow") + ", ".join(variant.methods))
            if variant.arguments:
                click.secho(click.style("Arguments: ", fg="yellow") + ", ".join(variant.arguments))
            if variant.defaults:
                click.secho(click.style("Defaults: ", fg="yellow") + repr(variant.defaults))
            click.echo()


class RenderInterceptionError(Exception):
    """Exception raised to intercept Jinja2 template rendering."""


def _render_intercept(condition: Callable[[dict[str, Any]], bool] = lambda kwargs: True):
    """Create a Jinja2 render interceptor that raises an exception when a condition is met."""

    def interceptor(sender: types.CKANApp, **kwargs: Any):
        if condition(kwargs):
            raise RenderInterceptionError(kwargs)

    return interceptor


def _observe_endpoint(
    endpoint: str,
    params: dict[str, Any],
    app: types.CKANApp,
    user: model.User | None = None,
    method: str = "get",
) -> dict[str, Any]:
    """Observe the template and context variables used by a Flask endpoint."""
    try:
        url = tk.url_for(endpoint, **params)
    except BuildError as err:
        tk.error_shout(err)
        raise click.Abort from err

    with (
        app.test_request_context(url, method=method),
        flask.signals.before_render_template.connected_to(_render_intercept()),
    ):
        if user:
            tk.login_user(user)

        try:
            app.full_dispatch_request()

        except NotFound as err:
            tk.error_shout(err)
            raise click.Abort from err

        except RenderInterceptionError as err:
            return err.args[0]

        tk.error_shout(f"Endpoint {endpoint} did not render any template")
        raise click.Abort


@endpoint.command("observe", context_settings={"allow_extra_args": True, "ignore_unknown_options": True})
@click.pass_context
@click.argument("endpoint")
@click.option("--auth-user")
@click.option("--method", default="get")
@click.option("-v", "--verbose", is_flag=True, help="Show full context variables.")
@click.option("--ignore", default=("request", "session", "g", "csrf_token", "current_user"), multiple=True)
def endpoint_observe(  # noqa: PLR0913
    ctx: click.Context,
    endpoint: str,
    auth_user: str,
    verbose: bool,
    ignore: tuple[str, ...],
    method: str,
):
    """Observe the template and context variables used by a Flask endpoint."""
    app = ctx.meta["flask_app"]
    user = model.User.get(auth_user)

    with app.app_context():
        try:
            params = dict(arg.split("=") for arg in ctx.args)
        except ValueError as err:
            tk.error_shout("Extra arguments must follow the format: NAME=VALUE")
            raise click.Abort from err

        data = _observe_endpoint(endpoint, params, app, user=user, method=method)

        click.secho(click.style("Template: ", fg="yellow") + data["template"].name)
        click.secho(
            click.style("Context types(use `-v` to see values): ", fg="yellow")
            + pprint.pformat({key: type(value) for key, value in data["context"].items() if key not in ignore})
        )
        if verbose:
            click.secho(
                click.style("Context variables: ", fg="yellow")
                + pprint.pformat({key: value for key, value in data["context"].items() if key not in ignore})
            )


def _dump_encoder(value: Any):
    return f"<INVALID JSON: {value}>"


@endpoint.command("dump")
@click.pass_context
@click.option("--auth-user", required=True)
@click.option("--user", required=True)
@click.option("--package", required=True)
@click.option("--resource", required=True)
@click.option("--resource-view", required=True)
@click.option("--organization", required=True)
@click.option("--group", required=True)
@click.option("--ignore", default=("request", "session", "g", "csrf_token", "current_user"), multiple=True)
@click.option("--endpoints", multiple=True)
@click.option("-v", "--verbose", is_flag=True)
def endpoint_dump(  # noqa: PLR0912, PLR0913, C901
    ctx: click.Context,
    auth_user: str,
    user: str,
    package: str,
    resource: str,
    resource_view: str,
    organization: str,
    group: str,
    ignore: tuple[str, ...],
    endpoints: tuple[str, ...],
    verbose: bool,
):
    """Dump templates and context variables used by Flask endpoints in JSON format."""
    app = ctx.meta["flask_app"]

    if not (auth_obj := model.User.get(auth_user)):
        tk.error_shout("Object specified by `--auth` does not exist")
        raise click.Abort

    user_dict = tk.get_action("user_show")({"ignore_auth": True}, {"id": user})
    package_dict = tk.get_action("package_show")({"ignore_auth": True}, {"id": package})
    resource_dict = tk.get_action("resource_show")({"ignore_auth": True}, {"id": resource})
    resource_view_dict = tk.get_action("resource_view_show")({"ignore_auth": True}, {"id": resource_view})
    group_dict = tk.get_action("group_show")({"ignore_auth": True}, {"id": group})
    organization_dict = tk.get_action("organization_show")({"ignore_auth": True}, {"id": organization})

    result = {}
    with app.app_context():
        for name, route in reference.routes.items():
            if endpoints and name not in endpoints:
                continue

            if route.plugin and not plugin_loaded(route.plugin):
                continue

            if not route.check_availability():
                continue

            params = route.make_params(
                name,
                {
                    "resource": resource_dict,
                    "package": package_dict,
                    "resource_view": resource_view_dict,
                    "group": group_dict,
                    "organization": organization_dict,
                    "user": user_dict,
                },
            )
            params.update(route.args)

            data = _observe_endpoint(
                route.endpoint or name, params, app, user=auth_obj if route.authenticated else None
            )

            result[name] = {
                "template": data["template"].name,
                "context_types": {
                    key: type(value).__name__ for key, value in data["context"].items() if key not in ignore
                },
            }
            if verbose:
                result[name]["context_variables"] = {
                    key: value for key, value in data["context"].items() if key not in ignore
                }

    click.echo(json.dumps(result, default=_dump_encoder))
