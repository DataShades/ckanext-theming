# Dataset Delete Confirmation Page

Confirm deletion of a dataset.

## Overview

Delete confirmation page provides:

- Final confirmation before deletion
- Warning about consequences

/// admonition | Screenshots
![confirm delete](../screenshots/dataset-confirm-delete.jpeg)
///

## URL Pattern

```
GET /dataset/delete/{id}
POST /dataset/delete/{id}
```

**Examples:**
```
<<vars.site_url>>/dataset/delete/annual-report
```

## Purpose

The delete page:

- Prevents accidental deletion
- Informs about impact
- Requires explicit confirmation

## Actions Available

| Action          | Description              |
|-----------------|--------------------------|
| Confirm delete  | Permanently remove       |
| Cancel          | Keep dataset             |

## Related Pages

- [Dataset Edit](edit.md) - Edit dataset
- [Dataset Read](read.md) - View dataset
- [Admin Trash](../admin/trash.md) - Purge deleted items
