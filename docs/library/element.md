# Elements

*   **`badge`**: Displays a badge element.
    *   Arguments:
        *   `text` (string): The text to display in the badge.
        *   `style` (string): The color of the badge.
*   **`button`**: Renders a button.
    *   Arguments:
        *   `content` (string): The text to display on the button.
        *   `href` (string, optional):  If provided, renders a link instead of a button.
        *   `type` (string, optional): The button type. Defaults to "button".
        *   `size` (string, optional): The button size. Defaults to "default".
        *   `color` (string, optional): The button color. Defaults to "primary".
*   **`divider`**: Creates a horizontal divider.
    *   Arguments: None
*   **`heading`**: Generates a heading (h1-h6).
    *   Arguments:
        *   `text` (string): The heading text.
        *   `level` (integer, optional): The heading level (1-6). Defaults to 1.
*   **`image`**: Displays an image.
    *   Arguments:
        *   `src` (string): The image source URL.
        *   `alt` (string): The image alt text.
        *   `width` (string, optional): The image width.
        *   `height` (string, optional): The image height.
*   **`link`**: Creates a hyperlink.
    *   Arguments:
        *   `content` (string): The link text.
        *   `href` (string): The link URL.
        *   `title` (string, optional): The link title.
*   **`tag`**: Displays a tag.
    *   Arguments:
        *   `text` (string): The tag text.
*   **`text`**: Renders plain text.
    *   Arguments:
        *   `content` (string): The text content.
*   **`text_block`**: Displays a block of text.
    *   Arguments:
        *   `content` (string): The text content.
*   **`video`**: Embeds a video.
    *   Arguments:
        *   `src` (string): The video source URL.
        *   `width` (string, optional): The video width.
        *   `height` (string, optional): The video height.
