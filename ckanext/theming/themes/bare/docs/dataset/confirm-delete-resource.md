# Resource Delete Confirmation

Confirm deletion of a dataset resource.

## Overview

Resource delete confirmation:
- Final check before resource removal
- Shows resource information
- Warns about data loss

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

## Template

**File:** `templates/package/confirm_delete_resource.html`

## Screenshot Placeholder

![Resource Delete](../screenshots/resource-delete-confirm.png)
*Placeholder: Resource delete confirmation*

## Related Pages

- [Resource Edit](../resource/edit.md) - Edit resource
- [Dataset Resources](resources.md) - Manage resources
- [Dataset Delete](confirm-delete.md) - Delete dataset
