{% from "_macros.html" import parameters_table %}

{%raw%}
# Feedback

Feedback components are essential for user interaction and communication. They
provide ways to show notifications, request confirmations, display loading
states, and handle other interactive feedback mechanisms. Many of these
components work in pairs - for example, [`modal`][] components work with
`modal_handle` components, and [`popover`][] components work with
`popover_handle` components.

## Alert

The `alert` component displays notification and alert messages to users,
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

```django
<!-- Basic alert -->
{{ ui.alert("Operation completed successfully") }}

<!-- Dismissible alert -->
{{ ui.alert("This message can be dismissed", dismissible=true) }}

<!-- Alert with custom styling -->
{{ ui.alert("Warning: Check your input", style="danger") }}
```
///

{%endraw%}
{{parameters_table(component_ref.alert)}}
{%raw%}

/// details | Theme-Specific Parameters
    type: tip

- `variant` (string): Style variant (e.g., "filled", "outlined", "tonal")
- `elevation` (int): Shadow level (e.g., 0-24)
- `timeout` (int): Auto-dismiss timeout in milliseconds
- `icon` (string): Icon to display in the alert
///


## Modal

The `modal` component creates modal dialog containers that overlay the main
content to focus user attention on specific tasks or information. Modals are
used for forms, detailed views, settings, and any content that requires focused
user attention without navigating away from the current page.

Modal components handle overlay backgrounds, positioning, and interaction
patterns to ensure they capture user attention appropriately while remaining
accessible. They typically include close mechanisms and may prevent interaction
with the background content until dismissed. The component works with
`modal_handle` and `modal_close_handle` components to provide complete modal
interaction experiences.

There is a special version of modal dialog called `confirm_modal`. The
`confirm_modal` component creates confirmation dialog modals that require user
acknowledgment before proceeding with potentially important or destructive
actions. These modals are essential for preventing accidental data loss or
unintended operations by requiring explicit user confirmation.

Confirmation modals typically include clear messaging about the action to be
confirmed, prominent action buttons (usually "Confirm" and "Cancel"), and
sometimes additional context about the consequences of the action.

The confirm modal works by submitting a form when the user confirms the
action. In simple cases, it submits an empty form via POST, but you can specify
the ID of an existing form when building the `confirm_modal` - in this case,
that specific form will be submitted upon confirmation. This allows for
integration with existing form workflows.


/// admonition | Usage Example
    type: example

```django
<!-- Basic modal -->
{%- set id = ui.util.id() -%}
{{ ui.modal_handle("Open modal", id=id) }}
{{ ui.modal(lipsum(1), title="Standard modal", id=id) }}

<!-- Modal with multiple buttons -->
{%- set id = ui.util.id() -%}
{{ ui.modal_handle("Modal with actions", id=id) }}
{{ ui.modal(lipsum(1),
    title="Modal with footer",
    id=id,
    footer=ui.button("Do nothing") ~ ui.modal_close_handle("Close", id=id)) }}

<!-- Dismissible modal -->
{% call ui.util.call(ui.modal, title="Dismissible Modal", id="dismissible-modal", dismissible=true) %}
    Dismissible content
{% endcall %}
{{ ui.modal_handle("Open", id="dismissible-modal") }}

<!-- Confirmation modal -->
{%- set id = ui.util.id() -%}
{{ ui.modal_handle("Confirm modal", id=id) }}
{{ ui.confirm_modal(lipsum(1), title="Confirmation", id=id) }}

```
///

{%endraw%}

#### Modal

{{parameters_table(component_ref.modal)}}

#### Confirm modal

{{parameters_table(component_ref.confirm_modal)}}

{%raw%}


/// details | Theme-Specific Parameters
    type: tip

- `size` (string): Size of the modal (e.g., "sm", "md", "lg", "xl")
- `centered` (bool): Whether to center the modal vertically
- `scrollable` (bool): Whether the modal body should be scrollable
- `backdrop` (string): Backdrop style (e.g., "static", "true")
- `animation` (bool): Whether to use open/close animations
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

```django
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

```django
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

```django
<!-- Basic spinner -->
{{ ui.spinner() }}

<!-- Spinner with size -->
{{ ui.spinner(size="lg") }}
```
///

| Parameter | Type   | Default | Description                                                              |
|-----------|--------|---------|--------------------------------------------------------------------------|
| `size`    | string | "md"    | Size of the spinner (e.g., "sm", "md", "lg").                            |
| `style`   | string | -       | Visual style of the toast (e.g., "success", "warning", "error", "info"). |



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

```django
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

```django
<!-- Basic tooltip -->
{{ ui.tooltip("Button", tooltip="Click to submit the form") }}

<!-- Tooltip with position -->
{{ ui.tooltip("Info", tooltip="Additional information", position="top") }}
```
///
{%endraw%}
