# Organization Changes Page

View the revision history of an organization.

## Overview

The changes page displays:
- Organization revision history
- Change timestamps
- Editor information
- Revision comparisons
- Field-level changes

## URL Pattern

```
GET /organization/changes/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/changes/environmental-protection-agency
<<vars.site_url>>/organization/changes/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The changes page allows users to:
- Track organization modifications
- View previous versions
- Compare revisions
- Understand change history
- Restore previous versions (if authorized)

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| View revisions | See change history | Revision list |
| Compare revisions | See differences | Compare checkboxes |
| View revision | See specific version | View link |
| Restore revision | Revert to previous | Restore button |
| Back to org | Return to main page | Back link |

## Template

**File:** `templates/organization/changes.html`

### Template Structure

```jinja
{% extends "organization/_base.html" %}

{%- block subtitle -%}
    {{ ui.subtitle_item(_("Changes")) }}
{%- endblock -%}

{%- block primary_content_inner %}
    <h2>{{ _('Changes') }}</h2>

    {% if revisions %}
        {{ ui.table() }}
            {{ ui.table_head() }}
                {{ ui.table_row() }}
                    {{ ui.table_cell(_('Select')) }}
                    {{ ui.table_cell(_('Revision')) }}
                    {{ ui.table_cell(_('Timestamp')) }}
                    {{ ui.table_cell(_('Editor')) }}
                    {{ ui.table_cell(_('Message')) }}
                    {{ ui.table_cell(_('Actions')) }}

            {{ ui.table_body() }}
                {% for revision in revisions %}
                    {{ ui.table_row() }}
                        {{ ui.table_cell() }}
                            {{ ui.checkbox(name='revision', value=revision.revision_id) }}

                        {{ ui.table_cell() }}
                            {{ revision.revision_id[:8] }}

                        {{ ui.table_cell() }}
                            {{ h.render_datetime(revision.timestamp, with_hours=true) }}

                        {{ ui.table_cell() }}
                            {{ ui.link(revision.author, h.url_for('user.read', id=revision.author)) }}

                        {{ ui.table_cell() }}
                            {{ revision.message or '-' }}

                        {{ ui.table_cell() }}
                            {{ ui.button(_('View'), href=h.url_for('organization.read', id=group_dict.id, revision=revision.revision_id)) }}
                {% endfor %}
            {{ ui.table_body() }}
        {{ ui.table() }}

        {{ ui.button(_('Compare Selected'), onclick='compareRevisions()') }}
    {% else %}
        {{ ui.alert(_('This organization has no change history yet'), style='info') }}
    {% endif %}
{%- endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `group_dict` | Organization dictionary |
| `revisions` | List of revision objects |
| `revision_count` | Total revisions |

### Revision Object

Each revision contains:
- `revision_id` - Unique identifier
- `timestamp` - When change occurred
- `author` - User who made change
- `message` - Optional change message
- `changes` - List of changed fields

## Screenshot Placeholder

![Organization Changes](../screenshots/organization-changes.png)

**What to show:**
- Revision history table
- Timestamps and editors
- Change messages
- View/compare actions
- Empty state (if no changes)

## Customization Notes

### Revision Display

Customize revision rows:
```jinja
{% block revision_row %}
    <tr>
        <td>
            {{ ui.checkbox(name='revision', value=revision.revision_id) }}
        </td>
        <td>
            <code>{{ revision.revision_id[:8] }}</code>
        </td>
        <td>
            <span class="timestamp" title="{{ h.render_datetime(revision.timestamp) }}">
                {{ h.time_ago_from_timestamp(revision.timestamp) }}
            </span>
        </td>
        <td>
            {{ ui.avatar(revision.author, size=30) }}
            {{ ui.link(revision.author, h.url_for('user.read', id=revision.author)) }}
        </td>
        <td>
            {{ revision.message or '<em class="text-muted">' ~ _('No message') ~ '</em>'|safe }}
        </td>
        <td>
            <div class="revision-actions">
                {{ ui.button(_('View'), size='small') }}
                {% if h.check_access('organization_update') %}
                    {{ ui.button(_('Restore'), size='small', style='warning') }}
                {% endif %}
            </div>
        </td>
    </tr>
{% endblock %}
```

### Change Diff

Show field differences:
```jinja
{% block change_diff %}
    <div class="diff-view">
        <h3>{{ _('Changes in this Revision') }}</h3>

        {% for field, old_val, new_val in revision.changes %}
            <div class="diff-item">
                <strong>{{ field }}:</strong>
                <div class="diff-values">
                    <span class="old-value">{{ old_val or _('Empty') }}</span>
                    <span class="arrow">→</span>
                    <span class="new-value">{{ new_val or _('Empty') }}</span>
                </div>
            </div>
        {% endfor %}
    </div>
{% endblock %}
```

### Compare Functionality

Implement comparison:
```javascript
function compareRevisions() {
    const selected = document.querySelectorAll('input[name="revision"]:checked');
    if (selected.length !== 2) {
        alert('{{ _("Please select exactly 2 revisions to compare") }}');
        return;
    }

    const rev1 = selected[0].value;
    const rev2 = selected[1].value;

    window.location.href = '{{ h.url_for("organization.changes_diff", id=group_dict.id) }}' +
        '?rev1=' + rev1 + '&rev2=' + rev2;
}
```

### Styling

Changes-specific styling:
```scss
.organization-changes {
    .revision-table {
        // Table styling
        width: 100%;
    }

    .revision-actions {
        // Action buttons
        display: flex;
        gap: 0.5rem;
    }

    .diff-view {
        // Diff display
        margin-top: 2rem;

        .diff-item {
            padding: 1rem;
            border: 1px solid #eee;
            margin-bottom: 1rem;
            border-radius: 4px;

            .old-value {
                text-decoration: line-through;
                color: #dc3545;
                background: #ffe6e6;
                padding: 0.25rem 0.5rem;
                border-radius: 3px;
            }

            .new-value {
                color: #28a745;
                background: #e6ffe6;
                padding: 0.25rem 0.5rem;
                border-radius: 3px;
            }

            .arrow {
                margin: 0 0.5rem;
                color: #666;
            }
        }
    }

    .empty-state {
        // No changes state
        text-align: center;
        padding: 3rem;
    }
}
```

## Related Pages

- [Organization Read](read.md) - Main organization page
- [Organization Activity](activity.md) - Activity stream
- [Organization Edit](edit.md) - Edit organization
- [Dataset History](../dataset/history.md) - Dataset version history

## Best Practices

1. **Clear Timeline**: Show revisions chronologically
2. **Attribution**: Credit editors clearly
3. **Diff Visibility**: Highlight changes clearly
4. **Navigation**: Easy return to main page
5. **Restoration**: Allow reverting (with permissions)
6. **Performance**: Paginate long histories

## Extension Hooks

Extensions can modify changes by:
- Adding revision metadata
- Adding custom diff views
- Adding restore workflows
- Adding revision comments
- Adding export functionality
