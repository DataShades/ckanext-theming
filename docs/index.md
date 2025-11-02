# CKAN Theming Extension

This extension provides a flexible and powerful way to customize the look and feel of a CKAN instance. It allows developers and designers to create and apply themes without modifying core CKAN code, ensuring easier upgrades and maintenance.

## Overview

The CKAN Theming Extension introduces a theming system based on Jinja2 templates and a configurable UI.  Themes can extend existing themes, providing a layered approach to customization.  Key features include:

*   **Theme Registration:**  Extensions can register themes, making them available for selection.
*   **Theme Switching:**  Administrators can easily switch between themes via the CKAN admin interface or the CLI.
*   **UI Customization:** Themes define a UI that provides macros for common elements, allowing for consistent and reusable components.
*   **Extensibility:** The system is designed to be extensible, allowing for advanced customization through custom macros and UI implementations.
*   **Command-Line Interface (CLI):**  A CLI is provided for managing themes, listing available themes, and listing available components.

## Getting Started

[Link to installation instructions](installation.md)

## Concepts

*   **Theme:** A directory containing Jinja2 templates, static assets (CSS, JavaScript, images), and a configuration file.
*   **UI:**  An interface that provides access to a set of macros for use in templates.
*   **Macros:** Reusable snippets of Jinja2 code that define the structure and appearance of UI elements.

## Further Reading

*   [Theme Development](theme_development.md)
*   [UI Implementation](ui_implementation.md)
*   [CLI Usage](cli_usage.md)
