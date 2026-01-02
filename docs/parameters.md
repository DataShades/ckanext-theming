# Standard Parameter Values

This page describes the expected values for common parameters across all UI
components. Using standardized parameter values ensures consistency across
different themes and simplifies theme switching. Each theme implementation
should support these standard values, though they may translate them to
framework-specific equivalents.

## Size Parameters

Size parameters are used across many components to control sizing and
spacing. The following values are standardized:

| Value | Description           | Framework Equivalent                                             |
|-------|-----------------------|------------------------------------------------------------------|
| `xs`  | Extra small size      | Bootstrap: `sm`, Tailwind: `xs`, Bulma: `is-small`               |
| `sm`  | Small size            | Bootstrap: `sm`, Tailwind: `sm`, Bulma: `is-small`               |
| `md`  | Medium size (default) | Bootstrap: `md` (or no class), Tailwind: `md`, Bulma: (no class) |
| `lg`  | Large size            | Bootstrap: `lg`, Tailwind: `lg`, Bulma: `is-medium`              |
| `xl`  | Extra large size      | Bootstrap: `lg`, Tailwind: `xl`, Bulma: `is-large`               |

## Style/Variant Parameters

Style parameters control the visual appearance and semantic meaning of
components. The following values are standardized:

| Value       | Description                     | Framework Equivalent                                                               |
|-------------|---------------------------------|------------------------------------------------------------------------------------|
| `primary`   | Primary/important style         | Bootstrap: `primary`, Tailwind: `primary`, Bulma: `is-primary`                     |
| `secondary` | Secondary/alternative style     | Bootstrap: `secondary`, Tailwind: `secondary`, Bulma: `is-secondary` or `is-light` |
| `success`   | Success/positive state          | Bootstrap: `success`, Tailwind: `success`, Bulma: `is-success`                     |
| `warning`   | Warning/cautionary state        | Bootstrap: `warning`, Tailwind: `warning`, Bulma: `is-warning`                     |
| `danger`    | Danger/error/destructive action | Bootstrap: `danger`, Tailwind: `danger`, Bulma: `is-danger`                        |
| `info`      | Informational state             | Bootstrap: `info`, Tailwind: `info`, Bulma: `is-info`                              |
| `light`     | Light/low emphasis style        | Bootstrap: `light`, Tailwind: `light`, Bulma: `is-light`                           |
| `dark`      | Dark/high contrast style        | Bootstrap: `dark`, Tailwind: `dark`, Bulma: `is-dark`                              |


## Icon Parameters

Icon parameters expect Font Awesome icon names without the `fa-` prefix. Themes
that use different icon sets should provide translation via `ui.util.icon()`.

**Common icon names:**

| Icon                   | Role                   |
|------------------------|------------------------|
| `home`                 | Home navigation        |
| `search`               | Search functionality   |
| `user`                 | User/profile related   |
| `cog`                  | Settings/configuration |
| `plus`                 | Add/create actions     |
| `minus`                | Remove/reduce actions  |
| `trash`                | Delete/trash actions   |
| `edit`                 | Edit/update actions    |
| `download`             | Download actions       |
| `upload`               | Upload actions         |
| `eye`                  | View/show actions      |
| `lock`                 | Security/locked state  |
| `unlock`               | Unlocked/open state    |
| `info-circle`          | Information/help       |
| `exclamation-triangle` | Warning                |
| `times`                | Close/remove/cancel    |
| `check`                | Success/confirmation   |
| `chevron-down`         | Expand/down arrow      |
| `chevron-up`           | Collapse/up arrow      |
| `chevron-left`         | Previous/back          |
| `chevron-right`        | Next/forward           |

/// note

Themes should implement `ui.util.icon()` to translate these names to their
specific icon system (e.g., Bootstrap Icons, Material Icons, custom SVG icons).

///

## Direction Parameters

Direction parameters control layout orientation and positioning:

| Value            | Description               | Framework Equivalent                           |
|------------------|---------------------------|------------------------------------------------|
| `row`            | Horizontal layout         | Flexbox: `flex-row`, CSS Grid: `grid-flow-col` |
| `column`         | Vertical layout           | Flexbox: `flex-col`, CSS Grid: `grid-flow-row` |
| `row-reverse`    | Reverse horizontal layout | Flexbox: `flex-row-reverse`                    |
| `column-reverse` | Reverse vertical layout   | Flexbox: `flex-column-reverse`                 |


