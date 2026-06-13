{% from "_macros.html" import parameters_table %}
{% raw %}
# Elements

Basic building blocks used throughout the interface.

## Action Elements

### Button

Interactive elements for triggering actions.
{% endraw %}
{{parameters_table(component_ref.button, 'button')}}
{% raw %}
### Link

Standard hyperlinks for navigation.
{% endraw %}
{{parameters_table(component_ref.link, 'link')}}
{% raw %}
## Content Indicators

### Badge

Small indicators for counts or status.
{% endraw %}
{{parameters_table(component_ref.badge, 'badge')}}
{% raw %}
### Tag

Labels for categorizing content.
{% endraw %}
{{parameters_table(component_ref.tag, 'tag')}}
{% raw %}
## Visual Media

### Icon

Graphical symbols representing actions or concepts.
{% endraw %}
{{parameters_table(component_ref.icon, 'icon')}}
{% raw %}
### Image

Displaying images with proper attributes.
{% endraw %}
{{parameters_table(component_ref.image, 'image')}}
{% raw %}
### Video

Video player component.
{% endraw %}
{{parameters_table(component_ref.video, 'video')}}
{% raw %}
## Utilities

### Datetime

Formatted and localized date and time display.
{% endraw %}
{{parameters_table(component_ref.datetime, 'datetime')}}
{% raw %}
### Empty

A component shown when there is no content to display.
{% endraw %}
{{parameters_table(component_ref.empty, 'empty')}}
