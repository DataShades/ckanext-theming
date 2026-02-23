# Dashboard Pages

User dashboard and content management.

## Overview

The dashboard provides a central location for users to:
- View personalized activity feed
- Manage their content
- Access quick actions
- Monitor notifications

## Pages

### Main Dashboard

**Template:** `templates/user/dashboard.html`
**URL:** `/dashboard`

Shows:
- Recent activity from followed items
- News feed
- Quick statistics

### My Datasets

**Template:** `templates/user/dashboard_datasets.html`
**URL:** `/dashboard/datasets`

Shows:
- User's created datasets
- Draft datasets
- Quick edit actions

### My Organizations

**Template:** `templates/user/dashboard_organizations.html`
**URL:** `/dashboard/organizations`

Shows:
- Organizations user belongs to
- Admin permissions
- Quick access links

### My Groups

**Template:** `templates/user/dashboard_groups.html`
**URL:** `/dashboard/groups`

Shows:
- Groups user belongs to
- Group memberships
- Activity updates

## Template

**Main Template:** `templates/user/dashboard.html`

### Structure

```jinja
{% extends "user/_base.html" %}
{%- set _layout = _layout|default("content_focus") -%}

{%- block primary_content_inner %}
    {{ ui.dashboard_activity_stream(activities) }}
{% endblock %}
```

## Screenshot Placeholders

### Main Dashboard
![Dashboard](../screenshots/dashboard.png)
*Placeholder: Activity feed and widgets*

### My Datasets
![Datasets](../screenshots/dashboard-datasets.png)
*Placeholder: Dataset management list*

### My Organizations
![Organizations](../screenshots/dashboard-orgs.png)
*Placeholder: Organization list*

### My Groups
![Groups](../screenshots/dashboard-groups.png)
*Placeholder: Group list*

## Related Pages

- [User Profile](../user/read.md) - User profile
- [User Activity](../user/activity.md) - Activity stream
- [Dataset Search](../dataset/search.md) - Browse datasets
