# Resource Section

This section covers pages for managing dataset resources.

## Overview

Resource pages handle:

- Resource viewing and download
- Resource metadata editing
- Data visualization
- Data dictionary management
- Resource previews

## Pages in This Section

| Page                        | Description     |
|-----------------------------|-----------------|
| [Read](read.md)             | View resource   |
| [Edit](edit.md)             | Edit resource   |
| [History](history.md)       | Version history |
| [Views](views.md)           | Manage views    |
| [Dictionary](dictionary.md) | Data dictionary |
| [Data](data.md)             | Resource data   |

## URL Structure

```
/dataset/{id}/resource/{rid}              # Read resource
/dataset/{id}/resource/{rid}/edit         # Edit resource
/dataset/{id}/resource/{rid}/history      # Resource history
/dataset/{id}/resource/{rid}/views        # Manage views
/dataset/{id}/resource/{rid}/views/new    # New view
/dataset/{id}/resource/{rid}/dictionary   # Data dictionary
/dataset/{id}/resource/{rid}/data         # Resource data
```

## Resource Types

CKAN supports various resource types:

- File uploads (CSV, Excel, PDF, etc.)
- URL links to external data
- API endpoints
- Database tables (via DataStore)

## Customization Tips

1. **Read Page**: Enhance preview and download options
2. **Edit Page**: Add custom metadata fields
3. **Views**: Add custom visualization types
4. **Dictionary**: Enhance field management
5. **Styling**: Apply consistent theming

## Screenshots

<!-- TODO: Add screenshots of your themed resource pages -->

### Resource Read
![Resource Read](../screenshots/resource-read.png)

### Resource Edit
![Resource Edit](../screenshots/resource-edit.png)

### Resource Views
![Resource Views](../screenshots/resource-views.png)

### Data Dictionary
![Data Dictionary](../screenshots/resource-dictionary.png)

## Related Sections

- [Dataset](../dataset/index.md) - Parent dataset
- [Admin](../admin/index.md) - System administration
