# Add Member

Add a new member to an organization.

## Overview

The add member page provides:

- User selection interface
- Role assignment
- Permission explanation

/// admonition | Screenshots

![form](../screenshots/organization-member-new.jpeg)

///

## URL Pattern

```
GET /organization/member_new/{id}
POST /organization/member_new/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/member_new/environmental-protection-agency
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
