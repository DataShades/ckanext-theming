# Sections

Section components help organize content into distinct areas of the page,
providing clear visual separation and structure. They are used to create
different areas like sidebars, main content sections, and other page
divisions. These components work with content components to create organized
and hierarchical page layouts.

## Facet Section

The [`facet_section`][facet-section] component creates dedicated sections for
facet filter displays, organizing filter options into logical groups within the
filtering interface. This component is specifically designed for search and
filtering functionality, providing clear visual separation between different
types of filters such as organization, group, license, or format filters.

Facet sections are crucial for creating intuitive filtering experiences,
especially when dealing with complex datasets that have multiple filterable
attributes. The component ensures that related filter options are grouped
together and clearly distinguished from other filter categories. It works
closely with [`facet`][] components to provide a comprehensive filtering
interface.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic facet section -->
{% call ui.util.call(ui.facet_section, title="Organization") %}
    {% call ui.util.call(ui.facet_wrapper, title="Organization") %}
        {{ ui.facet("Government", key="org", value="gov", count=15) }}
    {% endcall %}
{% endcall %}
```
///

/// admonition | Relationship
    type: info

The [`facet_section`][facet-section] component works with [`facet`][] and
[`facet_wrapper`][facet-wrapper] components to create comprehensive filtering
interfaces. While facet sections provide the structural grouping, individual
facets provide the specific filter options.

///

| Parameter | Type   | Default | Description                                      |
|-----------|--------|---------|--------------------------------------------------|
| `content` | string | -       | The content to display within the facet section. |
| `title`   | string | -       | Title of the section.                            |

/// details | Theme-Specific Parameters
    type: tip

- `collapsible` (bool): Whether the section can be collapsed
- `initially_collapsed` (bool): Whether the section starts collapsed
- `icon` (string): Icon to display with the section
///

## Section

The [`section`][] component provides a general-purpose container for organizing
content into distinct sections within a page. This component creates clear
visual separation between different content areas and helps establish a logical
information hierarchy. Sections are fundamental for creating well-structured
pages that guide users through content in an organized manner.

The section component typically includes appropriate spacing, potential
headers, and visual boundaries that distinguish it from surrounding
content. It's versatile enough to be used for various content types including
introduction areas, feature highlights, content groupings, or any other logical
content divisions. The component ensures consistent styling and spacing across
different themes while maintaining flexibility for various content types.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic section -->
{{ ui.section("Content for this section", title="Section title") }}
```
///

| Parameter | Type   | Default | Description                                |
|-----------|--------|---------|--------------------------------------------|
| `content` | string | -       | The content to display within the section. |
| `title`   | string | -       | Title of the section.                      |

/// details | Theme-Specific Parameters
    type: tip

- `collapsible` (bool): Whether the section can be collapsed
- `icon` (string): Icon to display with the section
///

## Sidebar Section

The [`sidebar_section`][sidebar-section] component creates dedicated sections
within sidebar areas, organizing sidebar content into logical groups. Sidebars
often contain multiple types of information such as navigation, filters,
related content, or supplementary information, and this component helps
organize that content into distinct, well-separated areas.

Sidebar sections are particularly important for maintaining usability in narrow
column layouts where space is limited. The component ensures that different
types of sidebar content are clearly separated and easily distinguishable. It
works well with navigation components, filter components, and other
sidebar-specific elements to create cohesive sidebar experiences that remain
usable across different screen sizes.

/// admonition | Usage Example
    type: example

```jinja2
<!-- Basic sidebar section -->
{{ ui.sidebar_section("Sidebar content", title="Sidebar title") }}
```
///

| Parameter | Type   | Default | Description                                        |
|-----------|--------|---------|----------------------------------------------------|
| `content` | string | -       | The content to display within the sidebar section. |
| `title`   | string | -       | Title of the section.                              |

/// details | Theme-Specific Parameters
    type: tip

- `collapsible` (bool): Whether the section can be collapsed
- `icon` (string): Icon to display with the section
///
