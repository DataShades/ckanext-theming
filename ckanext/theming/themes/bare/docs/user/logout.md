# User Logout Page

End user session and logout.

## Overview

Logout page provides:
- Logout confirmation
- Session termination
- Return to home option

## URL Pattern

```
GET /user/logout
```

## Purpose

The logout page:
- Confirms logout was successful
- Clears session data
- Provides navigation options

## Template

**File:** `templates/user/logout.html`

### Structure

```jinja
{% extends "user/_base.html" %}
{%- set _layout = _layout|default("content_focus") -%}

{% block subtitle %}
    {{ ui.subtitle_item(_('Logout')) }}
{% endblock %}

{% block primary_content_inner %}
    <h2>{{ _('You have logged out') }}</h2>

    <p>{{ _('You have successfully logged out.') }}</p>

    {{ ui.button(_('Go to Home'), href=h.url_for('home.index')) }}
    {{ ui.button(_('Login'), href=h.url_for('user.login')) }}
{% endblock %}
```

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| Go home | Return to homepage | Home button |
| Login | Log back in | Login button |

## Screenshot Placeholder

![Logout](../screenshots/user-logout.png)
*Placeholder: Logout confirmation page*

## Related Pages

- [Login](login.md) - User login
- [Home](../home/home.md) - Home page
