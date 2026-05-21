from __future__ import annotations

import logging
from typing import Any, cast

import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckan import types

from .interfaces import ITheme
from .lib import collect_themes, enable_theme, ui
from .themes import make_classic_polyfill, make_mb_polyfill

log = logging.getLogger(__name__)


__all__ = ["register_themes", "update_config", "make_middleware", "ThemingMixin"]


def register_themes():
    return [make_classic_polyfill(), make_mb_polyfill()]


def update_config(config: Any):
    if config["testing"]:
        tk.add_template_directory(config, "tests/templates")

    collect_themes()
    if theme := config.get("ckan.ui.theme"):
        enable_theme(theme, config)


def make_middleware(app: types.CKANApp, config: Any) -> types.CKANApp:  # pyright: ignore[reportUnusedParameter]
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

    def update_config(self, config: Any):
        if "theming" not in config["ckan.plugins"]:
            update_config(config)

    def register_themes(self):
        return register_themes()

    def make_middleware(self, app: types.CKANApp, config: Any) -> types.CKANApp:
        if "theming" not in config["ckan.plugins"]:
            make_middleware(app, config)
        return app
