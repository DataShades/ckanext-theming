# User Confirm Delete

Confirm deletion of a user account.

## Overview

User delete confirmation:
- Final verification
- Account deletion warning
- Data impact notice

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

## Template

**File:** `templates/user/confirm_delete.html`

## Screenshot Placeholder

![User Delete](../screenshots/user-delete-confirm.png)
*Placeholder: User account deletion confirmation*

## Related Pages

- [Edit Profile](edit.md) - Edit profile
- [User Profile](read.md) - View profile
