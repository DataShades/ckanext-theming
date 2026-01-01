# Form Components

Form components provide all the necessary elements for creating and managing forms in CKAN. These components handle user input and form submission.

## Overview

Form components are essential for user interaction and data input. They provide consistent styling and behavior for all form elements, ensuring accessibility and proper validation handling. Many form components work together in structured relationships - for example, `form` components work with `form_start`, `form_end`, `form_actions`, and `form_errors` to create complete form experiences.

## Autocomplete Component

The `autocomplete` component creates input fields with autocomplete functionality that suggests possible values as users type. This component is particularly valuable for forms with large sets of possible values, such as location selectors, category pickers, or user search fields.

Autocomplete components provide enhanced user experience by reducing typing effort and helping users select from predefined options. They typically display suggestions in a dropdown list as the user types, filtering options based on the input. The component handles accessibility requirements and ensures suggestions are properly announced to screen readers.

## Checkbox Component

The `checkbox` component creates checkbox input elements that allow users to select one or multiple options from a set. Checkboxes are fundamental for forms where users need to make binary choices or select multiple items from a list.

Checkbox components handle proper labeling, accessibility attributes, and visual styling to ensure they're easily identifiable and usable. They can be used individually or grouped together, and often work with other form components to create comprehensive input experiences.

## Extra Field Component

The `extra_field` component creates additional form fields that can be dynamically added to forms. This component is particularly useful for forms where users might need to add custom metadata, tags, or other variable information that isn't part of the standard form structure.

Extra field components provide flexibility for forms that need to accommodate varying amounts of information. They often work with `extra_field_multiplicator` and `extra_fields_collection` components to create dynamic form experiences where users can add as many fields as needed.

/// admonition | Relationship
    type: info

The `extra_field` component works with `extra_field_multiplicator` and `extra_fields_collection` components to create dynamic form experiences. While individual extra fields provide the input structure, the other components handle the dynamic addition and collection of fields.
///

## Extra Field Multiplicator Component

The `extra_field_multiplicator` component provides tools for adding multiple extra fields to forms dynamically. This component creates the interface elements that allow users to add additional fields as needed, typically through an "Add Field" button or similar control.

The multiplicator component handles the JavaScript functionality needed to add new field instances while maintaining proper form structure and validation. It ensures that each new field has unique identifiers and proper naming conventions for form processing.

/// admonition | Relationship
    type: info

The `extra_field_multiplicator` component works with `extra_field` and `extra_fields_collection` components to create dynamic form experiences. The multiplicator provides the addition mechanism, while the other components provide the field structure and collection handling.
///

## Extra Fields Collection Component

The `extra_fields_collection` component manages collections of extra fields within forms, providing the structural container for dynamically added fields. This component ensures that all extra fields are properly organized and processed as a group.

The collection component handles validation, processing, and display of multiple extra fields, ensuring they maintain proper form structure and accessibility. It works with the other extra field components to create cohesive dynamic form experiences.

/// admonition | Relationship
    type: info

The `extra_fields_collection` component works with `extra_field` and `extra_field_multiplicator` components to manage dynamic form fields. The collection provides the container structure for all extra fields.
///

## Field Errors Component

The `field_errors` component displays field-specific error messages that provide feedback about validation issues with individual form fields. These error messages are crucial for helping users understand what needs to be corrected in specific fields.

Field error components are typically displayed near the relevant form field and provide clear, actionable information about what went wrong and how to fix it. They ensure proper accessibility by linking errors to their associated fields and providing appropriate ARIA attributes.

## File Input Component

The `file_input` component creates file upload input elements that allow users to select and upload files. This component handles the complexities of file selection, including multiple file selection, file type validation, and progress indication during upload.

File input components provide enhanced user experience through features like drag-and-drop support, file previews, and upload progress tracking. They handle accessibility requirements and ensure file uploads work consistently across different browsers and devices.

## Form Component

The `form` component creates complete form containers that organize all form elements into a cohesive unit. This component provides the overall structure for forms and handles form-level functionality such as submission handling and validation management.

The form component works with several related components including `form_start`, `form_end`, `form_actions`, and `form_errors` to create complete form experiences. It ensures proper form structure, accessibility, and functionality while maintaining consistency across different form types.

/// admonition | Relationship
    type: info

The `form` component works with `form_start`, `form_end`, `form_actions`, and `form_errors` components to create complete form experiences. The form provides the overall container, while the other components provide specific structural elements.
///

## Form Actions Component

The `form_actions` component creates containers for form action buttons such as submit, cancel, and reset buttons. This component ensures that form actions are consistently positioned and styled across different forms.

Form actions components handle the layout and styling of action buttons, ensuring they're clearly visible and appropriately spaced. They often include buttons like "Save Changes", "Cancel", or "Reset Form" that control the form submission and navigation flow.

/// admonition | Relationship
    type: info

The `form_actions` component works within `form` containers to provide consistent action button placement. While the form provides the overall structure, the actions component handles the submission controls.
///

## Form End Component

The `form_end` component marks the end of form containers, providing the closing structure for complete form experiences. This component ensures proper form closure and handles any necessary cleanup or finalization functionality.

Form end components work with `form_start` components to create complete form boundaries, ensuring all form elements are properly contained and processed. They handle form-level functionality that occurs at the end of form processing.

