# Organization Bulk Process Page

Manage all datasets owned by the organization in bulk.

## Overview

The bulk process page provides:
- List of all organization datasets
- Bulk edit capabilities
- State changes (activate/deactivate)
- Organization transfer
- Delete operations

## URL Pattern

```
GET /organization/bulk_process/{id}
POST /organization/bulk_process/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/bulk_process/environmental-protection-agency
<<vars.site_url>>/organization/bulk_process/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The bulk process page allows administrators to:
- View all organization datasets
- Select multiple datasets
- Change dataset states in bulk
- Transfer ownership
- Delete multiple datasets
- Export dataset list

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| Select datasets | Choose for bulk action | Checkboxes |
| Make public | Set public state | Bulk action |
| Make private | Set private state | Bulk action |
| Delete | Remove datasets | Bulk delete |
| Transfer | Change ownership | Transfer action |
| Export | Download list | Export button |

## Template

**File:** `templates/organization/bulk_process.html`

### Template Structure

```jinja
{% extends "organization/_edit_base.html" %}
{%- set _layout = _layout | default("content_control") -%}

{%- set dataset_type = h.default_package_type() %}

{%- block subtitle -%}
    {{ ui.subtitle_item(_('Datasets')) }}
{%- endblock -%}

{%- block primary_content_inner %}
    <h2>{{ _('Manage Datasets') }}</h2>

    {{ ui.form(method="POST") }}
        <div class="dataset-filters">
            {{ ui.input(
                name='q',
                label=_('Search datasets'),
                placeholder=_('Filter...'),
                value=q
            ) }}

            {{ ui.select(
                name='state',
                label=_('Filter by state'),
                options=[
                    {'value': '', 'text': _('All States')},
                    {'value': 'active', 'text': _('Active')},
                    {'value': 'draft', 'text': _('Draft')},
                    {'value': 'deleted', 'text': _('Deleted')},
                ]
            ) }}
        </div>

        {{ ui.table() }}
            {{ ui.table_head() }}
                {{ ui.table_row() }}
                    {{ ui.table_cell() }}
                        {{ ui.checkbox(id='select-all', onchange='toggleAll()') }}
                    {{ ui.table_cell(_('Name')) }}
                    {{ ui.table_cell(_('State')) }}
                    {{ ui.table_cell(_('Resources')) }}
                    {{ ui.table_cell(_('Actions')) }}

            {{ ui.table_body() }}
                {% for dataset in datasets %}
                    {{ ui.table_row() }}
                        {{ ui.table_cell() }}
                            {{ ui.checkbox(
                                name='selected',
                                value=dataset.id,
                                id='dataset-' ~ dataset.id
                            ) }}

                        {{ ui.table_cell() }}
                            {{ ui.link(dataset.title or dataset.name, h.url_for('dataset.read', id=dataset.id)) }}
                            <br>
                            <small class="text-muted">{{ dataset.id[:8] }}</small>

                        {{ ui.table_cell() }}
                            <span class="state-badge state-{{ dataset.state }}">{{ dataset.state }}</span>

                        {{ ui.table_cell() }}
                            {{ dataset.resource_count }}

                        {{ ui.table_cell() }}
                            <div class="dataset-actions">
                                {{ ui.button(_('Edit'), href=h.url_for('dataset.edit', id=dataset.id), size='small') }}
                            </div>
                {% endfor %}
            {{ ui.table_body() }}
        {{ ui.table() }}

        <div class="bulk-actions">
            <span>{{ _('With selected...') }}</span>

            {{ ui.select(
                name='bulk_action',
                options=[
                    {'value': '', 'text': _('Select action')},
                    {'value': 'public', 'text': _('Make Public')},
                    {'value': 'private', 'text': _('Make Private')},
                    {'value': 'delete', 'text': _('Delete')},
                ],
                onchange='performBulkAction()'
            ) }}

            {{ ui.button(_('Apply'), type='submit') }}
        </div>
    {{ ui.form() }}

    {{ ui.pagination(page=page, href=h.pager_url) }}
{%- endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `group_dict` | Organization dictionary |
| `datasets` | Dataset list |
| `page` | Pagination object |
| `q` | Search query |
| `dataset_type` | Package type |

## Screenshot Placeholder

![Organization Bulk Process](../screenshots/organization-bulk-process.png)

**What to show:**
- Dataset table with checkboxes
- Search/filter controls
- State indicators
- Bulk action dropdown
- Pagination controls

## Customization Notes

### Dataset Filters

Add filtering options:
```jinja
{% block dataset_filters %}
    <div class="dataset-filters">
        <div class="filter-row">
            {{ ui.input(
                name='q',
                label=_('Search'),
                placeholder=_('Search by name or description...')
            ) }}

            {{ ui.select(
                name='state',
                label=_('State'),
                options=[
                    {'value': '', 'text': _('All')},
                    {'value': 'active', 'text': _('Active')},
                    {'value': 'draft', 'text': _('Draft')},
                    {'value': 'deleted', 'text': _('Deleted')},
                ]
            ) }}

            {{ ui.select(
                name='visibility',
                label=_('Visibility'),
                options=[
                    {'value': '', 'text': _('All')},
                    {'value': 'public', 'text': _('Public')},
                    {'value': 'private', 'text': _('Private')},
                ]
            ) }}
        </div>
    </div>
{% endblock %}
```

### Bulk Actions

Implement bulk operations:
```jinja
{% block bulk_actions %}
    <div class="bulk-actions-bar">
        <span>{{ _('With selected...') }}</span>

        {{ ui.select(
            name='bulk_action',
            options=[
                {'value': '', 'text': _('Select action')},
                {'value': 'public', 'text': _('Make Public')},
                {'value': 'private', 'text': _('Make Private')},
                {'value': 'delete', 'text': _('Delete')},
                {'value': 'transfer', 'text': _('Transfer to Org')},
                {'value': 'export', 'text': _('Export Metadata')},
            ]
        ) }}

        {{ ui.button(_('Apply'), type='submit', name='apply') }}
    </div>
{% endblock %}
```

### State Badges

Style dataset states:
```jinja
{% block state_badge %}
    {% set state_colors = {
        'active': 'bg-success',
        'draft': 'bg-warning',
        'deleted': 'bg-danger'
    } %}

    <span class="state-badge {{ state_colors.get(dataset.state, '') }}">
        {{ dataset.state|title }}
    </span>
{% endblock %}
```

### Styling

Bulk process-specific styling:
```scss
.organization-bulk-process {
    .dataset-filters {
        // Filter area
        margin-bottom: 1.5rem;

        .filter-row {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }
    }

    .dataset-table {
        // Table styling
        width: 100%;

        .select-column {
            width: 50px;
            text-align: center;
        }
    }

    .state-badge {
        // State indicator
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: capitalize;

        &.state-active {
            background: #28a745;
            color: white;
        }

        &.state-draft {
            background: #ffc107;
            color: #333;
        }

        &.state-deleted {
            background: #dc3545;
            color: white;
        }
    }

    .bulk-actions {
        // Action bar
        margin-top: 1.5rem;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 4px;
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .dataset-actions {
        // Row actions
        display: flex;
        gap: 0.5rem;
    }
}
```

## Related Pages

- [Organization Read](read.md) - Main organization page
- [Dataset Edit](../dataset/edit.md) - Edit individual dataset
- [Dataset Search](../dataset/search.md) - Search datasets

## Best Practices

1. **Clear Selection**: Show selected items
2. **State Visibility**: Indicate dataset states
3. **Confirmation**: Confirm bulk actions
4. **Search/Filter**: Easy dataset finding
5. **Feedback**: Show action results
6. **Performance**: Paginate large lists

## Extension Hooks

Extensions can modify bulk process by:
- Adding custom bulk actions
- Adding dataset filters
- Adding export formats
- Adding workflow states
- Adding approval operations
