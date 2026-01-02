# Form

Form components provide all the necessary elements for creating and managing
forms in CKAN. These components handle user input and form submission.

## Overview

Form components are essential for user interaction and data input. They provide
consistent styling and behavior for all form elements, ensuring accessibility
and proper validation handling. Many form components work together in
structured relationships - for example, [`form`][] components work with
[`form_start`][form-start], [`form_end`][form-end],
[`form_actions`][form-actions], and [`form_errors`][form-errors] to create
complete form experiences.

## Autocomplete

The [`autocomplete`][] component creates input fields with autocomplete
functionality that suggests possible values as users type. This component is
particularly valuable for forms with large sets of possible values, such as
location selectors, category pickers, or user search fields.

Autocomplete components provide enhanced user experience by reducing typing
effort and helping users select from predefined options. They typically display
suggestions in a dropdown list as the user types, filtering options based on
the input. The component handles accessibility requirements and ensures
suggestions are properly announced to screen readers.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic autocomplete -->
{{ ui.autocomplete(name="search", placeholder="Search...") }}

<!-- Autocomplete with source -->
{{ ui.autocomplete(name="location", placeholder="Enter location", source="/api/locations") }}
```
///

## Checkbox

The [`checkbox`][] component creates checkbox input elements that allow users to select one or multiple options from a set. Checkboxes are fundamental for forms where users need to make binary choices or select multiple items from a list.

Checkbox components handle proper labeling, accessibility attributes, and visual styling to ensure they're easily identifiable and usable. They can be used individually or grouped together, and often work with other form components to create comprehensive input experiences.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic checkbox -->
{{ ui.checkbox("Accept terms", name="terms", value="yes") }}

<!-- Checked checkbox -->
{{ ui.checkbox("Subscribe to newsletter", name="subscribe", checked=True) }}

<!-- Checkbox with label -->
{{ ui.checkbox("Remember me", name="remember", label="Remember my login") }}
```
///

## Extra Field

The [`extra_field`][extra-field] component creates additional form fields that can be dynamically added to forms. This component is particularly useful for forms where users might need to add custom metadata, tags, or other variable information that isn't part of the standard form structure.

Extra field components provide flexibility for forms that need to accommodate varying amounts of information. They often work with [`extra_field_multiplicator`][extra-field-multiplicator] and [`extra_fields_collection`][extra-fields-collection] components to create dynamic form experiences where users can add as many fields as needed.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic extra field -->
{{ ui.extra_field(index=0) }}

<!-- Extra field with data -->
{{ ui.extra_field(index=1, data={"key": "custom_field", "value": "custom_value"}) }}
```
///

/// admonition | Relationship
    type: info

The [`extra_field`][extra-field] component works with [`extra_field_multiplicator`][extra-field-multiplicator] and [`extra_fields_collection`][extra-fields-collection] components to create dynamic form experiences. While individual extra fields provide the input structure, the other components handle the dynamic addition and collection of fields.

///

## Extra Field Multiplicator

The [`extra_field_multiplicator`][extra-field-multiplicator] component provides tools for adding multiple extra fields to forms dynamically. This component creates the interface elements that allow users to add additional fields as needed, typically through an "Add Field" button or similar control.

The multiplicator component handles the JavaScript functionality needed to add new field instances while maintaining proper form structure and validation. It ensures that each new field has unique identifiers and proper naming conventions for form processing.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic extra field multiplicator -->
{{ ui.extra_field_multiplicator(index=2) }}

<!-- Extra field multiplicator with label -->
{{ ui.extra_field_multiplicator(index=3, label="Add Another Field") }}
```
///

/// admonition | Relationship
    type: info

The [`extra_field_multiplicator`][extra-field-multiplicator] component works
with [`extra_field`][extra-field] and
[`extra_fields_collection`][extra-fields-collection] components to create
dynamic form experiences. The multiplicator provides the addition mechanism,
while the other components provide the field structure and collection handling.

///

## Extra Fields Collection

The [`extra_fields_collection`][extra-fields-collection] component manages
collections of extra fields within forms, providing the structural container
for dynamically added fields. This component ensures that all extra fields are
properly organized and processed as a group.

