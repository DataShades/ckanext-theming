# Search

Search components enable users to find content within the CKAN instance. They
provide the interface for searching, filtering, and displaying search results
in a consistent manner. These components work together to create comprehensive
search experiences that help users discover relevant content efficiently.

## Search Active Filters

The [`search_active_filters`][search-active-filters] component displays the
currently active filters in search interfaces, showing users which filters are
currently applied to their search results. This component is crucial for search
usability, allowing users to understand what filters are affecting their
results and providing easy ways to remove or modify active filters.

Active filters are typically displayed as removable tags or badges that show
the filter type and value. Users can click these elements to remove specific
filters, providing immediate feedback and control over their search
criteria. The component ensures that users always know which filters are active
and can easily modify their search parameters.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic search active filters -->
{{ ui.search_active_filters(
    active_filters={"organization": ["gov"], "format": ["csv"]},
    facet_titles={"organization": "Organization", "format": "Format"}
) }}
```
///

| Parameter        | Type | Default | Description                                       |
|------------------|------|---------|---------------------------------------------------|
| `active_filters` | dict | -       | Dictionary of currently active filters.           |
| `facet_titles`   | dict | -       | Dictionary mapping filter keys to display titles. |
| `facets`         | dict | -       | Available facet information.                      |
| `use_htmx`       | bool | -       | Whether to use HTMX for enhanced functionality.   |

/// details | Theme-Specific Parameters
    type: tip

- `variant` (string): Style variant (e.g., "inline", "stacked")
- `show_clear_all` (bool): Whether to show clear all button
- `limit` (int): Maximum number of filters to display
- `show_counts` (bool): Whether to show filter counts
///

## Search Advanced Controls

The [`search_advanced_controls`][search-advanced-controls] component provides
advanced search controls that offer additional search functionality beyond
basic keyword searching. These controls typically include options for
field-specific searching, date ranges, complex query building, or other
sophisticated search capabilities.

Advanced controls are usually hidden by default and revealed when users need
more precise search capabilities. The component handles the interface for these
advanced features while maintaining accessibility and usability. It ensures
that advanced search functionality is available to users who need it without
cluttering the interface for users who prefer simple searches.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic search advanced controls -->
{{ ui.search_advanced_controls() }}
```
///

## Search Form Box

The [`search_form_box`][search-form-box] component creates the container for
search forms, providing the form element structure and HTMX integration for
enhanced search functionality. This component serves as the foundational
wrapper for search forms, handling form submission and accessibility
requirements.

Search form box components are designed to work with HTMX for enhanced user
experience, automatically adding appropriate HTMX attributes when the
`use_htmx` parameter is enabled. The component ensures proper form structure
and accessibility while maintaining flexibility for different search contexts
and requirements.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic search form box -->
{% call ui.util.call(ui.search_form_box) %}
    {{ ui.search_input(name="q", value="") }}
    {{ ui.search_submit_button("Search") }}
{% endcall %}

<!-- Search form box with HTMX -->
{% call ui.util.call(ui.search_form_box, use_htmx=true) %}
    {{ ui.search_input(name="q", value="") }}
    {{ ui.search_submit_button("Search") }}
{% endcall %}
```
///

| Parameter  | Type   | Default | Description                                        |
|------------|--------|---------|----------------------------------------------------|
| `content`  | string | -       | The content to display within the search form box. |
| `use_htmx` | bool   | -       | Whether to use HTMX for enhanced functionality.    |

/// details | Theme-Specific Parameters
    type: tip

- `method` (string): Form method (e.g., "get", "post")
- `action` (string): Form action URL
///

/// admonition | Relationship
    type: info

The [`search_form_box`][search-form-box] component serves as the container for
[`search_form`][search-form], [`search_input`][search-input], and
[`search_submit_button`][search-submit-button] components. It provides the
overall form structure that wraps these elements together.

///

## Search Form

The [`search_form`][search-form] component creates complete search forms that
organize all search-related elements into a cohesive unit. This component
provides the overall structure for search interfaces and handles form
submission and validation for search operations.

Search form components work with several related elements including
[`search_input`][search-input], [`search_submit_button`][search-submit-button],
and various filter controls to create complete search experiences. The
component ensures proper form structure, accessibility, and functionality while
maintaining consistency across different search contexts throughout the
application.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic search form -->
{{ ui.search_form(
    query="search term",
    item_count=25,
    first_item_position=1,
    last_item_position=10,
    active_filters={},
    facets={},
    facet_titles={},
    use_htmx=False
) }}

<!-- Search form with sorting and filters -->
{{ ui.search_form(
    query="data",
    sorting="title_string asc",
    sorting_options=[{"text": "Name A-Z", "value": "title_string asc"}],
    item_count=15,
    first_item_position=1,
    last_item_position=10,
    active_filters={"organization": ["gov"]},
    facets={"organization": {"items": [{"name": "gov", "display_name": "Government"}]}},
    facet_titles={"organization": "Organization"},
    use_htmx=True
) }}
```
///

