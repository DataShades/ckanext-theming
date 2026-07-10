# Integrating with ckanext-theming

Standardizing your templates around the `ui.*` components is highly
recommended, but portal maintainers using your extension might not have
`ckanext-theming` explicitly enabled or configured.

To ensure your extension works out-of-the-box in all environments, you can use
the **`ThemingMixin`** approach. This allows your extension to adopt standard
`ui` components while remaining fully functional whether `ckanext-theming` is
enabled or not.

---

## How It Works

The `ThemingMixin` is a helper class designed to provide automatic, zero-config fallbacks for extensions:

1. **When `ckanext-theming` is enabled**: The mixin acts as a simple `no-op`. The active theme handles all standard component rendering.
2. **When `ckanext-theming` is NOT enabled**:
    * The mixin dynamically designates one of its descendant plugins (the latest loaded in the plugin list to maintain correct template inheritance priority) to act as the theme bootstrapper.
    * It registers polyfill themes that map standard `ui.*` elements directly
      to CKAN's native snippets and core macros (for example, `ui.package`
      delegates to `snippets/package_item.html`, and `ui.input` delegates to
      CKAN's core `form.input` macro).
    * It injects the `ui` helper variable into templates automatically.

This ensures that template components "just work" even on portals running a classic, unconfigured CKAN setup.

---

## Implementing the Mixin

Add `ckanext-theming` to your extension's requirements (e.g., in `setup.py`, `pyproject.toml`, or `requirements.txt`) with a minimal version restriction:

```toml title="pyproject.toml"
dependencies = ["ckanext-theming>=0.0.4"]
```

Import `ThemingMixin` and place it **first** in your plugin's class hierarchy inheritance chain:

```python title="ckanext/my_extension/plugin.py"

import ckan.plugins as p
from ckanext.theming.plugin import ThemingMixin

class MyPlugin(ThemingMixin, p.SingletonPlugin):
    # Your plugin code goes here
    pass
```


/// admonition | Mandatory `super()` Calls
    type: danger

Because `ThemingMixin` implements `ITheme`, `p.IConfigurer`, and
`p.IMiddleware` internally to bootstrap the polyfill fallback environment,
**you must call `super()`** inside methods of these interfaces if your plugin
overrides them.

If you omit the `super()` calls, the bootstrap mechanism will be bypassed, and
your templates will raise errors on portals where `ckanext-theming` is not
explicitly enabled.

Namely, the following methods are used by mixin and require `super()` call:

* `ITheme.register_themes`
* `ITheme.get_default_theme_ui_sources`
* `IConfigurer.update_config`
* `IMiddleware.make_middleware`

///

Ensure your overrides call their parents as shown below:

```python
from typing import Any
import typing_extensions import override

from ckan import types
from ckanext.theming import lib
from ckanext.theming.plugin import ThemingMixin
from ckanext.theming.interfaces import ITheme

class MyPlugin(ThemingMixin, ITheme, p.IConfigurer, p.IMiddleware, p.SingletonPlugin):

    @override
    def update_config(self, config: Any) -> None:
        # 1. Call super first to let ThemingMixin update configurations
        super().update_config(config)

        # 2. Add your extension's custom configs
        p.toolkit.add_template_directory(config, "templates")

    @override
    def register_themes(self) -> list[lib.Theme]:
        # 1. Collect themes registered by theming mixin
        themes = super().register_themes()

        # 2. Add your own theme registration
        # themes.append(...)
        return themes

    @override
    def make_middleware(self, app: types.CKANApp, config: Any) -> types.CKANApp:
        # 1. Pass down middleware pipeline creation
        app = super().make_middleware(app, config)

        # 2. Wrap app with your custom middleware
        ...

        # 3. Do not forget to return the original app
        return app
```

/// note

If you are not using `ui.*` components in templates and instead just defining
them for other extensions via `get_default_theme_ui_sources`, you can go even
further and handle scenario, where `ckanext-theming` is not installed at all.

If `ThemingMixin` cannot be imported (ckanext-theming is not installed),
replace it with plain `object` class, to allow inheritance.

```python
# ckanext/my_extension/plugin.py
import ckan.plugins as p
try:
    from ckanext.theming.plugin import ThemingMixin
except ImportError:
    ThemingMixin = object

class MyPlugin(ThemingMixin, p.SingletonPlugin):

    # Implementation of ITheme.get_default_theme_ui_sources. If theming is installed,
    # the following method will register additional UI macros. Otherwise, it will never
    # be called.
    def get_default_theme_ui_sources(self):
        sources = super().get_default_theme_ui_sources()
        return sources + ["my_extension/default_ui.html"]
```

///


---

## Constraints & Compatibility

This mixin pattern relies on interface inheritance behavior introduced in
**CKAN >= 2.11**. If your extension must support older legacy versions of CKAN,
the automatic fallback polyfill will not work.

The fallback polyfill themes are designed purely to prevent rendering errors on
non-theming portals by delegating to classic CKAN HTML snippets. When using
`ThemingMixin` you can safely call `ui.*` inside templates, but that's the
only feature of the theming plugin that is enabled by mixin. CLI commands or
component explorer will not be available.
