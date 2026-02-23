# Admin Panel

Main administration dashboard.

## Overview

The admin panel provides:

- System overview
- Quick links to admin tools
- System statistics
- Administrator list

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

| Action         | Description         |
|----------------|---------------------|
| View config    | Edit site settings  |
| Manage trash   | Purge deleted items |
| View sysadmins | See administrators  |

## Template

**File:** `templates/admin/index.html`

## Screenshot Placeholder

![Admin Panel](../screenshots/admin-index.png)
*Placeholder: Admin dashboard with tools and stats*

## Related Pages

- [Config](config.md) - Site configuration
- [Trash](trash.md) - Purge deleted items
