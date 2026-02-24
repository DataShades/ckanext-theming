# Confirm Delete

Confirm deletion of a user account.

## Overview

User delete confirmation:

- Final verification
- Account deletion warning
- Data impact notice

/// admonition | Screenshots
![confirm delete](../screenshots/user-confirm-delete.jpeg)
///

## URL Pattern

```
GET /user/delete/{id}
POST /user/delete/{id}
```

## Purpose

Warns about consequences:

- Account removal
- Dataset ownership changes
- Membership removal
- API token revocation

## Actions Available

| Action          | Description              |
|-----------------|--------------------------|
| Confirm delete  | Permanently remove       |
| Cancel          | Keep account             |

## Related Pages

- [Edit Profile](edit.md) - Edit profile
- [User Profile](read.md) - View profile
