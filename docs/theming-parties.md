# Theming parties and their roles

Theming in CKAN can be approached by three different types of users, each with different levels of knowledge and constraints. Understanding these roles helps in making better decisions about when to use raw HTML vs. themed components.

## 1. Theme Developers

Theme developers are responsible for creating complete themes that can be used by portals. They have the most freedom and responsibility in the theming ecosystem.

/// details | Responsibilities
- Providing all components for other parties to use
- Creating comprehensive UI widget libraries (`ui` macros)
- Ensuring cross-browser compatibility and responsive design
- Following CKAN theming best practices and conventions
- Maintaining backward compatibility when possible
///

/// details | Capabilities
- Use raw HTML, CSS, and JavaScript freely
- Create custom CSS classes and structures
- Integrate third-party CSS frameworks (Bootstrap, Bulma, Tailwind, etc.)
- Define how components look and behave across the entire portal
///

/// details | Constraints
- Need to provide comprehensive theme components for others
- Must consider upgrade paths for portals using their themes
- Should maintain API compatibility for `ui` macros
///

## 2. Extension Developers

Extension developers create reusable CKAN extensions that should work across different themes and portals.

/// details | Responsibilities
- Creating theme-compatible extensions
- Using only widgets provided by the theme's `ui` system
- Avoiding theme-specific CSS classes or HTML structures
- Ensuring extensions work regardless of the active theme
///

/// details | Capabilities
- Use UI macro system (`ui.*` widgets) provided by themes
- Rely on consistent API across different themes
- Create extensions that work on any portal with minimal customization
///

/// details | Constraints
- Cannot assume any specific theme is in use
- Cannot use raw HTML with theme-specific classes
- Cannot rely on specific CSS frameworks or design systems
- Must work within the constraints of the theme's widget system
///

/// admonition | Example
    type: example

```jinja2
<!-- Good: Using UI macros -->
{{ ui.heading(_('My Extension Title'), level=2) }}
{{ ui.card(_('Card Title'), content=_('Card content'), footer=_('Card footer')) }}

<!-- Avoid: Raw HTML with specific classes -->
<div class="card">
  <h2 class="card-title">Title</h2>
  <div class="card-body">Content</div>
</div>
```
///

## 3. Portal Maintainers

Portal maintainers configure specific CKAN portals and have deep knowledge of the chosen theme.

/// details | Responsibilities
- Customizing the specific portal to meet business requirements
- Leveraging theme-specific features when beneficial
- Maintaining the portal and planning for upgrades
///

/// details | Capabilities
- Use theme-specific HTML and CSS classes when needed
- Apply custom styling and overrides
- Leverage advanced theme features
- Access raw theming capabilities for unique requirements
///

/// details | Constraints
- Risk of breakage when migrating themes
- Extra maintenance during theme updates
- Less portable code if theme-specific features are heavily used
///

## Best Practices

### For All Parties
- Prefer UI widgets over raw HTML when possible
- Document theme dependencies clearly
- Consider maintainability and upgrade paths

### For Portal Maintainers Specifically
While portal maintainers *can* use theme-specific HTML and CSS classes, it's recommended to prefer UI widgets for the following reasons:

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Theme Migration | If the portal migrates to a different theme, UI widget-based code will continue to work |
| Theme Updates   | Theme updates won't break customized sections that use UI widgets                       |
| Consistency     | Maintains visual consistency across the theme                                           |
| Maintenance     | Easier to maintain over time                                                            |


### When to Use Raw HTML vs. Widgets
|                       |                                                                                      |
|-----------------------|--------------------------------------------------------------------------------------|
| Use UI widgets        | For standard components like buttons, cards, forms, navigation                       |
| Consider raw HTML     | For highly customized layouts or when theme widgets don't meet specific requirements |
| Always prefer widgets | When functionality can be achieved through theme components                          |

### Migration Strategy

If a portal decides to switch themes:

- Code using UI widgets will continue to work (though appearance may change)
- Code using raw HTML with theme-specific classes will need updating
- A gradual approach is recommended to migrate away from theme-specific code