The collection component handles validation, processing, and display of multiple extra fields, ensuring they maintain proper form structure and accessibility. It works with the other extra field components to create cohesive dynamic form experiences.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic extra fields collection -->
{{ ui.extra_fields_collection(extras=[{"key": "field1", "value": "value1"}, {"key": "field2", "value": "value2"}]) }}

<!-- Extra fields collection with limit -->
{{ ui.extra_fields_collection(extras=[], limit=5) }}
```
///

/// admonition | Relationship
    type: info

The [`extra_fields_collection`][extra-fields-collection] component works with
[`extra_field`][extra-field] and
[`extra_field_multiplicator`][extra-field-multiplicator] components to manage
dynamic form fields. The collection provides the container structure for all
extra fields.

///

## Field Errors

The [`field_errors`][field-errors] component displays field-specific error messages that provide feedback about validation issues with individual form fields. These error messages are crucial for helping users understand what needs to be corrected in specific fields.

Field error components are typically displayed near the relevant form field and provide clear, actionable information about what went wrong and how to fix it. They ensure proper accessibility by linking errors to their associated fields and providing appropriate ARIA attributes.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic field errors -->
{{ ui.field_errors(["Field is required", "Must be at least 3 characters"]) }}

<!-- Field errors with attributes -->
{{ ui.field_errors(["Invalid email format"], attrs={"class": "error-messages"}) }}
```
///

## File Input

The [`file_input`][file-input] component creates file upload input elements that allow users to select and upload files. This component handles the complexities of file selection, including multiple file selection, file type validation, and progress indication during upload.

File input components provide enhanced user experience through features like drag-and-drop support, file previews, and upload progress tracking. They handle accessibility requirements and ensure file uploads work consistently across different browsers and devices.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic file input -->
{{ ui.file_input(name="upload", label="Upload File") }}

<!-- File input with accept attribute -->
{{ ui.file_input(name="image", label="Upload Image", accept=".jpg,.png,.gif") }}

<!-- Multiple file input -->
{{ ui.file_input(name="files", label="Upload Multiple Files", multiple=True) }}
```
///

## Form

The [`form`][] component creates complete form containers that organize all form elements into a cohesive unit. This component provides the overall structure for forms and handles form-level functionality such as submission handling and validation management.

The form component works with several related components including
[`form_start`][form-start], [`form_end`][form-end],
[`form_actions`][form-actions], and [`form_errors`][form-errors] to create
complete form experiences. It ensures proper form structure, accessibility, and
functionality while maintaining consistency across different form types.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic form -->
{{ ui.form(ui.input(name="name", label="Name") ~ ui.submit("Submit")) }}

<!-- Form with method and action -->
{{ ui.form(ui.input(name="email", label="Email") ~ ui.submit("Save"), method="POST", action="/save") }}
```
///

/// admonition | Relationship
    type: info

The [`form`][] component works with [`form_start`][form-start], [`form_end`][form-end], [`form_actions`][form-actions],
and [`form_errors`][form-errors] components to create complete form experiences. The form
provides the overall container, while the other components provide specific
structural elements.  ///

## Form Actions

The [`form_actions`][form-actions] component creates containers for form action buttons such as submit, cancel, and reset buttons. This component ensures that form actions are consistently positioned and styled across different forms.

Form actions components handle the layout and styling of action buttons, ensuring they're clearly visible and appropriately spaced. They often include buttons like "Save Changes", "Cancel", or "Reset Form" that control the form submission and navigation flow.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic form actions -->
{{ ui.form_actions(ui.button("Save", type="submit") ~ ui.button("Cancel", href="/cancel")) }}

