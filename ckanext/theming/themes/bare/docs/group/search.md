# Group Index Page

List and search all group in the CKAN portal.

## Overview

The group index page provides:

- List of all group
- Search functionality
- Sorting options
- Pagination

/// admonition | Screenshots

/// tab | Group list
![list](../screenshots/group-index.jpeg)
///

/// tab | Search empty
![search empty](../screenshots/group-index-search-empty.jpeg)
///

/// tab | With add button
![with add](../screenshots/group-index-with-add-button.jpeg)
///

///

## URL Pattern

```
GET /group
GET /group?q={query}
GET /group?sort={field}
```

**Examples:**
```
<<vars.site_url>>/group
<<vars.site_url>>/group?q=environmental
<<vars.site_url>>/group?sort=title asc
```

## Purpose

The index page allows users to:

- Browse all group
- Search for specific group
- Discover dataset owners

## Actions Available

| Action       | Description       |
|--------------|-------------------|
| Search       | Find group        |
| Sort         | Change order      |
| View group   | Navigate to group |
| Create group | Add new group     |

## Related Pages

- [Group Read](read.md) - View individual group
- [Group Create](new.md) - Create new group
- [Dataset Search](../dataset/search.md) - Search datasets by group
