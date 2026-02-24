# Trash

Purge deleted items from the system.

## Overview

The trash page provides:

- List of deleted items
- Purge functionality
- Item type filtering
- Confirmation dialogs

/// admonition | Screenshots

/// tab | Trash list
![trash](../screenshots/admin-trash.jpeg)
///

/// tab | Confirm delete
![confirm](../screenshots/admin-trash-confirm-delete.jpeg)
///

///

## URL Pattern

```
GET /ckan-admin/trash
POST /ckan-admin/trash
```

**Example:**
```
<<vars.site_url>>/ckan-admin/trash
```

## Purpose

The trash page allows sysadmins to:

- View deleted datasets
- View deleted organizations
- View deleted groups
- Permanently purge items

## Actions Available

| Action         | Description              |
|----------------|--------------------------|
| View trash     | See deleted items        |
| Purge all      | Delete everything        |
| Purge by type  | Delete specific type     |

## Related Pages

- [Admin Panel](index.md) - Admin dashboard
- [Config](config.md) - Site configuration
