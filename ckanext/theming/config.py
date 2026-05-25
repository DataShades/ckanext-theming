from __future__ import annotations

import ckan.plugins.toolkit as tk

THEME = "ckan.ui.theme"
ENABLE_VIEWS = "ckan.ui.enable_theming_views"


def theme() -> str:
    """Returns the name of the active theme, or empty string if no theme is active."""
    return tk.config[THEME] or ""


def enable_views() -> bool:
    """Returns True if the theming views are enabled, False otherwise."""
    return tk.config[ENABLE_VIEWS]
