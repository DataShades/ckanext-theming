# Navigation

Navigation macros provide structured ways to implement various navigation patterns throughout the application. These components help users understand their location within the site and navigate between different sections effectively.

## `breadcrumb_wrapper`

Wraps the breadcrumb trail to provide proper container structure and styling for hierarchical navigation paths. Breadcrumbs show the user's current location within the site hierarchy and provide an easy way to navigate back to parent sections.

**Use Cases:**

- E-commerce category hierarchies
- Document navigation
- Site structure visualization
- User location tracking
- Hierarchical content organization

**Usage Context:**

Use on pages where users need to understand their location within a hierarchy and potentially navigate to parent sections. Commonly appears near the top of content pages.

**Example:**

```
{{ ui.breadcrumb_wrapper(
  ui.breadcrumb_item("Home", href="/") +
  ui.breadcrumb_item("Categories", href="/categories") +
  ui.breadcrumb_item("Technology", href="/categories/tech") +
  ui.breadcrumb_item("Laptops", href="/categories/tech/laptops")
) }}
```

**Recommendations:**

- Limit to 3-5 levels to avoid clutter
- Different themes implement breadcrumbs differently (Bootstrap: .breadcrumb, Tailwind: flex with separators, Bulma: .breadcrumb)
- Don't include the current page in the breadcrumb trail

## `breadcrumb_item`

Creates a single item in a breadcrumb trail that represents a step in the navigation hierarchy. Each item provides a clickable link to a previous level in the site structure.

**Use Cases:**

- Linking to parent categories
- Document hierarchy navigation
- Site location indicators
- Navigation history

**Usage Context:**

Use within a `breadcrumb_wrapper` to create individual steps in the navigation path. Each item should represent a meaningful section of the site hierarchy.

**Example:**

```
{{ ui.breadcrumb_item("Products", href="/products") }}
```

**Recommendations:**

- Use clear, descriptive text
- Don't apply to the current page item
- Different themes may customize separators (Bootstrap: CSS arrows, Tailwind: SVG arrows, Bulma: / character)
- Ensure the last item in the trail represents the current page without a link

## `nav_wrapper`

Wraps a navigation element to provide proper container structure and styling for primary navigation areas. Serves as the main container for navigation items, ensuring consistent styling and behavior.

**Use Cases:**

- Main site navigation
- Secondary navigation menus
- Top navigation bars
- Sidebar navigation
- Footer navigation

**Usage Context:**

Use as the container for navigation items to create a structured navigation area with consistent styling.

**Example:**

```
{{ ui.nav_wrapper(
  ui.nav_item("Home", href="/") +
  ui.nav_item("Products", href="/products") +
  ui.nav_item("About", href="/about", active=true)
) }}
```

**Recommendations:**

- Use for primary navigation areas
- Different themes provide various navigation containers (Bootstrap: .navbar, Tailwind: flex container, Bulma: .nav)
- Consider responsive behavior for mobile devices

## `nav_item`

Creates a single item in a navigation list with active state indication. Navigation items are the fundamental building blocks of site navigation, providing links to different sections of the site.

**Use Cases:**

- Main menu links
- Secondary navigation
- Sidebar items
- Top navigation links
- Tab navigation items

**Usage Context:**

Use within a `nav_wrapper` to create actionable navigation items. The `active` parameter highlights the current page or section.

**Example:**

```
{{ ui.nav_item("Dashboard", href="/dashboard", active=true) }}
```

**Recommendations:**

- Use meaningful text that describes the target content
- Set `active=true` for the current page or section
- Different themes may apply different active styling (Bootstrap: .active, Tailwind: bg-blue-100, Bulma: .is-active)
- Consider accessibility when implementing active states

## `tab_wrapper`

Wraps a tabbed interface to provide proper container structure and styling for tab-based navigation. Tabs organize content into separate sections that can be accessed via clickable headers.

**Use Cases:**

- Content organization
- Settings panels
- Profile sections
- Dashboard views
- Category navigation

**Usage Context:**

Use when you need to organize content into multiple sections that can be accessed without leaving the current page. Commonly used in settings or profile pages.

**Example:**

