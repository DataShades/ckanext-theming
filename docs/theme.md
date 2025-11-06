# Creating and Registering CKAN Themes

This guide explains how to create and register a new theme in CKAN using the theming extension. The examples below reference the provided `bare` theme as a reference implementation.

## Overview

A CKAN theme allows you to customize the look and feel of your CKAN instance by overriding templates, assets, and providing a set of UI macros that can be used consistently across your site.

## Theme Structure

A CKAN theme should be organized in a specific directory structure within your extension:

```
your_extension/
├── ckanext/
│   └── your_extension/
│       ├── themes/
│       │   └── your_theme/
│       │       ├── macros/
│       │       │   └── ui/
│       │       │       ├── component.html
│       │       │       ├── container.html
│       │       │       ├── data.html
│       │       │       ├── element.html
│       │       │       ├── feedback.html
│       │       │       ├── form.html
│       │       │       ├── meta.html
│       │       │       ├── misc.html
│       │       │       └── nav.html
│       │       ├── templates/
│       │       │   └── (your custom templates)
│       │       ├── assets/
│       │       │   ├── css/
│       │       │   ├── js/
│       │       │   └── images/
│       │       └── theme.py (optional - theme configuration)
│       └── plugin.py
```

## Registering a Theme

### 1. Define Your Theme in the Plugin Class

In your extension's `plugin.py` file, implement the `IConfigurer` and `ITheme` interfaces. The key method is `register_themes()` which returns a dictionary mapping theme names to `Theme` objects:

```python
import os
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.theming.lib import Theme

class YourExtensionPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITheme, inherit=True)

    def update_config(self, config_):
        # Add this plugin's templates to CKAN's list of template directories
        toolkit.add_template_directory(config_, 'themes/your_theme/templates')
        toolkit.add_public_directory(config_, 'themes/your_theme/assets')
        toolkit.add_resource('themes/your_theme/assets', 'your_extension_theme')

    def register_themes(self):
        # Return a dictionary of theme names to Theme objects
        root = os.path.dirname(os.path.abspath(__file__))
        return {
            'your_theme': Theme(
                os.path.join(root, 'themes/your_theme'),
                # Optionally specify a parent theme to extend
                # extends='parent_theme_name'
            ),
        }
```

### 2. Custom UI Implementation (Optional)

You can customize the macro loading mechanism by setting a custom UI class on the Theme. Create a custom UI class that extends the base UI implementation:

```python
from ckanext.theming.lib import MacroUI

class YourThemeUI(MacroUI):
    source = "your_extension/themes/your_theme/macros/ui.html"

    def __init__(self, app):
        super().__init__(app)
        # Additional initialization if needed
```

Then assign it to your theme:

```python
def register_themes(self):
    from .theme import YourThemeUI  # Import your custom UI class

    root = os.path.dirname(os.path.abspath(__file__))
    theme = Theme(os.path.join(root, 'themes/your_theme'))
    theme.UI = YourThemeUI  # Set custom UI class

    return {
        'your_theme': theme,
    }
```

### 3. Create Theme Macros

Your theme should provide a set of macros that can be used throughout CKAN templates. The `bare` theme provides a good example of the structure:

Create `themes/your_theme/macros/ui.html`:

