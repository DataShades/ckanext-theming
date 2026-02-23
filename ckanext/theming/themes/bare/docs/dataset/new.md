# Dataset Create Page

The form for creating new datasets in CKAN.

## Overview

The dataset create page provides:
- Multi-stage form wizard
- Basic metadata input
- Organization selection
- Tag input
- License selection
- Custom field support

## URL Pattern

```
GET /dataset/new
POST /dataset/new
```

**Example:**
```
<<vars.site_url>>/dataset/new
```

## Purpose

The create page allows authorized users to:
- Add new datasets to the portal
- Enter metadata and description
- Upload or link to resources
- Categorize with tags and groups
- Set licensing and access controls

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| Enter metadata | Fill dataset details | Form fields |
| Add tags | Categorize dataset | Tag input |
| Select license | Choose license | License dropdown |
| Select organization | Assign ownership | Organization dropdown |
| Add resources | Upload/link files | Resource section |
| Save dataset | Create dataset | Submit button |
| Cancel | Abort creation | Cancel button |

## Template

**File:** `templates/package/new.html`

### Template Structure

```jinja
{% extends "package/_edit_base.html" %}

{%- block subtitle -%}
    {{ ui.subtitle_item(h.humanize_entity_type('package', dataset_type, 'create title') or _('Create Dataset')) }}
{%- endblock -%}

{%- block primary_content_inner %}
    {{ ui.form(method="POST", enctype="multipart/form-data") }}
        {{ ui.form_errors(error_summary) }}
        {{ ui.package_basic_fields(data, errors) }}
        {{ ui.package_metadata_fields(data, errors) }}
        {{ ui.form_actions() }}
            {{ ui.submit(_('Create Dataset')) }}
        {{ ui.form_actions() }}
    {{ ui.form() }}
{%- endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `data` | Form data dictionary |
| `errors` | Validation errors |
| `error_summary` | Summary of errors |
| `dataset_type` | Package type |
| `group_type` | Default group type |

### Form Stages

CKAN uses a multi-stage form:
1. **Basic Info** - Title, description, tags
2. **Data Files** - Add resources
3. **Review** - Confirm and save

## Screenshot Placeholder

![Dataset Create](../screenshots/dataset-new.png)

**What to show:**
- Full create form
- All input fields visible
- Validation errors (if any)
- Submit/cancel buttons
- Stage indicator (if using wizard)

## Customization Notes

### Form Fields

Default fields include:
- Title (required)
- Description (markdown supported)
- Tags
- License
- Organization
- Author
- Author email
- Maintainer
- Maintainer email
- Version
- URL (source)

### Adding Custom Fields

```jinja
{% block package_metadata_fields_custom %}
    {{ ui.input(
        name='custom_field',
        label=_('Custom Field'),
        placeholder=_('Enter value'),
        value=data.custom_field,
        errors=errors.custom_field
    ) }}
{% endblock %}
```

### Validation

Client and server-side validation:
```python
# In plugin validator
def dataset_validator(key, data, errors, context):
    if not data.get(('title',)):
        errors[('title',)].append(_('Missing value'))
```

### Organization Selection

Configure organization display:
```jinja
{% block package_metadata_fields_owner_org %}
    {{ ui.select(
        name='owner_org',
        label=_('Organization'),
        options=organizations,
        value=data.owner_org,
        errors=errors.owner_org
    ) }}
{% endblock %}
```

### License Selection

License dropdown options:
```jinja
{% block package_metadata_fields_license %}
    {{ ui.select(
        name='license_id',
        label=_('License'),
        options=licenses,
        value=data.license_id,
        errors=errors.license_id
    ) }}
{% endblock %}
```

### Styling

Key form styling:
```scss
.dataset-new {
    .form-field {
        // Field wrapper
    }

    .input-group {
        // Input styling
    }

    .error-message {
        // Error styling
    }

    .form-actions {
        // Button container
    }
}
```

## Related Pages

- [Dataset Edit](edit.md) - Modify existing dataset
- [Dataset Read](read.md) - View created dataset
- [Dataset Search](search.md) - Browse datasets

## Best Practices

1. **Clear Labels**: Use descriptive field labels
2. **Help Text**: Provide field guidance
3. **Validation**: Show clear error messages
4. **Required Fields**: Mark required fields clearly
5. **Progress Indication**: Show form progress
6. **Autosave**: Consider draft autosave

## Extension Hooks

Extensions can modify create form by:
- Adding custom form fields
- Adding custom validators
- Modifying form workflow
- Adding file upload widgets
- Adding metadata templates
