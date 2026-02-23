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

Enables dynamic search for:

- Dataset search
- Organization search
- Group search
- User search

## How It Works

HTMX enables:

1. **Live Search**: Results update as you type
2. **Dynamic Facets**: Facet counts update
3. **URL Sync**: Browser history maintained
4. **Loading States**: Visual feedback

## Customization Notes

### HTMX Attributes

Configure HTMX behavior through attributes:

```html
<form hx-get="/dataset/search" 
      hx-target="#search-results" 
      hx-swap="outerHTML">
```

### Loading States

Show loading indicators during search:

```html
<div id="search-results" hx-indicator=".search-loading">
    <!-- Results here -->
</div>
```

### Event Triggers

Configure when search triggers:

```html
<input name="q" 
       hx-trigger="input changed delay:500ms" />
```

## Related Pages

- [Dataset Search](../dataset/search.md) - Main search
- [Organization Index](../organization/index.md) - Organization search
