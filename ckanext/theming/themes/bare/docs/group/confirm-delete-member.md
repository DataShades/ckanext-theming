
# Group Delete Member Confirmation Page

Confirm removal of a member from a group.

## Overview

Member delete confirmation:

- Verify member removal
- Show member role
- Confirm action

/// admonition | Screenshots
![confirm delete](../screenshots/group-confirm-delete-member.jpeg)
///

## URL Pattern

```
GET /group/member_delete/{id}
POST /group/member_delete/{id}
```

## Purpose

Prevents accidental removal of:

- Group access
- Member permissions
- Dataset associations

## Actions Available

| Action          | Description              |
|-----------------|--------------------------|
| Confirm remove  | Remove member            |
| Cancel          | Keep member              |

## Related Pages

- [Group Members](members.md) - Member list
- [Group Manage Members](manage-members.md) - Manage members
