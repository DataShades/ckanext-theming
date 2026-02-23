# HTMX Search Components

Dynamic search functionality using HTMX.

## Overview

HTMX search provides:
- Live search results
- Dynamic facet updates
- No page refresh
- URL synchronization

## Components

### Search HTMX

**Template:** `templates/package/snippets/search_htmx.html`

Enables dynamic search for:
- Dataset search
- Organization search
- Group search
- User search

## How It Works

```jinja
{%- with dataset_type=dataset_type,
  fields_grouped=fields_grouped,
  search_facets=search_facets,
  facet_titles=facet_titles,
  disable_htmx=false -%}
  {%- include "package/snippets/search_htmx.html" -%}
{%- endwith -%}
```

### Features

1. **Live Search**: Results update as you type
2. **Dynamic Facets**: Facet counts update
3. **URL Sync**: Browser history maintained
4. **Loading States**: Visual feedback

## Customization Notes

### HTMX Attributes

```jinja
{{ ui.form(
    hx={
        'get': h.url_for('dataset.search'),
        'target': '#search-results',
        'swap': 'outerHTML',
        'push-url': 'true'
    }
) }}
```

### Loading States

```jinja
<div id="search-results" hx-indicator=".search-loading">
    <!-- Results here -->
</div>

<div class="search-loading htmx-indicator">
    {{ ui.spinner() }}
</div>
```

### Event Triggers

```jinja
{{ ui.input(
    name='q',
    hx={
        'get': h.url_for('dataset.search'),
        'target': '#search-results',
        'trigger': 'input changed delay:500ms'
    }
) }}
```

## Related Pages

- [Dataset Search](../dataset/search.md) - Main search
- [Organization Index](../organization/index.md) - Organization search
