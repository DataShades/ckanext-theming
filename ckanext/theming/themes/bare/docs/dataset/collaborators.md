# Dataset Collaborators

Manage dataset collaborators who have special permissions.

## Overview

Collaborators allow users who aren't organization members to:
- Edit specific datasets
- Manage dataset resources
- Have custom permission levels

## URL Pattern

```
GET /dataset/collaborators/{id}
POST /dataset/collaborators/{id}
GET /dataset/collaborators/{id}/new
POST /dataset/collaborators/{id}/new
GET /dataset/collaborators/{id}/delete/{user_id}
```

**Examples:**
```
<<vars.site_url>>/dataset/collaborators/annual-report
<<vars.site_url>>/dataset/collaborators/annual-report/new
```

## Purpose

Collaborators enable:
- Cross-organization collaboration
- Temporary access grants
- Fine-grained permissions
- External contributor support

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| View collaborators | See current collaborators | List |
| Add collaborator | Grant access to user | Add button |
| Edit permissions | Change access level | Permission dropdown |
| Remove collaborator | Revoke access | Remove button |

## Templates

**Files:**
- `package/collaborators/collaborators.html` - List view
- `package/collaborators/collaborator_new.html` - Add form
- `package/collaborators/confirm_delete.html` - Remove confirmation

### Capacity Levels

| Capacity | Permissions |
|----------|-------------|
| `editor` | Can edit dataset and resources |
| `admin` | Full control including delete |

## Screenshot Placeholder

![Collaborators](../screenshots/dataset-collaborators.png)
*Placeholder: Collaborator management list*

## Related Pages

- [Dataset Edit](edit.md) - Edit dataset
- [Organization Members](../organization/members.md) - Organization members
- [Dataset Resources](resources.md) - Resource management
