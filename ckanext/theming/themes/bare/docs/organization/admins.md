# Organization Manage Members Page

Bulk management interface for organization members.

## Overview

The manage members page provides:

- Complete member list
- Bulk role changes
- Bulk removal
- Member search/filter

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
<<vars.site_url>>/organization/member_manage/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The manage members page allows administrators to:

- View all members at once
- Change multiple member roles
- Remove multiple members
- Search and filter members

## Actions Available

| Action           | Description              |
|------------------|--------------------------|
| Select members   | Choose for bulk action   |
| Change roles     | Update multiple roles    |
| Remove members   | Delete multiple members  |
| Search           | Filter members           |

## Related Pages

- [Organization Members](members.md) - Simple member list
- [Add Member](member-new.md) - Add single member
- [Administrators](admins.md) - Admin list
