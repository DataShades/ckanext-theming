# Resource Edit

Edit resource metadata.

## Overview

Resource edit page provides:
- Pre-populated metadata form
- File replacement option
- URL update
- Metadata editing

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

## Template

**File:** `templates/package/resource_edit.html`

## Screenshot Placeholder

![Resource Edit](../screenshots/resource-edit.png)
*Placeholder: Resource edit form*

## Related Pages

- [Resource Read](read.md) - View resource
- [New Resource](../dataset/new-resource.md) - Create resource
