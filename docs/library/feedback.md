{% from "_macros.html" import parameters_table %}
{% raw %}
# Feedback & Overlays

These components provide feedback to the user, such as notifications, loading
states, and interactive overlays.

## Notifications

### Alert

Immediate, prominent feedback often displayed inline or at the top of a page.
{% endraw %}
{{parameters_table(component_ref.alert, 'alert')}}
{% raw %}
### Toast

Brief, self-dismissing messages typically shown in the corner of the screen.
{% endraw %}
{{parameters_table(component_ref.toast_stack, 'toast_stack')}}
{{parameters_table(component_ref.toast, 'toast')}}
{% raw %}
## Overlays

### Modal

Dialog boxes that appear on top of the page content.

/// admonition | Usage Example
    type: example

```django
{%- set modal_id = ui.util.id() -%}
{{ ui.modal_handle(_("Open Modal"), id=modal_id) }}

{%- call ui.util.call(ui.modal, title=_("Example Modal"), id=modal_id) -%}
    <p>Modal content goes here.</p>
    {%- call ui.util.call(ui.form_actions) -%}
        {{ ui.modal_close_handle(_("Close"), id=modal_id) }}
    {%- endcall -%}
{%- endcall -%}
```
///
{% endraw %}
{{parameters_table(component_ref.modal, 'modal')}}
{{parameters_table(component_ref.confirm_modal, 'confirm_modal')}}
{{parameters_table(component_ref.modal_handle, 'modal_handle')}}
{{parameters_table(component_ref.modal_close_handle, 'modal_close_handle')}}
{% raw %}
### Popover

Small overlays that appear near a trigger element, often on click.
{% endraw %}
{{parameters_table(component_ref.popover, 'popover')}}
{{parameters_table(component_ref.popover_handle, 'popover_handle')}}
{% raw %}
### Tooltip

Brief informational text that appears on hover or focus.
{% endraw %}
{{parameters_table(component_ref.tooltip, 'tooltip')}}
{% raw %}
## Loading States

### Spinner

Animated icon indicating that an action is in progress.
{% endraw %}
{{parameters_table(component_ref.spinner, 'spinner')}}
{% raw %}
### Progress

Visual indicator of progress for long-running tasks.
{% endraw %}
{{parameters_table(component_ref.progress, 'progress')}}
