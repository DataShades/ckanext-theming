# Group Pages Documentation

The Group section pages follow the same structure as Organization pages. This document provides a quick reference for all group pages.

## Page Templates

All group pages use these templates:

| Page | Template | Extends |
|------|----------|---------|
| Index | `group/index.html` | `group/_base.html` |
| Read | `group/read.html` | `group/_base.html` |
| About | `group/about.html` | `group/_base.html` |
| New | `group/new.html` | `group/_edit_base.html` |
| Edit | `group/edit.html` | `group/_edit_base.html` |
| Members | `group/members.html` | `group/_base.html` |
| Member New | `group/member_new.html` | `group/_edit_base.html` |
| Manage Members | `group/manage_members.html` | `group/_edit_base.html` |
| Admins | `group/admins.html` | `group/_edit_base.html` |
| Activity | `group/activity_stream.html` | `group/_base.html` |
| Changes | `group/changes.html` | `group/_base.html` |
| Followers | `group/followers.html` | `group/_base.html` |

## URL Patterns

```
/group                              # Index
/group/{id}                         # Read
/group/about/{id}                   # About
/group/new                          # Create
/group/edit/{id}                    # Edit
/group/members/{id}                 # Members
/group/member_new/{id}              # Add Member
/group/member_manage/{id}           # Manage Members
/group/admins/{id}                  # Administrators
/group/activity/{id}                # Activity
/group/changes/{id}                 # Changes
/group/followers/{id}               # Followers
```

## Key Differences from Organizations

### Template Variables

Group pages use `group_dict` instead of `organization_dict`:

```jinja
{# In group templates #}
{{ group_dict.title }}
{{ group_dict.description }}
{{ group_dict.image_url }}
```

### Access Checks

```jinja
{% if h.check_access('group_update', {'id': group_dict.id}) %}
    {{ ui.button(_('Edit'), href=h.url_for('group.edit', id=group_dict.id)) }}
{% endif %}
```

### URL Patterns

```jinja
{{ h.url_for('group.read', id=group.name) }}
{{ h.url_for('group.edit', id=group.id) }}
{{ h.url_for('group.delete', id=group.id) }}
```

## Screenshot Placeholders

### Group Index
![Group Index](../screenshots/group-index.png)
*Placeholder: List of groups with search and filters*

### Group Read
![Group Read](../screenshots/group-read.png)
*Placeholder: Group profile with datasets*

### Group About
![Group About](../screenshots/group-about.png)
*Placeholder: Group description and details*

### Group Create/Edit
![Group Edit](../screenshots/group-edit.png)
*Placeholder: Group creation/edit form*

### Group Members
![Group Members](../screenshots/group-members.png)
*Placeholder: Member list with roles*

### Group Activity
![Group Activity](../screenshots/group-activity.png)
*Placeholder: Activity feed*

## Customization Notes

### Reusing Organization Patterns

Most group pages can be customized similarly to organization pages:

```scss
// Copy organization styles with namespace change
.group-index { @extend .organization-index; }
.group-read { @extend .organization-read; }
.group-members { @extend .organization-members; }
```

### Group-Specific Features

1. **Thematic Focus**: Emphasize topic/subject matter
2. **Community Aspect**: Highlight collaboration
3. **Flexible Structure**: Less formal than organizations
4. **Public by Default**: Usually open access

## Related Documentation

For detailed documentation on each page type, see the corresponding Organization pages:

- [Organization Index](../organization/index.md) → Group Index pattern
- [Organization Read](../organization/read.md) → Group Read pattern
- [Organization Members](../organization/members.md) → Group Members pattern
- [Organization Activity](../organization/activity.md) → Group Activity pattern

## Quick Reference

### Common Macros

```jinja
{{ ui.group(group) }}           {# Group card #}
{{ ui.search_form(...) }}       {# Search form #}
{{ ui.facet_section(...) }}     {# Facets #}
{{ ui.form(...) }}              {# Form wrapper #}
{{ ui.table(...) }}             {# Table #}
```

### Common Variables

```jinja
{{ group_dict }}    {# Group data #}
{{ group }}         {# Group object #}
{{ datasets }}      {# Group datasets #}
{{ members }}       {# Group members #}
{{ page }}          {# Pagination #}
```

### Common Actions

```jinja
{# Create #}
{{ h.url_for('group.new') }}

{# Read #}
{{ h.url_for('group.read', id=group.name) }}

{# Edit #}
{{ h.url_for('group.edit', id=group.id) }}

{# Delete #}
{{ h.url_for('group.delete', id=group.id) }}

{# Search #}
{{ h.url_for('group.search', q=query) }}
```
