# Data

Data components are designed to present structured information in a clear and
accessible way. They handle complex data structures like tables, charts, and
other data visualization needs. Many of these components work together in
hierarchical relationships - for example, [`table`][] components work with
[`table_head`][table-head], [`table_body`][table-body],
[`table_row`][table-row], and [`table_cell`][table-cell] components to create
complete data displays.

## Chart

The [`chart`][] component displays charts and graphs that visualize data in
various formats such as bar charts, line graphs, pie charts, and other
visualization types. Charts are essential for making complex data more
understandable and revealing patterns, trends, and relationships that might not
be apparent in raw data.

Chart components handle various aspects of data visualization including
responsive sizing, accessibility features, and different chart types. They
provide a consistent interface for displaying data visualizations while
allowing themes to implement their preferred charting libraries and visual
styles. The component ensures that charts remain accessible to users with
different needs and work well across different devices and screen sizes.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic chart component -->
{{ ui.chart(data=[[1,2,3], [3,2,4]], type="bar") }}
{{ ui.chart(data=[[1,2,3], [3,2,4]], type="line") }}
{{ ui.chart(data=[1,2,3], type="pie") }}
```
///

| Parameter | Type   | Default | Description                                     |
|-----------|--------|---------|-------------------------------------------------|
| `content` | string | -       | The content to display.                         |
| `data`    | list   | -       | The data to visualize in the chart.             |
| `labels`  | list   | -       | Labels for datasets.                            |
| `type`    | string | -       | The type of chart (e.g., "bar", "line", "pie"). |

/// details | Theme-Specific Parameters
    type: tip

- `responsive` (bool): Whether the chart is responsive
- `animation` (bool): Whether to use animations
- `legend` (bool): Whether to show legend
///

## Code

The [`code`][] component displays code blocks with appropriate formatting, syntax
highlighting, and accessibility features. Code components are important for
documentation, technical content, and any situation where users need to view or
copy code snippets.

Code components handle various aspects of code display including syntax
highlighting for different programming languages, line numbering when
appropriate, and proper formatting that preserves code structure. The component
ensures code remains readable and accessible while providing features like
copy-to-clipboard functionality that enhance the user experience for technical
content.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic code component -->
{{ ui.code("print('Hello World')") }}
```
///

| Parameter  | Type   | Default | Description                                   |
|------------|--------|---------|-----------------------------------------------|
| `content`  | string | -       | The code content to display.                  |
| `language` | string | -       | Programming language for syntax highlighting. |

/// details | Theme-Specific Parameters
    type: tip

- `line_numbers` (bool): Whether to show line numbers
- `wrap_lines` (bool): Whether to wrap long lines
- `copy_button` (bool): Whether to show copy button
- `dedent` (bool): Remove common leading whitespaces
///

## Definition List

The [`definition_list`][definition-list] component displays definition lists
that present key-value pairs in a structured format. Definition lists are
particularly useful for displaying metadata, configuration information, or any
content that consists of terms and their corresponding definitions or values.

Definition list components handle proper semantic markup and consistent styling
for terms and their definitions. They provide clear visual separation between
different term-definition pairs and ensure the relationship between terms and
definitions remains clear. This component is especially valuable for displaying
structured information like dataset metadata, user profiles, or system
configuration details.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic definition list -->
{{ ui.definition_list([
    ["Hello", "Praesent augue."],
    ["World", "Proin quam nisl, tincidunt et, mattis eget, convallis nec, purus."]
]) }}
```
///

| Parameter | Type                  | Default | Description                                    |
|-----------|-----------------------|---------|------------------------------------------------|
| `items`   | list[tuple[str, str]] | -       | The content to display in the definition list. |

/// details | Theme-Specific Parameters
    type: tip

- `striped` (bool): Whether to use striped styling
- `bordered` (bool): Whether to show borders
- `compact` (bool): Whether to use compact spacing
///

## Table

The [`table`][] component creates table containers that organize data in rows and
columns, providing a structured format for displaying related
information. Tables are fundamental for presenting tabular data in an
organized, scannable format that allows users to compare values and identify
patterns.

Table components work with several related components to create complete table
structures: [`table_head`][table-head] for headers, [`table_body`][table-body]
for main content, [`table_row`][table-row] for individual rows, and
[`table_cell`][table-cell] for individual data cells. This component provides
the overall container structure and handles responsive behavior to ensure
tables remain usable across different devices.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic table component -->
{%- call ui.util.call(ui.table) -%}
    {{ ui.table_head(ui.table_row(ui.util.map(ui.table_cell, ["Header 1", "Header 2"]))) }}

    {%- call ui.util.call(ui.table_body) -%}
        {%- call ui.util.call(ui.table_row) -%}
            {{ ui.table_cell("Cell 1") }}
            {{ ui.table_cell("Cell 2") }}
        {%- endcall %}
    {%- endcall %}
{%- endcall %}

<!-- Table with borders and stripes -->
{%- call ui.util.call(ui.table, bordered=true, striped=true) -%}
    {{ ui.table_head(ui.table_row(ui.table_cell("Header 1") ~ ui.table_cell("Header 2"))) }}

    {%- call ui.util.call(ui.table_body) -%}
        {{ ui.table_row(ui.table_cell("Cell 1") ~ ui.table_cell("Cell 2")) }}
    {%- endcall %}
{%- endcall %}

```
///

