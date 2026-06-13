# Advanced Development

This page covers advanced hooks and techniques for extension developers who
want to integrate deeply with the theming system.

## The `ITheme` Interface

Extensions can interact with the theming system by implementing the `ITheme`
interface.

### 1. Providing Default Implementations
If your extension provides a new UI component that should have a generic
fallback implementation, use `get_default_theme_ui_sources`.

```python
def get_default_theme_ui_sources(self) -> list[str]:
    return ["macros/my_extension_defaults.html"]
```

**Lower Priority**: Macros in these files will be used only if the active
theme does **not** define a macro with the same name.

**Use Case**: Providing basic markup for a new widget that a theme can
  optionally style later.

### 2. Providing Additional Components
To provide components that should **not** be overridden by themes, use
`get_additional_theme_ui_sources`.

```python
def get_additional_theme_ui_sources(self) -> list[str]:
    return ["macros/my_extension_widgets.html"]
```

**Higher Priority**: Macros in these files take precedence over theme
  implementations.

**Use Case**: Complex logic-heavy widgets where the HTML structure is
  critical for the extension's functionality.

### 3. Patching the UI Object
For absolute control, you can use `patch_theme_ui` to dynamically add or
modify components on the `ui` object.

```python
def patch_theme_ui(self, theme, ui):
    # Dynamically add a simple component
    ui._add_component("timestamp", lambda: ui.util.now().isoformat())
```

---

## Component Categories

In `components.yaml` (and when using CLI tools), components are grouped into
categories. Understanding these helps you prioritize your implementation:

- **Essential**: Fundamental to CKAN's operation. Every theme **must**
  implement these (e.g., `button`, `input`, `form`).
- **Recommended**: Highly recommended for a complete user experience (e.g.,
  `card`, `alert`, `modal`).
- **Experimental**: New or unstable components that might change in future
  versions.
- **Plugin**: Components provided by other extensions (like
  `ckanext-scheming`).
- **Custom**: Theme-specific components that aren't part of the standard
  library.
