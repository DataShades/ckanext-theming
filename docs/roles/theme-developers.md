# Theme Developers Guide

As a **Theme Developer**, your primary goal is to establish a cohesive visual system and implement the component macro API (`ui.*`) to render pages reliably. This guide highlights the customization philosophy of `ckanext-theming` and how to architect themes for scalability.

---

## Architectural Goals

1. **API Completeness**: Implement all standard components defined in [components.yaml](file:///home/sergey/projects/core/ckanext-theming/ckanext/theming/components.yaml) to ensure any extension relying on `ui.*` components renders without throwing errors.
2. **Layout Stability**: Ensure that HTML grids, wrappers, and containers are robust and handle differing lengths of content elegantly.
3. **Accessibility**: Guarantee keyboard navigation, screen reader support, and focus states on all interactive elements.

---

## Customization Philosophy: Macros vs. Snippets

Traditional CKAN development promotes overriding individual snippets (`{% snippet "snippets/package_item.html" %}`) to customize parts of a page. However, this often leads to broken layouts: snippets are evaluated at runtime, and custom markup inserted by portal maintainers or extensions may break the layout expectations of the parent containers.

**`ckanext-theming` shifts this responsibility to the active theme:**
- **No layout assumptions**: We do not predict how custom markup will affect the page.
- **Theme-directed customization**: It is up to the active theme to decide how it supports customization of its components (e.g. by accepting slot arguments, nested blocks via `ui.util.call`, or custom dictionaries).

---

## Handling Complex Components

For complex, large components (such as a search facets panel, header block, or activity streams list), writing all the HTML directly inside a single macro in `ui.html` makes the file unreadable.

### Best Practice: Separate Implementation Files
You should move the implementation of complex components into separate helper files within your theme (e.g., under a subfolder in `templates/`) and include them inside the macro body:

```django
{# Inside themes/my_theme/templates/macros/ui.html #}

{%- macro search_facets(facets, limits) -%}
    {# Delegate the actual markup to a theme-specific helper template #}
    {%- include "theme_helpers/search_facets_impl.html" with context -%}
{%- endmacro -%}
```

### Constraints for Users & Extensions
- **Theme-Specific Implementation**: The helper files (like `search_facets_impl.html`) are theme-specific implementation details.
- **Rule of Engagement**: Extension authors or portal maintainers **must not** attempt to override or rely on these theme-specific helper files unless they are certain the portal will not switch themes. If the theme changes, those files will disappear, causing rendering failures.

---

## Incorporating Popular Extension Components

As a theme creator, you want your theme to look stunning when popular CKAN extensions (such as `ckanext-harvest` or `ckanext-scheming`) are enabled.

- **Proactive Styling**: If an extension is popular enough, you can write native implementations of its custom components directly inside your theme's `ui.html`.
- **How**: Check the custom component signatures defined by the extension, and add matching macros to your `ui.html` using your theme's specific CSS framework. This overrides the extension's default basic markup with your premium styling automatically.
