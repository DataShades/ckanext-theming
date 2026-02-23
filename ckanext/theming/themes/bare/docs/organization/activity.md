# Organization Activity Stream Page

View the activity stream for an organization.

## Overview

The activity page displays:
- Recent actions in the organization
- Dataset changes
- Member updates
- Organization modifications
- User activity feed

## URL Pattern

```
GET /organization/activity/{id}
GET /organization/activity/{id}?offset={number}
```

**Examples:**
```
<<vars.site_url>>/organization/activity/environmental-protection-agency
<<vars.site_url>>/organization/activity/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
<<vars.site_url>>/organization/activity/epa?offset=20
```

## Purpose

The activity page allows users to:
- Track organization changes
- Monitor dataset updates
- See member activity
- Follow organization timeline
- Understand organization evolution

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| View activity | See activity items | Activity list |
| Filter activity | Show specific types | Filter controls |
| Load more | Show older activity | Load more button |
| Subscribe | Follow organization | Follow button |
| Back to org | Return to main page | Back link |

## Template

**File:** `templates/organization/activity_stream.html`

### Template Structure

```jinja
{% extends "organization/_base.html" %}

{%- block subtitle -%}
    {{ ui.subtitle_item(_('Activity Stream')) }}
{%- endblock -%}

{%- block primary_content_inner %}
    <h2>{{ _('Activity Stream') }}</h2>

    {{ ui.activity_list(activities) }}
        {% for activity in activities %}
            {{ ui.activity(activity) }}
        {% endfor %}
    {{ ui.activity_list() }}

    {{ ui.pagination(
        page=page,
        total=total_count,
        href=h.url_for('organization.activity', id=group_dict.id, offset=offset)
    ) }}
{% endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `group_dict` | Organization dictionary |
| `activities` | List of activity objects |
| `page` | Current page number |
| `offset` | Current offset |
| `total_count` | Total activities |

### Activity Types

Common organization activity types:
- `new organization` - Organization created
- `changed organization` - Organization updated
- `new dataset` - Dataset added to org
- `changed dataset` - Dataset modified
- `deleted dataset` - Dataset removed
- `new member` - Member joined
- `changed member` - Member role changed
- `removed member` - Member left

## Screenshot Placeholder

![Organization Activity](../screenshots/organization-activity.png)

**What to show:**
- Activity feed/timeline
- User avatars/names
- Action descriptions
- Timestamps
- Pagination controls

## Customization Notes

### Activity Display

Customize activity rendering:
```jinja
{% block activity_item %}
    <div class="activity-item">
        <div class="activity-avatar">
            {{ ui.avatar(activity.user, size=50) }}
        </div>
        <div class="activity-content">
            <p class="activity-message">
                {{ activity.message|safe }}
            </p>
            <p class="activity-time">
                {{ h.time_ago_from_timestamp(activity.timestamp) }}
            </p>

            {% if activity.data and activity.data.dataset %}
                <div class="activity-dataset">
                    {{ ui.link(activity.data.dataset.title, h.url_for('dataset.read', id=activity.data.dataset.id)) }}
                </div>
            {% endif %}
        </div>
    </div>
{% endblock %}
```

### Activity Filters

Add filtering:
```jinja
{% block activity_filters %}
    <div class="activity-filters">
        {{ ui.button(_('All'), class='active', data-filter='all') }}
        {{ ui.button(_('Datasets'), data-filter='dataset') }}
        {{ ui.button(_('Members'), data-filter='member') }}
        {{ ui.button(_('Organization'), data-filter='organization') }}
    </div>
{% endblock %}
```

### Activity Icons

Map types to icons:
```jinja
{% set icons = {
    'new organization': 'building',
    'changed organization': 'edit',
    'new dataset': 'file-plus',
    'changed dataset': 'file-edit',
    'deleted dataset': 'trash',
    'new member': 'user-plus',
    'changed member': 'user-edit',
    'removed member': 'user-minus',
} %}

{{ ui.icon(icons.get(activity.activity_type, 'circle')) }}
```

### Styling

Activity-specific styling:
```scss
.organization-activity {
    .activity-list {
        // List container
    }

    .activity-item {
        // Individual activity
        display: flex;
        gap: 1rem;
        padding: 1rem;
        border-bottom: 1px solid #eee;

        &:hover {
            background: #f8f9fa;
        }
    }

    .activity-avatar {
        // User avatar
        flex-shrink: 0;
    }

    .activity-content {
        // Content area
        flex: 1;

        .activity-message {
            margin: 0 0 0.5rem 0;
        }

        .activity-time {
            color: #666;
            font-size: 0.875rem;
        }

        .activity-dataset {
            margin-top: 0.5rem;
            padding: 0.5rem;
            background: #f0f7ff;
            border-radius: 4px;
        }
    }

    .activity-filters {
        // Filter buttons
        display: flex;
        gap: 0.5rem;
        margin-bottom: 1.5rem;
    }
}
```

## Related Pages

- [Organization Read](read.md) - Main organization page
- [Organization Changes](changes.md) - Revision history
- [Dataset Activity](../dataset/activity.md) - Dataset activity
- [User Activity](../user/activity.md) - User activity

## Best Practices

1. **Clear Timeline**: Show activities chronologically
2. **User Attribution**: Show who did what
3. **Action Clarity**: Describe actions clearly
4. **Time Context**: Show when actions occurred
5. **Pagination**: Handle long activity lists
6. **Performance**: Load activities efficiently

## Extension Hooks

Extensions can modify activity by:
- Adding custom activity types
- Modifying activity messages
- Adding activity filters
- Adding activity notifications
- Adding export functionality
