from __future__ import annotations

import logging
from typing import cast

import click

from ckan.cli import error_shout
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
        parent = info.extends
        while parent:
            if parent_info := themes.get(parent):
                lineage.append(parent)
                parent = parent_info.extends
            else:
                lineage.append(click.style(parent, fg="red"))

        if lineage:
            click.secho(f"\tExtends: {' -> '.join(lineage)}")


@theme.command("components")
@click.pass_context
def list_components(ctx: click.Context):
    """List available components."""
    theme = cast(str, config["ckan.ui.theme"])
    info = lib_theme.get_theme(theme)

    ui = info.build_ui(ctx.obj.app._wsgi_app)

    for item in ui:
        click.echo(f"\t{item}: {getattr(ui, item)}")
