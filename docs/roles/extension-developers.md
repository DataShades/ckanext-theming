# Extension Developers Guide

As an **Extension Developer**, your goal is to build feature-rich plugins that integrate seamlessly with whatever theme a portal maintainer chooses. This guide explains how to leverage standardized components, register custom components securely, and handle theme-specific styling without breaking other layouts.


## Core Development Goals

**Theme Portability**: Do not write raw HTML with framework-specific classes
(e.g. Bootstrap's `btn btn-primary` or Tailwind's `bg-blue-500`).

**Semantic Calls**: Always call standard `ui.*` component macros (e.g., `{{
ui.button(...) }}`) in your extension templates.

**Graceful Fallbacks**: Ensure that if a portal uses an abstract or custom
theme that doesn't natively support your extension, the layout does not break.


## Registering Custom Components

Sometimes your extension needs to introduce a brand-new UI component that is not part of CKAN's standard list (for example, a `harvester_status` box or a `map_viewer`).

### The Method: Registering via Default Components Hook
You should implement the `ITheme` interface in your extension's plugin class and register your custom component files using `get_default_theme_ui_sources()`:

```python
# ckanext/my_extension/plugin.py
import ckan.plugins as p
from ckanext.theming.interfaces import ITheme

class MyExtensionPlugin(p.SingletonPlugin, ITheme):

    def get_default_theme_ui_sources(self) -> list[str]:
        # Return the path to the file defining your custom components
        return ["templates/macros/my_extension_defaults.html"]
```

### Why Do This?
**Seamless Customization**: Theme creators who want to explicitly support your extension can redefine your custom macros (e.g., `harvester_status`) inside their own `ui.html` using their theme's native CSS classes.

**Automatic Fallback**: If the active theme does not override the macro, the theming loader automatically falls back to the default component implementation provided in your `my_extension_defaults.html` file.


## Scenario Playbook: Customization & Coexistence

Here are common scenarios you will encounter as an extension developer, and the recommended behavior:

### Scenario A: You want to customize a component specifically for a popular theme

**The Problem**: You want to alter a component's structure to match the look of
a popular theme (e.g. `nsw-design-system`), but doing so with raw markup might
break other themes.

**The Method**: You must refer to the target theme's documentation. Customize the component **only** when that theme is active, leaving unknown themes intact to avoid layout breakages. You can check the active theme programmatically or use the `patch_theme_ui()` hook:

  ```python
  def patch_theme_ui(self, theme, ui):
      if theme.name == "nsw-design-system":
          # Override or patch components specifically for NSW DS
          ui._add_component("custom_widget", nds_custom_implementation)
  ```

### Scenario B: You want to let portal maintainers integrate your components manually

**The Goal**: Provide advanced layout controls that can't be automatically
  inserted without risking container layout issues.

**The Method**: Provide a set of custom UI components in your extension, and
document how the end user can call or incorporate them into their theme's
templates. Provide code snippets and mockups rather than injecting raw tags
programmatically.

### Scenario C: You need to pass complex layout blocks into standard theme components

**The Goal**: You want to render a complex panel of filters inside a `ui.card` component.

**The Method**: Do not write raw HTML strings and pass them as text parameters. Always use the `ui.util.call` wrapper to safely pass nested block content into the theme's card:
  ```django
  {% call ui.util.call(ui.card, title=_("Harvester Filters")) %}
      <div class="my-custom-filter-inputs">
          {{ ui.input(name="q", label=_("Filter Query")) }}
          {{ ui.select_box(...) }}
      </div>
  {% endcall %}
  ```
