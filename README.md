[![Tests](https://github.com/DataShades/ckanext-theming/workflows/Tests/badge.svg?branch=main)](https://github.com/DataShades/ckanext-theming/actions)

# ckanext-theming

This is a prototype of CKAN theming proposal. It defines a standard way to
customize the look and feel of a CKAN instance. It allows developers and
designers to create and apply themes without modifying core CKAN code, ensuring
easier upgrades and maintenance.

## Requirements

Compatibility with core CKAN versions:

| CKAN version | Compatible? |
|--------------|-------------|
| 2.11         | no          |
| 2.12         | yes         |

## Overview

The CKAN Theming Extension introduces a modern theming system that provides a
structured approach to UI customization. The system is built around a
macro-based UI framework that allows themes to provide consistent, reusable
components across CKAN instances.


Traditional CKAN Theme Implementation

 - Uses snippets for complex widgets
 - Majority of UI elements is implemented directly as template code with HTML
 - Contains framework-specific HTML with CSS classes directly in templates
 - Example: Input macros are called with Bootstrap classes as parameters

Suggested macro-based approach

 - Creates a collection of UI macros that abstract the underlying CSS framework
 - Developers use semantic calls like `{{ ui.button("Click Me", style="primary") }}` instead of writing HTML
 - Different themes can implement the same macros with different CSS frameworks (Bootstrap 5, Tailwind, Bulma,
   Pico CSS, etc.)
 - The theme system allows switching between completely different CSS frameworks by changing one configuration
   setting
 - Each theme provides its own implementation of the same set of macros using its specific CSS framework
   classes
 - Provides a consistent API regardless of the underlying CSS framework


The key benefit is the complete separation of content structure from styling. This means users can
completely change the visual appearance of their CKAN instance (from Bootstrap to Tailwind, for example) by
just changing the theme configuration, without modifying any templates or code.



## Installation

To install ckanext-theming:

1. Activate your CKAN virtual environment:

   ```sh
   pip install ckanext-theming
   ```

1. Add `theming` to the `ckan.plugins` setting in your CKAN config file:

   ```ini
   ckan.plugins = ... theming
   ```

1. Specify theme using `ckan.ui.theme` config option. Check available themes
   using `ckan theme list` CLI command

   ```ini
   ckan.ui.theme = bare
   ```

## Usage

### Registering Themes

Extensions can register themes by implementing the `ITheme` interface in their
plugin class:

```python
import ckan.plugins as p
from ckanext.theming.interfaces import ITheme
from ckanext.theming.lib import Theme

class MyThemePlugin(ITheme, p.SingletonPlugin):

    def get_ui(self):
        return {
            "my_theme": Theme("/path/to/my_theme/root"),
            "extended_my_theme": Theme("/path/to/extended_my_theme/root", parent="my_theme"),
        }
```

### Using UI Macros

Once a theme is active, UI macros can be used in templates:

```jinja
{{ ui.button("Click Me", style="primary", type="button") }}
{{ ui.card(title="My Card", content="Card content here") }}
{{ ui.alert("Success message", style="success") }}
```

### Creating Custom Themes

For detailed instructions on creating custom themes, see [theming guide](https://datashades.github.io/ckanext-theming/theme/).
