# User Profile Page

View a user's public profile and activity.

## Overview

The user profile page displays:
- User information (name, bio, etc.)
- User statistics
- Recent activity
- Social links
- Follow functionality

## URL Pattern

```
GET /user/{id}
GET /user/{name}
```

**Examples:**
```
<<vars.site_url>>/user/john-doe
<<vars.site_url>>/user/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The profile page allows users to:
- View user information
- See user's public activity
- Follow/unfollow user
- Contact user (if enabled)
- Navigate to user's content

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| View info | Read user details | Profile section |
| Follow | Subscribe to updates | Follow button |
| View activity | See activity feed | Activity link |
| View datasets | See user's datasets | Datasets link |
| View organizations | See user's orgs | Organizations link |
| Edit profile | Modify profile (self) | Edit button |

## Template

**File:** `templates/user/read.html`

### Template Structure

```jinja
{% extends "user/_base.html" %}

{%- block page_action -%}
    {{ ui.page_action(_('Add Dataset'), href=h.url_for('dataset.new')) if h.check_access('package_create') }}
{%- endblock -%}

{%- block subtitle -%}
    {{ ui.subtitle_item(user_dict.display_name) }}
{%- endblock -%}

{%- block primary_content_inner %}
    {{ ui.user_info(user_dict) }}

    <h3>{{ _('Recent Activity') }}</h3>
    {{ ui.activity_list(activities) }}
        {% for activity in activities %}
            {{ ui.activity(activity) }}
        {% endfor %}
    {{ ui.activity_list() }}
{%- endblock -%}

{%- block secondary_content %}
    {{ ui.card(title=_('User Info')) }}
        <dl>
            <dt>{{ _('Username') }}</dt>
            <dd>{{ user_dict.name }}</dd>

            <dt>{{ _('Member since') }}</dt>
            <dd>{{ h.render_datetime(user_dict.created) }}</dd>

            <dt>{{ _('Followers') }}</dt>
            <dd>{{ follower_count }}</dd>

            <dt>{{ _('Following') }}</dt>
            <dd>{{ following_count }}</dd>
        </dl>

        {% if is_myself or am_following %}
            {{ ui.follow_button(user_dict, am_following) }}
        {% endif %}
    {{ ui.card() }}
{%- endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `user_dict` | User data dictionary |
| `is_myself` | Viewing own profile flag |
| `am_following` | Current user follows flag |
| `follower_count` | Number of followers |
| `following_count` | Number following |
| `activities` | Recent activity items |

## Screenshot Placeholder

![User Profile](../screenshots/user-profile.png)

**What to show:**
- User avatar/header
- Profile information
- Statistics (followers, following, etc.)
- Recent activity feed
- Follow/edit button
- Navigation to user's content

## Customization Notes

### User Information

Customize profile display:
```jinja
{% block user_info %}
    <div class="user-profile">
        <div class="user-avatar">
            {{ ui.avatar(user_dict, size=150) }}
        </div>

        <div class="user-details">
            <h1>{{ user_dict.display_name }}</h1>

            {% if user_dict.about %}
                <div class="user-bio">
                    {{ h.render_markdown(user_dict.about) }}
                </div>
            {% endif %}

            <div class="user-meta">
                {% if user_dict.email %}
                    <span>{{ ui.icon('envelope') }} {{ user_dict.email }}</span>
                {% endif %}

                {% if user_dict.created %}
                    <span>{{ ui.icon('calendar') }} {{ _('Joined') }} {{ h.time_ago_from_timestamp(user_dict.created) }}</span>
                {% endif %}
            </div>
        </div>
    </div>
{% endblock %}
```

### Statistics

Display user stats:
```jinja
{% block user_stats %}
    <div class="user-stats">
        <div class="stat-item">
            <span class="stat-value">{{ user_dict.number_created_packages }}</span>
            <span class="stat-label">{{ _('Datasets') }}</span>
        </div>

        <div class="stat-item">
            <span class="stat-value">{{ follower_count }}</span>
            <span class="stat-label">{{ _('Followers') }}</span>
        </div>

        <div class="stat-item">
            <span class="stat-value">{{ following_count }}</span>
            <span class="stat-label">{{ _('Following') }}</span>
        </div>
    </div>
{% endblock %}
```

### Follow Button

Implement follow functionality:
```jinja
{% block follow_button %}
    {% if not is_myself %}
        {% if am_following %}
            {{ ui.button(
                _('Unfollow'),
                style='danger',
                hx={
                    'post': h.url_for('user.unfollow', id=user_dict.id),
                    'target': '#follow-section',
                    'swap': 'outerHTML'
                }
            ) }}
        {% else %}
            {{ ui.button(
                _('Follow'),
                style='primary',
                hx={
                    'post': h.url_for('user.follow', id=user_dict.id),
                    'target': '#follow-section',
                    'swap': 'outerHTML'
                }
            ) }}
        {% endif %}
    {% endif %}
{% endblock %}
```

### Styling

Profile-specific styling:
```scss
.user-read {
    .user-profile {
        // Profile header
        display: flex;
        gap: 2rem;
        margin-bottom: 2rem;
        padding-bottom: 2rem;
        border-bottom: 1px solid #eee;
    }

    .user-avatar {
        // Avatar image
        flex-shrink: 0;
    }

    .user-details {
        // User info
        flex: 1;

        .user-bio {
            margin: 1rem 0;
            line-height: 1.6;
        }

        .user-meta {
            display: flex;
            gap: 1.5rem;
            color: #666;
            font-size: 0.875rem;
        }
    }

    .user-stats {
        // Statistics
        display: flex;
        gap: 2rem;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 4px;

        .stat-item {
            text-align: center;

            .stat-value {
                display: block;
                font-size: 1.5rem;
                font-weight: 600;
            }

            .stat-label {
                font-size: 0.875rem;
                color: #666;
            }
        }
    }
}
```

## Related Pages

- [Edit Profile](edit.md) - Modify profile
- [User Activity](activity.md) - Activity stream
- [User Followers](followers.md) - Follower list
- [Dashboard](../dashboard/dashboard.md) - Personal dashboard

## Best Practices

1. **Clear Identity**: Show user avatar and name
2. **Activity Feed**: Display recent actions
3. **Statistics**: Show contribution metrics
4. **Social Features**: Enable follow/contact
5. **Privacy**: Respect privacy settings
6. **Responsive**: Mobile-friendly layout

## Extension Hooks

Extensions can modify profile by:
- Adding custom user fields
- Adding user badges/achievements
- Adding contact widgets
- Adding user analytics
- Adding social media links
