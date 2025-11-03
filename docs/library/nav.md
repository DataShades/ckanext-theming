# Navigation

## `breadcrumb_wrapper`

Wraps the breadcrumb trail. This is a block macro.

### Arguments

*   `content` (string): breadcrumb items.

## `breadcrumb_item`

Creates a single item in a breadcrumb trail.

### Arguments

*   `content` (string): The text to display for the breadcrumb item.
*   `href` (string): The URL for the breadcrumb item.

## `nav_wrapper`

Wraps a navigation element (e.g., `<nav>`). This is a block macro.

### Arguments

*   `content` (string): nav items.

## `nav_item`

Creates a single item in a navigation list.

### Arguments

*   `content` (string): The text to display for the navigation item.
*   `href` (string): The URL for the navigation item.
*   `active` (boolean): Whether the item is currently active. Defaults to `false`.

## `tab_wrapper`

Wraps a tabbed interface. This is a block macro.

### Arguments

*   `content` (string): tab items.

## `tab_item`

Creates a single tab item.

### Arguments

*   `content` (string): The text to display for the tab item.
*   `href` (string): The URL for the tab item.
*   `active` (boolean): Whether the tab is currently active. Defaults to `false`.

## `menu_wrapper`

Wraps a menu. This is a block macro.

### Arguments

*   `content` (string): menu items.

## `menu_item`

Creates a single item in a menu.

### Arguments

*   `content` (string): The text to display for the menu item.
*   `href` (string): The URL for the menu item.
*   `active` (boolean): Whether the item is currently active. Defaults to `false`.

## `pagination`

Renders pagination controls.

### Arguments

*   `page` (integer): The current page number. Defaults to 1.
*   `total_pages` (integer): The total number of pages. Defaults to 1.
*   `url_generator` (callable): A function to generate URLs for pages. Defaults to `h.pager_url`.
*   `padding` (integer): The number of page links to show around the current page. Defaults to 2.
