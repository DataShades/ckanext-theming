# Organization Changes Page

View the revision history of an organization.

## Overview

The changes page displays:

- Organization revision history
- Change timestamps
- Editor information
- Field-level changes

/// admonition | Screenshots
![changes](../screenshots/organization-changes.jpeg)
///

## URL Pattern

```
GET /organization/changes/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/changes/environmental-protection-agency
<<vars.site_url>>/organization/changes/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The changes page allows users to:

- Track organization modifications
- View previous versions
- Compare revisions
- Understand change history

## Actions Available

| Action            | Description              |
|-------------------|--------------------------|
| View revisions    | See change history       |
| Compare revisions | See differences          |
| View revision     | See specific version     |
| Restore revision  | Revert to previous       |

## Related Pages

- [Organization Read](read.md) - Main organization page
- [Organization Activity](activity.md) - Activity stream
- [Organization Edit](edit.md) - Edit organization
