# User Profile Page

View a user's public profile and activity.

## Overview

The user profile page displays:

- User information (name, bio, etc.)
- User statistics
- Recent activity
- Social links

/// admonition | Screenshots

/// tab | Main view
![main](../screenshots/user-read.jpeg)
///

/// tab | Activity section
![activity](../screenshots/user-read-activity.jpeg)
///

/// tab | Sidebar
![sidebar](../screenshots/user-read-sidebar.jpeg)
///

/// tab | Follow button
![follow](../screenshots/user-read-follow-button.jpeg)
///

///

## URL Pattern

```
GET /user/{id}
GET /user/{name}
```

**Examples:**
```
<<vars.site_url>>/user/john-doe
<<vars.site_url>>/user/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The profile page allows users to:

- View user information
- See user's public activity
- Follow/unfollow user
- Navigate to user's content

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| View info     | Read user details        |
| Follow        | Subscribe to updates     |
| View activity | See activity feed        |
| View datasets | See user's datasets      |

## Related Pages

- [Edit Profile](edit.md) - Modify profile
- [User Activity](activity.md) - Activity stream
- [User Followers](followers.md) - Follower list
