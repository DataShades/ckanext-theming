# Element Components

Element components are basic UI building blocks like buttons, links, headings, and other fundamental interface elements. These components form the foundation of the user interface.

## Overview

Element components are the basic building blocks of the UI. They provide consistent styling and behavior for fundamental interface elements that are used throughout the application. These components ensure that basic UI elements maintain consistent appearance and behavior across different themes and contexts.

## Avatar Component

The `avatar` component displays user avatars and profile images, providing visual identification for users throughout the application. Avatars are essential for creating a sense of community and personalization, allowing users to quickly identify who created content, made changes, or is associated with specific actions.

Avatar components typically handle image sizing, circular cropping, and fallback representations when no image is available. They often include support for initials-based avatars when users don't have profile pictures, ensuring consistent visual representation regardless of whether a user has uploaded an image. The component ensures appropriate sizing and styling across different contexts where avatars might appear.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `src` | string | - | URL to the avatar image. If not provided, a default placeholder image is used. |
| `alt` | string | - | Alternative text for accessibility. If not provided, a default value is used. |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and customization:

- `size` (string): Size of the avatar (e.g., "sm", "md", "lg") - commonly used in Bootstrap themes
- `rounded` (bool): Whether to apply rounded corners - common in Bootstrap themes
- `variant` (string): Style variant (e.g., "circle", "square") - theme-dependent

/// details | Usage Example
    type: example

```jinja2
<!-- Avatar with user image -->
{{ ui.avatar(src="/path/to/user/image.jpg", alt="User Name") }}

<!-- Avatar with fallback -->
{{ ui.avatar(alt="Default User") }}
```
///


## Badge Component

The `badge` component displays status badges and indicators that provide quick visual information about states, counts, or categories. Badges are compact elements that draw attention to important information without requiring significant interface space. They're commonly used for showing notification counts, status indicators, or categorizing content.

Badge components typically come in different styles to indicate different types of information: success badges for positive states, warning badges for cautionary information, error badges for problems, and neutral badges for general information. The component handles consistent sizing, coloring, and positioning to ensure badges are visually distinct and appropriately styled based on their purpose.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | The text or number to display in the badge. |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and customization:

- `variant` (string): Style variant (e.g., "primary", "secondary", "success", "danger") - common in Bootstrap themes
- `pill` (bool): Whether to use pill-shaped styling - common in Bootstrap themes
- `size` (string): Size of the badge (e.g., "sm", "lg") - theme-dependent

/// details | Usage Example
    type: example

```jinja2
<!-- Simple badge -->
{{ ui.badge("New") }}

<!-- Count badge -->
{{ ui.badge("12") }}

<!-- Status badge -->
{{ ui.badge("Active") }}
```
///


## Breadcrumb Divider Component

The `breadcrumb_divider` component displays dividers between breadcrumb navigation items, creating visual separation and indicating the hierarchical relationship between navigation levels. These dividers are subtle but important elements that enhance the readability and understanding of breadcrumb trails.

Breadcrumb dividers typically use simple visual elements like chevrons, arrows, or simple separators to indicate the progression from one level to another in the navigation hierarchy. The component works in conjunction with `breadcrumb` and `breadcrumb_wrapper` components to create cohesive navigation experiences that help users understand their current location within the site structure.

/// details | Usage Example
    type: example

```jinja2
<!-- Default divider -->
{{ ui.breadcrumb_divider() }}

<!-- Custom divider -->
{{ ui.breadcrumb_divider(content=">") }}
```
///

/// admonition | Relationship
    type: info

The `breadcrumb_divider` component works with `breadcrumb` and `breadcrumb_wrapper` components to create complete breadcrumb navigation experiences. While breadcrumbs provide the navigation structure, dividers provide the visual separation between levels.
///


## Button Component

The `button` component creates interactive buttons that allow users to perform actions, submit forms, or navigate within the application. Buttons are fundamental interactive elements that require consistent styling and behavior to ensure users can easily identify actionable elements throughout the interface.

Button components typically support different styles for different purposes: primary buttons for main actions, secondary buttons for alternative actions, and various other styles for different contexts. The component handles proper accessibility attributes, hover states, focus indicators, and consistent sizing to ensure buttons are both visually appealing and functionally accessible.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | The text to display on the button. |
| `href` | string | - | If provided, the button will be rendered as an anchor tag instead of a button element. |
| `type` | string | "button" | The type attribute for button elements (e.g., "button", "submit", "reset"). |
| `style` | string | "primary" | The visual style of the button (e.g., "primary", "secondary", "danger"). |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and behavior:

