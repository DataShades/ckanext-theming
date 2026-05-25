{%raw%}# Creating CKAN Themes

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


/// details | Create new theme using CLI
    type: info

New theme can be created by making a copy of an existing theme using CKAN CLI:

```sh
ckan theme create THEME_NAME
```

The folder THEME_NAME will be created in the current directory and will contain
all the files with minimalistic theme implementation. It does not look nice,
but it does not contain any framework-specific code, so it's the best starting
point.

To create a theme by copying an existing theme, specify `--base` option

```sh
ckan theme create THEME_NAME --base ANOTHER_COOOL_THEME
```

To create theme in a different location, provide path to the base folder after
theme name. In this case THEME_NAME will be created inside specified location
instead of the current folder.


```sh
ckan theme create THEME_NAME /base/location/for/the/new/theme
```

///

## Registering a Theme

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


/// details | Theme inheritance
    type: info

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

Child themes inherit all macros and templates from the parent, but can
selectively override only the components they want to customize. Unimplemented
macros fall back to the parent theme.

///

/// details | Additional macro sources
    type: tip

To load macros from an additional file(in addition to `macros/ui.html`),
implement `ITheme.get_additional_theme_ui_sources`:

```python
def get_additional_theme_ui_sources(self) -> list[str]:
    return ["additional/location/of/macros.html"]
```

///

## Creating UI Macros

Create `themes/your_theme/templates/macros/ui.html` with definitions of all the
macros.

```django
{% macro input() %}
    ...
{% endmacro %}
```

Macros can be defined elsewhere and re-exported by creating global
template variables:

```django
{% import "macros/your_theme_macros/element.html" as element %}

{# Re-export macro #}
{% set button = element.button %}
{% set card = element.card %}
```

/// admonition | **DO NOT** define macros inside blocks
    type: warning

Macros defined inside blocks will be unavailable for import. Imports are
processed at compile time, while blocks are evaluated at render time, so macros
defined inside blocks are invisible for external code.

///

/// details | Reusable themes
    type: tip

When macros created directly inside `ui.html` or unconditionaly re-exported as
in example above, child theme cannot override these macros. The code below
**DOES NOT** work:

```django
{# inside child theme's macros/ui.html #}
{% ckan_extends %}

{# Override macro #}
{% set button = my_custom_button %}
```

Jinja2 processes template hierarchy in a reverse order, so the original
`button` macro will take precedence over the custom one. To make such overrides
possible, never define macros directly inside `ui.html` and always use
re-export with the default fallback:

```django
{% import "macros/ui/element.html" as element %}

{# keep definition from the child template or fallback to the original implementation #}
{% set button = button | default(element.button) %}
{% set card = card | default(element.card) %}

{# use the same fallback-strategy for macros defined in the current file. Give
the child template an opportunity to define its own `input` macro and, when
such macro is not defined, use the original `_input` as a fallback implementation #}
{% macro _input() %}
    ...
{% endmacro %}
{% set input = input | default(_input)%}

```

Even if you define macros directly inside `ui.html`, child theme can override
them. But to achieve this, it must implement
`ITheme.get_additional_theme_ui_sources`. This method returns list of files
with macros that have higher priority than the base `ui.html`. The downside of
this approach is a bigger list of macro sources which leads to more complex
development and unpredictable macro locations.

///


Each macro file should contain actual implementations that use appropriate CSS classes for your chosen framework. When implementing macros, follow these conventions:

#### Parameter Order Consistency
All macros follow the same parameter convention:

- `content` is the first positional parameter
- All other parameters use named parameters with appropriate defaults
- Always use `kwargs` for extra attributes that may be passed to the element

/// admonition | Example
    type: example

`content` is the first parameter. Usually content is the most complex part of
the macro output, that must be provided by the caller. Other parameters can
either be specified without a default value if there are no suitable
options(`href`), or use most expected/neutral values as defaults(`type=button`,
`style=primary or default`).

