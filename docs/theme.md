# Creating CKAN Themes

## Theme Structure

A CKAN theme should be organized in the following directory structure:

```
your_theme/
 ├── templates/
 │   ├── (your custom templates)
 │   └── macros/
 │       └── ui.html
 │
 ├── assets/
 │   └── (CSS, JS, and other assets)
 │
 └── public/
     └── (static files served directly)
```

## Registering a Theme

### 1. Implement the `ITheme` Interface

In your extension's `plugin.py` file, implement the `ITheme` interface. The key
method is `register_themes()` which returns a list of `Theme` objects:

```python
import os
import ckan.plugins as p
from ckanext.theming.interfaces import ITheme
from ckanext.theming.lib import Theme

class YourExtensionPlugin(ITheme, p.SingletonPlugin):

    def register_themes(self):
        # Return a list of theme Theme objects
        root = os.path.dirname(os.path.abspath(__file__))
        return [
            Theme(
                'your_theme',
                os.path.join(root, 'themes/your_theme'),
                # Optionally specify a parent theme to extend
                # parent='parent_theme_name'
            ),
        ]
```

### 2. Theme Inheritance

Themes can inherit from parent themes to build upon existing functionality:

```python
def register_themes(self):
    root = os.path.dirname(os.path.abspath(__file__))
    return [
        Theme(
            'child_theme',
            os.path.join(root, 'themes/child_theme'),
            parent='parent_theme_name'  # Inherits from another theme
        ),
    ]
```

Child themes inherit all macros and templates from the parent, but can selectively override only the components they want to customize. Unimplemented macros fall back to the parent theme.

### 3. Custom UI Implementation (Optional)

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
    return [
        Theme(
            'your_theme',
            os.path.join(root, 'themes/your_theme'),
            ui_factory=YourThemeUI,  # Set custom UI class
        ),
    ]
```

## Creating UI Macros

### 1. Create the Main Macros Entry Point

Create `themes/your_theme/templates/macros/ui.html` with definitions of all the macros. You can define macros elsewhere and re-export them by creating global template variables:

```html
{% import "macros/ui/element.html" as element %}

{# Re-export macro #}
{% set button = element.button %}
{% set card = element.card %}

{# Define new macro #}
{% macro input() %}
    ...
{% endmacro %}
```

/// note | Flexible themes

When macros created directly inside `ui.html` or unconditionaly re-exported as
in example above, child theme cannot override these macros using the following
code:

```html
{% ckan_extends %}

{# Override macro #}
{% set button = my_custom_button %}
```

Jinja2 processes template hierarchy in a reverse order, so the original
`button` macro will take precedence over the custom one. To make such overrides
possible, never define macros directly inside `ui.html` and always use
re-export with the default fallback:

```html
{% import "macros/ui/element.html" as element %}

{# keep definition from the child template or fallback to the original implementation #}
{% set button = button | default(element.button) %}
{% set card = card |default(element.card) %}

{# use the same fallback-strategy for macros defined in the current file. Give
the child template an opportunity to define its own `input` macro and, when
such macro is not defined, use the original `_input` as a fallback implementation #}
{% macro _input() %}
    ...
{% endmacro %}
{% set input = input | default(_input)%}

```

///

### 2. Implement Individual Macro Files

Each macro file should contain actual implementations that use appropriate CSS classes for your chosen framework. When implementing macros, follow these conventions:

#### Parameter Order Consistency
All macros follow the same parameter convention:

- `content` is the first positional parameter (and often the only one when needed)
- All other parameters use named parameters with appropriate defaults
- Always use `kwargs` for extra attributes that may be passed to the element.

Example `themes/your_theme/templates/macros/ui/element.html` (using Bootstrap classes):

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

### 3. UI Utilities

The theming system provides utility functions accessible via `ui.util`:

- `ui.util.attrs(kwargs)`: Helper to render HTML attributes from a dictionary
- `ui.util.call(element, *args, **kwargs)`: Call an inline element as a block element
- `ui.util.map(element, items, *args, **kwargs)`: Map an element over a collection
- `ui.util.now()`: Get the current UTC datetime
- `ui.util.id(value, prefix="id-")`: Generate a unique identifier
- `ui.util.keep_item(category, key, value)`: Store items in UI storage
- `ui.util.pop_items(category, key=None)`: Retrieve and remove items from UI storage
- `ui.util.get_items(category, key=None)`: Get items from UI storage

Example usage of utilities:

```html
{%- macro button_group(items) -%}
    <div class="btn-group">
        {{ ui.util.map(ui.button, items) }}
    </div>
{%- endmacro %}

{# Using call with util.call #}
{% call ui.util.call(ui.button, style="primary") %}
    <i class="icon"></i>
    Click me!
{% endcall %}
```

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

## Using UI Macros in Templates

Once a theme is active, UI macros can be used in templates:

```jinja
{{ ui.button("Click Me", style="primary", type="button") }}
{{ ui.card(title="My Card", content="Card content here") }}
{{ ui.alert("Success message", style="success") }}
{{ ui.link("Visit CKAN", href="https://ckan.org", blank=True) }}
```

All parameters except for `content` must be passed to macro by name. This
simplifies transition between themes, when macros expect different set of
arguments or define them in different order. `content` always comes first when
it's present, that's why it's safe to pass it without name, but all other
arguments have no recommended order and every theme is free to choose according
to its preferences.

## CLI Tools for Theme Development

The theming system provides comprehensive CLI tools for theme development and management:

### Theme Management
```bash
# List available themes
ckan theme list

# Create a new theme with all required structure
ckan theme create mytheme

# Create a new theme in a specific location
ckan theme create mytheme /path/to/themes
```

### Component Management
```bash
# List available components for the configured theme
ckan theme component list

# List available components for a specific theme
ckan theme component list -t mytheme

# Analyze UI components and their implementations
ckan theme component analyze
ckan theme component analyze link button card

# Check if a theme implements all required UI components
ckan theme component check
ckan theme component check -t mytheme
```

### Template Management
```bash
# List template files in a theme
ckan theme template list
ckan theme template list -t mytheme

# Verify that a theme contains all required templates
ckan theme template check
ckan theme template check -t mytheme

# Analyze theme templates and their structure
ckan theme template analyze
ckan theme template analyze _header.html _footer.html
ckan theme template analyze --relative-filename
```

### Endpoint Analysis
```bash
# List registered Flask endpoints
ckan theme endpoint list

# List variants of Flask endpoints
ckan theme endpoint variants
ckan theme endpoint variants dataset.search dataset.read

# Observe the template and context variables used by a Flask endpoint
ckan theme endpoint observe dataset.search
ckan theme endpoint observe dataset.read id=my-dataset -v
ckan theme endpoint observe dataset.read --auth-user admin id=my-dataset

# Dump templates and context variables used by Flask endpoints in JSON format
ckan theme endpoint dump --auth-user admin --user testuser --package testpkg --resource testres --resource-view testview --organization testorg --group testgroup
```

## Configuration

To use a theme, configure it in your CKAN configuration:

```ini
ckan.plugins = ... theming
ckan.ui.theme = your_theme
```

## Reference Implementation

The `bare` theme in this extension serves as a reference implementation showing the minimal structure needed for a theme. You can use it as a starting point for building your own themes by running:

```bash
ckan theme create mytheme
```

This creates a new theme based on the bare theme structure with all required components.
