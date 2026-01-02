
# Containers

Container components form the building blocks of page layouts, providing
structure and organization for other UI elements. They help create visual
hierarchy and group related content together. Many container components work in
pairs - for example, [`list`][] containers work with [`list_item`][list-item]
elements, and [`grid`][] containers work with [`column`][] elements.

## Accordion

The [`accordion`][] component creates collapsible content sections that allow
users to expand and collapse content as needed. This component is particularly
useful for organizing large amounts of information in a space-efficient manner,
allowing users to focus on relevant sections while keeping the interface
uncluttered.

Accordions are commonly used for FAQ sections, detailed metadata displays, and
any content that benefits from progressive disclosure. The component typically
includes a header that serves as the toggle control and a content area that
expands or collapses. It works with [`accordion_wrapper`][accordion-wrapper] to
provide consistent grouping of multiple accordion sections.

/// admonition | Relationship
    type: info

The [`accordion`][] component works with
[`accordion_wrapper`][accordion-wrapper] to create organized accordion
groups. While individual accordions handle single collapsible sections, the
wrapper provides the container for multiple accordions.

///

/// admonition | Usage Example
    type: example

```jinja2
<!-- Simple accordion -->
{%- call ui.util.call(ui.accordion_wrapper) -%}
    {%- call ui.util.call(ui.accordion, title="More Information") -%}
        Detailed information about this section
    {%- endcall %}
{%- endcall %}

<!-- Open accordion by default -->
{{ ui.accordion_wrapper(
    ui.accordion("Detailed information about this section", title="More Information")
) }}
```
///

| Parameter | Type   | Default | Description                                            |
|-----------|--------|---------|--------------------------------------------------------|
| `content` | string | -       | The content to display when the accordion is expanded. |
| `title`   | string | -       | The title displayed in the accordion header.           |
| `open`    | bool   | -       | Whether the accordion should be open by default.       |

/// details | Theme-Specific Parameters
    type: tip

- `style` (string): Style variant (e.g., "primary", "secondary")
- `flush` (bool): Whether to remove borders and rounded corners
- `independent` (bool): Whether the accordion should remain open when sibling accordion is opened
///


## Button Group

The [`button_group`][button-group] component groups related buttons together,
providing visual cohesion and indicating that the buttons are functionally
related. This component is useful for grouping action buttons, toggle buttons,
or any set of buttons that perform related functions.

Button groups help users understand the relationship between different actions
and provide a cleaner interface than individual buttons scattered throughout
the layout. The component ensures consistent spacing and alignment between
grouped buttons, regardless of the underlying CSS framework.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Group of action buttons -->
{{ ui.button_group(
    ui.button("Edit", href="/edit")
    ~ ui.button("Delete", href="/delete", style="danger")
) }}

<!-- Group with vertical direction -->
{%- call ui.util.call(uibutton_group, direction="column") -%}
    {{ ui.button("First") }}
    {{ ui.button("Second") }}
    {{ ui.button("Third") }}
{%- endcall %}

```
///

| Parameter   | Type   | Default | Description                                                                      |
|-------------|--------|---------|----------------------------------------------------------------------------------|
| `content`   | string | -       | The buttons to group together.                                                   |
| `direction` | string | "row"   | The direction of the button group ("row" for horizontal, "column" for vertical). |

/// details | Theme-Specific Parameters
    type: tip

- `size` (string): Size of the button group (e.g., "sm", "lg")
- `toolbar` (bool): Whether to use toolbar styling
- `justified` (bool): Whether to make buttons equal width
///

## Card

The [`card`][] component provides a self-contained container for related
content, typically featuring a header, body, and optional footer. Cards are
versatile containers that can display various types of content including text,
images, buttons, and other components. They provide visual separation from
surrounding content and create a consistent appearance for similar content
blocks.

Cards are particularly effective for displaying collections of related
information such as dataset summaries, user profiles, or content previews. The
component handles consistent styling, spacing, and layout across different
themes while maintaining the flexibility to accommodate various content types.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic card -->
{{ ui.card("Dataset description goes here", title="Dataset Title") }}

<!-- Card with image -->
{{ ui.card("Description", title="Dataset Title", img="/path/to/image.jpg") }}

<!-- Card with link -->
{{ ui.card("Description", title="Dataset Title", href="/dataset/123") }}

<!-- Card with footer -->
{{ ui.card("Description", title="Dataset Title", footer="Updated: 2023-01-01") }}
```
///

| Parameter | Type   | Default | Description                             |
|-----------|--------|---------|-----------------------------------------|
| `content` | string | -       | The main content of the card.           |
| `title`   | string | -       | The title displayed in the card header. |
| `footer`  | string | -       | Content for the card footer.            |
| `img`     | string | -       | URL to an image to display in the card. |
| `href`    | string | -       | URL to link the entire card to.         |