| Parameter             | Type   | Default | Description                                     |
|-----------------------|--------|---------|-------------------------------------------------|
| `query`               | string | -       | The current search query.                       |
| `item_count`          | int    | -       | Total number of search results.                 |
| `first_item_position` | int    | -       | Position of the first item in the current page. |
| `last_item_position`  | int    | -       | Position of the last item in the current page.  |
| `sorting`             | string | -       | Current sorting option.                         |
| `sorting_options`     | list   | -       | Available sorting options.                      |
| `query_error`         | string | -       | Error message if query is invalid.              |
| `facets`              | dict   | -       | Available facet filters.                        |
| `facet_titles`        | dict   | -       | Titles for facet filters.                       |
| `active_filters`      | dict   | -       | Currently active filters.                       |
| `use_htmx`            | bool   | -       | Whether to use HTMX for enhanced functionality. |
| `query_name`          | string | "q"     | Name of the query parameter.                    |
| `sorting_name`        | string | "sort"  | Name of the sorting parameter.                  |

/// details | Theme-Specific Parameters
    type: tip

- `variant` (string): Style variant (e.g., "simple", "advanced")
///

/// admonition | Relationship
    type: info

The [`search_form`][search-form] component works with
[`search_input`][search-input], [`search_submit_button`][search-submit-button],
[`search_form_box`][search-form-box], and various filter components to create
complete search experiences. The form provides the overall container structure
for all search elements through its use of the search_form_box component.

///

## Search Input

The [`search_input`][search-input] component creates search input fields where
users enter their search queries. This component handles the primary text input
for search operations and often includes features like search suggestions,
history, or instant search capabilities.

Search input components are fundamental to the search experience, providing the
primary interface for users to enter their search criteria. The component
ensures proper accessibility, styling, and functionality while supporting
features like autocomplete or search history that enhance the user
experience. It handles various input types and validation requirements specific
to search functionality.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic search input -->
{{ ui.search_input(name="q", value="search term", placeholder="Search...") }}

<!-- Search input with custom label -->
{{ ui.search_input(name="query", label="Find datasets", placeholder="Enter search terms") }}
```
///

| Parameter     | Type   | Default     | Description                                |
|---------------|--------|-------------|--------------------------------------------|
| `name`        | string | "q"         | Name attribute for the search input field. |
| `value`       | string | -           | Current value of the search input.         |
| `placeholder` | string | "Search..." | Placeholder text for the search input.     |
| `label`       | string | -           | Label text for the search input.           |

/// details | Theme-Specific Parameters
    type: tip

- `size` (string): Size of the input (e.g., "sm", "lg")
- `variant` (string): Style variant (e.g., "filled", "outlined")
- `icon` (string): Icon to display in the input
- `clearable` (bool): Whether to show clear button
- `search_button` (bool): Whether to include search button inside input
///

/// admonition | Relationship
    type: info

The [`search_input`][search-input] component works within
[`search_form`][search-form] containers alongside
[`search_submit_button`][search-submit-button] and other search controls to
create complete search interfaces.

///

## Search Pagination Info

The [`search_pagination_info`][search-pagination-info] component displays
information about search results pagination, showing users details about the
current page, total results, and their position within the result set. This
information is crucial for users to understand the scope of their search
results and their current position within those results.

Pagination info components typically display text like "Showing 1-10 of 127
results" or similar information that helps users understand the extent of their
search results. The component ensures this information is clearly visible and
properly formatted, helping users navigate through large result sets
effectively.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic search pagination info -->
{{ ui.search_pagination_info(total=127, first=1, last=10) }}

<!-- Search pagination info with custom template -->
{{ ui.search_pagination_info(total=50, first=21, last=30, template=_("Results {first} - {last} out of {total}")) }}
```
///

