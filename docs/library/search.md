{% from "_macros.html" import parameters_table %}
{% raw %}
# Search

Components for building comprehensive search interfaces with filtering, sorting,
and result counts.

## Search Form

The `search_form` component is a high-level wrapper that coordinates all search
elements.
{% endraw %}
{{parameters_table(component_ref.search_form, 'search_form')}}
{% raw %}
### Search Input Area

These components handle the primary search query input.
{% endraw %}
{{parameters_table(component_ref.search_form_box, 'search_form_box')}}
{{parameters_table(component_ref.search_input, 'search_input')}}
{{parameters_table(component_ref.search_submit_button, 'search_submit_button')}}
{% raw %}
## Results & Controls

### Search Information

Displays counts and current search context.
{% endraw %}
{{parameters_table(component_ref.search_results_text, 'search_results_text')}}
{{parameters_table(component_ref.search_active_filters, 'search_active_filters')}}
{% raw %}
### Advanced Controls & Sorting
{% endraw %}
{{parameters_table(component_ref.search_sort_control, 'search_sort_control')}}
{{parameters_table(component_ref.search_advanced_controls, 'search_advanced_controls')}}
