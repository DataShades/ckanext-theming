# Dataset Read Page

The main page for viewing dataset details, metadata, and resources.

## Overview

The dataset read page displays:
- Dataset title and description
- Metadata (author, license, tags, etc.)
- Resource list with downloads
- Social sharing options
- Follow/unfollow functionality
- Related information

## URL Pattern

```
GET /dataset/{id}
GET /dataset/{name}
```

**Examples:**
```
<<vars.site_url>>/dataset/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
<<vars.site_url>>/dataset/annual-environmental-report-2024
```

## Purpose

The read page is the primary view for dataset information. It should:
- Present all dataset metadata clearly
- Provide access to resources (downloads, APIs)
- Show related information and navigation
- Enable user interactions (follow, share)

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| View resource | Access resource data | Resource card/link |
| Download resource | Download resource file | Download button |
| Edit dataset | Modify dataset (if authorized) | Edit button |
| Delete dataset | Remove dataset (if authorized) | Delete button |
| Follow dataset | Subscribe to updates | Follow button |
| View history | See version history | History link |
| View activity | See activity stream | Activity link |
| Add to group | Associate with groups | Group links |
| Share dataset | Share via social media | Share links |

## Template

**File:** `templates/package/read.html`

### Template Structure

```jinja
{% extends "package/_base.html" %}

{%- block subtitle -%}
    {{ ui.subtitle_item(pkg_dict.title or pkg_dict.name) }}
{%- endblock -%}

{%- block primary_content_inner %}
    {{ ui.package_info(pkg_dict) }}
    {{ ui.resource_list(resources) }}
{%- endblock -%}

{%- block secondary_content %}
    {{ ui.package_social_info(pkg_dict) }}
    {{ ui.package_follow_button(pkg_dict) }}
{%- endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `pkg_dict` | Dataset metadata dictionary |
| `resources` | List of dataset resources |
| `tags` | Dataset tags |
| `groups` | Associated groups |
| `organization` | Owning organization |
| `license` | License information |
| `author` | Dataset author |
| `maintainer` | Dataset maintainer |

### Resource Display

Resources are displayed using:
```jinja
{% for resource in resources %}
    {{ ui.resource(resource) }}
{% endfor %}
```

## Screenshot Placeholder

![Dataset Read](../screenshots/dataset-read.png)

**What to show:**
- Full dataset view with title and description
- Metadata section (author, license, tags)
- Resource list with download options
- Sidebar with social/follow info
- Navigation breadcrumbs
- Action buttons (edit, delete, follow)

## Customization Notes

### Metadata Display

Customize which metadata fields to show:
```jinja
{% block package_info %}
    <dl class="metadata">
        <dt>{{ _('Title') }}</dt>
        <dd>{{ pkg_dict.title }}</dd>

        <dt>{{ _('Description') }}</dt>
        <dd>{{ h.render_markdown(pkg_dict.notes) }}</dd>

        <dt>{{ _('License') }}</dt>
        <dd>{{ ui.license(pkg_dict.license) }}</dd>
    </dl>
{% endblock %}
```

### Resource Ordering

Resources can be ordered:
```python
# In plugin or view
resources.sort(key=lambda r: r['position'])
```

### Custom Fields

Add custom metadata fields:
```jinja
{% block package_additional_info %}
    {{ super() }}
    {% for extra in pkg_dict.extras %}
        <tr>
            <td>{{ extra.key }}</td>
            <td>{{ extra.value }}</td>
        </tr>
    {% endfor %}
{% endblock %}
```

### Tags Display

Style and configure tags:
```jinja
{% block package_tags %}
    <div class="tags">
        {% for tag in pkg_dict.tags %}
            {{ ui.tag(tag.name, href=h.url_for('dataset.search', tags=tag.name)) }}
        {% endfor %}
    </div>
{% endblock %}
```

### Social Sharing

Add social sharing buttons:
```jinja
{% block package_social %}
    <div class="social-share">
        {{ ui.link(_('Tweet'), 'https://twitter.com/share?url=' ~ h.full_current_url()) }}
        {{ ui.link(_('Share on Facebook'), 'https://www.facebook.com/sharer.php?u=' ~ h.full_current_url()) }}
    </div>
{% endblock %}
```

### Styling

Key areas to style:
```scss
.dataset-read {
    .dataset-heading {
        // Title styling
    }

    .dataset-notes {
        // Description styling
    }

    .resource-list {
        // Resource cards
    }

    .metadata {
        // Metadata table/list
    }

    .tags {
        // Tag styling
    }
}
```

## Related Pages

- [Dataset Search](search.md) - Browse/search datasets
- [Dataset Edit](edit.md) - Modify dataset
- [Resource Read](../resource/read.md) - View individual resource
- [Dataset History](history.md) - Version history

## Best Practices

1. **Clear Hierarchy**: Organize information logically
2. **Prominent Resources**: Make downloads easily accessible
3. **Metadata Visibility**: Show important metadata clearly
4. **Action Buttons**: Place actions where users expect them
5. **Responsive Design**: Ensure mobile compatibility
6. **Accessibility**: Use semantic HTML and ARIA labels

## Extension Hooks

Extensions can modify read page by:
- Adding custom metadata sections
- Adding resource preview widgets
- Adding download statistics
- Adding related datasets section
- Adding custom action buttons
- Modifying resource display
