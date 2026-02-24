
# Organization Read Page

View organization details and browse its datasets.

## Overview

The organization read page displays:

- Organization profile information
- Datasets owned by organization
- Organization statistics
- Navigation to sub-pages

/// admonition | Screenshots

/// tab | Main view
![main](../screenshots/organization-read.jpeg)
///

/// tab | Datasets section
![datasets](../screenshots/organization-read-datasets.jpeg)
///

/// tab | Sidebar info
![sidebar](../screenshots/organization-read-sidebar.jpeg)
///

/// tab | Edit button
![edit](../screenshots/organization-read-edit-button.jpeg)
///

///

## URL Pattern

```
GET /organization/{id}
GET /organization/{name}
GET /organization/{id}?page={number}
```

**Examples:**
```
<<vars.site_url>>/organization/environmental-protection-agency
<<vars.site_url>>/organization/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The read page allows users to:

- View organization information
- Browse organization's datasets
- Understand organization's role
- Access organization management

## Actions Available

| Action            | Description              |
|-------------------|--------------------------|
| View datasets     | Browse org datasets      |
| Search datasets   | Filter org datasets      |
| Follow org        | Subscribe to updates     |
| Edit org          | Modify organization      |
| View about        | See org details          |

## Related Pages

- [Organization Index](index.md) - List all organizations
- [Organization About](about.md) - Organization details
- [Organization Edit](edit.md) - Edit organization
