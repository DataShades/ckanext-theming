# Organization Activity Stream Page

View the activity stream for an organization.

## Overview

The activity page displays:

- Recent actions in the organization
- Dataset changes
- Member updates
- Organization modifications

/// admonition | Screenshots
![activity](../screenshots/organization-activity.jpeg)
///

## URL Pattern

```
GET /organization/activity/{id}
GET /organization/activity/{id}?offset={number}
```

**Examples:**
```
<<vars.site_url>>/organization/activity/environmental-protection-agency
<<vars.site_url>>/organization/activity/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The activity page allows users to:

- Track organization changes
- Monitor dataset updates
- See member activity
- Follow organization timeline

## Actions Available

| Action          | Description              |
|-----------------|--------------------------|
| View activity   | See activity items       |
| Filter activity | Show specific types      |
| Load more       | Show older activity      |
| Subscribe       | Follow organization      |

## Related Pages

- [Organization Read](read.md) - Main organization page
- [Organization Changes](changes.md) - Revision history
- [Dataset Activity](../dataset/activity.md) - Dataset activity
