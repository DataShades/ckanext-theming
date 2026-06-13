# The Living Styleguide

One of the most powerful features of `ckanext-theming` is the built-in **Component
Explorer**. This is a live, interactive styleguide that shows you exactly how
every component looks and behaves in your **currently active theme**.

## Accessing the Styleguide

Once the extension is installed and enabled, add `#!ini
ckan.ui.enable_theming_views = true` to the CKAN config file. Now you can
access the explorer at: `{your_ckan_url}/theming/`

## What you can find here

### 1. Component Previews
Browse through all standard UI components (buttons, cards, forms, etc.). Each
component page shows:

- Live Rendering: See the component styled by your active theme.
- Example Variations: Many components show different states (e.g., primary
  vs. secondary buttons, different alert styles).
- Arguments Reference: A table of all standard arguments supported by the
  component.

### 2. Interactive Examples
The explorer isn't just static. Many components include interactive examples
that allow you to see how they respond to different data or configurations.

### 3. Utility Function Reference
The `/theming/util/` section provides a reference for the `ui.util` functions,
such as `id()`, `now()`, and the critical `attrs()` helper.

## Why use the explorer?

- For Theme Developers: It serves as a checklist. You can quickly see which
  components you haven't implemented yet or which ones need visual polish.
- For Extension Developers: It's a "menu" of available building blocks. You
  can copy-paste the usage examples directly into your templates.
- For Designers: You can test responsiveness and accessibility (ARIA
  attributes) of components in a clean, isolated environment.

## Customizing Examples

If you are developing a new theme, you can provide your own examples for your
custom components. The explorer automatically scans your theme's
`templates/theming/examples/{component_name}/` directory for additional
snippets to display.
