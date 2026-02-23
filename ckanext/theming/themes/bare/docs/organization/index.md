# Organization Index Page

List and search all organizations in the CKAN portal.

## Overview

The organization index page provides:

- List of all organizations
- Search functionality
- Sorting options
- Pagination
- Organization count

## URL Pattern

```
GET /organization
GET /organization?q={query}
GET /organization?sort={field}
```

**Examples:**
```
<<vars.site_url>>/organization
<<vars.site_url>>/organization?q=environmental
<<vars.site_url>>/organization?sort=title asc
```

## Purpose

The index page allows users to:
- Browse all organizations
- Search for specific organizations
- Discover dataset owners
- Navigate to organization pages

## Actions Available

| Action              | Description                 |
|---------------------|-----------------------------|
| Search              | Find organizations          |
| Sort                | Change order                |
| View organization   | Navigate to org             |
| Create organization | Add new org (if authorized) |
| Pagination          | Navigate pages              |

## Template

**File:** `templates/organization/index.html`

### Template Structure

```jinja
{% extends "organization/_base.html" %}
{%- set _layout = _layout | default("fullwidth") -%}

{%- block breadcrumb_content %}
    {{ ui.breadcrumb(_('Organizations'), h.url_for('organization.index')) }}
{%- endblock -%}

{%- block primary_content_inner %}
    {{ ui.search_form(
        action=h.url_for('organization.index'),
        name='q',
        value=q
    ) }}

    {{ ui.sort_controls(
        sorts=[
            {'value': 'name asc', 'text': _('Name Ascending')},
            {'value': 'name desc', 'text': _('Name Descending')},
            {'value': 'packages asc', 'text': _('Datasets Ascending')},
            {'value': 'packages desc', 'text': _('Datasets Descending')},
        ]
    ) }}

    {{ ui.grid() }}
        {% for org in page.items %}
            {{ ui.column(span={"xs": 12, "md": 6, "lg": 4}) }}
                {{ ui.organization(org) }}
            {{ ui.column() }}
        {% endfor %}
    {{ ui.grid() }}

    {{ ui.pagination(page=page, href=h.pager_url) }}
{%- endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `page` | Pagination object |
| `q` | Search query |
| `sort_by_selected` | Current sort |
| `group_type` | Organization type |
| `organizations` | Organization list |

## Screenshot Placeholder

![Organization Index](../screenshots/organization-index.png)

**What to show:**
- Full page with search bar
- Grid of organization cards
- Sort options
- Pagination controls
- Create button (if authorized)

## Customization Notes

### Organization Display

Customize organization cards:
```jinja
{% block organization_item %}
    <div class="organization-card">
        {% if org.image_url %}
            {{ ui.image(org.image_url, alt=org.title, class='org-logo') }}
        {% endif %}

        <h3>{{ ui.link(org.title or org.name, h.url_for('organization.read', id=org.name)) }}</h3>

        <p>{{ h.markdown_extract(org.description, 150) }}</p>

        <div class="org-stats">
            <span>{{ org.package_count }} datasets</span>
            <span>{{ org.member_count }} members</span>
        </div>
    </div>
{% endblock %}
```

### Search Configuration

Configure search behavior:
```jinja
{% block search_form %}
    {{ ui.form(
        method='GET',
        action=h.url_for('organization.index'),
        class='organization-search'
    ) }}
        {{ ui.input(
            name='q',
            label=_('Search organizations'),
            placeholder=_('Search...'),
            value=q
        ) }}
        {{ ui.submit(_('Search')) }}
    {{ ui.form() }}
{% endblock %}
```

### Sorting Options

Available sort options:
- Name Ascending
- Name Descending
- Datasets Ascending
- Datasets Descending
- Date Created (Newest)
- Date Created (Oldest)

### Empty State

Handle no organizations:
```jinja
{% block organizations_empty %}
    <div class="empty-state">
        {{ ui.icon('building', size='large') }}
        <h3>{{ _('No Organizations') }}</h3>
        <p>{{ _('There are no organizations in this portal yet') }}</p>
        {% if h.check_access('organization_create') %}
            {{ ui.button(_('Create Organization'), href=h.url_for('organization.new'), style='primary') }}
        {% endif %}
    </div>
{% endblock %}
```

### Styling

Index-specific styling:
```scss
.organization-index {
    .organization-grid {
        // Grid layout
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 1.5rem;
    }

    .organization-card {
        // Card styling
        border: 1px solid #eee;
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
    }

    .org-logo {
        // Logo styling
        max-height: 100px;
        max-width: 200px;
        object-fit: contain;
        margin-bottom: 1rem;
    }

    .org-stats {
        // Statistics
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 1rem;
        color: #666;
    }
}
```

## Related Pages

- [Organization Read](read.md) - View individual organization
- [Organization Create](new.md) - Create new organization
- [Dataset Search](../dataset/search.md) - Search datasets by organization

## Best Practices

1. **Visual Identity**: Show organization logos
2. **Clear Stats**: Display dataset and member counts
3. **Easy Search**: Prominent search functionality
4. **Responsive Grid**: Mobile-friendly layout
5. **Empty State**: Guide users to create first org
6. **Accessibility**: Ensure keyboard navigation

## Extension Hooks

Extensions can modify index by:
- Adding custom facets
- Adding organization types
- Adding custom filters
- Adding organization metadata
- Adding bulk operations
