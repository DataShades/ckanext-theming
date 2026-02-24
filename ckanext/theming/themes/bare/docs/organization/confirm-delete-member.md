
# Delete Member Confirmation

Confirm removal of a member from an organization.

## Overview

Member delete confirmation:

- Verify member removal
- Show member role
- Confirm action

/// admonition | Screenshots
![confirm delete](../screenshots/organization-confirm-delete-member.jpeg)
///

## URL Pattern

```
GET /organization/member_delete/{id}
POST /organization/member_delete/{id}
```

## Purpose

Prevents accidental removal of:

- Organization access
- Member permissions
- Dataset ownership

## Actions Available

| Action          | Description              |
|-----------------|--------------------------|
| Confirm remove  | Remove member            |
| Cancel          | Keep member              |

## Related Pages

- [Organization Members](members.md) - Member list
- [Organization Manage Members](manage-members.md) - Manage members
