# Organizations

View organizations a user belongs to.

## Overview

Organizations page displays:

- User's organization memberships
- Role in each organization
- Organization details

/// admonition | Screenshots

![organizations](../screenshots/user-organizations.jpeg)

///

## URL Pattern

```
GET /user/{id}/organizations
```

## Purpose

Allows users to:

- View organization memberships
- See roles and permissions
- Navigate to organizations

## Actions Available

| Action           | Description              |
|------------------|--------------------------|
| View orgs        | See organization list    |
| View role        | See membership level     |
| Navigate to org  | Go to organization       |

## Related Pages

- [User Profile](read.md) - User profile
- [Organization Index](../organization/index.md) - All organizations
- [Dashboard Organizations](../dashboard/content.md) - My organizations
