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

Standard Atom 1.0 format:
```xml
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>CKAN Datasets</title>
  <entry>
    <title>Dataset Title</title>
    <link href="..."/>
    <updated>2024-01-01T00:00:00Z</updated>
  </entry>
</feed>
```

### RSS Feed

RSS 2.0 format:
```xml
<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
  <channel>
    <title>CKAN Datasets</title>
    <item>
      <title>Dataset Title</title>
      <link>...</link>
      <pubDate>Mon, 01 Jan 2024</pubDate>
    </item>
  </channel>
</rss>
```

## Customization Notes

### Feed Styling

While feeds are XML, you can customize:
- Feed titles
- Item descriptions
- Content formatting

### Custom Feeds

Create custom feeds for:
- Specific organizations
- Specific groups
- Custom searches
- Themed collections

## Related Pages

- [Dataset Search](../dataset/search.md) - Dataset listings
- [Organization Read](../organization/read.md) - Organization content