- `size` (string): Size of the button (e.g., "sm", "lg") - common in Bootstrap themes
- `outline` (bool): Whether to use outline style - common in Bootstrap themes
- `block` (bool): Whether to make the button full-width - common in Bootstrap themes
- `disabled` (bool): Whether the button is disabled
- `variant` (string): Additional style variant (e.g., "outline-primary", "link") - theme-dependent

/// details | Usage Example
    type: example

```jinja2
<!-- Primary button -->
{{ ui.button("Submit Form", style="primary") }}

<!-- Secondary button -->
{{ ui.button("Cancel", style="secondary") }}

<!-- Link styled as button -->
{{ ui.button("View Details", href="/details") }}

<!-- Button with attributes -->
{{ ui.button("Delete", type="submit", style="danger", attrs={"onclick": "return confirm('Are you sure?')"}) }}
```
///


## Datetime Component

The `datetime` component displays date and time information in a consistent, localized format. This component is crucial for showing when content was created, updated, or when events occurred, providing temporal context that helps users understand the relevance and freshness of information.

Datetime components handle various formatting options and localization requirements, ensuring that dates and times are displayed in formats appropriate for the user's locale and preferences. The component can display relative times (like "2 hours ago") or absolute times, and handles time zone considerations to ensure accurate representation of temporal information.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `dt` | datetime | - | The datetime object or string to format and display. |
| `date_format` | string | - | The format string to use for displaying the date/time (e.g., "%Y-%m-%d %H:%M"). |
| `with_hours` | bool | - | Whether to include hours in the display. |
| `empty` | string | "" | Text to display if the datetime is empty or invalid. |

#### Theme-Specific Parameters

Different themes may support additional parameters for formatting and display:

- `relative` (bool): Whether to display relative time (e.g., "2 hours ago") - theme-dependent
- `timezone` (string): Timezone to use for display - theme-dependent
- `locale` (string): Locale for formatting - theme-dependent
- `format_short` (string): Short format string for compact display - theme-dependent

/// details | Usage Example
    type: example

```jinja2
<!-- Display datetime with default format -->
{{ ui.datetime(dt="2023-01-01T12:00:00Z") }}

<!-- Display with custom format -->
{{ ui.datetime(dt="2023-01-01T12:00:00Z", date_format="%Y-%m-%d %H:%M") }}

<!-- Display with hours -->
{{ ui.datetime(dt="2023-01-01T12:00:00Z", with_hours=True) }}
```
///


## Divider Component

The `divider` component creates visual dividers between content sections, providing clear separation without adding significant visual weight. Dividers are important for organizing content and creating visual hierarchy, helping users distinguish between different sections or groups of related information.

Divider components can be simple horizontal lines or more complex elements that include text or other content. They provide subtle but effective visual separation that helps organize content without adding clutter or competing with primary content for attention.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | Text or content to display in the middle of the divider. If not provided, a simple horizontal line is displayed. |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling:

- `orientation` (string): Orientation of the divider (e.g., "horizontal", "vertical") - theme-dependent
- `variant` (string): Style variant (e.g., "solid", "dashed", "dotted") - theme-dependent
- `inset` (bool): Whether to add margin/padding - theme-dependent
- `textAlign` (string): Text alignment when content is present (e.g., "center", "left", "right") - theme-dependent

/// details | Usage Example
    type: example

```jinja2
<!-- Simple divider -->
{{ ui.divider() }}

<!-- Divider with content -->
{{ ui.divider(content="Section Break") }}
```
///


## Heading Component

The `heading` component creates page and section headings that establish document structure and visual hierarchy. Headings are fundamental for accessibility and SEO, providing semantic structure that helps both users and search engines understand the organization and importance of content.

Heading components support different levels (typically h1 through h6) to create proper document structure and visual hierarchy. The component ensures consistent styling and appropriate semantic markup while maintaining the flexibility to adapt to different content requirements and design contexts.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | The text to display in the heading. |
| `level` | int | 2 | The heading level (1-6) which determines the HTML tag (h1, h2, etc.). |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and behavior:

