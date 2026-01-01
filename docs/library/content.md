# Content Components

Content components represent major content entities in CKAN such as datasets, organizations, users, and other core entities. These components are responsible for displaying structured information about these entities.

## Overview

Content components are designed to display information about CKAN's core entities in a consistent and structured way. They handle the presentation of complex data structures like packages, organizations, users, and their relationships. These components often work in conjunction with their corresponding wrapper components to provide complete structural and visual representations.

## Activity Component

The `activity` component displays individual activity stream entries, showing user actions and system events in a structured format. It presents information about what happened, who performed the action, and when it occurred. This component is typically wrapped by the `activity_wrapper` to provide consistent grouping and styling of multiple activity entries.

Activity components are essential for showing the dynamic nature of a CKAN instance, allowing users to track changes, updates, and interactions with datasets and other content. The component handles various types of activities such as dataset creation, updates, and user interactions.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic activity component -->
{{ ui.activity("User created a new dataset", activity=activity_data) }}

<!-- Activity with attributes -->
{{ ui.activity("User updated profile", activity=activity_data, attrs={"class": "activity-item"}) }}
```
///

/// admonition | Relationship
    type: info

The `activity` component works with `activity_wrapper` to create organized activity streams. While the activity component handles individual entries, the wrapper provides the container for multiple entries.
///

## Facet Component

The `facet` component displays individual facet filter options, allowing users to refine search results and browse content by specific criteria. Facets are crucial for data discovery and exploration in CKAN, enabling users to filter datasets by organization, group, license, format, and other attributes.

The facet component typically displays the filter name, available options, and selection status. It works in conjunction with `facet_wrapper` and `facet_section` components to create comprehensive filtering interfaces. Facets are particularly important for large datasets where users need to narrow down results efficiently.

/// admonition | Relationship
    type: info

The `facet` component is closely related to `facet_wrapper` and `facet_section` components. The facet component displays individual filter options, while the wrapper and section components provide the structural container.
///

/// details | Usage Example
    type: example

```jinja2
<!-- Basic facet component -->
{{ ui.facet("Organization", key="org", value="Government", count=15, active=False) }}

<!-- Active facet component -->
{{ ui.facet("Format", key="format", value="CSV", count=8, active=True) }}
```
///

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | The text to display in the facet (the filter option name). |
| `key` | string | - | The facet key (e.g., "organization", "format"). |
| `value` | string | - | The specific value for this facet option. |
| `count` | int | - | Number of items matching this facet option. |
| `active` | bool | - | Whether this facet option is currently active. |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and behavior:

- `variant` (string): Style variant (e.g., "primary", "secondary") - theme-dependent
- `size` (string): Size of the facet (e.g., "sm", "lg") - theme-dependent
- `removable` (bool): Whether to show remove button for active facets - theme-dependent
- `icon` (string): Icon to display with the facet - theme-dependent
- `disabled` (bool): Whether the facet is disabled - theme-dependent

## License Component

The `license` component displays license information for datasets and other content. It presents licensing terms in a clear and accessible way, helping users understand the terms under which they can use, share, and modify the data. The component typically shows license name, URL, and description.

License components are important for data governance and compliance, ensuring that users understand the permissions and restrictions associated with datasets. Different themes may present license information differently, but the component interface remains consistent across implementations.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic license component -->
{{ ui.license("Creative Commons Attribution", id="cc-by", url="https://creativecommons.org/licenses/by/4.0/") }}

<!-- License with attributes -->
{{ ui.license("Open Data Commons", id="odc", attrs={"class": "license-info"}) }}
```
///

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | The license name or display text. |
| `id` | string | - | The license identifier. |
| `url` | string | - | The URL to the license details. |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and presentation:

- `variant` (string): Style variant (e.g., "full", "abbreviated") - theme-dependent
- `show_icon` (bool): Whether to show license icon - theme-dependent
- `inline` (bool): Whether to display inline with text - theme-dependent
- `size` (string): Size of the license display (e.g., "sm", "lg") - theme-dependent
- `show_url` (bool): Whether to show the license URL - theme-dependent

## Group Component

The `group` component displays information about CKAN groups, which are used to organize datasets around specific topics or themes. It presents group metadata including name, description, image, and associated datasets. Groups help users discover related datasets and understand the thematic organization of content.

The group component often includes links to view group details, browse datasets within the group, and access group-specific information. It works with `group_wrapper` to provide consistent presentation of multiple groups in listings and search results.

/// admonition | Relationship
    type: info

The `group` component is typically wrapped by `group_wrapper` components to provide consistent styling and layout when displaying multiple groups together.
///

/// details | Usage Example
    type: example

```jinja2
<!-- Basic group component -->
{{ ui.group(group_data) }}

<!-- Group with attributes -->
{{ ui.group(another_group, attrs={"class": "group-item"}) }}
```
///

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `group` | object | - | The group data object containing group information. |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and presentation:

- `variant` (string): Style variant (e.g., "card", "list") - theme-dependent
- `size` (string): Size of the group display (e.g., "sm", "lg") - theme-dependent
- `show_datasets` (bool): Whether to show dataset count - theme-dependent
- `show_description` (bool): Whether to show group description - theme-dependent
- `show_image` (bool): Whether to show group image - theme-dependent
///

