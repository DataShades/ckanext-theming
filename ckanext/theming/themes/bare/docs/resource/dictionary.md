# Resource Data Dictionary Page

View version history of a resource.

## Overview

Resource history page displays:

- Resource revisions
- Change timestamps
- Editor information
- Version comparison

/// admonition | Screenshots
![history](../screenshots/resource-history.jpeg)
///

## URL Pattern

```
GET /dataset/{id}/resource/{resource_id}/history
```

## Purpose

Allows users to:

- Track resource changes
- View previous versions
- Compare revisions
- Restore previous versions

## Actions Available

| Action            | Description              |
|-------------------|--------------------------|
| View revisions    | See change history       |
| Compare revisions | See differences          |
| View revision     | See specific version     |

## Related Pages

- [Resource Edit](edit.md) - Edit resource
