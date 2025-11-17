from __future__ import annotations

import logging
import os
from typing import cast

import click

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
        click.echo(f"\tPath: {info.path}")

        lineage = []
        parent = info.parent
        while parent:
            if parent_info := themes.get(parent):
                lineage.append(parent)
                parent = parent_info.parent
            else:
                lineage.append(click.style(parent, fg="red"))

        if lineage:
            click.secho(f"\tExtends: {' -> '.join(lineage)}")


@theme.command("debug")
def debug_themes():
    """Comprehensive debug information about all registered themes."""
    themes = lib_theme.collect_themes()

    click.secho("=== Theme Debug Information ===", fg="green")

    for name, info in themes.items():
        click.secho(f"\nTheme: {name}", fg="yellow", bold=True)
        click.echo(f"  Path: {info.path}")

        # Check if the theme directory exists
        if os.path.exists(info.path):
            click.echo(click.style("  ✓ Directory exists", fg="green"))
        else:
            click.echo(click.style("  ✗ Directory does not exist", fg="red"))

        # Check for theme templates directory
        templates_path = os.path.join(info.path, "templates")
        if os.path.exists(templates_path):
            click.echo(click.style("  ✓ Templates directory exists", fg="green"))
        else:
            click.echo(click.style("  ✗ Templates directory missing", fg="red"))

        # Check for macro UI file
        macro_path = os.path.join(templates_path, "macros", "ui.html")
        if os.path.exists(macro_path):
            click.echo(click.style("  ✓ Macros UI file exists", fg="green"))
        else:
            click.echo(click.style("  ✗ Macros UI file missing", fg="red"))

        # Show parent relationship
        if info.parent:
            click.echo(f"  Parent: {info.parent}")
            if info.parent in themes:
                click.echo(click.style("  ✓ Parent theme exists", fg="green"))
            else:
                click.echo(click.style("  ✗ Parent theme does not exist", fg="red"))
        else:
            click.echo("  Parent: None (base theme)")


@theme.command("components")
@click.pass_context
def list_components(ctx: click.Context):
    """List available components."""
    theme = cast(str, config["ckan.ui.theme"])
    info = lib_theme.get_theme(theme)

    ui = info.build_ui(ctx.obj.app._wsgi_app)

    for item in ui:
        click.echo(f"\t{item}: {getattr(ui, item)}")


@theme.command("analyze")
@click.argument("theme_name", required=False)
@click.pass_context
def analyze_theme(ctx: click.Context, theme_name: str | None):
    """Analyze a specific theme's UI components and their implementations."""
    if theme_name is None:
        theme_name = cast(str, config["ckan.ui.theme"])
        click.echo(f"Using active theme: {theme_name}")
    else:
        click.echo(f"Analyzing theme: {theme_name}")

    try:
        info = lib_theme.get_theme(theme_name)
        ui = info.build_ui(ctx.obj.app._wsgi_app)

        click.secho(f"\n=== Analysis of '{theme_name}' theme ===", fg="green")
        click.echo(f"Theme path: {info.path}")

        if info.parent:
            click.echo(f"Parent theme: {info.parent}")

        click.secho("\nAvailable UI components:", fg="yellow")
        components = list(ui)
        click.echo(f"Total components: {len(components)}")

        for component in sorted(components):
            comp_func = getattr(ui, component)
            # Try to get the source or signature information
            try:
                import inspect

                sig = inspect.signature(comp_func)
                click.echo(f"  {component}{sig}")
            except:
                click.echo(f"  {component}")

        # Check for templates directory and list template files
        templates_path = os.path.join(info.path, "templates")
        if os.path.exists(templates_path):
            click.secho("\nTemplate files:", fg="yellow")
            for root, _dirs, files in os.walk(templates_path):
                for file in files:
                    if file.endswith((".html", ".htm", ".xml")):
                        rel_path = os.path.relpath(os.path.join(root, file), info.path)
                        click.echo(f"  {rel_path}")

    except KeyError:
        click.echo(click.style(f"Error: Theme '{theme_name}' not found", fg="red"))
        click.echo("Available themes:")
        themes = lib_theme.collect_themes()
        for name in themes:
            click.echo(f"  - {name}")


@theme.command("verify")
@click.argument("theme_name", required=False)
@click.pass_context
def verify_theme(ctx: click.Context, theme_name: str | None):
    """Verify that a theme implements all required UI macros."""
    if theme_name is None:
        theme_name = cast(str, config["ckan.ui.theme"])

    try:
        info = lib_theme.get_theme(theme_name)
        ui = info.build_ui(ctx.obj.app._wsgi_app)

        click.secho(f"Verifying theme: {theme_name}", fg="green")

        # Get all components from this theme
        theme_components = set(ui)

        # Get all components from base themes to compare against
        all_themes = lib_theme.collect_themes()
        base_theme = "bare"  # Use bare as the reference base theme
        if base_theme in all_themes:
            base_ui = all_themes[base_theme].build_ui(ctx.obj.app._wsgi_app)
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
            click.echo(click.style("  Status: FAILED - Some required components are missing", fg="red"))
            return 1
        click.echo(click.style("  Status: PASSED - All required components implemented", fg="green"))
        return 0

    except KeyError:
        click.echo(click.style(f"Error: Theme '{theme_name}' not found", fg="red"))
        return 1


@theme.command("check")
@click.argument("theme_name", required=False)
def check_theme(theme_name: str | None):
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
        essential_templates = ["base.html", "page.html", "_header.html", "_footer.html", "macros/ui.html"]

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
