# Elements

Element macros provide the building blocks for creating basic UI components. These macros are theme-agnostic but can be customized with different CSS frameworks for styling.

## `avatar`

Displays a user avatar with fallback to a placeholder image. The macro ensures consistent sizing and styling of user profile pictures throughout the application.

**Use Cases:**
- User profile displays
- Comment sections
- Author information
- Team member listings

**Usage Context:**
Best used in areas where user identity needs to be visually represented, typically alongside user names or profile information.

**Example:**
```
{{ ui.avatar(src="/images/user.jpg", alt="User Name") }}
```

**Recommendations:**
- Include appropriate alt text for accessibility
- The macro will fallback to a placeholder if no source is provided
- Different themes may customize the default dimensions (e.g., Bootstrap may use 48x48, Tailwind might use w-10 h-10)

## `badge`

Displays a badge element typically used for highlighting status, categories, or small amounts of metadata. Badges are compact and visually distinct from surrounding content.

**Use Cases:**
- Status indicators (e.g., "New", "Hot", "Verified")
- Category labels
- Count indicators
- Small metadata tags

**Usage Context:**
Ideal for inline supplementary information that needs visual emphasis without taking much space.

**Example:**
```
<div>
  Feature Name
  {{ ui.badge("New") }}
</div>
```

**Recommendations:**
- Keep content concise (1-2 words)
- Different themes may apply different styling (Bootstrap uses .badge, Bulma uses .tag)
- Consider color coding for different meanings

## `button`

Renders a button element with customizable styling and behavior. Buttons are interactive elements that trigger actions when clicked.

**Use Cases:**
- Form submissions
- Action triggers
- Navigation buttons
- Modal triggers

**Usage Context:**
Use for any interactive element that performs an action when clicked, as opposed to links which navigate to new content.

**Example:**
```
{{ ui.button("Submit Form", type="primary") }}
{{ ui.button("Cancel", type="secondary") }}
```

**Recommendations:**
- Use appropriate button types for visual consistency
- Different themes provide various styling options (Bootstrap: btn-primary, btn-secondary; Tailwind: bg-blue-600, bg-gray-600; Bulma: is-primary, is-link)

## `divider`

Creates a horizontal divider to separate content sections visually. Provides a clear visual break between content blocks without adding excessive spacing.

**Use Cases:**
- Separating content sections
- Visual breaks in forms
- Delineating content areas

**Usage Context:**
Use when you need to separate different sections of content within a single container or when content needs visual separation.

**Example:**
```
Content above
{{ ui.divider() }}
Content below
```

**Recommendations:**
- Use sparingly to maintain visual hierarchy
- Different themes may implement different styles (Bootstrap: <hr>, Tailwind: border-t, Bulma: <hr>)

## `heading`

Generates a heading element (h1-h6) with appropriate semantic HTML and theme-appropriate styling. Provides consistent heading hierarchy throughout the application.

**Use Cases:**
- Section headings
- Content titles
- Hierarchy establishment
- SEO-friendly structure

**Usage Context:**
Use to establish document structure and create a visual hierarchy, following proper heading levels (h1 for main content, h2 for sections, etc.).

**Example:**
```
{{ ui.heading("Main Title", level=1) }}
{{ ui.heading("Section Title", level=2) }}
```

**Recommendations:**
- Maintain proper heading hierarchy for accessibility
- Different themes may apply different typography scales (Bootstrap: h1-h6 classes, Tailwind: text-4xl, text-3xl, etc., Bulma: title classes)

## `image`

Displays an image with optional alt text. Provides consistent image handling with proper accessibility attributes.

**Use Cases:**
- Content images
- Decorative images
- Icons
- User uploads

**Usage Context:**
Use for any image that's part of the content or user interface, ensuring proper alt text for accessibility.

**Example:**
```
{{ ui.image("/path/to/image.jpg", alt="Descriptive text") }}
```

**Recommendations:**
- Always include meaningful alt text
- Consider lazy loading for performance
- Different themes may apply default responsive classes (Bootstrap: img-fluid, Tailwind: object-cover)

## `link`

Creates a hyperlink element for navigation and resource linking. Provides consistent link styling across the theme.

**Use Cases:**
- Navigation links
- Content references
- External links
- Breadcrumb items

**Usage Context:**
Use for any navigation or resource linking, as opposed to buttons which perform actions.

**Example:**
```
{{ ui.link("Home Page", href="/") }}
{{ ui.link("Documentation", href="/docs") }}
```

**Recommendations:**
- Use meaningful link text instead of "click here"
- Different themes may apply different styling (Bootstrap: link classes, Tailwind: text-blue-600, Bulma: has-text-link)

## `tag`

Displays a tag element, typically used for categorization, filtering, or keyword identification. Tags are interactive elements that often link to filtered content.

**Use Cases:**
- Content categorization
- Filtering options
- Keyword tags
- Topic labels

**Usage Context:**
Use when you need to represent categories or keywords that link to filtered content.

**Example:**
```
{{ ui.tag("Technology", id="tech") }}
{{ ui.tag("Tutorial", href="/blog?tag=tutorial") }}
```

**Recommendations:**
- Keep tag text concise
- Different themes may customize appearance (Bootstrap: badge, Tailwind: badge classes, Bulma: tag)

## `text`

Renders plain text content with consistent styling. Provides a way to ensure text displays consistently across different themes.

**Use Cases:**
- Descriptive text
- Explanatory content
- Simple text blocks
- Content that doesn't require special formatting

**Usage Context:**
Use when you need to render simple text content that should follow theme typography settings.

**Example:**
```
{{ ui.text("This is a simple text block with theme-appropriate styling.") }}
```

**Recommendations:**
- Use for regular body text content
- Different themes may apply base text styles (Bootstrap: p, Tailwind: text-gray-700, Bulma: content)

## `video`

Embeds a video element with optional controls. Provides consistent video player integration with proper accessibility attributes.

**Use Cases:**
- Content videos
- Tutorials
- Product demonstrations
- Media content

**Usage Context:**
Use for embedding video content directly in pages, with controls or in a controlled playback scenario.

**Example:**
```
{{ ui.video("/path/to/video.mp4", controls=true) }}
```

**Recommendations:**
- Always include controls for user interaction
- Consider providing alternative content for accessibility
- Different themes may apply responsive video classes (Bootstrap: embed-responsive, Tailwind: w-full)

## `icon`

Displays an icon element.

### Arguments

*   `name` (string): The name of the icon.
*   `size` (string): The size of the icon. Defaults to "md".

## `label`

Displays a form label.

### Arguments

*   `text` (string): The label text.
*   `for_id` (string): The ID of the form element this label is for. Defaults to `None`.
