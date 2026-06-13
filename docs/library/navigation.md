{% from "_macros.html" import parameters_table %}
{% raw %}
# Navigation

Navigation components help users move through the application. They range from
global site navigation to page-specific actions and breadcrumbs.

## Menu Navigation

Most navigation menus consist of a wrapper component and multiple item
components.

### Generic Navigation

Use `nav` and `nav_item` for generic navigation menus.

```django
{%- call ui.util.call(ui.nav) -%}
    {{ ui.nav_item(_("Home"), href="/") }}
    {{ ui.nav_item(_("Datasets"), href="/dataset") }}
    {{ ui.nav_item(_("Organizations"), href="/organization") }}
{%- endcall %}
```

{% endraw %}
{{parameters_table(component_ref.nav, 'nav')}}
{{parameters_table(component_ref.nav_item, 'nav_item')}}
{% raw %}
### Main Site Navigation

The primary navigation usually found in the header.

/// admonition | Usage Example
    type: example

```django
{%- call ui.util.call(ui.main_nav) -%}
    {{ ui.main_nav_item(_("Datasets"), href=h.url_for("dataset.search")) }}
    {{ ui.main_nav_item(_("Organizations"), href=h.url_for("organization.index")) }}
    {{ ui.main_nav_item(_("Groups"), href=h.url_for("group.index")) }}
{%- endcall %}
```
///
{% endraw %}
{{parameters_table(component_ref.main_nav, 'main_nav')}}
{{parameters_table(component_ref.main_nav_item, 'main_nav_item')}}
{% raw %}
### Account Navigation

```django
{%- call ui.util.call(ui.account_nav) -%}
    {{ ui.account_nav_item(_("Profile"), href=h.url_for("user.profile")) }}
    {{ ui.account_nav_item(_("Settings"), href=h.url_for("user.settings")) }}
    {{ ui.account_nav_item(_("Logout"), href=h.url_for("user.logout")) }}
{%- endcall -%}
```


User-specific links like "Profile", "Settings", or "Logout".
{% endraw %}
{{parameters_table(component_ref.account_nav, 'account_nav')}}
{{parameters_table(component_ref.account_nav_item, 'account_nav_item')}}
{% raw %}
### Sidebar & Content Navigation

`sidebar_nav` is used for sidebar menus, while `content_nav` is often used for
tabs within a specific entity page (e.g., Dataset tabs).

```django
{%- call ui.util.call(ui.sidebar_nav) -%}
    {{ ui.sidebar_nav_item(_("Overview"), href=h.url_for("dataset.read", id=package.id)) }}
    {{ ui.sidebar_nav_item(_("Resources"), href=h.url_for("dataset.resources", id=package.id)) }}
    {{ ui.sidebar_nav_item(_("Activity"), href=h.url_for("dataset.activity", id=package.id)) }}
{%- endcall -%}
```

{% endraw %}
{{parameters_table(component_ref.sidebar_nav, 'sidebar_nav')}}
{{parameters_table(component_ref.sidebar_nav_item, 'sidebar_nav_item')}}
{% raw %}
### Footer Navigation

Specialized navigation for the footer area.

```django
{%- call ui.util.call(ui.footer) -%}
    {%- call ui.util.call(ui.footer_main_nav) -%}
        {{ ui.footer_main_nav_item(_("Home"), href="/") }}
        {{ ui.footer_main_nav_item(_("Datasets"), href="/dataset") }}
        {{ ui.footer_main_nav_item(_("Organizations"), href="/organization") }}
    {%- endcall -%}
    {%- call ui.util.call(ui.footer_secondary_nav) -%}
        {{ ui.footer_secondary_nav_item(_("Contact Us"), href="/contact") }}
        {{ ui.footer_secondary_nav_item(_("Privacy Policy"), href="/privacy") }}
    {%- endcall -%}
{%- endcall %}
```

#### Main footer navigation

Primary links in the footer rendered by wrapper `footer_main_nav` and
collection of `footer_main_nav_item`.

{% endraw %}
{{parameters_table(component_ref.footer_main_nav, 'footer_main_nav')}}
{{parameters_table(component_ref.footer_main_nav_item, 'footer_main_nav_item')}}
{% raw %}

#### Secondary footer navigation

Less prominent links in the footer, often for legal or support pages.  Rendered
by wrapper `footer_secondary_nav` and collection of
`footer_secondary_nav_item`.

{% endraw %}
{{parameters_table(component_ref.footer_secondary_nav, 'footer_secondary_nav')}}
{{parameters_table(component_ref.footer_secondary_nav_item, 'footer_secondary_nav_item')}}
{% raw %}
## Actions

Actions are prominent links or buttons used to perform operations on the
current page or entity.

### Page Actions

Page-level actions like "Add Dataset".

```django
{%- call ui.util.call(ui.page_action_wrapper) -%}
    {{ ui.page_action(_("Add Dataset"), href=h.url_for("dataset.new") , style="primary") }}
{%- endcall -%}
```


{% endraw %}
{{parameters_table(component_ref.page_action_wrapper, 'page_action_wrapper')}}
{{parameters_table(component_ref.page_action, 'page_action')}}
{% raw %}

### Content Actions

