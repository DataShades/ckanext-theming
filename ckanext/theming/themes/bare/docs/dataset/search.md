# Dataset Search Page

The main search and browse interface for discovering datasets in the CKAN portal.

## Overview


The dataset search page provides:

- Full-text search across datasets
- Faceted filtering (organization, tags, format, etc.)
- Sorting options
- Pagination
- Search result statistics

/// admonition | Screenshots

///tab | Default search page
![normal](../screenshots/dataset-search-normal.jpeg)
///

/// tab | Search page with query
![facet applied](../screenshots/dataset-search-query-applied.jpeg)
///


/// tab | Search page with applied filters
![facet applied](../screenshots/dataset-search-facet-applied.jpeg)
///

/// tab | Add-dataset button
![facet applied](../screenshots/dataset-search-add-button.jpeg)
///

///

## URL Pattern

```
GET /dataset
GET /dataset?q={query}
GET /dataset?organization={org}&tags={tag}&res_format={format}
```

**Examples:**
```
<<vars.site_url>>/dataset
<<vars.site_url>>/dataset?q=environment
<<vars.site_url>>/dataset?organization=epa&tags=climate
```

## Purpose

The search page is the primary way users discover datasets. It should:

- Provide powerful search capabilities
- Offer intuitive filtering options
- Display relevant results clearly
- Guide users to refine their search

## Actions Available

| Action          | Description         |
|-----------------|---------------------|
| Search datasets | Full-text search    |
| Filter by facet | Narrow results      |
| Sort results    | Change order        |
| Clear filters   | Reset search        |
| View dataset    | Navigate to dataset |
| Create dataset  | Add new dataset     |
| Pagination      | Navigate pages      |



## Customization Notes

### Search Configuration

Configure search behavior in CKAN config:
```ini
ckan.datasets_per_page = 20
ckan.facets = organization groups tags res_format license_id
ckan.search.show_all_types = False
```

### Facet Customization

Modify which facets appear:
```python
# In plugin or config
ckan.facets = custom_facet1 custom_facet2 organization tags
```

## Related Pages

- [Dataset Read](read.md) - View individual dataset
- [Dataset Create](new.md) - Create new dataset
- [Organization Read](../organization/read.md) - Filter by organization
- [Group Read](../group/read.md) - Filter by group
