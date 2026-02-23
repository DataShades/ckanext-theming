# Resource History

View version history of a resource.

## Overview

Resource history page displays:
- Resource revisions
- Change timestamps
- Editor information
- Version comparison

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

## Template

**File:** `templates/package/resource_history.html`

## Screenshot Placeholder

![Resource History](../screenshots/resource-history.png)
*Placeholder: Resource version history*

## Related Pages

- [Resource Edit](edit.md) - Edit resource
- [Dataset History](../dataset/history.md) - Dataset history