<!-- Form actions with attributes -->
{{ ui.form_actions(ui.submit("Submit") ~ ui.button("Cancel"), attrs={"class": "form-actions"}) }}
```
///

/// admonition | Relationship
    type: info

The [`form_actions`][form-actions] component works within [`form`][] containers to provide consistent action button placement. While the form provides the overall structure, the actions component handles the submission controls.
///

## Form End

The [`form_end`][form-end] component marks the end of form containers, providing the closing structure for complete form experiences. This component ensures proper form closure and handles any necessary cleanup or finalization functionality.

Form end components work with [`form_start`][form-start] components to create complete form boundaries, ensuring all form elements are properly contained and processed. They handle form-level functionality that occurs at the end of form processing.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic form end -->
{{ ui.form_end() }}

<!-- Form end with attributes -->
{{ ui.form_end(attrs={"class": "form-end"}) }}
```
///

/// admonition | Relationship
    type: info

The [`form_end`][form-end] component works with [`form_start`][form-start] components to define complete form boundaries. While the start component marks the beginning, the end component marks the conclusion of the form structure.
///

## Form Errors

The [`form_errors`][form-errors] component displays form-wide error messages that provide feedback about issues affecting the entire form or multiple fields. These errors are distinct from field-specific errors and typically indicate broader validation or processing problems.

Form error components are displayed prominently within the form to ensure users notice critical issues that prevent form submission. They provide clear information about what went wrong and often include guidance about how to resolve the issues.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic form errors -->
{{ ui.form_errors({"name": ["Name is required"], "email": ["Invalid email format"]}) }}

<!-- Form errors with attributes -->
{{ ui.form_errors({"password": ["Password too weak"]}, attrs={"class": "form-errors"}) }}
```
///

/// admonition | Relationship
    type: info

The [`form_errors`][form-errors] component works within [`form`][] containers alongside [`field_errors`][field-errors] components. While field errors address specific input issues, form errors address broader validation or processing problems.
///

## Form Start

The [`form_start`][form-start] component marks the beginning of form containers, establishing the opening structure for complete form experiences. This component handles form initialization and sets up the necessary attributes and functionality for proper form operation.

Form start components work with [`form_end`][form-end] components to create complete form boundaries, ensuring all form elements are properly contained. They handle form-level attributes such as action URLs, method types, and encoding types that are necessary for proper form processing.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic form start -->
{{ ui.form_start(method="POST", action="/submit") }}

<!-- Form start with enctype -->
{{ ui.form_start(method="POST", action="/upload", enctype="multipart/form-data") }}
```
///

/// admonition | Relationship
    type: info

The [`form_start`][form-start] component works with [`form_end`][form-end] components to define complete form boundaries. While the start component establishes the form structure, the end component provides the conclusion.
///

## Hidden Input

The [`hidden_input`][hidden-input] component creates hidden form input elements that store data without displaying it to users. Hidden inputs are essential for maintaining state, security tokens, and other information that needs to be submitted with forms but shouldn't be visible or editable.

Hidden input components handle the proper HTML structure and attributes for hidden form fields, ensuring they're properly processed during form submission while remaining invisible to users. They maintain accessibility standards and proper form functionality.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic hidden input -->
{{ ui.hidden_input(name="csrf_token", value="abc123") }}

<!-- Hidden input with attributes -->
{{ ui.hidden_input(name="user_id", value="123", attrs={"data-hidden": "true"}) }}
```
///

## Input

The [`input`][] component creates general text input fields for collecting user text input. This is one of the most fundamental form components, used for collecting various types of text data including names, email addresses, search terms, and other textual information.

Input components handle various input types such as text, email, password, and number fields, providing appropriate validation and formatting for each type. They ensure proper accessibility, styling, and functionality while maintaining consistency across different input contexts.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic text input -->
{{ ui.input(name="username", label="Username", placeholder="Enter your username") }}

<!-- Email input -->
{{ ui.input(name="email", type="email", label="Email", placeholder="user@example.com") }}

<!-- Password input -->
{{ ui.input(name="password", type="password", label="Password", required=True) }}

<!-- Input with validation errors -->
{{ ui.input(name="title", label="Title", value="Dataset Title", errors=["Title is required"]) }}
```
///

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | Help text or description for the input. |
| `name` | string | - | Name attribute for the input field. |
| `id` | string | - | ID attribute for the input field. |
| `label` | string | - | Label text for the input field. |
| `value` | string | - | Value of the input field. |
| `required` | bool | - | Whether the field is required. |
| `placeholder` | string | - | Placeholder text for the input field. |
| `type` | string | "text" | Input type (e.g., "text", "email", "password", "number"). |
| `errors` | list | [] | List of error messages to display. |

