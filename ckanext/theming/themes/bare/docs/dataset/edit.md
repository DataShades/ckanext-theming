# Edit

The form for editing existing datasets in CKAN.

## Overview

The dataset edit page provides:

- Pre-populated form with current values
- All metadata fields from create
- Delete option

/// admonition | Screenshots

/// tab | Edit form
![form](../screenshots/dataset-edit-form.jpeg)
///

/// tab | Validation errors
![errors](../screenshots/dataset-edit-errors.jpeg)
///

///

## URL Pattern

```
GET /dataset/edit/{id}
POST /dataset/edit/{id}
```

**Examples:**
```
<<vars.site_url>>/dataset/edit/annual-environmental-report
<<vars.site_url>>/dataset/edit/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The edit page allows authorized users to:

- Modify dataset metadata
- Change categorization
- Delete dataset

## Actions Available

| Action           | Description            |
|------------------|------------------------|
| Edit metadata    | Modify dataset fields  |
| Delete dataset   | Remove dataset         |
| Save changes     | Update dataset         |

## Related Pages

- [Dataset Create](new.md) - Create new dataset
- [Dataset Read](read.md) - View dataset
