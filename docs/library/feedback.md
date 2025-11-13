# Feedback

Feedback macros provide components for communicating with users, providing notifications, collecting user feedback, and displaying system status. These components enhance the user experience by providing clear, timely information about system state and user actions.

## `alert`

Displays an alert message to inform users about important information, success states, warnings, or error conditions. Alerts provide a salient way to communicate status updates and important information.

**Use Cases:**

- Success messages after form submission
- Error notifications
- Warning messages
- Important notices
- System status updates
- Confirmation messages

**Usage Context:**

Use to communicate immediate feedback about user actions or system states. Position where users expect system feedback, typically near the top of content areas.

**Example:**

```
{{ ui.alert("Your changes have been saved successfully!", style="success") }}
{{ ui.alert("Please review the highlighted fields for corrections.", style="warning") }}
{{ ui.alert("An error occurred while processing your request.", style="danger") }}
```

**Arguments:**

- `style` (string): Visual styling of the alert. One of "primary", "secondary", "info", "success", "warning", "danger". Defaults to "info".

**Recommendations:**

- Use appropriate alert styles (info, success, warning, danger)
- Different themes provide various alert styles (Bootstrap: .alert, .alert-success, Tailwind: bg-green-100 text-green-800, Bulma: .notification)
- Keep messages concise and actionable
- Include dismiss functionality when appropriate
- Ensure proper contrast for accessibility
- Consider auto-dismiss for non-critical alerts

## `toast`

Displays a temporary notification that appears briefly at the edge of the screen. Toasts provide unobtrusive, time-limited messages that don't interrupt user workflow.

**Use Cases:**

- Quick status updates
- Confirmation of actions
- Minor notifications
- Background process feedback
- Discrete feedback

**Usage Context:**

Use for brief notifications that don't require immediate attention, allowing users to continue their current task without interruption.

**Example:**

```
{{ ui.toast("Item added to cart", style="success") }}
{{ ui.toast("Preferences saved", style="info") }}
```

**Arguments:**

- `style` (string): Visual styling of the toast. One of "primary", "secondary", "info", "success", "warning", "danger". Defaults to "info".

**Recommendations:**

- Use for non-critical, brief messages
- Different themes implement toasts differently (Bootstrap: .toast, Tailwind: fixed positioning, Bulma: .toast)
- Set appropriate display duration (typically 3-6 seconds)
- Position consistently on screen
- Include appropriate visual styling for accessibility
- Provide a way to manually dismiss if needed

## `modal`

Renders an overlay modal dialog for focused interaction that requires user attention. Modals temporarily interrupt normal workflow to request confirmation, display important information, or collect specific input.

**Use Cases:**

- Confirmation dialogs
- Critical information display
- Form overlays
- Image or content preview
- Multi-step processes
- Detailed options configuration

**Usage Context:**

Use for interactions that require immediate user attention and decision-making, temporarily focusing user attention on a specific task.

**Example:**

```
{{ ui.modal(title="Delete Confirmation", body="Are you sure you want to delete this item? This action cannot be undone.", footer=ui.button("Delete", style="danger", type="button") + ui.button("Cancel", style="secondary", type="button")) }}
```

**Recommendations:**

- Use sparingly to avoid disrupting workflow
- Include clear title and actionable content
- Different themes provide various modal implementations (Bootstrap: .modal, Tailwind: backdrop-filter, Bulma: .modal)
- Ensure proper keyboard navigation and focus management
- Include clear close mechanisms
- Consider mobile responsiveness

## `tooltip`

Provides a brief hint or explanation that appears on hover or focus. Tooltips offer contextual information without cluttering the interface.

**Use Cases:**

- Icon explanations
- Button functionality
- Abbreviation meanings
- Field clarifications
- Accessible additional information

**Usage Context:**

Use for supplementary information that helps users understand interface elements without obstructing the main content.

**Example:**

```
{{ ui.tooltip("Click to save your work") }}
  {{ ui.button("Save", style="primary", type="button") }}
{{ ui.tooltip() }}
```

**Recommendations:**

- Keep text brief (1-2 words or short phrase)
- Different themes implement tooltips differently (Bootstrap: data-bs-toggle, Tailwind: group/tooltip, Bulma: tooltip)
- Ensure proper accessibility with ARIA attributes
- Don't rely solely on tooltips for critical information
- Consider touch interfaces where hover isn't available

## `popover`

Displays a popup panel with more detailed information or options than a tooltip. Popovers provide richer content than tooltips while remaining contextual to their triggering element.

**Use Cases:**

- Detailed explanations
- Rich content previews
- Action menus
- Extended field information
- Interactive content

**Usage Context:**

Use when you need to display more information or functionality than a simple tooltip, but still want to maintain context with the triggering element.

**Example:**

```
{{ ui.popover(title="Advanced Settings", content="Configure additional options for this feature...") }}
  {{ ui.button("Settings", style="secondary", type="button") }}
{{ ui.popover() }}
```

**Recommendations:**

- Use for richer content than tooltips can accommodate
- Different themes provide various popover styles (Bootstrap: .popover, Tailwind: dropdown-style, Bulma: .dropdown)
- Ensure proper positioning and dismissal
- Don't overload with too much content
- Consider mobile touch behavior

## `progress`

Displays a progress bar to indicate percentage completion of a task. Progress bars provide visual feedback about ongoing operations and estimated completion times.

**Use Cases:**

- File upload progress
- Data processing
- Multi-step forms
- Loading indicators
- Task completion

**Usage Context:**

Use when users need to understand how much of a task has been completed and how much remains, especially for operations that take multiple seconds.

**Example:**

```
{{ ui.progress(value=75, max=100, label="Uploading files... 75%") }}
```

**Recommendations:**

- Update values dynamically for accurate representation
- Different themes style progress bars differently (Bootstrap: .progress, Tailwind: progress element, Bulma: .progress)
- Include textual percentage when possible
- Consider determinate vs indeterminate progress
- Provide estimated time remaining when known

## `spinner`

Displays a loading indicator to show ongoing processing or waiting state. Spinners provide visual feedback that the system is processing or fetching data.

**Use Cases:**

- Page loading
- Data fetching
- Processing states
- Waiting for responses
- Background operations

**Usage Context:**

Use when the system needs to indicate that processing is happening, preventing users from thinking the system is frozen.

**Example:**

```
{{ ui.spinner(size="md") }}
```

**Recommendations:**

- Use appropriate size for context
- Different themes provide various spinner implementations (Bootstrap: .spinner, Tailwind: animate-spin, Bulma: .loader)
- Consider combining with text labels for clarity
- Use consistently across the application
- Consider accessibility with ARIA labels
