# Organization Members Page

View and manage organization members.

## Overview

The members page displays:
- List of organization members
- Member roles (admin, member, editor)
- Member count
- Add member functionality
- Member management

## URL Pattern

```
GET /organization/members/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/members/environmental-protection-agency
<<vars.site_url>>/organization/members/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The members page allows users to:
- View all organization members
- See member roles and permissions
- Add new members (if authorized)
- Manage member access
- Remove members (if authorized)

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| View members | See member list | Member table |
| Add member | Invite new member | Add button |
| Edit role | Change member role | Role dropdown |
| Remove member | Delete membership | Remove button |
| Manage members | Bulk management | Manage link |

## Template

**File:** `templates/organization/members.html`

### Template Structure

```jinja
{% extends "organization/_base.html" %}

{%- block subtitle -%}
    {{ ui.subtitle_item(_('Members')) }}
{%- endblock -%}

{%- block primary_content_inner %}
    <h2>{{ _('Members') }}</h2>

    {% if members %}
        {{ ui.table() }}
            {{ ui.table_head() }}
                {{ ui.table_row() }}
                    {{ ui.table_cell(_('User')) }}
                    {{ ui.table_cell(_('Role')) }}
                    {{ ui.table_cell(_('Actions')) }}

            {{ ui.table_body() }}
                {% for member in members %}
                    {{ ui.table_row() }}
                        {{ ui.table_cell() }}
                            {{ ui.avatar(member.user_id, size=40) }}
                            {{ ui.link(member.user_name, h.url_for('user.read', id=member.user_id)) }}

                        {{ ui.table_cell() }}
                            <span class="role-badge role-{{ member.capacity }}">{{ member.capacity }}</span>

                        {{ ui.table_cell() }}
                            {% if h.check_access('organization_member_create', {'id': group_dict.id}) %}
                                {{ ui.button(_('Remove'), style='danger', size='small') }}
                            {% endif %}
                {% endfor %}
            {{ ui.table_body() }}
        {{ ui.table() }}
    {% else %}
        {{ ui.alert(_('This organization has no members yet'), style='info') }}
    {% endif %}

    {% if h.check_access('organization_member_create', {'id': group_dict.id}) %}
        {{ ui.button(_('Add Member'), href=h.url_for('organization.member_new', id=group_dict.id), style='primary') }}
    {% endif %}
{%- endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `group_dict` | Organization dictionary |
| `members` | List of member objects |
| `member_count` | Total members |

### Member Object

Each member contains:
- `user_id` - User identifier
- `user_name` - Username
- `capacity` - Role (admin, member, editor)
- `created` - Membership creation date

## Screenshot Placeholder

![Organization Members](../screenshots/organization-members.png)

**What to show:**
- Member table with avatars
- Role badges
- Action buttons
- Add member button
- Empty state (if no members)

## Customization Notes

### Member Display

Customize member rows:
```jinja
{% block member_row %}
    <tr>
        <td>
            <div class="member-info">
                {{ ui.avatar(member.user_id, size=50) }}
                <div>
                    <strong>{{ member.user_name }}</strong>
                    {% if member.email %}
                        <small>{{ member.email }}</small>
                    {% endif %}
                </div>
            </div>
        </td>
        <td>
            <span class="role-badge role-{{ member.capacity }}">
                {{ ui.icon(get_role_icon(member.capacity)) }}
                {{ member.capacity|title }}
            </span>
        </td>
        <td>
            <div class="member-actions">
                {{ ui.button(_('Edit Role'), onclick='editRole()') }}
                {{ ui.button(_('Remove'), style='danger') }}
            </div>
        </td>
    </tr>
{% endblock %}
```

### Role Badges

Style different roles:
```jinja
{% block role_badge %}
    {% set role_styles = {
        'admin': 'bg-danger',
        'editor': 'bg-primary',
        'member': 'bg-secondary'
    } %}

    <span class="role-badge {{ role_styles.get(member.capacity, '') }}">
        {{ member.capacity|title }}
    </span>
{% endblock %}
```

### Add Member

Implement add functionality:
```jinja
{% block add_member %}
    {{ ui.dropdown(label=_('Add Member')) }}
        {{ ui.link(_('Add User'), h.url_for('organization.member_new', id=group_dict.id)) }}
        {{ ui.link(_('Invite User'), h.url_for('organization.member_invite', id=group_dict.id)) }}
        {{ ui.link(_('Bulk Add'), h.url_for('organization.member_bulk', id=group_dict.id)) }}
    {{ ui.dropdown() }}
{% endblock %}
```

### Empty State

No members message:
```jinja
{% block members_empty %}
    <div class="empty-state">
        {{ ui.icon('users', size='large') }}
        <h3>{{ _('No Members') }}</h3>
        <p>{{ _('This organization has no members yet') }}</p>
        {% if h.check_access('organization_member_create') %}
            {{ ui.button(_('Add First Member'), href=h.url_for('organization.member_new', id=group_dict.id), style='primary') }}
        {% endif %}
    </div>
{% endblock %}
```

### Styling

Members-specific styling:
```scss
.organization-members {
    .member-table {
        // Table styling
        width: 100%;
    }

    .member-info {
        // Member cell
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .role-badge {
        // Role styling
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 500;

        &.role-admin {
            background: #dc3545;
            color: white;
        }

        &.role-editor {
            background: #007bff;
            color: white;
        }

        &.role-member {
            background: #6c757d;
            color: white;
        }
    }

    .member-actions {
        // Action buttons
        display: flex;
        gap: 0.5rem;
    }

    .empty-state {
        // No members state
        text-align: center;
        padding: 3rem;
    }
}
```

## Related Pages

- [Organization Read](read.md) - Main organization page
- [Add Member](member-new.md) - Add new member
- [Manage Members](manage-members.md) - Bulk management
- [Administrators](admins.md) - Admin list

## Best Practices

1. **Clear Roles**: Show member permissions
2. **Visual Identity**: Use avatars
3. **Easy Actions**: Quick access to manage
4. **Empty State**: Guide to add first member
5. **Permissions**: Show appropriate actions
6. **Responsive**: Mobile-friendly table

## Extension Hooks

Extensions can modify members by:
- Adding custom member metadata
- Adding bulk operations
- Adding member invitations
- Adding approval workflows
- Adding member analytics
