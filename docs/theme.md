# Creating CKAN themes

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

Each macro file should contain actual implementations that use appropriate CSS classes for your chosen framework. When implementing macros, follow these conventions:

#### Parameter Order Consistency
All macros follow the same parameter convention:
- `content` is the first positional parameter (and often the only one when needed)
- All other parameters use named parameters with appropriate defaults
- Use `**kwargs` for extra attributes that will be passed to the element

Example `themes/your_theme/macros/ui/element.html` (using Bootstrap classes):

```html
{%- macro button(content, href, type="button", style="primary") -%}
    {%- if href -%}
        <a {{ ui.util.attrs(kwargs) }} href="{{ href }}" class="btn btn-{{ style }}">{{ content }}</a>
    {%- else -%}
        <button {{ ui.util.attrs(kwargs) }} type="{{ type }}" class="btn btn-{{ style }}">{{ content }}</button>
    {%- endif %}
{%- endmacro %}

{%- macro divider(content) -%}
    {%- if content -%}
        <div {{ ui.util.attrs(kwargs) }} class="divider-with-content">
            <hr><span>{{ content }}</span><hr>
        </div>
    {%- else -%}
        <hr {{ ui.util.attrs(kwargs) }}>
    {%- endif %}
{%- endmacro %}

{%- macro image(src, alt, height, width) -%}
    <img
        {{ ui.util.attrs(kwargs) }}
        src="{{ src }}"
        {%- if alt %} alt="{{ alt }}"{% endif %}
        {%- if height %} height="{{ height }}"{% endif %}
        {%- if width %} width="{{ width }}"{% endif %}
    >
{%- endmacro %}

{%- macro link(content, href, blank) -%}
    {%- if blank -%}
        {%- do kwargs.setdefault("attrs", {}).setdefault("target", "_blank") -%}
        {%- do kwargs.setdefault("attrs", {}).setdefault("rel", "noopener noreferrer") -%}
    {%- endif %}
    <a {{ ui.util.attrs(kwargs) }} href="{{ href or content }}">{{ content }}</a>
{%- endmacro %}
```

/// note

All macros should accept arbitrary keyword arguments. If a macro doesn't
reference `kwargs` directly in its body, add `{%- do kwargs -%}` as the first
line. If it uses attributes, use `{{ ui.util.attrs(kwargs) }}`.

///

### Accessibility Considerations

When implementing theme components, ensure proper accessibility support by using appropriate ARIA attributes and semantic HTML:

```html
{%- macro button(content, href, type="button", style="primary") -%}
    {%- if href -%}
        <a {{ ui.util.attrs(kwargs) }}
           href="{{ href }}"
           class="btn btn-{{ style }}"
           {% if not kwargs.aria %}aria-label="{{ content }}"{% endif %}>
            {{ content }}
        </a>
    {%- else -%}
        <button {{ ui.util.attrs(kwargs) }}
                type="{{ type }}"
                class="btn btn-{{ style }}"
                {% if not kwargs.aria %}aria-label="{{ content }}"{% endif %}>
            {{ content }}
        </button>
    {%- endif %}
{%- endmacro %}

{%- macro input(content, name, id, label, value, required, placeholder, type="text", errors=[]) -%}
    {%- set field_id = id or ("field-" ~ name) if name else ui.util.id() if label else "" -%}
    {%- set error_id = ui.util.id() if errors -%}
    {%- set help_id = ui.util.id() if content -%}

    <div>
        {%- if label -%}
            <label for="{{ field_id }}">{{ label }}</label>
        {%- endif %}
        {%- if content -%}
            <div class="input-help" id="{{ help_id }}">{{ content }}</div>
        {%- endif %}
        <input
            {{ ui.util.attrs(kwargs) }}
            type="{{ type }}"
            {%- if name %} name="{{ name }}"{% endif %}
            id="{{ field_id }}"
            {%- if value %} value="{{ value }}"{% endif %}
            {%- if placeholder %} placeholder="{{ placeholder }}"{% endif %}
            {%- if required %} required{% endif %}
            {%- if content %} aria-describedby="{{ help_id }}"{% endif %}
            {%- if errors %} aria-invalid="true"{% endif %}
        >
        {%- if errors %}
            <span id="{{ error_id }}">{{ ui.field_errors(errors) }}</span>
        {%- endif %}
    </div>
{%- endmacro %}
```

Use proper ARIA attributes (`aria-label`, `aria-describedby`, `aria-invalid`, `aria-hidden`, etc.), semantic HTML elements, and ensure keyboard navigation support.

### CLI Tool Integration

This theming system integrates with CKAN's CLI tools for theme development and management:

```bash
# List available themes
ckan theme list

# Check theme components
ckan theme components

# Validate theme implementation
ckan theme validate <theme-name>

# Debug theme issues
ckan theme debug

# Generate new theme scaffolding
ckan theme create <theme-name>

# Analyze theme structure
ckan theme analyze <theme-name>
```
### 5. Provide Template Overrides (Optional)

Create custom templates in `themes/your_theme/templates/` to override CKAN's
default templates. Common templates to override include:

- `_base.html` - The main base template
- `home/index.html` - Home page template
- `package/search.html` - Dataset search page template


### 6. Theme Inheritance

Themes can inherit from parent themes to build upon existing functionality:

```python
def register_themes(self):
    root = os.path.dirname(os.path.abspath(__file__))
    return {
        'child_theme': Theme(
            os.path.join(root, 'themes/child_theme'),
            parent='parent_theme_name'  # Inherits from another theme
        ),
    }
```

Child themes inherit all macros and templates from the parent, but can selectively override only the components they want to customize. Unimplemented macros fall back to the parent theme.

### 7. Add Assets

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
