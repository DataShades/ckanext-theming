# Group Delete Confirmation

Confirm deletion of a group.

## Overview

Group delete confirmation:
- Final verification step
- Shows group information
- Warns about impact

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

## Template

**File:** `templates/group/confirm_delete.html`

## Screenshot Placeholder

![Group Delete](../screenshots/group-delete-confirm.png)
*Placeholder: Group delete confirmation*

## Related Pages

- [Group Edit](edit.md) - Edit group
- [Group Index](index.md) - Group list
