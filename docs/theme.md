# Creating and Registering CKAN Themes

A CKAN theme allows you to customize the look and feel of your CKAN instance by providing a set of UI macros that can be used consistently across your site. The theming system works by providing a collection of macros that replace or augment the default UI elements.

## Theme Structure

A CKAN theme should be organized in a specific directory structure:

```
your_theme/
 ├── templates/
 │   ├── (your custom templates)
 │   └── macros/
 │       └── ui.html
 │
 ├── assets/
 │   └── webassets.yml
 │
 └── public/
```

## Registering a Theme

### 1. Implement the ITheme Interface in Your Plugin

In your extension's `plugin.py` file, implement the `ITheme` interface. The key method is `register_themes()` which returns a dictionary mapping theme names to `Theme` objects:

```python
import os
import ckan.plugins as p
from ckanext.theming.interfaces import ITheme
from ckanext.theming.lib import Theme

class YourExtensionPlugin(ITheme, p.SingletonPlugin):

    def register_themes(self):
        # Return a dictionary of theme names to Theme objects
        root = os.path.dirname(os.path.abspath(__file__))
        return {
            'your_theme': Theme(
                os.path.join(root, 'themes/your_theme'),
                # Optionally specify a parent theme to extend
                # parent='parent_theme_name'
            ),
        }
```

### 2. Custom UI Implementation (Optional)

You can customize the macro loading mechanism by setting a custom UI class on the Theme. This allows you to customize how macros are loaded:

```python
from ckanext.theming.lib import MacroUI, Theme

class YourThemeUI(MacroUI):
    source = "custom/location/of/macros/ui.html"

    def __init__(self, app):
        super().__init__(app)
        # Additional initialization if needed
```

Then assign it to your theme:

```python
def register_themes(self):
    from .theme import YourThemeUI  # Import your custom UI class

    root = os.path.dirname(os.path.abspath(__file__))
    theme = Theme(os.path.join(root, 'themes/your_theme'))
    theme.UI = YourThemeUI  # Set custom UI class

    return {
        'your_theme': theme,
    }
```

### 3. Create the Main Macros Entry Point

Create `themes/your_theme/macros/ui.html` with definition of all the
macros. You can define macro elsewhere and re-export it by creating global
template variable.

```html
{% import "macros/ui/element.html" as element %}

{# Re-export macro #}
{% set button = element.button %}

{# Define new macro #}
{% macro input() %}
    ...
{% endmacro %}
```

### 4. Implement Individual Macro Files

Each macro file should contain actual implementations that use appropriate CSS classes for your chosen framework:

Example `themes/your_theme/macros/ui/element.html` (using Bootstrap classes):

```html
{%- macro button(content, style="primary", type="button") -%}
    <button type="{{ type }}" class="btn btn-{{ style }}">
        {{ content }}
    </button>
{%- endmacro %}

{%- macro divider() -%}
    <hr class="my-4"/>
{%- endmacro %}

{%- macro image(src, alt="") -%}
    <img {{ ui.util.attrs(kwargs) }} class="img-fluid"
        alt="{{ alt }}" src="{{ src }}"/>
{%- endmacro %}

{%- macro link(content, href) -%}
    <a class="link-primary text-decoration-none" href="{{ href or content }}">
        {{ content }}
    </a>
{%- endmacro %}
```

/// note

All macros should accept arbitrary keyword arguments. If a macro doesn't
reference `kwargs` directly in its body, add `{%- do kwargs -%}` as the first
line. If it uses attributes, use `{{ ui.util.attrs(kwargs) }}`.

///
### 5. Provide Template Overrides (Optional)

Create custom templates in `themes/your_theme/templates/` to override CKAN's
default templates. Common templates to override include:

- `base.html` - The main base template
- `home/index.html` - Home page template
- `package/search.html` - Dataset search page template


### 6. Add Assets

Include CSS, JavaScript, and image assets in `themes/your_theme/assets/` to
style and enhance your theme.

## Using the Theme

Once your theme is properly registered:

1. Install your extension: `pip install -e .`
2. Add your plugin alongside with `theming` to CKAN's configuration:
   `ckan.plugins = ... your_extension theming`
3. Configure the theme in your CKAN configuration: `ckan.ui.theme = your_theme`
4. The theme will be available and can be used throughout CKAN templates via
   the UI macros

## Reference Implementation

The `bare`, `bulma`, `tailwind`, and `bs5` themes in this extension
serve as reference implementations showing how different CSS frameworks can be
integrated with the theming system. You can use them as starting points for
building your own themes.
