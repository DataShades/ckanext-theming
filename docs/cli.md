# CLI

## `ckan theme list`

Lists all available themes in the system, showing their paths and inheritance hierarchy.

```bash
ckan theme list
```

Output includes:

- Theme name
- Path to the theme directory
- Parent theme lineage (if any)

## `ckan theme create`

Creates a new theme with all required structure and templates by copying the bare theme.

```bash
# Create a new theme in the current directory
ckan theme create mytheme

# Create a new theme in a specific location
ckan theme create mytheme /path/to/themes
```

Arguments:

- `name`: Name of the new theme
- `location` (optional): Directory where the theme should be created (defaults to current directory)

## `ckan theme component list`

Lists all available UI components for a specific theme.

```bash
# List components for the configured theme
ckan theme component list

# List components for a specific theme
ckan theme component list -t mytheme
```

Options:

- `-t, --theme`: Specify the theme to analyze (defaults to configured theme)

## `ckan theme component analyze`

Analyzes UI components and their implementations, showing detailed information about each component.

```bash
# Analyze all components for the configured theme
ckan theme component analyze

# Analyze specific components
ckan theme component analyze link button card

# Analyze components for a specific theme
ckan theme component analyze -t mytheme
```

Output includes:

- Component name
- Type (Callable macro, Macro, etc.)
- Category (Essential, Recommended, Custom)
- Signature information

Options:

- `-t, --theme`: Specify the theme to analyze (defaults to configured theme)

## `ckan theme component check`

Verifies that a theme implements all required UI components, showing missing and extra components.

```bash
# Check components for the configured theme
ckan theme component check

# Check components for a specific theme
ckan theme component check -t mytheme
```

Output includes:

- Total number of implemented components
- Missing components by category
- Extra components (if any)

Options:

- `-t, --theme`: Specify the theme to check (defaults to configured theme)

## `ckan theme template list`

Lists all template files in a theme.

```bash
# List templates for the configured theme
ckan theme template list

# List templates for a specific theme
ckan theme template list -t mytheme
```

Options:

- `-t, --theme`: Specify the theme to analyze (defaults to configured theme)

## `ckan theme template check`

Validates theme implementation against core CKAN templates, showing missing and extra templates.

```bash
# Check templates for the configured theme
ckan theme template check

# Check templates for a specific theme
ckan theme template check -t mytheme
```

Output includes:

- Total number of templates in the theme
- Missing templates by category
- Extra templates (if any)

Options:

- `-t, --theme`: Specify the theme to check (defaults to configured theme)

## `ckan theme template analyze`

Analyzes theme templates, showing detailed information about their structure and relationships.

```bash
# Analyze all templates for the configured theme
ckan theme template analyze

# Analyze specific templates
ckan theme template analyze _header.html _footer.html

# Analyze templates for a specific theme
ckan theme template analyze -t mytheme

# Show relative filenames
ckan theme template analyze --relative-filename
```

Output includes:

- Template name
- Category (Essential, Recommended, Custom)
- Filename
- Included templates
- Extended templates
- Template hierarchy
- Defined blocks
- All available blocks (including from parent templates)

Options:

- `-t, --theme`: Specify the theme to analyze (defaults to configured theme)
- `--relative-filename`: Show relative file paths instead of absolute paths

## Common Options

Most theme commands support the `--theme` option to specify which theme to operate on:

```bash
# Use the configured theme (from ckan.ui.theme config)
ckan theme component list

# Explicitly specify a theme
ckan theme component list -t mytheme
```

If no theme is specified, the commands will use the theme configured in the `ckan.ui.theme` configuration option.
