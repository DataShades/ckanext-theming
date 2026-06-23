# The Living Styleguide

One of the most powerful features of `ckanext-theming` is the built-in **Component Explorer**. This is a live, interactive styleguide that shows you exactly how every component looks and behaves in your **currently active theme**.

## Accessing the Styleguide

Once the extension is installed and enabled, add the following to your CKAN configuration file (e.g., `ckan.ini`):

```ini
ckan.ui.enable_theming_views = true
```

Now you can access the explorer at: `{your_ckan_url}/theming/`


## What You Can Find Here

### 1. Component Previews
Browse through all standard UI components (buttons, cards, forms, etc.). Each component page shows:

**Live Rendering**: See the component styled by your active theme.

**Example Variations**: Interactive states and variations (e.g., primary vs. secondary buttons, different alert styles).

**Arguments Reference**: A table of all standard arguments supported by the component (as declared in the component library schema).

### 2. JavaScript reference
The `/theming/util/` section provides a reference for the JavaScript functions available inside `sandbox.ui`:

```js
sb = ckan.sandbox();
const btn = sb.ui.button("Click");
```

### 3. Utility Function Reference
The `/theming/util/` section provides a reference for the `ui.util` functions, such as `id()`, `now()`, and the critical `attrs()` helper.



## Why Use the Explorer?

- **For Theme Developers**: It serves as a checklist. You can quickly see which components you haven't implemented yet or which ones need visual polish.
- **For Extension Developers**: It's a "menu" of available building blocks. You can copy-paste the usage examples directly into your templates.
- **For Designers**: You can test responsiveness and accessibility (ARIA attributes) of components in a clean, isolated environment.


## Adding Components and Examples to the Styleguide

Themes and extensions can dynamically add new components and extend existing examples in the Component Explorer. This allows you to document theme-specific components and show how they are configured.

The explorer scans the active theme's template directory for specific paths:

* `templates/theming/components/` - to find component registration files.
* `templates/theming/examples/{component_name}/` - to find examples for a given component.

### Directory Structure Example

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



### 1. Extending Existing Component Examples

To add custom examples to a standard component (like `button`, `card`, etc.), create an HTML file inside the active theme's `templates/theming/examples/{component_name}/` directory.

* The files are loaded in alphabetical/numerical order. Prefixing them with
  `001_`, `002_` helps control ordering. It's recommmended to start custom
  examples with prefix like `010_` or `020_`, to put them after all standard
  examples
* Inside the file, use the `show_example` helper to render the interactive code
  box. Note, content of this macro call must be wrapped into `raw` jinja2 tag,
  to avoid immediate rendering.

#### Example: Adding theme-specific button examples

Create `templates/theming/examples/button/020_my_theme_icons.html`:

```html
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

!!! note

    Wrap your example code in `{%- raw %}` ... `{%- endraw %}` inside the
    `show_example` call. This allows the Component Explorer to display both the
    live preview of the component and the raw Jinja code snippet for developers to
    copy.

### 2. Registering New Custom Components

If your theme or extension introduces entirely new components that are not part of the standard `ckanext-theming` library, you can register them on the styleguide sidebar and create dedicated documentation pages for them.

#### Step A: Register the Component Page
Create a template file named `{Component_Name}.html` in the active theme's `templates/theming/components/` directory. This file defines the description, overview, and arguments for your component.

It should extend `"theming/base_component.html"` and override the `overview` block.

!!! example "Registering the Callout component"

    Create `theming/components/callout.html`:

    ```html
    {%- extends "theming/base_component.html" -%}
    {%- set parametrized = parametrized or ["callout"] -%}

    {%- block overview -%}
        <p>
            Callouts are a snippet of information that draws attention to important content.
        </p>
    {%- endblock %}
    ```

    **`parametrized`**: Set this variable to a list of macro names whose parameters
    you want to document in the Arguments Reference table shown at the end of
    the page. By default this variable will include the name of the current
    component(matches the `{Component_Name}.html` part of the template)

#### Step B: Add Examples for the Custom Component

Once the component is registered, you can provide examples for it. Create an
example HTML file under
`templates/theming/examples/{Component_Name}/{example_name}.html`. Note, that
letter case in the name of examples folder must be the same as in the name of
HTML template: `MyCoMpOnEnT.html` -> `MyCoMpOnEnT/{example_name}.html`.

!!! example "Standard example for `callout`"

    Create `theming/examples/callout/001_standard.html`:

    ```html
    <h3>Standard</h3>

    {%- call ui.util.call(show_example) -%}
        {%- raw %}
            {%- call ui.util.call(ui.nds_callout) -%}
                {{ ui.heading("Title", level=4) }}
                <p>{{ lipsum(1) }}</p>
            {%- endcall %}
        {%- endraw %}
    {%- endcall %}
    ```

Once this is done done, your new custom component page will automatically
appear under the **Custom** category in the Component Explorer sidebar,
displaying your live previews, code blocks, and description.
