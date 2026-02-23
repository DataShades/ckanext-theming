# Organization Add Member Page

Add a new member to an organization.

## Overview

The add member page provides:
- User selection interface
- Role assignment
- Permission explanation
- Validation

## URL Pattern

```
GET /organization/member_new/{id}
POST /organization/member_new/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/member_new/environmental-protection-agency
<<vars.site_url>>/organization/member_new/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The add member page allows authorized users to:
- Search for existing users
- Select user to add
- Assign role (admin, editor, member)
- Set permissions

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| Search user | Find user | User search |
| Select user | Choose user | User dropdown |
| Set role | Assign role | Role selector |
| Add member | Create membership | Submit button |
| Cancel | Abort | Cancel button |

## Template

**File:** `templates/organization/member_new.html`

### Template Structure

```jinja
{% extends "organization/_edit_base.html" %}

{%- block subtitle -%}
    {{ ui.subtitle_item(_('Add Member')) }}
{%- endblock -%}

{%- block primary_content_inner %}
    <h2>{{ _('Add Member to Organization') }}</h2>

    {{ ui.form(method="POST") }}
        {{ ui.form_errors(error_summary) }}

        {{ ui.input(
            name='username',
            label=_('User'),
            placeholder=_('Search for user...'),
            value=data.username,
            errors=errors.username,
            required=true,
            autocomplete='user-search'
        ) }}

        {{ ui.select(
            name='role',
            label=_('Role'),
            options=[
                {'value': 'member', 'text': _('Member')},
                {'value': 'editor', 'text': _('Editor')},
                {'value': 'admin', 'text': _('Admin')},
            ],
            value=data.role,
            errors=errors.role,
            required=true
        ) }}

        {{ ui.form_actions() }}
            {{ ui.submit(_('Add Member')) }}
            {{ ui.button(_('Cancel'), href=h.url_for('organization.members', id=group_dict.id), type='button') }}
        {{ ui.form_actions() }}
    {{ ui.form() }}

    <div class="role-help">
        <h3>{{ _('Role Descriptions') }}</h3>
        {{ ui.accordion(
            title=_('What do the roles mean?'),
            open=false
        ) }}
            <dl>
                <dt>{{ _('Admin') }}</dt>
                <dd>{{ _('Can edit the organization, add/remove members, and manage all datasets') }}</dd>

                <dt>{{ _('Editor') }}</dt>
                <dd>{{ _('Can create and edit datasets within this organization') }}</dd>

                <dt>{{ _('Member') }}</dt>
                <dd>{{ _('Can view private datasets and collaborate') }}</dd>
            </dl>
        {{ ui.accordion() }}
    </div>
{%- endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `group_dict` | Organization dictionary |
| `data` | Form data |
| `errors` | Validation errors |
| `error_summary` | Error summary |
| `users` | Available users (if search performed) |

## Screenshot Placeholder

![Organization Add Member](../screenshots/organization-member-new.png)

**What to show:**
- User search/input field
- Role selection dropdown
- Role descriptions
- Submit/cancel buttons
- Validation errors (if any)

## Customization Notes

### User Search

Implement user search:
```jinja
{% block user_search %}
    {{ ui.form(method='GET', id='user-search-form') }}
        {{ ui.input(
            name='q',
            label=_('Search Users'),
            placeholder=_('Enter username or email...'),
            value=q,
            hx={
                'get': h.url_for('organization.member_new', id=group_dict.id),
                'target': '#user-results',
                'trigger': 'input changed delay:500ms'
            }
        ) }}
    {{ ui.form() }}

    <div id="user-results">
        {% if users %}
            {{ ui.list() }}
                {% for user in users %}
                    {{ ui.list_item() }}
                        {{ ui.link(
                            user.name,
                            '#',
                            onclick="selectUser('" ~ user.name ~ "')"
                        ) }}
                    {{ ui.list_item() }}
                {% endfor %}
            {{ ui.list() }}
        {% endif %}
    </div>
{% endblock %}
```

### Role Selection

Enhanced role selector:
```jinja
{% block role_selection %}
    <div class="role-selector">
        {% for role in ['member', 'editor', 'admin'] %}
            <label class="role-option {{ 'selected' if data.role == role }}">
                {{ ui.radio(name='role', value=role, checked=data.role == role) }}
                <div class="role-info">
                    <strong>{{ role|title }}</strong>
                    <p>{{ get_role_description(role) }}</p>
                </div>
            </label>
        {% endfor %}
    </div>
{% endblock %}
```

### Role Descriptions

Detailed role help:
```jinja
{% block role_help %}
    <div class="role-help">
        <h3>{{ _('Role Permissions') }}</h3>

        <table class="role-permissions">
            <thead>
                <tr>
                    <th>{{ _('Permission') }}</th>
                    <th>{{ _('Member') }}</th>
                    <th>{{ _('Editor') }}</th>
                    <th>{{ _('Admin') }}</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{{ _('View datasets') }}</td>
                    <td>{{ ui.icon('check') }}</td>
                    <td>{{ ui.icon('check') }}</td>
                    <td>{{ ui.icon('check') }}</td>
                </tr>
                <tr>
                    <td>{{ _('Create datasets') }}</td>
                    <td>{{ ui.icon('x') }}</td>
                    <td>{{ ui.icon('check') }}</td>
                    <td>{{ ui.icon('check') }}</td>
                </tr>
                <tr>
                    <td>{{ _('Edit datasets') }}</td>
                    <td>{{ ui.icon('x') }}</td>
                    <td>{{ ui.icon('check') }}</td>
                    <td>{{ ui.icon('check') }}</td>
                </tr>
                <tr>
                    <td>{{ _('Manage members') }}</td>
                    <td>{{ ui.icon('x') }}</td>
                    <td>{{ ui.icon('x') }}</td>
                    <td>{{ ui.icon('check') }}</td>
                </tr>
            </tbody>
        </table>
    </div>
{% endblock %}
```

### Styling

Add member-specific styling:
```scss
.organization-member-new {
    .user-search {
        // Search area
        margin-bottom: 1.5rem;
    }

    .role-selector {
        // Role options
        display: flex;
        flex-direction: column;
        gap: 1rem;

        .role-option {
            border: 2px solid #eee;
            border-radius: 4px;
            padding: 1rem;
            cursor: pointer;

            &.selected {
                border-color: #007bff;
                background: #f0f7ff;
            }
        }
    }

    .role-help {
        // Help section
        margin-top: 2rem;
        padding: 1.5rem;
        background: #f8f9fa;
        border-radius: 4px;
    }

    .role-permissions {
        // Permission table
        width: 100%;

        th, td {
            padding: 0.75rem;
            text-align: center;
            border: 1px solid #dee2e6;
        }
    }
}
```

## Related Pages

- [Organization Members](members.md) - View all members
- [Organization Manage Members](manage-members.md) - Bulk management
- [User Profile](../user/read.md) - User details

## Best Practices

1. **Easy Search**: Help find users quickly
2. **Clear Roles**: Explain permissions
3. **Validation**: Prevent duplicate members
4. **Confirmation**: Show success message
5. **Cancel Option**: Easy return to members
6. **Accessibility**: Keyboard navigation

## Extension Hooks

Extensions can modify add member by:
- Adding custom user search
- Adding custom roles
- Adding invitation workflow
- Adding approval process
- Adding bulk import
