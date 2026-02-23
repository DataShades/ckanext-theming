# Group Create Page

Create a new group.

## Overview

Group create page provides:

- Group information form
- Image upload
- Description field

/// admonition | Screenshots

/// tab | Empty form
![empty](../screenshots/group-new-empty.jpeg)
///

/// tab | Filled form
![filled](../screenshots/group-new-filled.jpeg)
///

///

## URL Pattern

```
GET /group/new
POST /group/new
```

**Example:**
```
<<vars.site_url>>/group/new
```

## Purpose

Allows users to:

- Create thematic collections
- Categorize datasets
- Build communities

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| Enter details | Fill group form          |
| Upload image  | Add group logo           |
| Save          | Create group             |

## Related Pages

- [Group Edit](edit.md) - Edit group
- [Group Index](index.md) - Group list
