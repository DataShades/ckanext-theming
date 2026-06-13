{% from "_macros.html" import parameters_table %}
{% raw %}
# Layout

Layout components provide the structural foundation for your pages. They help
organize content into rows, columns, sections, and containers, ensuring a
consistent and responsive user interface across different screen sizes.

## Container

The `container` component is the most basic layout element. It wraps your
content and provides a maximum width, centering it on the page.

/// admonition | Usage Example
    type: example

```django
<!-- Basic container -->
{{ ui.container("Content within a container") }}

<!-- Fluid container (full width) -->
{{ ui.container("Full-width content", fluid=true) }}
```
///
{% endraw %}
{{parameters_table(component_ref.container, 'container')}}
{% raw %}
## Grid System

The grid system allows you to create complex, responsive layouts using rows and
columns.

### Grid

The `grid` component serves as a container for `row` elements (or directly for
`column` elements depending on the theme).
{% endraw %}
{{parameters_table(component_ref.grid, 'grid')}}
{% raw %}
### Row

The `row` component wraps `column` elements and controls their alignment and
spacing.
{% endraw %}
{{parameters_table(component_ref.row, 'row')}}
{% raw %}
### Column

The `column` component defines the width of your content within a row. It supports
responsive spans for different breakpoints.

/// admonition | Usage Example
    type: example

```django
{%- call ui.util.call(ui.grid) -%}
    {%- call ui.util.call(ui.row) -%}
        {{ ui.column("1/3 on medium screens", span={"md": 4}) }}
        {{ ui.column("2/3 on medium screens", span={"md": 8}) }}
    {%- endcall %}
{%- endcall %}
```
///
{% endraw %}
{{parameters_table(component_ref.column, 'column')}}
{% raw %}
## Sections

Sections help divide your page into logical areas.

### Section

A generic section wrapper for grouping related content.

```django
{{ ui.section("This is a section of content", title="this is a title") }}
```

{% endraw %}
{{parameters_table(component_ref.section, 'section')}}
{% raw %}
### Sidebar Section

Specifically designed for content in sidebars, often with different styling or
collapsible behavior.

```django
{{ ui.sidebar_section("This is a sidebar section", title="Sidebar Title") }}
```

{% endraw %}
{{parameters_table(component_ref.sidebar_section, 'sidebar_section')}}
{% raw %}
## Content Containers

These components provide specific ways to wrap and present groups of related
information.

### Card

The `card` component provides a self-contained container for related
content, typically featuring a header, body, and optional footer.

/// admonition | Usage Example
    type: example

```django
{{ ui.card("Dataset description goes here", title="Dataset Title", footer="Updated: 2023-01-01") }}
```
///
{% endraw %}
{{parameters_table(component_ref.card, 'card')}}
{% raw %}
### Accordion

The `accordion` component creates collapsible content sections. Use
`accordion_wrapper` to group multiple accordions together.

/// admonition | Usage Example
    type: example

```django
{%- call ui.util.call(ui.accordion_wrapper) -%}
    {{ ui.accordion("Content 1", title="Section 1") }}
    {{ ui.accordion("Content 2", title="Section 2") }}
{%- endcall %}
```
///
{% endraw %}
{{parameters_table(component_ref.accordion, 'accordion')}}
{% raw %}
### List

The `list` component provides a container for collections of `list_item`
components.

```django
{%- call ui.util.call(ui.list) -%}
    {{ ui.list_item("First item") }}
    {{ ui.list_item("Second item") }}
    {{ ui.list_item("Third item") }}
{%- endcall %}
```


{% endraw %}
{{parameters_table(component_ref.list, 'list')}}
{{parameters_table(component_ref.list_item, 'list_item')}}
{% raw %}
### Button Group

Groups related buttons together, providing visual cohesion.

```django
{%- call ui.util.call(ui.button_group) -%}
    {{ ui.button("Save", style="primary") }}
    {{ ui.button("Cancel", style="secondary") }}
{%- endcall %}
```


{% endraw %}
{{parameters_table(component_ref.button_group, 'button_group')}}
{% raw %}
## Visual Helpers

### Heading

Creates page and section headings (h1-h6).

```django
{{ ui.heading("This is a heading", level=2) }}
```


{% endraw %}
{{parameters_table(component_ref.heading, 'heading')}}
{% raw %}
### Divider

Creates a visual separator between content sections.

```django
{{ ui.divider() }}
```

{% endraw %}
{{parameters_table(component_ref.divider, 'divider')}}
