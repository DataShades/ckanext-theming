
# Organization Members Page

View and manage organization members.

## Overview

The members page displays:

- List of organization members
- Member roles (admin, member, editor)
- Member count
- Add member functionality

/// admonition | Screenshots

/// tab | Members list
![list](../screenshots/organization-members.jpeg)
///

/// tab | Empty state
![empty](../screenshots/organization-members-empty.jpeg)
///

///

## URL Pattern

```
GET /organization/members/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/members/environmental-protection-agency
<<vars.site_url>>/organization/members/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The members page allows users to:

- View all organization members
- See member roles and permissions
- Add new members (if authorized)
- Manage member access

## Actions Available

| Action          | Description              |
|-----------------|--------------------------|
| View members    | See member list          |
| Add member      | Invite new member        |
| Edit role       | Change member role       |
| Remove member   | Delete membership        |

## Related Pages

- [Organization Read](read.md) - Main organization page
- [Add Member](member-new.md) - Add new member
- [Manage Members](manage-members.md) - Bulk management
