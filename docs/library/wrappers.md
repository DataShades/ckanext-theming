# Wrapper Components

Wrapper components provide structural containers and layout elements that wrap other UI components. These components are essential for organizing content and creating consistent layouts across the application.

## Overview

Wrapper components are used to provide consistent structural patterns for different types of content and UI elements. They typically don't have visible output themselves but provide the structural foundation for other components. These components work in conjunction with their content counterparts - for example, `accordion_wrapper` works with `accordion` components, and `panel_wrapper` works with `panel` components.

## Accordion Wrapper

The `accordion_wrapper` component provides the structural container for accordion elements. It establishes the base styling and behavior for accordion groups, ensuring consistent appearance and interaction patterns across different themes. This wrapper works in conjunction with the `accordion` component to create collapsible content sections.

/// admonition | Relationship
    type: info

The `accordion_wrapper` component is designed to work with `accordion` components. While the accordion component defines the individual collapsible sections, the wrapper provides the container that holds multiple accordions together.
///

## Account Navigation Wrapper

The `account_nav_wrapper` component creates a consistent container for account-related navigation elements. It ensures that user account navigation maintains a uniform appearance and structure across different themes and pages. This component typically wraps `account_nav_item` elements to provide proper spacing and styling.

## Activity Wrapper

The `activity_wrapper` component provides a structural container for activity stream content. It ensures that activity entries are properly formatted and styled consistently. This wrapper works with the `activity` component to display user actions and system events in a structured format.

## Breadcrumb Wrapper

The `breadcrumb_wrapper` component creates a container for breadcrumb navigation elements. It ensures proper spacing and styling for breadcrumb trails, working in conjunction with `breadcrumb` and `breadcrumb_divider` components to create a cohesive navigation experience.

## Content Action Wrapper

The `content_action_wrapper` component provides a container for content-specific action buttons and links. It ensures that actions related to specific content items (like edit, delete, or share buttons) are consistently positioned and styled. This component typically wraps `content_action` elements.

## Content Navigation Wrapper

The `content_nav_wrapper` component creates a container for navigation elements related to specific content. It provides consistent styling and positioning for content navigation, typically wrapping `content_nav_item` components to maintain a uniform appearance.

## Dropdown Wrapper

The `dropdown_wrapper` component provides the structural foundation for dropdown menus. It ensures proper positioning, styling, and behavior for dropdown components. This wrapper works with dropdown-related components to create consistent menu experiences across different themes.

## Facet Wrapper

The `facet_wrapper` component creates a container for facet filter elements, which are crucial for search and filtering functionality in CKAN. It works with `facet` and `facet_section` components to provide a consistent interface for filtering datasets and other content.

/// admonition | Relationship
    type: info

The `facet_wrapper` component is closely related to `facet` and `facet_section` components. While the wrapper provides the container structure, the facet components provide the actual filter controls and display elements.
///

## Group Wrapper

The `group_wrapper` component provides a structural container for group-related content. It ensures that group information, listings, and related elements maintain consistent styling and layout. This wrapper works with `group` components to display organizational structures within CKAN.

## Main Navigation Wrapper

The `main_nav_wrapper` component creates a container for the primary site navigation. It ensures that the main navigation maintains consistent styling and behavior across different pages and themes. This component typically wraps `main_nav_item` elements.

## Menu Wrapper

The `menu_wrapper` component provides a general container for menu structures throughout the application. It works with `menu_item` components to create consistent menu experiences, whether for dropdowns, navigation, or other menu-based interfaces.

## Navigation Wrapper

The `nav_wrapper` component serves as a general container for navigation elements. It provides the structural foundation for various navigation patterns and works with different navigation item components to ensure consistency.

## Organization Wrapper

The `organization_wrapper` component creates a container for organization-related content. It works with `organization` components to provide consistent display of organizational information, members, and related content within CKAN.

## Package Wrapper

The `package_wrapper` component provides a structural container for package (dataset) related content. It ensures that dataset information, resources, and related elements maintain consistent styling and layout. This wrapper works with `package` components to display dataset information effectively.

## Page Action Wrapper

The `page_action_wrapper` component creates a container for page-specific action elements. It ensures that actions like "Add Dataset" or "Create Group" are consistently positioned and styled across different pages. This component typically wraps `page_action` elements.

## Panel Wrapper

The `panel_wrapper` component provides the structural container for panel components. It establishes the base styling and behavior for panels, working in conjunction with `panel` and `panel_handle` components to create expandable content sections.

/// admonition | Relationship
    type: info

The `panel_wrapper` component works closely with `panel` and `panel_handle` components. The wrapper provides the container, the panel contains the content, and the handle provides the interactive element for controlling the panel.
///

## Resource Wrapper

The `resource_wrapper` component creates a container for resource-related content. It ensures that resource information, download links, and related elements maintain consistent styling and layout. This wrapper works with `resource` components to display resource information effectively.

## Tab Wrapper

The `tab_wrapper` component provides the structural container for tab-based interfaces. It works with `tab_handle` components to create consistent tab navigation and content switching experiences across different themes.

/// admonition | Relationship
    type: info

The `tab_wrapper` component is designed to work with `tab_handle` components. The wrapper provides the container structure, while the handles provide the interactive elements for switching between tab content.
///

## User Wrapper

The `user_wrapper` component creates a container for user-related content. It ensures that user profiles, activity, and related information maintain consistent styling and layout. This wrapper works with `user` components to display user information effectively.