Entity-level actions like "Edit", "Manage", or "Delete".

```django
{%- call ui.util.call(ui.content_action_wrapper) -%}
    {{ ui.content_action(_("Edit"), href=h.url_for("dataset.edit", id=package.id)) }}
    {{ ui.content_action(_("Manage"), href=h.url_for("dataset.manage", id=package.id)) }}
    {{ ui.content_action(_("Delete"), href=h.url_for("dataset.delete", id=package.id), style="danger") }}
{%- endcall -%}
```


{% endraw %}
{{parameters_table(component_ref.content_action_wrapper, 'content_action_wrapper')}}
{{parameters_table(component_ref.content_action, 'content_action')}}
{% raw %}
## Breadcrumbs

Breadcrumbs show the user's location in the site hierarchy.

/// admonition | Usage Example
    type: example

```django
{%- call ui.util.call(ui.breadcrumb_wrapper) -%}
    {{ ui.breadcrumb(_("Home"), href="/", initial=true) }}
    {{ ui.breadcrumb(_("Datasets"), href="/dataset") }}
    {{ ui.breadcrumb(package.title, active=true) }}
{%- endcall %}
```
///
{% endraw %}
{{parameters_table(component_ref.breadcrumb_wrapper, 'breadcrumb_wrapper')}}
{{parameters_table(component_ref.breadcrumb, 'breadcrumb')}}
{% raw %}
## Pagination

Pagination controls for moving between pages of results. Can be rendered via
single `pagination` component in most cases.

```django
{{ ui.pagination(page=2, total_pages=5) }}
```

{% endraw %}
{{parameters_table(component_ref.pagination, 'pagination')}}
{% raw %}

When custom pager required, low-level components `pagination_wrapper` and
`pagination_item` can be used.

```django
{%- call ui.util.call(ui.pagination_wrapper) -%}
    {{ ui.pagination_item(_("Previous"), href="#", disabled=true) }}
    {{ ui.pagination_item("1", href="#", active=true) }}
    {{ ui.pagination_item("2", href="#") }}
    {{ ui.pagination_item("3", href="#") }}
    {{ ui.pagination_item(_("Next"), href="#") }}
{%- endcall -%}
```


{% endraw %}
{{parameters_table(component_ref.pagination_wrapper, 'pagination_wrapper')}}
{{parameters_table(component_ref.pagination_item, 'pagination_item')}}
{% raw %}
## Dropdowns

`dropdown` component provides a toggleable menu.

```django
{%- call ui.util.call(ui.dropdown, label=_("Actions")) -%}
    {{ ui.dropdown_item(_("Edit"), href=h.url_for("dataset.edit", id=package.id)) }}
    {{ ui.dropdown_item(_("Manage"), href=h.url_for("dataset.manage", id=package.id)) }}
    {{ ui.dropdown_item(_("Delete"), href=h.url_for("dataset.delete", id=package.id), style="danger") }}
{%- endcall -%}
```

{% endraw %}
{{parameters_table(component_ref.dropdown, 'dropdown')}}
{{parameters_table(component_ref.dropdown_item, 'dropdown_item')}}
{% raw %}
## Tabs

Tabs are used to organize content into different panes within the same page.

### Tabbed Content

A high-level wrapper that can handle both the tab handles and the panes.

```django
{%- call ui.util.call(ui.tabbed_content) -%}
    {% call ui.util.call(ui.tab_wrapper) -%}
        {{ ui.tab(_("Overview"), active=true) }}
        {{ ui.tab(_("Resources")) }}
        {{ ui.tab(_("Activity")) }}
    {%- endcall -%}

    {%- call ui.util.call(ui.tab_pane_wrapper) -%}
        {{ ui.tab_pane("Overview content here", active=true) }}
        {{ ui.tab_pane("Resources content here") }}
        {{ ui.tab_pane("Activity content here") }}
    {%- endcall -%}
{%- endcall -%}
```

{% endraw %}
{{parameters_table(component_ref.tabbed_content, 'tabbed_content')}}
{% raw %}

### Low-level Tab Components

Use these for more control over tab layout.

Tab navigation itself consists of a wrapper (`tab_wrapper`) and individual tab
handles (`tab`)

```django
{%- call ui.util.call(ui.tab_wrapper) -%}
    {{ ui.tab(_("Overview"), active=true) }}
    {{ ui.tab(_("Resources")) }}
    {{ ui.tab(_("Activity")) }}
{%- endcall -%}
```

{% endraw %}
{{parameters_table(component_ref.tab_wrapper, 'tab_wrapper')}}
{{parameters_table(component_ref.tab, 'tab')}}
{% raw %}

Tab panes are rendered using `tab_pane_wrapper` and individual panes with `tab_pane`.

```django
{%- call ui.util.call(ui.tab_pane_wrapper) -%}
    {{ ui.tab_pane("Overview content here", active=true) }}
    {{ ui.tab_pane("Resources content here") }}
    {{ ui.tab_pane("Activity content here") }}
{%- endcall -%}
```

{% endraw %}
{{parameters_table(component_ref.tab_pane_wrapper, 'tab_pane_wrapper')}}
{{parameters_table(component_ref.tab_pane, 'tab_pane')}}
