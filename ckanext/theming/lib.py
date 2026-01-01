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
import dataclasses
import datetime
import logging
import os
import uuid
from collections import defaultdict
from collections.abc import Iterable, Iterator
from typing import Any, Protocol

from flask import current_app
from jinja2.runtime import Macro
from markupsafe import Markup
from typing_extensions import override
from werkzeug.local import LocalProxy

import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckan import types
from ckan.common import config
from ckan.exceptions import CkanConfigurationException
from ckan.lib.helpers import helper_functions as h

from .interfaces import ITheme

log = logging.getLogger(__name__)

NAMESPACE_UI = uuid.uuid4()


class PElement(Protocol):
    def __call__(self, *args: Any, **kwargs: Any) -> Markup: ...


class Util:
    ui: UI
    _storage_key = "ui_storage"

    def __init__(self, ui: UI):
        self.ui = ui

    def attrs(self, kwargs: dict[str, Any]):
        """Helper method to render HTML attributes from a dictionary."""
        parts = []

        groups = [
            ("aria", "aria-"),
            ("data", "data-"),
            ("on", "on"),
            ("hx", "hx-"),
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

    def map(self, el: PElement, items: Iterable[Any], /, *args: Any, **kwargs: Any) -> Markup:
        """Map an element over a collection of items.

        Renders the specified element for each item in the collection and
        concatenates the results.

        :param el: The element to render for each item.
        :param items: The collection of items.
        :param args: Positional arguments to pass to the element.
        :param kwargs: Named arguments to pass to the element.
        :return: A Markup object containing the concatenated results.
        """
        return Markup().join(el(item, *args, **kwargs) for item in items)

    def now(self, tz: datetime.timezone = datetime.timezone.utc):
        """Get the current UTC datetime.

        :param tz: Timezone for the returned datetime. Defaults to UTC.
        :return: Current datetime with the specified timezone.
        """
        return datetime.datetime.now(tz)

    def id(self, value: str | None = None, prefix: str = "id-"):
        """Generate a unique identifier.

        If `value` is provided, a UUID5 based on the value is generated,
        otherwise a random UUID4 is generated.

        Useful for generating unique HTML element IDs.

        :param value: Optional value to base the UUID5 on.
        :param prefix: Prefix to prepend to the identifier.
        :return: An identifier string.
        """
        result = uuid.uuid5(NAMESPACE_UI, value) if value else uuid.uuid4()
        return f"{prefix}{result.hex}"

    def keep_item(self, category: str, key: str, value: Any):
        """Keep an item in the UI storage under the specified category.

        This method allows storing arbitrary items in a per-request storage
        associated with the UI. Items can be retrieved later during the same
        request.

        :param category: The category under which to store the item.
        :param key: The key for the item.
        :param value: The item to store.
        """
        storage = tk.g.setdefault(self._storage_key, defaultdict(dict))
        storage[category][key] = value

    def pop_items(self, category: str, key: str | None = None, default: Any = None) -> dict[str, Any] | Any:
        """Pop items from the UI storage under the specified category.

        :param category: The category from which to pop items.
        :param key: Optional key of the item to pop. If not provided, all items
                    under the category are popped.
        :param default: Default value to return if the key is not found.
        :return: The popped item(s) from the UI storage.
        """
        storage = tk.g.setdefault(self._storage_key, defaultdict(dict))
        return storage[category].pop(key, default) if key else storage.pop(category)

    def get_items(self, category: str, key: str | None = None, default: Any = None) -> dict[str, Any] | Any:
        """Get all items stored under the specified category in the UI storage.

        :param category: The category from which to get items.
        :param key: Optional key of the item to get. If not provided, all items
                    under the category are returned.
        :param default: Default value to return if the key is not found.
        :return: The requested item(s) from the UI storage.
        """
        storage = tk.g.setdefault(self._storage_key, defaultdict(dict))
        return storage[category].get(key, default) if key else storage[category]

    def icon(self, name: str) -> str:
        """Normalize icon name.

        Maps common icon names to their corresponding names in the theme's icon
        set. If no mapping exists, returns the original name. This allows using
        consistent icon names across different themes. For example, "search" is
        mapped to "magnifying-glass" if the theme does not have icon with ID
        `search`. Themes can override these mappings as needed.

        # TODO: Make this configurable per theme.

        :param name: Common name of the icon.
        :return: The name of the corresponding icon provided by theme

        """
        icon_map = {
            "search": "magnifying-glass",
            "edit": "pencil",
            "delete": "trash",
            "add": "plus-circle",
            "info": "info-circle",
            "warning": "exclamation-triangle",
            "user": "user-circle",
        }
        return icon_map.get(name, name)


class UI(Iterable[str], abc.ABC):
    """Abstract base class for theme UIs.

    A UI provides access to a set of macros that can be used in templates.
    """

    Util: type[Util] = Util
    util: Util
    inv: dict[str, PElement]

    def __init__(self, app: types.CKANApp):
        """Initialize the UI with the CKAN application instance.

        :param app: The CKAN application instance.
        """
        self.inv = {}
        self.util = self.Util(self)

    @override
    def __iter__(self) -> Iterator[str]:
        """Return an iterable of element names provided by this UI.

        :return: An iterable of element names.
        """
        return iter(self.inv)

    def __getattr__(self, name: str) -> PElement:
        """Get an element factory by name.

        :param name: The name of the element.
        :return: A callable that produces the element.
        """
        if name not in self.inv:
            raise AttributeError(name)

        return self.inv[name]


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
        self._fill_inventory()

    def _fill_inventory(self):
        mod = self.__tpl.module
        self.inv: dict[str, PElement] = {name: getattr(mod, name) for name in dir(mod) if not name.startswith("_")}

    @override
    def __getattr__(self, name: str):
        # reset macro cache at the beginning of the request in debug mode. This
        # allows to edit UI macros without restarting the server.
        if config["debug"] and not getattr(tk.g, "_ui_compiled", False):
            self.__tpl._module = self.__tpl.make_module()
            tk.g._ui_compiled = True
            self._fill_inventory()

        return super().__getattr__(name)


@dataclasses.dataclass
class Theme:
    """Information about a theme.

    :param path: Path to the theme directory.
    :param parent: Name of the parent theme, or None.
    """

    path: str
    parent: str | None = None

    ui_factory: type[UI] = MacroUI

    def build_ui(self, app: types.CKANApp) -> UI:
        """Build a UI instance for this theme.

        :param app: The CKAN application instance.
        :return: A UI instance.
        """
        return self.ui_factory(app)

    def template_path(self):
        """Get the path to the theme's templates directory."""
        return os.path.join(self.path, "templates")

    def public_path(self):
        """Get the path to the theme's public directory."""
        return os.path.join(self.path, "public")

    def asset_path(self):
        """Get the path to the theme's assets directory."""
        return os.path.join(self.path, "assets")


def get_theme(name: str):
    """Get theme by name.

    :raises KeyError: if theme not found
    """
    themes = collect_themes()
    return themes[name]


def collect_themes() -> dict[str, Theme]:
    """Collect available themes from core and plugins."""
    # ckan_root = os.path.dirname(os.path.abspath(ckan.__file__))
    themes: dict[str, Theme] = {
        # "classic": Theme(os.path.join(ckan_root, "templates")),
        # "midnight-blue": Theme(os.path.join(ckan_root, "templates-midnight-blue")),
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
        theme = info.parent

    return paths


def enable_theme(name: str, config: Any):
    """Enable the specified theme.

    This function updates the CKAN configuration to include template and
    static file directories from the specified theme and its parent themes.

    :param name: The name of the theme to switch to.
    :param config: The CKAN configuration dictionary.
    :raises CkanConfigurationException: if the theme or its parent is not found

    """
    themes = collect_themes()

    next_name = name
    enabled_themes = {next_name}
    here = os.path.dirname(__file__)

    while theme := themes.get(next_name):
        if os.path.isdir(theme.template_path()):
            tk.add_template_directory(config, os.path.relpath(theme.template_path(), here))

        if os.path.isdir(theme.asset_path()):
            tk.add_resource(os.path.relpath(theme.asset_path(), here), f"theming/{next_name}")

        if os.path.isdir(theme.public_path()):
            tk.add_public_directory(config, os.path.relpath(theme.public_path(), here))

        next_name = theme.parent
        if not next_name:
            break

        if next_name in enabled_themes:
            log.warning("Theme %s causes a recursion in theme hierarchy", next_name)
            break

        enabled_themes.add(next_name)

    else:
        msg = f"Theme '{next_name}' is not recognised."
        raise CkanConfigurationException(msg)

    UIManager.reset()


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
