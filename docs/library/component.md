# Components

Component macros provide specialized components for representing CKAN-specific entities like groups, organizations, packages, and resources. These components are designed for the CKAN platform and handle the display of complex data objects with appropriate formatting and linking.

## `group_item`

Renders a visual representation of a CKAN group with associated metadata, image, and navigation. Provides a consistent way to display group information throughout the application with appropriate linking and visual representation.

**Use Cases:**
- Group listings
- Category displays
- Organizational structures
- Topic collections
- Community displays
- Project groupings

**Usage Context:**
Use when displaying a list of groups in CKAN, such as on category pages, browse pages, or when showing related groups.

**Example:**
```
{{ ui.group_item({
  "title": "Research Groups",
  "name": "research",
  "description": "Groups focused on academic research",
  "image_display_url": "/images/research.jpg",
  "num_followers": 24,
  "packages": 15
}) }}
```

**Recommendations:**
- Displays relevant metadata like follower count and package count
- Different themes customize group item appearance (Bootstrap: card layout, Tailwind: flex items, Bulma: media object)
- Includes appropriate images when available
- Provides proper linking to group pages
- Maintains consistent styling with other CKAN entity displays

## `organization_item`

Renders a visual representation of a CKAN organization with associated metadata, image, and navigation. Organizations are specialized groups in CKAN that typically represent institutions or companies managing datasets.

**Use Cases:**
- Organization listings
- Publisher displays
- Institutional showcases
- Organizational hierarchies
- Dataset publisher listings
- Authority displays

**Usage Context:**
Use when displaying a list of organizations in CKAN, such as on publisher browse pages or when showing organizational structure.

**Example:**
```
{{ ui.organization_item({
  "title": "City Government",
  "name": "city-gov",
  "description": "Official datasets from the city government",
  "image_display_url": "/images/government-logo.png",
  "num_followers": 120,
  "packages": 45
}) }}
```

**Recommendations:**
- Treat similar to group items with organization-specific styling
- Different themes may differentiate organization items visually (Bootstrap: with organization badges, Tailwind: with authority indicators, Bulma: with organization-specific styles)
- Emphasizes trust and authority aspects
- Includes appropriate branding elements
- Provides clear navigation to organization page

## `package_item`

Renders a visual representation of a CKAN package (dataset) with associated metadata and navigation. Packages represent datasets in CKAN and are one of the core entity types displayed to users.

**Use Cases:**
- Dataset listings
- Search results
- Browse dataset pages
- Featured datasets
- Recently updated datasets
- Related package displays

**Usage Context:**
Use when displaying a list of datasets in CKAN, such as on search results pages, dataset browse pages, or when showing related datasets.

**Example:**
```
{{ ui.package_item({
  "title": "Population Statistics 2024",
  "name": "population-stats-2024",
  "notes": "Annual population statistics broken down by demographics...",
  "resources": [{"name": "CSV File", "format": "CSV"}],
  "organization": {
    "title": "National Statistics Office",
    "name": "stats-office"
  },
  "tags": [{"display_name": "demographics"}, {"display_name": "population"}],
  "metadata_modified": "2024-01-01T10:00:00Z"
}) }}
```

**Recommendations:**
- Displays key metadata including title, description, organization, and tags
- Different themes provide various dataset item styles (Bootstrap: resource cards, Tailwind: dataset previews, Bulma: package listings)
- Includes organization information for provenance
- Shows resource count or formats
- Provides clear access to dataset details
- Optimized for search result displays

## `resource_item`

Renders a visual representation of a CKAN resource which represents downloadable files or access points within packages. Resources are the actual data files or services within a dataset.

**Use Cases:**
- Dataset resource lists
- Download displays
- Resource browsing
- File type listings
- API endpoint displays
- Resource access points

**Usage Context:**
Use when displaying resources within a package, such as on dataset detail pages or when showing download options.

**Example:**
```
{{ ui.resource_item({
  "name": "Data file (CSV)",
  "description": "Complete dataset in CSV format",
  "format": "CSV",
  "mimetype": "text/csv",
  "size": 2048576,
  "url": "/datasets/population-stats-2024.csv",
  "created": "2024-01-01T10:00:00Z"
}) }}
```

**Recommendations:**
- Displays format, size, and description information
- Different themes style resources appropriately (Bootstrap: list-group items, Tailwind: resource cards, Bulma: panel-blocks)
- Shows file size and format for user expectations
- Provides direct access to the resource URL
- May include format-specific icons or styling
- Optimized for download action prominence
