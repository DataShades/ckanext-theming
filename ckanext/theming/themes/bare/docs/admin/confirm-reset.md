
# Admin Reset Configuration Page

Confirm reset of site configuration to defaults.

## Overview

Reset confirmation page:

- Final verification
- Lists items to be reset
- Warns about data loss

/// admonition | Screenshots
![confirm reset](../screenshots/admin-confirm-reset.jpeg)
///

## URL Pattern

```
GET /ckan-admin/reset_config
POST /ckan-admin/reset_config
```

## Purpose

Resets configuration:

- Site title
- Site description
- Logo
- Custom CSS
- All configurable items

## Actions Available

| Action          | Description              |
|-----------------|--------------------------|
| Confirm reset   | Reset to defaults        |
| Cancel          | Keep current settings    |

## Related Pages

- [Admin Config](config.md) - Site configuration
- [Admin Panel](index.md) - Admin dashboard
