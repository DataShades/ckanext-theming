# Dataset Read Page

The main page for viewing dataset details, metadata, and resources.

## Overview

The dataset read page displays:

- Dataset title and description
- Metadata (author, license, tags, etc.)
- Resource list
- Social sharing options
- Follow/unfollow functionality
- Related information

/// admonition | Screenshots

/// tab | Dataset details page
![normal](../screenshots/dataset-read-normal.jpeg)
///

/// tab | Resources
![normal](../screenshots/dataset-read-resources.jpeg)
///

/// tab | Additional info
![normal](../screenshots/dataset-read-additional-info.jpeg)
///

/// tab | Manage button
![normal](../screenshots/dataset-read-manage-button.jpeg)
///

/// tab | Follow button
![normal](../screenshots/dataset-read-follow-button.jpeg)
///

/// tab | Unfollow button
![normal](../screenshots/dataset-read-unfollow-button.jpeg)
///

///

## URL Pattern

```
GET /dataset/{id}
GET /dataset/{name}
```

**Examples:**
```
<<vars.site_url>>/dataset/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
<<vars.site_url>>/dataset/annual-environmental-report-2024
```

## Purpose

The read page is the primary view for dataset information. It should:

- Present all dataset metadata clearly
- Provide access to resources (downloads, APIs)
- Show related information and navigation
- Enable user interactions (follow, share)

## Actions Available

| Action            | Description                    |
|-------------------|--------------------------------|
| View resource     | Access resource data           |
| Download resource | Download resource file         |
| Edit dataset      | Modify dataset (if authorized) |
| Follow dataset    | Subscribe to updates           |
| View activity     | See activity stream            |
| Share dataset     | Share via social media         |


## Related Pages

- [Dataset Search](search.md) - Browse/search datasets
- [Dataset Edit](edit.md) - Modify dataset
- [Resource Read](../resource/read.md) - View individual resource
- [Dataset History](history.md) - Version history
