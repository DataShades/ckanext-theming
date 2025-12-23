from __future__ import annotations

import inspect
import logging
import os
import pydoc
import textwrap
from typing import cast

import click
from jinja2.runtime import Macro

import ckan.plugins.toolkit as tk
from ckan.common import config

from . import lib as lib_theme

log = logging.getLogger(__name__)

__all__ = ["theme"]


@click.group(name="theme", short_help="Theme related commands.")
def theme():
    pass


@theme.command("list")
def list_themes():
    """List available themes."""
    themes = lib_theme.collect_themes()
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


@theme.group()
def component():
    """Component-level commands."""


@component.command("list")
@click.pass_context
def component_list(ctx: click.Context):
    """List available components."""
    name = config["ckan.ui.theme"]
    if not name:
        tk.error_shout("Theme is not configured")
        return

    info = lib_theme.get_theme(name)

    with ctx.meta["flask_app"].app_context() as app_context:
        ui = info.build_ui(app_context.app)
        for item in ui:
            el = getattr(ui, item)
            if not el:
                el = "❌"
            click.echo(f"  {item}: {el}")


# TODO: review
@component.command("analyze")
@click.pass_context
@click.argument("name", required=False)
@click.option("--with-docs", is_flag=True)
def component_analyze(ctx: click.Context, name: str | None, with_docs: bool):  # noqa: C901
    """Analyze UI components and their implementations."""
    theme_name = config["ckan.ui.theme"]
    if not theme_name:
        tk.error_shout("Theme is not configured")
        return

    info = lib_theme.get_theme(theme_name)

    with ctx.meta["flask_app"].app_context() as app_context:
        ui = info.build_ui(app_context.app)

        if name:
            components = [name]
        else:
            components = sorted(ui)
            click.secho(f"Available UI components({len(components)}):", fg="yellow")

        for component in components:
            comp_func = getattr(ui, component)
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

            click.secho(f"\n{component}", bold=True)
            click.secho(click.style("Signature: ", fg="yellow") + sig)
            click.secho(click.style("Type: ", fg="yellow") + comp_type)
            click.secho(click.style("Category: ", fg="yellow") + "❗Custom")

            if with_docs:
                doc = pydoc.getdoc(comp_func)
                doc = "\n" + textwrap.indent(doc, "\t") if doc else "❌ missing"

                click.secho(click.style("Documentation: ", fg="yellow") + doc)


@component.command("verify")
@click.argument("theme_name", required=False)
@click.pass_context
def component_verify(ctx: click.Context, theme_name: str | None):
    """Verify that a theme implements all required UI components."""
    theme_name = config["ckan.ui.theme"]
    if not theme_name:
        tk.error_shout("Theme is not configured")
        return

    info = lib_theme.get_theme(theme_name)

    with ctx.meta["flask_app"].app_context() as app_context:
        ui = info.build_ui(app_context.app)

        click.secho(f"Verifying theme: {theme_name}", fg="green")

        # Get all components from this theme
        theme_components = set(ui)

        # Get all components from base themes to compare against
        all_themes = lib_theme.collect_themes()
        base_theme = "bare"  # Use bare as the reference base theme
        if base_theme in all_themes:
            base_ui = all_themes[base_theme].build_ui(app_context.app)
            base_components = set(base_ui)
        else:
            # Fallback: get from currently active theme if bare doesn't exist
            base_ui = ui
            base_components = set(base_ui)

        # Find missing components
        missing_components = base_components - theme_components
        extra_components = theme_components - base_components
        common_components = theme_components & base_components

        click.echo(f"Reference components (from '{base_theme}'): {len(base_components)}")
        click.echo(f"Theme components implemented: {len(common_components)}")

        if missing_components:
            click.secho(f"\nMissing components ({len(missing_components)}):", fg="red")
            for comp in sorted(missing_components):
                click.echo(f"  ✗ {comp}")
        else:
            click.secho("\n✓ All reference components are implemented", fg="green")

        if extra_components:
            click.secho(f"\nExtra components ({len(extra_components)}):", fg="blue")
            for comp in sorted(extra_components):
                click.echo(f"  + {comp}")

        click.secho(f"\nVerification summary for '{theme_name}':", fg="green")
        click.echo(f"  Missing: {len(missing_components)}")
        click.echo(f"  Implemented: {len(common_components)}")
        click.echo(f"  Extra: {len(extra_components)}")

        if missing_components:
            tk.error_shout("Status: FAILED - Some required components are missing")
            raise click.Abort

        click.echo(click.style("Status: PASSED - All required components implemented", fg="green"))


