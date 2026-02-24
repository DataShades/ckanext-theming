# Read

View organization details and browse its datasets.

## Overview

The organization read page displays:

- Organization profile information
- Datasets owned by organization
- Organization statistics
- Navigation to sub-pages

/// admonition | Screenshots

![main](../screenshots/organization-read.jpeg)

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
