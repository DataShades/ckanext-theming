# User API Tokens Page

Manage API access tokens.

## Overview

The API tokens page provides:
- List of active tokens
- Create new tokens
- Revoke tokens
- Token usage information

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
- Monitor token usage

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| Create token | Generate new token | New token button |
| Copy token | Copy to clipboard | Copy button |
| Revoke token | Delete token | Revoke button |
| View usage | See token activity | Usage link |

## Template

**File:** `templates/user/api_tokens.html`

## Screenshot Placeholder

![API Tokens](../screenshots/user-api-tokens.png)
*Placeholder: Token list with create form*

## Related Pages

- [User Profile](read.md) - User profile
- [API Documentation](../other/api.md) - API docs
