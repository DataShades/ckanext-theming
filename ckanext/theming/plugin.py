from __future__ import annotations

import logging
import os
from typing import Any

from typing_extensions import override

import ckan.plugins.toolkit as tk
from ckan import plugins as p
from ckan import types

from . import reference
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
        root = os.path.dirname(os.path.abspath(__file__))
        return [
            Theme("bare", os.path.join(root, "themes/bare"), icon_map=reference.bare_icons),
        ]

    @override
    def make_middleware(self, app: types.CKANApp, config: Any) -> types.CKANApp:
        app.jinja_env.add_extension("jinja2.ext.debug")

        app.jinja_env.globals.update({"ui": ui})
        return app
