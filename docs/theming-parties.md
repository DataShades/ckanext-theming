# Theming Parties

Theming in CKAN involves three distinct parties, each with different responsibilities and capabilities. The theming system enables a clear separation of concerns where each party can focus on their specific role without interfering with others.

## 1. Theme Developers

Theme developers create complete themes that define the visual appearance and UI component implementations for CKAN instances.

/// details | Responsibilities
- Implementing UI components (`ui` macros) for different CSS frameworks
- Creating comprehensive UI widget libraries that abstract CSS framework specifics
- Ensuring cross-browser compatibility and responsive design
- Following CKAN theming best practices and conventions
- Maintaining API compatibility for UI components
- Supporting theme inheritance and extension
///

/// details | Capabilities
- Use raw HTML, CSS, and JavaScript to implement components
- Integrate different CSS frameworks (Bootstrap, Tailwind, Bulma, etc.)
- Define how components look and behave across the entire portal
- Create theme inheritance hierarchies
- Implement accessibility features consistently
- Provide comprehensive component coverage
///

/// details | Constraints
- Must provide consistent API across all UI components
- Need to maintain backward compatibility for component interfaces
- Should implement all required components to ensure full functionality
- Must consider upgrade paths for portals using their themes
- Need to follow established naming conventions and patterns
///

## 2. Extension Developers

Extension developers create reusable CKAN extensions that should work across different themes and portals without modification.

/// details | Responsibilities
- Creating theme-compatible extensions using the UI macro system
- Using only components provided by the theme's `ui` system
- Avoiding theme-specific CSS classes or HTML structures
- Ensuring extensions work regardless of the active theme
- Following CKAN extension development best practices
///

/// details | Capabilities
- Use the standardized UI macro system (`ui.*` components)
- Rely on consistent API across different themes
- Create extensions that work on any portal with minimal customization
- Focus on functionality rather than presentation
- Leverage theme-provided accessibility features
///

/// details | Constraints
- Cannot assume any specific theme is in use
- Cannot use raw HTML with theme-specific classes
- Cannot rely on specific CSS frameworks or design systems
- Must work within the constraints of the theme's component system
- Limited to available UI components provided by themes
- Cannot implement custom visual styles directly
///

/// admonition | Example
    type: example

```jinja2
<!-- Good: Using UI components -->
{{ ui.button(_("Submit"), type="submit", style="primary") }}
{{ ui.card(title=_("Dataset Information"), content=dataset.description) }}
{{ ui.link(_("View Dataset"), href=url_for("dataset.read", id=dataset.id)) }}

<!-- Avoid: Raw HTML with specific classes -->
<button class="btn btn-primary">Submit</button>
<div class="card">
  <h3 class="card-title">Dataset Information</h3>
  <p class="card-body">{{ dataset.description }}</p>
</div>
```
///

## 3. Portal Maintainers

Portal maintainers configure specific CKAN portals and have knowledge of the chosen theme and business requirements.

/// details | Responsibilities
- Configuring the active theme for the portal
- Customizing the portal to meet specific business requirements
- Managing theme selection and potential migrations
- Maintaining the portal and planning for upgrades
- Leveraging theme-specific features when beneficial
///

/// details | Capabilities
- Select and configure the appropriate theme for the portal
- Use theme-specific templates when necessary
- Apply custom styling and overrides at the portal level
- Leverage advanced theme features
- Access raw theming capabilities for unique requirements
- Override specific templates while maintaining component usage
///

/// details | Constraints
- Risk of breakage when migrating themes
- Extra maintenance during theme updates
- Need to understand the selected theme's capabilities
- Should prefer UI components over raw HTML for consistency
- Limited to the components and features provided by the selected theme
///

## Component Categories

The theming system defines different categories of components to guide implementation and usage:

/// details | Essential Components
- Required for basic CKAN functionality
- Must be implemented by all themes
- Examples: `link`, `button`, `input`, `form`
- Critical for portal operation
///

/// details | Recommended Components
- Enhance user experience but not strictly required
- Should be implemented by complete themes
- Examples: `card`, `alert`, `navigation`, `grid`
- Provide better user interface consistency
///

/// details | Custom Components
- Theme-specific or extension-specific components
- Optional based on theme requirements
- Examples: framework-specific components, custom widgets
- Extend the basic component set
///

## Best Practices

### For All Parties
- Prefer UI components over raw HTML when possible
- Follow established naming conventions
- Consider maintainability and upgrade paths
- Document theme dependencies clearly
- Implement accessibility features appropriately

### For Theme Developers
- Maintain consistent API across all components
- Provide comprehensive component coverage
- Implement proper error handling
- Follow accessibility standards
- Support theme inheritance properly

### For Extension Developers
- Use only documented UI components
- Test with different themes when possible
- Avoid assumptions about visual appearance
- Focus on functionality rather than presentation
- Follow CKAN extension development patterns

### For Portal Maintainers
While portal maintainers *can* use theme-specific HTML and CSS classes, it's recommended to prefer UI components for the following reasons:

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Theme Migration | If the portal migrates to a different theme, UI component-based code will continue to work |
| Theme Updates   | Theme updates won't break customized sections that use UI components                    |
| Consistency     | Maintains visual consistency across the theme                                           |
| Maintenance     | Easier to maintain over time                                                            |
| Accessibility   | Benefits from theme-provided accessibility features                                     |

### When to Use UI Components vs. Raw HTML
|                       |                                                                                      |
|-----------------------|--------------------------------------------------------------------------------------|
| Use UI components     | For standard components like buttons, cards, forms, navigation, links                |
| Consider raw HTML     | For highly customized layouts or when theme components don't meet specific requirements |
| Always prefer components | When functionality can be achieved through theme-provided components             |

### Migration Strategy

When a portal decides to switch themes:

- Code using UI components will continue to work (though appearance may change)
- Code using raw HTML with theme-specific classes will need updating
- A gradual approach is recommended to migrate away from theme-specific code
- Use CLI tools to verify component coverage when switching themes: `ckan theme component check`
