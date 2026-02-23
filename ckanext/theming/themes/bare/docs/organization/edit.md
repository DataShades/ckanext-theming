# Organization Create Page

Form for creating new organizations in CKAN.

## Overview

The organization create page provides:

- Organization information form
- Image upload
- Custom field support

/// admonition | Screenshots

/// tab | Empty form
![empty](../screenshots/organization-new-empty.jpeg)
///

/// tab | Filled form
![filled](../screenshots/organization-new-filled.jpeg)
///

///

## URL Pattern

```
GET /organization/new
POST /organization/new
```

**Example:**
```
<<vars.site_url>>/organization/new
```

## Purpose

The create page allows authorized users to:

- Create new organizations
- Define organization details
- Upload organization logo

## Actions Available

| Action           | Description              |
|------------------|--------------------------|
| Enter details    | Fill organization form   |
| Upload image     | Add organization logo    |
| Save             | Create organization      |

## Related Pages

- [Organization Edit](edit.md) - Edit existing organization
- [Organization Read](read.md) - View created organization
- [Organization Index](index.md) - List all organizations
