# Wrapper Components

Wrapper components are used to provide consistent structural patterns for
different types of content and UI elements. They typically don't have visible
output themselves but provide the structural foundation for other
components. These components work in conjunction with their content
counterparts - for example, `accordion_wrapper` works with `accordion`
components, and `panel_wrapper` works with `panel` components.

## Accordion Wrapper

The `accordion_wrapper` component provides the structural container for accordion elements. It establishes the base styling and behavior for accordion groups, ensuring consistent appearance and interaction patterns across different themes. This wrapper works in conjunction with the `accordion` component to create collapsible content sections.

/// admonition | Relationship
    type: info

The `accordion_wrapper` component is designed to work with `accordion` components. While the accordion component defines the individual collapsible sections, the wrapper provides the container that holds multiple accordions together.
///

/// details | Usage Example
    type: example

```jinja2
<!-- Basic accordion wrapper -->
{% call ui.util.call(ui.accordion_wrapper) %}
    {{ ui.accordion("First section content", title="First Section") }}
    {{ ui.accordion("Second section content", title="Second Section") }}
{% endcall %}

<!-- Accordion wrapper with attributes -->
{% call ui.util.call(ui.accordion_wrapper, attrs={"class": "faq-accordions"}) %}
    {{ ui.accordion("FAQ content", title="Frequently Asked Questions") }}
{% endcall %}
```
///

## Account Navigation Wrapper

The `account_nav_wrapper` component creates a consistent container for account-related navigation elements. It ensures that user account navigation maintains a uniform appearance and structure across different themes and pages. This component typically wraps `account_nav_item` elements to provide proper spacing and styling.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic account navigation wrapper -->
{% call ui.util.call(ui.account_nav_wrapper) %}
    {{ ui.account_nav_item("Profile", href="/profile") }}
    {{ ui.account_nav_item("Settings", href="/settings") }}
{% endcall %}

<!-- Account navigation wrapper with attributes -->
{% call ui.util.call(ui.account_nav_wrapper, attrs={"class": "account-menu"}) %}
    {{ ui.account_nav_item("Dashboard", href="/dashboard") }}
{% endcall %}
```
///

## Activity Wrapper

The `activity_wrapper` component provides a structural container for activity stream content. It ensures that activity entries are properly formatted and styled consistently. This wrapper works with the `activity` component to display user actions and system events in a structured format.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic activity wrapper -->
{% call ui.util.call(ui.activity_wrapper) %}
    {{ ui.activity("User created a dataset", activity=activity_data) }}
    {{ ui.activity("User updated profile", activity=activity_data2) }}
{% endcall %}

<!-- Activity wrapper with attributes -->
{% call ui.util.call(ui.activity_wrapper, attrs={"class": "activity-stream"}) %}
    {{ ui.activity("Recent activity", activity=recent_activity) }}
{% endcall %}
```
///

## Breadcrumb Wrapper

The `breadcrumb_wrapper` component creates a container for breadcrumb navigation elements. It ensures proper spacing and styling for breadcrumb trails, working in conjunction with `breadcrumb` and `breadcrumb_divider` components to create a cohesive navigation experience.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic breadcrumb wrapper -->
{% call ui.util.call(ui.breadcrumb_wrapper) %}
    {{ ui.breadcrumb("Home", href="/", is_first=True) }}
    {{ ui.breadcrumb("Datasets", href="/datasets", is_first=False) }}
    {{ ui.breadcrumb("Dataset", href="/dataset", is_first=False) }}
{% endcall %}

<!-- Breadcrumb wrapper with attributes -->
{% call ui.util.call(ui.breadcrumb_wrapper, attrs={"class": "custom-breadcrumbs"}) %}
    {{ ui.breadcrumb("Home", href="/", is_first=True) }}
    {{ ui.breadcrumb("Section", href="/section", is_first=False) }}
{% endcall %}
```
///

## Content Action Wrapper

The `content_action_wrapper` component provides a container for content-specific action buttons and links. It ensures that actions related to specific content items (like edit, delete, or share buttons) are consistently positioned and styled. This component typically wraps `content_action` elements.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic content action wrapper -->
{% call ui.util.call(ui.content_action_wrapper) %}
    {{ ui.content_action("Edit", href="/edit") }}
    {{ ui.content_action("Delete", href="/delete") }}
{% endcall %}

<!-- Content action wrapper with attributes -->
{% call ui.util.call(ui.content_action_wrapper, attrs={"class": "content-actions"}) %}
    {{ ui.content_action("Share", href="/share") }}
{% endcall %}
```
///

## Content Navigation Wrapper