/// details | Theme-Specific Parameters
    type: tip

- `style` (string): Style variant (e.g., "primary", "secondary", "outline")
- `direction` (string): Stack image and content horizontally instead of vertically (e.g., "row", "column")
- `size` (string): Size of the card (e.g., "sm", "lg")
- `outline` (bool): Whether to use outline style
- `clickable` (bool): Whether the card should have hover effects indicating clickability
- `shadow` (string): Shadow level (e.g., "none", "sm", "lg")
///

## Column

The [`column`][] component defines individual columns within grid layouts,
working in conjunction with the [`grid`][] component to create responsive,
structured layouts. Columns allow content to be organized horizontally in a
flexible manner, adapting to different screen sizes and device types.

The column component typically accepts parameters for responsive behavior,
allowing developers to specify how many columns an element should span on
different screen sizes. This component is fundamental to creating modern,
responsive layouts that work well across desktop, tablet, and mobile devices.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Simple column (1/12) -->
{%- call ui.util.call(ui.grid) -%}
    {{ ui.column("Content in a column") }}
{%- endcall %}

<!-- Column with responsive span -->
{%- call ui.util.call(ui.grid) -%}
    {{ ui.column("Responsive column", span={"xs": 12, "md": 6, "lg": 4}) }}
{%- endcall %}
```
///

| Parameter | Type   | Default | Description                                                                   |
|-----------|--------|---------|-------------------------------------------------------------------------------|
| `content` | string | -       | The content to display in the column.                                         |
| `span`    | dict   | -       | Responsive span configuration with breakpoints (e.g., `{"xs": 12, "md": 6}`). |

/// details | Theme-Specific Parameters
    type: tip

- `offset` (dict): Offset configuration for pushing/pulling columns
- `order` (dict): Order configuration for reordering columns
- `align` (string): Self-alignment (e.g., "start", "center", "end")
- `gutters` (bool): Whether to remove gutters between columns
///

/// admonition | Relationship
    type: info

The [`column`][] component works with [`grid`][] components to create
structured layouts. While the grid provides the overall layout structure,
columns define the individual content areas within that structure.

///

## Container

The [`container`][] component provides the main structural container for page
content, establishing the primary layout boundaries and responsive
behavior. This component typically handles the maximum width, centering, and
padding for main content areas, ensuring consistent spacing and alignment
throughout the application.

Container components are essential for maintaining visual consistency across
different pages and sections of the application. They provide the foundational
structure upon which other layout components are built, ensuring that content
maintains proper margins and alignment regardless of the underlying CSS
framework.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic container -->
{{ ui.container("Content within a container") }}

<!-- Fluid container -->
{{ ui.container("Full-width content", fluid=true) }}
```
///

| Parameter | Type   | Default | Description                                                             |
|-----------|--------|---------|-------------------------------------------------------------------------|
| `content` | string | -       | The content to display within the container.                            |
| `fluid`   | bool   | -       | Whether to make the container full-width without max-width constraints. |

/// details | Theme-Specific Parameters
    type: tip

- `size` (string): Container size (e.g., "sm", "md", "lg", "xl")
- `centered` (bool): Whether to center the container
- `padding` (string): Padding level (e.g., "sm", "md", "lg")
- `gutter` (string): Gutter size for responsive spacing
///

## Grid

The [`grid`][] component creates structured grid layouts that organize content
in rows and columns. It works with [`column`][] components to define the
overall layout structure, providing responsive behavior and consistent spacing
between elements. Grid components are fundamental to creating modern, flexible
layouts that adapt to different screen sizes.

Grid layouts are particularly useful for displaying collections of similar
content such as dataset cards, user profiles, or content thumbnails. The
component handles complex responsive behavior, ensuring that content reflows
appropriately on different devices while maintaining visual consistency.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic grid -->
{%- call ui.util.call(ui.grid) -%}
    {{ ui.column("Item 1", span={"xs": 12, "md": 6}) }}
    {{ ui.column("Item 2", span={"xs": 12, "md": 6}) }}
{%- endcall %}
```
///

| Parameter | Type   | Default | Description                                                 |
|-----------|--------|---------|-------------------------------------------------------------|
| `content` | string | -       | The content to display within the grid (typically columns). |

/// details | Theme-Specific Parameters
    type: tip

- `gap` (string): Gap between grid items (e.g., "sm", "md", "lg")
- `align_items` (string): Alignment of items (e.g., "start", "center", "end")
- `justify_content` (string): Justification of content (e.g., "start", "center", "end")
- `direction` (string): Direction of the grid (e.g., "row", "column")
- `reverse` (bool): Whether to reverse the direction
///

/// admonition | Relationship
    type: info

The [`grid`][] component works with [`column`][] components to create
structured layouts. The grid provides the overall structure, while columns
define the individual content areas within that structure.

///

## List

The [`list`][] component provides a container for collections of items, working
with [`list_item`][list-item] components to create structured content
displays. This component handles consistent spacing, styling, and layout for
list content, ensuring that items are properly aligned and visually distinct.

List components are fundamental for displaying collections of related items,
navigation menus, or any content that benefits from sequential
organization. The component provides flexibility for both ordered and unordered
lists while maintaining consistent styling across different themes.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic list -->
{%- call ui.util.call(ui.list) -%}
    {{ ui.list_item("Item 1") }}
    {{ ui.list_item("Item 2") }}
    {{ ui.list_item("Item 3") }}
{%- endcall %}
```
///

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | The content to display in the list (typically list items). |

