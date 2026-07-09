
# Component Library

The component library is the heart of the theming system. It provides a set of
high-level, semantic building blocks that you use to construct your user
interface.

Instead of wrestling with raw HTML and CSS classes, you call these components
using Jinja2 macros. The active theme takes care of rendering the correct HTML
for its chosen CSS framework.

## How to use components

Most components follow a simple, predictable pattern.

### 1. Simple Content
For components that just take text or a simple string, pass it as the first
argument:

```django
{{ ui.button("Click Me") }}
{{ ui.alert("Success message", style="success") }}
```

### 2. Complex Content (Block Usage)
For more complex content (like nested HTML or other components), use the `ui.util.call` helper:

```django
{% call ui.util.call(ui.card, title="Dataset Info") %}
    <p>This is a <strong>very important</strong> dataset.</p>
    {{ ui.button("Download", href="/...") }}
{% endcall %}
```

!!! note

    Keep in mind that `ui.util.call` simply passes the block content into the first
    argument of the called component. The following two ways of rendering
    `something` are identical:

    ```django
    {{ ui.something("CONTENT", argument="value") }}

    {% call ui.util.call(ui.something, argument="value") -%}
        CONTENT
    {%- endcall %}
    ```


### 3. Entity-based Components
Some components are designed to work directly with CKAN's data objects (like
datasets, organizations, or users):

```django
{{ ui.package(package=dataset_dict) }}
{{ ui.user(user=user_dict) }}
```

## Key Benefits

**Semantic Code**: Your templates describe *what* an element is (a button, a card), not *how* it should look.

**Theme Interoperability**: Write your extension once, and it will look great on any theme that implements the standard library.

**Clean Templates**: Drastically reduce the amount of boilerplate HTML in your templates.

## Diving Deeper

While you can get very far with just the basics, the system offers powerful
features for advanced use cases:

