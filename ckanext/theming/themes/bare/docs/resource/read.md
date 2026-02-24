# Read

View resource details and access data.

## Overview

The resource read page displays:

- Resource information
- File download option
- Data preview
- Resource metadata
- Views and visualizations

/// admonition | Screenshots

/// tab | Main view
![main](../screenshots/resource-read.jpeg)
///

/// tab | Info section
![info](../screenshots/resource-read-info.jpeg)
///

/// tab | Edit button
![edit](../screenshots/resource-read-edit-button.jpeg)
///

///

## URL Pattern

```
GET /dataset/{id}/resource/{resource_id}
```

**Examples:**
```
<<vars.site_url>>/dataset/annual-report/resource/abc123
```

## Purpose

Allows users to:

- View resource details
- Download file
- Preview data
- Access visualizations
- View data dictionary

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| Download      | Download file            |
| Preview       | View data preview        |
| Edit          | Modify resource          |
| View views    | See visualizations       |
| Dictionary    | View data dictionary     |

## Resource Information

| Field       | Description              |
|-------------|--------------------------|
| Name        | Resource title           |
| Description | Resource description     |
| Format      | File format (CSV, etc.)  |
| Size        | File size                |
| Created     | Creation date            |
| License     | Resource license         |

## Related Pages

- [Dataset Read](../dataset/read.md) - Parent dataset
- [Resource Edit](edit.md) - Edit resource
- [Resource Views](views.md) - Visualizations
- [Resource New](new.md) - Create resource
