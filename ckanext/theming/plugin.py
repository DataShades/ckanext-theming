from __future__ import annotations

import logging
from typing import Any

from flask import Blueprint
from typing_extensions import override

import ckan.plugins.toolkit as tk
from ckan import plugins as p
from ckan import types

from ckanext.theming.themes import make_bare_theme

from . import config as cfg
from . import default_ui_sources, make_middleware, register_themes, update_config, views
from .interfaces import ITheme

log = logging.getLogger(__name__)


@tk.blanket.cli
@tk.blanket.config_declarations
class ThemingPlugin(ITheme, p.IConfigurer, p.IMiddleware, p.IBlueprint, p.SingletonPlugin):
    @override
    def update_config(self, config: Any):
        update_config(config)

        if config["testing"]:
            tk.add_template_directory(config, "tests/templates")

    @override
    def register_themes(self):
        return register_themes() + [make_bare_theme()]

    @override
    def get_default_theme_ui_sources(self) -> list[str]:
        return default_ui_sources()

    @override
    def make_middleware(self, app: types.CKANApp, config: Any) -> types.CKANApp:
        make_middleware(app, config)
        return app

    @override
    def get_blueprint(self) -> list[Blueprint]:
        if cfg.enable_views():
            return [views.bp]
        return []
