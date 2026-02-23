# User Pages Reference

Quick reference for all user pages.

## All User Pages

| Page | Template | URL | Description |
|------|----------|-----|-------------|
| [Login](login.md) | `user/login.html` | `/user/login` | User authentication |
| [Logout](login.md) | `user/logout.html` | `/user/logout` | End session |
| [Register](new.md) | `user/new.html` | `/user/register` | Create account |
| [Profile](read.md) | `user/read.html` | `/user/{id}` | View profile |
| [Edit](edit.md) | `user/edit.html` | `/user/edit` | Edit profile |
| [Activity](activity.md) | `user/activity_stream.html` | `/user/activity/{id}` | Activity feed |
| [Followers](followers.md) | `user/followers.html` | `/user/followers/{id}` | Follower list |
| [Organizations](organizations.md) | `user/read_organizations.html` | `/user/{id}/organizations` | User's orgs |
| [Groups](groups.md) | `user/read_groups.html` | `/user/{id}/groups` | User's groups |
| [API Tokens](api-tokens.md) | `user/api_tokens.html` | `/user/{id}/api-tokens` | API access |
| [Request Reset](request-reset.md) | `user/request_reset.html` | `/user/reset` | Password recovery |
| [Perform Reset](perform-reset.md) | `user/perform_reset.html` | `/user/reset/{key}` | Set new password |
| [User List](list.md) | `user/list.html` | `/user` | All users |
| [Dashboard](../dashboard/dashboard.md) | `user/dashboard.html` | `/dashboard` | User dashboard |

## Common Templates

### `_base.html`
```jinja
{% extends "_layout.html" %}
{%- set _layout = _layout|default("content_context") -%}
```

### `_edit_base.html`
```jinja
{% extends "user/_base.html" %}
```

## Common Variables

```jinja
{{ user_dict }}        {# User data #}
{{ is_myself }}        {# Viewing own profile #}
{{ am_following }}     {# Following status #}
{{ follower_count }}   {# Follower count #}
```

## Common Actions

```jinja
{# Login/Logout #}
{{ h.url_for('user.login') }}
{{ h.url_for('user.logout') }}

{# Profile #}
{{ h.url_for('user.read', id=user.name) }}
{{ h.url_for('user.edit') }}

{# API Tokens #}
{{ h.url_for('user.api_tokens', id=user.id) }}

{# Password Reset #}
{{ h.url_for('user.request_reset') }}
{{ h.url_for('user.perform_reset', key=reset_key) }}
```

## Screenshot Checklist

- [ ] Login page
- [ ] Register page
- [ ] User profile
- [ ] Edit profile
- [ ] API tokens
- [ ] Password reset request
- [ ] Password reset form
- [ ] User list
- [ ] Followers page
- [ ] Activity stream

## Related Sections

- [Dashboard](../dashboard/index.md)
- [Organization](../organization/index.md)
- [Group](../group/index.md)
- [Admin](../admin/index.md)
