# Error Pages

Error handling and custom error pages.

## Overview

CKAN displays error pages for:

- 404 Not Found
- 403 Forbidden
- 500 Internal Server Error

/// admonition | Screenshots

/// tab | 404 Not Found
![404](../screenshots/error-404.jpeg)
///

/// tab | 403 Forbidden
![403](../screenshots/error-403.jpeg)
///

///

## URL Patterns

Errors can occur on any URL:

```
/nonexistent-page       # 404
/protected-page         # 403
/crash-endpoint         # 500
```

## Purpose

Error pages:

- Inform users of problems
- Provide navigation options
- Maintain branding consistency

## Actions Available

| Action      | Description              |
|-------------|--------------------------|
| Go home     | Return to homepage       |
| Search      | Search for content       |
| Go back     | Return to previous page  |

## Related Pages

- [Home](../home/home.md) - Return to home
- [Search](../dataset/search.md) - Search for content
