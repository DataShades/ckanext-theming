# User Followers Page

View users following a specific user.

## Overview

Followers page shows:

- List of followers
- Follower count
- User connections

/// admonition | Screenshots

/// tab | With followers
![with followers](../screenshots/user-followers-with-followers.jpeg)
///

/// tab | Empty state
![empty](../screenshots/user-followers-empty.jpeg)
///

///

## URL Pattern

```
GET /user/followers/{id}
```

## Purpose

Allows users to:

- See who is following the user
- Understand user influence
- Connect with followers

## Actions Available

| Action         | Description              |
|----------------|--------------------------|
| View followers | See follower list        |
| Follow         | Subscribe to user        |
| View profile   | Navigate to user         |

## Related Pages

- [User Profile](read.md) - User profile
- [Dataset Followers](../dataset/followers.md) - Dataset followers
