# Organization Index Page

List and search all organizations in the CKAN portal.

## Overview

The organization index page provides:

- List of all organizations
- Search functionality
- Sorting options
- Pagination

/// admonition | Screenshots

/// tab | Organization list
![list](../screenshots/organization-index.jpeg)
///

/// tab | Search empty
![search empty](../screenshots/organization-index-search-empty.jpeg)
///

/// tab | With add button
![with add](../screenshots/organization-index-with-add-button.jpeg)
///

///

## URL Pattern

```
GET /organization
GET /organization?q={query}
GET /organization?sort={field}
```

**Examples:**
```
<<vars.site_url>>/organization
<<vars.site_url>>/organization?q=environmental
<<vars.site_url>>/organization?sort=title asc
```

## Purpose

The index page allows users to:

- Browse all organizations
- Search for specific organizations
- Discover dataset owners

## Actions Available

| Action              | Description              |
|---------------------|--------------------------|
| Search              | Find organizations       |
| Sort                | Change order             |
| View organization   | Navigate to org          |
| Create organization | Add new org              |

## Related Pages

- [Organization Read](read.md) - View individual organization
- [Organization Create](new.md) - Create new organization
- [Dataset Search](../dataset/search.md) - Search datasets by organization
