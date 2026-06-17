# Standalone Component Libraries

A **Component Library** (or UI Library) is a type of theme that only provides UI component macros (`ui.*`), asset files (CSS, JS, fonts), and icon mappings. It **does not redefine core CKAN page templates** (like `package/read.html` or `user/login.html`).

This pattern allows you to bundle styling rules, CSS frameworks, and interactions into a modular, reusable design system package that other layout themes can inherit from.


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

### Modular Macro Files for Large Design Systems
For large component libraries, putting all macro definitions inside a single `ui.html` file makes it unmaintainable. Instead, split the macros into logical files inside a subdirectory (e.g. `templates/macros/ui/`) and import them with context in the main `ui.html`:

```django
{# templates/macros/ui.html #}
{% import "macros/ui/forms.html" as _forms with context %}
{% import "macros/ui/feedback.html" as _feedback with context %}

{# Mappings with fallback bindings #}
{% set input = input | default(_forms.input) %}
{% set alert = alert | default(_feedback.alert) %}
{% set popover = popover | default(_feedback.popover) %}
{% set popover_handle = popover_handle | default(_feedback.popover_handle) %}
```


## JavaScript Initialization in Component Libraries

Interactive components (like popovers, modals, or toasts) often require JavaScript. As a best practice, **avoid inline `<script>` tags inside macro definitions**. Inline scripts suffer from several issues:

- They pollute the DOM and degrade page performance.
- They may execute before the main JavaScript bundle is fully loaded (resulting in `undefined` reference errors).
- They cause duplicate initialization or fail to bind when components are dynamically injected/re-rendered (e.g. via AJAX/HTMX).

### Recommended Pattern: Declarative Attributes and Global Initializer

**Declare triggers in the macro HTML:**

Instead of writing a `<script>` tag inside the macro, use standard data
attributes (e.g. `data-bs-toggle="popover"`) or custom targets:

```django
{%- macro popover_handle(content, id=None) -%}
    {%- set popover_attrs = {
        "data-bs-toggle": "popover",
        "data-bs-content": "(see #" ~ id ~ "-popover-content)",
        "tabindex": "0"
    } -%}
    <span {{ ui.util.attrs(ui.util.augment_attrs(kwargs, popover_attrs)) }}>
        {{ content }}
    </span>
{%- endmacro %}
```

!!! note

       Make sure to pass `popover_attrs` without specifying `key=None` in
       `augment_attrs`. Omitting it (which defaults to `key="attrs"`) ensures
       that fully qualified names like `data-bs-toggle` are correctly nested
       within the `attrs` sub-dictionary so that they are serialized to HTML
       attributes.

**Initialize globally in the theme JS asset:**

Create a single initialization script in `assets/js/` (and register it in `webassets.yml`) that runs on `DOMContentLoaded` and targets the elements declaratively:

```javascript
document.addEventListener("DOMContentLoaded", () => {
    // Find all declarative popovers
    const popovers = document.querySelectorAll('[data-bs-toggle="popover"]');
    popovers.forEach((el) => {
        // Safely resolve content references (if target is in another element)
        const contentAttr = el.getAttribute('data-bs-content') || '';
        const match = contentAttr.match(/^\(see\s+(#.+)\)$/);
        const options = {};
        if (match && match[1]) {
            const targetEl = document.querySelector(match[1]);
            if (targetEl) {
                options.content = targetEl.innerHTML;
                options.html = true;
            }
        }

        // Initialize idempotently
        bootstrap.Popover.getOrCreateInstance(el, options);
    });
});
```

**Handle dynamic updates/JS APIs cleanly:**

If your UI library provides a JavaScript API to register components dynamically (e.g. `sandbox.ui.popover(content, {target})`), ensure that any existing instances on the target element are properly disposed of before creating the new one to prevent conflicts:
```javascript
popover(content, props) {
    const target = props.target;
    // Clean up stale instances first
    const existing = bootstrap.Popover.getInstance(target);
    if (existing) {
        existing.dispose();
    }
    // Configure new attributes and instantiate
    target.setAttribute("data-bs-toggle", "popover");
    target.setAttribute("data-bs-content", content);
    return new bootstrap.Popover(target);
}
```


## Why Create a Standalone Component Library?

**Reusability**: You can write the complex markup and class rules for a framework (such as Tailwind CSS or Bulma) once.

**Layout Independence**: Multiple portals can define completely different page layouts (one with a sidebar navigation, another with a header drawer) while using the same component library to maintain a unified visual system.

**Framework Upgrades**: If you upgrade the underlying design system version (e.g., Bootstrap 4 to 5, or Tailwind 3 to 4), you only modify the macros and stylesheets inside the component library. Any theme inheriting from it automatically updates.
