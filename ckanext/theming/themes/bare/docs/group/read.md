
# Group Read Page

View group details and datasets.

## Overview

Group read page displays:

- Group information
- Group datasets
- Member information
- Group statistics

/// admonition | Screenshots

/// tab | Main view
![main](../screenshots/group-read.jpeg)
///

/// tab | Datasets section
![datasets](../screenshots/group-read-datasets.jpeg)
///

/// tab | Sidebar info
![sidebar](../screenshots/group-read-sidebar.jpeg)
///

///

## URL Pattern

```
GET /group/{id}
GET /group/{name}
```

**Examples:**
```
<<vars.site_url>>/group/environmental-data
<<vars.site_url>>/group/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The read page allows users to:

- View group description
- Browse group datasets
- See group members
- Follow group

## Actions Available

| Action          | Description              |
|-----------------|--------------------------|
| View datasets   | Browse group datasets    |
| Search datasets | Filter group datasets    |
| Follow group    | Subscribe to updates     |
| Edit group      | Modify group             |

## Related Pages

- [Group Index](index.md) - Group list
- [Group Edit](edit.md) - Edit group
- [Dataset Search](../dataset/search.md) - Dataset search
