# Admin Config Page

Site configuration management.

## Overview

The config page provides:

- Site settings form
- Branding options
- Feature toggles
- Configuration reset

/// admonition | Screenshots

/// tab | Config form
![config](../screenshots/admin-config.jpeg)
///

/// tab | Form fields
![form](../screenshots/admin-config-form.jpeg)
///

///

## URL Pattern

```
GET /ckan-admin/config
POST /ckan-admin/config
```

**Example:**
```
<<vars.site_url>>/ckan-admin/config
```

## Purpose

The config page allows sysadmins to:

- Customize site appearance
- Configure features
- Update branding
- Reset to defaults

## Actions Available

| Action          | Description              |
|-----------------|--------------------------|
| Edit config     | Modify site settings     |
| Save changes    | Apply configuration      |
| Reset config    | Restore defaults         |

## Related Pages

- [Admin Panel](index.md) - Admin dashboard
- [Reset Config](confirm-reset.md) - Reset to defaults
