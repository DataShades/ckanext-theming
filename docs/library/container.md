# Container

Container macros provide layout structures and grouping elements that help organize content in a visually appealing and semantically correct way. These components are theme-agnostic and can be customized with different CSS frameworks for styling and responsiveness.

## `accordion_wrapper`

Wraps an accordion component to provide proper container styling and structure. Serves as the parent container for multiple accordion items, handling the overall appearance and behavior of the accordion group.

**Use Cases:**

- FAQ sections
- Configuration panels
- Content organization
- Space-efficient information display

**Usage Context:**

Use when you need to present multiple content sections that can be individually expanded or collapsed to save screen space and organize related information.

**Example:**

```
{{ ui.accordion_wrapper(
  ui.accordion_item(title="First Item", open=true) +
  ui.accordion_item(title="Second Item") +
  ui.accordion_item(title="Third Item")
) }}
```

**Recommendations:**

- Group related content together in a single wrapper
- Different themes may apply different styling (Bootstrap: .accordion, Tailwind: space-y-2, Bulma: accordion wrapper)
- Consider accessibility implications when implementing accordion behavior

## `accordion_item`

Creates a single expandable/collapsible item within an accordion. Provides a title header that toggles the visibility of associated content, helping to organize information while conserving space.

**Use Cases:**

- Frequently asked questions
- Settings panels
- Content categorization
- Expandable content sections

**Usage Context:**

Use within an `accordion_wrapper` to create individual expandable sections. Each item should contain information that can be understood independently from other items.

**Example:**

```
{% call ui.accordion_item(title="How do I sign up?", open=true) %}
  <p>Visit our registration page and fill out the form with your details.</p>
{% endcall %}
```

**Recommendations:**

- Keep titles concise and descriptive
- Different themes may customize the toggle behavior (Bootstrap: data-bs-toggle, Tailwind: requires JavaScript, Bulma: details/summary)
- Set `open=true` for important content that should be visible by default

## `card`

Renders a card component for grouping related content in a visually distinct container. Cards are versatile elements that can contain images, text, actions, and other content in an organized, self-contained unit.

**Use Cases:**

- Product listings
- Content previews
- User profiles
- Dashboard widgets
- Blog post previews

**Usage Context:**

Use for displaying related information in a self-contained, visually distinct container that stands out from surrounding content.

**Example:**

```
{{ ui.card(
  title="Product Feature",
  content="This feature allows users to quickly access important information.",
  img="/images/feature.jpg",
  href="/features/123",
  footer="Updated: Today"
) }}
```

**Recommendations:**

- Use consistent sizing within the same context
- Different themes provide various card implementations (Bootstrap: .card, Tailwind: shadow rounded-lg, Bulma: .card)
- Include a clear call-to-action or link when appropriate

## `column`

Creates a single column within a grid layout system. Provides responsive layout capabilities by creating flexible content containers that adapt to screen size.

**Use Cases:**

- Responsive grid layouts
- Content organization
- Multi-column layouts
- Flexible content arrangement

**Usage Context:**

Use within a grid system to create individual content containers that adjust based on available space and screen size.

**Example:**

```
{{ ui.grid(
  ui.column("Column 1 content") +
  ui.column("Column 2 content") +
  ui.column("Column 3 content")
) }}
```

**Recommendations:**

- Use with grid containers for proper layout
- Different themes implement column systems differently (Bootstrap: .col, Tailwind: flex-1, Bulma: .column)
- Consider responsive behavior across different screen sizes

## `container`

Creates a responsive container block with appropriate margins, padding, and maximum width. Provides a consistent content wrapper that centers content and provides appropriate spacing.

**Use Cases:**

- Main page content wrapper
- Section content containers
- Consistent layout structure
- Responsive content organization

**Usage Context:**

Use as the primary wrapper for main content areas to ensure consistent spacing and responsive behavior across different screen sizes.

**Example:**

```
{{ ui.container("Main page content", fluid=false) }}
```

**Recommendations:**

- Use as the primary wrapper for main content
- Different themes provide various options (Bootstrap: .container, .container-fluid; Tailwind: max-w-7xl; Bulma: .container)
- Set `fluid=true` for full-width layouts when needed

## `grid`

Creates a grid layout system for organizing content in responsive rows and columns. Provides a structured way to arrange content in a grid format that adapts to different screen sizes.

**Use Cases:**

- Dashboard layouts
- Product listings
- Image galleries
- Content organization
- Responsive design

**Usage Context:**

Use when you need to arrange content in a grid format with responsive behavior across different screen sizes.

**Example:**

```
{{ ui.grid(
  ui.column("Item 1") +
  ui.column("Item 2") +
  ui.column("Item 3"),
  columns=3
) }}
```

**Recommendations:**

- Define appropriate number of columns for the content
- Different themes implement grid systems differently (Bootstrap: .row with .col, Tailwind: grid, Bulma: .columns)
- Consider mobile responsiveness when designing grid layouts

## `panel`

Creates a panel block for grouping related content with optional title. Panels provide a structured way to organize content sections with clear visual separation.

**Use Cases:**

- Settings sections
- Content grouping
- Dashboard sections
- Information organization
- Administrative interfaces

**Usage Context:**

Use when you need to group related content together with a clear header, often in administrative or configuration interfaces.

**Example:**

```
{{ ui.panel("Panel content goes here", title="Panel Title") }}
```

**Recommendations:**

- Use for grouping related content sections
- Different themes may implement panels differently (Bootstrap: .card, Tailwind: bg-white shadow, Bulma: .panel or .card)
- Consider accessibility when using panels for navigation

## `row`

Creates a horizontal row block within a container system. Provides proper alignment and spacing for horizontal content arrangement.

**Use Cases:**

- Horizontal content arrangement
- Grid system implementation
- Responsive layout structure
- Content organization

**Usage Context:**

Use within container systems to create horizontal arrangements of content that can contain multiple columns.

**Example:**

```
{{ ui.row(ui.column("Column 1") + ui.column("Column 2")) }}
```

**Recommendations:**

- Use within container systems for proper layout
- Different themes implement rows differently (Bootstrap: .row, Tailwind: flex, Bulma: .columns)
- Ensure proper column count within rows for responsive behavior

## `section`

Creates a semantic section block with appropriate spacing and structure. Provides a way to group related content in a semantically meaningful container.

**Use Cases:**

- Content sections
- Page organization
- Semantic grouping
- Layout structure

**Usage Context:**

Use to create distinct sections of content that have a common purpose or theme, providing semantic meaning and appropriate spacing.

**Example:**

```
{{ ui.section("Content for this section goes here") }}
```

**Recommendations:**

- Use for semantic content grouping
- Different themes may add default spacing (Bootstrap: py-5, Tailwind: py-12, Bulma: section)
- Consider using with headings to provide proper document structure

## `jumbotron`

Creates a jumbotron container for featured content.

### Arguments

*   `content` (string): content of the jumbotron.
*   `title` (string): title for the jumbotron. Defaults to `None`.
*   `subtitle` (string): subtitle for the jumbotron. Defaults to `None`.

## `well`

Creates a well container for inset content.

### Arguments

*   `content` (string): content of the well.

## `media_object`

Creates a media object with aligned content.

### Arguments

*   `img` (string): image source URL for the media object.
*   `content` (string): content to display next to the image.

## `list_group_item`

Creates a single item in a list group.

### Arguments

*   `content` (string): content of the list group item.
*   `active` (boolean): Whether the item is currently active. Defaults to `false`.
