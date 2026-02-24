# Groups

View and manage the groups associated with a dataset.

## Overview

The groups page displays:

- Groups the dataset belongs to
- Group descriptions and images
- Add/remove group associations

/// admonition | Screenshots

/// tab | With groups
![with groups](../screenshots/dataset-groups.jpeg)
///

/// tab | Empty state
![empty](../screenshots/dataset-groups-empty.jpeg)
///

///

## URL Pattern

```
GET /dataset/groups/{id}
```

**Examples:**
```
<<vars.site_url>>/dataset/groups/annual-environmental-report
```

## Purpose

The groups page allows users to:

- See which groups contain this dataset
- Add dataset to groups (if authorized)

## Actions Available

| Action            | Description          |
|-------------------|----------------------|
| View groups       | See group list       |
| Add to group      | Associate with group |
| Remove from group | Disassociate         |
| View group        | Navigate to group    |

## Related Pages

- [Dataset Read](read.md) - Main dataset view
- [Group Index](../group/index.md) - Browse all groups
- [Group Read](../group/read.md) - View individual group