```
{{ ui.tab_wrapper(
  ui.tab_item("Profile", href="#profile", active=true) +
  ui.tab_item("Settings", href="#settings") +
  ui.tab_item("Activity", href="#activity")
) }}
```

**Recommendations:**

- Use for organizing related content sections
- Different themes implement tabs differently (Bootstrap: .nav-tabs, Tailwind: border-b with underline, Bulma: .tabs)
- Ensure proper ARIA attributes for accessibility

## `tab_item`

Creates a single tab in a tabbed interface with active state indication. Each tab serves as a clickable header that reveals associated content.

**Use Cases:**

- Profile sections
- Settings categories
- Content filtering
- Dashboard sections
- Information organization

**Usage Context:**

Use within a `tab_wrapper` to create individual tab elements that control content visibility. The `active` parameter indicates the currently selected tab.

**Example:**

```
{{ ui.tab_item("Account", href="#account", active=true) }}
```

**Recommendations:**

- Keep tab titles concise
- Set `active=true` for the currently selected tab
- Different themes may customize appearance (Bootstrap: .nav-link, Tailwind: border-b-2, Bulma: .is-active)
- Ensure tab content is properly associated with tab items

## `menu_wrapper`

Wraps a menu to provide proper container structure and styling for menu systems. Menus organize related links or actions in a structured format.

**Use Cases:**

- Dropdown menus
- Sidebar menus
- Context menus
- Administrative menus
- Navigation menus

**Usage Context:**

Use as the container for menu items to create organized lists of related functionality or content links.

**Example:**

```
{{ ui.menu_wrapper(
  ui.menu_item("Edit", href="/edit") +
  ui.menu_item("Delete", href="/delete") +
  ui.menu_item("Share", href="/share")
) }}
```

**Recommendations:**

- Use for related actions or links
- Different themes implement menus differently (Bootstrap: .dropdown-menu, Tailwind: space-y-1, Bulma: .menu-list)
- Consider vertical vs. horizontal menu layouts

## `menu_item`

Creates a single item in a menu system with active state indication. Menu items are clickable elements that perform actions or navigate to different content areas.

**Use Cases:**

- Dropdown menu options
- Sidebar navigation items
- Context menu actions
- Administrative links
- Navigation links

**Usage Context:**

Use within a `menu_wrapper` to create individual menu options. The `active` parameter highlights the current selection.

**Example:**

```
{{ ui.menu_item("Account Settings", href="/account/settings", active=true) }}
```

**Recommendations:**

- Use clear, action-oriented text
- Set `active=true` for the current selection
- Different themes may customize appearance (Bootstrap: .dropdown-item, Tailwind: px-4 py-2, Bulma: .panel-block)
- Consider icon integration for visual recognition

## `pagination`

Renders pagination controls for navigating through multiple pages of content. Pagination controls help users navigate through large sets of content distributed across multiple pages.

**Use Cases:**

- Search results
- Product listings
- User lists
- Content archives
- Data tables

**Usage Context:**

Use when content is divided across multiple pages to help users navigate between different sections of the dataset.

**Example:**

```
{{ ui.pagination(page=currentPage, total_pages=totalPages, url_generator=h.pager_url, padding=2) }}
```

**Recommendations:**

- Use consistent URL patterns for page navigation
- Different themes style pagination differently (Bootstrap: .pagination, Tailwind: flex with buttons, Bulma: .pagination)
- Show current page clearly and provide first/last page navigation
- Consider the number of page links to show with the `padding` parameter
- Implement proper ARIA labels for accessibility (current page, page N of M)

## `dropdown_wrapper`

Wraps a dropdown menu.

### Arguments

*   `content` (string): dropdown menu items.
*   `title` (string): The title for the dropdown button. Defaults to `None`.

## `dropdown_item`

Creates a single item in a dropdown menu.

### Arguments

*   `content` (string): The text to display for the dropdown item.
*   `href` (string): The URL for the dropdown item. Defaults to "#".

## `sidebar`

Creates a sidebar navigation container.

### Arguments

*   `content` (string): content to display in the sidebar.

## `navbar`

Creates a navigation bar.

### Arguments

*   `brand` (string): The brand/branding content for the navbar.
*   `items` (string): navigation items to display in the navbar.

## `breadcrumb_divider`

Creates a breadcrumb divider element.

### Arguments

None
