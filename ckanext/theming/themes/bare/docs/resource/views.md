# Views Management

Manage visualizations for a resource.

## Overview

Resource views page provides:

- List of configured views
- View type selection
- View configuration

/// admonition | Screenshots
![views](../screenshots/resource-views.jpeg)
///

## URL Pattern

```
GET /dataset/{id}/resource/{resource_id}/views
GET /dataset/{id}/resource/{resource_id}/views/new
```

## Purpose

Allows users to:

- Create data visualizations
- Configure view types

## Actions Available

| Action       | Description              |
|--------------|--------------------------|
| View list    | See existing views       |
| Add view     | Create new view          |
| Edit view    | Modify view config       |

## Related Pages

- [Resource Read](read.md) - View resource
- [Resource Edit](edit.md) - Edit resource
- [Dataset Resource Views](../dataset/resource-views.md) - Dataset views
