# User API Tokens Page

Manage API access tokens.

## Overview

The API tokens page provides:

- List of active tokens
- Create new tokens
- Revoke tokens
- Token usage information

/// admonition | Screenshots

/// tab | Token list
![tokens](../screenshots/user-api-tokens.jpeg)
///

/// tab | Create form
![create](../screenshots/user-api-tokens-create-form.jpeg)
///

///

## URL Pattern

```
GET /user/{id}/api-tokens
POST /user/{id}/api-tokens
```

**Examples:**
```
<<vars.site_url>>/user/john-doe/api-tokens
<<vars.site_url>>/user/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f/api-tokens
```

## Purpose

The API tokens page allows users to:

- Generate API access tokens
- Manage token permissions
- Revoke compromised tokens

## Actions Available

| Action       | Description              |
|--------------|--------------------------|
| Create token | Generate new token       |
| Copy token   | Copy to clipboard        |
| Revoke token | Delete token             |

## Related Pages

- [User Profile](read.md) - User profile
- [API Documentation](../other/api.md) - API docs