## Organization Component

The `organization` component displays information about CKAN organizations, which represent institutions, departments, or other entities that publish datasets. It presents organizational metadata including name, description, image, and published datasets. Organizations are fundamental to CKAN's data governance model.

The organization component typically includes information about the organization's datasets, members, and administrative structure. It works with `organization_wrapper` to provide consistent presentation when displaying multiple organizations or organization listings.

/// admonition | Relationship
    type: info

The `organization` component is typically wrapped by `organization_wrapper` components to provide consistent styling and layout when displaying multiple organizations together.
///

/// details | Usage Example
    type: example

```jinja2
<!-- Basic organization component -->
{{ ui.organization(org_data) }}

<!-- Organization with attributes -->
{{ ui.organization(another_org, attrs={"class": "org-item"}) }}
```
///

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `organization` | object | - | The organization data object containing organization information. |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and presentation:

- `variant` (string): Style variant (e.g., "card", "list") - theme-dependent
- `size` (string): Size of the organization display (e.g., "sm", "lg") - theme-dependent
- `show_datasets` (bool): Whether to show dataset count - theme-dependent
- `show_description` (bool): Whether to show organization description - theme-dependent
- `show_image` (bool): Whether to show organization image - theme-dependent
///

## Package Component

The `package` component displays information about CKAN packages (datasets), which are the core content items in CKAN. It presents dataset metadata including title, description, resources, tags, and other relevant information. The package component is central to CKAN's data discovery functionality.

The component handles complex dataset information including multiple resources, metadata fields, and relationships with organizations and groups. It works with `package_wrapper` to provide consistent presentation in search results, listings, and related dataset displays.

/// admonition | Relationship
    type: info

The `package` component is typically wrapped by `package_wrapper` components to provide consistent styling and layout when displaying multiple packages together.
///

/// details | Usage Example
    type: example

```jinja2
<!-- Basic package component -->
{{ ui.package(dataset_data) }}

<!-- Package with attributes -->
{{ ui.package(another_dataset, attrs={"class": "dataset-item"}) }}
```
///

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `pkg` | object | - | The package/dataset data object containing dataset information. |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and presentation:

- `variant` (string): Style variant (e.g., "card", "list") - theme-dependent
- `size` (string): Size of the package display (e.g., "sm", "lg") - theme-dependent
- `show_resources` (bool): Whether to show resource count - theme-dependent
- `show_description` (bool): Whether to show dataset description - theme-dependent
- `show_badges` (bool): Whether to show status badges - theme-dependent
///

## Resource Component

The `resource` component displays information about individual resources within packages. Resources represent the actual data files or links within a dataset, including file format, size, description, and download links. The component handles various resource types including uploaded files, external links, and API endpoints.

Resource components are crucial for data access, providing users with the means to download, view, or interact with the actual data contained in datasets. The component works with `resource_wrapper` to provide consistent presentation when displaying multiple resources within a package.

/// admonition | Relationship
    type: info

The `resource` component is typically wrapped by `resource_wrapper` components to provide consistent styling and layout when displaying multiple resources together.
///

/// details | Usage Example
    type: example

```jinja2
<!-- Basic resource component -->
{{ ui.resource(resource_data) }}

<!-- Resource with attributes -->
{{ ui.resource(another_resource, attrs={"class": "resource-item"}) }}
```
///

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `resource` | object | - | The resource data object containing resource information. |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and presentation:

- `variant` (string): Style variant (e.g., "card", "list") - theme-dependent
- `size` (string): Size of the resource display (e.g., "sm", "lg") - theme-dependent
- `show_download` (bool): Whether to show download button - theme-dependent
- `show_format` (bool): Whether to show file format - theme-dependent
- `show_size` (bool): Whether to show file size - theme-dependent
///

## User Component

The `user` component displays information about CKAN users, including profile information, activity, and contributions. It presents user metadata such as name, display name, bio, and associated content like created datasets or organizations. The component handles both public profile information and user-specific details when appropriate.

User components are important for community features and understanding content provenance. They work with `user_wrapper` to provide consistent presentation when displaying multiple users or user listings, such as member lists or contributor information.

/// admonition | Relationship
    type: info

The `user` component is typically wrapped by `user_wrapper` components to provide consistent styling and layout when displaying multiple users together.
///

/// details | Usage Example
    type: example

```jinja2
<!-- Basic user component -->
{{ ui.user(user_data) }}

<!-- User with attributes -->
{{ ui.user(another_user, attrs={"class": "user-item"}) }}
```
///

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `user` | object | - | The user data object containing user information. |

#### Theme-Specific Parameters

Different themes may support additional parameters for styling and presentation:

- `variant` (string): Style variant (e.g., "card", "inline") - theme-dependent
- `size` (string): Size of the user display (e.g., "sm", "lg") - theme-dependent
- `show_avatar` (bool): Whether to show user avatar - theme-dependent
- `show_display_name` (bool): Whether to show user's display name - theme-dependent
- `show_link` (bool): Whether to link to user profile - theme-dependent
///
