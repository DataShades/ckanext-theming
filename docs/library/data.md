---
include_yaml:
    component_ref: ckanext/theming/components.yaml
---


# Data & Visualization

Components for displaying structured data, code, and visualizations.

## Tables

Tables are used to organize complex data into rows and columns.


!!! example

    ```django
    {%- call ui.util.call(ui.table, striped=true) -%}
        {%- call ui.util.call(ui.table_head) -%}
            {%- call ui.util.call(ui.table_row) -%}
                {{ ui.table_cell(_("Name"), header=true) }}
                {{ ui.table_cell(_("Value"), header=true) }}
            {%- endcall -%}
        {%- endcall -%}
        {%- call ui.util.call(ui.table_body) -%}
            {%- call ui.util.call(ui.table_row) -%}
                {{ ui.table_cell("Item 1") }}
                {{ ui.table_cell("100") }}
            {%- endcall -%}
        {%- endcall -%}
    {%- endcall -%}
    ```


<<parameters_table(component_ref.table, 'table')>>
<<parameters_table(component_ref.table_head, 'table_head')>>
<<parameters_table(component_ref.table_body, 'table_body')>>
<<parameters_table(component_ref.table_row, 'table_row')>>
<<parameters_table(component_ref.table_cell, 'table_cell')>>

## Visualizations

### Chart

Renders a chart using data provided in the parameters.


!!! example

    ```django
    {{ ui.chart(data=[10, 20, 30], labels=["A", "B", "C"], type="pie") }}
    ```


<<parameters_table(component_ref.chart, 'chart')>>

## Technical Content

### Code

Displays code blocks with optional syntax highlighting and dedenting.

<<parameters_table(component_ref.code, 'code')>>