/// details | Theme-Specific Parameters
    type: tip

- `size` (string): Size of the input (e.g., "sm", "lg")
- `variant` (string): Style variant (e.g., "filled", "outlined")
- `helper_text` (string): Additional helper text below the input
- `disabled` (bool): Whether the input is disabled
- `readonly` (bool): Whether the input is read-only
///

## Markdown

The [`markdown`][] component creates markdown editor inputs that allow users to write content using markdown syntax. This component is particularly useful for forms where users need to create formatted content without dealing with complex WYSIWYG editors.

Markdown components provide syntax highlighting, preview functionality, and appropriate tooling to help users create well-formatted content using simple markdown syntax. They balance ease of use with formatting capabilities, making them suitable for various content creation scenarios.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic markdown component -->
{{ ui.markdown(name="content", label="Content", placeholder="Enter markdown content...") }}

<!-- Markdown with value -->
{{ ui.markdown(name="description", label="Description", value="# Title\n\nContent here...", required=True) }}
```
///

## Radio

The [`radio`][] component creates radio button input elements that allow users to select one option from a set of mutually exclusive choices. Radio buttons are essential for forms where users must choose a single option from multiple possibilities.

Radio components handle proper grouping, accessibility attributes, and visual styling to ensure users understand the selection constraints. They ensure that only one option can be selected within a group and provide clear visual feedback about the current selection.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic radio component -->
{{ ui.radio("Option 1", name="choice", value="option1") }}

<!-- Checked radio component -->
{{ ui.radio("Option 2", name="choice", value="option2", checked=True) }}
```
///

## Range Input

The [`range_input`][range-input] component creates range slider inputs that allow users to select a value from a continuous range. This component is useful for forms where users need to specify values like ratings, quantities, or other continuous data.

Range input components provide visual feedback about the selected value and handle accessibility requirements for slider controls. They ensure proper keyboard navigation and screen reader support while maintaining intuitive interaction patterns.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic range input -->
{{ ui.range_input(min_value=0, max_value=100) }}

<!-- Range input with initial value -->
{{ ui.range_input(min_value=0, max_value=10, value=5) }}
```
///

## Select

The [`select`][] component creates dropdown select input elements that allow users to choose from a predefined list of options. Select components are fundamental for forms where users need to choose from multiple options in a space-efficient manner.

Select components handle option display, selection management, and accessibility requirements. They work with [`select_option`][select-option] and [`select_box`][select-box] components to create complete selection experiences with proper structure and functionality.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic select with options as list -->
{{ ui.select(name="category", label="Category", options=["Option 1", "Option 2", "Option 3"]) }}

<!-- Select with selected option -->
{{ ui.select(name="status", label="Status", selected="active", options=["active", "inactive", "pending"]) }}

<!-- Select with complex options -->
{{ ui.select(name="country", label="Country", options=[{"value": "us", "text": "United States"}, {"value": "ca", "text": "Canada"}]) }}
```
///

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | Help text or description for the select. |
| `name` | string | - | Name attribute for the select field. |
| `id` | string | - | ID attribute for the select field. |
| `label` | string | - | Label text for the select field. |
| `selected` | string/list | - | Value(s) that should be selected by default. |
| `options` | list | - | List of options to display in the select. |
| `multiple` | bool | - | Whether multiple options can be selected. |
| `required` | bool | - | Whether the field is required. |
| `autocomplete` | string | - | Autocomplete behavior for the select. |
| `errors` | list | [] | List of error messages to display. |

/// details | Theme-Specific Parameters
    type: tip

- `size` (string): Size of the select (e.g., "sm", "lg")
- `variant` (string): Style variant (e.g., "filled", "outlined")
- `helper_text` (string): Additional helper text below the select
- `disabled` (bool): Whether the select is disabled
- `native` (bool): Whether to use native browser select
///

/// admonition | Relationship
    type: info

