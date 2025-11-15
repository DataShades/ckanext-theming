# Data

Data macros provide components for displaying and organizing information in structured formats. These components handle tabular data, lists, statistics, and other data visualization needs with proper accessibility and consistent styling.

## `table`

Renders a complete table element with optional styling features like striped rows and borders. Provides a semantic HTML table structure with theme-appropriate styling and accessibility features.

**Use Cases:**

- Data grids and reports
- Comparison tables
- Product listings
- User data displays
- Financial reports
- Analytics dashboards
- Schedule or calendar displays

**Usage Context:**

Use when you need to display structured data in a tabular format where rows and columns represent related information.

**Example:**

```
{% call ui.util.call(ui.table_block, striped=true, bordered=true) %}
    {% call ui.util.call(ui.table_head) %}
        {% call ui.util.call(ui.table_row) %}
            {{ ui.table_cell("Name", heading=true) }}
            {{ ui.table_cell("Email", heading=true) }}
            {{ ui.table_cell("Status", heading=true) }}
        {% endcall %}
    {% endcall %}
    {% call ui.util.call(ui.table_body) %}
        {% call ui.util.call(ui.table_row) %}
            {{ ui.table_cell("John Doe") }}
            {{ ui.table_cell("john@example.com") }}
            {{ ui.table_cell("Active") }}
        {% endcall %}
    {% endcall %}
{% endcall %}
```

**Recommendations:**

- Use appropriate styling options for readability (striped for dense data, bordered for clarity)
- Different themes provide various table styles (Bootstrap: .table, .table-striped, Tailwind: divide-y, Bulma: .table)
- Ensure proper header structure with table_head_block and table_cell(heading=true)
- Include proper scope attributes for accessibility (automatically handled by theme)
- Consider responsive behavior for mobile viewing (horizontal scrolling or stacking)

## `table_head`

Renders the table header section (`<thead>`) to contain header rows. Provides semantic structure for table headers and proper accessibility markup.

**Use Cases:**

- Table header sections
- Column labeling
- Data category identification
- Header row grouping
- Column sorting indicators

**Usage Context:**

Use to wrap the header row(s) of a table to provide proper semantic structure and accessibility features.

**Example:**

```
{% call ui.util.call(ui.table_head) %}
    {% call ui.util.call(ui.table_row) %}
        {{ ui.table_cell("Name", heading=true) }}
        {{ ui.table_cell("Email", heading=true) }}
        {{ ui.table_cell("Status", heading=true) }}
    {% endcall %}
{% endcall %}
```

**Recommendations:**

- Always use with table_body_block for proper structure
- Different themes may apply specific styling (Bootstrap: .thead-light, Tailwind: bg-gray-50, Bulma: .table th is-light)
- Use heading=true for table_cell elements inside the header
- Provides proper ARIA associations for screen readers

## `table_body`

Renders the table body section (`<tbody>`) to contain data rows. Provides semantic structure for the main data content of the table with proper accessibility features.

**Use Cases:**

- Table data rows
- Dynamic content display
- Scrollable table content
- Data pagination
- Row-level interactions

**Usage Context:**

Use to wrap the data rows of a table to provide proper semantic structure and styling for the main content.

**Example:**

```
{% call ui.util.call(ui.table_body) %}
    {% call ui.util.call(ui.table_row) %}
        {{ ui.table_cell("Product A") }}
        {{ ui.table_cell("$29.99") }}
        {{ ui.table_cell("In Stock") }}
    {% endcall %}
    {% call ui.util.call(ui.table_row) %}
        {{ ui.table_cell("Product B") }}
        {{ ui.table_cell("$39.99") }}
        {{ ui.table_cell("Out of Stock") }}
    {% endcall %}
{% endcall %}
```

**Recommendations:**

- Always pair with table_head_block for complete structure
- Different themes may provide different styling (Bootstrap: default body styling, Tailwind: divide-y, Bulma: .table td)
- Can be made scrollable for large datasets
- Properly associated with headers for screen reader accessibility

## `table_row`

Renders a complete table row with cells from a list of content. Provides a convenient shorthand for creating table rows from data arrays, useful for programmatic table generation.

**Use Cases:**

- Programmatic table generation
- Data-driven tables
- CSV import displays
- Dynamic row creation
- Template-driven content display

**Usage Context:**

Use when you have data in an array format that you want to convert to a table row without manually creating each cell.

**Example:**

```
{{ ui.table_row(cells=["Name", "Email", "Date"], heading=true) }}

{{ ui.table_row(ui.table_cell("John Doe") ~ ui.table_cell("john@example.com") ~ ui.table_cell("2024-01-01")) }}

{% call ui.util.call(ui.table_row) %}
    {{ ui.table_cell("Jane Smith") }}
    {{ ui.table_cell("jane@example.com") }}
    {{ ui.table_cell("2024-01-02") }}
{% endcall %}
```

**Recommendations:**

- Useful for dynamic table generation
- Use heading=true for header rows
- Different themes will apply styling based on parent table configuration
- Ensure consistent data structure across rows

## `table_cell`

Renders a table cell (`<td>` or `<th>`) with content and optional header designation. Provides the basic building block for table content with proper semantic structure and accessibility features.

**Use Cases:**

- Data cells in tables
- Header cells
- Action cells
- Empty state cells
- Rich content cells

**Usage Context:**

Use as the fundamental unit of table content, either for data cells or header cells.

**Example:**

```
{{ ui.table_cell("Regular Data Cell") }}
{{ ui.table_cell("Header Cell", heading=true) }}
```

**Recommendations:**

- Use heading=true for column and row headers
- Different themes provide various cell styling (Bootstrap: .table-cell, Tailwind: px-6 py-4, Bulma: .table td/th)
- Consider content length and alignment
- Properly associated with headers and rows for accessibility

## `list_group`

Renders a list group.

### Arguments

*   `items` (list): A list of items to display in the list group.

## `definition_list`

Renders a definition list.

### Arguments

*   `items` (list): A list of tuples containing term-definition pairs.

## `stat`

Displays a statistic value with label.

### Arguments

*   `label` (string): The label for the statistic.
*   `value` (string): The value of the statistic.
*   `icon` (string): An optional icon to display with the statistic. Defaults to `None`.

## `chart`

Embeds a chart element.

### Arguments

*   `type` (string): The type of chart to render.
*   `data` (any): The data for the chart.
*   `options` (any): Chart options. Defaults to `None`.

## `code_block`

Renders a code block.

### Arguments

*   `content` (string): The code content to display.
*   `language` (string): The programming language for syntax highlighting. Defaults to "text".
