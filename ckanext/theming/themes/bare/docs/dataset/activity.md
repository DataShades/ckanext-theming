# Activity Stream

View the activity stream and recent changes for a dataset.

## Overview

The activity page displays:

- Recent actions on the dataset
- Timestamps for each action
- Action types (create, update, delete, etc.)

/// admonition | Screenshots
![activity](../screenshots/dataset-activity-stream.jpeg)
///

## URL Pattern

```
GET /dataset/activity/{id}
```

**Examples:**
```
<<vars.site_url>>/dataset/activity/annual-environmental-report
```

## Purpose

The activity page allows users to:

- Track recent changes to dataset
- See who made what changes
- Follow activity timeline

## Actions Available

| Action          | Description              |
|-----------------|--------------------------|
| View activity   | See activity items       |
| Load more       | Show older activity      |

## Related Pages

- [Dataset Read](read.md) - Main dataset view
- [User Activity](../user/activity.md) - User activity stream
