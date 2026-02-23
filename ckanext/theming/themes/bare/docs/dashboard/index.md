# Dashboard Section

This section covers the user dashboard pages.

## Overview

Dashboard pages provide:

- Personal activity feed
- Quick access to user content
- Management shortcuts
- Notifications

## Pages in This Section

| Page                                 | Description     |
|--------------------------------------|-----------------|
| [Dashboard](dashboard.md)            | Main dashboard  |
| [My Datasets](datasets.md)           | User's datasets |
| [My Organizations](organizations.md) | User's orgs     |
| [My Groups](groups.md)               | User's groups   |

## Access

Dashboard requires authentication:
```python
@dashboard.before_request
def before_request():
    if current_user.is_anonymous:
        flash_error(_('Not authorized to see this page'))
        return redirect_to('user.login')
```

## URL Structure

```
/dashboard                    # Main dashboard
/dashboard/datasets           # User's datasets
/dashboard/organizations      # User's organizations
/dashboard/groups             # User's groups
```

## Customization Tips

1. **Dashboard**: Customize activity feed and widgets
2. **Datasets**: Add quick actions and filters
3. **Organizations**: Show management options
4. **Groups**: Display group activity

## Screenshots

<!-- TODO: Add screenshots of your themed dashboard pages -->

### Dashboard
![Dashboard](../screenshots/dashboard.png)

### My Datasets
![Datasets](../screenshots/dashboard-datasets.png)

### My Organizations
![Organizations](../screenshots/dashboard-orgs.png)

### My Groups
![Groups](../screenshots/dashboard-groups.png)

## Related Sections

- [User](../user/index.md) - User account
- [Dataset](../dataset/index.md) - Dataset management
- [Organization](../organization/index.md) - Organizations
