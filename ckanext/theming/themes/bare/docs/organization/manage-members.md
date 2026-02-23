# Organization Manage Members Page

Bulk management interface for organization members.

## Overview

The manage members page provides:
- Complete member list
- Bulk role changes
- Bulk removal
- Member search/filter
- Export functionality

## URL Pattern

```
GET /organization/member_manage/{id}
POST /organization/member_manage/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/member_manage/environmental-protection-agency
<<vars.site_url>>/organization/member_manage/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The manage members page allows administrators to:
- View all members at once
- Change multiple member roles
- Remove multiple members
- Search and filter members
- Export member list

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| Select members | Choose for bulk action | Checkboxes |
| Change roles | Update multiple roles | Bulk role change |
| Remove members | Delete multiple members | Bulk remove |
| Search | Filter members | Search input |
| Export | Download member list | Export button |
| Save | Apply changes | Save button |

## Template

**File:** `templates/organization/manage_members.html`

### Template Structure

```jinja
{% extends "organization/_edit_base.html" %}

{%- block subtitle -%}
    {{ ui.subtitle_item(_('Members')) }}
{%- endblock -%}

{%- block primary_content_inner %}
    <h2>{{ _('Manage Members') }}</h2>

    {{ ui.form(method="POST") }}
        <div class="member-filters">
            {{ ui.input(
                name='q',
                label=_('Search members'),
                placeholder=_('Filter by name...'),
                value=q
            ) }}
        </div>

        {{ ui.table() }}
            {{ ui.table_head() }}
                {{ ui.table_row() }}
                    {{ ui.table_cell() }}
                        {{ ui.checkbox(id='select-all', onchange='toggleAll()') }}
                    {{ ui.table_cell(_('User')) }}
                    {{ ui.table_cell(_('Role')) }}
                    {{ ui.table_cell(_('Actions')) }}

            {{ ui.table_body() }}
                {% for member in members %}
                    {{ ui.table_row() }}
                        {{ ui.table_cell() }}
                            {{ ui.checkbox(
                                name='selected',
                                value=member.user_id,
                                id='member-' ~ member.user_id
                            ) }}

                        {{ ui.table_cell() }}
                            {{ ui.avatar(member.user_id, size=40) }}
                            {{ ui.link(member.user_name, h.url_for('user.read', id=member.user_id)) }}

                        {{ ui.table_cell() }}
                            {{ ui.select(
                                name='role-' ~ member.user_id,
                                options=[
                                    {'value': 'member', 'text': _('Member')},
                                    {'value': 'editor', 'text': _('Editor')},
                                    {'value': 'admin', 'text': _('Admin')},
                                ],
                                value=member.capacity
                            ) }}

                        {{ ui.table_cell() }}
                            {{ ui.button(_('Remove'), style='danger', size='small') }}
                {% endfor %}
            {{ ui.table_body() }}
        {{ ui.table() }}

        <div class="bulk-actions">
            {{ ui.button(_('Save Changes'), type='submit', style='primary') }}
            {{ ui.button(_('Remove Selected'), type='submit', name='action', value='remove', style='danger') }}
        </div>
    {{ ui.form() }}
{%- endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `group_dict` | Organization dictionary |
| `members` | List of member objects |
| `q` | Search query |
| `selected` | Selected member IDs |

## Screenshot Placeholder

![Organization Manage Members](../screenshots/organization-manage-members.png)

**What to show:**
- Full member table
- Checkboxes for selection
- Role dropdowns inline
- Search/filter controls
- Bulk action buttons

## Customization Notes

### Member Filters

Add filtering options:
```jinja
{% block member_filters %}
    <div class="member-filters">
        <div class="filter-row">
            {{ ui.input(
                name='q',
                label=_('Search'),
                placeholder=_('Search by name or email...')
            ) }}

            {{ ui.select(
                name='role_filter',
                label=_('Filter by role'),
                options=[
                    {'value': '', 'text': _('All Roles')},
                    {'value': 'admin', 'text': _('Admin')},
                    {'value': 'editor', 'text': _('Editor')},
                    {'value': 'member', 'text': _('Member')},
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
    <div class="bulk-actions">
        <div class="bulk-actions-bar">
            <span>{{ _('With selected...') }}</span>

            {{ ui.select(
                name='bulk_action',
                options=[
                    {'value': '', 'text': _('Select action')},
                    {'value': 'role_member', 'text': _('Set as Member')},
                    {'value': 'role_editor', 'text': _('Set as Editor')},
                    {'value': 'role_admin', 'text': _('Set as Admin')},
                    {'value': 'remove', 'text': _('Remove')},
                ],
                onchange='performBulkAction()'
            ) }}

            {{ ui.button(_('Apply'), type='submit') }}
        </div>
    </div>
{% endblock %}
```

### Export Functionality

Add export option:
```jinja
{% block export %}
    <div class="export-section">
        {{ ui.button(_('Export Members'), onclick='exportMembers()') }}

        <script>
        function exportMembers() {
            window.location.href = '{{ h.url_for("organization.members_export", id=group_dict.id) }}';
        }
        </script>
    </div>
{% endblock %}
```

### Select All

Implement toggle functionality:
```javascript
function toggleAll() {
    const selectAll = document.getElementById('select-all');
    const checkboxes = document.querySelectorAll('input[name="selected"]');
    checkboxes.forEach(cb => cb.checked = selectAll.checked);
}

function performBulkAction() {
    const action = document.querySelector('[name="bulk_action"]').value;
    if (action) {
        document.querySelector('[name="action"]').value = action;
        document.querySelector('form').submit();
    }
}
```

### Styling

Manage-specific styling:
```scss
.organization-manage-members {
    .member-filters {
        // Filter area
        margin-bottom: 1.5rem;

        .filter-row {
            display: flex;
            gap: 1rem;
        }
    }

    .member-table {
        // Table styling
        width: 100%;

        .select-column {
            width: 50px;
            text-align: center;
        }
    }

    .bulk-actions {
        // Action bar
        margin-top: 1.5rem;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 4px;

        .bulk-actions-bar {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
    }

    .export-section {
        // Export area
        margin-top: 1rem;
        text-align: right;
    }
}
```

## Related Pages

- [Organization Members](members.md) - Simple member list
- [Add Member](member-new.md) - Add single member
- [Administrators](admins.md) - Admin list

## Best Practices

1. **Clear Selection**: Show selected items
2. **Inline Editing**: Edit roles in place
3. **Confirmation**: Confirm bulk actions
4. **Search/Filter**: Easy member finding
5. **Export**: Allow data export
6. **Feedback**: Show action results

## Extension Hooks

Extensions can modify manage by:
- Adding custom member fields
- Adding invitation management
- Adding approval workflows
- Adding member analytics
- Adding custom exports
