# Admin Panel Page

Main administration dashboard.

## Overview

The admin panel provides:

- System overview
- Quick links to admin tools
- System statistics
- Administrator list

/// admonition | Screenshots

/// tab | Admin panel
![panel](../screenshots/admin-index.jpeg)
///

/// tab | Admin tools
![tools](../screenshots/admin-index-tools.jpeg)
///

///

## URL Pattern

```
GET /ckan-admin
```

**Example:**
```
<<vars.site_url>>/ckan-admin
```

## Purpose

The admin panel allows sysadmins to:

- View system status
- Access admin tools
- Manage site configuration
- Monitor system health

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| View config   | Edit site settings       |
| Manage trash  | Purge deleted items      |
| View sysadmins| See administrators       |

## Related Pages

- [Config](config.md) - Site configuration
- [Trash](trash.md) - Purge deleted items
