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

## `textarea`

Renders an HTML `<textarea>` field.

### Arguments

*   `name` (string): The name attribute for the textarea.
*   `id` (string): The id attribute for the textarea. If `name` is provided and `id` is empty, `id` defaults to "field-`name`".
*   `label` (string): The label text for the textarea. Defaults to "".
*   `value` (string): The value content for the textarea. Defaults to "".
*   `errors` (list): A list of error messages to display. Defaults to `[]`.
*   `required` (boolean): Whether the textarea field is required. Defaults to `false`.

## `select`

Renders an HTML `<select>` dropdown field.

### Arguments

*   `name` (string): The name attribute for the select.
*   `id` (string): The id attribute for the select. If `name` is provided and `id` is empty, `id` defaults to "field-`name`".
*   `label` (string): The label text for the select. Defaults to "".
*   `options` (list): A list of options for the dropdown. Can be strings or dictionaries with 'value' and 'text' keys. Defaults to `[]`.
*   `selected` (string): The selected value. Defaults to `None`.
*   `errors` (list): A list of error messages to display. Defaults to `[]`.
*   `required` (boolean): Whether the select field is required. Defaults to `false`.

## `radio`

Renders an HTML radio button `<input type="radio">` field.

### Arguments

*   `name` (string): The name attribute for the radio button.
*   `id` (string): The id attribute for the radio button.
*   `label` (string): The label text for the radio button. Defaults to "".
*   `value` (string): The value attribute for the radio button. Defaults to "on".
*   `checked` (boolean): Whether the radio button is initially checked. Defaults to `false`.
*   `errors` (list): A list of error messages to display. Defaults to `[]`.
*   `required` (boolean): Whether the radio button field is required. Defaults to `false`.

## `file_input`

Renders an HTML file input `<input type="file">` field.

### Arguments

*   `name` (string): The name attribute for the file input.
*   `id` (string): The id attribute for the file input. If `name` is provided and `id` is empty, `id` defaults to "field-`name`".
*   `label` (string): The label text for the file input. Defaults to "".
*   `errors` (list): A list of error messages to display. Defaults to `[]`.
*   `required` (boolean): Whether the file input field is required. Defaults to `false`.

## `range_input`

Renders an HTML range input `<input type="range">` field.

### Arguments

*   `name` (string): The name attribute for the range input.
*   `id` (string): The id attribute for the range input. If `name` is provided and `id` is empty, `id` defaults to "field-`name`".
*   `label` (string): The label text for the range input. Defaults to "".
*   `value` (integer): The initial value of the range input. Defaults to 0.
*   `min` (integer): The minimum value of the range input. Defaults to 0.
*   `max` (integer): The maximum value of the range input. Defaults to 100.
*   `errors` (list): A list of error messages to display. Defaults to `[]`.
*   `required` (boolean): Whether the range input field is required. Defaults to `false`.

## `toggle_switch`

Renders a toggle switch element.

### Arguments

*   `name` (string): The name attribute for the toggle switch.
*   `id` (string): The id attribute for the toggle switch. If `name` is provided and `id` is empty, `id` defaults to "field-`name`".
*   `label` (string): The label text for the toggle switch. Defaults to "".
*   `value` (string): The value attribute when the switch is on. Defaults to "on".
*   `checked` (boolean): Whether the toggle switch is initially on. Defaults to `false`.
*   `errors` (list): A list of error messages to display. Defaults to `[]`.
*   `required` (boolean): Whether the toggle switch field is required. Defaults to `false`.