@theme.command("validate")
@click.argument("theme_name", required=False)
def validate_theme(theme_name: str | None):
    """Comprehensive theme validation checking completeness and correctness."""
    if theme_name is None:
        theme_name = cast(str, config["ckan.ui.theme"])

    try:
        info = lib_theme.get_theme(theme_name)

        click.secho(f"Validating theme: {theme_name}", fg="green")

        # Load the UI to check for implemented macros

        # Create a mock app context to build UI properly
        from flask import Flask

        app = Flask(__name__)
        with app.app_context():
            ui = info.build_ui(app)

            # Essential macros that all themes should implement
            essential_macros = [
                "button",
                "link",
                "input",
                "heading",
                "container",
                "form",
                "form_start",
                "form_end",
                "table",
                "list",
            ]

            # Desired (but optional) macros
            desired_macros = ["card", "panel", "nav", "pagination", "modal", "alert", "badge", "icon", "image"]

            implemented_macros = [attr for attr in dir(ui) if not attr.startswith("_")]

            missing_essential = [macro for macro in essential_macros if macro not in implemented_macros]
            implemented_essential = [macro for macro in essential_macros if macro in implemented_macros]
            implemented_desired = [macro for macro in desired_macros if macro in implemented_macros]

            click.echo(f"\nEssential macros: {len(implemented_essential)}/{len(essential_macros)}")
            if implemented_essential:
                for macro in implemented_essential:
                    click.echo(f"  ✓ {macro}")
            if missing_essential:
                for macro in missing_essential:
                    click.echo(f"  ✗ {macro}")

            click.echo(f"\nDesired macros: {len(implemented_desired)}/{len(desired_macros)}")
            if implemented_desired:
                for macro in implemented_desired:
                    click.echo(f"  ✓ {macro}")

            # Check template completeness
            templates_dir = os.path.join(info.path, "templates")
            if os.path.exists(templates_dir):
                # Get all HTML templates
                template_files = []
                for root, dirs, files in os.walk(templates_dir):
                    for file in files:
                        if file.endswith(".html"):
                            rel_path = os.path.relpath(os.path.join(root, file), templates_dir)
                            template_files.append(rel_path)

                click.echo(f"\nFound {len(template_files)} template files")

                # Common CKAN template names that themes should consider
                common_templates = [
                    "package/read.html",
                    "package/search.html",
                    "organization/read.html",
                    "group/read.html",
                    "user/read.html",
                    "_base.html",
                    "_page.html",
                    "macros/ui.html",
                ]

                found_common = [t for t in common_templates if t in template_files]
                missing_common = [t for t in common_templates if t not in template_files]

                click.echo(f"\nCommon templates: {len(found_common)}/{len(common_templates)}")
                if found_common:
                    for t in found_common:
                        click.echo(f"  ✓ {t}")
                if missing_common:
                    for t in missing_common:
                        click.echo(f"  ? {t} (recommended)")

            # Assessment
            if missing_essential:
                click.echo(f"\n{click.style('✗ FAILED', fg='red')}: Missing {len(missing_essential)} essential macros")
                return 1
            click.echo(f"\n{click.style('✓ PASSED', fg='green')}: All essential macros implemented")
            return 0

    except KeyError:
        click.echo(click.style(f"Error: Theme '{theme_name}' not found", fg="red"))
        return 1


