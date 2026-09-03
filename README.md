[![Tests](https://github.com/DataShades/ckanext-theming/workflows/Tests/badge.svg?branch=main)](https://github.com/DataShades/ckanext-theming/actions)

# ckanext-theming

This is a prototype of CKAN theming proposal. It defines a standard way to
customize the look and feel of a CKAN instance. It allows developers and
designers to create and apply themes without modifying core CKAN code, ensuring
easier upgrades and maintenance.

Theme implementations:

| Theme                                            | Description                                          |
|--------------------------------------------------|------------------------------------------------------|
| [Midnight blue portable][midnight-blue-portable] | CKAN's built-in theme(v2.12) rewritten with macros   |
| [NSW Design system][nsw-ds]                      | Mapping of [NSW DS][nsw-ds] components to CKAN theme |


[midnight-blue-portable]: https://github.com/dataShades/ckanext-midnight-blue-theme
[nsw-ds-theme]: https://github.com/DataShades/ckanext-nswdesignsystem
[nsw-ds]: https://designsystem.nsw.gov.au/
## Requirements

Compatibility with core CKAN versions:

| CKAN version | Compatible? |
|--------------|-------------|
| 2.11         | not tested  |
| 2.12         | yes         |

## Overview

The CKAN Theming Extension introduces a modern theming system that provides a
structured approach to UI customization. The system is built around a
macro-based UI framework that allows themes to provide consistent, reusable
components across CKAN instances.


**Traditional CKAN theme implementation:**

- Uses snippets for complex widgets
- Majority of UI elements is implemented directly as template code with HTML
- Contains framework-specific HTML with CSS classes directly in templates

Example: Input macros are called with Bootstrap classes as parameters

**Suggested macro-based approach:**

- Creates a collection of UI macros that abstract the underlying CSS framework
- Developers use semantic calls like `{{ ui.button("Click Me", style="primary") }}` instead of writing HTML
- Different themes can implement the same macros with different CSS frameworks
  (Bootstrap, Tailwind, Bulma, PicoCSS, etc.)
- The theme system allows switching between completely different CSS frameworks by changing one configuration
  setting
- Each theme provides its own implementation of the same set of macros using its specific CSS framework
  classes
- Provides a consistent API regardless of the underlying CSS framework

## Core philosophy

`ckanext-theming` is designed to be **optional and non-intrusive**. You don't
have to rewrite your existing code to use it. You can adopt it incrementally,
using it only for new features or specific components where you want to benefit
from theme portability.

For a deeper dive into what this project is (and isn't), check out the
[Philosophy & Goals](https://datashades.github.io/ckanext-theming/philosophy/)
page in our documentation.

## Installation

To install ckanext-theming:

1. Activate your CKAN virtual environment:
   ```sh
   pip install ckanext-theming
   ```

2. Add `theming` to the `ckan.plugins` setting in your CKAN config file:
   ```ini
   ckan.plugins = ... theming
   ```

3. Specify theme using `ckan.ui.theme` config option. Check available themes
   using `ckan theme list` CLI command
   ```ini
   ckan.ui.theme = classic-polyfill
   ```

## Usage

When theming plugin is active, UI macros can be used in templates:

```django
{{ ui.button("Click Me", style="primary", type="button") }}
{{ ui.card("Card content here", title="My Card") }}
{{ ui.alert("Success message", style="success") }}
```

Extensions can register themes by implementing the `ITheme` interface in their
plugin class:

```python
import ckan.plugins as p
from ckanext.theming.interfaces import ITheme
from ckanext.theming.lib import Theme

class MyThemePlugin(ITheme, p.SingletonPlugin):

    def register_themes(self):
        return [
            Theme("my_theme", "/path/to/my_theme/root"),
            Theme("extended_my_theme", "/path/to/extended_my_theme/root", parent="my_theme"),
        ]
```

If extension does not creates a new theme and instead just uses `ui.*`
components inside templates, it's recommended to add `ckanext-theming>=0.0.6`
to project dependencies and decorate extension's plugin class with
`themed_plugin` decorator. In this way, even if theming plugin is not activated
and no active theme is selected, `ui.*` components will remain available in
templates and fallback component library (either midnight-blue or classic,
depending on portal settings) will be automatically enabled.

```python
import ckan.plugins as p
from ckanext.theming.plugin import themed_plugin

@themed_plugin
class MyExtPlugin(p.SingletonPlugin):
    ...
```


### Creating custom themes

For detailed instructions on creating custom themes, see [theming guide](https://datashades.github.io/ckanext-theming/theme/basic).
