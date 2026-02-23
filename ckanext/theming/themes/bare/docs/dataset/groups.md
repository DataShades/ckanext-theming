# Dataset Groups Page

View and manage the groups associated with a dataset.

## Overview

The groups page displays:
- Groups the dataset belongs to
- Group descriptions and images
- Add/remove group associations
- Group browsing

## URL Pattern

```
GET /dataset/groups/{id}
```

**Examples:**
```
<<vars.site_url>>/dataset/groups/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
<<vars.site_url>>/dataset/groups/annual-environmental-report
```

## Purpose

The groups page allows users to:
- See which groups contain this dataset
- Browse related thematic collections
- Add dataset to groups (if authorized)
- Remove dataset from groups (if authorized)

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| View groups | See group list | Group cards |
| Add to group | Associate with group | Add button |
| Remove from group | Disassociate | Remove button |
| View group | Navigate to group | Group link |
| Back to dataset | Return to main page | Back link |

## Template

**File:** `templates/package/group_list.html`

### Template Structure

```jinja
{% extends "package/_base.html" %}

{% set default_group_type = h.default_group_type('group') %}
{%- set page_title = h.humanize_entity_type('group', default_group_type, 'page title') or _('Groups') -%}

{%- block subtitle -%}
    {{ ui.subtitle_item(page_title) }}
{%- endblock -%}

{%- block primary_content_inner %}
    <h2>{{ page_title }}</h2>

    {% if groups %}
        {{ ui.grid() }}
            {% for group in groups %}
                {{ ui.column(span={"xs": 12, "md": 6, "lg": 4}) }}
                    {{ ui.group(group) }}
                {{ ui.column() }}
            {% endfor %}
        {{ ui.grid() }}
    {% else %}
        {{ ui.alert(_('This dataset is not in any groups yet'), style='info') }}
    {% endif %}

    {% if h.check_access('package_update', {'id': pkg_dict.id}) %}
        {{ ui.button(_('Add to group'), href=h.url_for('group.new')) }}
    {% endif %}
{% endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `pkg_dict` | Dataset dictionary |
| `groups` | List of group objects |
| `group_count` | Total group count |
| `default_group_type` | Group type identifier |

### Group Object

Each group contains:
- `id` - Group ID
- `name` - Group name
- `title` - Display title
- `description` - Group description
- `image_url` - Group image
- `package_count` - Dataset count

## Screenshot Placeholder

![Dataset Groups](../screenshots/dataset-groups.png)

**What to show:**
- Grid of group cards
- Group images and descriptions
- Add/remove buttons
- Empty state (if no groups)

## Customization Notes

### Group Display

Customize group cards:
```jinja
{% block group_item %}
    <div class="group-card">
        <div class="group-image">
            {% if group.image_url %}
                {{ ui.image(group.image_url, alt=group.title) }}
            {% else %}
                {{ ui.image('/images/placeholder-group.png', alt=group.title) }}
            {% endif %}
        </div>
        <div class="group-info">
            <h3>{{ ui.link(group.title or group.name, h.url_for('group.read', id=group.name)) }}</h3>
            <p>{{ h.markdown_extract(group.description, 100) }}</p>
            <span class="dataset-count">{{ group.package_count }} datasets</span>
        </div>
    </div>
{% endblock %}
```

### Add to Group

Implement add functionality:
```jinja
{% block add_to_group %}
    {{ ui.dropdown(label=_('Add to group')) }}
        {% for group in available_groups %}
            {{ ui.form(method='POST', action=h.url_for('dataset.group_add', id=pkg_dict.id)) }}
                {{ ui.hidden_input(name='group', value=group.id) }}
                {{ ui.submit(group.title) }}
            {{ ui.form() }}
        {% endfor %}
    {{ ui.dropdown() }}
{% endblock %}
```

### Remove from Group

Implement remove functionality:
```jinja
{% block remove_button %}
    {{ ui.form(
        method='POST',
        action=h.url_for('group.dataset_remove', id=group.id, dataset=pkg_dict.id)
    ) }}
        {{ ui.hidden_input(name='confirmed', value='1') }}
        {{ ui.button(_('Remove'), style='danger', type='submit') }}
    {{ ui.form() }}
{% endblock %}
```

### Empty State

Customize empty state:
```jinja
{% block groups_empty %}
    <div class="empty-state">
        {{ ui.icon('users', size='large') }}
        <h3>{{ _('No Groups') }}</h3>
        <p>{{ _('This dataset is not in any groups yet') }}</p>
        {% if h.check_access('package_update') %}
            {{ ui.button(_('Add to Group'), href='#') }}
        {% endif %}
    </div>
{% endblock %}
```

### Styling

Groups-specific styling:
```scss
.dataset-groups {
    .group-grid {
        // Grid layout
    }

    .group-card {
        // Group card styling
        border: 1px solid #eee;
        border-radius: 4px;
        overflow: hidden;
        margin-bottom: 1.5rem;
    }

    .group-image {
        // Image container
        height: 200px;
        object-fit: cover;
    }

    .group-info {
        // Group details
        padding: 1rem;
    }

    .empty-state {
        // No groups state
        text-align: center;
        padding: 3rem;
    }
}
```

## Related Pages

- [Dataset Read](read.md) - Main dataset view
- [Group Index](../group/index.md) - Browse all groups
- [Group Read](../group/read.md) - View individual group
- [Organization Read](../organization/read.md) - View organization

## Best Practices

1. **Visual Cards**: Use images for groups
2. **Clear Actions**: Make add/remove obvious
3. **Descriptions**: Show group purpose
4. **Empty State**: Handle no groups gracefully
5. **Permissions**: Show actions based on access
6. **Navigation**: Easy access to group pages

## Extension Hooks

Extensions can modify groups by:
- Adding custom group types
- Adding group metadata
- Adding bulk operations
- Adding group suggestions
- Adding group analytics
