{%raw%}
# Handles

Handle components are interactive elements that allow users to control other UI
components. They typically trigger actions like opening modals, or showing
popovers. These components work in close relationship with their target
components - for example, `modal_handle` components work with
[`modal`][] components.


## Popover Handle

The [`popover_handle`][popover-handle] component provides interactive elements
that trigger the display of popover content. This component creates the
interface elements that, when activated (typically through hover or click),
show additional information or controls in a popover container.

Popover handles are designed to be unobtrusive yet clearly identifiable,
providing contextual information without requiring dedicated interface
space. The component handles proper event binding, positioning calculations,
and accessibility attributes to ensure popovers are both functional and
accessible. It works with [`popover`][] components to create complete popover
experiences.

/// admonition | Usage Example
    type: example

```django
<!-- Basic popover handle -->
{{ ui.popover_handle("?", id="help-popover") }}
```
///

/// admonition | Relationship
    type: info

The [`popover_handle`][popover-handle] component works with [`popover`][]
components to create contextual information displays. While the handle provides
the trigger mechanism, the popover provides the content container.

///
{%endraw%}
