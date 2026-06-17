# Standalone Component Libraries

A **Component Library** (or UI Library) is a type of theme that only provides UI component macros (`ui.*`), asset files (CSS, JS, fonts), and icon mappings. It **does not redefine core CKAN page templates** (like `package/read.html` or `user/login.html`).

This pattern allows you to bundle styling rules, CSS frameworks, and interactions into a modular, reusable design system package that other layout themes can inherit from.

---

## Design System Structure

A standalone component library (such as the built-in `nds-ui` or `classic-polyfill` libraries) is structured like this:

```
my_component_library/
 ├── templates/
 │   └── macros/
 │       └── ui.html       # Definitions for all standard ui.* macros
 ├── assets/
 │   ├── css/              # Design system styling files
 │   ├── js/               # Custom interactive modules
 │   └── webassets.yml     # Registers stylesheets and scripts
 └── theme.py              # Registers the library metadata and icon mappings
```

---

## Theme Configuration (`theme.py`)

In the library's `theme.py` file, instantiate a `Theme` instance pointing to the library directory. Standalone component libraries often include a custom `icon_map` to map standard icon IDs (e.g., `search`, `trash`) to design-system-specific icon sets (such as Google Material Symbols or FontAwesome):

```python
import os
from ckanext.theming.lib import Theme

here = os.path.dirname(__file__)

# Mapping standard icon names to Material Icon names
icon_map = {
    "search": "search_icon",
    "trash": "delete_forever",
    "edit": "edit_note",
    "home": "home_app",
}

def make_theme(name: str = "my-component-library"):
    return Theme(
        name,
        here,
        icon_map=icon_map,
        # A standalone library has no parent (parent=None)
    )
```

---

## The Macro Registry (`templates/macros/ui.html`)

In a component library, `ui.html` contains the concrete implementations of all standard components declared in [components.yaml](file:///home/sergey/projects/core/ckanext-theming/ckanext/theming/components.yaml) using the CSS classes of your chosen design system.

### Inheritance Fallback Setup (Important for Library Authors)
To allow child themes to selectively override specific macros while falling back to the library implementations for the rest, you must use **re-exports with the default fallback strategy**:

Instead of defining macros directly, write fallback bindings:

```django
{# templates/macros/ui.html #}

{%- macro _button(content, href, type="button", style="primary") -%}
    <button {{ ui.util.attrs(kwargs, {"class": "nds-btn nds-btn--" ~ style}) }} type="{{ type }}">
        {{ content }}
    </button>
{%- endmacro -%}

{# Let a child theme define 'button' first. If undefined, fall back to our _button implementation #}
{% set button = button | default(_button) %}
```

---

## Why Create a Standalone Component Library?

1. **Reusability**: You can write the complex markup and class rules for a framework (such as Tailwind CSS or Bulma) once.
2. **Layout Independence**: Multiple portals can define completely different page layouts (one with a sidebar navigation, another with a header drawer) while using the same component library to maintain a unified visual system.
3. **Framework Upgrades**: If you upgrade the underlying design system version (e.g., Bootstrap 4 to 5, or Tailwind 3 to 4), you only modify the macros and stylesheets inside the component library. Any theme inheriting from it automatically updates.
