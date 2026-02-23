# Organization Administrators Page

View the list of administrators for an organization.

## Overview

The administrators page displays:
- List of users with admin role
- Admin count
- Admin permissions
- Contact information

## URL Pattern

```
GET /organization/admins/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/admins/environmental-protection-agency
<<vars.site_url>>/organization/admins/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The administrators page allows users to:
- See who manages the organization
- Identify decision makers
- Contact administrators
- Understand admin structure

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| View admins | See admin list | Admin cards |
| Contact admin | Reach out | Contact links |
| View profile | Navigate to user | User link |
| Add admin | Promote to admin | Promote button |

## Template

**File:** `templates/organization/admins.html`

### Template Structure

```jinja
{% extends "organization/_edit_base.html" %}

{%- block subtitle -%}
    {{ ui.subtitle_item(_('Administrators')) }}
{%- endblock -%}

{%- block primary_content_inner %}
    <h2>{{ _('Administrators') }}</h2>

    {% if admins %}
        {{ ui.grid() }}
            {% for admin in admins %}
                {{ ui.column(span={"xs": 12, "md": 6, "lg": 4}) }}
                    <div class="admin-card">
                        {{ ui.avatar(admin.user_id, size=80) }}

                        <h3>{{ ui.link(admin.user_name, h.url_for('user.read', id=admin.user_id)) }}</h3>

                        {% if admin.email %}
                            <p>{{ ui.icon('envelope') }} {{ ui.link(admin.email, 'mailto:' ~ admin.email) }}</p>
                        {% endif %}

                        <div class="admin-meta">
                            <span>{{ _('Admin since') }} {{ h.render_datetime(admin.created) }}</span>
                        </div>

                        <div class="admin-actions">
                            {{ ui.button(_('View Profile'), href=h.url_for('user.read', id=admin.user_id)) }}
                        </div>
                    </div>
                {{ ui.column() }}
            {% endfor %}
        {{ ui.grid() }}
    {% else %}
        {{ ui.alert(_('This organization has no administrators yet'), style='info') }}
    {% endif %}
{%- endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `group_dict` | Organization dictionary |
| `admins` | List of admin members |
| `admin_count` | Total administrators |

## Screenshot Placeholder

![Organization Administrators](../screenshots/organization-admins.png)

**What to show:**
- Grid of admin cards
- User avatars
- Contact information
- Admin since date
- Empty state (if no admins)

## Customization Notes

### Admin Cards

Customize admin display:
```jinja
{% block admin_card %}
    <div class="admin-card">
        <div class="admin-header">
            {{ ui.avatar(admin.user_id, size=100) }}
            <span class="admin-badge">{{ ui.icon('shield') }} {{ _('Admin') }}</span>
        </div>

        <div class="admin-body">
            <h3>{{ ui.link(admin.display_name, h.url_for('user.read', id=admin.user_id)) }}</h3>

            {% if admin.bio %}
                <p>{{ h.markdown_extract(admin.bio, 100) }}</p>
            {% endif %}

            <ul class="admin-contact">
                {% if admin.email %}
                    <li>{{ ui.icon('envelope') }} {{ admin.email }}</li>
                {% endif %}
            </ul>
        </div>

        <div class="admin-footer">
            <small>{{ _('Member since') }} {{ h.render_datetime(admin.created) }}</small>
        </div>
    </div>
{% endblock %}
```

### Admin Badge

Style admin indicator:
```jinja
{% block admin_badge %}
    <span class="admin-badge">
        {{ ui.icon('crown', size='large') }}
        <span>{{ _('Administrator') }}</span>
    </span>
{% endblock %}
```

### Empty State

No admins message:
```jinja
{% block admins_empty %}
    <div class="empty-state">
        {{ ui.icon('shield', size='large') }}
        <h3>{{ _('No Administrators') }}</h3>
        <p>{{ _('This organization has no administrators yet') }}</p>
        {% if h.check_access('organization_member_create', {'id': group_dict.id}) %}
            {{ ui.button(_('Add Administrator'), href=h.url_for('organization.member_new', id=group_dict.id), style='primary') }}
        {% endif %}
    </div>
{% endblock %}
```

### Styling

Admins-specific styling:
```scss
.organization-admins {
    .admin-grid {
        // Grid layout
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 1.5rem;
    }

    .admin-card {
        // Card styling
        border: 1px solid #eee;
        border-radius: 8px;
        overflow: hidden;
        text-align: center;

        &:hover {
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
    }

    .admin-header {
        // Card header
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 1rem;
        position: relative;
    }

    .admin-badge {
        // Badge styling
        position: absolute;
        top: 1rem;
        right: 1rem;
        background: rgba(255,255,255,0.9);
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
    }

    .admin-body {
        // Card body
        padding: 1.5rem;
    }

    .admin-contact {
        // Contact list
        list-style: none;
        padding: 0;
        margin: 1rem 0;

        li {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            justify-content: center;
        }
    }

    .empty-state {
        // No admins state
        text-align: center;
        padding: 3rem;
    }
}
```

## Related Pages

- [Organization Members](members.md) - All members
- [Organization Manage Members](manage-members.md) - Bulk management
- [Add Member](member-new.md) - Add new member
- [User Profile](../user/read.md) - User details

## Best Practices

1. **Clear Identity**: Show admin status
2. **Contact Info**: Make admins reachable
3. **Visual Distinction**: Differentiate from members
4. **Empty State**: Guide to add first admin
5. **Responsive Grid**: Mobile-friendly layout
6. **Accessibility**: Proper semantic markup

## Extension Hooks

Extensions can modify admins by:
- Adding admin metadata
- Adding admin hierarchy
- Adding contact widgets
- Adding admin analytics
- Adding approval workflows
