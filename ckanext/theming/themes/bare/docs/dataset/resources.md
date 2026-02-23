# Dataset Resources Management Page

Manage the resources associated with a dataset.

## Overview

The resources page provides:

- List of all dataset resources
- Resource ordering (drag & drop)
- Add new resources

/// admonition | Screenshots

/// tab | Resource list
![list](../screenshots/dataset-resources-list.jpeg)
///

/// tab | Reordering resources
![empty](../screenshots/dataset-resources-reorder.jpeg)
///

///

## URL Pattern

```
GET /dataset/resources/{id}
POST /dataset/resources/{id}
```

**Examples:**
```
<<vars.site_url>>/dataset/resources/annual-environmental-report
```

## Purpose

The resources page allows users to:

- View all dataset resources
- Reorder resources
- Add new resources

## Actions Available

| Action           | Description              |
|------------------|--------------------------|
| View resources   | See resource list        |
| Add resource     | Create new resource      |
| Reorder          | Change resource order    |

## Related Pages

- [Dataset Read](read.md) - View dataset with resources
- [Resource Read](../resource/read.md) - View individual resource
- [Resource Edit](../resource/edit.md) - Edit resource
