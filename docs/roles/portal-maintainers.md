# Portal maintainers guide

As a **Portal Maintainer** (or Site Administrator), your role is to configure the CKAN portal, integrate chosen extensions, and manage branding customizations. This guide focuses on configuring themes, safely applying local customizations, and maintaining portals across upgrades.


## Core maintenance goals

**Branding & Theme Swappability**: Configure the site's layout and color palettes to match organization guidelines. Maintain the ability to swap themes without breaking site features.

**Upgrade Stability**: Avoid customizations that lead to "upgrade lock" (where upgrading CKAN or extensions breaks your custom templates).

**Consistent User Experience**: Ensure that components from different third-party extensions share a cohesive visual styling.


## Theme configuration

The active theme is controlled by the `ckan.ui.theme` setting in your CKAN configuration file (`.ini`):

```ini
ckan.plugins = theming nds_ui_plugin nsw_design_system_plugin
ckan.ui.theme = nsw-design-system
```

You can discover all registered themes on your system and their inheritance lineages using the CKAN CLI:
```bash
ckan theme list
```


## Applying custom styling safely

If you need to make cosmetic adjustments (like altering colors, font sizes, or paddings) to match local branding, follow these best practices:

### 1. Prefer `_extra_class` over custom CSS wrappers
When calling standard macros, pass custom class names via the `_extra_class` argument. This appends your class to the theme's native layout container safely:
```django
{{ ui.button("Join Us", href="/join", _extra_class="my-brand-glow") }}
```

### 2. Declare custom styles in local stylesheets
Avoid editing core theme stylesheets or the component library files. Put custom CSS rules into your own extension's asset files, using the custom classes declared in `_extra_class`.


## Overriding components locally

If a third-party extension registers a custom component (e.g. `map_viewer`) but the active theme does not style it properly, you can override its styling locally.

### Step-by-step component override
1. Create a custom extension (or use your portal's local customization extension).
2. Register an additional theme UI source in your plugin class:
   ```python
   def get_additional_theme_ui_sources(self):
       return ["templates/macros/local_overrides.html"]
   ```
3. Inside `local_overrides.html`, define the matching macro name:
   ```django
   {%- macro map_viewer(data_url) -%}
       {# Define your custom map viewer HTML structure #}
       <div class="my-custom-map-wrapper">
           <iframe src="{{ data_url }}"></iframe>
       </div>
   {%- endmacro -%}
   ```
This will take precedence over the fallback component provided by the extension, allowing you to control its styling completely.
