# Navigation

Navigation components help users move through the application and find
content. They provide consistent navigation patterns and help maintain user
orientation within the site. Many navigation components work in hierarchical
relationships - for example, [`nav_item`][nav-item] components work within
navigation containers, and [`breadcrumb`][] components work with
[`breadcrumb_wrapper`][breadcrumb-wrapper] and
[`breadcrumb_divider`][breadcrumb-divider] components.

## Breadcrumb

The [`breadcrumb`][] component creates breadcrumb navigation trails that show users their current location within the site hierarchy. Breadcrumbs are essential for user orientation, helping users understand where they are in relation to the overall site structure and providing easy navigation back to parent sections.

Breadcrumb components typically display a series of linked navigation items that represent the path from the site root to the current page. They work with [`breadcrumb_wrapper`][breadcrumb-wrapper] and [`breadcrumb_divider`][breadcrumb-divider] components to create complete breadcrumb experiences with proper visual separation and structural organization. Breadcrumbs are particularly valuable for sites with deep hierarchical structures where users might navigate several levels deep.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic breadcrumb -->
{{ ui.breadcrumb(content="Home", href="/") }}
{{ ui.breadcrumb(content="Datasets", href="/datasets", is_first=False) }}
{{ ui.breadcrumb(content="Dataset Name", is_first=False) }}

<!-- Breadcrumb with dividers -->
{{ ui.breadcrumb(content="Home", href="/") }}
{{ ui.breadcrumb_divider() }}
{{ ui.breadcrumb(content="Section", href="/section", is_first=False) }}
```
///

/// admonition | Relationship
    type: info

The [`breadcrumb`][] component works with [`breadcrumb_wrapper`][breadcrumb-wrapper] and [`breadcrumb_divider`][breadcrumb-divider] components to create complete breadcrumb navigation experiences. While breadcrumbs provide the navigation structure, the wrapper provides the container and dividers provide visual separation.
///

## Nav Item

The [`nav_item`][nav-item] component creates navigation menu items that serve as individual elements within navigation structures. These components are the fundamental building blocks of navigation menus, providing the clickable elements that allow users to move between different sections of the site.

Nav item components handle proper styling, active state indication, and accessibility attributes to ensure navigation is both visually clear and functionally accessible. They can contain various types of content including text, icons, or other components, making them flexible for different navigation requirements. The component ensures consistent appearance and behavior across different navigation contexts.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic navigation item -->
{{ ui.nav_item(content="Home", href="/") }}

<!-- Active navigation item -->
{{ ui.nav_item(content="Datasets", href="/datasets", active=True) }}

<!-- Navigation item with icon -->
{{ ui.nav_item(content=(ui.icon("home") ~ " Home"), href="/") }}
```
///

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | The text or content to display in the navigation item. |
| `href` | string | - | The URL that the navigation item links to. |
| `active` | bool | - | Whether the navigation item is currently active/selected. |

/// details | Theme-Specific Parameters
    type: tip

- `disabled` (bool): Whether the navigation item is disabled
- `variant` (string): Style variant (e.g., "primary", "secondary")
- `dropdown` (bool): Whether the item has a dropdown menu
- `external` (bool): Whether it's an external link
///

## Main Nav Item

The [`main_nav_item`][main-nav-item] component creates navigation items specifically for the main site navigation menu. These components represent the primary navigation options that users will encounter on most pages, typically linking to major sections of the site like datasets, organizations, groups, or user accounts.

Main nav items are designed to be prominent and easily identifiable, often featuring larger text, distinctive styling, or other visual elements that make them stand out as primary navigation options. The component ensures these important navigation elements are clearly visible and accessible while maintaining consistency with the overall navigation design.

## Account Nav Item

The [`account_nav_item`][account-nav-item] component creates navigation items specifically for account-related navigation menus. These components provide links to account-specific sections such as profile management, dashboard, settings, or other user account functions.

Account nav items are typically displayed in account-related contexts or in persistent account menus that appear when users are logged in. The component ensures these navigation options are clearly associated with account functionality and maintain appropriate styling and positioning within account navigation contexts.

## Content Nav Item

The [`content_nav_item`][content-nav-item] component creates navigation items for content-specific navigation menus. These components provide navigation options related to specific content items, such as tabs for different aspects of a dataset, organization, or other content entity.

Content nav items are context-sensitive and typically appear on content-specific pages where users need to navigate between different aspects or views of the same content. The component ensures these navigation options are clearly associated with the current content and maintain appropriate styling and positioning within content navigation contexts.

## Page Action

The [`page_action`][page-action] component creates page-specific action items that provide quick access to actions related to the current page or context. These components typically appear as buttons or links that allow users to perform actions like "Add Dataset", "Create Group", or other page-specific functions.

Page action components are context-sensitive and provide immediate access to the most relevant actions for the current page. They're typically positioned prominently to ensure users can easily find and access important actions without having to navigate to other sections of the site. The component ensures these actions are clearly visible and appropriately styled for their importance.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Add dataset action -->
{{ ui.page_action(content="Add Dataset", href="/dataset/new") }}

