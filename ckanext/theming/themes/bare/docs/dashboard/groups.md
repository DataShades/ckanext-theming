# Dashboard Groups Page

View and manage your groups.

## Overview

The groups dashboard displays:

- Groups you belong to
- Your role in each group
- Quick access to group pages

/// admonition | Screenshots

![groups](../screenshots/dashboard-groups.jpeg)

///

## URL Pattern

```
GET /dashboard/groups
```

**Example:**
```
<<vars.site_url>>/dashboard/groups
```

## Purpose

Allows users to:

- View group memberships
- See roles and permissions
- Navigate to groups
- Manage groups (if member)

## Actions Available

| Action         | Description              |
|----------------|--------------------------|
| View groups    | See group list           |
| Navigate to group | Go to group           |
| Manage group   | Edit group               |
| View members   | See group members        |

## Related Pages

- [Dashboard](dashboard.md) - Main dashboard
- [Group Index](../group/index.md) - Browse groups
- [Group Create](../group/new.md) - Create group
