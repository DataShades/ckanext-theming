
# Group Edit Page

Edit group metadata.

## Overview

Group edit page provides:

- Pre-populated form
- Image upload
- Description editing

/// admonition | Screenshots
![edit](../screenshots/group-edit-form.jpeg)
///

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

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| Edit details  | Modify group fields      |
| Update image  | Change logo              |
| View group    | See public view          |

## Related Pages

- [Group Read](read.md) - View group
- [Group Create](new.md) - Create group
