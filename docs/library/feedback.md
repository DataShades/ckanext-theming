# Feedback

## `alert`

Displays an alert message.

### Arguments

*   `message` (string): The alert message to display.
*   `type` (string): The type of alert (e.g., "info", "success", "warning", "danger"). Defaults to "info".
*   `dismissible` (boolean): Whether the alert can be dismissed. Defaults to `True`.

## `toast`

Displays a toast notification.

### Arguments

*   `message` (string): The toast message to display.
*   `type` (string): The type of toast. Defaults to "info".

## `modal`

Renders a modal dialog.

### Arguments

*   `title` (string): The title of the modal. Defaults to `None`.
*   `body` (string): The content of the modal. Defaults to `None`.
*   `footer` (string): The footer content of the modal. Defaults to `None`.

## `tooltip`

Creates a tooltip element.

### Arguments

*   `text` (string): The text to display in the tooltip.

## `popover`

Creates a popover element.

### Arguments

*   `title` (string): The title of the popover. Defaults to `None`.
*   `content` (string): The content of the popover. Defaults to `None`.

## `progress`

Renders a progress bar.

### Arguments

*   `value` (integer): The current value of the progress bar.
*   `max` (integer): The maximum value of the progress bar. Defaults to 100.
*   `label` (string): An optional label to display. Defaults to `None`.

## `spinner`

Displays a loading spinner.

### Arguments

*   `size` (string): The size of the spinner. Defaults to "md".
