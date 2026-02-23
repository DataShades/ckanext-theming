# Dataset Activity Stream Page

View the activity stream and recent changes for a dataset.

## Overview

The activity page displays:
- Recent actions on the dataset
- User activity feed
- Timestamps for each action
- Action types (create, update, delete, etc.)
- Links to related items

## URL Pattern

```
GET /dataset/activity/{id}
GET /dataset/activity/{id}?offset={number}
```

**Examples:**
```
<<vars.site_url>>/dataset/activity/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
<<vars.site_url>>/dataset/activity/annual-environmental-report
<<vars.site_url>>/dataset/activity/annual-environmental-report?offset=20
```

## Purpose

The activity page allows users to:
- Track recent changes to dataset
- See who made what changes
- Monitor dataset updates
- Follow activity timeline
- Understand dataset evolution

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| View activity | See activity items | Activity list |
| Filter activity | Show specific types | Filter controls |
| Load more | Show older activity | Load more button |
| Subscribe | Follow dataset activity | Follow button |
| Back to dataset | Return to main page | Back link |

## Template

**File:** `templates/package/activity_stream.html`

### Template Structure

```jinja
{% extends "package/_base.html" %}

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
        href=h.url_for('dataset.activity', id=pkg_dict.id, offset=offset)
    ) }}
{% endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `pkg_dict` | Dataset dictionary |
| `activities` | List of activity objects |
| `page` | Current page number |
| `offset` | Current offset |
| `total_count` | Total activities |

### Activity Object

Each activity contains:
- `id` - Activity ID
- `timestamp` - When it occurred
- `user_id` - Who did it
- `object_id` - Related object
- `activity_type` - Type of action
- `data` - Additional data

### Activity Types

Common activity types:
- `new package` - Dataset created
- `changed package` - Dataset updated
- `deleted package` - Dataset deleted
- `new resource` - Resource added
- `changed resource` - Resource updated
- `deleted resource` - Resource deleted

## Screenshot Placeholder

![Dataset Activity](../screenshots/dataset-activity.png)

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
        </div>
    </div>
{% endblock %}
```

### Activity Icons

Map activity types to icons:
```jinja
{% set icons = {
    'new package': 'plus',
    'changed package': 'edit',
    'deleted package': 'trash',
    'new resource': 'file',
    'changed resource': 'pencil',
} %}

{{ ui.icon(icons.get(activity.activity_type, 'circle')) }}
```

### Filter Controls

Add activity filtering:
```jinja
{% block activity_filters %}
    <div class="activity-filters">
        {{ ui.button(_('All'), class='active') }}
        {{ ui.button(_('Creates')) }}
        {{ ui.button(_('Updates')) }}
        {{ ui.button(_('Deletes')) }}
    </div>
{% endblock %}
```

### RSS Feed

Add activity feed subscription:
```jinja
{% block activity_feed_link %}
    {{ ui.link(
        _('RSS Feed'),
        h.url_for('dataset.activity', id=pkg_dict.id, format='rss'),
        icon='rss'
    ) }}
{% endblock %}
```

### Styling

Activity-specific styling:
```scss
.dataset-activity {
    .activity-list {
        // List container
    }

    .activity-item {
        // Individual activity
        display: flex;
        gap: 1rem;
        padding: 1rem;
        border-bottom: 1px solid #eee;
    }

    .activity-avatar {
        // User avatar
    }

    .activity-message {
        // Message text
    }

    .activity-time {
        // Timestamp styling
        color: #666;
        font-size: 0.875rem;
    }
}
```

## Related Pages

- [Dataset Read](read.md) - Main dataset view
- [Dataset History](history.md) - Version history
- [User Activity](../user/activity.md) - User activity stream
- [Organization Activity](../organization/activity.md) - Organization activity

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
