# Organization Delete Confirmation

Confirm deletion of an organization.

## Overview

Organization delete confirmation:
- Final verification
- Shows organization impact
- Warns about datasets

## URL Pattern

```
GET /organization/delete/{id}
POST /organization/delete/{id}
```

## Purpose

Warns about consequences:
- Dataset ownership loss
- Member access removal
- Permanent deletion

## Template

**File:** `templates/organization/confirm_delete.html`

## Screenshot Placeholder

![Org Delete](../screenshots/organization-delete-confirm.png)
*Placeholder: Organization delete confirmation*

## Related Pages

- [Organization Edit](edit.md) - Edit organization
- [Organization Index](index.md) - Organization list