The `content_nav_wrapper` component creates a container for navigation elements related to specific content. It provides consistent styling and positioning for content navigation, typically wrapping `content_nav_item` components to maintain a uniform appearance.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic content navigation wrapper -->
{% call ui.util.call(ui.content_nav_wrapper) %}
    {{ ui.content_nav_item("Info", href="/info") }}
    {{ ui.content_nav_item("Resources", href="/resources") }}
{% endcall %}

<!-- Content navigation wrapper with attributes -->
{% call ui.util.call(ui.content_nav_wrapper, attrs={"class": "content-nav"}) %}
    {{ ui.content_nav_item("Settings", href="/settings") }}
{% endcall %}
```
///

## Dropdown Wrapper

The `dropdown_wrapper` component provides the structural foundation for dropdown menus. It ensures proper positioning, styling, and behavior for dropdown components. This wrapper works with dropdown-related components to create consistent menu experiences across different themes.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic dropdown wrapper -->
{% call ui.util.call(ui.dropdown_wrapper) %}
    {{ ui.dropdown_item("Option 1", href="/option1") }}
    {{ ui.dropdown_item("Option 2", href="/option2") }}
{% endcall %}

<!-- Dropdown wrapper with attributes -->
{% call ui.util.call(ui.dropdown_wrapper, attrs={"class": "dropdown-menu"}) %}
    {{ ui.dropdown_item("Settings", href="/settings") }}
{% endcall %}
```
///

## Facet Wrapper

The `facet_wrapper` component creates a container for facet filter elements, which are crucial for search and filtering functionality in CKAN. It works with `facet` and `facet_section` components to provide a consistent interface for filtering datasets and other content.

/// admonition | Relationship
    type: info

The `facet_wrapper` component is closely related to `facet` and `facet_section` components. While the wrapper provides the container structure, the facet components provide the actual filter controls and display elements.
///

/// details | Usage Example
    type: example

```jinja2
<!-- Basic facet wrapper -->
{% call ui.util.call(ui.facet_wrapper) %}
    {{ ui.facet("Organization", key="org", value="Government", count=15, active=False) }}
    {{ ui.facet("Format", key="format", value="CSV", count=8, active=False) }}
{% endcall %}

<!-- Facet wrapper with attributes -->
{% call ui.util.call(ui.facet_wrapper, attrs={"class": "facet-container"}) %}
    {{ ui.facet("License", key="license", value="Open", count=12, active=False) }}
{% endcall %}
```
///
///

## Group Wrapper

The `group_wrapper` component provides a structural container for group-related content. It ensures that group information, listings, and related elements maintain consistent styling and layout. This wrapper works with `group` components to display organizational structures within CKAN.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic group wrapper -->
{% call ui.util.call(ui.group_wrapper) %}
    {{ ui.group(group_data) }}
{% endcall %}

<!-- Group wrapper with attributes -->
{% call ui.util.call(ui.group_wrapper, attrs={"class": "group-listing"}) %}
    {{ ui.group(another_group) }}
{% endcall %}
```
///

## Main Navigation Wrapper

The `main_nav_wrapper` component creates a container for the primary site navigation. It ensures that the main navigation maintains consistent styling and behavior across different pages and themes. This component typically wraps `main_nav_item` elements.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic main navigation wrapper -->
{% call ui.util.call(ui.main_nav_wrapper) %}
    {{ ui.main_nav_item("Datasets", href="/datasets") }}
    {{ ui.main_nav_item("Organizations", href="/organizations") }}
{% endcall %}

<!-- Main navigation wrapper with attributes -->
{% call ui.util.call(ui.main_nav_wrapper, attrs={"class": "main-navigation"}) %}
    {{ ui.main_nav_item("Groups", href="/groups") }}
{% endcall %}
```
///

## Menu Wrapper

The `menu_wrapper` component provides a general container for menu structures throughout the application. It works with `menu_item` components to create consistent menu experiences, whether for dropdowns, navigation, or other menu-based interfaces.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic menu wrapper -->
{% call ui.util.call(ui.menu_wrapper) %}
    {{ ui.menu_item("Option 1", href="/option1") }}
    {{ ui.menu_item("Option 2", href="/option2") }}
{% endcall %}

<!-- Menu wrapper with attributes -->
{% call ui.util.call(ui.menu_wrapper, attrs={"class": "custom-menu"}) %}
    {{ ui.menu_item("Settings", href="/settings") }}
{% endcall %}
```
///

## Navigation Wrapper

The `nav_wrapper` component serves as a general container for navigation elements. It provides the structural foundation for various navigation patterns and works with different navigation item components to ensure consistency.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic navigation wrapper -->
{% call ui.util.call(ui.nav_wrapper) %}
    {{ ui.nav_item("Home", href="/") }}
    {{ ui.nav_item("About", href="/about") }}
{% endcall %}

<!-- Navigation wrapper with attributes -->
{% call ui.util.call(ui.nav_wrapper, attrs={"class": "nav-container"}) %}
    {{ ui.nav_item("Contact", href="/contact") }}
{% endcall %}
```
///

