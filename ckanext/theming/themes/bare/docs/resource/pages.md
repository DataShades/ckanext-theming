# Resource Pages Reference

Quick reference for all resource pages.

## All Resource Pages

| Page | Template | URL | Description |
|------|----------|-----|-------------|
| [Read](read.md) | `package/resource_read.html` | `/dataset/{id}/resource/{rid}` | View resource |
| [Edit](edit.md) | `package/resource_edit.html` | `/dataset/{id}/resource/{rid}/edit` | Edit metadata |
| [History](history.md) | `package/resource_history.html` | `/dataset/{id}/resource/{rid}/history` | Version history |
| [Views](views.md) | `package/resource_views.html` | `/dataset/{id}/resource/{rid}/views` | Manage views |
| [New View](views.md) | `package/new_view.html` | `/dataset/{id}/resource/{rid}/views/new` | Create view |
| [Dictionary](dictionary.md) | `datastore/dictionary.html` | `/dataset/{id}/resource/{rid}/dictionary` | Data dictionary |
| [Data](data.md) | `datapusher/resource_data.html` | `/dataset/{id}/resource/{rid}/data` | Resource data |

## Common Templates

### `_resource_edit_base.html`
```jinja
{% extends "package/_edit_base.html" %}
```

## Common Variables

```jinja
{{ resource }}      {# Resource data #}
{{ package }}       {# Parent dataset #}
{{ pkg_dict }}      {# Dataset dictionary #}
{{ views }}         {# Resource views #}
{{ data_dictionary }} # Field definitions #}
```

## Common Actions

```jinja
{# Read #}
{{ h.url_for('resource.read', id=pkg.id, resource_id=resource.id) }}

{# Edit #}
{{ h.url_for('resource.edit', id=pkg.id, resource_id=resource.id) }}

{# Views #}
{{ h.url_for('resource.views', id=pkg.id, resource_id=resource.id) }}

{# Dictionary #}
{{ h.url_for('resource.dictionary', id=pkg.id, resource_id=resource.id) }}
```

## Screenshot Checklist

- [ ] Resource read page
- [ ] Resource edit form
- [ ] Resource history
- [ ] Resource views list
- [ ] New view form
- [ ] Data dictionary
- [ ] Resource data preview

## Related Sections

- [Dataset](../dataset/index.md)
- [Admin](../admin/index.md)
- [Other](../other/index.md)
