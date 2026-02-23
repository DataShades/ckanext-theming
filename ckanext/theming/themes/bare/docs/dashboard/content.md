# Dashboard Content Pages

Dashboard sub-pages for managing user content.

## My Datasets

**Template:** `templates/user/dashboard_datasets.html`
**URL:** `/dashboard/datasets`

### Overview

Shows all datasets created by the current user:
- Published datasets
- Draft datasets
- Deleted datasets (if applicable)

### Actions

- Edit dataset
- View dataset
- Create new dataset
- Filter by state

### Screenshot

![My Datasets](../screenshots/dashboard-datasets.png)
*Placeholder: Dataset management list*

## My Organizations

**Template:** `templates/user/dashboard_organizations.html`
**URL:** `/dashboard/organizations`

### Overview

Shows organizations where user is a member:
- Admin permissions
- Editor permissions
- Member permissions

### Actions

- View organization
- Manage organization (if admin)
- Create new organization
- Filter by role

### Screenshot

![My Organizations](../screenshots/dashboard-orgs.png)
*Placeholder: Organization membership list*

## My Groups

**Template:** `templates/user/dashboard_groups.html`
**URL:** `/dashboard/groups`

### Overview

Shows groups where user is a member:
- Groups user belongs to
- Membership level
- Group activity

### Actions

- View group
- Manage group (if member)
- Create new group
- Browse group datasets

### Screenshot

![My Groups](../screenshots/dashboard-groups.png)
*Placeholder: Group membership list*

## Related Pages

- [Dashboard](dashboard.md) - Main dashboard
- [User Profile](../user/read.md) - User profile
- [Dataset Search](../dataset/search.md) - Browse datasets