The [`select`][] component works with [`select_option`][select-option] and [`select_box`][select-box] components to create complete selection experiences. The select provides the container, while options provide the choices.
///

## Select Box

The [`select_box`][select-box] component creates containers for select input elements, providing the structural foundation for dropdown selection controls. This component handles the visual presentation and interaction patterns for select elements.

Select box components work with [`select`][] and [`select_option`][select-option] components to create cohesive selection experiences. They ensure proper styling, positioning, and accessibility for dropdown controls while maintaining consistency across different themes.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic select box -->
{{ ui.select_box(ui.select_option("Option 1", "opt1") ~ ui.select_option("Option 2", "opt2")) }}

<!-- Select box with attributes -->
{{ ui.select_box(ui.select_option("Choice A", "a") ~ ui.select_option("Choice B", "b"), attrs={"class": "custom-select"}) }}
```
///

/// admonition | Relationship
    type: info

The [`select_box`][select-box] component works with [`select`][] and [`select_option`][select-option] components to create complete selection experiences. The box provides the container styling and structure.
///

## Select Option

The [`select_option`][select-option] component creates individual options within select input elements, providing the choices that users can select from dropdown lists. Each option represents a single choice within the selection control.

Select option components handle proper value assignment, display text, and selection states. They work within [`select`][] elements to create the complete list of available choices, ensuring proper functionality and accessibility for each option.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic select option -->
{{ ui.select_option("Option Text", "option_value") }}

<!-- Selected option -->
{{ ui.select_option("Selected Option", "selected_value", selected=True) }}
```
///

/// admonition | Relationship
    type: info

The [`select_option`][select-option] component works within [`select`][] elements to provide individual choices. While the select provides the container, options provide the available selections.
///

## Submit

The [`submit`][] component creates form submission buttons that trigger form processing when clicked. Submit buttons are essential for form completion and must be clearly identifiable and appropriately styled to encourage user action.

Submit components handle form submission functionality, validation triggering, and appropriate visual styling to distinguish them from other buttons. They ensure proper accessibility and provide clear feedback about the submission action.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic submit button -->
{{ ui.submit("Save Changes", name="save") }}

<!-- Submit with different style -->
{{ ui.submit("Submit Form", name="submit", attrs={"class": "btn btn-primary"}) }}

<!-- Submit with confirmation -->
{{ ui.submit("Delete", name="delete", attrs={"onclick": "return confirm('Are you sure?')", "class": "btn btn-danger"}) }}
```
///

## Textarea

The [`textarea`][] component creates multi-line text input fields that allow users to enter longer text content. Textareas are essential for forms where users need to provide detailed information, descriptions, comments, or other multi-line text input.

Textarea components handle appropriate sizing, scrolling behavior, and accessibility requirements for multi-line text input. They provide sufficient space for users to enter and edit longer content while maintaining proper form structure and validation capabilities.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic textarea -->
{{ ui.textarea(name="description", label="Description", placeholder="Enter description here...") }}

<!-- Textarea with value -->
{{ ui.textarea(name="content", label="Content", value="Existing content", required=True) }}

<!-- Textarea with validation errors -->
{{ ui.textarea(name="comment", label="Comment", errors=["Comment is required"]) }}
```
///

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | Help text or description for the textarea. |
| `name` | string | - | Name attribute for the textarea field. |
| `id` | string | - | ID attribute for the textarea field. |
| `label` | string | - | Label text for the textarea field. |
| `value` | string | - | Value of the textarea field. |
| `required` | bool | - | Whether the field is required. |
| `placeholder` | string | - | Placeholder text for the textarea field. |
| `rows` | int | - | Number of visible text rows. |
| `cols` | int | - | Number of visible text columns. |
| `errors` | list | [] | List of error messages to display. |

/// details | Theme-Specific Parameters
    type: tip

- `size` (string): Size of the textarea (e.g., "sm", "lg")
- `variant` (string): Style variant (e.g., "filled", "outlined")
- `helper_text` (string): Additional helper text below the textarea
- `disabled` (bool): Whether the textarea is disabled
- `readonly` (bool): Whether the textarea is read-only
///
