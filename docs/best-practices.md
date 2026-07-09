
# Technical Best Practices

This page explains the technical advantages of the `ckanext-theming` system
and how to ensure your themes are high-quality, performant, and accessible.

## Performance: Macros vs. Snippets

One of the secondary benefits of this system is improved rendering performance.

### 1. Compiled Code
Standard CKAN snippets (`{% snippet ... %}`) are processed at runtime. Every
time a snippet is called, Jinja2 (potentially) checks the filesystem and
performs a search through the template directories.

In contrast, **Macros** are compiled into Python code by Jinja2 when the
template is first loaded. Calling a macro is effectively a native Python
function call, which is significantly faster than snippet resolution.

### 2. Reduced I/O
Because all components for a theme are typically defined in one or two macro
files (loaded via `get_default_theme_ui_sources` or `macros/ui.html`), the
number of individual file lookups on the server is drastically reduced.

---

## Accessibility (a11y)

Accessibility is a core goal of this project. To maintain it, theme authors
must follow these guidelines:

### 1. Always use `ui.util.attrs(kwargs)`
The most common mistake is to hardcode attributes inside a macro and forget to
render the attributes passed by the user.

**Incorrect (Loses accessibility attributes):**
```django
{% macro button(content) %}
  <button class="btn">{{ content }}</button>
{% endmacro %}
```

**Correct (Preserves ARIA, data, and event attributes):**
```django
{% macro button(content) %}
  <button {{ ui.util.attrs(kwargs, {"class": "btn"}) }}>{{ content }}</button>
{% endmacro %}
```

By using `ui.util.attrs`, you ensure that if an extension developer calls
`{{ ui.button("Search", aria={"label": "Search datasets"}) }}`, the resulting
HTML will correctly include `aria-label="Search datasets"`.

### 2. Semantic HTML
Whenever possible, use semantic HTML tags. The system provides `ui.util.tag`
to help you render dynamic wrappers while keeping the inner content semantic.

### 3. Keyboard Navigation
Ensure that interactive components (buttons, links, inputs) have visible focus
states and correct `tabindex` behavior if you are using non-standard elements
(like a `<div>` styled as a button—though we highly recommend against this).

---

## Maintenance & Stability

### 1. Avoid Positional Arguments
Except for the first `content` argument (when applicable), **always use named arguments**.

This ensures that if a new version of the extension adds a parameter to a standard component, your theme will not break because of a signature mismatch. The `**kwargs` (implicit in macros) will safely catch and ignore any parameters your specific theme doesn't handle yet.

**Incorrect:**
```django
{{ ui.link("New Dataset", "/dataset/new", _extra_class="nav-link") }}
```

**Correct:**
```django
{{ ui.link("New Dataset", href="/dataset/new", _extra_class="nav-link") }}
```


## Modifying Attributes: `ui.util.augment_attrs`

When building macros, you often need to merge default attributes (like default
styles, roles, or actions) with user-provided arguments in `kwargs`. **Never**
pass an `attrs` dictionary directly if you are forwarding `kwargs`
(e.g. `attrs={"class": "foo"}, **kwargs`), as this may conflict with custom
attributes the user passes.

Instead, always use the helper utility `ui.util.augment_attrs`.

### Function Signature
```python
def augment_attrs(
    kwargs: dict[str, Any],
    defaults_dict: dict[str, Any] | None = None,
    /,
    key: str | None = "attrs",
    extra_class: str | None = None
) -> dict[str, Any]
```

### Best Practice Rules for `augment_attrs`
1. **Targeting Attributes Sub-dictionary (Default):**
   By default, `key="attrs"`. This merges a dictionary of defaults into the `attrs` sub-dictionary within `kwargs`.
   ```django
   {{ ui.util.augment_attrs(kwargs, {"role": "menuitem", "aria-expanded": "false"}) }}
   ```
2. **Merging CSS Classes:**
   Use the `extra_class` argument to safely append a CSS class to the component’s extra classes without overwriting any user-provided classes.
   ```django
   {{ ui.util.augment_attrs(kwargs, extra_class="dropdown-item") }}
   ```
3. **Modifying Different Targets:**
   If you want to modify a top-level key or a different nested dictionary within `kwargs`, change the `key` parameter. For example, to modify the main kwargs root:
   ```django
   {{ ui.util.augment_attrs(kwargs, {"data-custom": "value"}, key=none) }}
   ```

### Comprehensive Example
Here is a robust menu link component that safely combines role attributes and CSS classes:
```django
{% macro menu_link(content, href=None) %}
    {%- set augmented_kwargs = ui.util.augment_attrs(
        kwargs,
        {"role": "menuitem"},
        extra_class="dropdown-item"
    ) -%}
    {{ ui.link(content, href=href, **augmented_kwargs) }}
{% endmacro %}
```
