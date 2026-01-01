# Data Components

Data components handle the display and presentation of structured data, tables, charts, and other data visualization elements.

## Overview

Data components are designed to present structured information in a clear and accessible way. They handle complex data structures like tables, charts, and other data visualization needs. Many of these components work together in hierarchical relationships - for example, `table` components work with `table_head`, `table_body`, `table_row`, and `table_cell` components to create complete data displays.

## Chart Component

The `chart` component displays charts and graphs that visualize data in various formats such as bar charts, line graphs, pie charts, and other visualization types. Charts are essential for making complex data more understandable and revealing patterns, trends, and relationships that might not be apparent in raw data.

Chart components handle various aspects of data visualization including responsive sizing, accessibility features, and different chart types. They provide a consistent interface for displaying data visualizations while allowing themes to implement their preferred charting libraries and visual styles. The component ensures that charts remain accessible to users with different needs and work well across different devices and screen sizes.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic chart component -->
{{ ui.chart(data=chart_data, type="bar") }}

<!-- Chart with attributes -->
{{ ui.chart(data=chart_data, type="line", attrs={"class": "data-chart"}) }}
```
///

## Code Component

The `code` component displays code blocks with appropriate formatting, syntax highlighting, and accessibility features. Code components are important for documentation, technical content, and any situation where users need to view or copy code snippets.

Code components handle various aspects of code display including syntax highlighting for different programming languages, line numbering when appropriate, and proper formatting that preserves code structure. The component ensures code remains readable and accessible while providing features like copy-to-clipboard functionality that enhance the user experience for technical content.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic code component -->
{{ ui.code("print('Hello World')") }}

<!-- Code with attributes -->
{{ ui.code("function test() { return true; }", attrs={"class": "code-block"}) }}
```
///

## Definition List Component

The `definition_list` component displays definition lists that present key-value pairs in a structured format. Definition lists are particularly useful for displaying metadata, configuration information, or any content that consists of terms and their corresponding definitions or values.

Definition list components handle proper semantic markup and consistent styling for terms and their definitions. They provide clear visual separation between different term-definition pairs and ensure the relationship between terms and definitions remains clear. This component is especially valuable for displaying structured information like dataset metadata, user profiles, or system configuration details.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic definition list -->
{{ ui.definition_list() }}

<!-- Definition list with attributes -->
{{ ui.definition_list(attrs={"class": "metadata-list"}) }}
```
///

## Table Component

The `table` component creates table containers that organize data in rows and columns, providing a structured format for displaying related information. Tables are fundamental for presenting tabular data in an organized, scannable format that allows users to compare values and identify patterns.

Table components work with several related components to create complete table structures: `table_head` for headers, `table_body` for main content, `table_row` for individual rows, and `table_cell` for individual data cells. This component provides the overall container structure and handles responsive behavior to ensure tables remain usable across different devices.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic table component -->
{{ ui.table(ui.table_head(ui.table_row(ui.table_cell("Header 1") ~ ui.table_cell("Header 2"))) ~ ui.table_body(ui.table_row(ui.table_cell("Cell 1") ~ ui.table_cell("Cell 2")))) }}

<!-- Table with attributes -->
{{ ui.table(content, attrs={"class": "data-table"}) }}
```
///

/// admonition | Relationship
    type: info

The `table` component works with `table_head`, `table_body`, `table_row`, and `table_cell` components to create complete table structures. The table provides the container, while the other components provide the internal structure.
///

## Table Body Component

The `table_body` component defines the main content area of tables, containing the primary data rows that display the actual information. Table body components provide semantic structure and appropriate styling for the main content of data tables, distinguishing it from header and footer sections.

Table body components work within `table` containers and contain multiple `table_row` elements. They handle consistent styling for data rows and ensure proper visual hierarchy within the overall table structure. The component ensures that data rows maintain appropriate spacing and styling that makes the information easy to scan and understand.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic table body component -->
{{ ui.table_body(ui.table_row(ui.table_cell("Data 1") ~ ui.table_cell("Data 2"))) }}

<!-- Table body with attributes -->
{{ ui.table_body(content, attrs={"class": "table-body"}) }}
```
///

/// admonition | Relationship
    type: info

The `table_body` component works within `table` containers and contains `table_row` elements. While the table provides the overall structure, the body contains the main data content.
///

## Table Cell Component

The `table_cell` component creates individual cells within table rows, containing the actual data values or content. Table cells are the fundamental building blocks of table data, providing the containers for individual pieces of information within the table structure.

Table cell components handle various aspects of cell display including appropriate sizing, alignment, and responsive behavior. They can contain various types of content including text, links, images, or other components, making them flexible for different data presentation needs. The component ensures cells maintain proper spacing and alignment within the overall table structure.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic table cell component -->
{{ ui.table_cell("Cell content") }}

<!-- Table cell with attributes -->
{{ ui.table_cell("Styled cell", attrs={"class": "data-cell"}) }}
```
///

/// admonition | Relationship
    type: info

The `table_cell` component works within `table_row` elements to create individual data cells. While rows provide the horizontal structure, cells provide the individual data containers.
///

## Table Head Component

The `table_head` component defines the header section of tables, containing column titles and other identifying information that helps users understand the data structure. Table headers are crucial for accessibility and usability, providing context for the data in each column.

Table head components work within `table` containers and typically contain `table_row` elements with header cells. They provide semantic structure and appropriate styling that distinguishes header information from main content. The component ensures headers remain visible and accessible, often implementing features like sticky headers for large tables.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic table head component -->
{{ ui.table_head(ui.table_row(ui.table_cell("Header 1") ~ ui.table_cell("Header 2"))) }}

<!-- Table head with attributes -->
{{ ui.table_head(content, attrs={"class": "table-header"}) }}
```
///

/// admonition | Relationship
    type: info

The `table_head` component works within `table` containers and contains header rows. While the table provides the overall structure, the head provides the identifying column information.
///

## Table Row Component

The `table_row` component creates individual rows within tables, organizing related data across multiple columns. Table rows are essential for maintaining the structural integrity of tabular data and ensuring related information remains properly aligned.

Table row components work within `table_body` or `table_head` sections and contain multiple `table_cell` elements. They handle consistent styling and spacing that makes the table structure clear and readable. The component ensures rows maintain proper alignment and spacing within the overall table structure.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic table row component -->
{{ ui.table_row(ui.table_cell("Cell 1") ~ ui.table_cell("Cell 2")) }}

<!-- Table row with attributes -->
{{ ui.table_row(content, attrs={"class": "table-row"}) }}
```
///

/// admonition | Relationship
    type: info

The `table_row` component works within `table_body` or `table_head` sections and contains `table_cell` elements. While the body or head provides the section context, rows provide the horizontal organization.
///
