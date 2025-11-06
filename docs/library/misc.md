# Miscellaneous

## `datetime`

Formats a datetime object for display, including a `data-datetime` attribute for machine-readable format.

### Arguments

*   `dt` (datetime object): The datetime object to format.

## `spacer`

Creates a spacing element.

### Arguments

*   `size` (string): The size of the spacer. Defaults to "md".

## `divider_with_text`

Creates a horizontal divider with centered text.

### Arguments

*   `content` (string): text to display in the center of the divider.

## `truncate`

Creates a text truncation container.

### Arguments

*   `content` (string): content to potentially truncate.
*   `max_lines` (integer): maximum number of lines to display before truncating. Defaults to 1.

## `badge_count`

Displays a count badge.

### Arguments

*   `count` (integer): the count value to display in the badge.

## `skeleton_loader`

Displays a skeleton loader for content placeholders.

### Arguments

*   `type` (string): the type of skeleton loader. Defaults to "text".

## `notification`

Displays a notification message.

### Arguments

*   `title` (string): The title of the notification. Defaults to `None`.
*   `content` (string): The content of the notification.
*   `type` (string): The type of notification (e.g., "info", "success", "warning", "error"). Defaults to "info".
