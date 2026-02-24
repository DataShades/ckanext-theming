# Resource Data Page

View and manage resource data processed by Datapusher.

## Overview

Resource data page provides:

- Data preview
- DataStore status
- Push to DataStore option
- Data dictionary access

/// admonition | Screenshots

/// tab | Data view
![data](../screenshots/resource-data.jpeg)
///

/// tab | Push button
![push](../screenshots/resource-data-push-button.jpeg)
///

///

## URL Pattern

```
GET /dataset/{id}/resource/{resource_id}/data
```

## Purpose

Allows users to:

- Preview tabular data
- Check DataStore status
- Push data to DataStore
- Access data dictionary

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| Preview data  | View data table          |
| Push to DS    | Upload to DataStore      |
| View dictionary | See field definitions  |

## Related Pages

- [Resource Read](read.md) - View resource
- [Data Dictionary](dictionary.md) - Field definitions
- [Resource Views](views.md) - Data visualizations
