# Themes Relying on Component Libraries

A **Layout-Only Theme** focuses on page structure, HTML page skeletons (`base.html`, `page.html`), and page-level routes (like `package/search.html`). It does not define custom CSS or JS assets itself, nor does it contain a `macros/` folder. Instead, it delegates all component rendering to a standalone **Component Library** by setting it as its `parent`.

This pattern separates structural layout changes from core style implementations.

---

## Structure of a Reliant Theme

An example of this split is the `nsw-design-system` theme which inherits from the `nds-ui` library:

```
my_reliant_theme/
 ├── templates/
 │   ├── base.html                  # Main layout skeleton
 │   ├── footer.html                # Custom footer structure
 │   ├── header.html                # Custom header layout
 │   └── package/
 │       └── search.html            # Custom search page layout
 └── theme.py                       # Registers the theme metadata
```

Notice that there is **no** `templates/macros/ui.html` or `assets/` folder in the layout theme. All component definitions are inherited from the parent.

---

## Configuring the Theme (`theme.py`)

To inherit from a component library, set the `parent` parameter in the `Theme` class to the name of the target UI library:

```python
# themes/my_reliant_theme/theme.py
import os
from ckanext.theming.lib import Theme

here = os.path.dirname(__file__)

def make_theme(name: str = "my-reliant-theme"):
    return Theme(
        name,
        here,
        parent="my-component-library"  # Inherits all macros & assets from the UI library
    )
```

---

## Building Templates

Inside your reliant theme templates, you can call any `ui.*` components defined by the parent library.

For example, your custom `templates/header.html` page template might look like this:

```django
{# templates/header.html #}
<header class="site-header">
    <div class="container">
        <div class="logo">
            <a href="/">{{ ui.image(src="/images/logo.svg", alt="My Site Logo") }}</a>
        </div>

        <nav class="main-nav">
            {% call ui.util.call(ui.nav) %}
                {{ ui.link("Home", href="/") }}
                {{ ui.link("Datasets", href="/dataset") }}
                {{ ui.link("Organizations", href="/organization") }}
            {% endcall %}
        </nav>

        <div class="header-actions">
            {% if current_user.is_authenticated %}
                {{ ui.button("Dashboard", href=h.url_for("user.dashboard"), style="secondary") }}
            {% else %}
                {{ ui.button("Log In", href=h.url_for("user.login"), style="primary") }}
            {% endif %}
        </div>
    </div>
</header>
```

When CKAN renders this header:

1. The templates are pulled from the layout theme `my-reliant-theme`.
2. The `ui.image`, `ui.nav`, `ui.link`, and `ui.button` macros are resolved from the parent theme `my-component-library`.

---

## Key Advantages

**Shared Styling**: Multiple reliant themes (e.g. `nsw-design-system-dark`, `nsw-design-system-minimal`) can share the exact same component definitions in `nds-ui`, making them look consistent while rearranging the layout grids.

**Easy Theme Swapping**: If you want to switch your design framework (e.g., from Bootstrap 5 to Tailwind), you only swap the parent library setting from `parent="bootstrap-lib"` to `parent="tailwind-lib"`. Your structural templates remain unchanged.

**Simpler Upgrades**: The templates in your reliant theme are standard HTML skeletons calling semantic functions. They are insulated from changes in CSS class names or framework markup.
