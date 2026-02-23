# Dataset Followers Page

View the list of users following a dataset.

## Overview

The followers page displays:
- List of users following the dataset
- User profiles and avatars
- Follow count
- Follow/unfollow functionality

## URL Pattern

```
GET /dataset/followers/{id}
```

**Examples:**
```
<<vars.site_url>>/dataset/followers/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
<<vars.site_url>>/dataset/followers/annual-environmental-report
```

## Purpose

The followers page allows users to:
- See who is following the dataset
- Understand dataset popularity
- Connect with interested users
- Follow/unfollow the dataset

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| View followers | See follower list | User list |
| Follow dataset | Subscribe to updates | Follow button |
| Unfollow dataset | Stop following | Unfollow button |
| View user profile | Navigate to user | User link |
| Back to dataset | Return to main page | Back link |

## Template

**File:** `templates/package/followers.html`

### Template Structure

```jinja
{% extends "package/_base.html" %}

{%- block subtitle -%}
    {{ ui.subtitle_item(_("Followers")) }}
{%- endblock -%}

{%- block primary_content_inner %}
    <h2>{{ _('Followers') }}</h2>

    {% if followers %}
        {{ ui.list() }}
            {% for user in followers %}
                {{ ui.list_item() }}
                    {{ ui.avatar(user, size=50) }}
                    {{ ui.link(user.display_name, h.url_for('user.read', id=user.name)) }}
            {% endfor %}
        {{ ui.list() }}
    {% else %}
        {{ ui.alert(_('No one is following this dataset yet'), style='info') }}
    {% endif %}
{% endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `pkg_dict` | Dataset dictionary |
| `followers` | List of follower objects |
| `follower_count` | Total follower count |
| `am_following` | Current user follows flag |

### Follower Object

Each follower contains:
- `id` - User ID
- `name` - Username
- `display_name` - Display name
- `image_url` - Avatar URL

## Screenshot Placeholder

![Dataset Followers](../screenshots/dataset-followers.png)

**What to show:**
- List of followers with avatars
- Follow/unfollow button
- Follower count
- Empty state (if no followers)

## Customization Notes

### Follower Display

Customize follower list:
```jinja
{% block follower_item %}
    <div class="follower-card">
        {{ ui.avatar(follower, size=60) }}
        <div class="follower-info">
            <h4>{{ ui.link(follower.display_name, h.url_for('user.read', id=follower.name)) }}</h4>
            <p>{{ follower.email if h.check_access('user_show') }}</p>
        </div>
    </div>
{% endblock %}
```

### Follow Button

Implement follow functionality:
```jinja
{% block follow_button %}
    {% if am_following %}
        {{ ui.button(
            _('Unfollow'),
            style='danger',
            hx={
                'post': h.url_for('dataset.unfollow', id=pkg_dict.id),
                'target': '#follow-section',
                'swap': 'outerHTML'
            }
        ) }}
    {% else %}
        {{ ui.button(
            _('Follow'),
            style='primary',
            hx={
                'post': h.url_for('dataset.follow', id=pkg_dict.id),
                'target': '#follow-section',
                'swap': 'outerHTML'
            }
        ) }}
    {% endif %}
{% endblock %}
```

### Empty State

Customize empty state:
```jinja
{% block followers_empty %}
    <div class="empty-state">
        {{ ui.icon('users', size='large') }}
        <h3>{{ _('No Followers Yet') }}</h3>
        <p>{{ _('Be the first to follow this dataset!') }}</p>
        {{ ui.button(_('Follow Now'), style='primary') }}
    </div>
{% endblock %}
```

### Sorting/Filtering

Add follower sorting:
```jinja
{% block follower_filters %}
    <div class="follower-filters">
        {{ ui.select(
            name='sort',
            options=[
                {'value': 'recent', 'text': _('Most Recent')},
                {'value': 'alphabetical', 'text': _('Alphabetical')}
            ]
        ) }}
    </div>
{% endblock %}
```

### Styling

Followers-specific styling:
```scss
.dataset-followers {
    .follower-list {
        // List container
    }

    .follower-card {
        // Individual follower
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 1rem;
        border: 1px solid #eee;
        border-radius: 4px;
        margin-bottom: 1rem;
    }

    .follower-info {
        // Follower details
    }

    .empty-state {
        // No followers state
        text-align: center;
        padding: 3rem;
    }
}
```

## Related Pages

- [Dataset Read](read.md) - Main dataset view
- [User Profile](../user/read.md) - User profile page
- [Dataset Activity](activity.md) - Activity stream
- [Organization Followers](../organization/followers.md) - Organization followers

## Best Practices

1. **Clear List**: Display followers prominently
2. **User Avatars**: Show profile pictures
3. **Easy Follow**: Make follow action simple
4. **Empty State**: Handle zero followers gracefully
5. **Privacy**: Respect user privacy settings
6. **Performance**: Paginate large follower lists

## Extension Hooks

Extensions can modify followers by:
- Adding follower statistics
- Adding follower notifications
- Adding bulk follow options
- Adding follower export
- Adding follower analytics
