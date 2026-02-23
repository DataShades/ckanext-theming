# Dataset Resources Management Page

Manage the resources (files, links, APIs) associated with a dataset.

## Overview

The resources page provides:
- List of all dataset resources
- Resource ordering (drag & drop)
- Add new resources
- Edit/delete existing resources
- Resource visibility controls

## URL Pattern

```
GET /dataset/resources/{id}
POST /dataset/resources/{id}
```

**Examples:**
```
<<vars.site_url>>/dataset/resources/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
<<vars.site_url>>/dataset/resources/annual-environmental-report
```

## Purpose

The resources page allows users to:
- View all dataset resources
- Reorder resources
- Add new resources
- Edit resource metadata
- Delete resources
- Set resource visibility

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| View resources | See resource list | Resource cards |
| Add resource | Create new resource | Add button |
| Edit resource | Modify resource | Edit button |
| Delete resource | Remove resource | Delete button |
| Reorder | Change resource order | Drag handles |
| Toggle visibility | Show/hide resource | Visibility toggle |
| Save order | Persist new order | Save button |

## Template

**File:** `templates/package/resources.html`

### Template Structure

```jinja
{% extends "package/_edit_base.html" %}

{%- set drag_id = ui.util.id() -%}
{%- set wrapper_id = ui.util.id() -%}

{%- block subtitle -%}
    {{ ui.subtitle_item(_('Resources')) }}
{%- endblock -%}

{%- block primary_content_inner %}
    <h2>{{ _('Resources') }}</h2>

    {% if resources %}
        <div id="{{ wrapper_id }}" data-drag="{{ drag_id }}">
            {% for resource in resources %}
                <div class="resource-item" data-id="{{ resource.id }}">
                    {{ ui.icon('drag-handle', class='drag-handle') }}

                    <div class="resource-info">
                        <h3>{{ ui.link(resource.name or _('Unnamed'), h.url_for('resource.read', id=pkg_dict.id, resource_id=resource.id)) }}</h3>
                        <p>{{ resource.description|truncate(100) }}</p>
                        <span class="format-badge">{{ resource.format }}</span>
                    </div>

                    <div class="resource-actions">
                        {{ ui.button(_('Edit'), href=h.url_for('resource.edit', id=pkg_dict.id, resource_id=resource.id)) }}
                        {{ ui.button(_('Delete'), style='danger', onclick='confirmDelete()') }}
                    </div>
                </div>
            {% endfor %}
        </div>

        {{ ui.button(_('Save order'), style='primary') }}
    {% else %}
        {{ ui.alert(_('This dataset has no resources yet'), style='info') }}
    {% endif %}

    {{ ui.button(_('Add Resource'), href=h.url_for('dataset.new_resource', id=pkg_dict.id), style='primary') }}
{% endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `pkg_dict` | Dataset dictionary |
| `resources` | List of resource objects |
| `resource_count` | Total resources |
| `can_add` | User can add resources flag |

### Resource Object

Each resource contains:
- `id` - Resource ID
- `name` - Resource name
- `description` - Resource description
- `format` - File format (CSV, PDF, etc.)
- `url` - Resource URL
- `size` - File size
- `created` - Creation date

## Screenshot Placeholder

![Dataset Resources](../screenshots/dataset-resources.png)

**What to show:**
- List of resource cards
- Drag handles for reordering
- Edit/delete buttons
- Add resource button
- Empty state (if no resources)

## Customization Notes

### Resource Display

Customize resource cards:
```jinja
{% block resource_item %}
    <div class="resource-card">
        <div class="resource-format">
            {{ ui.icon(h.resource_icon(resource.format)) }}
        </div>
        <div class="resource-details">
            <h4>{{ resource.name or _('Unnamed Resource') }}</h4>
            <p>{{ h.markdown_extract(resource.description, 50) }}</p>
            <div class="resource-meta">
                <span>{{ resource.format }}</span>
                <span>{{ h.size_or_link(resource.has_url, resource.size) }}</span>
            </div>
        </div>
        <div class="resource-actions">
            <!-- Actions here -->
        </div>
    </div>
{% endblock %}
```

### Drag and Drop

Implement reordering:
```javascript
// In assets/script.js
new Sortable(document.getElementById(wrapper_id), {
    handle: '.drag-handle',
    animation: 150,
    onEnd: function(evt) {
        // Save new order via AJAX
    }
});
```

### Add Resource

Multiple resource types:
```jinja
{% block add_resource %}
    <div class="add-resource">
        <h3>{{ _('Add Resource') }}</h3>
        <div class="resource-types">
            {{ ui.button(_('Upload File'), href=h.url_for('dataset.new_resource', id=pkg_dict.id)) }}
            {{ ui.button(_('Link to File'), href=h.url_for('dataset.new_resource', id=pkg_dict.id, type='link')) }}
            {{ ui.button(_('Link to API'), href=h.url_for('dataset.new_resource', id=pkg_dict.id, type='api')) }}
        </div>
    </div>
{% endblock %}
```

### Empty State

Customize empty state:
```jinja
{% block resources_empty %}
    <div class="empty-state">
        {{ ui.icon('file', size='large') }}
        <h3>{{ _('No Resources Yet') }}</h3>
        <p>{{ _('Add your first resource to share data') }}</p>
        {{ ui.button(_('Add Resource'), href=h.url_for('dataset.new_resource', id=pkg_dict.id), style='primary') }}
    </div>
{% endblock %}
```

### Styling

Resources-specific styling:
```scss
.dataset-resources {
    .resource-list {
        // List container
    }

    .resource-card {
        // Resource card
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 1rem;
        border: 1px solid #eee;
        border-radius: 4px;
        margin-bottom: 1rem;
    }

    .resource-format {
        // Format icon
        font-size: 2rem;
        color: #666;
    }

    .resource-actions {
        // Action buttons
        margin-left: auto;
        display: flex;
        gap: 0.5rem;
    }

    .drag-handle {
        // Drag cursor
        cursor: move;
    }
}
```

## Related Pages

- [Dataset Read](read.md) - View dataset with resources
- [Resource Read](../resource/read.md) - View individual resource
- [Resource Edit](../resource/edit.md) - Edit resource
- [Resource Views](../resource/views.md) - Manage resource views

## Best Practices

1. **Clear Format**: Show file format prominently
2. **Easy Reorder**: Make drag-and-drop intuitive
3. **Quick Actions**: Provide edit/delete access
4. **Empty State**: Guide users to add first resource
5. **Validation**: Validate resource URLs/files
6. **Feedback**: Show save confirmation

## Extension Hooks

Extensions can modify resources by:
- Adding custom resource types
- Adding resource preview
- Adding upload widgets
- Adding validation rules
- Adding metadata fields
