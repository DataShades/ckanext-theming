# Dataset Create Page

The form for creating new datasets in CKAN.

## Overview

The dataset create page provides:

- Basic metadata input
- Organization selection
- Tag input
- License selection

/// admonition | Screenshots

![empty](../screenshots/dataset-new-form.jpeg)

///

## URL Pattern

```
GET /dataset/new
POST /dataset/new
```

**Example:**
```
<<vars.site_url>>/dataset/new
```

## Purpose

The create page allows authorized users to:

- Add new datasets to the portal
- Enter metadata and description
- Categorize with tags and groups

## Actions Available

| Action           | Description            |
|------------------|------------------------|
| Enter metadata   | Fill dataset details   |
| Add tags         | Categorize dataset     |
| Select license   | Choose license         |
| Select organization | Assign ownership    |
| Save dataset     | Create dataset         |

## Related Pages

- [Dataset Edit](edit.md) - Modify existing dataset
- [Dataset Read](read.md) - View created dataset
- [Dataset Search](search.md) - Browse datasets
