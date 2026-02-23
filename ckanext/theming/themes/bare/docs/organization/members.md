# Organization Edit Page

Form for editing existing organizations in CKAN.

## Overview

The organization edit page provides:

- Pre-populated form with current values
- All organization fields
- Image upload/replace
- Delete option

/// admonition | Screenshots

/// tab | Edit form
![form](../screenshots/organization-edit-form.jpeg)
///

/// tab | Delete section
![delete](../screenshots/organization-edit-delete-section.jpeg)
///

///

## URL Pattern

```
GET /organization/edit/{id}
POST /organization/edit/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/edit/environmental-protection-agency
<<vars.site_url>>/organization/edit/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
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
