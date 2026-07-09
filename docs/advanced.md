# Advanced Development

This page covers advanced hooks and techniques for extension developers who
want to integrate deeply with the theming system.

## The `ITheme` Interface

Extensions can interact with the theming system by implementing the `ITheme`
interface.

### Providing Default Implementations
If your extension provides a new UI component that should have a generic
fallback implementation, use `get_default_theme_ui_sources`.

```python
def get_default_theme_ui_sources(self) -> list[str]:
    return ["macros/my_extension_defaults.html"]
```

**Lower Priority**: Macros in these files will be used only if the active
theme does **not** define a macro with the same name.

**Use Case**: Providing basic markup for a new widget that a theme can
  optionally style later.

### Providing Additional Components
To provide components that should **not** be overridden by themes, use
`get_additional_theme_ui_sources`.

```python
def get_additional_theme_ui_sources(self) -> list[str]:
    return ["macros/my_extension_widgets.html"]
```

**Higher Priority**: Macros in these files take precedence over theme
  implementations.

**Use Case**: Complex logic-heavy widgets where the HTML structure is
  critical for the extension's functionality.

### Patching the UI Object
For absolute control, you can use `patch_theme_ui` to dynamically add or
modify components on the `ui` object.

```python
def patch_theme_ui(self, theme, ui):
    # Dynamically add a simple component
    ui._add_component("timestamp", lambda: ui.util.now().isoformat())
```

---

## Advanced Theme Definition

When registering a `Theme` class, you can customize several advanced parameters
to adapt it to your workflow or frontend build chain.

### Customizing Theme Directory Structure

By default, the `Theme` class looks for assets, public files, and templates in
standard folder locations. If your project has a different structure (for
example, if you compile frontend code with Vite, Webpack, or similar bundlers
into a `dist` or `build` directory), you can override these folder locations:

* **`template_folder`** (defaults to `"templates"`): Directory containing theme templates and macros.
* **`public_folder`** (defaults to `"public"`): Directory for static public files served directly.
* **`asset_folder`** (defaults to `"assets"`): Directory containing css/js source and compiled webassets.

```python
from ckanext.theming.lib import Theme

theme = Theme(
    name="my_compiled_theme",
    path=path,
    # Custom subdirectories relative to the theme path
    template_folder="src/templates",
    public_folder="dist/static",
    asset_folder="src/assets",
)
```

---

## Icon Abstraction and Mapping

To ensure that different themes can swap icon libraries (e.g., FontAwesome,
Material Icons, or custom SVG assets) without breaking template logic, the
theming extension provides an icon mapping abstraction.

### Specifying Icon Maps

The `Theme` class accepts an `icon_map` dictionary that translates generic icon identifier requests (such as `"home"`, `"trash"`, `"edit"`) to theme-specific names:

```python
theme = Theme(
    name="my_custom_theme",
    path=path,
    icon_map={
        "home": "house-outline",
        "trash": "delete-forever",
        "edit": "pencil-square",
        "search": "magnifying-glass",
    }
)
```

### Resolving Icons in Templates

Inside your templates, call `ui.icon(name)` (which delegates to `ui.util.icon(name)`) to fetch the mapped icon identifier.

* If the active theme defines a mapping in `icon_map`, it returns the mapped value.
* If not, the system recursively checks parent themes up the inheritance chain.
* If no theme in the chain defines a mapping, it falls back to returning the original `name` parameter.

```html
<!-- Renders the icon mapped to "trash" -->
{{ ui.icon("trash") }}
```

Typically, you define a custom `icon` macro in your theme's `macros/ui.html` which wraps the mapped name in your chosen icon library markup:

```html
{%- macro icon(name) -%}
    <!-- Example using FontAwesome -->
    <i class="fa fa-{{ ui.util.icon(name) }}" aria-hidden="true"></i>
{%- endmacro %}
```

---

## Extending the Utility Library

The theming system attaches a utility helper library to `ui.util` in
templates. You can extend or customize these utilities for a specific theme by
providing a custom `util_factory`.

### Extending Util via `util_factory`

To add custom utilities:
1. Subclass the default `Util` (or `BaseUtil`) class.
2. Define your helper methods.
3. Pass your custom class as the `util_factory` to the `Theme` definition.

```python
from ckanext.theming.lib import Util, Theme

class CustomThemeUtil(Util):
    def format_bytes(self, size_in_bytes: int) -> str:
        """Custom helper to format file sizes."""
        for unit in ["B", "KB", "MB", "GB"]:
            if size_in_bytes < 1024:
                return f"{size_in_bytes:.1f} {unit}"
            size_in_bytes /= 1024
        return f"{size_in_bytes:.1f} TB"

    def icon(self, name: str) -> str:
        """Optionally override default icon mapping logic."""
        if name == "special-action":
            return "star-filled"
        return super().icon(name)

# Register the theme with your custom util factory
theme = Theme(
    name="my_custom_theme",
    path=path,
    util_factory=CustomThemeUtil,
)
```

### Accessing Custom Utilities in Templates

In your Jinja templates, you can call these custom helpers directly from `ui.util`:

```html
<p>File Size: {{ ui.util.format_bytes(resource.size) }}</p>
```

---

## Customizing the UI Registration Factory

By default, the `Theme` class uses `MacroUI` to locate and load element macros
from your template files. If you need complete control over how UI elements are
collected or if you want to register programmatically-generated elements, you
can provide a custom `ui_factory`.

### Extending UI via `ui_factory`

To define a custom UI factory:

1. Subclass `MacroUI` (or the base `UI` class).
2. Override `__init__` or other methods to register your custom callable components via `_add_component`.
3. Pass your factory to the `Theme` definition.

```python
from ckanext.theming.lib import MacroUI, Theme

class CustomUIFactory(MacroUI):
    def __init__(self, app, theme, util):
        super().__init__(app, theme, util)

        # Register a programmatically-generated component
        self._add_component(
            "render_banner",
            lambda text, style="info": f'<div class="banner banner-{style}">{text}</div>'
        )

theme = Theme(
    name="my_custom_theme",
    path=path,
    ui_factory=CustomUIFactory,
)
```

You can then call the programmatically added component in your templates:

```html
{{ ui.render_banner("Welcome to the new portal!", style="warning") }}
```

---

## Component Categories

In `components.yaml` (and when using CLI tools), components are grouped into
categories. Understanding these helps you prioritize your implementation:

- **Essential**: Fundamental to CKAN's operation and for extensions.
- **Recommended**: Highly recommended for a complete user experience (e.g.,
  `header`, `footer`). These components are not often used in extensions.
- **Experimental**: New or unstable components that might change in future
  versions.
- **Plugin**: Components provided by other extensions (like
  `ckanext-scheming`).
- **Custom**: Theme-specific components that aren't part of the standard
  library.
