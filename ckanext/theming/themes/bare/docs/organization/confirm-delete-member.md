# Organization Delete Confirmation Page

Confirm deletion of an organization.

## Overview

Organization delete confirmation:

- Final verification
- Shows organization impact
- Warns about datasets

/// admonition | Screenshots
![confirm delete](../screenshots/organization-confirm-delete.jpeg)
///

## URL Pattern

```
GET /organization/delete/{id}
POST /organization/delete/{id}
```

## Purpose

Warns about consequences:

- Dataset ownership loss
- Member access removal
- Permanent deletion

## Actions Available

| Action          | Description              |
|-----------------|--------------------------|
| Confirm delete  | Permanently remove       |
| Cancel          | Keep organization        |

## Related Pages

- [Organization Edit](edit.md) - Edit organization
- [Organization Index](index.md) - Organization list
