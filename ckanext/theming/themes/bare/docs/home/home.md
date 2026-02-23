# Home Page

The main landing page of the CKAN portal, serving as the entry point for
visitors.

## Overview

The home page provides:

- Site-wide search functionality
- Display of recent/featured datasets
- Statistics overview (dataset count, etc.)

![normal](../screenshots/homepage_normal.jpeg)

## URL Pattern

```
GET /
```

**Example:**
```
<<vars.site_url>>
```

## Purpose

The home page is the first impression visitors get of your CKAN instance. It should:
- Clearly communicate the purpose of the data portal
- Provide easy access to search functionality
- Showcase available datasets
- Guide users to main content areas

## Actions Available

| Action               | Description                            |
|----------------------|----------------------------------------|
| Search datasets      | Search across all datasets             |
| Browse datasets      | View recent datasets                   |
| Navigate to sections | Access datasets, organizations, groups |
| Login/Register       | Access user account features           |

## Related Pages

- [About Page](about.md) - Organization information
- [Dataset Search](../dataset/search.md) - Full dataset search
- [Login](../user/login.md) - User authentication
