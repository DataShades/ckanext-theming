# Manage Members

Bulk management interface for organization members.

## Overview

The manage members page provides:

- Complete member list
- Role changes
- Member removal

/// admonition | Screenshots
![manage](../screenshots/organization-manage-members.jpeg)
///

## URL Pattern

```
GET /organization/member_manage/{id}
POST /organization/member_manage/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/member_manage/environmental-protection-agency
```

## Purpose

The manage members page allows administrators to:

- View all members at once
- Change member roles
- Remove members

## Actions Available

| Action         | Description            |
|----------------|------------------------|
| Select members | Choose for bulk action |
| Change roles   | Update roles           |
| Remove members | Delete members         |


## Related Pages

- [Organization Members](members.md) - Simple member list
- [Add Member](member-new.md) - Add single member
- [Administrators](admins.md) - Admin list
