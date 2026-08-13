# Philosophy & Goals

The `ckanext-theming` extension is a proposal for a more flexible and
maintainable way to build CKAN user interfaces. This page explains the core
principles behind this project, what it aims to achieve, and just as
importantly, what it is **not**.

## What this project IS

### 1. An optional layer

This extension provides a set of tools and a suggested workflow. It is **not**
a replacement for the existing CKAN template system, but an enhancement to it.
You can adopt it partially, fully, or not at all. It's totally normal to enable
the `theming` plugin only to use some of it's helpers on CLI commands, without
a single change in templates.

### 2. An abstraction for reusability
The core idea is to move from "writing HTML with specific CSS classes" to
"calling UI components with semantic meaning". Instead of:
`#!html <button class="btn btn-primary">Save</button>`, you use
`#!django {{ ui.button("Save", style="primary") }}`.

This abstraction allows:

- Theme Portability: The same extension can look native in a Bootstrap theme,
  a Tailwind theme, or a custom CSS theme without changing its code.
- Easier Upgrades: When a new version of a CSS framework is released, you
  only update the macro definitions in one place, not every single template in
  every extension.

### 3. A bridge for ecosystem compatibility

By using a shared set of UI components, different extensions can work together
visually. If Extension A and Extension B both use `ui.card`, they will
automatically look consistent on your portal, regardless of which theme you
chose.

## What this project IS NOT

### 1. It is NOT mandatory
Installing this extension does **not** force you to rewrite your existing
templates. Your current snippets, blocks, and raw HTML will continue to work exactly
as they did before. You can start using `ui.*` macros for new features while
keeping your legacy code untouched.

### 2. It is NOT a "black box"

Some people worry that an abstraction layer makes things harder to debug. In
this system, every `ui.*` call eventually resolves to a standard Jinja2 macro
that you can inspect, override, and customize just like any other CKAN
template. You have full control over the final HTML output.

### 3. It is NOT a performance bottleneck

The overhead of calling a Jinja2 macro instead of writing raw HTML is
negligible. The system is designed to be as lightweight as possible, leveraging
standard Jinja2 features.

Additionally, certain components, like buttons, package items, sidebars are
already rendered not with inline HTML, but with snippets. In this case, macros
show considerable performance gain(x5-x20) due to Jinja2 caching utilities that
are applied to macros but are not used with snippets.

Generally, the average performance of the portal is not affected when using
theming, unless you meet an edge case that almost never happen in real
projects. For example, page that does not use any includes and snippets(i.e. it
does not rely on standard `page.html` that includes footer & header) will be
rendered faster WITHOUT theming; page that uses hundreds or thousands of input
snippets will be rendered faster WITH theming. As mentioned before, you can
omit theming when the page will benefit from inline HTML if compatibility with
different themes is not critical, but template rendering is unlikely to be a
bottleneck in your application.

## Why should you use it?

If you are a **portal maintainer**:

- You can switch between different visual styles (themes) with a single config change.
- You reduce the risk of UI breakage when updating CKAN or its extensions.

/// note

In reality, compatibility between different themes is not ideal, so you'll
still get broken pages. But theming extension reduces the number of
issues.

Whether there will be broken pages or not mostly depends on theme
implementation. For example, the basic footer navigation may look like this:

```django
{% call ui.util.call(ui.footer_main_nav) %}
    {{ ui.footer_main_nav_item("First link") }}
    {{ ui.footer_main_nav_item("Second link") }}
{% endcall %}
```

As long as theme implements these components atomically, they will be rendered
correctly whenever you are using them. But if theme expects that there is a
`#!html <div class="footer-container">` wrapper around footer navigation,
you'll have to add it manually or else navigation will look broken.

So, if theme is implemented without assumptions about component surrounding, it
will be more stable. If theme cannot be implemented in this way for some
reasons, it may require certain work when applied.

///

If you are an **extension developer**:

- You don't have to guess which CSS framework the target portal is using.
- You don't need to provide multiple sets of templates for `bootstrap5`,
  `bootstrap3`, `midnight-blue` and other base template folders.
- Your extension will look "correct" on any portal that has a compatible theme.
- You spend less time writing repetitive HTML and more time on functionality.

## Incremental adoption

The best way to use `ckanext-theming` is to start small:

1. Add theming extension as a dependency of your project.
2. Decorate main plugin class with `ckanext.theming.plugin.themed_plugin`.
3. Use UI components like `#!django {{ ui.button(...) }}` or `#!django {{ ui.input(...) }}` instead of raw HTML.
4. See how it simplifies your templates and keeps them clean.

Remember: **You are in control.** Use as much or as little of the theming system
as makes sense for your specific project.


/// admonition
    type: tip

Enable `theming` plugin and use CLI command `ckan theme component list` to
see all available components, and `ckan theme component analyze NAME` to
see usage details of the component `NAME` (i.e. `button`, `input`, et.)

///
