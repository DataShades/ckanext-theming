# Dataset Section

This section covers all pages related to dataset (package) management and viewing in CKAN.

## Overview

Datasets (packages) are the core content type in CKAN. This section includes pages for:

- Searching and browsing datasets
- Viewing dataset details
- Creating and editing datasets
- Managing dataset resources
- Viewing dataset history and activity

## Pages in This Section

| Page                                | Description                  |
|-------------------------------------|------------------------------|
| [Search](search.md)                 | Search and filter datasets   |
| [Read](read.md)                     | View dataset details         |
| [Create](new.md)                    | Create new dataset           |
| [Edit](edit.md)                     | Edit dataset metadata        |
| [History](history.md)               | View dataset version history |
| [Activity](activity.md)             | Dataset activity stream      |
| [Followers](followers.md)           | Dataset followers list       |
| [Groups](groups.md)                 | Dataset group associations   |
| [Resources](resources.md)           | Manage dataset resources     |

## Common Templates

### `_base.html`
Base template for all dataset pages:
```jinja
{% extends "_layout.html" %}
{%- set _layout = _layout|default("right_sidebar") -%}
{% set dataset_type = pkg_dict.type if pkg_dict else dataset_type or 'dataset' %}
```

### `_edit_base.html`
Base template for edit/create pages:
```jinja
{% extends "package/_base.html" %}
```

### Key Macros

| Macro | Description | Usage |
|-------|-------------|-------|
| `ui.package()` | Display package card | Package listings |
| `ui.resource()` | Display resource card | Resource listings |
| `ui.search_form()` | Search form | Search page |
| `ui.facet_section()` | Facet filter section | Search sidebar |
| `ui.form()` | Form wrapper | Create/Edit forms |
| `ui.input()` | Form input | Form fields |

## URL Structure

```
/dataset                          # Search/Browse
/dataset/{id}                     # Read dataset
/dataset/new                      # Create dataset
/dataset/edit/{id}                # Edit dataset
/dataset/delete/{id}              # Delete dataset
/dataset/activity/{id}            # Activity stream
/dataset/followers/{id}           # Followers
/dataset/groups/{id}              # Groups association
/dataset/resources/{id}           # Manage resources
/dataset/{id}/resource/{rid}      # Read resource
/dataset/{id}/resource/{rid}/edit # Edit resource
/dataset/{id}/resource/{rid}/views # Manage views
```

## Customization Tips

1. **Search Page**: Customize facets, sorting options, and result display
2. **Read Page**: Enhance dataset display with custom fields and visualizations
3. **Forms**: Add custom form fields and validation
4. **Resources**: Customize resource preview and download options
5. **Styling**: Apply consistent theming across all dataset pages

## Screenshots

<!-- TODO: Add screenshots of your themed dataset pages -->

### Dataset Search
![Dataset Search](../screenshots/dataset-search.png)
*Placeholder: Search results with facets sidebar*

### Dataset Read
![Dataset Read](../screenshots/dataset-read.png)
*Placeholder: Full dataset view with resources*

### Dataset Edit Form
![Dataset Edit](../screenshots/dataset-edit.png)
*Placeholder: Dataset edit form*

## Related Sections

- [Organization](../organization/index.md) - Dataset ownership
- [Resource](../resource/index.md) - Dataset resources
- [Group](../group/index.md) - Dataset group associations
- [Admin](../admin/index.md) - Dataset administration