- `size` (string): Visual size override (e.g., "sm", "lg") - theme-dependent
- `weight` (string): Font weight (e.g., "normal", "bold") - theme-dependent
- `color` (string): Text color - theme-dependent
- `truncate` (bool): Whether to truncate long text - theme-dependent
- `underline` (bool): Whether to add underline decoration - theme-dependent

/// details | Usage Example
    type: example

```jinja2
<!-- Main page heading -->
{{ ui.heading("Dataset Overview", level=1) }}

<!-- Section heading -->
{{ ui.heading("Dataset Information", level=2) }}

<!-- Subsection heading -->
{{ ui.heading("Metadata", level=3) }}
```
///


## Icon Component

The `icon` component displays icon elements that provide visual cues, represent actions, or enhance content understanding. Icons are powerful visual elements that can communicate concepts quickly and efficiently, transcending language barriers and providing intuitive interface elements.

Icon components typically support various icon sets or libraries, allowing themes to implement their preferred icon system while maintaining consistent usage patterns. The component handles sizing, coloring, and accessibility attributes to ensure icons are both visually effective and properly accessible to users with different needs.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | string | - | The name of the icon to display (e.g., "home", "search", "user"). |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and behavior:

- `size` (string): Size of the icon (e.g., "sm", "lg", "2x", "3x") - common in Font Awesome themes
- `color` (string): Color of the icon - theme-dependent
- `flip` (string): Flip direction (e.g., "horizontal", "vertical") - theme-dependent
- `rotate` (int): Rotation angle (e.g., 90, 180, 270) - theme-dependent
- `spin` (bool): Whether to animate rotation - theme-dependent
- `fixed_width` (bool): Whether to use fixed width - common in Font Awesome themes

/// details | Usage Example
    type: example

```jinja2
<!-- Basic icon -->
{{ ui.icon("home") }}

<!-- Icon with attributes -->
{{ ui.icon("search", attrs={"aria-hidden": "true"}) }}
```
///


## Image Component

The `image` component displays images with appropriate handling for sizing, loading, and accessibility. Images are important for visual communication and content enhancement, but require careful handling to ensure they load efficiently and remain accessible to all users.

Image components handle various aspects of image display including responsive sizing, lazy loading for performance, alt text for accessibility, and fallback handling when images fail to load. The component ensures images contribute positively to the user experience without causing performance or accessibility issues.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `src` | string | - | The URL or path to the image file. |
| `alt` | string | - | Alternative text for accessibility. If not provided, the image will have a role="presentation" attribute. |
| `height` | int | - | The height of the image in pixels. |
| `width` | int | - | The width of the image in pixels. |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and optimization:

- `size` (string): Predefined size (e.g., "sm", "md", "lg") - theme-dependent
- `rounded` (bool): Whether to apply rounded corners - common in Bootstrap themes
- `thumbnail` (bool): Whether to apply thumbnail styling - common in Bootstrap themes
- `fluid` (bool): Whether to make the image responsive - common in Bootstrap themes
- `loading` (string): Loading behavior (e.g., "lazy", "eager") - HTML attribute
- `crossorigin` (string): Cross-origin policy for the image - HTML attribute

/// details | Usage Example
    type: example

```jinja2
<!-- Basic image -->
{{ ui.image(src="/path/to/image.jpg", alt="Descriptive text") }}

<!-- Image with dimensions -->
{{ ui.image(src="/path/to/image.jpg", alt="Descriptive text", width=300, height=200) }}

<!-- Image with attributes -->
{{ ui.image(src="/path/to/image.jpg", alt="Descriptive text", attrs={"loading": "lazy"}) }}
```
///


## Link Component

The `link` component creates hyperlinks that allow users to navigate between pages or to external resources. Links are fundamental navigation elements that require consistent styling and behavior to ensure users can easily identify and interact with them.

Link components handle various states including normal, hover, visited, and active states to provide clear visual feedback about link status and interactivity. The component ensures proper accessibility attributes and consistent styling that makes links easily identifiable while maintaining visual harmony with the overall design.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | The text to display in the link. |
| `href` | string | - | The URL or path that the link points to. |
| `blank` | bool | - | Whether to open the link in a new tab/window. |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and behavior:

- `variant` (string): Style variant (e.g., "primary", "secondary", "link") - theme-dependent
- `underline` (string): Underline behavior (e.g., "always", "hover", "never") - theme-dependent
- `disabled` (bool): Whether the link is disabled - theme-dependent
- `external` (bool): Whether to add external link indicators - theme-dependent
- `download` (bool): Whether the link is for downloading - HTML attribute

