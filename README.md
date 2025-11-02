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


## Installation

**TODO:** Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-theming:

1. Activate your CKAN virtual environment, for example:

   ```sh
   pip install ckanext-theming
   ```

2. Add `theming` to the `ckan.plugins` setting in your CKAN
   config file.

# Overview

The CKAN Theming Extension introduces a theming system based on Jinja2
templates and a configurable UI.  Themes can extend existing themes, providing
a layered approach to customization. Key features:

* Extensions can register themes, making them available for selection.
* Administrators can switch between themes via the CKAN config file.
* Themes define a UI that provides macros for common elements, allowing for
  consistent and reusable components.
* The system is designed to be extensible, allowing for advanced customization
  through custom macros and UI implementations.
* A CLI is provided for debugging themes, listing available themes and
  components.

## Config settings

None at present

**TODO:** Document any optional config settings here. For example:

```ini
# The minimum number of hours to wait before re-checking a resource
# (optional, default: 24).
ckanext.theming.some_setting = some_default_value
```

## Developer installation

To install ckanext-theming for development, activate your CKAN virtualenv and
do:

```sh
git clone https://github.com/DataShades/ckanext-theming.git
cd ckanext-theming
pip install -e ".[dev]"
```

## Tests

To run the tests, do:

```sh
pytest --ckan-ini=test.ini
```

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