```html
{% import "macros/ui/component.html" as component with context %}
{% import "macros/ui/container.html" as _container with context %}
{% import "macros/ui/data.html" as data with context %}
{% import "macros/ui/element.html" as element with context %}
{% import "macros/ui/feedback.html" as feedback with context %}
{% import "macros/ui/form.html" as _form with context %}
{% import "macros/ui/meta.html" as meta with context %}
{% import "macros/ui/misc.html" as misc with context %}
{% import "macros/ui/nav.html" as _nav with context %}

{# Element macros #}
{% set avatar = element.avatar %}
{% set badge = element.badge %}
{% set button = element.button %}
{% set divider = element.divider %}
{% set heading = element.heading %}
{% set image = element.image %}
{% set link = element.link %}
{% set tag = element.tag %}
{% set text = element.text %}
{% set text_block = element.text_block %}
{% set video = element.video %}
{% set icon = element.icon %}
{% set label = element.label %}

{# Navigation macros #}
{% set breadcrumb_item = _nav.breadcrumb_item %}
{% set breadcrumb_wrapper = _nav.breadcrumb_wrapper %}
{% set menu_wrapper = _nav.menu_wrapper %}
{% set menu_item = _nav.menu_item %}
{% set nav_wrapper = _nav.nav_wrapper %}
{% set nav_item = _nav.nav_item %}
{% set pagination = _nav.pagination %}
{% set tab_wrapper = _nav.tab_wrapper %}
{% set tab_item = _nav.tab_item %}
{% set dropdown_wrapper = _nav.dropdown_wrapper %}
{% set dropdown_item = _nav.dropdown_item %}
{% set sidebar = _nav.sidebar %}
{% set navbar = _nav.navbar %}
{% set breadcrumb_divider = _nav.breadcrumb_divider %}

{# Container macros #}
{% set accordion_wrapper = _container.accordion_wrapper %}
{% set accordion_item = _container.accordion_item %}
{% set card = _container.card %}
{% set column = _container.column %}
{% set container = _container.container %}
{% set grid = _container.grid %}
{% set panel = _container.panel %}
{% set row = _container.row %}
{% set section = _container.section %}
{% set jumbotron = _container.jumbotron %}
{% set well = _container.well %}
{% set media_object = _container.media_object %}
{% set list_group_item = _container.list_group_item %}

{# Meta macros #}
{% set header_block = meta.header_block %}
{% set footer_block = meta.footer_block %}
{% set account_block = meta.account_block %}

{# Data macros #}
{% set table_block = data.table_block %}
{% set table_head_block = data.table_head_block %}
{% set table_body_block = data.table_body_block %}
{% set table_row_block = data.table_row_block %}
{% set table_row = data.table_row %}
{% set table_cell = data.table_cell %}
{% set list_group = data.list_group %}
{% set definition_list = data.definition_list %}
{% set stat = data.stat %}
{% set chart = data.chart %}
{% set code_block = data.code_block %}

{# Form macros #}
{% set form_block = _form.form_block %}
{% set form_start = _form.form_start %}
{% set form_end = _form.form_end %}
{% set form_errors = _form.form_errors %}
{% set input = _form.input %}
{% set checkbox = _form.checkbox %}
{% set textarea = _form.textarea %}
{% set select = _form.select %}
{% set radio = _form.radio %}
{% set file_input = _form.file_input %}
{% set range_input = _form.range_input %}
{% set toggle_switch = _form.toggle_switch %}

{# Feedback macros #}
{% set alert = feedback.alert %}
{% set toast = feedback.toast %}
{% set modal = feedback.modal %}
{% set tooltip = feedback.tooltip %}
{% set popover = feedback.popover %}
{% set progress = feedback.progress %}
{% set spinner = feedback.spinner %}

{# Component macros #}
{% set group_item = component.group_item %}
{% set organization_item = component.organization_item %}
{% set package_item = component.package_item %}
{% set resource_item = component.resource_item %}

{# Miscellaneous macros #}
{% set datetime = misc.datetime %}
{% set spacer = misc.spacer %}
{% set divider_with_text = misc.divider_with_text %}
{% set truncate = misc.truncate %}
{% set badge_count = misc.badge_count %}
{% set skeleton_loader = misc.skeleton_loader %}
{% set notification = misc.notification %}
```

### 4. Implement Individual Macro Files

Each macro file should contain actual implementations following the patterns from the `bare` theme:

Example `themes/your_theme/macros/ui/element.html`:

```html
{%- macro badge(content) -%}
    <span class="badge">{{ content }}</span>
{%- endmacro %}

{%- macro button(content, type="button") -%}
    <button class="btn btn-{{ type }}" type="{{ type }}">{{ content }}</button>
{%- endmacro %}

{%- macro heading(content, level=1) -%}
    {%- set tag = "h" ~ level %}
    <{{ tag }} class="heading-{{ level }}">{{ content }}</{{ tag }}>
{%- endmacro %}

{%- macro link(content, href) -%}
    <a class="custom-link" href="{{ href or content }}">{{ content }}</a>
{%- endmacro %}

{# Add more element macros as needed #}
```

### 5. Provide Template Overrides

Create custom templates in `themes/your_theme/templates/` to override CKAN's default templates. Common templates to override include:

- `base.html` - The main base template
- `home/index.html` - Home page template
- `header.html` - Header section
- `footer.html` - Footer section

### 6. Add Assets

Include CSS, JavaScript, and image assets in `themes/your_theme/assets/` to style and enhance your theme.

## Using the Theme

Once your theme is properly registered:

1. Install your extension: `pip install -e .`
2. Add your plugin to CKAN's configuration: `ckan.plugins = ... your_extension`
3. The theme will be available and can be used throughout CKAN templates via the UI macros

## Best Practices

1. **Consistency**: Follow CKAN's UI macro patterns to ensure consistency across different themes
2. **Accessibility**: Ensure your theme follows accessibility guidelines
3. **Responsive Design**: Make sure your theme works well on different screen sizes
4. **Performance**: Optimize CSS and JavaScript files
5. **Documentation**: Document any custom macros or features in your theme

## Reference Implementation

The `bare` theme in this extension serves as a reference implementation showing the minimal required structure and macros. You can use it as a starting point for building more feature-rich themes.