/// details | Usage Example
    type: example

```jinja2
<!-- Internal link -->
{{ ui.link("View Dataset", href="/dataset/my-dataset") }}

<!-- External link -->
{{ ui.link("Visit External Site", href="https://example.com", blank=True) }}

<!-- Link with attributes -->
{{ ui.link("Download", href="/download/file", attrs={"download": true}) }}

<!-- Link with custom styling -->
{{ ui.link("Learn More", href="/more-info", attrs={"class": "btn btn-primary"}) }}
```
///


## Tag Component

The `tag` component displays tag elements that categorize or label content, making it easier to organize and discover related items. Tags are important for content discovery and organization, allowing users to quickly identify content themes or categories.

Tag components typically provide consistent styling for tag elements while supporting various states such as active, inactive, or selected tags. The component ensures tags are visually distinct from other content while maintaining readability and appropriate spacing for tag collections.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | The text to display in the tag. |
| `href` | string | - | The URL that the tag links to. If not provided, the tag links to a search for the tag. |
| `id` | string | - | The ID of the tag, used for linking in search queries when href is not provided. |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and behavior:

- `variant` (string): Style variant (e.g., "primary", "secondary", "success") - theme-dependent
- `size` (string): Size of the tag (e.g., "sm", "lg") - theme-dependent
- `rounded` (bool): Whether to apply rounded corners - theme-dependent
- `outline` (bool): Whether to use outline style - theme-dependent
- `removable` (bool): Whether to include a remove button - theme-dependent

/// details | Usage Example
    type: example

```jinja2
<!-- Basic tag -->
{{ ui.tag("Data") }}

<!-- Tag with custom ID -->
{{ ui.tag("Open Data", id="open-data") }}

<!-- Tag with custom href -->
{{ ui.tag("Government", href="/search?tags=government") }}
```
///


## Text Component

The `text` component handles text content elements, providing consistent styling and formatting for various types of textual content. This component ensures that text elements maintain appropriate typography, spacing, and readability across different contexts and themes.

Text components can handle various text styles including paragraphs, emphasized text, code blocks, and other text formatting needs. The component ensures proper line heights, font sizes, and spacing to maintain readability while adapting to different content requirements and design contexts.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | The text content to display. |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and formatting:

- `variant` (string): Text style variant (e.g., "muted", "success", "danger") - theme-dependent
- `size` (string): Text size (e.g., "sm", "lg") - theme-dependent
- `weight` (string): Font weight (e.g., "light", "normal", "bold") - theme-dependent
- `align` (string): Text alignment (e.g., "left", "center", "right") - theme-dependent
- `transform` (string): Text transformation (e.g., "uppercase", "lowercase", "capitalize") - theme-dependent

/// details | Usage Example
    type: example

```jinja2
<!-- Basic text -->
{{ ui.text("This is a paragraph of text.") }}

<!-- Text with attributes -->
{{ ui.text("Styled text", attrs={"class": "highlight"}) }}
```
///


## Video Component

The `video` component displays video content with appropriate handling for different video formats, responsive sizing, and accessibility features. Video components are important for rich media content but require careful implementation to ensure they work well across different devices and user contexts.

Video components handle various aspects of video display including responsive sizing, playback controls, accessibility features, and fallback handling when video content cannot be displayed. The component ensures videos enhance the user experience without causing performance or accessibility issues.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `src` | string | - | The URL or path to the video file. |
| `controls` | bool | - | Whether to show video controls. |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and functionality:

- `autoplay` (bool): Whether to autoplay the video - HTML attribute
- `loop` (bool): Whether to loop the video - HTML attribute
- `muted` (bool): Whether to mute the video by default - HTML attribute
- `poster` (string): Poster image URL to show before video plays - HTML attribute
- `preload` (string): Preload behavior (e.g., "auto", "metadata", "none") - HTML attribute
- `responsive` (bool): Whether to make the video responsive - theme-dependent

/// details | Usage Example
    type: example

```jinja2
<!-- Basic video -->
{{ ui.video(src="/path/to/video.mp4") }}

<!-- Video with controls -->
{{ ui.video(src="/path/to/video.mp4", controls=True) }}
```
///
