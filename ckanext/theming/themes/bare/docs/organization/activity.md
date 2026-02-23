# Organization Administrators Page

View the list of administrators for an organization.

## Overview

The administrators page displays:

- List of users with admin role
- Admin count
- Admin permissions
- Contact information

/// admonition | Screenshots

/// tab | Admins list
![list](../screenshots/organization-admins.jpeg)
///

/// tab | Empty state
![empty](../screenshots/organization-admins-empty.jpeg)
///

///

## URL Pattern

```
GET /organization/admins/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/admins/environmental-protection-agency
<<vars.site_url>>/organization/admins/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The administrators page allows users to:

- See who manages the organization
- Identify decision makers
- Contact administrators

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| View admins   | See admin list           |
| Contact admin | Reach out                |
| View profile  | Navigate to user         |
| Add admin     | Promote to admin         |

## Related Pages

- [Organization Members](members.md) - All members
- [Organization Manage Members](manage-members.md) - Bulk management
- [Add Member](member-new.md) - Add new member
