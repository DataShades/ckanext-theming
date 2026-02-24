# Data Dictionary

Define and manage field metadata for tabular resources.

## Overview

Data dictionary page provides:

- Field definitions
- Type information
- Label editing
- Description management

/// admonition | Screenshots

![dictionary](../screenshots/resource-dictionary.jpeg)

///

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

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| Edit fields   | Modify field metadata    |
| Add labels    | Set human-readable names |
| Set types     | Define field types       |

## Related Pages

- [Resource Views](views.md) - Data visualizations
- [Resource Read](read.md) - View resource
