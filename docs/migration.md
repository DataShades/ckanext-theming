{% raw %}
# Migration Guide: Snippets to Macros

If you are coming from traditional CKAN development, you are likely used to
writing raw HTML with framework-specific classes or using snippets for complex
UI elements. This guide shows how these patterns translate to the
`ckanext-theming` system.

## 1. Simple Buttons

### Traditional
You write HTML with Bootstrap classes (or whatever framework you use).
```html
<button type="submit" class="btn btn-primary btn-lg">
  Save Dataset
</button>
```

### With Macros
You use a semantic call. The theme handles the `btn`, `btn-primary`, and `btn-lg` classes.
```django
{{ ui.button(_("Save Dataset"), type="submit", style="primary", size="lg") }}
```

---

## 2. Information Alerts

### Traditional
```html
<div class="alert alert-info">
  <i class="fa fa-info-circle"></i>
  This dataset is public.
</div>
```

### With Macros
```django
{{ ui.alert(_("This dataset is public."), style="info", icon="info-circle") }}
```

---

## 3. Complex Cards (Snippets)

### Traditional
You might use a snippet and pass data to it.
```django
{% snippet "snippets/package_item.html", package=pkg %}
```

### With Macros
You use the `package` component. It's still a single line, but it's now part of
a standardized API that works across different themes.
```django
{{ ui.package(package=pkg) }}
```

---

## 4. Nested Content (The `call` pattern)

This is where the most power lies. Traditional CKAN development often makes it
hard to pass complex HTML into a snippet without using multiple blocks or
global variables.

### Traditional
```html
<div class="card">
  <div class="card-header">Custom Header</div>
  <div class="card-body">
    <p>Some custom HTML content.</p>
    <a href="..." class="btn">Click me</a>
  </div>
</div>
```

### With Macros
Using `ui.util.call`, you can nest components and raw HTML naturally.
```django
{% call ui.util.call(ui.card, title="Custom Header") %}
  <p>Some custom HTML content.</p>
  {{ ui.button(_("Click me"), href="...") }}
{% endcall %}
```

---

## 5. Form Fields

### Traditional
```django
{% import "macros/form.html" as form %}
{{ form.input("title", label=_("Title"), value=data.title, placeholder="eg. My Dataset") }}

```

### With Macros
The macro handles the wrapper, label, ID generation, and accessibility attributes.
```django
{{ ui.input(name="title", label=_("Title"), value=data.title, placeholder="eg. My Dataset") }}
```

---

## Summary of Changes

| Feature | Traditional CKAN | ckanext-theming |
| :--- | :--- | :--- |
| **Logic** | Mix of HTML and template logic | Pure semantic calls |
| **CSS Classes** | Hardcoded in templates | Abstracted into the theme |
| **Portability** | Locked to one CSS framework | Works with any compatible theme |
| **Maintenance** | Update HTML in every template | Update macro in one place |
{% endraw %}
