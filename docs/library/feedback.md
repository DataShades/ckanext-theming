# Feedback

Feedback components are essential for user interaction and communication. They
provide ways to show notifications, request confirmations, display loading
states, and handle other interactive feedback mechanisms. Many of these
components work in pairs - for example, [`modal`][] components work with
[`modal_handle`][modal-handle] components, and [`popover`][] components work
with [`popover_handle`][popover-handle] components.

## Alert

The [`alert`][] component displays notification and alert messages to users,
providing feedback about system status, errors, warnings, or successful
operations. Alerts are crucial for user experience as they provide immediate
feedback about actions taken or system conditions that users should be aware
of.

Alerts typically come in different styles to indicate different types of
information: success messages for completed actions, warnings for cautionary
information, errors for problems that need attention, and informational
messages for general notifications. The component handles consistent styling
and positioning to ensure messages are clearly visible and appropriately styled
based on their importance and type.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic alert -->
{{ ui.alert("Operation completed successfully") }}

<!-- Dismissible alert -->
{{ ui.alert("This message can be dismissed", dismissible=true) }}

<!-- Alert with custom styling -->
{{ ui.alert("Warning: Check your input", style="danger") }}
```
///

| Parameter     | Type   | Default | Description                                                              |
|---------------|--------|---------|--------------------------------------------------------------------------|
| `message`     | string | -       | The content to display in the alert.                                     |
| `dismissible` | bool   | -       | Whether the alert can be dismissed by the user.                          |
| `style`       | string | -       | Visual style of the alert (e.g., "success", "warning", "error", "info"). |

/// details | Theme-Specific Parameters
    type: tip

- `variant` (string): Style variant (e.g., "filled", "outlined", "tonal")
- `elevation` (int): Shadow level (e.g., 0-24)
- `timeout` (int): Auto-dismiss timeout in milliseconds
- `icon` (string): Icon to display in the alert
///

## Confirm Modal

The [`confirm_modal`][confirm-modal] component creates confirmation dialog modals that require
user acknowledgment before proceeding with potentially important or destructive
actions. These modals are essential for preventing accidental data loss or
unintended operations by requiring explicit user confirmation.

Confirmation modals typically include clear messaging about the action to be
confirmed, prominent action buttons (usually "Confirm" and "Cancel"), and
sometimes additional context about the consequences of the action. The
component works with [`modal_handle`][modal-handle] components to trigger the
confirmation dialog when needed.

The confirm modal works by submitting a form when the user confirms the
action. In simple cases, it submits an empty form via POST, but you can specify
the ID of an existing form when building the confirm_modal - in this case, that
specific form will be submitted upon confirmation. This allows for integration
with existing form workflows.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic confirm modal -->
{% call ui.util.call(ui.confirm_modal, title="Confirm Action", id="confirm-action") %}
    <p>Are you sure you want to perform this action?</p>
{% endcall %}
{{ ui.modal_handle("Open", id="confirm-action") }}

<!-- Confirm modal with custom form -->
{{ ui.confirm_modal(
    "Are you sure you want to delete this item? This action cannot be undone.",
    title="Confirm Delete",
    id="confirm-delete",
    form_id="delete-form"
) }}

{{ ui.form(
    ui.input(name="id", value="123"),
    method="POST",
    action="/dataset/delete",
    attrs={"id": "delete-form"}
) }}

{{ ui.modal_handle("Open", id="confirm-delete") }}

<!-- Confirm modal with custom buttons -->
{{ ui.confirm_modal(
    "Please confirm that you want to proceed with this operation.",
    title="Confirm Operation",
    id="confirm-operation",
    confirm_label="Yes, Proceed",
    cancel_label="No, Cancel"
) %}

{{ ui.modal_handle("Open", id="confirm-operation") }}
```
///

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | The main content to display in the confirmation modal. |
| `title` | string | - | The title displayed in the modal header. |
| `id` | string | - | Unique identifier for the modal. |
| `form_id` | string | - | ID of an existing form to submit when confirmed (instead of submitting an empty form). |
| `confirm_label` | string | "Confirm" | Label for the confirm button. |
| `cancel_label` | string | "Cancel" | Label for the cancel button. |

/// details | Theme-Specific Parameters
    type: tip

