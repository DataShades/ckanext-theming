# Group Add Member Page

Add a new member to a group.

## Overview

Add member page provides:

- User selection
- Role assignment
- Permission explanation

/// admonition | Screenshots
![add member](../screenshots/group-member-new.jpeg)
///

## URL Pattern

```
GET /group/member_new/{id}
POST /group/member_new/{id}
```

## Purpose

Allows authorized users to:

- Search for existing users
- Select user to add
- Assign role (admin, editor, member)

## Actions Available

| Action      | Description              |
|-------------|--------------------------|
| Search user | Find user                |
| Select user | Choose user              |
| Set role    | Assign role              |

## Related Pages

- [Group Members](members.md) - Member list
- [Group Manage Members](manage-members.md) - Manage members
