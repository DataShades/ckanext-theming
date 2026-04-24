# Component Library

Components in the theming system follow predictable patterns that make them
easy to use and understand. The system is built around Jinja2 macros that are
accessible through the `ui` global variable in templates.

### Content Components

Most components that accept content as their primary input follow a consistent
pattern where the first argument is the content, followed by named arguments
for styling and behavior:

```jinja
{{ ui.button("Click Me") }}
{{ ui.card("Card content here", title="My Card") }}
{{ ui.alert("Success message", style="success") }}
```

In this example, `"Click Me"` is the content passed positionally as the first
argument, while `style="success"` is passed as a named argument.

### Entity Components

Some components in the "content" category (such as `group`, `package`,
`resource`, `user`, etc.) work differently and typically accept structured data
objects rather than simple content strings:

```jinja
{{ ui.package(dataset_dict) }}
{{ ui.organization(org_dict) }}
{{ ui.user(user_dict) }}
```

## Parameter Handling

### Named Arguments Convention

All arguments after the first content argument (if applicable) should be passed
by name. This approach provides flexibility for different themes to implement
their own variations of components with varying numbers of parameters:

```jinja
{{ ui.button("Save", style="primary", rounded=true, size="large") }}
{{ ui.input(type="text", placeholder="Enter text", required=true) }}
```

### Arbitrary Named Parameters

Every component accepts arbitrary named parameters. If a component doesn't know
how to handle a particular parameter, it will be ignored. This allows for
maximum flexibility when working with different themes:

```jinja
{{ ui.button("Submit", custom_param="ignored", style="primary") }}
```

## HTML Attributes

### Standard Attributes

HTML attributes can be passed via the `attrs` dictionary parameter:

```jinja
{{ ui.button("Submit",
    attrs={"disabled": true, "id": "submit-btn", "class": "custom-button"}
) }}
```

### Special Attribute Namespaces

Attributes from common namespaces (`data-`, `aria-`, `hx-`, and `on` event
handlers) can be passed either inside the `attrs` dictionary or via separate
parameters:

```jinja
{{ ui.button("Submit",
    attrs={"data-module": "form-submitter"},
    aria={"labelledby": "label-id"},
    data={"module": "autocomplete"},
    hx={"boost": "true"},
    on={"click": "handleSubmit()"}
) }}
```

When using separate parameters, they are automatically prefixed with the
appropriate namespace (`data-`, `aria-`, `hx-`) or treated as event handlers
(`on`).

### Attribute Precedence

Attributes passed via arguments have higher precedence than attributes defined
in the macro implementation. This allows you to override default behavior:

```jinja
{# This will use "custom-class" instead of the theme's default button classes #}
{{ ui.button("Text", attrs={"class": "custom-class"}) }}
```

## Block Elements and Complex Content

### Inline vs Block Usage

Components that accept content as their first parameter can be used in two ways:

1. **Inline usage** for simple content:
```jinja
{{ ui.button("Simple Button") }}
```

2. **Block usage** via `ui.util.call` for complex content:
```jinja
{% call ui.util.call(ui.button, style="primary") %}
    {{ ui.icon("search") }}
    Search Datasets
{% endcall %}
```

The `ui.util.call` function allows passing complex content (including nested
components) into elements that don't have a `caller()` block in their
implementation.

### Mapping Over Collections

Multiple items can be processed and concatenated using `ui.util.map`:

```jinja
{# Renders an icon for each item in the list #}
{{ ui.util.map(ui.icon, ["search", "home", "user"]) }}

{# More complex example with additional parameters #}
{{ ui.util.map(ui.button, ["Save", "Cancel", "Delete"], style="secondary") }}
```

Alternatively, you can concatenate components as Jinja2 strings:

```jinja
{{ ui.icon("search") ~ ui.icon("home") ~ ui.icon("user") }}
```

## Interactive Element Coordination

### Handle Components

Handle components (like modal handles, tab handles, etc.) are typically
connected to their corresponding interactive elements via matching `id`
parameters:

```jinja
{# Create a modal handle #}
{{ ui.modal_handle("Open Modal", id="my-modal") }}

{# Elsewhere, create the corresponding modal #}
{{ ui.modal("Modal content", id="my-modal") }}
```

### Unique ID Generation

To guarantee ID uniqueness, use the `ui.util.id()` helper instead of hardcoding IDs:

```jinja
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

```jinja
{{ ui.datetime(ui.util.now(), date_format="%Y-%m-%d") }}
```

### Request-Scoped Data Storage

Data can be stored during a request using `ui.util.keep_item()` and retrieved
later with `ui.util.pop_items()`:

```jinja
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

Icons can be normalized using `ui.util.icon()` which maps commpon icon names to
their corresponding names in the theme's icon set:

```jinja
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
7. **Data Flow**: Use `ui.util.*_item()` functions for managing request-scoped data

These patterns ensure that components remain flexible, accessible, and
consistent across different themes while maintaining the separation of content
structure from visual presentation.