```django
{%- macro button(content, href, type="button", style="primary") -%}
    {%- if href -%}
        <a {{ ui.util.attrs(kwargs) }} href="{{ href }}" class="btn btn-{{ style }}">
            {{ content }}
        </a>
    {%- else -%}
        <button {{ ui.util.attrs(kwargs) }} type="{{ type }}" class="btn btn-{{ style }}">
            {{ content }}
        </button>
    {%- endif %}
{%- endmacro %}
```

Sometimes macro can work even without content. In the example below, divider
without content will be rendered as a plain horizontal line, while divider with
content will show this content surrounded by horizontal lines.

```django
{%- macro divider(content) -%}
    {%- if content -%}
        <div {{ ui.util.attrs(kwargs) }} class="divider-with-content">
            <hr><span>{{ content }}</span><hr>
        </div>
    {%- else -%}
        <hr {{ ui.util.attrs(kwargs) }}>
    {%- endif %}
{%- endmacro %}
```

Certain macros do not present any HTML/textual content to user(or do not accept
it at least). In this case it's reasonable to omit `content` completely. It
would be acceptable to use move `alt` on the first position and call it
`content`, but there are two reasons not to do it: it may be misleading;
`content` usually meant for potentially complex HTML, not only plain
text. `src` is also is not a good candidate for `content`, because it's an
attribute, not the actual content shown to user.

```django
{%- macro image(src, alt, height, width) -%}
    <img
        {{ ui.util.attrs(kwargs) }}
        src="{{ src }}"
        {%- if alt %} alt="{{ alt }}"{% endif %}
        {%- if height %} height="{{ height }}"{% endif %}
        {%- if width %} width="{{ width }}"{% endif %}
    >
{%- endmacro %}
```

To render additional attributes on the tag, use `ui.util.attrs(kwargs)`. It
will take `attrs` parameter from additional arguments provided during macro
call and transform it into attribute string. Certain macro will expose
parameters to simplify attribute assgnment. For example, the following macro
has `blank` parameter, that modifies `attrs` parameter. Because of its internal
logic, instead of calling it like `ui.link(..., attrs={"target": "_blank",
"rel": "noopener noreferrer"})`, you can use shorter form `ui.link(..., blank=true)`

```django
{%- macro link(content, href, blank) -%}
    {%- if blank -%}
        {%- do kwargs.setdefault("attrs", {}).setdefault("target", "_blank") -%}
        {%- do kwargs.setdefault("attrs", {}).setdefault("rel", "noopener noreferrer") -%}
    {%- endif %}
    <a {{ ui.util.attrs(kwargs) }} href="{{ href or content }}">{{ content }}</a>
{%- endmacro %}
```

Note, every macro in the example uses `kwargs` variables. It must not be added
to signature: whenever Jinja2 sees that `kwargs` is used inside macro body, it
implicitely adds `**kwargs` to macro signature; attempt to do it explicitely
will cause en error.

Because of `kwargs` usage, users can call any of these macros with additional
parameters, even if current theme does not process them. In this way, when user
switches from a different theme, that has more arguments inside macro
definition, pages will not break because of invalid call payload.

///

### UI Utilities

The theming system provides utility functions accessible via `ui.util`:

/// details | `ui.util.attrs(kwargs)`
    type: info

Helper to render HTML attributes from a dictionary. It extracts from `kwargs`
parameters with names `attrs`, `aria`, `data`, `on`, `hx` and builds attribute
string from them. Also it has second argument, that can be used to specify
default attributes(`attrs`), that user can override during macro call:

```django
{% macro button(content) %}
    <button {{ ui.util.attrs(kwargs, {"class": "btn"}) }}>
        {{ content }}
    </button>
{% endmacro %}
```

///

/// details | `ui.util.call(element, *args, **kwargs)`
    type: info

Call an inline element as a block element. It takes the content of the call
block and pass it as a first argument of the called macro. Use this to add
complex content with nested HTML into element.

