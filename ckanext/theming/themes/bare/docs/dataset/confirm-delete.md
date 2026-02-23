# Dataset Delete Confirmation

Confirm deletion of a dataset.

## Overview

Delete confirmation page provides:
- Final confirmation before deletion
- Warning about consequences
- Related resource information

## URL Pattern

```
GET /dataset/delete/{id}
POST /dataset/delete/{id}
```

**Examples:**
```
<<vars.site_url>>/dataset/delete/annual-report
<<vars.site_url>>/dataset/delete/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The delete page:
- Prevents accidental deletion
- Informs about impact
- Requires explicit confirmation

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| Confirm delete | Permanently remove | Confirm button |
| Cancel | Keep dataset | Cancel button |

## Template

**File:** `templates/package/confirm_delete.html`

### Structure

```jinja
{% extends "_layout.html" %}
{%- set _layout = _layout|default("content_focus") -%}

{% block subtitle %}
    {{ ui.subtitle_item(_('Confirm Delete')) }}
{% endblock %}

{% block primary_content_inner %}
    <h2>{{ _('Delete Dataset') }}</h2>

    {{ ui.alert(_('Are you sure you want to delete this dataset?'), style='danger') }}

    <p>{{ _('This will also delete:') }}</p>
    <ul>
        <li>{{ resource_count }} resources</li>
        <li>{{ view_count }} views</li>
    </ul>

    {{ ui.form(method="POST") }}
        {{ ui.hidden_input(name='confirmed', value='1') }}
        {{ ui.submit(_('Delete'), style='danger') }}
        {{ ui.button(_('Cancel'), href=h.url_for('dataset.read', id=pkg.id)) }}
    {{ ui.form() }}
{% endblock %}
```

## Screenshot Placeholder

![Delete Confirm](../screenshots/dataset-delete-confirm.png)
*Placeholder: Delete confirmation dialog*

## Related Pages

- [Dataset Edit](edit.md) - Edit dataset
- [Dataset Read](read.md) - View dataset
- [Admin Trash](../admin/trash.md) - Purge deleted items
