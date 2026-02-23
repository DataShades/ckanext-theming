# Group Edit

Edit group metadata.

## Overview

Group edit page provides:
- Pre-populated form
- Image upload
- Description editing
- Custom fields

## URL Pattern

```
GET /group/edit/{id}
POST /group/edit/{id}
```

## Purpose

Allows authorized users to:
- Update group title
- Modify description
- Change group image
- Update custom fields

## Template

**File:** `templates/group/edit.html`

## Screenshot Placeholder

![Group Edit](../screenshots/group-edit.png)
*Placeholder: Group edit form*

## Related Pages

- [Group Read](read.md) - View group
- [Group Create](new.md) - Create group
