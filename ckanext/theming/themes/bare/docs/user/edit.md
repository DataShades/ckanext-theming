# Edit Profile

Edit user profile information.

## Overview

The edit profile page provides:

- Profile information form
- Password change
- Image upload

/// admonition | Screenshots

![form](../screenshots/user-edit.jpeg)

///

## URL Pattern

```
GET /user/edit
POST /user/edit
```

**Example:**
```
<<vars.site_url>>/user/edit
```

## Purpose

The edit page allows users to:

- Update profile information
- Change password
- Upload profile image

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| Edit profile  | Modify user fields       |
| Change password | Update password        |
| Upload image  | Change profile picture   |

## Related Pages

- [User Profile](read.md) - View profile
- [User Register](new.md) - Registration form
