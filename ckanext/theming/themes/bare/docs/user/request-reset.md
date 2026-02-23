# Password Reset Pages

Password recovery flow pages.

## Overview

Password reset consists of two pages:
1. **Request Reset** - Request password reset email
2. **Perform Reset** - Set new password with reset key

## URL Patterns

### Request Reset
```
GET /user/reset
POST /user/reset
```

### Perform Reset
```
GET /user/reset/{key}
POST /user/reset/{key}
```

**Examples:**
```
<<vars.site_url>>/user/reset
<<vars.site_url>>/user/reset/abc123xyz
```

## Purpose

Password reset allows users to:
- Recover forgotten passwords
- Reset compromised credentials
- Regain account access

## Pages

### Request Reset Page

**Template:** `templates/user/request_reset.html`

**Fields:**
- Email address

**Actions:**
- Send reset email
- Cancel/Back to login

### Perform Reset Page

**Template:** `templates/user/perform_reset.html`

**Fields:**
- New password
- Confirm password

**Actions:**
- Set new password
- Cancel

## Screenshot Placeholders

### Request Reset
![Request Reset](../screenshots/user-request-reset.png)
*Placeholder: Email input form*

### Perform Reset
![Perform Reset](../screenshots/user-perform-reset.png)
*Placeholder: New password form*

## Related Pages

- [Login](login.md) - User login
- [Edit Profile](edit.md) - Change password when logged in
