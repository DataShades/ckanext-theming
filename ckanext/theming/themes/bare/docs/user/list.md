# List

List all registered users.

## Overview

User list page provides:

- Directory of all users
- Search functionality
- Sorting options
- Pagination

/// admonition | Screenshots

/// tab | User list
![list](../screenshots/user-list.jpeg)
///

/// tab | Search results
![search](../screenshots/user-list-search.jpeg)
///

///

## URL Pattern

```
GET /user
GET /user?q={query}
GET /user?order_by={field}
```

**Examples:**
```
<<vars.site_url>>/user
<<vars.site_url>>/user?q=john
<<vars.site_url>>/user?order_by=created
```

## Purpose

Allows users to:

- Browse all users
- Find specific users
- View user profiles
- See community size

## Actions Available

| Action       | Description              |
|--------------|--------------------------|
| Search users | Find users               |
| Sort         | Change order             |
| View profile | See user details         |

## Related Pages

- [User Profile](read.md) - View profile
- [User Register](new.md) - Create account
