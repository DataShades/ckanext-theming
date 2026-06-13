# Recipes & Best Practices

This page contains a collection of common patterns and solutions for real-world
theming tasks.

## 1. Adding custom data attributes

If you need to pass custom `data-*` attributes to a component (e.g., for a
JavaScript module), use the `data` parameter.

```django
{{ ui.button(_("Save"), data={"module": "my-module"}) }}
```


## 2. Adding custom CSS classes

Sometimes you want to add a specific class to a component without overriding
its entire implementation. Standard components support the `_extra_class`
parameter for this purpose.


```django
{{ ui.button(_("Big Button"), _extra_class="my-custom-big-class") }}
```


This will result in:
`#!html <button class="btn btn-primary my-custom-big-class" ...>`

## 3. Conditional wrappers

Sometimes you want to wrap content in a tag only if a certain condition is met.
Use `ui.util.tag` for this.


```django
{{ ui.util.tag(content, "a" if href else "", attrs={"href": href}) }}
```


If `href` is present, it renders an `<a>` tag. If not, it just prints the
content as-is.

## 3. Persistent unique IDs

When connecting a handle (like a button) to a target (like a modal), you need a
unique ID. If you have a CKAN object with a unique name, you can use it to
generate a stable, reproducible ID.


```django
{% set modal_id = ui.util.id(package.name, prefix="modal-") %}
{{ ui.modal_handle(_("View Details"), id=modal_id) }}
{{ ui.modal(package.notes, id=modal_id) }}
```


## 4. Mapping over a list of items

If you have a list of simple strings and want to render a component for each
of them, use `ui.util.map`.


```django
{# Renders three badges #}
{{ ui.util.map(ui.badge, ["New", "Hot", "Trending"], style="primary") }}
```


## 5. Overriding a single component in your portal

If you like a theme but want to change just one specific component (e.g., the
`footer`) for your portal:

1. Create a new theme in your local extension that extends the base theme.
2. In your `register_themes()`:
   ```python
   Theme("my_portal_theme", path, parent="classic-polyfill")
   ```
3. Create `templates/macros/ui.html` in your extension.
4. Redefine only the `footer` macro. Everything else will fall back to the
   parent theme.
5. Enable your theme by setting `ckan.ui.theme = my_portal_theme` in the config
   file.

As an alternative approach, you can add additional file with macro definitions,
instead of extending the theme. This approach works better when your extension
provides a set of theme-agnostic components that must be automatically
registered whenever your extension is enabled, but it can be used for component
overrides as well:

1. Create a new file with macross in your extension. The name does not matter
   as long as it does not match existing template
   name. `macros/my_extension_components.html` is a good choice.
2. Implement `ITheme.get_additional_theme_ui_sources() -> list[str]` method:
   ```python
   def get_additional_theme_ui_sources(self):
       return ["macros/my_extension_components.html"]
   ```
3. Define only the `footer` macro. This macro will be registered after theme
   macros and will take place of the existing `footer` macro.

Both approaches result in exactly the same macro structure. The former focuses
of the fact that you are overriding parts of the theme, while the latter
implies that you are adding new components, unrelated to the existing
theme. Depending on your intention you can choose either of them, but
registering a custom theme is more correct according to the goal.
