# Resource Delete Confirmation Page

Confirm deletion of a dataset resource.

## Overview

Resource delete confirmation:

- Final check before resource removal
- Shows resource information
- Warns about data loss

/// admonition | Screenshots
![confirm delete](../screenshots/dataset-confirm-delete-resource.jpeg)
///

## URL Pattern

```
GET /dataset/{id}/resource/{resource_id}/delete
POST /dataset/{id}/resource/{resource_id}/delete
```

## Purpose

Prevents accidental deletion of:

- Uploaded files
- Linked data
- Resource views

## Actions Available

| Action          | Description              |
|-----------------|--------------------------|
| Confirm delete  | Permanently remove       |
| Cancel          | Keep resource            |

## Related Pages

- [Resource Edit](../resource/edit.md) - Edit resource
- [Dataset Resources](resources.md) - Manage resources
- [Dataset Delete](confirm-delete.md) - Delete dataset
