# Feedback

Feedback components provide interactive elements for user feedback, notifications, and modal interactions. These components help communicate with users and provide interactive experiences.

## Overview

Feedback components are essential for user interaction and communication. They provide ways to show notifications, request confirmations, display loading states, and handle other interactive feedback mechanisms. Many of these components work in pairs - for example, `modal` components work with `modal_handle` components, and `popover` components work with `popover_handle` components.

## Alert Component

The `alert` component displays notification and alert messages to users, providing feedback about system status, errors, warnings, or successful operations. Alerts are crucial for user experience as they provide immediate feedback about actions taken or system conditions that users should be aware of.

Alerts typically come in different styles to indicate different types of information: success messages for completed actions, warnings for cautionary information, errors for problems that need attention, and informational messages for general notifications. The component handles consistent styling and positioning to ensure messages are clearly visible and appropriately styled based on their importance and type.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic alert -->
{{ ui.alert("Operation completed successfully") }}

<!-- Dismissible alert -->
{{ ui.alert("This message can be dismissed", dismissible=True) }}

<!-- Alert with custom styling -->
{{ ui.alert("Warning: Check your input", attrs={"class": "alert-warning"}) }}
```
///

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `message` | string | - | The content to display in the alert. |
| `dismissible` | bool | - | Whether the alert can be dismissed by the user. |
| `style` | string | - | Visual style of the alert (e.g., "success", "warning", "error", "info"). |

/// details | Theme-Specific Parameters
    type: tip

- `variant` (string): Style variant (e.g., "filled", "outlined", "tonal")
- `elevation` (int): Shadow level (e.g., 0-24)
- `closable` (bool): Whether to show close button
- `timeout` (int): Auto-dismiss timeout in milliseconds
- `icon` (string): Icon to display in the alert
///

## Confirm Modal Component

The `confirm_modal` component creates confirmation dialog modals that require user acknowledgment before proceeding with potentially important or destructive actions. These modals are essential for preventing accidental data loss or unintended operations by requiring explicit user confirmation.

Confirmation modals typically include clear messaging about the action to be confirmed, prominent action buttons (usually "Confirm" and "Cancel"), and sometimes additional context about the consequences of the action. The component works with `modal_handle` components to trigger the confirmation dialog when needed.

/// admonition | Relationship
    type: info

The `confirm_modal` component works with `modal_handle` components to create interactive confirmation experiences. While the modal provides the dialog structure, the handle provides the trigger mechanism.
///

## Modal Component

The `modal` component creates modal dialog containers that overlay the main content to focus user attention on specific tasks or information. Modals are used for forms, detailed views, settings, and any content that requires focused user attention without navigating away from the current page.

Modal components handle overlay backgrounds, positioning, and interaction patterns to ensure they capture user attention appropriately while remaining accessible. They typically include close mechanisms and may prevent interaction with the background content until dismissed. The component works with `modal_handle` and `modal_close_handle` components to provide complete modal interaction experiences.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic modal -->
{% call ui.util.call(ui.modal, title="Modal Title", id="my-modal") %}
    Modal content goes here
{% endcall %}

<!-- Modal with footer -->
{% call ui.util.call(ui.modal, title="Modal with Actions", id="modal-with-footer", footer=(ui.button("Close") ~ ui.button("Save", style="primary"))) %}
    Content with footer
{% endcall %}

<!-- Dismissible modal -->
{% call ui.util.call(ui.modal, title="Dismissible Modal", id="dismissible-modal", dismissible=True) %}
    Dismissible content
{% endcall %}
```
///

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | The main content to display in the modal. |
| `title` | string | - | The title displayed in the modal header. |
| `id` | string | - | Unique identifier for the modal. |
| `footer` | string | - | Content for the modal footer (typically action buttons). |
| `dismissible` | bool | - | Whether the modal can be dismissed by clicking outside or pressing escape. |
| `dismiss_label` | string | - | Label for the dismiss/close button. |

/// details | Theme-Specific Parameters
    type: tip

