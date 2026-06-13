{% from "_macros.html" import parameters_table %}
{% raw %}
# Forms

Form components handle user input and provide consistent styling and validation
feedback.

## Form Structure

Use these components to define the boundaries and overall structure of your
forms.

### Form Container

The `form` macro is a high-level wrapper that handles opening and closing tags,
CSRF tokens, and basic form attributes.

/// admonition | Usage Example
    type: example

```django
{%- call ui.util.call(ui.form, method="POST") -%}
    {{ ui.input(name="title", label=_("Title")) }}
    {%- call ui.util.call(ui.form_actions) -%}
        {{ ui.button(_("Save"), type="submit") }}
    {%- endcall -%}
{%- endcall -%}
```
///
{% endraw %}
{{parameters_table(component_ref.form, 'form')}}
{% raw %}
### Low-level Form Components

Use these when you need more control over the form's HTML structure.


/// admonition | Usage Example
    type: example

```django
{{ ui.form_start(method="POST") }}

{{ h.csrf_input() }}
{{ ui.input(name="title", label=_("Title")) }}

{%- call ui.util.call(ui.form_actions) -%}
    {{ ui.button(_("Save"), type="submit") }}
{%- endcall -%}

{{ ui.form_end() }}
```
///

{% endraw %}
{{parameters_table(component_ref.form_start, 'form_start')}}
{{parameters_table(component_ref.form_end, 'form_end')}}
{{parameters_table(component_ref.form_actions, 'form_actions')}}
{% raw %}

### Fieldsets and Annotations
{% endraw %}
{{parameters_table(component_ref.fieldset, 'fieldset')}}
{{parameters_table(component_ref.form_annotation, 'form_annotation')}}
{% raw %}
## Input Components

These components represent individual form fields.

### Text Inputs

Basic single-line and multi-line text inputs.
{% endraw %}
{{parameters_table(component_ref.input, 'input')}}
{{parameters_table(component_ref.textarea, 'textarea')}}
{{parameters_table(component_ref.hidden_input, 'hidden_input')}}
{% raw %}
### Rich Inputs

Specialized inputs for specific data types or enhanced interactivity.
{% endraw %}
{{parameters_table(component_ref.markdown, 'markdown')}}
{{parameters_table(component_ref.autocomplete, 'autocomplete')}}
{{parameters_table(component_ref.file_input, 'file_input')}}
{{parameters_table(component_ref.range_input, 'range_input')}}
{% raw %}
### Selection Inputs
{% endraw %}
{{parameters_table(component_ref.select, 'select')}}
{{parameters_table(component_ref.select_box, 'select_box')}}
{{parameters_table(component_ref.select_option, 'select_option')}}
{{parameters_table(component_ref.checkbox, 'checkbox')}}
{{parameters_table(component_ref.radio, 'radio')}}
{% raw %}
## Validation and Feedback
{% endraw %}
{{parameters_table(component_ref.form_errors, 'form_errors')}}
{{parameters_table(component_ref.field_errors, 'field_errors')}}
{{parameters_table(component_ref.field_info, 'field_info')}}
{% raw %}
## Dynamic Fields (Extras)

Used for handling dynamic key-value pairs (e.g., CKAN's extra fields).
{% endraw %}
{{parameters_table(component_ref.extra_fields_collection, 'extra_fields_collection')}}
{{parameters_table(component_ref.extra_field, 'extra_field')}}
