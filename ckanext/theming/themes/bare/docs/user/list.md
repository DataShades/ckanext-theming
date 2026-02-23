# User Groups Page

View groups a user belongs to.

## Overview

Groups page displays:

- User's group memberships
- Role in each group
- Group details

/// admonition | Screenshots

/// tab | With groups
![groups](../screenshots/user-groups.jpeg)
///

/// tab | Empty state
![empty](../screenshots/user-groups-empty.jpeg)
///

///

## URL Pattern

```
GET /user/{id}/groups
```

## Purpose

Allows users to:

- View group memberships
- See roles and permissions
- Navigate to groups

## Actions Available

| Action          | Description              |
|-----------------|--------------------------|
| View groups     | See group list           |
| View role       | See membership level     |
| Navigate to group | Go to group            |

## Related Pages

- [User Profile](read.md) - User profile
- [Group Index](../group/index.md) - All groups
- [Dashboard Groups](../dashboard/content.md) - My groups