- `size` (string): Size of the modal (e.g., "sm", "md", "lg", "xl")
- `centered` (bool): Whether to center the modal vertically
- `scrollable` (bool): Whether the modal body should be scrollable
- `backdrop` (string): Backdrop style (e.g., "static", "true")
- `animation` (bool): Whether to use open/close animations
///

/// admonition | Relationship
    type: info

The `modal` component works with `modal_handle` and `modal_close_handle` components to create complete modal experiences. The modal provides the container, handles provide the interaction mechanisms.
///

## Popover Component

The `popover` component creates popover content containers that appear near specific elements to provide additional information or controls. Popovers are less intrusive than modals and are typically used for contextual help, quick actions, or supplementary information that doesn't require full user focus.

Popover components handle positioning relative to their trigger elements, ensuring they remain visible and accessible. They often appear on hover or click and disappear when the user moves away or clicks elsewhere. The component works with `popover_handle` components to provide the trigger mechanism for showing and hiding popovers.

/// admonition | Relationship
    type: info

The `popover` component works with `popover_handle` components to create contextual information displays. While the popover provides the content container, the handle provides the trigger mechanism.
///

## Progress Component

The `progress` component displays progress indicators that show the status of ongoing operations such as file uploads, data processing, or other time-consuming tasks. Progress indicators are important for user experience as they provide feedback that operations are proceeding and give users an estimate of remaining time.

Progress components typically show both visual progress (as a filled bar) and numerical progress (as percentages or counts). They help prevent user frustration by confirming that operations are progressing and provide reassurance that the system is still responsive during longer operations.

## Spinner Component

The `spinner` component displays loading spinners that indicate ongoing operations or content loading. Spinners are essential for providing immediate feedback that the system is processing a request or loading content, preventing users from taking additional actions that might cause conflicts.

Spinner components are typically small, animated elements that can be placed inline with content or used as full-page overlays. They provide visual confirmation that the system is active and processing, helping maintain user confidence during operations that might otherwise appear to hang or freeze.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic spinner -->
{{ ui.spinner() }}

<!-- Spinner with size -->
{{ ui.spinner(size="lg") }}

<!-- Spinner with attributes -->
{{ ui.spinner(attrs={"class": "loading-spinner"}) }}
```
///

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `size` | string | "md" | Size of the spinner (e.g., "sm", "md", "lg"). |

/// details | Theme-Specific Parameters
    type: tip

- `variant` (string): Style variant (e.g., "border", "grow", "dots")
- `color` (string): Color of the spinner
- `animation` (string): Animation type (e.g., "spin", "pulse", "bounce")
- `full_screen` (bool): Whether to display as full-screen overlay
- `overlay` (bool): Whether to show as overlay with backdrop
///

## Toast Component

The `toast` component displays toast notification messages that appear briefly to provide feedback about operations or system events. Toast notifications are less intrusive than alerts and typically disappear automatically after a short period, making them ideal for non-critical information that doesn't require user action.

Toast components are often used for confirming successful operations, providing status updates, or alerting users to events that don't require immediate attention. They typically appear in a corner of the screen and can be dismissed manually or disappear automatically, ensuring they don't interfere with ongoing user tasks.

## Tooltip Component

The `tooltip` component displays tooltips that provide additional information about elements when users hover over or focus on them. Tooltips are essential for providing contextual help, explaining abbreviations, or offering brief descriptions without cluttering the main interface.

Tooltip components handle positioning to ensure they remain visible and readable, often appearing above, below, or to the side of the target element. They provide a non-intrusive way to offer additional information that enhances user understanding without requiring dedicated interface space.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic tooltip -->
{{ ui.tooltip("Button", tooltip="Click to submit the form") }}

<!-- Tooltip with position -->
{{ ui.tooltip("Info", tooltip="Additional information", position="top") }}

<!-- Tooltip with attributes -->
{{ ui.tooltip(ui.icon("help"), tooltip="Help information", attrs={"class": "help-tooltip"}) }}
```
///
