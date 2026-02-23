# Theme Documentation

Welcome to the Theme Documentation. This documentation provides a comprehensive
guide to all pages in the CKAN portal, designed to help users understand their
CKAN instance.

## Overview

This documentation covers all the pages available in a standard CKAN
installation, organized by functional sections. Each page documentation
includes:

- **Purpose**: Description of what the page is used for
- **URL Pattern**: Example URLs showing how to access the page
- **Actions**: Available user actions on the page

| Section                       | Description                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------|
| [Home](home/)                 | The public-facing pages accessible to all visitors.                                 |
| [Admin](admin/)               | Administrative pages for system administrators.                                     |
| [User](user/)                 | User account and authentication pages.                                              |
| [Group](group/)               | Pages for group management (similar to organizations but for thematic collections). |
| [Organization](organization/) | Pages for organization management.                                                  |
| [Dataset](dataset/)           | Pages for managing and viewing datasets (packages).                                 |
| [Dashboard](dashboard/)       | Personal user dashboard.                                                            |
| [Resource](resource/)         | Pages for managing dataset resources.                                               |
| [Other](other/)               | Additional pages and utilities.                                                     |


## Template Structure

The theme uses the following template structure:

```
templates/
├── _base.html           # Base template with HTML structure
├── _page.html           # Page wrapper template
├── _layout.html         # Layout selection template
├── _header.html         # Header component
├── _footer.html         # Footer component
├── layout/              # Layout templates
│   ├── default.html
│   ├── fullwidth.html
│   ├── left_sidebar.html
│   ├── right_sidebar.html
│   └── ...
├── macros/              # UI macros
│   └── ui.html
├── package/             # Dataset templates
├── organization/        # Organization templates
├── group/               # Group templates
├── user/                # User templates
├── admin/               # Admin templates
└── ...
```


---

**Note**: This documentation is designed to be copied and adapted when creating new themes based on the bare theme. Customize the content to reflect your specific implementation.
