from __future__ import annotations

import logging
import os
from typing import Any

from flask import current_app
from typing_extensions import override
from werkzeug.local import LocalProxy

import ckan.plugins.toolkit as tk
from ckan import plugins as p
from ckan import types

from .interfaces import ITheme
from .lib import UI, Theme, get_theme, switch_theme

log = logging.getLogger(__name__)


@tk.blanket.cli
@tk.blanket.config_declarations
class ThemingPlugin(ITheme, p.IConfigurer, p.IMiddleware, p.SingletonPlugin):
    @override
    def update_config(self, config: Any):
        if config["ckan.ui.theme"]:
            switch_theme(config["ckan.ui.theme"], config)
        UIManager.reset()

    @override
    def register_themes(self) -> dict[str, Theme]:
        root = os.path.dirname(os.path.abspath(__file__))
        return {
            "bare": Theme(os.path.join(root, "themes/bare")),
            "bulma": Theme(os.path.join(root, "themes/bulma"), parent="bare"),
            "tailwind": Theme(os.path.join(root, "themes/tailwind"), parent="bare"),
            "bs5": Theme(os.path.join(root, "themes/bs5"), parent="bare"),
            "pico": Theme(os.path.join(root, "themes/pico"), parent="bare"),
        }

    @override
    def make_middleware(self, app: types.CKANApp, config: Any) -> types.CKANApp:
        app.jinja_env.add_extension("jinja2.ext.debug")

        app.jinja_env.globals.update({"ui": ui})
        return app


class UIManager:
    ui: UI | None = None

    @classmethod
    def get(cls):
        """Get the current UI instance. Creates one if it doesn't exist."""
        if cls.ui is None:
            cls.set(tk.config["ckan.ui.theme"])

        return cls.ui

    @classmethod
    def set(cls, theme: str):
        """Set the UI instance to a new theme."""
        cls.ui = get_theme(theme).build_ui(current_app)

    @classmethod
    def reset(cls):
        """Reset the UI instance to None."""
        cls.ui = None


ui = LocalProxy(UIManager.get)
