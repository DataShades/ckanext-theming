# Container

## `accordion_wrapper`

Wraps an accordion component.

### Arguments

*   `content` (string): accordion items.

## `accordion_item`

Creates a single item in an accordion.

### Arguments

*   `title` (string): title of the accordion item.
*   `open` (boolean): Whether the accordion item is initially open. Defaults to `false`.
*   `content` (string): content of the accordion item, passed via the `caller()` block.

## `card`

Renders a card component.

### Arguments

*   `content` (string): content of the card.
*   `title` (string): title of the card.
*   `footer` (string): footer content of the card.
*   `img` (string): image source URL for the card.
*   `href` (string): URL to link to when the card is clicked.

## `column`

Creates a single column inside the grid.

### Arguments

*   `content` (string): content of the column.

## `container`

Creates a container block.

### Arguments

*   `content` (string): content of the container.
*   `fluid` (boolean): Whether the container should be fluid. Defaults to `false`.

## `grid`

Creates a grid layout block.

### Arguments

*   `content` (string): content of the grid.
*   `columns` (integer): number of columns in the grid.

## `panel`

Creates a panel block.

### Arguments

*   `content` (string): content of the panel.
*   `title` (string): title of the panel.

## `row`

Creates a row block.

### Arguments

*   `content` (string): content of the row.

## `section`

Creates a section block.

### Arguments

*   `content` (string): content of the section.
