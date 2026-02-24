# Edit

Form for editing existing organizations in CKAN.

## Overview

The organization edit page provides:

- Pre-populated form with current values
- All organization fields
- Image upload/replace
- Delete option

/// admonition | Screenshots

![form](../screenshots/organization-edit-form.jpeg)

///

## URL Pattern

```
GET /organization/edit/{id}
POST /organization/edit/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/edit/environmental-protection-agency
```

## Purpose

The edit page allows authorized users to:

- Modify organization details
- Update logo/image
- Change contact information
- Delete organization (if authorized)

## Actions Available

| Action           | Description              |
|------------------|--------------------------|
| Edit details     | Modify org fields        |
| Update image     | Change logo              |
| Delete org       | Remove organization      |
| View org         | See public view          |

## Related Pages

- [Organization Create](new.md) - Create new organization
- [Organization Read](read.md) - View organization
- [Organization Delete](confirm-delete.md) - Delete confirmation