/// details | Theme-Specific Parameters
    type: tip

- `ordered` (bool): Whether to use ordered list (numbers) instead of unordered
- `variant` (string): Style variant (e.g., "flush", "inline")
- `size` (string): Size of the list (e.g., "sm", "lg")
- `divider` (bool): Whether to show dividers between items
- `horizontal` (bool): Whether to display items horizontally
///

/// admonition | Relationship
    type: info

The `list` component works with `list_item` components to create structured
lists. While the list provides the container structure, individual list items
provide the content within that structure.

///

## List Item

The [`list_item`][list-item] component represents individual items within list
containers, providing consistent styling and behavior for list elements. Each
list item works within the context of a [`list`][] component to create cohesive
list displays. List items can contain various types of content including text,
links, images, and other components.

List items are essential for creating organized content displays, navigation
menus, and any interface element that benefits from sequential
presentation. The component ensures proper spacing, alignment, and styling
within the broader list structure.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic list item -->
{{ ui.list_item("Simple list item") }}

<!-- List item with attributes -->
{{ ui.list_item("Styled list item", attrs={"class": "active"}) }}

<!-- List item with complex content -->
{{ ui.list_item(ui.link("Link in list", href="/page") ~ ui.badge("New")) }}
```
///

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | The content to display in the list item. |

/// details | Theme-Specific Parameters
    type: tip

- `active` (bool): Whether the item is currently active/selected
- `disabled` (bool): Whether the item is disabled
- `style` (string): Style variant (e.g., "primary", "secondary")
- `action` (bool): Whether the item is an action item
///

/// admonition | Relationship
    type: info

The [`list_item`][list-item] component works within [`list`][] components to
create structured lists. While the list provides the container, individual list
items provide the content elements within that container.

///

## Panel

The [`panel`][] component creates content containers that can be switched
between using [`panel_handle`][panel-handle] components. Unlike accordions
which are visually collapsible, panels are completely hidden when not active
and only one panel is typically visible at a time. This makes them ideal for
tab-like interfaces where users can switch between different content sections.

Panels are useful for organizing related content in a way that maximizes space
efficiency while allowing users to focus on one section at a time. The
component works with [`panel_handle`][panel-handle] components to provide the
switching mechanism and [`panel_wrapper`][panel-wrapper] to provide the
container structure for multiple panels.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic panel -->
{{ panel_handle("Show #1", id="panel-1") }}
{{ panel_handle("Show #2", id="panel-2") }}

{%- call ui.util.call(ui.panel_wrapper) -%}
    {{ ui.panel("Panel #1 content goes here", id="panel-1") }}
    {{ ui.panel("Panel #2 content goes here", id="panel-2") }}
{%- endcall %}


<!-- Active panel -->
{%- call ui.util.call(ui.panel_wrapper) -%}
    {{ ui.panel("Visible panel content", id="panel-2", active=true) }}
    {{ ui.panel("Hidden panel content", id="panel-2") }}
{%- endcall %}
```
///

| Parameter | Type   | Default | Description                                     |
|-----------|--------|---------|-------------------------------------------------|
| `content` | string | -       | The content to display in the panel.            |
| `id`      | string | -       | Unique identifier for the panel.                |
| `active`  | bool   | -       | Whether the panel is active/visible by default. |


/// details | Theme-Specific Parameters
    type: tip

- `collapsible` (bool): Whether the panel can be collapsed (vs. switched)
- `outline` (bool): Whether to use outline style
///

/// admonition | Relationship
    type: info

The [`panel`][] component works with [`panel_wrapper`][panel-wrapper] and
[`panel_handle`][panel-handle] components to create tab-like switching
experiences. The panel provides the content structure, the wrapper provides the
container for multiple panels, and the handle provides the switching mechanism.

///
