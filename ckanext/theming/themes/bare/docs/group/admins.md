# Group Manage Members Page

Bulk management of group members.

## Overview

Manage members page provides:

- Complete member list
- Bulk role changes
- Bulk removal
- Search/filter

/// admonition | Screenshots
![manage](../screenshots/group-manage-members.jpeg)
///

## URL Pattern

```
GET /group/member_manage/{id}
POST /group/member_manage/{id}
```

## Purpose

Allows administrators to:

- View all members at once
- Change multiple member roles
- Remove multiple members

## Actions Available

| Action         | Description              |
|----------------|--------------------------|
| Select members | Choose for bulk action   |
| Change roles   | Update multiple roles    |
| Remove members | Delete multiple members  |

## Related Pages

- [Group Members](members.md) - Member list
- [Group Add Member](member-new.md) - Add member
