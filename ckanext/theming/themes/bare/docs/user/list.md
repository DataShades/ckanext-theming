# User List Page

List all registered users.

## Overview

User list page provides:
- Directory of all users
- Search functionality
- Sorting options
- Pagination

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

| Action | Description | Element |
|--------|-------------|---------|
| Search users | Find users | Search input |
| Sort | Change order | Sort dropdown |
| View profile | See user details | User link |
| Pagination | Navigate pages | Page controls |

## Template

**File:** `templates/user/list.html`

### Sort Options

- Name (ascending/descending)
- Created date
- Last active

## Screenshot Placeholder

![User List](../screenshots/user-list.png)
*Placeholder: User directory listing*

## Related Pages

- [User Profile](read.md) - View profile
- [User Register](new.md) - Create account
