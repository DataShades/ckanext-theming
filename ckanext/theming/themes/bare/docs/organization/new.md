# Organization Create Page

Form for creating new organizations in CKAN.

## Overview

The organization create page provides:
- Organization information form
- Image upload
- Custom field support
- Validation

## URL Pattern

```
GET /organization/new
POST /organization/new
```

**Example:**
```
<<vars.site_url>>/organization/new
```

## Purpose

The create page allows authorized users to:
- Create new organizations
- Define organization details
- Upload organization logo
- Set custom metadata

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| Enter details | Fill organization form | Form fields |
| Upload image | Add organization logo | Image upload |
| Add custom fields | Set extra metadata | Custom fields |
| Save | Create organization | Submit button |
| Cancel | Abort creation | Cancel button |

## Template

**File:** `templates/organization/new.html`

### Template Structure

```jinja
{% extends "organization/_edit_base.html" %}

{% set label = h.humanize_entity_type('organization', group_type, 'create title') or _('Create an Organization') %}

{%- block subtitle -%}
    {{ ui.subtitle_item(label) }}
{%- endblock -%}

{%- block primary_content_inner %}
    {{ ui.form(method="POST", enctype="multipart/form-data") }}
        {{ ui.form_errors(error_summary) }}

        {{ ui.input(
            name='title',
            label=_('Title'),
            placeholder=_('My Organization'),
            value=data.title,
            errors=errors.title,
            required=true
        ) }}

        {{ ui.input(
            name='name',
            label=_('URL'),
            placeholder=_('my-organization'),
            value=data.name,
            errors=errors.name,
            required=true
        ) }}

        {{ ui.textarea(
            name='description',
            label=_('Description'),
            placeholder=_('Describe the organization...'),
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

        {{ ui.input(
            name='url',
            label=_('Website'),
            type='url',
            value=data.url,
            errors=errors.url
        ) }}

        {{ ui.form_actions() }}
            {{ ui.submit(_('Create Organization')) }}
            {{ ui.button(_('Cancel'), href=h.url_for('organization.index'), type='button') }}
        {{ ui.form_actions() }}
    {{ ui.form() }}
{%- endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `data` | Form data |
| `errors` | Validation errors |
| `error_summary` | Error summary |
| `group_type` | Organization type |

## Screenshot Placeholder

![Organization Create](../screenshots/organization-new.png)

**What to show:**
- Full create form
- All input fields
- Image upload widget
- Submit/cancel buttons
- Validation errors (if any)

## Customization Notes

### Form Fields

Default fields:
- Title (required)
- URL/Name (required, auto-generated)
- Description (markdown supported)
- Logo image
- Email
- Website URL
- Phone
- Custom extras

### Custom Fields

Add organization-specific fields:
```jinja
{% block organization_custom_fields %}
    {{ ui.input(
        name='org_code',
        label=_('Organization Code'),
        placeholder=_('ORG-001'),
        value=data.org_code,
        errors=errors.org_code
    ) }}

    {{ ui.select(
        name='org_type',
        label=_('Organization Type'),
        options=[
            {'value': 'government', 'text': _('Government')},
            {'value': 'nonprofit', 'text': _('Non-profit')},
            {'value': 'commercial', 'text': _('Commercial')},
        ],
        value=data.org_type,
        errors=errors.org_type
    ) }}
{% endblock %}
```

### Image Upload

Customize upload widget:
```jinja
{% block image_upload %}
    <div class="image-upload">
        <label>{{ _('Organization Logo') }}</label>

        {% if data.image_url %}
            <div class="current-image">
                {{ ui.image(data.image_url, alt=data.title) }}
            </div>
        {% endif %}

        {{ ui.file_input(
            name='image_upload',
            accept='image/*',
            errors=errors.image_upload
        ) }}

        <small>{{ _('Supported formats: PNG, JPG, GIF. Max size: 2MB') }}</small>
    </div>
{% endblock %}
```

### URL Slug Generation

Auto-generate URL from title:
```javascript
// Auto-generate URL slug from title
document.querySelector('[name="title"]').addEventListener('input', function() {
    const slug = this.value
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-+|-+$/g, '');

    const nameField = document.querySelector('[name="name"]');
    if (!nameField.value || nameField.dataset.auto) {
        nameField.value = slug;
        nameField.dataset.auto = 'true';
    }
});
```

### Styling

Create-specific styling:
```scss
.organization-new {
    .form-field {
        // Field wrapper
        margin-bottom: 1.5rem;
    }

    .image-upload {
        // Upload widget
        .current-image {
            margin-bottom: 1rem;

            img {
                max-height: 150px;
                max-width: 300px;
            }
        }
    }

    .form-actions {
        // Button area
        display: flex;
        gap: 1rem;
        margin-top: 2rem;
    }
}
```

## Related Pages

- [Organization Edit](edit.md) - Edit existing organization
- [Organization Read](read.md) - View created organization
- [Organization Index](index.md) - List all organizations

## Best Practices

1. **Clear Labels**: Use descriptive field names
2. **Required Indicators**: Mark required fields
3. **Auto-generate URL**: Create slug from title
4. **Image Preview**: Show uploaded logo
5. **Validation**: Clear error messages
6. **Help Text**: Provide field guidance

## Extension Hooks

Extensions can modify create by:
- Adding custom form fields
- Adding custom validators
- Adding image processing
- Adding approval workflows
- Adding organization templates
