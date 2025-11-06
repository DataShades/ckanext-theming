# Data

## `table_block`

Renders a table.

### Arguments

*   `striped` (boolean): Whether to stripe the table rows. Defaults to `false`.
*   `bordered` (boolean): Whether to add borders to the table. Defaults to `false`.

## `table_head_block`

Renders the table header.

### Arguments

None

## `table_body_block`

Renders the table body.

### Arguments

None

## `table_row_block`

Renders a table row.

### Arguments

None

## `table_row`

Renders a table row.

### Arguments

*   `columns` (list): A list of table cells.
*   `heading` (boolean): Whether the row is a header row. Defaults to `false`.

## `table_cell`

Renders a table cell.

### Arguments

*   `content` (string): The content of the table cell.
*   `heading` (boolean): Whether the cell is a header cell. Defaults to `false`.

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
