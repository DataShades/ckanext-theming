# Collaborators

Manage dataset collaborators who have special permissions.

## Overview

Collaborators allow users who aren't organization members to:

- Edit specific datasets
- Have custom permission levels

/// admonition | Screenshots

/// tab | Empty state
![empty](../screenshots/dataset-collaborators-empty.jpeg)
///

/// tab | With collaborator
![with collaborator](../screenshots/dataset-collaborators-with-collaborator.jpeg)
///

///

## URL Pattern

```
GET /dataset/collaborators/{id}
POST /dataset/collaborators/{id}
```

**Examples:**
```
<<vars.site_url>>/dataset/collaborators/annual-report
```

## Purpose

Collaborators enable:

- Cross-organization collaboration
- Temporary access grants
- Fine-grained permissions

## Actions Available

| Action              | Description              |
|---------------------|--------------------------|
| View collaborators  | See current collaborators |
| Add collaborator    | Grant access to user     |
| Edit permissions    | Change access level      |
| Remove collaborator | Revoke access            |

## Related Pages

- [Dataset Edit](edit.md) - Edit dataset
- [Organization Members](../organization/members.md) - Organization members
- [Dataset Resources](resources.md) - Resource management
