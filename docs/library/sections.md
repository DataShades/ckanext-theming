# Sections

Section components provide structural divisions for organizing content into logical sections and areas of the page.

## Overview

Section components help organize content into distinct areas of the page, providing clear visual separation and structure. They are used to create different areas like sidebars, main content sections, and other page divisions. These components work with content components to create organized and hierarchical page layouts.

## Facet Section

The `facet_section` component creates dedicated sections for facet filter displays, organizing filter options into logical groups within the filtering interface. This component is specifically designed for search and filtering functionality, providing clear visual separation between different types of filters such as organization, group, license, or format filters.

Facet sections are crucial for creating intuitive filtering experiences, especially when dealing with complex datasets that have multiple filterable attributes. The component ensures that related filter options are grouped together and clearly distinguished from other filter categories. It works closely with `facet` components to provide a comprehensive filtering interface.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic facet section -->
{{ ui.facet_section(ui.facet("Organization", "org", "Government", 15, active=False)) }}

<!-- Facet section with attributes -->
{{ ui.facet_section(ui.facet("Format", "format", "CSV", 8, active=False), attrs={"class": "facet-section"}) }}
```
///

/// admonition | Relationship
    type: info

The `facet_section` component works with `facet` and `facet_wrapper` components to create comprehensive filtering interfaces. While facet sections provide the structural grouping, individual facets provide the specific filter options.
///

## Section

The `section` component provides a general-purpose container for organizing content into distinct sections within a page. This component creates clear visual separation between different content areas and helps establish a logical information hierarchy. Sections are fundamental for creating well-structured pages that guide users through content in an organized manner.

The section component typically includes appropriate spacing, potential headers, and visual boundaries that distinguish it from surrounding content. It's versatile enough to be used for various content types including introduction areas, feature highlights, content groupings, or any other logical content divisions. The component ensures consistent styling and spacing across different themes while maintaining flexibility for various content types.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic section -->
{{ ui.section("Content for this section") }}

<!-- Section with attributes -->
{{ ui.section("Styled section content", attrs={"class": "custom-section"}) }}
```
///

## Sidebar Section

The `sidebar_section` component creates dedicated sections within sidebar areas, organizing sidebar content into logical groups. Sidebars often contain multiple types of information such as navigation, filters, related content, or supplementary information, and this component helps organize that content into distinct, well-separated areas.

Sidebar sections are particularly important for maintaining usability in narrow column layouts where space is limited. The component ensures that different types of sidebar content are clearly separated and easily distinguishable. It works well with navigation components, filter components, and other sidebar-specific elements to create cohesive sidebar experiences that remain usable across different screen sizes.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic sidebar section -->
{{ ui.sidebar_section("Sidebar content") }}

<!-- Sidebar section with attributes -->
{{ ui.sidebar_section("Navigation content", attrs={"class": "sidebar-nav-section"}) }}
```
///
