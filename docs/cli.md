# CLI Reference

The theming system provides comprehensive CLI tools for theme development,
auditing, and debugging.

## Development Workflow

While developing a theme, you can use these commands to ensure quality and
completeness:

**Auditing your theme**: Run `ckan theme component check` to see which
    standard components you still need to implement.

**Analyzing signatures**: Use `ckan theme component analyze link` to see the
    standard signature and arguments for a specific component.

**Checking template coverage**: Use `ckan theme template check` to verify
    that your theme implements all required CKAN templates.

**Debugging endpoints**: Use `ckan theme endpoint observe dataset.search`
    to see which template and variables are being used by a specific Flask
    route.

---

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
```

## `ckan theme component analyze`

Analyzes UI components and their implementations, showing detailed information about each component.

```bash
# Analyze all components for the configured theme
ckan theme component analyze

# Analyze specific components
ckan theme component analyze link button card
```

Output includes:

- Component name
- Type (Callable macro, Macro, etc.)
- Category (Essential, Recommended, Custom)
- Signature information

## `ckan theme component check`

Verifies that a theme implements all required UI components, showing missing and extra components.

```bash
# Check components for the configured theme
ckan theme component check
```

Output includes:

- Total number of implemented components
- Missing components by category
- Extra components (if any)


## `ckan theme template list`

Lists all template files in a theme.

```bash
# List templates for the configured theme
ckan theme template list
```

## `ckan theme template check`

Validates theme implementation against core CKAN templates, showing missing and extra templates.

```bash
# Check templates for the configured theme
ckan theme template check
```

Output includes:

- Total number of templates in the theme
- Missing templates by category
- Extra templates (if any)

## `ckan theme template analyze`

Analyzes theme templates, showing detailed information about their structure and relationships.

```bash
# Analyze all templates for the configured theme
ckan theme template analyze

# Analyze specific templates
ckan theme template analyze _header.html _footer.html

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
# Create a dump source file, to provide data for other commands
ckan theme endpoint dump --show-source > /path/to/source.yaml

# Dump all endpoints using parameter from the source file
ckan theme endpoint dump --user admin --source /path/to/source.yaml

# Dump specific endpoints
ckan theme endpoint dump --user admin  --endpoints=dataset.search --endpoints=dataset.read

# Dump with verbose output
ckan theme endpoint dump --user admin -v
```

Output includes:

- JSON object with endpoint names as keys
- Template name used by each endpoint
- Context variable types
- (with `-v`) Full context variable values

Options:

- `--user`: Authenticate as the specified user (required)
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

- `--include-frequency`: Show component count
