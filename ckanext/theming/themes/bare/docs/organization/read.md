# Organization Read Page

View organization details and browse its datasets.

## Overview

The organization read page displays:
- Organization profile information
- Datasets owned by organization
- Organization statistics
- Navigation to sub-pages
- Follow/unfollow functionality

## URL Pattern

```
GET /organization/{id}
GET /organization/{name}
GET /organization/{id}?page={number}
```

**Examples:**
```
<<vars.site_url>>/organization/environmental-protection-agency
<<vars.site_url>>/organization/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
<<vars.site_url>>/organization/epa?page=2
```

## Purpose

The read page allows users to:
- View organization information
- Browse organization's datasets
- Understand organization's role
- Follow organization updates
- Access organization management (if authorized)

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| View datasets | Browse org datasets | Dataset list |
| Search datasets | Filter org datasets | Search form |
| Follow org | Subscribe to updates | Follow button |
| Edit org | Modify organization | Edit button (if authorized) |
| Delete org | Remove organization | Delete button (if authorized) |
| View about | See org details | About link |
| View members | See member list | Members link |
| View activity | See activity stream | Activity link |

## Template

**File:** `templates/organization/read.html`

### Template Structure

```jinja
{% extends "organization/_base.html" %}

{%- set _layout = _layout | default("content_control") -%}

{%- block subtitle -%}
    {{ ui.subtitle_item(group_dict.title or group_dict.name) }}
{%- endblock -%}

{%- block content_action -%}
    {% if h.check_access('organization_update', {'id': group_dict.id}) %}
        {{ ui.content_action(_('Edit'), h.url_for('organization.edit', id=group_dict.id)) }}
    {% endif %}
{%- endblock -%}

{%- block primary_content_inner %}
    {{ ui.search_form(
        action=h.url_for('organization.read', id=group_dict.id),
        name='q',
        value=q
    ) }}

    {{ ui.dataset_list(datasets) }}
        {% for dataset in datasets %}
            {{ ui.package(dataset) }}
        {% endfor %}
    {{ ui.dataset_list() }}

    {{ ui.pagination(page=page, href=h.pager_url) }}
{%- endblock -%}

{%- block secondary_content %}
    {{ ui.organization_info(group_dict) }}
    {{ ui.organization_follow_button(group_dict) }}
{%- endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `group_dict` | Organization dictionary |
| `datasets` | Dataset results |
| `page` | Pagination object |
| `q` | Search query |
| `facets` | Available facets |
| `fields` | Active filters |
| `am_following` | User follows flag |

## Screenshot Placeholder

![Organization Read](../screenshots/organization-read.png)

**What to show:**
- Organization header with logo
- Dataset search within organization
- Dataset results list
- Sidebar with org info
- Action buttons (edit, follow, etc.)
- Breadcrumb navigation

## Customization Notes

### Organization Header

Customize org display:
```jinja
{% block organization_header %}
    <div class="org-header">
        {% if group_dict.image_url %}
            {{ ui.image(group_dict.image_url, alt=group_dict.title, class='org-logo') }}
        {% endif %}

        <h1>{{ group_dict.title or group_dict.name }}</h1>

        {% if group_dict.description %}
            <p class="org-description">{{ h.markdown_extract(group_dict.description, 200) }}</p>
        {% endif %}

        <div class="org-meta">
            <span>{{ group_dict.package_count }} datasets</span>
            <span>{{ group_dict.member_count }} members</span>
        </div>
    </div>
{% endblock %}
```

### Dataset Search

Search within organization:
```jinja
{% block dataset_search %}
    {{ ui.form(
        method='GET',
        action=h.url_for('organization.read', id=group_dict.id),
        class='dataset-search'
    ) }}
        {{ ui.input(
            name='q',
            label=_('Search datasets'),
            placeholder=_('Search within organization...'),
            value=q
        ) }}
        {{ ui.submit(_('Search')) }}
    {{ ui.form() }}
{% endblock %}
```

### Sidebar Information

Customize sidebar:
```jinja
{% block secondary_content %}
    <aside class="org-sidebar">
        {{ ui.card(title=_('Organization Info')) }}
            <dl>
                <dt>{{ _('Name') }}</dt>
                <dd>{{ group_dict.title }}</dd>

                <dt>{{ _('Datasets') }}</dt>
                <dd>{{ group_dict.package_count }}</dd>

                <dt>{{ _('Members') }}</dt>
                <dd>{{ group_dict.member_count }}</dd>

                {% if group_dict.created %}
                    <dt>{{ _('Created') }}</dt>
                    <dd>{{ h.render_datetime(group_dict.created) }}</dd>
                {% endif %}
            </dl>
        {{ ui.card() }}

        {{ ui.follow_button(group_dict, am_following) }}
    </aside>
{% endblock %}
```

### Empty State

No datasets message:
```jinja
{% block datasets_empty %}
    <div class="empty-state">
        {{ ui.icon('inbox', size='large') }}
        <h3>{{ _('No Datasets') }}</h3>
        <p>{{ _('This organization has no datasets yet') }}</p>
        {% if h.check_access('package_create', {'owner_org': group_dict.id}) %}
            {{ ui.button(_('Add Dataset'), href=h.url_for('dataset.new', owner_org=group_dict.id), style='primary') }}
        {% endif %}
    </div>
{% endblock %}
```

### Styling

Read-specific styling:
```scss
.organization-read {
    .org-header {
        // Header section
        display: flex;
        align-items: center;
        gap: 2rem;
        margin-bottom: 2rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid #eee;
    }

    .org-logo {
        // Logo styling
        max-height: 120px;
        max-width: 200px;
    }

    .org-sidebar {
        // Sidebar styling
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 4px;
    }

    .dataset-search {
        // Search form
        margin-bottom: 1.5rem;
    }
}
```

## Related Pages

- [Organization Index](index.md) - List all organizations
- [Organization About](about.md) - Organization details
- [Organization Edit](edit.md) - Edit organization
- [Dataset Read](../dataset/read.md) - View dataset

## Best Practices

1. **Clear Identity**: Show organization branding
2. **Dataset Focus**: Make datasets prominent
3. **Easy Navigation**: Link to related pages
4. **Search Within**: Allow filtering datasets
5. **Action Access**: Show appropriate actions
6. **Responsive**: Mobile-friendly layout

## Extension Hooks

Extensions can modify read by:
- Adding custom metadata
- Adding dataset filters
- Adding organization widgets
- Adding custom actions
- Adding related organizations
