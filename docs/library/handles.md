# Handle Components

Handle components provide interactive elements for controlling other components like modals, panels, and popovers. These components enable user interaction with container elements.

## Overview

Handle components are interactive elements that allow users to control other UI components. They typically trigger actions like opening modals, expanding panels, or showing popovers. These components work in close relationship with their target components - for example, `modal_handle` components work with `modal` components, and `panel_handle` components work with `panel` components.

## Modal Close Handle Component

The `modal_close_handle` component provides interactive elements specifically designed for closing modal dialogs. This component creates the close button or other interface elements that allow users to dismiss modal content and return to the main interface.

Modal close handles are essential for proper modal functionality and accessibility, providing users with a clear way to exit modal content. They typically appear as "X" buttons in modal headers or as overlay areas that close the modal when clicked. The component ensures proper accessibility attributes and keyboard navigation support for modal closing functionality.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic modal close handle -->
{{ ui.modal_close_handle("Close", id="my-modal") }}

<!-- Modal close handle with attributes -->
{{ ui.modal_close_handle(ui.icon("times"), id="modal-id", attrs={"class": "close-btn"}) }}
```
///

/// admonition | Relationship
    type: info

The `modal_close_handle` component works with `modal` components to provide complete modal interaction experiences. While the modal provides the content container, the close handle provides the dismissal mechanism.
///

## Modal Handle Component

The `modal_handle` component provides interactive elements that trigger the opening of modal dialogs. This component creates buttons, links, or other interface elements that, when activated, display modal content to the user.

Modal handles are the primary interface for initiating modal experiences, whether for forms, detailed views, confirmations, or other content that benefits from focused attention. The component handles proper event binding, accessibility attributes, and ensures smooth modal opening transitions. It works closely with `modal` components to create complete modal experiences.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic modal handle -->
{{ ui.modal_handle("Open Modal", id="my-modal") }}

<!-- Modal handle with attributes -->
{{ ui.modal_handle(ui.icon("plus") ~ " Add Item", id="add-modal", attrs={"class": "btn btn-primary"}) }}
```
///

/// admonition | Relationship
    type: info

The `modal_handle` component works with `modal` components to create complete modal experiences. While the handle provides the trigger mechanism, the modal provides the content container.
///

## Panel Handle Component

The `panel_handle` component provides interactive elements for controlling panel components, typically serving as the clickable area that expands or collapses panel content. Panel handles are essential for accordion-style interfaces and expandable content sections.

Panel handles create the user interface for toggling panel visibility, often displaying indicators about the current state (expanded or collapsed) and providing clear visual feedback when interacted with. The component ensures proper accessibility attributes and keyboard navigation support, making panel controls usable for all users. It works with `panel` and `panel_wrapper` components to create complete panel experiences.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic panel handle -->
{{ ui.panel_handle("Toggle Panel", id="panel-id") }}

<!-- Panel handle with attributes -->
{{ ui.panel_handle(ui.icon("chevron-down") ~ " Panel Title", id="panel-id", attrs={"class": "panel-toggle"}) }}
```
///

/// admonition | Relationship
    type: info

The `panel_handle` component works with `panel` and `panel_wrapper` components to create expandable panel experiences. While the panel provides the content container, the handle provides the control mechanism.
///

## Popover Handle Component

The `popover_handle` component provides interactive elements that trigger the display of popover content. This component creates the interface elements that, when activated (typically through hover or click), show additional information or controls in a popover container.

Popover handles are designed to be unobtrusive yet clearly identifiable, providing contextual information without requiring dedicated interface space. The component handles proper event binding, positioning calculations, and accessibility attributes to ensure popovers are both functional and accessible. It works with `popover` components to create complete popover experiences.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic popover handle -->
{{ ui.popover_handle("?", id="help-popover") }}

<!-- Popover handle with attributes -->
{{ ui.popover_handle(ui.icon("info"), id="info-popover", attrs={"class": "help-icon"}) }}
```
///

/// admonition | Relationship
    type: info

The `popover_handle` component works with `popover` components to create contextual information displays. While the handle provides the trigger mechanism, the popover provides the content container.
///
