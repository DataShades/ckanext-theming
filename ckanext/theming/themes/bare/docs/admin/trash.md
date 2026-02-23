# Admin Trash Page

Purge deleted items from the system.

## Overview

The trash page provides:
- List of deleted items
- Purge functionality
- Item type filtering
- Confirmation dialogs

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
- Restore items (if supported)

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| View trash | See deleted items | Item list |
| Purge all | Delete everything | Purge all button |
| Purge by type | Delete specific type | Type purge button |
| Cancel | Abort purge | Cancel button |

## Template

**File:** `templates/admin/trash.html`

## Screenshot Placeholder

![Trash](../screenshots/admin-trash.png)
*Placeholder: Deleted items list with purge options*

## Related Pages

- [Admin Panel](index.md) - Admin dashboard
- [Config](config.md) - Site configuration
