# Register

Create a new user account.

## Overview

Registration page provides:

- Account creation form
- Email verification
- Password setup

/// admonition | Screenshots

![empty](../screenshots/user-register-form.jpeg)

///

## URL Pattern

```
GET /user/register
POST /user/register
```

**Example:**
```
<<vars.site_url>>/user/register
```

## Purpose

Allows visitors to:

- Create CKAN account
- Set username and password
- Provide email address

## Actions Available

| Action    | Description              |
|-----------|--------------------------|
| Register  | Create account           |
| Login     | Go to login              |

## Related Pages

- [Login](login.md) - User login
- [User Profile](read.md) - User profile
