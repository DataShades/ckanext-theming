# Organization Add Member Page

Add a new member to an organization.

## Overview

The add member page provides:

- User selection interface
- Role assignment
- Permission explanation

/// admonition | Screenshots

/// tab | Add member form
![form](../screenshots/organization-member-new.jpeg)
///

/// tab | Role help
![help](../screenshots/organization-member-new-role-help.jpeg)
///

///

## URL Pattern

```
GET /organization/member_new/{id}
POST /organization/member_new/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/member_new/environmental-protection-agency
<<vars.site_url>>/organization/member_new/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The add member page allows authorized users to:

- Search for existing users
- Select user to add
- Assign role (admin, editor, member)
- Set permissions

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| Search user   | Find user                |
| Select user   | Choose user              |
| Set role      | Assign role              |
| Add member    | Create membership        |

## Related Pages

- [Organization Members](members.md) - View all members
- [Manage Members](manage-members.md) - Bulk management
- [User Profile](../user/read.md) - User details
