---
include_yaml:
    component_ref: ckanext/theming/components.yaml
---

# CKAN Content

Content components are designed to display CKAN's core entities in a consistent
way. Most entities have a singular component (e.g., `package`) and a list
wrapper (e.g., `package_list`).

## Datasets (Packages)

The `package` component displays information about a single dataset, typically
as a snippet in search results or a list.

!!! example


    ```django
    {%- call ui.util.call(ui.package_list) -%}
        {%- for pkg in packages -%}
            {{ ui.package(package=pkg) }}
        {%- endfor -%}
    {%- endcall -%}
    ```

<<parameters_table(component_ref.package_list, 'package_list')>>
<<parameters_table(component_ref.package, 'package')>>

## Organizations

Displays information about a CKAN organization.

!!! example


    ```django
    {%- call ui.util.call(ui.organization_list) -%}
        {%- for org in organizations -%}
            {{ ui.organization(organization=org) }}
        {%- endfor -%}
    {%- endcall -%}
    ```


<<parameters_table(component_ref.organization_list, 'organization_list')>>
<<parameters_table(component_ref.organization, 'organization')>>

## Groups

Displays information about a CKAN group.


!!! example


    ```django
    {%- call ui.util.call(ui.group_list) -%}
        {%- for group in groups -%}
            {{ ui.group(group=group) }}
        {%- endfor -%}
    {%- endcall -%}
    ```


<<parameters_table(component_ref.group_list, 'group_list')>>
<<parameters_table(component_ref.group, 'group')>>

## Resources

Displays information about a single resource within a dataset.


!!! example


    ```django
    {%- call ui.util.call(ui.resource_list) -%}
        {%- for resource in resources -%}
            {% set package = h.get_package(resource.package_id) %}
            {{ ui.resource(resource=resource, package=package) }}
        {%- endfor -%}
    {%- endcall -%}
    ```


<<parameters_table(component_ref.resource_list, 'resource_list')>>
<<parameters_table(component_ref.resource, 'resource')>>

## Users

Displays user profile information.


!!! example


    ```django
    {%- call ui.util.call(ui.user_list) -%}
        {%- for user in users -%}
            {{ ui.user(user=user) }}
        {%- endfor -%}
    {%- endcall -%}
    ```



<<parameters_table(component_ref.user_list, 'user_list')>>
<<parameters_table(component_ref.user, 'user')>>

## Search & Facets

Components for filtering and exploring content.

### Facets

`facet` components are used to filter search results. They are usually grouped
into a `facet_list` and further organized into `facet_section`s.

!!! example


    ```django
    {%- call ui.util.call(ui.facet_section, title=_("Organizations")) -%}
        {%- call ui.util.call(ui.facet_list) -%}
            {%- for item in facets -%}
                {{ ui.facet(item.display_name, key="organization", value=item.name, count=item.count) }}
            {%- endfor -%}
        {%- endcall -%}
    {%- endcall -%}
    ```

#### Facet section

<<parameters_table(component_ref.facet_section, 'facet_section')>>


#### Facet list and facet

<<parameters_table(component_ref.facet_list, 'facet_list')>>
<<parameters_table(component_ref.facet, 'facet')>>

### Filters Container

A high-level container for all search filters, typically shown in the sidebar.


!!! example


    ```django
    {%- call ui.util.call(ui.filters) -%}
        {%- call ui.util.call(ui.facet_section, title=_("Organizations")) -%}
            {%- call ui.util.call(ui.facet_list) -%}
                {%- for item in facets -%}
                    {{ ui.facet(item.display_name, key="organization", value=item.name, count=item.count) }}
                {%- endfor -%}
            {%- endcall -%}
        {%- endcall -%}

        {%- call ui.util.call(ui.facet_section, title=_("Tags")) -%}
            {%- call ui.util.call(ui.facet_list) -%}
                {%- for item in tag_facets -%}
                    {{ ui.facet(item.display_name, key="tags", value=item.name, count=item.count) }}
                {%- endfor -%}
            {%- endcall -%}
    {%- endcall -%}

    ```



<<parameters_table(component_ref.filters, 'filters')>>
