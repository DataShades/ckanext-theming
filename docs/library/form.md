# Form

Form macros provide a comprehensive system for creating consistent, accessible forms throughout the application. These components handle form structure, validation errors, and common form elements with proper accessibility and styling support.

## `form_block`

Displays a complete form wrapper with automatic CSRF protection and proper form structure. This macro handles the form creation process with security measures and proper opening and closing tags.

**Use Cases:**

- Complete standalone forms
- Content creation forms
- User registration
- Settings forms
- Search forms
- Contact forms

**Usage Context:**

Use as the main wrapper for any form that requires submission to the server, especially when CSRF protection is needed.

**Example:**

```
{{ ui.form_block(method="POST", action="/submit", include_csrf=true) }}
  {{ ui.input(name="username", label="Username") }}
  {{ ui.input(name="email", label="Email", type="email") }}
  {{ ui.textarea(name="comment", label="Comment") }}
  {{ ui.button("Submit", style="primary", type="submit") }}
{{ ui.form_end() }}
```

**Recommendations:**

- Always use for forms that submit to the server
- Enable CSRF protection (default behavior) for security
- Different themes may customize form styling (Bootstrap: .needs-validation, Tailwind: space-y-6, Bulma: .box)
- Consider using appropriate HTTP methods (GET for searches, POST for changes)

## `form_actions_wrapper`

Wraps form actions such as submit, reset, and cancel buttons. Provides consistent spacing and alignment for form control elements.

**Use Cases:**

- Submit and cancel buttons
- Form action grouping
- Button alignment
- Form submission controls
- Multi-step form navigation

**Usage Context:**

Use at the end of forms to wrap action buttons that perform operations like saving, submitting, or canceling.

**Example:**

```
{{ ui.form_actions_wrapper(
  ui.button("Save", style="primary", type="submit") +
  ui.button("Cancel", style="secondary", type="button")
) }}
```

**Recommendations:**

- Place below form content for consistency
- Different themes may position buttons differently (Bootstrap: mb-3, Tailwind: flex justify-between, Bulma: field is-grouped)
- Primary action should be visually prominent
- Consider progressive disclosure with multi-step forms

## `form_start`

Starts the HTML `<form>` tag with specified method, action, and encoding type. Provides the opening element for form structures with proper attributes.

**Use Cases:**

- Manual form construction
- Advanced form control
- Custom form behavior
- Form with special encoding
- Progressive enhancement scenarios

**Usage Context:**

Use when you need manual control over form creation or when building forms programmatically.

**Example:**

```
{{ ui.form_start(method="POST", action="/upload", enctype="multipart/form-data") }}
```

**Recommendations:**

- Pair with form_end() for proper closure
- Use appropriate enctype for file uploads (multipart/form-data)
- Different themes may apply default styling (Bootstrap: .form-horizontal, Tailwind: space-y-6)
- Ensure proper method (GET vs POST) for intended operation

## `form_end`

Closes the HTML `</form>` tag. Provides the closing element for form structures.

**Use Cases:**

- Closing form structures
- Manual form construction
- Form component building
- Custom form implementations

**Usage Context:**

Use to properly close any form started with form_start().

**Example:**

```
{{ ui.form_start(method="POST", action="/process") }}
  <!-- form content -->
{{ ui.form_end() }}
```

**Recommendations:**

- Always pair with form_start()
- Different themes may not customize this element specifically
- Essential for proper HTML structure

## `form_errors`

Displays a formatted list of form validation errors in a user-friendly way. Provides clear feedback about issues with form submission and guides users to correct problems.

**Use Cases:**

- Validation error display
- User feedback
- Form correction guidance
- Accessibility compliance
- Error summary presentation

**Usage Context:**

Place near the top of the form or near the submit button to provide immediate feedback when form submission fails validation.

**Example:**

```
{{ ui.form_errors(errors={
  "username": "Username is required and must be unique",
  "email": "Please enter a valid email address"
}) }}
```

**Recommendations:**

- Display prominently when validation fails
- Different themes style errors differently (Bootstrap: .alert-danger, Tailwind: bg-red-50 p-4, Bulma: .notification.is-danger)
- Include specific error messages for each field
- Use proper ARIA attributes for accessibility

## `input`

Renders a standard HTML input field with associated label and error handling. Provides a flexible component for various input types (text, email, password, etc.).

**Use Cases:**

- Text input fields
- Email and password fields
- Number inputs
- Search fields
- URL and tel inputs
- Custom input types

**Usage Context:**

Use for any single-line text input or specialized input fields like email addresses, passwords, numbers, etc.

**Example:**

```
{{ ui.input(name="email", label="Email Address", type="email", required=true) }}
{{ ui.input(name="phone", label="Phone Number", type="tel", value="+1234567890") }}
```

**Recommendations:**

- Always include appropriate labels for accessibility
- Use correct input types for better user experience (email, password, number)
- Different themes style inputs with various approaches (Bootstrap: .form-control, Tailwind: border-gray-300, Bulma: .input)
- Include error messages when validation fails
- Use `required=true` for mandatory fields

## `checkbox`

Renders an HTML checkbox input field with associated label and error handling. Provides a binary choice input with optional labeling.

**Use Cases:**

- Agreement checkboxes
- Option selections
- Feature toggles
- Consent forms
- Multiple choice selections

**Usage Context:**

Use when users need to make a binary choice or select multiple options from a small set.

**Example:**

```
{{ ui.checkbox(name="terms", label="I agree to the terms and conditions", required=true) }}
{{ ui.checkbox(name="newsletter", label="Subscribe to newsletter", checked=true) }}
```

**Recommendations:**

- Include clear, descriptive labels
- Different themes style checkboxes differently (Bootstrap: .form-check-input, Tailwind: form-checkbox, Bulma: .checkbox)
- Use `required=true` for mandatory agreements
- Consider using toggle switches for feature-like options
- Ensure proper accessibility with labels

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