```django
{% call ui.util.call(ui.button, type="submit") %}
    <i class="fa fa-info-circle"></i>
    Click
{% call%}

{# approximately the same but less readable version #}
{{ ui.call('<i class="fa fa-info-circle"></i> Click'|safe, type="submit") }}
```
///

/// details | `ui.util.map(element, items, *args, **kwargs)`
    type: info

Map an element over a collection

```django
{{ ui.util.map(ui.button, ["Click", "Press", "Push"], type="submit") }}
```
///

/// details | `ui.util.now()`
    type: info

Get the current UTC datetime

///

/// details | `ui.util.id(value, prefix="id-")`
    type: info

Generate a unique identifier(if value is empty) or transform value into stable
UUID.

///

/// details | `ui.util.tag(content, tag, **kwargs)`
    type: info

Renders an arbitrary tag. Use it to produce dynamic wrappers depending on
condition. If tag name is empty, conent will be printed as-is, without a
wrapper.

```django
{{ ui.util.tag(
    "Hello world",
    "span" if inline_tag else "div",
    attrs={"class": "wrapper"}) }}
```

///

/// details | `ui.util.keep_item(category, key, value)` and `ui.util.pop_items(category, key=None)`
    type: info

`keep_item` store items in UI storage. Similar to `h.flash_success`, but for
arbitrary data.

`pop_items` retrieve and remove items from UI storage. Similar to
`h.get_flashed_messages`, but for arbitrary data.

///


/// admonition | Example
    type: example

```django
{%- macro button_group(items) -%}
    <div {{ ui.util.attrs(kwargs) }} class="btn-group">
        {{ ui.util.map(ui.button, items, on={"click": "alert(42)"}) }}
    </div>
{%- endmacro %}

{# Using call with util.call #}
{% call ui.util.call(ui.button, style="primary", attrs={"id": ui.util.id()}) %}
    {{ ui.icon("home") }}
    Click me!
{% endcall %}
```

///

### Accessibility Considerations

When implementing theme components, ensure proper accessibility support by using appropriate ARIA attributes and semantic HTML:

```django
{%- macro button(content, href, type="button", style="primary") -%}
    {%- if href -%}
        <a {{ ui.util.attrs(kwargs, {"aria-label": content}) }}
           href="{{ href }}"
           class="btn btn-{{ style }}">
            {{ content }}
        </a>
    {%- else -%}
        <button {{ ui.util.attrs(kwargs, {"aria-label": content}) }}
                type="{{ type }}"
                class="btn btn-{{ style }}">
            {{ content }}
        </button>
    {%- endif %}
{%- endmacro %}

{%- macro input(content, name, id, label, value, required, placeholder, type="text", errors=[]) -%}
    {%- set field_id = id or (name and ("field-" ~ name)) or (label and ui.util.id()) or "" -%}
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

Once a theme is activated by setting its name as a value for `ckan.ui.theme`
config option, UI macros can be used in templates:

```jinja
{{ ui.button("Click Me", style="primary", type="button") }}
{{ ui.card("Card content here", title="My Card") }}
{{ ui.alert("Success message", style="success") }}
{{ ui.link("Visit CKAN", href="https://ckan.org", blank=true) }}
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
# List available components for the current theme
ckan theme component list

# Analyze UI components and their implementations.
# Specify component names to reduce output
ckan theme component analyze
ckan theme component analyze link button card

# Check if a theme implements all known UI components
ckan theme component check
```

### Template Management
```bash
# List template files
ckan theme template list

# Verify that a theme contains all required templates
ckan theme template check

# Analyze theme templates and their structure
ckan theme template analyze
ckan theme template analyze header.html package/search.html
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
```

## Configuration

To use a theme, configure it in your CKAN configuration:

```ini
ckan.plugins = ... theming your_theme_plugin
ckan.ui.theme = your_theme
```

## Reference Implementation

The `bare` theme in this extension serves as a reference implementation showing
the minimal structure needed for a theme. It can be used as a starting point
for building new themes by running:

```bash
ckan theme create mytheme
```

This creates a new theme based on the bare theme structure with all required components.
{%endraw%}
