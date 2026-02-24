# Resource

Add a new resource to a dataset.

## Overview

The new resource page provides:

- File upload functionality
- URL linking option
- Resource metadata form

/// admonition | Screenshots
![link](../screenshots/resource-new.jpeg)
///

## URL Pattern

```
GET /dataset/{id}/resource/new
POST /dataset/{id}/resource/new
```

**Examples:**
```
<<vars.site_url>>/dataset/annual-report/resource/new
```

## Purpose

Allows users to:

- Upload data files
- Link to external resources
- Add API endpoints
- Describe resource content

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| Upload file   | Select file to upload    |
| Link to URL   | Provide external URL     |
| Enter metadata| Describe resource        |
| Save          | Add resource             |

## Resource Types

| Type        | Description              |
|-------------|--------------------------|
| File Upload | Direct file upload       |
| Remote URL  | Link to external file    |
| API         | API endpoint URL         |

## Related Pages

- [Dataset Resources](../dataset/resources.md) - Manage resources
- [Resource Edit](edit.md) - Edit resource
- [Resource Read](read.md) - View resource
