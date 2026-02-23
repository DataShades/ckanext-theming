# Admin Config Page

Site configuration management.

## Overview

The config page provides:
- Site settings form
- Branding options
- Feature toggles
- Configuration reset

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

## Template

**File:** `templates/admin/config.html`

## Screenshot Placeholder

![Config](../screenshots/admin-config.png)
*Placeholder: Configuration form with all settings*

## Related Pages

- [Admin Panel](index.md) - Admin dashboard
- [Reset Config](index.md) - Reset to defaults