## Organization Wrapper

The `organization_wrapper` component creates a container for organization-related content. It works with `organization` components to provide consistent display of organizational information, members, and related content within CKAN.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic organization wrapper -->
{% call ui.util.call(ui.organization_wrapper) %}
    {{ ui.organization(org_data) }}
{% endcall %}

<!-- Organization wrapper with attributes -->
{% call ui.util.call(ui.organization_wrapper, attrs={"class": "org-listing"}) %}
    {{ ui.organization(another_org) }}
{% endcall %}
```
///

## Package Wrapper

The `package_wrapper` component provides a structural container for package (dataset) related content. It ensures that dataset information, resources, and related elements maintain consistent styling and layout. This wrapper works with `package` components to display dataset information effectively.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic package wrapper -->
{% call ui.util.call(ui.package_wrapper) %}
    {{ ui.package(dataset_data) }}
{% endcall %}

<!-- Package wrapper with attributes -->
{% call ui.util.call(ui.package_wrapper, attrs={"class": "dataset-listing"}) %}
    {{ ui.package(another_dataset) }}
{% endcall %}
```
///

## Page Action Wrapper

The `page_action_wrapper` component creates a container for page-specific action elements. It ensures that actions like "Add Dataset" or "Create Group" are consistently positioned and styled across different pages. This component typically wraps `page_action` elements.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic page action wrapper -->
{% call ui.util.call(ui.page_action_wrapper) %}
    {{ ui.page_action("Add Dataset", href="/dataset/new") }}
{% endcall %}

<!-- Page action wrapper with attributes -->
{% call ui.util.call(ui.page_action_wrapper, attrs={"class": "page-actions"}) %}
    {{ ui.page_action("Create Group", href="/group/new") }}
{% endcall %}
```
///

## Panel Wrapper

The `panel_wrapper` component provides the structural container for panel components. It establishes the base styling and behavior for panels, working in conjunction with `panel` and `panel_handle` components to create expandable content sections.

/// admonition | Relationship
    type: info

The `panel_wrapper` component works closely with `panel` and `panel_handle` components. The wrapper provides the container, the panel contains the content, and the handle provides the interactive element for controlling the panel.
///

/// details | Usage Example
    type: example

```jinja2
<!-- Basic panel wrapper -->
{% call ui.util.call(ui.panel_wrapper) %}
    {{ ui.panel("Panel content", title="Panel Title") }}
{% endcall %}

<!-- Panel wrapper with attributes -->
{% call ui.util.call(ui.panel_wrapper, attrs={"class": "panel-container"}) %}
    {{ ui.panel("Styled panel", active=True) }}
{% endcall %}
```
///
///

## Resource Wrapper

The `resource_wrapper` component creates a container for resource-related content. It ensures that resource information, download links, and related elements maintain consistent styling and layout. This wrapper works with `resource` components to display resource information effectively.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic resource wrapper -->
{% call ui.util.call(ui.resource_wrapper) %}
    {{ ui.resource(resource_data) }}
{% endcall %}

<!-- Resource wrapper with attributes -->
{% call ui.util.call(ui.resource_wrapper, attrs={"class": "resource-listing"}) %}
    {{ ui.resource(another_resource) }}
{% endcall %}
```
///

## Tab Wrapper

The `tab_wrapper` component provides the structural container for tab-based interfaces. It works with `tab_handle` components to create consistent tab navigation and content switching experiences across different themes.

/// admonition | Relationship
    type: info

The `tab_wrapper` component is designed to work with `tab_handle` components. The wrapper provides the container structure, while the handles provide the interactive elements for switching between tab content.
///

/// details | Usage Example
    type: example

```jinja2
<!-- Basic tab wrapper -->
{% call ui.util.call(ui.tab_wrapper) %}
    {{ ui.tab_handle("Tab 1", href="/tab1") }}
    {{ ui.tab_handle("Tab 2", href="/tab2", active=True) }}
{% endcall %}

<!-- Tab wrapper with attributes -->
{% call ui.util.call(ui.tab_wrapper, attrs={"class": "tab-container"}) %}
    {{ ui.tab_handle("Settings", href="/settings") }}
{% endcall %}
```
///

## User Wrapper

The `user_wrapper` component creates a container for user-related content. It ensures that user profiles, activity, and related information maintain consistent styling and layout. This wrapper works with `user` components to display user information effectively.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic user wrapper -->
{% call ui.util.call(ui.user_wrapper) %}
    {{ ui.user(user_data) }}
{% endcall %}

<!-- User wrapper with attributes -->
{% call ui.util.call(ui.user_wrapper, attrs={"class": "user-profile"}) %}
    {{ ui.user(another_user) }}
{% endcall %}
```
///
