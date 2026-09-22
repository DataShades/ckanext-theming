# Exposing extension components

As an extension developer, you often need to introduce custom UI components
specific to your extension's features, such as a `dataset_card`,
`harvest_status` banner, `spatial_map` widget, or `data_dictionary_table`.

`ckanext-theming` allows extensions to expose default component implementations
that work automatically across all themes out of the box, while giving theme
developers and portal maintainers full power to override or restyle them.

---

## Adding default component sources via interface

To expose components from your extension, implement the `ITheme` interface in
your plugin class and return your macro template paths from
`get_default_theme_ui_sources()`.

### Step 1: Implement `ITheme` in `plugin.py`

```python title="plugin.py"
import ckan.plugins as p
from ckanext.theming.interfaces import ITheme


class MyExtensionPlugin(ITheme, p.SingletonPlugin):

    def get_default_theme_ui_sources(self) -> list[str]:
        # Return path to template file containing default component macros
        return ["macros/my_extension_defaults.html"]
```

### Why use `get_default_theme_ui_sources()`?

- **Automatic Fallback**: If the active portal theme does not explicitly
  implement your custom component, `ckanext-theming` automatically falls back
  to your default macro implementation.
- **Lower Priority by Design**: Components registered via
  `get_default_theme_ui_sources()` have lower priority than theme macros
  (`macros/ui.html`) and additional sources
  (`get_additional_theme_ui_sources()`). This ensures theme developers can
  easily replace your components with theme-native markup without needing to
  modify your extension.

---

## Building custom components from native components

The best practice when writing default component macros is to **build custom
components using native `ui.*` primitives** rather than writing raw HTML with
framework-specific CSS classes (such as Bootstrap `btn btn-primary` or Tailwind
`bg-blue-500`).

When your component delegates to native primitives (`ui.card`, `ui.badge`,
`ui.button`, `ui.icon`, `ui.alert`, etc.), it automatically inherits the active
theme's styling, colors, borders, and typography!

### Example 1: Custom `dataset_card` component

Here is an example of a `dataset_card` custom component built entirely from native `ui.*` components:

```django title="templates/macros/my_extension_defaults.html"
{%- macro dataset_card(title, notes, formats=[], href=None, organization=None) -%}
    {% do kwargs %}
    {% set card_title %}
        {% if href %}
            {{ ui.link(title, href=href) }}
        {% else %}
            {{ title }}
        {% endif %}
    {% endset %}

    {% call ui.util.call(ui.card, title=card_title, _extra_class="dataset-card") %}
        {% if organization %}
            <div class="dataset-card-org">
                {{ ui.icon("building") }} {{ organization }}
            </div>
        {% endif %}

        {% if notes %}
            <p class="dataset-card-notes">{{ notes|truncate(160) }}</p>
        {% endif %}

        {% if formats %}
            <div class="dataset-card-formats">
                {% for fmt in formats %}
                    {{ ui.badge(fmt, style="info", _extra_class="me-1") }}
                {% endfor %}
            </div>
        {% endif %}

        {% if href %}
            <div class="dataset-card-actions mt-3">
                {{ ui.button(_("View Dataset"), href=href, style="secondary", size="sm") }}
            </div>
        {% endif %}
    {% endcall %}
{%- endmacro -%}
```

Notice how this component uses:
- `ui.card` for the outer structure
- `ui.link` for title navigation
- `ui.icon` for organization icons
- `ui.badge` for format tags
- `ui.button` for action links

When this `dataset_card` is rendered in **Midnight Blue**, it looks natively
like Midnight Blue. When rendered in **NSW Design System**, it adapts to NSW DS
cards, badges, and buttons automatically.

---

### Example 2: Custom `harvest_status` widget component

Here is an example of a `harvest_status` component built using `ui.alert`, `ui.icon`, `ui.badge`, and `ui.button`:

