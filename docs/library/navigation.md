# Navigation Components

Navigation components provide all the elements needed for site navigation, including menus, breadcrumbs, pagination, and other navigation aids.

## Overview

Navigation components help users move through the application and find content. They provide consistent navigation patterns and help maintain user orientation within the site. Many navigation components work in hierarchical relationships - for example, `nav_item` components work within navigation containers, and `breadcrumb` components work with `breadcrumb_wrapper` and `breadcrumb_divider` components.

## Breadcrumb Component

The `breadcrumb` component creates breadcrumb navigation trails that show users their current location within the site hierarchy. Breadcrumbs are essential for user orientation, helping users understand where they are in relation to the overall site structure and providing easy navigation back to parent sections.

Breadcrumb components typically display a series of linked navigation items that represent the path from the site root to the current page. They work with `breadcrumb_wrapper` and `breadcrumb_divider` components to create complete breadcrumb experiences with proper visual separation and structural organization. Breadcrumbs are particularly valuable for sites with deep hierarchical structures where users might navigate several levels deep.

/// admonition | Relationship
    type: info

The `breadcrumb` component works with `breadcrumb_wrapper` and `breadcrumb_divider` components to create complete breadcrumb navigation experiences. While breadcrumbs provide the navigation structure, the wrapper provides the container and dividers provide visual separation.
///

## Nav Item Component

The `nav_item` component creates navigation menu items that serve as individual elements within navigation structures. These components are the fundamental building blocks of navigation menus, providing the clickable elements that allow users to move between different sections of the site.

Nav item components handle proper styling, active state indication, and accessibility attributes to ensure navigation is both visually clear and functionally accessible. They can contain various types of content including text, icons, or other components, making them flexible for different navigation requirements. The component ensures consistent appearance and behavior across different navigation contexts.

## Main Nav Item Component

The `main_nav_item` component creates navigation items specifically for the main site navigation menu. These components represent the primary navigation options that users will encounter on most pages, typically linking to major sections of the site like datasets, organizations, groups, or user accounts.

Main nav items are designed to be prominent and easily identifiable, often featuring larger text, distinctive styling, or other visual elements that make them stand out as primary navigation options. The component ensures these important navigation elements are clearly visible and accessible while maintaining consistency with the overall navigation design.

## Account Nav Item Component

The `account_nav_item` component creates navigation items specifically for account-related navigation menus. These components provide links to account-specific sections such as profile management, dashboard, settings, or other user account functions.

Account nav items are typically displayed in account-related contexts or in persistent account menus that appear when users are logged in. The component ensures these navigation options are clearly associated with account functionality and maintain appropriate styling and positioning within account navigation contexts.

## Content Nav Item Component

The `content_nav_item` component creates navigation items for content-specific navigation menus. These components provide navigation options related to specific content items, such as tabs for different aspects of a dataset, organization, or other content entity.

Content nav items are context-sensitive and typically appear on content-specific pages where users need to navigate between different aspects or views of the same content. The component ensures these navigation options are clearly associated with the current content and maintain appropriate styling and positioning within content navigation contexts.

## Page Action Component

The `page_action` component creates page-specific action items that provide quick access to actions related to the current page or context. These components typically appear as buttons or links that allow users to perform actions like "Add Dataset", "Create Group", or other page-specific functions.

Page action components are context-sensitive and provide immediate access to the most relevant actions for the current page. They're typically positioned prominently to ensure users can easily find and access important actions without having to navigate to other sections of the site. The component ensures these actions are clearly visible and appropriately styled for their importance.

## Content Action Component

The `content_action` component creates content-specific action items that provide actions related to specific content items. These components typically appear near or within content displays and allow users to perform actions like editing, sharing, or managing specific content items.

Content action components are closely associated with specific content and provide immediate access to relevant actions for that content. They might include options like "Edit Dataset", "Delete Resource", or "Share Content" that are directly related to the content being displayed. The component ensures these actions are clearly associated with the relevant content and maintain appropriate styling and positioning.

## Tab Handle Component

The `tab_handle` component creates tab navigation handles that allow users to switch between different content sections within the same page. Tab handles are essential for organizing related content in a space-efficient manner while maintaining clear navigation between different sections.

Tab handle components handle active state indication, visual styling, and accessibility attributes to ensure tab navigation is both visually clear and functionally accessible. They work with tab content areas to create complete tabbed interface experiences, allowing users to switch between different views or aspects of related content without leaving the current page.

/// admonition | Relationship
    type: info

The `tab_handle` component works with tab content areas to create complete tabbed interface experiences. While tab handles provide the navigation mechanism, the content areas provide the display for different sections.
///

## Menu Item Component

The `menu_item` component creates menu items that serve as individual elements within various menu structures throughout the application. These components provide the clickable elements for dropdown menus, context menus, and other menu-based navigation systems.

Menu item components handle proper styling, active state indication, and accessibility attributes to ensure menus are both visually clear and functionally accessible. They can contain various types of content and often include sub-menus or other complex navigation structures. The component ensures consistent appearance and behavior across different menu contexts.

## Pagination Component

The `pagination` component creates pagination controls that allow users to navigate through multiple pages of content. Pagination is essential for content-heavy sections where displaying all items on a single page would be impractical or overwhelming.

Pagination components handle complex navigation patterns including page numbers, next/previous controls, and page size selection. They provide clear indication of current page position and total content extent, helping users understand their position within larger content collections. The component ensures pagination controls are clearly visible and easily accessible while maintaining appropriate styling and positioning.

## Dropdown Item Component

The `dropdown_item` component creates individual items within dropdown menus, providing the clickable elements that appear when dropdown menus are activated. These components are the fundamental building blocks of dropdown navigation systems.

Dropdown item components handle proper styling, active state indication, and accessibility attributes to ensure dropdown menus are both visually clear and functionally accessible. They can contain various types of content and often include sub-menus or other complex navigation structures. The component ensures consistent appearance and behavior across different dropdown contexts.
