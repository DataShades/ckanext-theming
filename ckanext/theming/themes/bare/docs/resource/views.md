# Resource Edit Page

Edit resource metadata.

## Overview

Resource edit page provides:

- Pre-populated metadata form
- File replacement option
- URL update
- Metadata editing

/// admonition | Screenshots
![edit](../screenshots/resource-edit.jpeg)
///

## URL Pattern

```
GET /dataset/{id}/resource/{resource_id}/edit
POST /dataset/{id}/resource/{resource_id}/edit
```

## Purpose

Allows users to:

- Update resource name
- Modify description
- Change format
- Update URL
- Replace file

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| Edit metadata | Modify resource fields   |
| Replace file  | Upload new file          |
| Update URL    | Change resource URL      |

## Related Pages

- [Resource Read](read.md) - View resource
- [New Resource](../dataset/new-resource.md) - Create resource
