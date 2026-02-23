# Organization About Page

View detailed information about an organization.

## Overview

The about page displays:

- Full organization description
- Contact information
- Organization metadata
- Related links

/// admonition | Screenshots
![about](../screenshots/organization-about.jpeg)
///

## URL Pattern

```
GET /organization/about/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/about/environmental-protection-agency
<<vars.site_url>>/organization/about/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The about page allows users to:

- Learn about the organization
- View contact details
- Understand organization's mission
- Access related resources

## Actions Available

| Action        | Description              |
|---------------|--------------------------|
| View details  | Read org information     |
| Edit org      | Modify details           |
| Contact       | Reach organization       |
| Back to org   | Return to main page      |

## Related Pages

- [Organization Read](read.md) - Main organization page
- [Organization Edit](edit.md) - Edit organization
- [Organization Index](index.md) - List all organizations
