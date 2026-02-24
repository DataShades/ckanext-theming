# Activity Stream

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
| Load more       | Show older activity      |

## Related Pages

- [Organization Read](read.md) - Main organization page
- [Dataset Activity](../dataset/activity.md) - Dataset activity
