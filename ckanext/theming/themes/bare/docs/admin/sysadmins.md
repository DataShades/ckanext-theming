# Sysadmins

Manage system administrators.

## Overview

The sysadmins page displays:

- List of current sysadmins
- Revoke sysadmin access
- Promote users to sysadmin
- User autocomplete for promotion

/// admonition | Screenshots

![sysadmins](../screenshots/admin-sysadmins.jpeg)

///

## URL Pattern

```
GET /ckan-admin
POST /ckan-admin
```

**Example:**
```
<<vars.site_url>>/ckan-admin
```

## Purpose

Allows sysadmins to:

- View current sysadmins
- Revoke sysadmin access from users
- Promote users to sysadmin
- Manage administrator access

## Actions Available

| Action              | Description              |
|---------------------|--------------------------|
| View sysadmins      | See sysadmin list        |
| Revoke access       | Remove sysadmin status   |
| Promote user        | Grant sysadmin status    |
| Search user         | Find user to promote     |

## Sysadmin Permissions

Sysadmins have full control over:

| Permission          | Description              |
|---------------------|--------------------------|
| Site configuration  | Modify site settings     |
| User management     | Manage all users         |
| Content management  | Manage all content       |
| System maintenance  | Purge deleted items      |

## Related Pages

- [Admin Config](config.md) - Site configuration
- [Admin Trash](trash.md) - Purge deleted items
- [User List](../user/list.md) - All users
