
# User Login Page

User authentication page for logging into CKAN.

## Overview

The login page provides:

- Username/email and password fields
- Remember me option
- Password reset link
- Registration link

/// admonition | Screenshots

/// tab | Login form
![login](../screenshots/user-login.jpeg)
///

/// tab | Validation errors
![errors](../screenshots/user-login-errors.jpeg)
///

///

## URL Pattern

```
GET /user/login
POST /user/login
```

**Example:**
```
<<vars.site_url>>/user/login
```

## Purpose

The login page allows users to:

- Authenticate with credentials
- Access protected features
- Return to original page after login

## Actions Available

| Action           | Description              |
|------------------|--------------------------|
| Login            | Authenticate             |
| Remember me      | Stay logged in           |
| Reset password   | Recover account          |
| Register         | Create account           |

## Related Pages

- [Register](new.md) - Create account
- [Request Reset](request-reset.md) - Password recovery
- [Dashboard](../dashboard/dashboard.md) - After login destination
