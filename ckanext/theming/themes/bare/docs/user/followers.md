# User Activity Stream Page

View a user's activity history.

## Overview

User activity page displays:

- User's recent actions
- Dataset changes
- Contributions timeline

/// admonition | Screenshots
![activity](../screenshots/user-activity.jpeg)
///

## URL Pattern

```
GET /user/activity/{id}
```

**Examples:**
```
<<vars.site_url>>/user/activity/john-doe
<<vars.site_url>>/user/activity/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

Allows viewing:

- User contributions
- Creation history
- Modification activity

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| View activity | See activity items       |
| Filter        | Show specific types      |
| Load more     | Show older activity      |

## Related Pages

- [User Profile](read.md) - User profile
- [Dataset Activity](../dataset/activity.md) - Dataset activity
