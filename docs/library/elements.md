# Element Components

Element components are basic UI building blocks like buttons, links, headings, and other fundamental interface elements. These components form the foundation of the user interface.

## Overview

Element components are the basic building blocks of the UI. They provide consistent styling and behavior for fundamental interface elements that are used throughout the application. These components ensure that basic UI elements maintain consistent appearance and behavior across different themes and contexts.

## Avatar Component

The `avatar` component displays user avatars and profile images, providing visual identification for users throughout the application. Avatars are essential for creating a sense of community and personalization, allowing users to quickly identify who created content, made changes, or is associated with specific actions.

Avatar components typically handle image sizing, circular cropping, and fallback representations when no image is available. They often include support for initials-based avatars when users don't have profile pictures, ensuring consistent visual representation regardless of whether a user has uploaded an image. The component ensures appropriate sizing and styling across different contexts where avatars might appear.

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

/// details | Usage Example
    type: example

```jinja2
<!-- Basic video -->
{{ ui.video(src="/path/to/video.mp4") }}

<!-- Video with controls -->
{{ ui.video(src="/path/to/video.mp4", controls=True) }}
```
///
