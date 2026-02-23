# Resource Views Management

Manage visualizations for a resource.

## Overview

Resource views page provides:
- List of configured views
- View type selection
- View configuration
- View ordering

## URL Pattern

```
GET /dataset/{id}/resource/{resource_id}/views
GET /dataset/{id}/resource/{resource_id}/views/new
POST /dataset/{id}/resource/{resource_id}/views
```

## Purpose

Allows users to:
- Create data visualizations
- Configure view types
- Reorder views
- Enable/disable views

## Templates

**Files:**
- `templates/package/resource_views.html` - Views list
- `templates/package/new_view.html` - Create/edit view
- `templates/package/edit_view.html` - Edit view
- `templates/package/snippets/_resource_view.html` - View snippet

### View Types

| Type | Description |
|------|-------------|
| `recline_view` | Data grid/table |
| `recline_graph_view` | Charts and graphs |
| `recline_map_view` | Geographic maps |
| `image_view` | Image display |
| `webpage_view` | Web page embed |
| `pdf_view` | PDF viewer |
| `datatables_view` | Sortable tables |

## Screenshot Placeholder

![Resource Views](../screenshots/resource-views.png)
*Placeholder: View management interface*

## Related Pages

- [Resource Read](read.md) - View resource
- [Resource Edit](edit.md) - Edit resource
- [Dataset Resource Views](../dataset/resource-views.md) - Dataset views
