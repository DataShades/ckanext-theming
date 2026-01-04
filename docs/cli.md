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

# Include all blocks in the analysis
ckan theme template analyze --with-all-blocks
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
- `--with-all-blocks`: Include all blocks in the output

## `ckan theme endpoint list`

Lists all registered Flask endpoints in the application.

```bash
# List all registered Flask endpoints
ckan theme endpoint list
```

## `ckan theme endpoint variants`

Lists variants of Flask endpoints, showing URL rules, methods, arguments, and defaults.

```bash
# List variants for all endpoints
ckan theme endpoint variants

# List variants for specific endpoints
ckan theme endpoint variants dataset.search dataset.read
```

Output includes:

- Endpoint name
- URL rule
- HTTP methods
- Arguments
- Defaults

Arguments:

- `endpoints` (optional): Specific endpoints to analyze (defaults to all endpoints)

## `ckan theme endpoint observe`

Observes the template and context variables used by a specific Flask endpoint.

```bash
# Observe a specific endpoint
ckan theme endpoint observe dataset.search

# Observe an endpoint with parameters
ckan theme endpoint observe dataset.read id=my-dataset

# Observe an endpoint with verbose output
ckan theme endpoint observe dataset.read id=my-dataset -v

# Observe an endpoint with authentication
ckan theme endpoint observe dataset.read --auth-user admin id=my-dataset

# Observe an endpoint with different HTTP method
ckan theme endpoint observe dataset.read --method post id=my-dataset
```

Output includes:

- Template name used by the endpoint
- Context variable types
- (with `-v`) Full context variable values

Arguments:

- `endpoint`: The Flask endpoint to observe
- Additional arguments to pass to the endpoint (format: NAME=VALUE)

Options:

- `-v, --verbose`: Show full context variables instead of just their types
- `--auth-user`: Authenticate as the specified user
- `--method`: HTTP method to use (default: get)
- `--ignore`: Context variables to ignore (can be specified multiple times)

## `ckan theme endpoint dump`

Dumps templates and context variables used by Flask endpoints in JSON format.

```bash
# Dump all endpoints with required data
ckan theme endpoint dump --auth-user admin --user testuser --package testpkg --resource testres --resource-view testview --organization testorg --group testgroup

# Dump specific endpoints
ckan theme endpoint dump --auth-user admin --user testuser --package testpkg --resource testres --resource-view testview --organization testorg --group testgroup --endpoints=dataset.search --endpoints=dataset.read

# Dump with verbose output
ckan theme endpoint dump --auth-user admin --user testuser --package testpkg --resource testres --resource-view testview --organization testorg --group testgroup -v
```

Output includes:

- JSON object with endpoint names as keys
- Template name used by each endpoint
- Context variable types
- (with `-v`) Full context variable values

Options:

- `--auth-user`: Authenticate as the specified user (required)
- `--user`: User ID to use for endpoint parameters (required)
- `--package`: Package ID to use for endpoint parameters (required)
- `--resource`: Resource ID to use for endpoint parameters (required)
- `--resource-view`: Resource view ID to use for endpoint parameters (required)
- `--organization`: Organization ID to use for endpoint parameters (required)
- `--group`: Group ID to use for endpoint parameters (required)
- `--ignore`: Context variables to ignore (can be specified multiple times)
- `--endpoints`: Specific endpoints to dump (can be specified multiple times)
- `-v, --verbose`: Show full context variables instead of just their types

## `ckan theme template component-usage`

Analyzes template files to identify which UI components are used in each template.

```bash
# Analyze component usage in all templates
ckan theme template component usage

# Show detailed usage information
ckan theme template component usage --include-frequency
```

Output includes:

- List of UI unknown and unused components
- List of UI components used in the template
- Count of each component usage

Options:

- `-t, --theme`: Specify the theme to analyze (defaults to configured theme)
- `--include-frequency`: Show component count

## Common Options

Most theme commands support the `--theme` option to specify which theme to operate on:

```bash
# Use the configured theme (from ckan.ui.theme config)
ckan theme component list

# Explicitly specify a theme
ckan theme component list -t mytheme
```

If no theme is specified, the commands will use the theme configured in the `ckan.ui.theme` configuration option.