| Parameter  | Type   | Default | Description                                                |
|------------|--------|---------|------------------------------------------------------------|
| `total`    | int    | -       | Total number of search results.                            |
| `first`    | int    | -       | Position of the first item in the current page.            |
| `last`     | int    | -       | Position of the last item in the current page.             |
| `template` | string | -       | Template string for formatting the pagination information. |

/// details | Theme-Specific Parameters
    type: tip

- `variant` (string): Style variant (e.g., "short", "detailed")
- `show_total` (bool): Whether to show total count
- `show_range` (bool): Whether to show item range
- `format` (string): Format for number display (e.g., "numeric", "words")
///

## Search Results Header

The [`search_results_header`][search-results-header] component creates headers
for search results displays, providing context and organization for the search
results. This component typically includes information about the search query,
result counts, and controls for managing or refining the search results.

Search results headers are important for orienting users and providing context
about their search. They often include the search query that was performed, the
number of results found, and controls for sorting or refining the results. The
component ensures this information is clearly presented and easily accessible
to users.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic search results header -->
{{ ui.search_results_header(item_count=25, first_item_position=1, last_item_position=10) }}

<!-- Search results header with query error -->
{{ ui.search_results_header(item_count=0, first_item_position=0, last_item_position=0, query_error="Invalid search query") }}
```
///

| Parameter             | Type   | Default | Description                                     |
|-----------------------|--------|---------|-------------------------------------------------|
| `item_count`          | int    | -       | Total number of search results.                 |
| `first_item_position` | int    | -       | Position of the first item in the current page. |
| `last_item_position`  | int    | -       | Position of the last item in the current page.  |
| `query_error`         | string | -       | Error message if the search query is invalid.   |

/// details | Theme-Specific Parameters
    type: tip

- `variant` (string): Style variant (e.g., "compact", "detailed")
- `show_count` (bool): Whether to show result count
- `show_range` (bool): Whether to show item range
- `template` (string): Custom template for header display
///

## Search Sort Control

The [`search_sort_control`][search-sort-control] component provides controls
for sorting search results in different ways, allowing users to organize their
results by relevance, date, name, or other criteria. Sorting controls are
essential for helping users find the most relevant results quickly.

Sort control components typically include dropdown menus or other interface
elements that allow users to select different sorting options. The component
handles the interface for these controls while ensuring proper accessibility
and clear indication of the current sort order. It provides users with the
ability to reorganize their results based on their specific needs.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic search sort control -->
{{ ui.search_sort_control(
    selected="relevance",
    options=[{"text": "Relevance", "value": "relevance"}, {"text": "Date", "value": "date"}]
) }}
```
///

| Parameter  | Type   | Default | Description                                                         |
|------------|--------|---------|---------------------------------------------------------------------|
| `name`     | string | "sort"  | Name attribute for the sort control.                                |
| `selected` | string | -       | Currently selected sort option.                                     |
| `options`  | list   | -       | Available sort options as [{"text": "...", "value": "..."}] format. |
| `label`    | string | -       | Label text for the sort control.                                    |

## Search Submit Button

The [`search_submit_button`][search-submit-button] component creates search
submission buttons that trigger search operations when clicked. This component
provides the primary action for initiating searches and must be clearly
identifiable and appropriately styled to encourage user action.

Search submit buttons handle the form submission functionality for search
operations and often include visual elements like search icons to clearly
indicate their purpose. The component ensures proper accessibility and provides
clear feedback about the search submission action. It works within
[`search_form`][search-form] containers to provide the primary search
initiation mechanism.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic search submit button -->
{{ ui.search_submit_button("Search") }}

<!-- Search submit with icon -->
{{ ui.search_submit_button(ui.icon("search") ~ " Search") }}
```
///

| Parameter | Type   | Default  | Description                        |
|-----------|--------|----------|------------------------------------|
| `content` | string | "Search" | The text to display on the button. |

/// details | Theme-Specific Parameters
    type: tip

- `size` (string): Size of the button (e.g., "sm", "lg")
- `variant` (string): Style variant (e.g., "primary", "secondary", "outline")
- `icon` (string): Icon to display on the button
- `loading` (bool): Whether to show loading state
- `full_width` (bool): Whether to make button full-width
///

/// admonition | Relationship
    type: info

The [`search_submit_button`][search-submit-button] component works within
[`search_form`][search-form] containers alongside
[`search_input`][search-input] and other search controls to create complete
search interfaces. While the input provides the query, the submit button
triggers the search operation.

///
