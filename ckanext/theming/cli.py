from __future__ import annotations

import contextlib
import inspect
import logging
import os
import re
import shutil
from collections import defaultdict
from collections.abc import Collection

import click
from jinja2 import TemplateNotFound
from jinja2.runtime import Macro

import ckan.plugins.toolkit as tk
from ckan.common import config

from . import lib, reference

log = logging.getLogger(__name__)

__all__ = ["theme"]

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
        name = config["ckan.ui.theme"]

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
            el = getattr(ui, item)
            if not el:
                el = "❌"
                click.echo(f"{item}: {el}")


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
def component_check(ctx: click.Context, theme: lib.Theme):
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
    """Validate theme implementation against core CKAN templates."""
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

        blocks = set(tpl.blocks)
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
                blocks.update(parent_tpl.blocks)

                with open(parent_tpl.filename) as src:
                    parent_content = src.read()

                extends = RE_EXTEND.search(parent_content)
                parent_name = extends.group("name") if extends else None

        if hierarchy:
            click.secho(click.style("Hierarchy: ", fg="yellow") + ", ".join(hierarchy))

        if hierarchy_break:
            click.secho(click.style("Hierarchy detection interrupted on: ", fg="red") + hierarchy_break)

        if tpl.blocks:
            click.secho(click.style("Own blocks: ", fg="yellow") + ", ".join(sorted(tpl.blocks)))

        if blocks:
            click.secho(click.style("All blocks: ", fg="yellow") + ", ".join(sorted(blocks)))

        click.echo()
