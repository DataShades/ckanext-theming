# Elements

## `avatar`

Displays a user avatar.

### Arguments

*   `src` (string): The image source URL.
*   `alt` (string): The image alt text. Defaults to "".

## `badge`

Displays a badge element.

### Arguments

*   `content` (string): The text to display in the badge.

## `button`

Renders a button.

### Arguments

*   `content` (string): The text to display on the button.
*   `type` (string): The button type. Defaults to "button".

## `divider`

Creates a horizontal divider.

### Arguments

None

## `heading`

Generates a heading (h1-h6).

### Arguments

*   `content` (string): The heading text.
*   `level` (integer): The heading level (1-6). Defaults to 1.

## `image`

Displays an image.

### Arguments

*   `src` (string): The image source URL.
*   `alt` (string): The image alt text. Defaults to "".

## `link`

Creates a hyperlink.

### Arguments

*   `content` (string): The link text.
*   `href` (string): The link URL. Same as content if empty.


## `tag`

Displays a tag.

### Arguments

*   `content` (string): The tag text.
*   `id` (string): The tag ID.
*   `href` (string): The tag URL.

## `text`

Renders plain text content.

### Arguments

*   `content` (string): The text content.

## `video`

Embeds a video.

### Arguments

*   `src` (string): The video source URL.
*   `controls` (boolean): Whether to display video controls. Defaults to `true`.
