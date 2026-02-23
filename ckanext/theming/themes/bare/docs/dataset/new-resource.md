# New Resource Page

Add a new resource to a dataset.

## Overview

The new resource page provides:
- File upload functionality
- URL linking option
- Resource metadata form
- File preview

## URL Pattern

```
GET /dataset/{id}/resource/new
POST /dataset/{id}/resource/new
```

**Examples:**
```
<<vars.site_url>>/dataset/annual-report/resource/new
<<vars.site_url>>/dataset/5f7f7d1e/resource/new
```

## Purpose

Allows users to:
- Upload data files
- Link to external resources
- Add API endpoints
- Describe resource content

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| Upload file | Select file to upload | File input |
| Link to URL | Provide external URL | URL input |
| Enter metadata | Describe resource | Form fields |
| Preview | View file preview | Preview area |
| Save | Add resource | Submit button |

## Templates

**Files:**
- `templates/package/new_resource.html` - Main form
- `templates/package/new_resource_not_draft.html` - For published datasets
- `templates/package/snippets/resource_form.html` - Resource form snippet

### Resource Types

1. **File Upload** - Direct file upload to CKAN
2. **Remote URL** - Link to external file
3. **API Endpoint** - API access URL

### Form Fields

- Name/Title
- Description
- Format (auto-detected for uploads)
- URL (for remote resources)
- License
- Additional metadata

## Screenshot Placeholder

![New Resource](../screenshots/dataset-new-resource.png)
*Placeholder: Resource creation form with upload*

## Related Pages

- [Dataset Resources](resources.md) - Manage resources
- [Resource Edit](../resource/edit.md) - Edit resource
- [Dataset Edit](edit.md) - Edit dataset
