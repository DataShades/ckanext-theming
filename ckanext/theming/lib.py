"""Theme and UI classes for CKAN theming system.

A theme is a directory containing templates and static files, and
optionally extending a parent theme. A UI provides access to a set of
functions that can be used in templates for building the user interface.

Themes can be registered by CKAN plugins using the ITheme interface.

Example usage::

    theme = get_theme(config["ckan.ui.theme"])
    ui = theme.build_ui(app)
    btn = ui.link("Click me!", href="https://ckan.org")
"""

from __future__ import annotations

import abc
import logging
import os
from collections.abc import Iterable, Iterator
from typing import Any, Protocol, cast

from jinja2.runtime import Macro
from markupsafe import Markup
from typing_extensions import override

import ckan
import ckan.plugins as p
from ckan import types
from ckan.common import config
from ckan.exceptions import CkanConfigurationException
from ckan.lib.helpers import helper_functions as h

from .interfaces import ITheme

log = logging.getLogger(__name__)


class PElement(Protocol):
    def __call__(self, *args: Any, **kwargs: Any) -> Markup: ...


class Util:
    ui: UI

    def __init__(self, ui: UI):
        self.ui = ui

    def attrs(self, kwargs: dict[str, Any]):
        """Helper method to render HTML attributes from a dictionary."""
        parts = []

        groups = [
            ("aria", "aria-"),
            ("data", "data-"),
            ("attrs", ""),
        ]

        for key, prefix in groups:
            if key in kwargs:
                parts.append(" ".join(f'{prefix}{k}="{v}"' for k, v in kwargs[key].items()))

        return h.literal(" ".join(parts))

    def call(self, el: PElement, /, *args: Any, caller: Macro, **kwargs: Any) -> Markup:
        """Call an inline element as a block element.

        Allows passing complex content into an element using a Jinja2
        caller. For example, following simple macro does not contain `caller()`::

            {% macro button(content) %}
                <button>{{ content }}</button>
            {% endmacro %}

        As result, it cannot be called in form `{% call ui.button() %}` and
        rendering button with nested HTML turns into a verbose task. But using
        `ui.util.call`, `button` can be used with `call`::

            {% call ui.util.call(ui.button) %}
                <i class="icon"/>
                Click!
            {% endcall %}

        The content of the `call` block will be passed as a first argument into
        the target macro. Any other positional and named arguments of the
        `ui.util.call` will be redirected into `ui.button` as well.
        """
        return el(caller(), *args, **kwargs)

    def merge(self, *fragments: Markup) -> Markup:
        """Merge multiple Markup fragments into a single Markup object."""
        return Markup().join(fragments)


class UI(Iterable[str], abc.ABC):
    """Abstract base class for theme UIs.

    A UI provides access to a set of macros that can be used in templates.
    """

    Util: type[Util] = Util
    util: Util

    def __init__(self, app: types.CKANApp):
        """Initialize the UI with the CKAN application instance.

        :param app: The CKAN application instance.
        """
        self.util = self.Util(self)

    @override
    @abc.abstractmethod
    def __iter__(self) -> Iterator[str]:
        """Return an iterable of element names provided by this UI.

        :return: An iterable of element names.
        """

    @abc.abstractmethod
    def __getattr__(self, name: str) -> PElement:
        """Get an element factory by name.

        :param name: The name of the element.
        :return: A callable that produces the element.
        """


class MacroUI(UI):
    """A UI implementation that loads macros from a Jinja2 template.

    The template should define macros for each UI element. The default template
    is "macros/ui.html".

    :param source: The path to the Jinja2 template containing the macros.
    """

    source: str = "macros/ui.html"

    @override
    def __init__(self, app: types.CKANApp):
        super().__init__(app)
        self.__env = app.jinja_env
        self.__tpl = app.jinja_env.get_template(self.source)

    @override
    def __getattr__(self, name: str):
        if config["debug"]:
            tpl = self.__env.get_template(self.source)
            mod = tpl.make_module()
        else:
            mod = self.__tpl.module
        el: PElement = getattr(mod, name)
        return el

    @override
    def __iter__(self) -> Iterator[str]:
        for name in dir(self.__tpl.module):
            if name.startswith("_"):
                continue
            yield name


class Theme:
    """Information about a theme.

    :param path: Path to the theme directory.
    :param extends: Name of the parent theme, or None.
    """

    path: str
    extends: str | None

    UI: type[UI] = MacroUI
    _ui: UI | None = None

    def __init__(self, path: str, extends: str | None = None):
        self.path = path
        self.extends = extends

    def build_ui(self, app: types.CKANApp) -> UI:
        """Build a UI instance for this theme.

        The default implementation returns a MacroUI instance that loads
        macros from "macros/ui.html" in the theme's template directory.

        :param app: The CKAN application instance.
        :return: A UI instance.
        """
        self._ui = self.UI(app)
        return self._ui


def get_theme(name: str):
    """Get theme by name.

    :raises KeyError: if theme not found
    """
    themes = collect_themes()
    return themes[name]


def collect_themes():
    """Collect available themes from core and plugins."""
    ckan_root = os.path.dirname(os.path.abspath(ckan.__file__))
    themes = {
        "classic": Theme(os.path.join(ckan_root, "templates")),
        "midnight-blue": Theme(os.path.join(ckan_root, "templates-midnight-blue")),
    }
    for plugin in p.PluginImplementations(ITheme):
        themes.update(plugin.register_themes())

    return themes


def resolve_paths(theme: str | None) -> list[str]:
    """Resolve theme paths including parent themes.

    :raises KeyError: if the parent theme is not found
    """
    themes = collect_themes()
    paths: list[str] = []
    while theme:
        info = themes[theme]
        paths.append(info.path)
        theme = info.extends

    return paths[::-1]


def switch_theme(name: str, config: Any):
    try:
        template_paths = resolve_paths(name)
    except KeyError as e:
        missing_theme: str = e.args[0]
        if missing_theme == name:
            msg = f"The configured theme '{name}' is not recognised."

        else:
            msg = f"The configured theme '{name}'" + f" extends unknown theme '{missing_theme}'."

        raise CkanConfigurationException(msg) from e

    log.info("Re-loading templates from %s", template_paths)

    if "plugin_template_paths" in config:
        template_paths = cast(list[str], config["plugin_template_paths"]) + template_paths

    if extra_template_paths := cast(str, config["extra_template_paths"]):
        # must be first for them to override defaults
        template_paths = extra_template_paths.split(",") + template_paths

    config["computed_template_paths"] = template_paths
