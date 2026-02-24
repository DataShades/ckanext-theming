# Delete Confirmation

Confirm deletion of a group.

## Overview

Group delete confirmation:

- Final verification step
- Shows group information
- Warns about impact

/// admonition | Screenshots
![confirm delete](../screenshots/group-confirm-delete.jpeg)
///

## URL Pattern

```
GET /group/delete/{id}
POST /group/delete/{id}
```

## Purpose

Prevents accidental deletion of:

- Group metadata
- Group associations
- Dataset categorizations

## Actions Available

| Action          | Description              |
|-----------------|--------------------------|
| Confirm delete  | Permanently remove       |
| Cancel          | Keep group               |

## Related Pages

- [Group Edit](edit.md) - Edit group
- [Group Index](index.md) - Group list