<!-- Page action with attributes -->
{{ ui.page_action(content="Create Group", href="/group/new", attrs={"class": "btn btn-primary"}) }}

<!-- Conditional page action -->
{{ ui.page_action(content="Add Organization", href="/organization/new") if h.check_access('organization_create') }}
```
///


| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | The text to display in the page action. |
| `href` | string | - | The URL that the action links to. |

/// details | Theme-Specific Parameters
    type: tip

Different themes may support additional parameters for styling and behavior:

- `style` (string): Button style (e.g., "primary", "secondary", "danger") - theme-dependent
- `size` (string): Button size (e.g., "sm", "lg") - theme-dependent
- `variant` (string): Style variant (e.g., "outline", "link") - theme-dependent
- `disabled` (bool): Whether the action is disabled - theme-dependent
- `icon` (string): Icon to display with the action - theme-dependent
///

## Content Action

The [`content_action`][content-action] component creates content-specific action items that provide actions related to specific content items. These components typically appear near or within content displays and allow users to perform actions like editing, sharing, or managing specific content items.

Content action components are closely associated with specific content and provide immediate access to relevant actions for that content. They might include options like "Edit Dataset", "Delete Resource", or "Share Content" that are directly related to the content being displayed. The component ensures these actions are clearly associated with the relevant content and maintain appropriate styling and positioning.

## Tab Handle

The [`tab_handle`][tab-handle] component creates tab navigation handles that allow users to switch between different content sections within the same page. Tab handles are essential for organizing related content in a space-efficient manner while maintaining clear navigation between different sections.

Tab handle components handle active state indication, visual styling, and accessibility attributes to ensure tab navigation is both visually clear and functionally accessible. They work with tab content areas to create complete tabbed interface experiences, allowing users to switch between different views or aspects of related content without leaving the current page.

/// admonition | Relationship
    type: info

The [`tab_handle`][tab-handle] component works with tab content areas to create complete tabbed interface experiences. While tab handles provide the navigation mechanism, the content areas provide the display for different sections.

///

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic tab handle -->
{{ ui.tab_handle(content="Tab 1", href="/tab1") }}

<!-- Active tab handle -->
{{ ui.tab_handle(content="Tab 2", href="/tab2", active=True) }}

<!-- Tab handle with attributes -->
{{ ui.tab_handle(content="Settings", href="/settings", attrs={"class": "nav-link"}) }}
```
///


| Parameter | Type   | Default | Description                                   |
|-----------|--------|---------|-----------------------------------------------|
| `content` | string | -       | The text to display in the tab handle.        |
| `href`    | string | -       | The URL that the tab links to.                |
| `active`  | bool   | -       | Whether the tab is currently active/selected. |

/// details | Theme-Specific Parameters
    type: tip

Different themes may support additional parameters for styling and behavior:

- `disabled` (bool): Whether the tab is disabled - theme-dependent
- `variant` (string): Style variant (e.g., "tabs", "pills") - theme-dependent
- `icon` (string): Icon to display with the tab - theme-dependent
- `count` (int): Count indicator to display on the tab - theme-dependent

///

## Menu Item

The [`menu_item`][menu-item] component creates menu items that serve as
individual elements within various menu structures throughout the
application. These components provide the clickable elements for dropdown
menus, context menus, and other menu-based navigation systems.

Menu item components handle proper styling, active state indication, and
accessibility attributes to ensure menus are both visually clear and
functionally accessible. They can contain various types of content and often
include sub-menus or other complex navigation structures. The component ensures
consistent appearance and behavior across different menu contexts.

## Pagination

The [`pagination`][] component creates pagination controls that allow users to
navigate through multiple pages of content. Pagination is essential for
content-heavy sections where displaying all items on a single page would be
impractical or overwhelming.

Pagination components handle complex navigation patterns including page
numbers, next/previous controls, and page size selection. They provide clear
indication of current page position and total content extent, helping users
understand their position within larger content collections. The component
ensures pagination controls are clearly visible and easily accessible while
maintaining appropriate styling and positioning.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic pagination -->
{{ ui.pagination(page=1, total=10, url_generator=h.pager_url) }}

<!-- Pagination with custom parameters -->
{{ ui.pagination(page=3, total=20, url_generator=h.pager_url, padding=3) }}

<!-- Pagination with attributes -->
{{ ui.pagination(page=2, total=15, url_generator=h.pager_url, attrs={"class": "custom-pagination"}) }}
```
///

## Dropdown Item

The [`dropdown_item`][dropdown-item] component creates individual items within
dropdown menus, providing the clickable elements that appear when dropdown
menus are activated. These components are the fundamental building blocks of
dropdown navigation systems.

Dropdown item components handle proper styling, active state indication, and
accessibility attributes to ensure dropdown menus are both visually clear and
functionally accessible. They can contain various types of content and often
include sub-menus or other complex navigation structures. The component ensures
consistent appearance and behavior across different dropdown contexts.
