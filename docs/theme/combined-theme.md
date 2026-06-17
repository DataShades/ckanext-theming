# Combined Themes

A **Combined Theme** provides both page-level templates and its own UI component library together in a single package. It registers a theme name that does not inherit from any parent (except perhaps standard fallbacks) and overrides both structural layouts and component macros inside its own directory.

The `midnight-blue-portable` theme is a prime example of a combined theme.

---

## File Structure of a Combined Theme

A combined theme defines both structural files and macro files inside the same templates hierarchy:

```
my_combined_theme/
 ├── templates/
 │   ├── base.html                  # Structural page layouts
 │   ├── header.html
 │   ├── footer.html
 │   ├── package/
 │   │   └── search.html
 │   │
 │   └── macros/
 │       └── ui.html                # UI library component macros
 ├── assets/
 │   ├── css/                       # Theme styles
 │   ├── js/                        # Theme interactive scripts
 │   └── webassets.yml
 └── theme.py                       # Theme configuration
```

---

## Configuring the Theme (`theme.py`)

Since a combined theme provides all components natively, it does not require a parent setting (or it can inherit from a minimal fallback polyfill like `classic-polyfill`):

```python
# themes/my_combined_theme/theme.py
import os
from ckanext.theming.lib import Theme

here = os.path.dirname(__file__)

def make_theme(name: str = "my-combined-theme"):
    return Theme(
        name,
        here
        # parent = None (or parent="classic-polyfill" to inherit standard CKAN fallbacks)
    )
```

---

## Rendering Flow

In a combined theme:
- CKAN checks `my_combined_theme/templates/` first for structural page overrides (e.g. `package/search.html`).
- Any `ui.*` component macros called inside these templates are resolved locally from `my_combined_theme/templates/macros/ui.html`.

---

## When to Build a Combined Theme

**Tight Visual Coupling**: If the layout elements (e.g., sidebars, grids, headers) are tightly dependent on component styles (e.g. card sizes, button paddings) and the design cannot easily be separated into an independent layout wrapper.

**Dedicated Corporate Portals**: When you are building a custom portal for a single organization with a highly specific design system. You don't expect the layout templates to be reused elsewhere, so packaging everything together simplifies the repository.

**Quick Prototyping**: Bundling templates and macros in one directory is faster for initial development since you can iterate on both structural pages and atomic components in the same codebase.
