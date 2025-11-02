# Form

## `form_block`

Displays a form wrapper, handling CSRF and rendering content within its block.

### Arguments

*   `method` (string): The form method. Defaults to "GET".
*   `action` (string): The form action URL. Defaults to "".
*   `enctype` (string): The form encoding type. Defaults to "".
*   `include_csrf` (boolean): Whether to include a CSRF token. Defaults to `true`.

## `form_actions_wrapper`

Wraps form actions. This is a block macro.

### Arguments

None

## `form_start`

Starts the HTML `<form>` tag.

### Arguments

*   `method` (string): The form method.
*   `action` (string): The form action URL. Defaults to "".
*   `enctype` (string): The form encoding type. Defaults to "".

## `form_end`

Closes the HTML `</form>` tag.

### Arguments

None

## `form_errors`

Displays a list of form errors.

### Arguments

*   `errors` (dict): A dictionary of form errors.

## `input`

Renders a generic HTML `<input>` field.

### Arguments

*   `name` (string): The name attribute for the input.
*   `id` (string): The id attribute for the input. If `name` is provided and `id` is empty, `id` defaults to "field-`name`".
*   `label` (string): The label text for the input. If empty, field has no label at all.
*   `value` (string): The value attribute for the input. Defaults to "".
*   `type` (string): The type attribute for the input (e.g., "text", "password", "email"). Defaults to "text".
*   `errors` (list): A list of error messages to display. Defaults to `[]`.
*   `required` (boolean): Whether the input field is required. Defaults to `false`.

## `checkbox`

Renders an HTML checkbox `<input type="checkbox">` field.

### Arguments

*   `name` (string): The name attribute for the checkbox.
*   `id` (string): The id attribute for the checkbox.
*   `label` (string): The label text for the checkbox. Defaults to "".
*   `value` (string): The value attribute for the checkbox when checked. Defaults to "on".
*   `checked` (boolean): Whether the checkbox is initially checked. Defaults to `false`.
*   `errors` (list): A list of error messages to display. Defaults to `[]`.
*   `required` (boolean): Whether the checkbox field is required. Defaults to `false`.