```django title="templates/macros/my_extension_defaults.html"
{%- macro harvest_status(status, last_run=None, errors_count=0, job_url=None) -%}
    {% set alert_style = "success" if status == "finished" else ("danger" if status == "failed" else "warning") %}
    {% set status_icon = "check-circle" if status == "finished" else ("exclamation-triangle" if status == "failed" else "clock") %}
    {% do kwargs.update({"style": alert_style})%}

    {% call ui.util.call(ui.alert, **kwargs) %}
        <div>
            {{ ui.icon(status_icon) }}
            <strong>{{ _("Harvester Status:") }}</strong>
            {{ ui.badge(status|capitalize, style=alert_style) }}

            {% if last_run %}
                <br />
                <span>
                    {{ _("Last run:") }} {{ last_run }}
                </span>
            {% endif %}

            {% if errors_count > 0 %}
                <br />
                <span>
                    ({{ errors_count }} {{ _("errors recorded") }})
                </span>
            {% endif %}
        </div>

        {% if job_url %}
            <div>
                {{ ui.button(_("View Job"), href=job_url, style="secondary", size="sm") }}
            </div>
        {% endif %}
    {% endcall %}
{%- endmacro -%}
```

---

## How extension users & theme developers replace these components

Because default components registered via `get_default_theme_ui_sources()` have
the lowest priority, extension users and theme authors can customize or replace
them easily:

### Replacement by Theme Developers

A theme developer who wants to provide a custom visual presentation for your
`dataset_card` or `harvest_status` simply adds a macro with the exact same name
to their theme's `templates/macros/ui.html`:

```django title="my_theme/templates/macros/ui.html"
{# Theme-native override for extension's harvest_status #}
{%- macro harvest_status(status, last_run=None, errors_count=0, job_url=None) -%}
    {% do kwargs %}
    <div class="nsw-in-page-alert nsw-in-page-alert--{{ 'success' if status == 'finished' else 'warning' }}">
        <h4 class="nsw-in-page-alert__title">Harvest Status: {{ status }}</h4>
        {% if job_url %}
            <a href="{{ job_url }}" class="nsw-button nsw-button--secondary">View Job Details</a>
        {% endif %}
    </div>
{%- endmacro -%}
```

### Replacement by Portal Maintainers / Extension Users

Portal maintainers who use your extension can also override your component
specifically for their site by registering an additional theme source using
`ITheme.get_additional_theme_ui_sources()`:

```python title="plugin.py"
class LocalCustomizationPlugin(ITheme, p.SingletonPlugin):

    def get_additional_theme_ui_sources(self) -> list[str]:
        return ["macros/local_harvest_overrides.html"]
```

```django title="templates/macros/local_harvest_overrides.html"
{%- macro harvest_status(status, last_run=None, errors_count=0, job_url=None) -%}
    {% do kwargs %}
    {# Portal-specific harvest status layout #}
    <div class="custom-portal-harvest-box status-{{ status }}">
        <span>Status: {{ status }}</span>
        {% if job_url %}<a href="{{ job_url }}">Logs</a>{% endif %}
    </div>
{%- endmacro -%}
```

---

## Summary of component resolution order

| Source Type                     | Interface Method                    | Priority        | Intended Audience                    | Use Case                                                    |
|:--------------------------------|:------------------------------------|:----------------|:-------------------------------------|:------------------------------------------------------------|
| **Additional Theme UI Sources** | `get_additional_theme_ui_sources()` | **Highest** | Portal Maintainers / Site Extensions | Local portal overrides & custom tweaks                      |
| **Theme Macros**                | Defined in theme `ui.html`          | **Medium**  | Theme Developers                     | Theme-native implementation of standard & custom components |
| **Default Theme UI Sources**    | `get_default_theme_ui_sources()`    | **Lowest**  | Extension Developers                 | Reusable, theme-portable default component fallbacks        |

For full details on overriding components in active themes, see [Customizing components](customizing-components.md).
