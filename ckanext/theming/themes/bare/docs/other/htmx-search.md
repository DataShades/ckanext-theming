# RSS/Atom Feeds

Syndication feeds for portal content.

## Overview

CKAN provides feeds for:

- Recently added datasets
- Organization activity
- Group activity
- User activity
- Custom searches

## URL Patterns

```
/feed/atom              # Atom feed
/feed/rss               # RSS feed
/dataset/feed           # Dataset feed
/organization/{id}/feed # Organization feed
```

## Purpose

Feeds allow users to:

- Subscribe to updates
- Monitor new content
- Track changes
- Integrate with readers

## Feed Types

### Atom Feed

Standard Atom 1.0 format for dataset updates.

### RSS Feed

RSS 2.0 format for broader compatibility.

## Related Pages

- [Dataset Search](../dataset/search.md) - Dataset listings
- [Organization Read](../organization/read.md) - Organization content
