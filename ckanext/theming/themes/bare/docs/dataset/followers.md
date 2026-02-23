# Dataset Followers Page

View the list of users following a dataset.

## Overview

The followers page displays:

- List of users following the dataset

/// admonition | Screenshots

/// tab | With followers
![with followers](../screenshots/dataset-followers-with-followers.jpeg)
///

/// tab | Empty state
![empty](../screenshots/dataset-followers-empty.jpeg)
///

///

## URL Pattern

```
GET /dataset/followers/{id}
```

**Examples:**
```
<<vars.site_url>>/dataset/followers/annual-environmental-report
```

## Purpose

The followers page allows users to:

- See who is following the dataset
- Understand dataset popularity
- Connect with interested users

## Actions Available

| Action            | Description              |
|-------------------|--------------------------|
| View followers    | See follower list        |
| View user profile | Navigate to user         |

## Related Pages

- [Dataset Read](read.md) - Main dataset view
- [User Profile](../user/read.md) - User profile page
- [Dataset Activity](activity.md) - Activity stream
