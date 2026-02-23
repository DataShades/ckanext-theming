# Dataset Search Page

The main search and browse interface for discovering datasets in the CKAN portal.

## Overview

The dataset search page provides:
- Full-text search across datasets
- Faceted filtering (organization, tags, format, etc.)
- Sorting options
- Pagination
- Search result statistics

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

| Action | Description | Element |
|--------|-------------|---------|
| Search datasets | Full-text search | Search input |
| Filter by facet | Narrow results | Facet sidebar |
| Sort results | Change order | Sort dropdown |
| Clear filters | Reset search | Clear link |
| View dataset | Navigate to dataset | Result card |
| Create dataset | Add new dataset | Action button (if authorized) |
| Pagination | Navigate pages | Page controls |

## Template

**File:** `templates/package/search.html`

### Template Structure

```jinja
{% extends "package/_base.html" %}
{%- set _layout = _layout|default("sidebar") -%}

{%- block primary_content_inner %}
    {{ ui.search_form(...) }}
    {{ ui.search_results_header(...) }}
    {{ ui.util.map(ui.package, datasets) }}
    {{ ui.pagination(...) }}
{%- endblock -%}

{%- block secondary_content %}
    {{ ui.facet_section(...) }}
{%- endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `q` | Search query string |
| `datasets` | List of dataset results |
| `search_facets` | Available facets |
| `facet_titles` | Facet display names |
| `fields` | Active filter fields |
| `fields_grouped` | Grouped filter values |
| `sort_by` | Current sort order |
| `page` | Pagination object |
| `dataset_type` | Type identifier (e.g., 'dataset') |

### HTMX Support

The search page supports HTMX for dynamic updates:
```jinja
{%- include "package/snippets/search_htmx.html" -%}
```

This enables:
- Live search results
- Dynamic facet updates
- No page refresh on filter changes

## Screenshot Placeholder

![Dataset Search](../screenshots/dataset-search.png)

**What to show:**
- Full page with search bar at top
- Faceted sidebar showing filters
- Search results as cards/list
- Sort options and result count
- Active filter indicators
- Pagination controls

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

### Result Display

Customize how results appear:
```jinja
{% block search_result %}
    {% for dataset in datasets %}
        {{ ui.package(dataset) }}
    {% endfor %}
{% endblock %}
```

### Sorting Options

Available sort options:
- Relevance (default)
- Name Ascending
- Name Descending
- Most Recent
- Least Recent
- Most Viewed
- Least Viewed

### Styling

Key areas to style:
```scss
.dataset-search {
    .search-form {
        // Search bar styling
    }

    .facets {
        // Sidebar facets
    }

    .dataset-card {
        // Result cards
    }

    .pagination {
        // Page controls
    }
}
```

## Related Pages

- [Dataset Read](read.md) - View individual dataset
- [Dataset Create](new.md) - Create new dataset
- [Organization Read](../organization/read.md) - Filter by organization
- [Group Read](../group/read.md) - Filter by group

## Best Practices

1. **Prominent Search**: Make search input highly visible
2. **Clear Facets**: Show active filters prominently
3. **Result Count**: Display total results clearly
4. **Responsive**: Ensure mobile-friendly layout
5. **Performance**: Optimize for fast search results
6. **Accessibility**: Ensure keyboard navigation works

## Extension Hooks

Extensions can modify search by:
- Adding custom facets
- Modifying search query logic
- Adding result filters
- Customizing sort options
- Adding search widgets
