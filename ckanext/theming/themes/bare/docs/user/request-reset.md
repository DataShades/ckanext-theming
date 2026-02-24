
# Password Reset Request Page

Request password reset email.

## Overview

Request reset page provides:

- Email input form
- Reset instructions
- Back to login link

/// admonition | Screenshots
![request reset](../screenshots/user-request-reset.jpeg)
///

## URL Pattern

```
GET /user/reset
POST /user/reset
```

## Purpose

Allows users to:

- Request password reset email
- Recover forgotten passwords
- Regain account access

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| Send email    | Request reset link       |
| Cancel        | Go back to login         |

## Related Pages

- [Login](login.md) - User login
- [Perform Reset](perform-reset.md) - Set new password
