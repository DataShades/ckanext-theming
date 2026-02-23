# Dataset Resource Views Page

Manage the visualizations and views for dataset resources.

## Overview

The resource views page provides:
- List of configured views for a resource
- View type selection (grid, graph, map, etc.)
- View configuration options
- View ordering and visibility

## URL Pattern

```
GET /dataset/{id}/resource/{resource_id}/views
GET /dataset/{id}/resource/{resource_id}/views/new
POST /dataset/{id}/resource/{resource_id}/views
```

**Examples:**
```
<<vars.site_url>>/dataset/annual-report/resource/abc123/views
<<vars.site_url>>/dataset/annual-report/resource/abc123/views/new
```

## Purpose

The views page allows users to:
- Create visualizations for resources
- Configure view types and options
- Reorder views
- Enable/disable views
- Preview views before saving

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| View list | See existing views | View cards |
| Add view | Create new view | Add button |
| Edit view | Modify view config | Edit button |
| Delete view | Remove view | Delete button |
| Reorder | Change view order | Drag handles |
| Preview | Test view | Preview button |
| Toggle visibility | Show/hide view | Visibility toggle |

## Template

**File:** `templates/package/new_view.html`

### Template Structure

```jinja
{% extends "package/_resource_edit_base.html" %}

{%- block subtitle -%}
    {{ ui.subtitle_item(_('Edit view') if resource_view.id else _('Add view')) }}
{%- endblock -%}

{%- block primary_content_inner %}
    {% if resource_view %}
        <!-- Edit existing view -->
        {{ ui.form(method="POST") }}
            {{ ui.form_errors(error_summary) }}
            {{ ui.input(name='title', label=_('Title'), value=resource_view.title) }}
            {{ ui.select(name='view_type', label=_('Type'), options=view_types) }}
            {{ ui.textarea(name='description', label=_('Description'), value=resource_view.description) }}
            <!-- View-specific config fields -->
            {{ ui.form_actions() }}
                {{ ui.submit(_('Save')) }}
            {{ ui.form_actions() }}
        {{ ui.form() }}
    {% else %}
        <!-- View type selection -->
        <h2>{{ _('Add View') }}</h2>
        {{ ui.grid() }}
            {% for view_type in available_views %}
                {{ ui.column(span={"xs": 12, "md": 6}) }}
                    <div class="view-type-card">
                        {{ ui.icon(view_type.icon, size='large') }}
                        <h3>{{ view_type.title }}</h3>
                        <p>{{ view_type.description }}</p>
                        {{ ui.button(_('Select'), href=h.url_for('dataset_resource.new_view', id=pkg_dict.id, resource_id=resource.id, view_type=view_type.type)) }}
                    </div>
                {{ ui.column() }}
            {% endfor %}
        {{ ui.grid() }}
    {% endif %}
{% endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `pkg_dict` | Dataset dictionary |
| `resource` | Resource object |
| `resource_view` | Current view object (if editing) |
| `view_types` | Available view types |
| `available_views` | Views for selection |
| `error_summary` | Validation errors |

### View Types

Common view types:
- `image_view` - Display image
- `recline_view` - Data grid/table
- `recline_graph_view` - Charts/graphs
- `recline_map_view` - Geographic maps
- `datatables_view` - Sortable tables
- `webpage_view` - Embed web pages
- `pdf_view` - PDF viewer

## Screenshot Placeholder

![Resource Views](../screenshots/resource-views.png)

**What to show:**
- View type selection grid
- View configuration form
- Preview area
- Save/cancel buttons

## Customization Notes

### View Type Cards

Customize view selection:
```jinja
{% block view_type_card %}
    <div class="view-type-card">
        <div class="view-icon">
            {{ ui.icon(view_type.icon, size='4x') }}
        </div>
        <h3>{{ view_type.title }}</h3>
        <p>{{ view_type.description }}</p>
        <ul class="view-features">
            {% for feature in view_type.features %}
                <li>{{ feature }}</li>
            {% endfor %}
        </ul>
        {{ ui.button(_('Select'), style='primary') }}
    </div>
{% endblock %}
```

### View Configuration

Dynamic config fields:
```jinja
{% block view_config %}
    {% if view_type == 'recline_graph_view' %}
        {{ ui.select(name='graph_type', label=_('Graph Type'), options=graph_types) }}
        {{ ui.input(name='x_axis', label=_('X Axis'), value=config.x_axis) }}
        {{ ui.input(name='y_axis', label=_('Y Axis'), value=config.y_axis) }}
        {{ ui.checkbox(name='show_legend', label=_('Show Legend'), checked=config.show_legend) }}
    {% elif view_type == 'recline_map_view' %}
        {{ ui.select(name='map_field', label=_('Location Field'), options=fields) }}
        {{ ui.input(name='latitude_field', label=_('Latitude'), value=config.lat_field) }}
        {{ ui.input(name='longitude_field', label=_('Longitude'), value=config.lon_field) }}
    {% endif %}
{% endblock %}
```

### Preview Area

Live preview:
```jinja
{% block view_preview %}
    <div class="view-preview">
        <h3>{{ _('Preview') }}</h3>
        <div id="preview-container">
            <!-- Preview rendered here -->
        </div>
        {{ ui.button(_('Refresh Preview'), onclick='refreshPreview()') }}
    </div>
{% endblock %}
```

### View Ordering

Implement reordering:
```jinja
{% block view_list %}
    <div class="view-list" data-sortable="true">
        {% for view in views %}
            <div class="view-item" data-id="{{ view.id }}">
                {{ ui.icon('drag-handle', class='drag-handle') }}
                <span class="view-title">{{ view.title }}</span>
                <span class="view-type">{{ view.view_type }}</span>
                <div class="view-actions">
                    {{ ui.button(_('Edit'), href=h.url_for('dataset_resource.edit_view', id=pkg_dict.id, resource_id=resource.id, view_id=view.id)) }}
                    {{ ui.button(_('Delete'), style='danger') }}
                </div>
            </div>
        {% endfor %}
    </div>
{% endblock %}
```

### Styling

Views-specific styling:
```scss
.resource-views {
    .view-type-card {
        // View type selection
        border: 2px solid #eee;
        border-radius: 8px;
        padding: 2rem;
        text-align: center;
        transition: border-color 0.3s;

        &:hover {
            border-color: var(--primary-color);
        }
    }

    .view-icon {
        // Icon container
        margin-bottom: 1rem;
    }

    .view-preview {
        // Preview area
        border: 1px solid #ddd;
        border-radius: 4px;
        padding: 1rem;
        margin-top: 1rem;
    }

    .view-list {
        // View ordering list
    }

    .view-item {
        // Individual view
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 0.75rem;
        border: 1px solid #eee;
        margin-bottom: 0.5rem;
    }
}
```

## Related Pages

- [Resource Read](../resource/read.md) - View resource with views
- [Resource Edit](../resource/edit.md) - Edit resource metadata
- [Dataset Resources](resources.md) - Manage dataset resources

## Best Practices

1. **Clear Types**: Show view type capabilities
2. **Live Preview**: Allow testing before saving
3. **Easy Config**: Simplify configuration
4. **Ordering**: Allow view reordering
5. **Defaults**: Provide sensible defaults
6. **Validation**: Validate view configuration

## Extension Hooks

Extensions can modify views by:
- Adding custom view types
- Adding view templates
- Adding preview enhancements
- Adding export options
- Adding embed capabilities
