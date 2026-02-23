# User Activity Stream

View a user's activity history.

## Overview

User activity page displays:
- User's recent actions
- Dataset changes
- Contributions timeline
- Activity feed

## URL Pattern

```
GET /user/activity/{id}
GET /user/activity/{id}?offset={number}
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
- Follow actions

## Template

**File:** `templates/user/activity_stream.html`

## Screenshot Placeholder

![User Activity](../screenshots/user-activity.png)
*Placeholder: User activity feed*

## Related Pages

- [User Profile](read.md) - User profile
- [Dataset Activity](../dataset/activity.md) - Dataset activity
- [Organization Activity](../organization/activity.md) - Organization activity
