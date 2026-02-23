# Dataset History Page

View the version history and change log for a dataset.

## Overview

The dataset history page displays:
- All versions of the dataset
- Change timestamps
- Editor information
- Revision IDs
- Change comparisons

## URL Pattern

```
GET /dataset/history/{id}
```

**Examples:**
```
<<vars.site_url>>/dataset/history/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
<<vars.site_url>>/dataset/history/annual-environmental-report
```

## Purpose

The history page allows users to:
- Track dataset changes over time
- View previous versions
- Compare different versions
- Understand who made changes
- Restore previous versions (if authorized)

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| View version | See specific version | Version link |
| Compare versions | See differences | Compare checkboxes + button |
| Restore version | Revert to previous (if authorized) | Restore button |
| Back to dataset | Return to main page | Back link |

## Template

**File:** `templates/package/history.html`

### Template Structure

```jinja
{% extends base_template %}

{% block primary_content_inner %}
    {%- block package_archive_notice -%}
        {% if pkg.state == 'deleted' %}
            {{ ui.alert(_('This dataset has been deleted'), style='warning') }}
        {% endif %}
    {%- endblock -%}

    <h2>{{ _('History') }}</h2>

    {{ ui.table() }}
        {{ ui.table_head() }}
            {{ ui.table_row() }}
                {{ ui.table_cell(_('Version')) }}
                {{ ui.table_cell(_('Timestamp')) }}
                {{ ui.table_cell(_('Editor')) }}
                {{ ui.table_cell(_('Action')) }}
        {{ ui.table_body() }}
            {% for revision in revisions %}
                {{ ui.table_row() }}
                    {{ ui.table_cell(revision.revision_id) }}
                    {{ ui.datetime(revision.timestamp) }}
                    {{ ui.link(revision.author, h.url_for('user.read', id=revision.author)) }}
                    {{ ui.link(_('View'), h.url_for('dataset.read', id=pkg.id, revision=revision.revision_id)) }}
            {% endfor %}
    {{ ui.table() }}
{% endblock %}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `pkg` | Dataset object |
| `pkg_dict` | Dataset dictionary |
| `revisions` | List of revision objects |
| `base_template` | Base template path |

### Revision Object

Each revision contains:
- `revision_id` - Unique identifier
- `timestamp` - When change occurred
- `author` - User who made change
- `message` - Optional change message
- `changes` - List of changed fields

## Screenshot Placeholder

![Dataset History](../screenshots/dataset-history.png)

**What to show:**
- Version history table
- Timestamps and editors
- View/compare action links
- Archive notice (if deleted)
- Navigation breadcrumbs

## Customization Notes

### Version Display

Customize version display:
```jinja
{% block version_info %}
    <div class="version-item">
        <h4>{{ _('Version') }} {{ loop.index }}</h4>
        <p>{{ _('Changed by') }} {{ revision.author }}</p>
        <p>{{ _('On') }} {{ h.render_datetime(revision.timestamp) }}</p>
    </div>
{% endblock %}
```

### Change Diff

Show what changed:
```jinja
{% block change_diff %}
    {% for field, old_val, new_val in revision.changes %}
        <div class="diff-item">
            <strong>{{ field }}:</strong>
            <span class="old">{{ old_val }}</span> →
            <span class="new">{{ new_val }}</span>
        </div>
    {% endfor %}
{% endblock %}
```

### Restore Functionality

Add restore capability:
```jinja
{% block restore_action %}
    {% if h.check_access('package_update', {'id': pkg.id}) %}
        {{ ui.form(method='POST', action=h.url_for('dataset.edit', id=pkg.id)) }}
            {{ ui.hidden_input(name='revision_id', value=revision.revision_id) }}
            {{ ui.submit(_('Restore this version')) }}
        {{ ui.form() }}
    {% endif %}
{% endblock %}
```

### Pagination

For long histories:
```jinja
{% block pagination %}
    {{ ui.pagination(
        page=page,
        total=total_revisions,
        href=h.url_for('dataset.history', id=pkg.id, page=page)
    ) }}
{% endblock %}
```

### Styling

History-specific styling:
```scss
.dataset-history {
    .version-table {
        // Table styling
    }

    .diff-item {
        // Change diff styling

        .old {
            text-decoration: line-through;
            color: #dc3545;
        }

        .new {
            color: #28a745;
        }
    }

    .archive-notice {
        // Deleted dataset notice
    }
}
```

## Related Pages

- [Dataset Read](read.md) - Main dataset view
- [Dataset Edit](edit.md) - Edit dataset
- [Dataset Activity](activity.md) - Activity stream
- [Resource History](../resource/history.md) - Resource version history

## Best Practices

1. **Clear Timeline**: Show versions chronologically
2. **Attribution**: Credit editors clearly
3. **Diff Visibility**: Highlight changes clearly
4. **Navigation**: Easy return to main page
5. **Restoration**: Allow reverting (with permissions)
6. **Performance**: Paginate long histories

## Extension Hooks

Extensions can modify history by:
- Adding version metadata
- Adding custom diff views
- Adding restore workflows
- Adding version comments
- Adding export functionality
