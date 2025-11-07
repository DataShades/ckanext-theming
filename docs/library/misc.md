# Miscellaneous

Miscellaneous macros provide utility functions and components that don't fit into the other categories but are commonly needed throughout the application. These components handle various utility needs like timestamps, spacing, content formatting, and other utility functions.

## `datetime`

Formats a datetime object for display with both human-readable and machine-readable representations. Provides consistent datetime formatting with proper machine-readable attributes for accessibility and semantic correctness.

**Use Cases:**
- Timestamp displays
- Date and time formatting
- Machine-readable datetime attributes
- Accessibility-friendly datetime display
- Consistent timestamp formatting
- ISO 8601 compliant values

**Usage Context:**
Use whenever you need to display a date or time value to users while maintaining proper machine-readable formats for accessibility and data processing.

**Example:**
```
{{ ui.datetime(datetime.now()) }}
<time datetime="2024-01-01T12:00:00Z">January 1, 2024, 12:00 PM</time>
```

**Recommendations:**
- Use for all datetime displays to maintain consistency
- Different themes will style the time element appropriately (Bootstrap: may use .text-muted, Tailwind: text-gray-500, Bulma: .has-text-grey)
- Includes data-datetime attribute for machine processing
- Follows internationalization best practices
- Provides accessible datetime information

## `spacer`

Creates a consistent amount of vertical or horizontal space between elements. Provides a standardized way to add whitespace without custom CSS, maintaining visual rhythm and spacing consistency.

**Use Cases:**
- Vertical spacing between sections
- Horizontal spacing between inline elements
- Consistent layout spacing
- Visual rhythm maintenance
- Responsive spacing adjustments
- Element separation

**Usage Context:**
Use to create consistent spacing between elements without custom CSS properties. Helps maintain visual consistency across different sections of the application.

**Example:**
```
Content above
{{ ui.spacer(size="md") }}
Content below
```

**Recommendations:**
- Use to maintain consistent spacing throughout the application
- Different themes provide various spacing scales (Bootstrap: my-* classes, Tailwind: space-y-4, Bulma: different height classes)
- Available sizes may vary by theme (xs, sm, md, lg, xl)
- Helps maintain visual hierarchy and readability

## `divider_with_text`

Creates a horizontal divider with centered text content, effectively separating content sections with descriptive labels. Provides a visually distinct way to separate related content groups.

**Use Cases:**
- Section separation with labels
- Content group boundaries
- Thematic breaks in forms
- Visual content organization
- Process step separators
- Category divisions

**Usage Context:**
Use when you need to clearly separate content sections with descriptive labels, such as in forms, articles, or content sections that need thematic separation.

**Example:**
```
Previous content section
{{ ui.divider_with_text("Or continue with") }}
Alternative content section
```

**Recommendations:**
- Use for clear content separation
- Different themes implement dividers differently (Bootstrap: hr with text, Tailwind: flex with hr elements, Bulma: field with addons)
- Keep text concise and descriptive
- Consider using for process steps or alternates

## `truncate`

Truncates content to a specified number of lines with an ellipsis, useful for content that may be too long to display fully in constrained spaces.

**Use Cases:**
- Long text in fixed-height containers
- Preview content truncation
- Headline and description limiting
- Card content management
- List item shortening
- Responsive content adjustment

**Usage Context:**
Use when displaying potentially long content in limited spaces where you want to show a preview with truncation rather than overflowing or wrapping.

**Example:**
```
{{ ui.truncate("This is a very long text that will be truncated to two lines maximum", max_lines=2) }}
```

**Recommendations:**
- Use in card components, lists, or any constrained space
- Different themes implement truncation differently (Bootstrap: CSS classes, Tailwind: line-clamp, Bulma: CSS properties)
- Consider providing a "Show More" option for full content
- Ensure accessibility with proper ARIA attributes if needed

## `badge_count`

Displays a numerical count in a visually distinct badge format, commonly used to show notifications, item counts, or status indicators.

**Use Cases:**
- Notification counters
- Item counts in lists
- Unread message indicators
- Cart item counts
- Status counts
- Filter result indicators

**Usage Context:**
Use to highlight numerical counts that require user attention or indicate the quantity of items in a particular category.

**Example:**
```
{{ ui.badge_count(12) }}
Notifications
```

**Recommendations:**
- Use for highlighting important counts
- Different themes provide various badge styles (Bootstrap: .badge, Tailwind: rounded-full, Bulma: .tag)
- Consider color coding for different meanings (new items, warnings, etc.)
- Should be visually prominent but not overwhelming

## `skeleton_loader`

Displays a loading placeholder with animated effects to indicate that content is being loaded. Provides a smooth user experience during content loading by showing where content will appear.

**Use Cases:**
- Content loading placeholders
- Image loading indicators
- List item placeholders
- Card loading states
- Page content loading
- Progressive content rendering

**Usage Context:**
Use when content is loading to provide visual feedback that improves perceived performance and user experience.

**Example:**
```
{{ ui.skeleton_loader(type="text") }}
```

**Recommendations:**
- Use during asynchronous content loading
- Different themes provide various skeleton implementations (Bootstrap: background animations, Tailwind: gradient animations, Bulma: animated backgrounds)
- Match the skeleton shape to the content it's replacing
- Enhances user experience during loading states
- Consider accessibility during loading states

## `notification`

Displays a notification message with optional title and content, providing a consistent way to show informative messages to users.

**Use Cases:**
- System notifications
- Informational messages
- Status updates
- Success confirmations
- Important announcements
- Content warnings

**Usage Context:**
Use for displaying messages that provide information to users without requiring immediate action, similar to alerts but for informational purposes.

**Example:**
```
{{ ui.notification(title="Information", content="Your profile has been updated successfully.", type="info") }}
```

**Recommendations:**
- Use for informative messages
- Different themes provide various notification styles (Bootstrap: alert variants, Tailwind: bg-* classes, Bulma: notification colors)
- Choose appropriate type (info, success, warning, etc.)
- Consider auto-dismissing for non-critical notifications
- Ensure accessibility with proper ARIA roles
## `spacer`

Creates a spacing element.

### Arguments

*   `size` (string): The size of the spacer. Defaults to "md".

## `divider_with_text`

Creates a horizontal divider with centered text.

### Arguments

*   `content` (string): text to display in the center of the divider.

## `truncate`

Creates a text truncation container.

### Arguments

*   `content` (string): content to potentially truncate.
*   `max_lines` (integer): maximum number of lines to display before truncating. Defaults to 1.

## `badge_count`

Displays a count badge.

### Arguments

*   `count` (integer): the count value to display in the badge.

## `skeleton_loader`

Displays a skeleton loader for content placeholders.

### Arguments

*   `type` (string): the type of skeleton loader. Defaults to "text".

## `notification`

Displays a notification message.

### Arguments

*   `title` (string): The title of the notification. Defaults to `None`.
*   `content` (string): The content of the notification.
*   `type` (string): The type of notification (e.g., "info", "success", "warning", "error"). Defaults to "info".
