# Read

View group details and datasets.

## Overview

Group read page displays:

- Group information
- Group datasets
- Member information
- Group statistics

/// admonition | Screenshots

![main](../screenshots/group-read.jpeg)

///

## URL Pattern

```
GET /group/{id}
GET /group/{name}
```

**Examples:**
```
<<vars.site_url>>/group/environmental-data
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
