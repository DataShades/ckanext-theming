# User Edit Profile Page

Edit user profile information.

## Overview

The edit profile page provides:
- Profile information form
- Password change
- Image upload
- Custom field support

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
- Modify contact details

## Template

**File:** `templates/user/edit.html`

### Key Fields

- Name
- Email
- About/bio
- Profile image
- Current password (for changes)
- New password

## Screenshot Placeholder

![Edit Profile](../screenshots/user-edit.png)
*Placeholder: Profile edit form with all fields*

## Related Pages

- [User Profile](read.md) - View profile
- [User Register](new.md) - Registration form
- [Request Reset](request-reset.md) - Password reset
