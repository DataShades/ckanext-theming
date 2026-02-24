# Administrators

View the list of administrators for an organization.

## Overview

The administrators page displays:

- List of users with admin role

/// admonition | Screenshots

![list](../screenshots/organization-admins.jpeg)

///

## URL Pattern

```
GET /organization/admins/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/admins/environmental-protection-agency
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
| View profile  | Navigate to user         |
| Add admin     | Promote to admin         |

## Related Pages

- [Organization Members](members.md) - All members
- [Organization Manage Members](manage-members.md) - Bulk management
- [Add Member](member-new.md) - Add new member
