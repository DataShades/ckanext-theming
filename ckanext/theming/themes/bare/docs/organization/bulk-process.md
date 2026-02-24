
# Organization Bulk Process Page

Manage all datasets owned by the organization in bulk.

## Overview

The bulk process page provides:

- List of all organization datasets
- Bulk edit capabilities
- State changes (activate/deactivate)
- Organization transfer

/// admonition | Screenshots
![bulk](../screenshots/organization-bulk-process.jpeg)
///

## URL Pattern

```
GET /organization/bulk_process/{id}
POST /organization/bulk_process/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/bulk_process/environmental-protection-agency
<<vars.site_url>>/organization/bulk_process/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The bulk process page allows administrators to:

- View all organization datasets
- Select multiple datasets
- Change dataset states in bulk
- Transfer ownership

## Actions Available

| Action         | Description              |
|----------------|--------------------------|
| Select datasets| Choose for bulk action   |
| Make public    | Set public state         |
| Make private   | Set private state        |
| Delete         | Remove datasets          |
| Transfer       | Change ownership         |

## Related Pages

- [Organization Read](read.md) - Main organization page
- [Dataset Edit](../dataset/edit.md) - Edit individual dataset
- [Dataset Search](../dataset/search.md) - Search datasets