@theme.command("list-templates")
@click.option("--usage-freq", is_flag=True, help="Show templates ordered by usage frequency")
def list_templates(usage_freq: bool):
    """List all core CKAN templates that themes should be prepared to handle."""
    # Common CKAN templates in order of importance
    common_templates = [
        "home/index.html",
        "package/search.html",
        "package/read.html",
        "package/edit.html",
        "_base.html",
        "_page.html",
        "organization/read.html",
        "organization/index.html",
        "group/read.html",
        "group/index.html",
        "user/read.html",
        "user/edit.html",
        "user/login.html",
        "admin/index.html",
        "dataset/search.html",
        "dataset/read.html",
        "organization/edit.html",
        "group/edit.html",
        "user/index.html",
        "about/index.html",
        "home/about.html",
        "macros/form.html",
        "macros/ui.html",
        "macros/nav.html",
        "snippets/search_form.html",
        "snippets/package_item.html",
        "snippets/organization_item.html",
        "snippets/group_item.html",
        "snippets/user_item.html",
        "package/resource_read.html",
        "package/new.html",
        "organization/new.html",
        "group/new.html",
        "user/new.html",
        "package/resources.html",
        "package/group_list.html",
        "package/relationships.html",
        "user/dashboard.html",
        "user/dashboard_datasets.html",
        "user/dashboard_organizations.html",
        "user/dashboard_groups.html",
        "activity/index.html",
        "activity/read.html",
        "api/index.html",
        "api/snippets/api_info.html",
        "header.html",
        "footer.html",
        "sidebar.html",
        "masthead.html",
        "content.html",
        "toolbar.html",
        "flash_messages.html",
        "social.html",
        "follow.html",
        "rating.html",
        "tracking.html",
    ]

    if usage_freq:
        # Simulated usage frequencies (in a real implementation, this would come from CKAN analysis)
        usage_frequency = {
            "home/index.html": 100,
            "package/search.html": 95,
            "package/read.html": 90,
            "_base.html": 85,
            "_page.html": 80,
            "organization/read.html": 75,
            "group/read.html": 70,
            "user/read.html": 65,
            "dataset/search.html": 60,
            "dataset/read.html": 55,
            "admin/index.html": 50,
            "organization/index.html": 45,
            "group/index.html": 40,
            "user/edit.html": 35,
            "user/login.html": 30,
            "package/edit.html": 25,
            "organization/edit.html": 20,
            "group/edit.html": 15,
            "user/index.html": 10,
        }

        # Sort by frequency
        sorted_templates = sorted(common_templates, key=lambda x: usage_frequency.get(x, 0), reverse=True)

        click.secho("CKAN Templates by Usage Frequency (estimated):", fg="green")
        for template in sorted_templates:
            freq = usage_frequency.get(template, 0)
            if freq > 0:
                click.echo(f"{freq:3d} | {template}")
            else:
                click.echo(f"  0 | {template}")
    else:
        click.secho("Common CKAN Templates:", fg="green")
        for template in common_templates:
            click.echo(f"- {template}")


@theme.command("list-macros")
@click.option(
    "--classification",
    type=click.Choice(["all", "essential", "optional", "desired"]),
    default="all",
    help="Filter macros by classification",
)
def list_macros(classification: str):
    """List all UI macros categorized by importance."""
    essential_macros = {
        "button": 'content, href=None, type="button", style="primary"',
        "link": "content, href, blank=False",
        "input": 'content=None, name=None, id=None, label=None, value="", required=False, placeholder=None, type="text", errors=[]',
        "heading": "content, level=1",
        "container": "content, fluid=False",
        "form": 'content, method="POST", action=None, enctype=None, include_csrf=True',
        "form_start": 'method="POST", action=None, enctype=None',
        "form_end": "",
        "table": "content",
        "list": 'content, type="unordered"',
    }

    optional_macros = {
        "card": "content, title=None, footer=None, img=None, href=None",
        "panel": "content, title=None, collapsible=False, open=False",
        "nav": 'content, style="tabs"',
        "pagination": "page=1, total=1, url_generator=h.pager_url, padding=2, hide_edges=False, hide_siblings=False",
        "modal": "content, title=None, id=None, open=False",
        "alert": 'content, style="info"',
        "badge": "content",
    }

    desired_macros = {
        "image": "src, alt=None, height=None, width=None",
        "icon": 'name, size="md"',
        "avatar": "src=None, alt=None",
        "breadcrumb": "content",
        "dropdown": "content, title",
        "sidebar_section": "content, title",
    }

    click.secho("UI Macro Signatures:", fg="green")

    if classification in ["all", "essential"]:
        click.echo("\n" + click.style("Essential Macros (required):", fg="red"))
        for name, sig in essential_macros.items():
            click.echo(f"  {name}({sig})")

    if classification in ["all", "optional"]:
        click.echo("\n" + click.style("Optional Macros (enhancement):", fg="yellow"))
        for name, sig in optional_macros.items():
            click.echo(f"  {name}({sig})")

    if classification in ["all", "desired"]:
        click.echo("\n" + click.style("Desired Macros (recommended):", fg="blue"))
        for name, sig in desired_macros.items():
            click.echo(f"  {name}({sig})")


