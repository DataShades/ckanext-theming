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
{{ ui.button("Click Me", type="primary") }}
{{ ui.card(title="My Card", content="Card content here") }}
{{ ui.alert("Success message", type="success") }}
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
