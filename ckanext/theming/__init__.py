from __future__ import annotations

import logging
from typing import Any, cast

import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckan import types

from . import config as cfg
from .interfaces import ITheme
from .lib import collect_themes, enable_theme, ui
from .themes import make_classic_polyfill, make_mb_polyfill

log = logging.getLogger(__name__)


__all__ = ["register_themes", "update_config", "make_middleware", "ThemingMixin"]


def register_themes():
    return [make_classic_polyfill(), make_mb_polyfill()]


def update_config(config_: Any):
    collect_themes()
    theme = cfg.theme()
    if not theme:
        if tk.config.get("ckan.base_templates_folder") == "templates-midnight-blue":
            theme = "midnight-blue-polyfill"
        else:
            theme = "classic-polyfill"

    if theme:
        enable_theme(theme, config_)


def default_ui_sources() -> list[str]:
    return ["macros/theming_default_ui.html"]


def make_middleware(app: types.CKANApp, config_: Any) -> types.CKANApp:  # pyright: ignore[reportUnusedParameter]
    if hasattr(app, "jinja_env"):
        app.jinja_env.add_extension("jinja2.ext.debug")
        app.jinja_env.globals.update({"ui": cast(Any, ui)})
    else:
        log.warning("Cannot initialize UI in the non-flask application")
    return app


class ThemingMixin:
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IMiddleware, inherit=True)
    p.implements(ITheme, inherit=True)

    def update_config(self, config_: Any):
        tk.add_template_directory(config_, "templates")

        if "theming" not in config_["ckan.plugins"]:
            update_config(config_)

    def register_themes(self):
        return register_themes()

    def get_default_theme_ui_sources(self) -> list[str]:
        return default_ui_sources()

    def make_middleware(self, app: types.CKANApp, config_: Any) -> types.CKANApp:
        if "theming" not in config_["ckan.plugins"]:
            make_middleware(app, config_)
        return app