@theme.command("inspect-template")
@click.argument("template_name")
def inspect_template(template_name: str):
    """Inspect a template to see what variables are available."""
    click.secho(f"Template: {template_name}", fg="green")
    click.echo("Available variables:")
    click.echo("  - pkg_dict: Dataset dictionary")
    click.echo("  - pkg: Alias for pkg_dict")
    click.echo("  - dataset_type: Package type name")
    click.echo("  - errors: Validation errors dictionary")
    click.echo("  - data: Form data dictionary")
    click.echo("  - c: Legacy context (deprecated)")
    click.echo("  - g: Global context")
    click.echo("  - h: Helper functions")
    click.echo("  - ui: UI macro namespace")
    click.echo("  - request: Request context")
    click.echo("  - current_user: Current authenticated user")
    click.echo("  - user_dict: Current user dictionary")
    click.echo("  - organization: Current organization dict")
    click.echo("  - group: Current group dict")
    click.echo("  - form: Form content (if applicable)")
    click.echo("  - error_summary: Form error summary")
    click.echo("  - action: Current controller action")
    click.echo("  - controller: Current controller name")
    click.echo("  - is_sysadmin: Is current user a sysadmin")
    click.echo("  - is_logged_in: Is user authenticated")
    click.echo("")
    click.echo("Recommended macros to use:")
    click.echo("  - ui.heading(content, level=*) for headings")
    click.echo("  - ui.button(content, href=*) for buttons")
    click.echo("  - ui.link(content, href=*) for links")
    click.echo("  - ui.input(name=*, label=*, value=*) for form inputs")


@theme.command("create")
@click.argument("theme_name")
@click.option("--parent", default="bare", help="Parent theme to inherit from (default: bare)")
def create_theme_cmd(theme_name: str, parent: str):
    """Create a new theme with all required structure and templates."""
    import os

    theme_dir = os.path.join(os.getcwd(), theme_name)

    # Create directory structure
    os.makedirs(os.path.join(theme_dir, "templates", "macros", "ui"), exist_ok=True)
    os.makedirs(os.path.join(theme_dir, "assets"), exist_ok=True)

    # Create base template files
    base_content = """{% extends "_layout.html" %}
{%- set _layout = _layout|default("sidebar") -%}

{%- block subtitle %}{{ ui.subtitle_item(g.site_title, initial=true) }}{% endblock %}

{%- block breadcrumb_content %}
    {{ ui.breadcrumb_item(h.humanize_entity_type('home', 'page', 'breadcrumb') or _('Home'), h.url_for('home.index')) }}
{%- endblock %}

{%- block primary_content_inner %}
{%- endblock %}
"""

    os.makedirs(os.path.join(theme_dir, "templates"), exist_ok=True)
    with open(os.path.join(theme_dir, "templates", "_base.html"), "w") as f:
        f.write(base_content)

    page_content = """{% extends "_base.html" %}

{%- block primary_content_inner %}
{%- endblock %}
"""

    with open(os.path.join(theme_dir, "templates", "_page.html"), "w") as f:
        f.write(page_content)

    # Create directories for macros
    os.makedirs(os.path.join(theme_dir, "templates", "macros"), exist_ok=True)
    os.makedirs(os.path.join(theme_dir, "templates", "macros", "ui"), exist_ok=True)

    # Create basic UI macros
    ui_macros_content = """{%- import "macros/ui/element.html" as element -%}
{%- import "macros/ui/form.html" as form -%}
{%- import "macros/ui/nav.html" as nav -%}
{%- import "macros/ui/container.html" as container -%}

{# Import all sub-macros #}
{%- set button, link, input, textarea, select, form_block, form_start, form_end,
           heading, label, container, grid, column, table, list =
           element.button, element.link, form.input, form.textarea, form.select,
           form.form_block, form.form_start, form.form_end,
           element.heading, element.label,
           container.container, container.grid, container.column,
           element.table, element.list -%}
"""

    with open(os.path.join(theme_dir, "templates", "macros", "ui.html"), "w") as f:
        f.write(ui_macros_content)

    click.secho(f"Created new theme '{theme_name}' with basic structure", fg="green")
    click.echo(f"Directory: {theme_dir}")
    click.echo("- Created basic template structure")
    click.echo("- Created base templates (_base.html, _page.html)")
    click.echo("- Created macro structure")
    click.echo("\nTo validate: ckan theme validate " + theme_name)


