# Search Components

Search components provide all the elements needed for search functionality, including search forms, filters, results display, and related controls.

## Overview

Search components enable users to find content within the CKAN instance. They provide the interface for searching, filtering, and displaying search results in a consistent manner. These components work together to create comprehensive search experiences that help users discover relevant content efficiently.

## Search Active Filters Component

The `search_active_filters` component displays the currently active filters in search interfaces, showing users which filters are currently applied to their search results. This component is crucial for search usability, allowing users to understand what filters are affecting their results and providing easy ways to remove or modify active filters.

Active filters are typically displayed as removable tags or badges that show the filter type and value. Users can click these elements to remove specific filters, providing immediate feedback and control over their search criteria. The component ensures that users always know which filters are active and can easily modify their search parameters.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic search active filters -->
{{ ui.search_active_filters(active_filters={"organization": ["gov"], "format": ["csv"]}, facet_titles={"organization": "Organization", "format": "Format"}) }}

<!-- Search active filters with attributes -->
{{ ui.search_active_filters(active_filters={"license": ["cc-by"]}, facet_titles={"license": "License"}, attrs={"class": "active-filters"}) }}
```
///

## Search Advanced Controls Component

The `search_advanced_controls` component provides advanced search controls that offer additional search functionality beyond basic keyword searching. These controls typically include options for field-specific searching, date ranges, complex query building, or other sophisticated search capabilities.

Advanced controls are usually hidden by default and revealed when users need more precise search capabilities. The component handles the interface for these advanced features while maintaining accessibility and usability. It ensures that advanced search functionality is available to users who need it without cluttering the interface for users who prefer simple searches.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic search advanced controls -->
{{ ui.search_advanced_controls() }}

<!-- Search advanced controls with attributes -->
{{ ui.search_advanced_controls(attrs={"class": "advanced-search-controls"}) }}
```
///

## Search Form Component

The `search_form` component creates complete search forms that organize all search-related elements into a cohesive unit. This component provides the overall structure for search interfaces and handles form submission and validation for search operations.

Search form components work with several related elements including `search_input`, `search_submit_button`, and various filter controls to create complete search experiences. The component ensures proper form structure, accessibility, and functionality while maintaining consistency across different search contexts throughout the application.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic search form -->
{{ ui.search_form(query="search term", item_count=25, first_item_position=1, last_item_position=10) }}

<!-- Search form with sorting -->
{{ ui.search_form(query="data", sorting="title_string asc", sorting_options=[{"text": "Name A-Z", "value": "title_string asc"}]) }}
```
///

/// admonition | Relationship
    type: info

The `search_form` component works with `search_input`, `search_submit_button`, and various filter components to create complete search experiences. The form provides the overall container structure for all search elements.
///

## Search Input Component

The `search_input` component creates search input fields where users enter their search queries. This component handles the primary text input for search operations and often includes features like search suggestions, history, or instant search capabilities.

Search input components are fundamental to the search experience, providing the primary interface for users to enter their search criteria. The component ensures proper accessibility, styling, and functionality while supporting features like autocomplete or search history that enhance the user experience. It handles various input types and validation requirements specific to search functionality.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic search input -->
{{ ui.search_input(name="q", value="search term", placeholder="Search...") }}

<!-- Search input with custom label -->
{{ ui.search_input(name="query", label="Find datasets", placeholder="Enter search terms") }}

<!-- Search input with attributes -->
{{ ui.search_input(name="search", placeholder="Search datasets...", attrs={"class": "search-input"}) }}
```
///

/// admonition | Relationship
    type: info

The `search_input` component works within `search_form` containers alongside `search_submit_button` and other search controls to create complete search interfaces.
///

## Search Pagination Info Component

The `search_pagination_info` component displays information about search results pagination, showing users details about the current page, total results, and their position within the result set. This information is crucial for users to understand the scope of their search results and their current position within those results.

Pagination info components typically display text like "Showing 1-10 of 127 results" or similar information that helps users understand the extent of their search results. The component ensures this information is clearly visible and properly formatted, helping users navigate through large result sets effectively.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic search pagination info -->
{{ ui.search_pagination_info(total=127, first=1, last=10) }}

<!-- Search pagination info with custom template -->
{{ ui.search_pagination_info(total=50, first=21, last=30, template=_("Results {first} - {last} out of {total}")) }}
```
///

## Search Results Header Component

The `search_results_header` component creates headers for search results displays, providing context and organization for the search results. This component typically includes information about the search query, result counts, and controls for managing or refining the search results.

Search results headers are important for orienting users and providing context about their search. They often include the search query that was performed, the number of results found, and controls for sorting or refining the results. The component ensures this information is clearly presented and easily accessible to users.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic search results header -->
{{ ui.search_results_header(item_count=25, first_item_position=1, last_item_position=10) }}

<!-- Search results header with query error -->
{{ ui.search_results_header(item_count=0, first_item_position=0, last_item_position=0, query_error="Invalid search query") }}
```
///

## Search Sort Control Component

The `search_sort_control` component provides controls for sorting search results in different ways, allowing users to organize their results by relevance, date, name, or other criteria. Sorting controls are essential for helping users find the most relevant results quickly.

Sort control components typically include dropdown menus or other interface elements that allow users to select different sorting options. The component handles the interface for these controls while ensuring proper accessibility and clear indication of the current sort order. It provides users with the ability to reorganize their results based on their specific needs.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic search sort control -->
{{ ui.search_sort_control(selected="relevance", options=[{"text": "Relevance", "value": "relevance"}, {"text": "Date", "value": "date"}]) }}

<!-- Search sort control with attributes -->
{{ ui.search_sort_control(name="sort", selected="title", options=[{"text": "Title A-Z", "value": "title_asc"}, {"text": "Title Z-A", "value": "title_desc"}], attrs={"class": "sort-control"}) }}
```
///

## Search Submit Button Component

The `search_submit_button` component creates search submission buttons that trigger search operations when clicked. This component provides the primary action for initiating searches and must be clearly identifiable and appropriately styled to encourage user action.

Search submit buttons handle the form submission functionality for search operations and often include visual elements like search icons to clearly indicate their purpose. The component ensures proper accessibility and provides clear feedback about the search submission action. It works within `search_form` containers to provide the primary search initiation mechanism.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic search submit button -->
{{ ui.search_submit_button("Search") }}

<!-- Search submit with icon -->
{{ ui.search_submit_button(ui.icon("search") ~ " Search") }}

<!-- Search submit with attributes -->
{{ ui.search_submit_button("Find", attrs={"class": "btn btn-primary"}) }}
```
///

/// admonition | Relationship
    type: info

The `search_submit_button` component works within `search_form` containers alongside `search_input` and other search controls to create complete search interfaces. While the input provides the query, the submit button triggers the search operation.
///
