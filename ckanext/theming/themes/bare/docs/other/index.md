# Other Pages Section

This section covers additional pages and utilities in the CKAN portal.

## Overview

Other pages include:

- Error pages
- Statistics
- Feeds
- HTMX search components
- Development tools

## Pages in This Section

| Page                          | Description          |
|-------------------------------|----------------------|
| [Error Pages](error-pages.md) | 404, 403, 500 errors |
| [Stats](stats.md)             | Site statistics      |
| [Feeds](feeds.md)             | RSS/Atom feeds       |
| [HTMX Search](htmx-search.md) | Dynamic search       |
| [Primer](primer.md)           | Style guide          |

## Error Pages

CKAN handles errors with custom templates:

### 404 Not Found
- Resource doesn't exist
- Invalid URL

### 403 Forbidden
- Access denied
- Authentication required

### 500 Server Error
- Internal server error
- Application crash

## URL Structure

```
/error/{code}              # Error pages
/stats                     # Statistics
/feed                      # RSS/Atom feeds
/development/primer        # Style guide
```

## Customization Tips

1. **Error Pages**: Customize branding and messaging
2. **Stats**: Add custom statistics
3. **Feeds**: Customize feed content
4. **Primer**: Document theme components

## Screenshots

<!-- TODO: Add screenshots of your themed pages -->

### 404 Error
![404 Error](../screenshots/error-404.png)

### Statistics
![Stats](../screenshots/stats.png)

### Style Primer
![Primer](../screenshots/primer.png)

## Related Sections

- [Home](../home/index.md) - Main pages
- [Admin](../admin/index.md) - Administration
- [Dataset](../dataset/index.md) - Content