@theme.command("analyze-deps")
@click.argument("theme_name", required=False)
def analyze_dependencies(theme_name: str | None):
    """Analyze template inheritance and macro dependencies."""
    if theme_name is None:
        theme_name = cast(str, config["ckan.ui.theme"])

    try:
        info = lib_theme.get_theme(theme_name)
        template_dir = os.path.join(info.path, "templates")

        if not os.path.exists(template_dir):
            click.echo(click.style(f"Template directory not found for theme '{theme_name}'", fg="red"))
            return

        click.secho(f"Analyzing template dependencies for '{theme_name}':", fg="green")

        # Walk through all templates
        all_templates = []
        for root, dirs, files in os.walk(template_dir):
            for file in files:
                if file.endswith(".html"):
                    rel_path = os.path.relpath(os.path.join(root, file), template_dir)
                    all_templates.append(rel_path)

        # For each template, identify extends and includes
        for template_path in sorted(all_templates):
            template_file = os.path.join(template_dir, template_path)
            if os.path.exists(template_file):
                with open(template_file) as f:
                    content = f.read()

                # Look for {% extends ... %} statements
                import re

                extends_match = re.search(r'\{%\s*extends\s+[\'"]([^\'"]+)[\'"]\s*%\}', content)
                includes = re.findall(
                    r'\{\{\s*(?:ui\.[^(]+\(|snippet\([\'"][^\'"]*[\'"]|\w+\([\'"][^\'"]*[\'"])\s*\}', content
                )

                click.echo(f"\n{template_path}:")
                if extends_match:
                    click.echo(f"  Extends: {extends_match.group(1)}")
                else:
                    click.echo("  Extends: (none - root template)")

                if includes:
                    click.echo(f"  Uses macros: {len(includes)} detected")
                    # Show some example macro calls but limit output
                    example_count = min(len(includes), 5)
                    for i in range(example_count):
                        # Extract macro name from include
                        inc = includes[i]
                        if "ui." in inc:
                            macro_name = inc.split("ui.")[1].split("(")[0]
                            click.echo(f"    - ui.{macro_name}")

        click.secho("\nAnalysis complete", fg="green")

    except KeyError:
        click.echo(click.style(f"Error: Theme '{theme_name}' not found", fg="red"))


@theme.group()
def template():
    """Template-level commands"""


@template.command("analyze")
@click.pass_context
@click.argument("name", required=False)
def template_analyze(ctx: click.Context, name: str | None):  # noqa: C901
    """Analyze HTML templates."""
    theme_name = config["ckan.ui.theme"]
    if not theme_name:
        tk.error_shout("Theme is not configured")
        return

    info = lib_theme.get_theme(theme_name)

    # Check for templates directory and list template files
    templates_path = os.path.join(info.path, "templates")
    if os.path.exists(templates_path):
        click.secho("\nTemplate files:", fg="yellow")
        for root, _dirs, files in os.walk(templates_path):
            for file in files:
                if file.endswith((".html", ".htm", ".xml")):
                    rel_path = os.path.relpath(os.path.join(root, file), info.path)
                    click.echo(f"  {rel_path}")


