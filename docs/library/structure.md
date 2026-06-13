{% from "_macros.html" import parameters_table %}
{% raw %}
# Site Structure

Components that define the top-level structure and persistent elements of the
portal.

## Page Header

The `header` component typically contains the site logo, branding, and main
navigation.
{% endraw %}
{{parameters_table(component_ref.header, 'header')}}
{% raw %}
### Account Area

Usually placed within the header to show user-related info and links.
{% endraw %}
{{parameters_table(component_ref.account, 'account')}}
{% raw %}
## Page Footer

Components for building the site footer.
{% endraw %}
{{parameters_table(component_ref.footer, 'footer')}}
{{parameters_table(component_ref.footer_main, 'footer_main')}}
{{parameters_table(component_ref.footer_secondary, 'footer_secondary')}}
{% raw %}
## Meta Components

### Subtitle Item

Used for building the page title that appears in the browser tab.
{% endraw %}
{{parameters_table(component_ref.subtitle_item, 'subtitle_item')}}