/// admonition | Relationship
    type: info

The `form_end` component works with `form_start` components to define complete form boundaries. While the start component marks the beginning, the end component marks the conclusion of the form structure.
///

## Form Errors Component

The `form_errors` component displays form-wide error messages that provide feedback about issues affecting the entire form or multiple fields. These errors are distinct from field-specific errors and typically indicate broader validation or processing problems.

Form error components are displayed prominently within the form to ensure users notice critical issues that prevent form submission. They provide clear information about what went wrong and often include guidance about how to resolve the issues.

/// admonition | Relationship
    type: info

The `form_errors` component works within `form` containers alongside `field_errors` components. While field errors address specific input issues, form errors address broader validation or processing problems.
///

## Form Start Component

The `form_start` component marks the beginning of form containers, establishing the opening structure for complete form experiences. This component handles form initialization and sets up the necessary attributes and functionality for proper form operation.

Form start components work with `form_end` components to create complete form boundaries, ensuring all form elements are properly contained. They handle form-level attributes such as action URLs, method types, and encoding types that are necessary for proper form processing.

/// admonition | Relationship
    type: info

The `form_start` component works with `form_end` components to define complete form boundaries. While the start component establishes the form structure, the end component provides the conclusion.
///

## Hidden Input Component

The `hidden_input` component creates hidden form input elements that store data without displaying it to users. Hidden inputs are essential for maintaining state, security tokens, and other information that needs to be submitted with forms but shouldn't be visible or editable.

Hidden input components handle the proper HTML structure and attributes for hidden form fields, ensuring they're properly processed during form submission while remaining invisible to users. They maintain accessibility standards and proper form functionality.

## Input Component

The `input` component creates general text input fields for collecting user text input. This is one of the most fundamental form components, used for collecting various types of text data including names, email addresses, search terms, and other textual information.

Input components handle various input types such as text, email, password, and number fields, providing appropriate validation and formatting for each type. They ensure proper accessibility, styling, and functionality while maintaining consistency across different input contexts.

## Markdown Component

The `markdown` component creates markdown editor inputs that allow users to write content using markdown syntax. This component is particularly useful for forms where users need to create formatted content without dealing with complex WYSIWYG editors.

Markdown components provide syntax highlighting, preview functionality, and appropriate tooling to help users create well-formatted content using simple markdown syntax. They balance ease of use with formatting capabilities, making them suitable for various content creation scenarios.

## Radio Component

The `radio` component creates radio button input elements that allow users to select one option from a set of mutually exclusive choices. Radio buttons are essential for forms where users must choose a single option from multiple possibilities.

Radio components handle proper grouping, accessibility attributes, and visual styling to ensure users understand the selection constraints. They ensure that only one option can be selected within a group and provide clear visual feedback about the current selection.

## Range Input Component

The `range_input` component creates range slider inputs that allow users to select a value from a continuous range. This component is useful for forms where users need to specify values like ratings, quantities, or other continuous data.

Range input components provide visual feedback about the selected value and handle accessibility requirements for slider controls. They ensure proper keyboard navigation and screen reader support while maintaining intuitive interaction patterns.

## Select Component

The `select` component creates dropdown select input elements that allow users to choose from a predefined list of options. Select components are fundamental for forms where users need to choose from multiple options in a space-efficient manner.

Select components handle option display, selection management, and accessibility requirements. They work with `select_option` and `select_box` components to create complete selection experiences with proper structure and functionality.

/// admonition | Relationship
    type: info

The `select` component works with `select_option` and `select_box` components to create complete selection experiences. The select provides the container, while options provide the choices.
///

## Select Box Component

The `select_box` component creates containers for select input elements, providing the structural foundation for dropdown selection controls. This component handles the visual presentation and interaction patterns for select elements.

Select box components work with `select` and `select_option` components to create cohesive selection experiences. They ensure proper styling, positioning, and accessibility for dropdown controls while maintaining consistency across different themes.

/// admonition | Relationship
    type: info

The `select_box` component works with `select` and `select_option` components to create complete selection experiences. The box provides the container styling and structure.
///

## Select Option Component

The `select_option` component creates individual options within select input elements, providing the choices that users can select from dropdown lists. Each option represents a single choice within the selection control.

Select option components handle proper value assignment, display text, and selection states. They work within `select` elements to create the complete list of available choices, ensuring proper functionality and accessibility for each option.

/// admonition | Relationship
    type: info

The `select_option` component works within `select` elements to provide individual choices. While the select provides the container, options provide the available selections.
///

## Submit Component

The `submit` component creates form submission buttons that trigger form processing when clicked. Submit buttons are essential for form completion and must be clearly identifiable and appropriately styled to encourage user action.

Submit components handle form submission functionality, validation triggering, and appropriate visual styling to distinguish them from other buttons. They ensure proper accessibility and provide clear feedback about the submission action.

## Textarea Component

The `textarea` component creates multi-line text input fields that allow users to enter longer text content. Textareas are essential for forms where users need to provide detailed information, descriptions, comments, or other multi-line text input.

Textarea components handle appropriate sizing, scrolling behavior, and accessibility requirements for multi-line text input. They provide sufficient space for users to enter and edit longer content while maintaining proper form structure and validation capabilities.
