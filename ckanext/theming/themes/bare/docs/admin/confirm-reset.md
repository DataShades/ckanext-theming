# Admin Reset Configuration Confirmation

Confirm reset of site configuration to defaults.

## Overview

Reset confirmation page:
- Final verification
- Lists items to be reset
- Warns about data loss

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

## Template

**File:** `templates/admin/confirm_reset.html`

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| Confirm reset | Reset to defaults | Confirm button |
| Cancel | Keep current settings | Cancel button |

## Screenshot Placeholder

![Reset Config](../screenshots/admin-reset-config.png)
*Placeholder: Configuration reset confirmation*

## Related Pages

- [Admin Config](config.md) - Site configuration
- [Admin Panel](index.md) - Admin dashboard
