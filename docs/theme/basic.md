# Basic Theme Creation

A theme defines the visual identity of a CKAN instance. The simplest way to create a theme is to bootstrap it using the CLI and start mapping standard CKAN components.

---

## 3-Step Theme Setup

1. **Bootstrap the Structure**
   Use the CKAN CLI to create a theme directory containing the default folder structure:
   ```bash
   ckan theme create my_basic_theme
   ```
   This copies the reference `bare` theme structure, creating `templates/`, `assets/`, and `public/` directories in the current folder.

2. **Register the Theme**
   In your extension's `plugin.py`, implement the `ITheme` interface and register your theme by returning a list of `Theme` instances from `register_themes()`:
   ```python
   import os
   import ckan.plugins as p
   from ckanext.theming.interfaces import ITheme
   from ckanext.theming.lib import Theme

   class MyThemePlugin(p.SingletonPlugin, ITheme):

       def register_themes(self) -> list[Theme]:
           root = os.path.dirname(os.path.abspath(__file__))
           return [
               Theme("my_basic_theme", os.path.join(root, "themes/my_basic_theme"))
           ]
   ```

3. **Activate the Theme**
   Configure your CKAN portal's `.ini` configuration file to load your plugin and set the active theme:
   ```ini
   ckan.plugins = ... theming my_theme_plugin
   ckan.ui.theme = my_basic_theme
   ```

---

## Minimal File Structure

A basic theme requires at least the following file structure to map macros and assets:

```
my_basic_theme/
 ├── templates/
 │   └── macros/
 │       └── ui.html       # Primary UI component macro mappings
 └── assets/
     └── webassets.yml     # Asset bundle config for theme css/js
```

---

## Implementing the macros/ui.html

The `templates/macros/ui.html` file serves as the main entry point for the theming system. Whenever a template calls `{{ ui.button(...) }}` or `{{ ui.card(...) }}`, the loader maps the call to a macro defined inside this file.

Here is a minimal `ui.html` implementation mapping standard fields:

```django
{# Import base helper macros if needed, or define directly #}

{%- macro button(content, href, type="button", style="primary") -%}
    {%- if href -%}
        <a {{ ui.util.attrs(kwargs, {"class": "btn btn-" ~ style}) }} href="{{ href }}">
            {{ content }}
        </a>
    {%- else -%}
        <button {{ ui.util.attrs(kwargs, {"class": "btn btn-" ~ style}) }} type="{{ type }}">
            {{ content }}
        </button>
    {%- endif -%}
{%- endmacro -%}

{%- macro card(content, title) -%}
    <div {{ ui.util.attrs(kwargs, {"class": "card"}) }}>
        {%- if title -%}
            <div class="card-header">{{ title }}</div>
        {%- endif -%}
        <div class="card-body">{{ content }}</div>
    </div>
{%- endmacro -%}
```

> [!IMPORTANT]
> Always use `ui.util.attrs(kwargs, defaults)` to merge attributes. This ensures custom attributes, ARIA tags, and events passed by extension templates (like `data-module`, `aria-label`, or HTMX bindings) are correctly rendered on your tags.