## Alignment Parameters

Alignment parameters control content alignment within components:

| Value      | Description                 | Framework Equivalent                                                      |
|------------|-----------------------------|---------------------------------------------------------------------------|
| `start`    | Align to start (left/top)   | Bootstrap: `start`, Tailwind: `items-start`, Bulma: `has-text-left`       |
| `center`   | Center alignment            | Bootstrap: `center`, Tailwind: `items-center`, Bulma: `has-text-centered` |
| `end`      | Align to end (right/bottom) | Bootstrap: `end`, Tailwind: `items-end`, Bulma: `has-text-right`          |
| `baseline` | Align to baseline           | Bootstrap: `baseline`, Tailwind: `items-baseline`                         |


## Position Parameters

Position parameters control element positioning and placement:

| Value    | Description     | Framework Equivalent                                      |
|----------|-----------------|-----------------------------------------------------------|
| `top`    | Top position    | Bootstrap: `top`, Tailwind: `top-0`, CSS: `position: top` |
| `bottom` | Bottom position | Bootstrap: `bottom`, Tailwind: `bottom-0`                 |
| `left`   | Left position   | Bootstrap: `left`, Tailwind: `left-0`                     |
| `right`  | Right position  | Bootstrap: `right`, Tailwind: `right-0`                   |
| `center` | Center position | Bootstrap: `center`, Tailwind: `center`                   |

## State Parameters

State parameters control component states and behaviors:

| Value      | Description                           | Framework Equivalent                                              |
|------------|---------------------------------------|-------------------------------------------------------------------|
| `active`   | Active/selected state                 | Bootstrap: `active`, Tailwind: `active`, Bulma: `is-active`       |
| `disabled` | Disabled/inactive state               | Bootstrap: `disabled`, Tailwind: `disabled`, Bulma: `is-disabled` |
| `readonly` | Read-only state                       | HTML attribute: `readonly`                                        |
| `required` | Required state                        | HTML attribute: `required`                                        |
| `checked`  | Checked state (for checkboxes/radios) | HTML attribute: `checked`                                         |

## Spacing Parameters

Spacing parameters control padding and margin:

| Value  | Description         | Framework Equivalent                      |
|--------|---------------------|-------------------------------------------|
| `none` | No spacing          | Bootstrap: `0`, Tailwind: `0`, Bulma: `0` |
| `sm`   | Small spacing       | Bootstrap: `1`, Tailwind: `1`, Bulma: `1` |
| `md`   | Medium spacing      | Bootstrap: `2`, Tailwind: `2`, Bulma: `2` |
| `lg`   | Large spacing       | Bootstrap: `3`, Tailwind: `3`, Bulma: `3` |
| `xl`   | Extra large spacing | Bootstrap: `4`, Tailwind: `4`, Bulma: `4` |

## Color Parameters

Color parameters control color schemes and themes:

| Value       | Description              | Framework Equivalent                                              |
|-------------|--------------------------|-------------------------------------------------------------------|
| `primary`   | Primary theme color      | Bootstrap: `primary`, Tailwind: `primary`, Bulma: `primary`       |
| `secondary` | Secondary theme color    | Bootstrap: `secondary`, Tailwind: `secondary`, Bulma: `secondary` |
| `success`   | Success/green color      | Bootstrap: `success`, Tailwind: `success`, Bulma: `success`       |
| `danger`    | Error/red color          | Bootstrap: `danger`, Tailwind: `danger`, Bulma: `danger`          |
| `warning`   | Warning/orange color     | Bootstrap: `warning`, Tailwind: `warning`, Bulma: `warning`       |
| `info`      | Informational/blue color | Bootstrap: `info`, Tailwind: `info`, Bulma: `info`                |


## Implementation Guidelines

When implementing themes, ensure that:

1. **Standard values are supported**: Your theme should handle all standard parameter values listed above
2. **Translation is provided**: If your CSS framework uses different naming conventions, implement translation in your theme
3. **Fallbacks are available**: Provide sensible defaults when standard values don't map directly to your framework
4. **Consistency is maintained**: Same parameter values should produce similar visual results across different themes
5. **Accessibility is preserved**: Ensure that visual differences are also conveyed through appropriate ARIA attributes and semantic markup

By following these standardized parameter values, themes become more
interoperable and users can switch between themes with minimal disruption to
their expectations about component behavior and appearance.