| Parameter | Type   | Default | Description                                                          |
|-----------|--------|---------|----------------------------------------------------------------------|
| `content` | string | -       | The content to display in the table (typically table head and body). |

/// admonition | Relationship
    type: info

The [`table`][] component works with [`table_head`][table-head], [`table_body`][table-body], [`table_row`][table-row], and
[`table_cell`][table-cell] components to create complete table structures. The table provides
the container, while the other components provide the internal structure.

///

## Table Body

The [`table_body`][table-body] component defines the main content area of
tables, containing the primary data rows that display the actual
information. Table body components provide semantic structure and appropriate
styling for the main content of data tables, distinguishing it from header and
footer sections.

Table body components work within [`table`][] containers and contain multiple
[`table_row`][table-row] elements. They handle consistent styling for data rows
and ensure proper visual hierarchy within the overall table structure. The
component ensures that data rows maintain appropriate spacing and styling that
makes the information easy to scan and understand.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic table body component -->
{%- call ui.util.call(ui.table) -%}
    {%- call ui.util.call(ui.table_body) -%}
        {{ ui.table_row(ui.table_cell("Cell 1") ~ ui.table_cell("Cell 2")) }}
    {%- endcall %}
{%- endcall %}
```
///

| Parameter | Type   | Default | Description                                                      |
|-----------|--------|---------|------------------------------------------------------------------|
| `content` | string | -       | The content to display in the table body (typically table rows). |

/// admonition | Relationship
    type: info

The [`table_body`][table-body] component works within [`table`][] containers
and contains [`table_row`][table-row] elements. While the table provides the
overall structure, the body contains the main data content.

///

## Table Cell

The [`table_cell`][table-cell] component creates individual cells within table
rows, containing the actual data values or content. Table cells are the
fundamental building blocks of table data, providing the containers for
individual pieces of information within the table structure.

Table cell components handle various aspects of cell display including
appropriate sizing, alignment, and responsive behavior. They can contain
various types of content including text, links, images, or other components,
making them flexible for different data presentation needs. The component
ensures cells maintain proper spacing and alignment within the overall table
structure.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic table cell component -->
{%- call ui.util.call(ui.table) -%}
    {%- call ui.util.call(ui.table_row) -%}
        {{ ui.table_cell("Cell 1", header=true) }}
        {{ ui.table_cell("Cell 2") }}
    {%- endcall %}
{%- endcall %}
```
///

| Parameter | Type   | Default | Description                               |
|-----------|--------|---------|-------------------------------------------|
| `content` | string | -       | The content to display in the table cell. |
| `header`  | bool   | -       | Whether this cell is a header cell.       |

/// details | Theme-Specific Parameters
    type: tip

- `align` (string): Text alignment (e.g., "left", "center", "right")
- `nowrap` (bool): Whether to prevent text wrapping
- `colspan` (int): Number of columns to span
- `rowspan` (int): Number of rows to span
///

/// admonition | Relationship
    type: info

The [`table_cell`][table-cell] component works within [`table_row`][table-row]
elements to create individual data cells. While rows provide the horizontal
structure, cells provide the individual data containers.

///

## Table Head

The [`table_head`][table-head] component defines the header section of tables,
containing column titles and other identifying information that helps users
understand the data structure. Table headers are crucial for accessibility and
usability, providing context for the data in each column.

Table head components work within [`table`][] containers and typically contain
[`table_row`][table-row] elements with header cells. They provide semantic
structure and appropriate styling that distinguishes header information from
main content. The component ensures headers remain visible and accessible,
often implementing features like sticky headers for large tables.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic table head component -->
{%- call ui.util.call(ui.table) -%}
    {{ ui.table_head(ui.table_row(ui.table_cell("Header 1") ~ ui.table_cell("Header 2"))) }}
{%- endcall %}
```
///

| Parameter | Type   | Default | Description                                                       |
|-----------|--------|---------|-------------------------------------------------------------------|
| `content` | string | -       | The content to display in the table head (typically header rows). |

/// details | Theme-Specific Parameters
    type: tip

- `sticky` (bool): Whether to make the header sticky
///

/// admonition | Relationship
    type: info

The [`table_head`][table-head] component works within [`table`][] containers
and contains header rows. While the table provides the overall structure, the
head provides the identifying column information.

///

## Table Row

The [`table_row`][table-row] component creates individual rows within tables,
organizing related data across multiple columns. Table rows are essential for
maintaining the structural integrity of tabular data and ensuring related
information remains properly aligned.

Table row components work within [`table_body`][table-body] or
[`table_head`][table-head] sections and contain multiple
[`table_cell`][table-cell] elements. They handle consistent styling and spacing
that makes the table structure clear and readable. The component ensures rows
maintain proper alignment and spacing within the overall table structure.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic table row component -->
{%- call ui.util.call(ui.table) -%}
    {%- call ui.util.call(ui.table_row) -%}
        {{ ui.table_cell("Cell 1") }}
        {{ ui.table_cell("Cell 2") }}
    {%- endcall %}
{%- endcall %}
```
///

| Parameter | Type   | Default | Description                                                      |
|-----------|--------|---------|------------------------------------------------------------------|
| `content` | string | -       | The content to display in the table row (typically table cells). |

/// admonition | Relationship
    type: info

The [`table_row`][table-row] component works within [`table_body`][table-body]
or [`table_head`][table-head] sections and contains [`table_cell`][table-cell]
elements. While the body or head provides the section context, rows provide the
horizontal organization.

///
