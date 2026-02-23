# Data Dictionary

Define and manage field metadata for tabular resources.

## Overview

Data dictionary page provides:
- Field definitions
- Type information
- Label editing
- Description management

## URL Pattern

```
GET /dataset/{id}/resource/{resource_id}/dictionary
POST /dataset/{id}/resource/{resource_id}/dictionary
```

## Purpose

Allows users to:
- Define field labels
- Add field descriptions
- Set field types
- Document data structure

## Template

**File:** `templates/datastore/dictionary.html`

### Field Properties

- Label (human-readable name)
- Description (field documentation)
- Type (string, number, date, etc.)
- Unit of measurement
- Required/optional status

## Screenshot Placeholder

![Data Dictionary](../screenshots/resource-dictionary.png)
*Placeholder: Data dictionary editor*

## Related Pages

- [Resource Data](data.md) - Resource data
- [Resource Views](views.md) - Data visualizations
- [Resource Read](read.md) - View resource
