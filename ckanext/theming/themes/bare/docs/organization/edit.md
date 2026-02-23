# Organization Edit Page

Form for editing existing organizations in CKAN.

## Overview

The organization edit page provides:
- Pre-populated form with current values
- All organization fields
- Image upload/replace
- Delete option
- Custom field support

## URL Pattern

```
GET /organization/edit/{id}
POST /organization/edit/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/edit/environmental-protection-agency
<<vars.site_url>>/organization/edit/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The edit page allows authorized users to:
- Modify organization details
- Update logo/image
- Change contact information
- Update custom metadata
- Delete organization (if authorized)

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| Edit details | Modify org fields | Form inputs |
| Update image | Change logo | Image upload |
| Delete org | Remove organization | Delete button |
| View org | See public view | View link |
| Save changes | Update organization | Submit button |
| Cancel | Discard changes | Cancel button |

## Template

**File:** `templates/organization/edit.html`

### Template Structure

```jinja
{% extends "organization/_edit_base.html" %}

{%- block subtitle -%}
    {{ ui.subtitle_item(_('Edit')) }}
{%- endblock -%}

{%- block content_action -%}
    {{ ui.content_action(_('View'), h.url_for('organization.read', id=group_dict.name)) if group_dict }}
{%- endblock -%}

{%- block primary_content_inner %}
    {{ ui.form(method="POST", enctype="multipart/form-data") }}
        {{ ui.form_errors(error_summary) }}

        {{ ui.input(
            name='title',
            label=_('Title'),
            value=data.title,
            errors=errors.title
        ) }}

        {{ ui.input(
            name='name',
            label=_('URL'),
            value=data.name,
            errors=errors.name
        ) }}

        {{ ui.textarea(
            name='description',
            label=_('Description'),
            value=data.description,
            errors=errors.description
        ) }}

        {{ ui.image_upload(
            name='image_upload',
            label=_('Logo'),
            value=data.image_url,
            errors=errors.image_url
        ) }}

        {{ ui.input(
            name='email',
            label=_('Email'),
            type='email',
            value=data.email,
            errors=errors.email
        ) }}

        {{ ui.form_actions() }}
            {{ ui.submit(_('Update Organization')) }}
            {{ ui.button(_('Cancel'), href=h.url_for('organization.read', id=group_dict.name), type='button') }}
        {{ ui.form_actions() }}
    {{ ui.form() }}

    {% if can_delete %}
        <div class="delete-section">
            {{ ui.confirm_modal(_('Are you sure you want to delete this organization?'), form_id='delete-form') }}
            {{ ui.button(_('Delete Organization'), style='danger', onclick='showModal()') }}
        </div>
    {% endif %}
{%- endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `group_dict` | Current organization data |
| `data` | Form data (pre-populated) |
| `errors` | Validation errors |
| `error_summary` | Error summary |
| `can_delete` | User can delete flag |

## Screenshot Placeholder

![Organization Edit](../screenshots/organization-edit.png)

**What to show:**
- Full edit form with populated values
- Current logo display
- All editable fields
- Delete button (if authorized)
- View link to public page

## Customization Notes

### Pre-populated Fields

All fields pre-filled:
```jinja
{{ ui.input(
    name='title',
    label=_('Title'),
    value=data.title,  # Pre-populated
    errors=errors.title
) }}
```

### Image Management

Handle image updates:
```jinja
{% block image_upload %}
    <div class="image-upload">
        <label>{{ _('Organization Logo') }}</label>

        {% if data.image_url %}
            <div class="current-image">
                {{ ui.image(data.image_url, alt=data.title) }}
                <label>
                    {{ ui.checkbox(name='clear_upload', label=_('Remove current image')) }}
                </label>
            </div>
        {% endif %}

        {{ ui.file_input(
            name='image_upload',
            accept='image/*',
            errors=errors.image_upload
        ) }}
    </div>
{% endblock %}
```

### Delete Confirmation

Secure delete process:
```jinja
{% block delete_section %}
    {% if h.check_access('organization_delete', {'id': group_dict.id}) %}
        <div class="delete-section">
            <h3>{{ _('Danger Zone') }}</h3>

            {{ ui.alert(_('Deleting an organization will remove it from the portal and may affect associated datasets.'), style='warning') }}

            {{ ui.form(
                method='POST',
                action=h.url_for('organization.delete', id=group_dict.id),
                id='delete-form'
            ) }}
                {{ ui.hidden_input(name='confirmed', value='1') }}
            {{ ui.form() }}

            {{ ui.button(_('Delete Organization'), style='danger', form='delete-form', type='submit') }}
        </div>
    {% endif %}
{% endblock %}
```

### Read-Only Fields

Make certain fields non-editable:
```jinja
{{ ui.input(
    name='id',
    label=_('ID'),
    value=data.id,
    disabled=true,
    help=_('Cannot be changed')
) }}

{{ ui.input(
    name='created',
    label=_('Created'),
    value=data.created,
    disabled=true
) }}
```

### Styling

Edit-specific styling:
```scss
.organization-edit {
    .form-field {
        // Field styling
        margin-bottom: 1.5rem;
    }

    .image-upload {
        // Upload area
        border: 2px dashed #ddd;
        padding: 1.5rem;
        text-align: center;
    }

    .delete-section {
        // Danger zone
        margin-top: 3rem;
        padding-top: 2rem;
        border-top: 2px solid #dc3545;

        h3 {
            color: #dc3545;
        }
    }

    .view-link {
        // View page link
        color: #007bff;
        text-decoration: none;
    }
}
```

## Related Pages

- [Organization Create](new.md) - Create new organization
- [Organization Read](read.md) - View organization
- [Organization Delete](new.md) - Delete confirmation

## Best Practices

1. **Show Current Values**: Pre-populate all fields
2. **Image Preview**: Display current logo
3. **Confirm Delete**: Require confirmation
4. **View Link**: Easy access to public page
5. **Validation**: Clear error messages
6. **Cancel Option**: Easy discard changes

## Extension Hooks

Extensions can modify edit by:
- Adding custom form fields
- Adding custom validators
- Adding approval workflows
- Adding audit trail
- Adding bulk operations