- `size` (string): Size of the modal (e.g., "sm", "md", "lg")
- `style` (string): Style variant (e.g., "primary", "danger")
- `backdrop` (string): Backdrop behavior (e.g., "static", "true")
- `animation` (bool): Whether to use open/close animations
///

/// admonition | Relationship
    type: info

The [`confirm_modal`][confirm-modal] component works with
[`modal_handle`][modal-handle] components to create interactive confirmation
experiences. While the modal provides the dialog structure, the handle provides
the trigger mechanism.

///

## Modal

The [`modal`][] component creates modal dialog containers that overlay the main
content to focus user attention on specific tasks or information. Modals are
used for forms, detailed views, settings, and any content that requires focused
user attention without navigating away from the current page.

Modal components handle overlay backgrounds, positioning, and interaction
patterns to ensure they capture user attention appropriately while remaining
accessible. They typically include close mechanisms and may prevent interaction
with the background content until dismissed. The component works with
[`modal_handle`][modal-handle] and [`modal_close_handle`][modal-close-handle]
components to provide complete modal interaction experiences.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic modal -->
{% call ui.util.call(ui.modal, title="Modal Title", id="my-modal", footer=ui.modal_close_handle("Close", id="my-modal")) %}
    Modal content goes here
{% endcall %}
{{ ui.modal_handle("Open", id="my-modal") }}

<!-- Modal with multiple buttons -->
{% set close = ui.modal_close_handle("Close", id="modal-with-footer") %}
{% set save = ui.button("Save") %}

{% call ui.util.call(ui.modal, title="Modal with Actions", id="modal-with-footer", footer=close ~ save) %}
    Content with footer
{% endcall %}
{{ ui.modal_handle("Open", id="modal-with-footer") }}

<!-- Dismissible modal -->
{% call ui.util.call(ui.modal, title="Dismissible Modal", id="dismissible-modal", dismissible=true) %}
    Dismissible content
{% endcall %}
{{ ui.modal_handle("Open", id="dismissible-modal") }}

```
///

| Parameter       | Type   | Default | Description                                                                |
|-----------------|--------|---------|----------------------------------------------------------------------------|
| `content`       | string | -       | The main content to display in the modal.                                  |
| `title`         | string | -       | The title displayed in the modal header.                                   |
| `id`            | string | -       | Unique identifier for the modal.                                           |
| `footer`        | string | -       | Content for the modal footer (typically action buttons).                   |
| `dismissible`   | bool   | -       | Whether the modal can be dismissed by clicking outside or pressing escape. |

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

The [`modal`][] component works with [`modal_handle`][modal-handle] and
[`modal_close_handle`][modal-close-handle] components to create complete modal
experiences. The modal provides the container, handles provide the interaction
mechanisms.

///

## Popover

The [`popover`][] component creates popover content containers that appear near
specific elements to provide additional information or controls. Popovers are
less intrusive than modals and are typically used for contextual help, quick
actions, or supplementary information that doesn't require full user focus.

Popover components handle positioning relative to their trigger elements,
ensuring they remain visible and accessible. They often appear on hover or
click and disappear when the user moves away or clicks elsewhere. The component
works with [`popover_handle`][popover-handle] components to provide the trigger
mechanism for showing and hiding popovers.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic popover -->
{% call ui.util.call(ui.popover, title="Help Information", id="help-popover") %}
    <p>This is helpful information about the current element.</p>
{% endcall %}
{{ ui.popover_handle("Show", id="help-popover") }}
```
///

| Parameter | Type   | Default | Description                                |
|-----------|--------|---------|--------------------------------------------|
| `content` | string | -       | The content to display in the popover.     |
| `title`   | string | -       | The title displayed in the popover header. |
| `id`      | string | -       | Unique identifier for the popover.         |

/// details | Theme-Specific Parameters
    type: tip

- `placement` (string): Position relative to trigger element (e.g., "top", "bottom", "left", "right")
- `trigger` (string): How to trigger the popover (e.g., "click", "hover")
- `delay` (int): Delay in milliseconds before showing/hiding
- `style` (string): Style variant (e.g., "primary", "secondary")
- `arrow` (bool): Whether to show an arrow pointing to the trigger element
///

/// admonition | Relationship
    type: info