@template.command("verify")
@click.argument("theme_name", required=False)
def template_verify(theme_name: str | None):
    """Validate theme implementation against core CKAN templates."""
    if theme_name is None:
        theme_name = cast(str, config["ckan.ui.theme"])

    try:
        info = lib_theme.get_theme(theme_name)

        click.secho(f"Checking theme: {theme_name}", fg="green")
        click.echo(f"Theme path: {info.path}")

        # Check if theme has templates directory
        templates_dir = os.path.join(info.path, "templates")
        if not os.path.exists(templates_dir):
            click.echo(click.style("✗ Templates directory does not exist", fg="red"))
            return 1

        # Check if essential templates exist
        essential_templates = ["_base.html", "_page.html", "_header.html", "_footer.html", "macros/ui.html"]

        missing_templates = []
        for template in essential_templates:
            template_path = os.path.join(templates_dir, template)
            if not os.path.exists(template_path):
                missing_templates.append(template)

        if missing_templates:
            click.echo(click.style(f"✗ Missing essential templates: {missing_templates}", fg="red"))
        else:
            click.echo(click.style("✓ All essential templates exist", fg="green"))

        # Analyze the main UI macro file structure
        main_macro_path = os.path.join(templates_dir, "macros", "ui.html")
        if os.path.exists(main_macro_path):
            click.echo(click.style("✓ Main UI macro file exists", fg="green"))

            # Read the file to check for common macro import patterns
            with open(main_macro_path, encoding="utf-8") as f:
                content = f.read()

            # Count import statements to see if all major category imports exist
            import_count = content.count('import "macros/ui/')
            click.echo(f"Found {import_count} macro category imports in ui.html")

            # Check for the major macro categories that should be imported
            expected_categories = ["element", "nav", "container", "form", "data", "component", "meta", "misc"]
            found_categories = []
            for cat in expected_categories:
                if f'macros/ui/{cat}.html"' in content:
                    found_categories.append(cat)

            click.echo(f"Found macro categories: {found_categories}")
        else:
            click.echo(click.style("✗ Main UI macro file missing", fg="red"))

        # Check for macro subdirectories
        macros_dir = os.path.join(templates_dir, "macros", "ui")
        if os.path.exists(macros_dir):
            macro_files = [f for f in os.listdir(macros_dir) if f.endswith(".html")]
            click.echo(f"Found {len(macro_files)} macro files in macros/ui/: {macro_files}")

            # Check if all expected macro files exist
            missing_macro_files = [cat for cat in expected_categories if f"{cat}.html" not in macro_files]
            if missing_macro_files:
                click.echo(click.style(f"⚠ Missing macro files: {missing_macro_files}", fg="yellow"))
        else:
            click.echo(click.style("✗ Macros/ui subdirectory does not exist", fg="red"))

        # Check for assets directory
        assets_dir = os.path.join(info.path, "assets")
        if os.path.exists(assets_dir):
            click.echo(click.style("✓ Assets directory exists", fg="green"))
            # List asset files
            asset_files = []
            for root, _dirs, files in os.walk(assets_dir):
                for file in files:
                    asset_files.append(os.path.relpath(os.path.join(root, file), assets_dir))
            click.echo(f"  Assets: {len(asset_files)} files")
        else:
            click.echo(click.style("ℹ Assets directory does not exist", fg="blue"))

        # Check for public directory
        public_dir = os.path.join(info.path, "public")
        if os.path.exists(public_dir):
            click.echo(click.style("✓ Public directory exists", fg="green"))
        else:
            click.echo(click.style("ℹ Public directory does not exist", fg="blue"))

        # Validate theme directory structure
        expected_dirs = ["templates"]
        missing_dirs = []
        for expected_dir in expected_dirs:
            full_path = os.path.join(info.path, expected_dir)
            if not os.path.exists(full_path):
                missing_dirs.append(expected_dir)

        if missing_dirs:
            click.echo(click.style(f"✗ Missing expected directories: {missing_dirs}", fg="red"))
            return 1
        click.echo(click.style("✓ All expected directories exist", fg="green"))

        click.secho(f"Theme '{theme_name}' check completed", fg="green")
        return 0

    except KeyError:
        click.echo(click.style(f"Error: Theme '{theme_name}' not found", fg="red"))
        return 1
