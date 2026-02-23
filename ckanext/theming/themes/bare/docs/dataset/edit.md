# Dataset Edit Page

The form for editing existing datasets in CKAN.

## Overview

The dataset edit page provides:
- Pre-populated form with current values
- All metadata fields from create
- Delete option
- Version history access
- Resource management links

## URL Pattern

```
GET /dataset/edit/{id}
POST /dataset/edit/{id}
```

**Examples:**
```
<<vars.site_url>>/dataset/edit/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
<<vars.site_url>>/dataset/edit/annual-environmental-report
```

## Purpose

The edit page allows authorized users to:
- Modify dataset metadata
- Update resources
- Change categorization
- Update licensing information
- Delete dataset (if authorized)

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| Edit metadata | Modify dataset fields | Form inputs |
| Update resources | Add/edit/remove resources | Resource section |
| Change license | Update license | License dropdown |
| Delete dataset | Remove dataset | Delete button |
| View history | See changes | History link |
| View dataset | See public view | View link |
| Save changes | Update dataset | Submit button |
| Cancel | Discard changes | Cancel button |

## Template

**File:** `templates/package/edit.html`

### Template Structure

```jinja
{% extends "package/_edit_base.html" %}

{%- block subtitle -%}
    {{ ui.subtitle_item(_('Edit')) }}
{%- endblock -%}

{%- block content_action -%}
    {{ ui.content_action(ui.icon("eye") ~ _("View"), h.url_for(pkg_dict.type ~ ".read", id=pkg_dict.name)) if pkg_dict }}
{%- endblock -%}

{%- block primary_content_inner %}
    {{ ui.form(method="POST", enctype="multipart/form-data") }}
        {{ ui.form_errors(error_summary) }}
        {{ ui.package_basic_fields(data, errors) }}
        {{ ui.package_metadata_fields(data, errors) }}
        {{ ui.form_actions() }}
            {{ ui.submit(_('Update Dataset')) }}
        {{ ui.form_actions() }}
    {{ ui.form() }}

    {% if can_delete %}
        {{ ui.confirm_modal(_('Are you sure?'), form_id='delete-form') }}
        {{ ui.button(_('Delete'), style='danger', onclick='showModal()') }}
    {% endif %}
{%- endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `pkg_dict` | Current dataset data |
| `data` | Form data (pre-populated) |
| `errors` | Validation errors |
| `error_summary` | Error summary |
| `can_delete` | User can delete flag |
| `form_style` | 'edit' for edit mode |

### Delete Confirmation

```jinja
{%- set can_delete = form_style == 'edit' and h.check_access('package_delete', {'id': data.id}) -%}
{%- if can_delete -%}
    {%- set removal_form_id = ui.util.id() -%}
    {{ ui.form(method="POST", action=h.url_for(dataset_type ~ ".delete", id=data.id), attrs={"id": removal_form_id}) }}
        {{ ui.hidden_input(name='confirmed', value='1') }}
    {{ ui.form() }}
{%- endif -%}
```

## Screenshot Placeholder

![Dataset Edit](../screenshots/dataset-edit.png)

**What to show:**
- Full edit form with populated values
- All editable fields
- Delete button (if authorized)
- View link to public page
- Submit/cancel buttons

## Customization Notes

### Pre-populated Fields

All fields are pre-filled with current values:
```jinja
{{ ui.input(
    name='title',
    label=_('Title'),
    value=data.title,  # Pre-populated
    errors=errors.title
) }}
```

### Read-Only Fields

Make certain fields read-only:
```jinja
{{ ui.input(
    name='id',
    label=_('ID'),
    value=data.id,
    disabled=true
) }}
```

### Custom Field Display

Show/hide fields based on conditions:
```jinja
{% if h.check_access('admin_update') %}
    {{ ui.input(
        name='admin_field',
        label=_('Admin Field'),
        value=data.admin_field
    ) }}
{% endif %}
```

### Version Notes

Track changes with version notes:
```jinja
{% block version_notes %}
    {{ ui.textarea(
        name='version_notes',
        label=_('Change Notes'),
        placeholder=_('Describe your changes')
    ) }}
{% endblock %}
```

### Styling

Edit-specific styling:
```scss
.dataset-edit {
    .form-field {
        // Field styling
    }

    .delete-section {
        // Delete button area
    }

    .view-link {
        // View page link
    }
}
```

## Related Pages

- [Dataset Create](new.md) - Create new dataset
- [Dataset Read](read.md) - View dataset
- [Dataset History](history.md) - Version history
- [Dataset Delete](new.md) - Delete confirmation

## Best Practices

1. **Show Current Values**: Pre-populate all fields
2. **Change Indication**: Show what changed (if possible)
3. **Confirm Delete**: Require confirmation for deletion
4. **Preserve Drafts**: Save drafts automatically
5. **Clear Navigation**: Link to view/history pages
6. **Access Control**: Show appropriate options per user

## Extension Hooks

Extensions can modify edit form by:
- Adding/editing form fields
- Adding custom validation
- Modifying save behavior
- Adding preview functionality
- Adding workflow states
