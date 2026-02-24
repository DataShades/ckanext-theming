# About

The about page provides information about the CKAN instance and the organization behind it.

## Overview

The about page typically displays:

- Portal's description
- Contact information
- Links to related resources
- Custom about text from configuration

/// admonition | Screenshots
![normal](../screenshots/home-about.jpeg)
///

## URL Pattern

```
GET /about
```

**Example:**
```
<<vars.site_url>>/about
```

## Purpose

The about page serves to:

- Introduce the organization/portal to visitors
- Provide contact and attribution information
- Explain the purpose and scope of the data portal
- Link to related resources and documentation

## Actions Available

| Action                 | Description           |
|------------------------|-----------------------|
| View organization info | Read about the portal |
| Navigate back          | Return to home page   |

## Content Sources

The about page content can come from:

1. **Configuration** (`ckan.site_about`):
   ```ini
   ckan.site_about = <p>Your custom about text here</p>
   ```

2. **Template Override**:
    - Directly edit `templates/home/about.html`
    - Use Jinja2 includes for modular content

3. **Translation Files**:
    - Override translatable strings
    - Provide localized content


## Related Pages

- [Home Page](home.md) - Main landing page
- [Admin Config](../admin/config.md) - Configure site about text
- [Error Pages](../other/error-pages.md) - Error handling