- [Standard Parameter Values](../parameters.md): Learn about the consistent naming for sizes, styles, and directions.
- [HTML Attributes](#html-attributes): How to pass arbitrary data, aria, or event attributes.
- [Interactive Element Coordination](#interactive-element-coordination): Using unique IDs and handles for modals and popovers.

---

## Technical Details

### Parameter Handling

#### Named Arguments Convention

All arguments after the first content argument (if applicable) should be passed
by name. This approach provides flexibility for different themes to implement
their own variations of components with varying numbers of parameters:

```django
{{ ui.button("Save", style="primary", rounded=true, size="large") }}
{{ ui.input(type="text", placeholder="Enter text", required=true) }}
```

### Arbitrary Named Parameters

Every component accepts arbitrary named parameters. If a component doesn't know
how to handle a particular parameter, it will be ignored. This allows for
maximum flexibility when working with different themes:

```django
{{ ui.button("Submit", custom_param="ignored", style="primary") }}
```

## HTML Attributes

### Standard Attributes

HTML attributes can be passed via the `attrs` dictionary parameter:

```django
{{ ui.button("Submit",
    attrs={"disabled": true, "id": "submit-btn", "class": "custom-button"}
) }}
```

### Special Attribute Namespaces

Attributes from common namespaces (`data-`, `aria-`, `hx-`, and `on` event
handlers) can be passed either inside the `attrs` dictionary or via separate
parameters:

```django
{{ ui.button("Submit",
    attrs={"data-role": "form-submitter"},
    aria={"labelledby": "label-id"},
    data={"module": "autocomplete"},
    hx={"boost": "true"},
    on={"click": "handleSubmit()"}
) }}
```

When using separate parameters, they are automatically prefixed with the
appropriate namespace (`data-`, `aria-`, `hx-`) or treated as event handlers
(`on`). Attributes specified via separate parameters have higher precedence
than ones from `attrs` dictionary.

### Attribute Precedence

Attributes passed via arguments have higher precedence than attributes defined
in the macro implementation. This allows you to override default behavior:

```django
{# This will use "custom-class" instead of the theme's default button classes #}
{{ ui.button("Text", attrs={"class": "custom-class"}) }}
```

### Custom CSS Classes

If you want to *add* a class to the default ones instead of replacing them
entirely, use the `_extra_class` parameter:

```django
{# This will add "my-class" to the button's class list #}
{{ ui.button("Text", _extra_class="my-class") }}
```

---

## Block Elements and Complex Content

### Inline vs Block Usage

Components that accept content as their first parameter can be used in two ways:

1. **Inline usage** for simple content:
```django
{{ ui.button("Simple Button") }}
```

2. **Block usage** via `ui.util.call` for complex content:
```django
{% call ui.util.call(ui.button, style="primary") %}
    {{ ui.icon("search") }}
    Search Datasets
{% endcall %}
```

The `ui.util.call` function allows passing complex content (including nested
components) into elements that don't have a `caller()` block in their
implementation.

!!! warning "Using `caller()`"


    When creating custom components you can use `caller()`, but always provide
    implementation that does not require it. This guarantees that all
    implementations of the component across different themes will not break when
    using safe way of calling via inline expression `ui.<component>` and via block
    call `ui.util.call(ui.<component>)`.

    ```django
    {% macro something(content) %}
        {% if content %}
            {{ content }}
        {% elif caller %}
            {{ caller() }}
        {% endif %}
    {% endmacro %}
    ```



### Mapping Over Collections

Multiple items can be processed and concatenated using `ui.util.map`:

```django
{# Renders an icon for each item in the list #}
{{ ui.util.map(ui.icon, ["search", "home", "user"]) }}

{# More complex example with additional parameters #}
{{ ui.util.map(ui.button, ["Save", "Cancel", "Delete"], style="secondary") }}
```

Alternatively, you can concatenate components as Jinja2 strings:

```django
{{ ui.icon("search") ~ ui.icon("home") ~ ui.icon("user") }}
```

## Interactive Element Coordination

### Handle Components

Handle components (like modal handles, dialog handles, etc.) are typically
connected to their corresponding interactive elements via matching `id`
parameters:

```django
{# Create a modal handle #}
{{ ui.modal_handle("Open Modal", id="my-modal") }}

{# Elsewhere, create the corresponding modal #}
{{ ui.modal("Modal content", id="my-modal") }}
```

### Unique ID Generation

To guarantee ID uniqueness, use the `ui.util.id()` helper instead of hardcoding IDs:

```django
{# Generate a random unique ID with optional prefix #}
{% set modal_id = ui.util.id(prefix="modal-") %}
{{ ui.modal_handle("Open Modal", id=modal_id) }}
{{ ui.modal("Content", id=modal_id) }}

{# Generate the same ID for a specific value #}
{{ ui.modal_handle("Open Modal", id=ui.util.id("my-specific-modal")) }}
{{ ui.modal("Content", id=ui.util.id("my-specific-modal")) }}
```

Using `ui.util.id()` with a specific value is useful when you have a unique
attribute of the rendered entity that contains characters not allowed in HTML
ID attributes, allowing you to obfuscate the value in a reproducible manner.

## Utility Functions

### Date and Time

Current datetime can be obtained via `ui.util.now()`:

```django
{{ ui.datetime(ui.util.now(), date_format="%Y-%m-%d") }}
```

### Request-Scoped Data Storage

Data can be stored during a request using `ui.util.keep_item()` and retrieved
later with `ui.util.pop_items()`:

```django
{# Store a notification message anywhere in the template #}
{{ ui.util.keep_item(
    "notifications",
    "welcome_msg",
    {"type": "info", "text": "Welcome!"}
) }}

{# Later, retrieve all notifications #}
{% set notifications = ui.util.pop_items("notifications") %}
{% for id, data in notifications.items() %}
    {{ ui.alert(data.text, style=data.type) }}
{% endfor %}
```

This pattern is particularly useful for "pushing" chunks of data (like toast
messages, alerts, or metadata) throughout templates without concerning yourself
about the actual rendering location, then collecting and rendering them
together at the appropriate place further in the layout.

## Icon Normalization

Icons can be normalized using `ui.util.icon()` which maps common icon names to
their corresponding names in the theme's icon set:

```django
{# Maps "search" to theme-specific icon name like "magnifying-glass" #}
{{ ui.icon(ui.util.icon("search")) }}
```

Note, this mapping is usually performed inside macro implementation and just
writing `{{ ui.icon("search") }}` should work in the same way.

## Best Practices

1. **Consistency**: Always pass content as the first positional argument when applicable
2. **Flexibility**: Use named arguments for all styling and behavioral parameters
3. **Accessibility**: Leverage `aria-*` attributes for accessibility
4. **Progressive Enhancement**: Use `hx-*` attributes for enhanced interactivity
5. **Unique IDs**: Use `ui.util.id()` for generating unique identifiers
6. **Complex Content**: Use `ui.util.call()` for components with complex nested content

These patterns ensure that components remain flexible, accessible, and
consistent across different themes while maintaining the separation of content
structure from visual presentation.
