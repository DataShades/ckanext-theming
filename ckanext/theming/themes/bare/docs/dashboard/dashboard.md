# Dashboard

Main user dashboard with activity feed.

## Overview

Dashboard provides:

- Personalized activity feed
- Quick statistics
- Content management shortcuts

/// admonition | Screenshots

![dashboard](../screenshots/dashboard.jpeg)

///

## URL Pattern

```
GET /dashboard
```

**Example:**
```
<<vars.site_url>>/dashboard
```

## Purpose

The dashboard allows users to:

- View recent activity from followed items
- Access quick actions
- Monitor notifications
- Navigate to personal content

## Actions Available

| Action           | Description              |
|------------------|--------------------------|
| View activity    | See activity feed        |
| View datasets    | Go to my datasets        |
| View orgs        | Go to my organizations   |
| View groups      | Go to my groups          |

## Related Pages

- [User Profile](../user/read.md) - User profile
- [User Activity](../user/activity.md) - Activity stream
- [Dashboard Datasets](datasets.md) - My datasets
- [Dashboard Organizations](organizations.md) - My organizations
- [Dashboard Groups](groups.md) - My groups
