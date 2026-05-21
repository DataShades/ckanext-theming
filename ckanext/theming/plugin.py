from __future__ import annotations

import logging
from typing import Any

from typing_extensions import override

import ckan.plugins.toolkit as tk
from ckan import plugins as p
from ckan import types

from ckanext.theming.themes import make_bare_theme

from . import make_middleware, register_themes, update_config
from .interfaces import ITheme

log = logging.getLogger(__name__)


@tk.blanket.cli
@tk.blanket.config_declarations
class ThemingPlugin(ITheme, p.IConfigurer, p.IMiddleware, p.SingletonPlugin):
    @override
    def update_config(self, config: Any):
        update_config(config)

    @override
    def register_themes(self):
        return register_themes() + [make_bare_theme()]

    @override
    def make_middleware(self, app: types.CKANApp, config: Any) -> types.CKANApp:
        make_middleware(app, config)
        return app
