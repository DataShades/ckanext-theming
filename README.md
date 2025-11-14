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
 - Uses template inheritance with base templates (base.html, page.html)
 - Contains inline HTML with CSS framework-specific classes directly in templates
 - Form macros and UI elements are implemented directly as template code with HTML
 - Example: Input elements have direct Bootstrap classes embedded in the macro

ckanext-theming Macro-Based Approach
 - Creates a collection of UI macros that abstract the underlying CSS framework
 - Developers use semantic calls like {{ ui.button("Click Me", style="primary") }} instead of writing HTML
 - Different themes can implement the same macros with different CSS frameworks (Bootstrap 5, Tailwind, Bulma,
   Pico CSS, etc.)
 - The theme system allows switching between completely different CSS frameworks by changing one configuration
   setting
 - Each theme provides its own implementation of the same set of macros using its specific CSS framework
   classes
 - Provides a consistent API regardless of the underlying CSS framework

How Users Can Customize Themes with Different CSS Frameworks

1. Theme Registration: Extensions can register new themes by implementing the ITheme interface and providing a
   Theme object
1. Macro Implementation: Each theme implements the same set of macros using their chosen CSS framework's
   classes
1. Configuration: Users can switch themes by setting ckan.ui.theme = theme-name in their config
1. Template Usage: Templates use semantic calls like {{ ui.button(...) }} instead of framework-specific HTML
1. Flexibility: The same CKAN templates can work with different CSS frameworks by simply changing the active
   theme

The key benefit is the complete separation of content structure from styling. This means users can
completely change the visual appearance of their CKAN instance (from Bootstrap to Tailwind, for example) by
just changing the theme configuration, without modifying any templates or code.



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

## Usage

### Registering Themes

Extensions can register themes by implementing the `ITheme` interface in their
plugin class:

```python
import ckan.plugins as plugins
from ckanext.theming.lib import MacroUI

class MyThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.ITheme, inherit=True)

    def info(self):
        return {
            'name': 'my_theme',
            'title': 'My Theme',
            'description': 'A custom theme implementation'
        }

    def get_ui(self):
        return MacroUI(source="my_extension/themes/my_theme/macros/ui.html")
```

### Using UI Macros

Once a theme is active, UI macros can be used in templates:

```html
{{ ui.button("Click Me", style="primary", type="button") }}
{{ ui.card(title="My Card", content="Card content here") }}
{{ ui.alert("Success message", style="success") }}
```

### Creating Custom Themes

For detailed instructions on creating custom themes, see [docs/theme.md](docs/theme.md).

## Configuration

The extension provides CLI commands for theme management:

```bash
# List available themes
ckan theme list

# Show theme components
ckan theme components

# Debug theme issues
ckan theme debug
```

## Development

### Installation

To install ckanext-theming for development:

```sh
git clone https://github.com/DataShades/ckanext-theming.git
cd ckanext-theming
pip install -e ".[dev]"
```

### Running Tests

```sh
pytest --ckan-ini=test.ini
```

### Documentation

Documentation is available in the `docs/` directory:
- [theme.md](docs/theme.md) - Guide to creating and registering themes
- [library/](docs/library/) - Documentation for individual UI macro components

## Contributing

This extension is designed to be extensible and welcomes contributions. See the individual macro documentation in `docs/library/` for details on the available components and how to extend them.

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
