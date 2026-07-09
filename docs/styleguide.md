# The Component Explorer

One of the most useful features of `ckanext-theming` is the built-in
**Component Explorer**. This is a live styleguide that shows you exactly how
every component looks and behaves in your **currently active theme**.

## Accessing the Styleguide

Once the extension is installed and enabled, add the following to your CKAN configuration file (e.g., `ckan.ini`):

```ini
ckan.ui.enable_theming_views = true
```

Now you can access the explorer at: `{your_ckan_url}/theming/`

/// admonition
    type: note

This endpoint is disabled by default, because there are no reasons to enable it
unless you are actively developing the portal's theme.

///


## What You Can Find Here

### 1. Component Previews

Browse through all standard UI components (buttons, cards, forms, etc.). Each
component page shows:

**Live Rendering**: See the component styled by your active theme.

**Example Variations**: Interactive states and variations (e.g., primary vs. secondary buttons, different alert styles).

**Arguments Reference**: A table of all standard arguments supported by the component (as declared in the component library schema).

### 2. JavaScript reference

The `/theming/js/` section provides a reference for the JavaScript functions
available inside `sandbox.ui`:

```js
sb = ckan.sandbox();
const btn = sb.ui.button("Click");
```

### 3. Utility Function Reference

The `/theming/util/` section provides a reference for the `ui.util` functions,
such as `id()`, `now()`, and the critical `attrs()` helper.



## Why Use the Explorer?

- **For Theme Developers**: It serves as a checklist. You can quickly see which
  components you haven't implemented yet or which ones need visual polish.
- **For Extension Developers**: It's a "menu" of available building blocks. You
  can copy-paste the usage examples directly into your templates.
- **For Designers**: You can test responsiveness and accessibility (ARIA
  attributes) of components in a clean, isolated environment.


## Adding Components and Examples to the Styleguide

Themes and extensions can dynamically add new components and extend existing
examples in the Component Explorer. This allows you to document theme-specific
components and show how they are configured.

The explorer scans the active theme's template directory for specific paths:

* `templates/theming/components/` - to find component registration files.
* `templates/theming/examples/{component_name}/` - to find examples for a given component.

/// admonition | Directory Structure Example
    type: example

Here is how files can be organized organized in the theme that extends stylefguide:

```text
mytheme/
└── templates/
    └── theming/
        ├── components/
        │   └── my_callout.html        # Registers my_callout component page
        └── examples/
            ├── button/
            │   └── 020_standard.html  # Extends standard 'button' component with mytheme examples
            └── my_callout/
                └── 001_standard.html  # Adds a 'Standard' example for the my_callout component
```

///

### Extending Existing Component Examples

To add custom examples to a standard component (like `button`, `card`, etc.), create an HTML file inside the active theme's `templates/theming/examples/{component_name}/` directory.

* The files are loaded in alphabetical/numerical order. Prefixing them with
  `001_`, `002_` helps control ordering. It's recommended to start custom
  examples with prefix like `010_` or `020_`, to put them after all standard
  examples
* Inside the file, use the `show_example` helper to render the interactive code
  box. Note, content of this macro call must be wrapped into `raw` jinja2 tag,
  to avoid immediate rendering.

/// admonition | Adding theme-specific button examples
    type: example

```django  title="templates/theming/examples/button/020_my_theme_icons.html"
<h3>My theme: icons</h3>
<p>
    My theme adds support of button icons. Provide <code>icon</code> parameter to add
    the icon before the button's label. Use <code>suffix_icon</code> to put icon after the label.
</p>

{%- call ui.util.call(show_example) -%}
    {%- raw %}
        {{ ui.button("Primary", icon="home") }}
        {{ ui.button("Secondary", suffix_icon="star") }}
        {{ ui.button("Both sides", icon="cog", suffix_icon="search") }}
    {%- endraw %}
{%- endcall %}
```

///


/// admonition
    type: hint

Wrap your example code in `#!django {%- raw %}` ... `#!django {%- endraw %}`
inside the `show_example` call. This allows the Component Explorer to display
both the live preview of the component and the raw Jinja code snippet for
developers to copy.

///

### Registering New Custom Components

If your theme or extension introduces entirely new components that are not part
of the standard `ckanext-theming` library, you can register them on the
styleguide sidebar and create dedicated documentation pages for them.

#### Step A: Register the Component Page

Create a template file named `{component_name}.html` in the active theme's
`templates/theming/components/` directory. This file defines the description,
overview, and arguments for your component.

It should extend `"theming/base_component.html"` and override the `overview` block.

/// admonition | Registering the Callout component
    type: example

```django title="templates/theming/components/callout.html"
{%- extends "theming/base_component.html" -%}

{%- block overview -%}
    <p>
        Callouts are a snippet of information that draws attention to important content.
    </p>
{%- endblock %}
```

///

/// tip

At the bottom of the component page you'll see an empty table. It will include
argument description for your macro, once you provide it.

Create `components.yaml` at the root folder of your theme and add definition of
custom components into it. Make sure that definitions follow the structure from
the example, to avoid parsing errors:

```yaml title="my_theme/components.yaml"
callout: # (1)!
  description: | # (2)!
    Callouts are a snippet of information that draws attention to important content.
  arguments: # (3)!
    content: # (4)!
      description: | # (5)!
        The content of the callout. This can include text, links, or other HTML elements.
    style: # (6)!
        description: Color scheme for the callout
        type: str # (7)!
```

1. Top-level key is a name of the component.
2. Brief component description explains its purpose.
3. Every key inside `arguments` is a name of possible macro argument.
4. Majority of components have `content` argument on the first position.
5. Brief description of the argument's role
6. It's recommended to provide a `type` in addition to the `description` for
   all arguments other than `content`.
7. This type is used for documentation only and you can use arbitrary text
   here, i.e. `#!yaml type: "primary", "secondary" or "danger"`.

By default, argument table is rendered for component with the name matching the
name of template, i.e. `callout` in this example. If the component name has
prefix that is missing from the template, or you want to render multiple tables
for related components, define in the global scope of the template a variable
`parametrized` with list of all component names that must be described.

```django title="templates/theming/components/callout.html"
{%- extends "theming/base_component.html" -%}
{%- set parametrized = ["callout", "callout_wrapper"] -%}

{%- block overview -%}
    ...
{%- endblock %}
```


///

#### Step B: Add Examples for the Custom Component

Once the component is registered, you can provide examples for it. Create an
example HTML file under
`templates/theming/examples/{component_name}/{example_name}.html`. Note, that
letter case in the name of examples folder must be the same as in the name of
HTML template: `MyCoMpOnEnT.html` -> `MyCoMpOnEnT/{example_name}.html`.

/// admonition | Standard example for `callout`
    type: example

```django title="templates/theming/examples/callout/001_standard.html"
<h3>Standard</h3>

{%- call ui.util.call(show_example) -%}
    {%- raw %}
        {%- call ui.util.call(ui.callout) -%}
            {{ ui.heading("Title", level=4) }}
            <p>{{ lipsum(1) }}</p>
        {%- endcall %}
    {%- endraw %}
{%- endcall %}
```

///

Once this is done done, your new custom component page will automatically
appear under the **Custom** category in the Component Explorer sidebar,
displaying your live previews, code blocks, and description.
