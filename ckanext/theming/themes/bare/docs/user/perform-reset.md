# Password Reset Perform Page

Set new password with reset key.

## Overview

Perform reset page provides:

- New password form
- Password confirmation
- Reset instructions

/// admonition | Screenshots

/// tab | Reset form
![reset](../screenshots/user-perform-reset.jpeg)
///

/// tab | Invalid key
![invalid](../screenshots/user-perform-reset-invalid-key.jpeg)
///

///

## URL Pattern

```
GET /user/reset/{key}
POST /user/reset/{key}
```

## Purpose

Allows users to:

- Set new password
- Confirm password match
- Regain account access

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| Set password  | Update password          |
| Cancel        | Go back to login         |

## Related Pages

- [Login](login.md) - User login
- [Request Reset](request-reset.md) - Password reset request
