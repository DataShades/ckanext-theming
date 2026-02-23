# Group Activity Stream Page

View group activity history.

## Overview

Activity page displays:

- Recent group actions
- Dataset changes
- Member updates
- Timeline

/// admonition | Screenshots
![activity](../screenshots/group-activity.jpeg)
///

## URL Pattern

```
GET /group/activity/{id}
```

## Purpose

Allows users to:

- Track group changes
- Monitor dataset updates
- See member activity

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| View activity | See activity items       |
| Filter        | Show specific types      |
| Load more     | Show older activity      |

## Related Pages

- [Group Read](read.md) - Group profile
- [Group Changes](changes.md) - Revision history
