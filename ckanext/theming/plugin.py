from __future__ import annotations

import logging
from typing import Any

from typing_extensions import override

import ckan.plugins.toolkit as tk
from ckan import plugins as p
from ckan import types

from ckanext.theming.themes.bare.theme import make_theme

from .interfaces import ITheme
from .lib import Theme, enable_theme, ui

log = logging.getLogger(__name__)


@tk.blanket.cli
@tk.blanket.config_declarations
class ThemingPlugin(ITheme, p.IConfigurer, p.IMiddleware, p.SingletonPlugin):
    @override
    def update_config(self, config: Any):
        if config["testing"]:
            tk.add_template_directory(config, "templates")

        if config["ckan.ui.theme"]:
            enable_theme(config["ckan.ui.theme"], config)

    @override
    def register_themes(self) -> list[Theme]:
        return [make_theme()]

    @override
    def make_middleware(self, app: types.CKANApp, config: Any) -> types.CKANApp:
        if hasattr(app, "jinja_env"):
            app.jinja_env.add_extension("jinja2.ext.debug")
            app.jinja_env.globals.update({"ui": ui})
        else:
            log.warning("Cannot initialize UI in the non-flask application")
        return app
