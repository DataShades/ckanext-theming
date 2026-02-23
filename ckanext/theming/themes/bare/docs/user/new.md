# User Register

Create a new user account.

## Overview

Registration page provides:
- Account creation form
- Email verification
- Password setup
- Terms acceptance

## URL Pattern

```
GET /user/register
POST /user/register
```

## Purpose

Allows visitors to:
- Create CKAN account
- Set username and password
- Provide email address
- Accept terms of service

## Template

**File:** `templates/user/new.html`

### Form Fields

- Username (required)
- Email (required)
- Password (required)
- Password confirmation (required)
- Name (optional)

## Screenshot Placeholder

![Register](../screenshots/user-register.png)
*Placeholder: Registration form*

## Related Pages

- [Login](login.md) - User login
- [User Profile](read.md) - User profile