The [`popover`][] component works with [`popover_handle`][popover-handle]
components to create contextual information displays. While the popover
provides the content container, the handle provides the trigger mechanism.

///

## Progress

The [`progress`][] component displays progress indicators that show the status
of ongoing operations such as file uploads, data processing, or other
time-consuming tasks. Progress indicators are important for user experience as
they provide feedback that operations are proceeding and give users an estimate
of remaining time.

Progress components typically show both visual progress (as a filled bar) and
numerical progress (as percentages or counts). They help prevent user
frustration by confirming that operations are progressing and provide
reassurance that the system is still responsive during longer operations.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic progress indicator -->
{{ ui.progress(value=50, max=100) }}

<!-- Progress with content -->
{{ ui.progress("50%", value=50, max=100) }}
```
///

| Parameter | Type   | Default | Description                                                                      |
|-----------|--------|---------|----------------------------------------------------------------------------------|
| `value`   | int    | 0       | Current progress value.                                                          |
| `max`     | int    | 100     | Maximum progress value.                                                          |
| `content` | string | -       | Content to display inside the progress bar. |

/// details | Theme-Specific Parameters
    type: tip

- `style` (string): Style variant (e.g., "primary", "success", "warning")
- `striped` (bool): Whether to use striped styling
- `animated` (bool): Whether to animate the progress bar
///

## Spinner

The [`spinner`][] component displays loading spinners that indicate ongoing
operations or content loading. Spinners are essential for providing immediate
feedback that the system is processing a request or loading content, preventing
users from taking additional actions that might cause conflicts.

Spinner components are typically small, animated elements that can be placed
inline with content or used as full-page overlays. They provide visual
confirmation that the system is active and processing, helping maintain user
confidence during operations that might otherwise appear to hang or freeze.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic spinner -->
{{ ui.spinner() }}

<!-- Spinner with size -->
{{ ui.spinner(size="lg") }}
```
///

| Parameter | Type   | Default | Description                                   |
|-----------|--------|---------|-----------------------------------------------|
| `size`    | string | "md"    | Size of the spinner (e.g., "sm", "md", "lg"). |

/// details | Theme-Specific Parameters
    type: tip

- `variant` (string): Style variant (e.g., "border", "grow", "dots")
- `color` (string): Color of the spinner
- `animation` (string): Animation type (e.g., "spin", "pulse", "bounce")
- `overlay` (bool): Whether to show as overlay with backdrop
///

## Toast

The [`toast`][] component displays toast notification messages that appear
briefly to provide feedback about operations or system events. Toast
notifications are less intrusive than alerts and typically disappear
automatically after a short period, making them ideal for non-critical
information that doesn't require user action.

Toast components are often used for confirming successful operations, providing
status updates, or alerting users to events that don't require immediate
attention. They typically appear in a corner of the screen and can be dismissed
manually or disappear automatically, ensuring they don't interfere with ongoing
user tasks.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic toast notification -->
{{ ui.toast("Operation completed successfully") }}

<!-- Toast with attributes -->
{{ ui.toast("Item saved", style="secondary") }}

<!-- Dismissible toast -->
{{ ui.toast("Informational message", dismissible=True) }}
```
///

| Parameter     | Type   | Default | Description                                                              |
|---------------|--------|---------|--------------------------------------------------------------------------|
| `content`     | string | -       | The message content to display in the toast.                             |
| `dismissible` | bool   | -       | Whether the toast can be dismissed by the user.                          |
| `style`       | string | -       | Visual style of the toast (e.g., "success", "warning", "error", "info"). |
| `duration`    | int    | -       | Duration in milliseconds before auto-dismissal.                          |

/// details | Theme-Specific Parameters
    type: tip

- `position` (string): Position on screen (e.g., "top-right", "bottom-left")
- `animation` (bool): Whether to use show/hide animations
///

## Tooltip

The [`tooltip`][] component displays tooltips that provide additional
information about elements when users hover over or focus on them. Tooltips are
essential for providing contextual help, explaining abbreviations, or offering
brief descriptions without cluttering the main interface.

Tooltip components handle positioning to ensure they remain visible and
readable, often appearing above, below, or to the side of the target
element. They provide a non-intrusive way to offer additional information that
enhances user understanding without requiring dedicated interface space.

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
