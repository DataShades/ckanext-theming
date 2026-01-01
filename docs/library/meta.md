# Meta Components

Meta components provide structural elements for the overall page structure like headers, footers, and navigation elements that appear consistently across pages.

## Overview

Meta components form the structural foundation of the page, providing consistent navigation and layout elements that appear across multiple pages and sections of the application. These components establish the primary layout framework and provide the consistent structural elements that users expect to find on every page.

## Account Component

The `account` component provides account-related meta elements that appear consistently across pages where user account information is relevant. This component typically displays user profile information, account status, or account-specific navigation elements that are important for user identification and account management.

Account components are essential for maintaining user awareness of their account status and providing quick access to account-related functions. They often include elements like user avatars, display names, notification indicators, or quick access to account settings. The component ensures consistent presentation of account information across different pages and contexts where user identification is important.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic account component -->
{{ ui.account() }}

<!-- Account with attributes -->
{{ ui.account(attrs={"class": "account-header"}) }}
```
///

## Header Component

The `header` component creates page headers that establish the top-level structure of pages and provide consistent navigation and branding elements. Headers are fundamental to page structure, typically containing site branding, primary navigation, search functionality, and other elements that appear on every page.

Header components handle complex layout requirements including responsive behavior, navigation menus, search bars, and branding elements. They ensure consistent positioning and styling of header content while adapting to different page types and content requirements. The component provides the structural foundation for the top portion of every page, creating visual consistency and familiar navigation patterns for users.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic header component -->
{{ ui.header() }}

<!-- Header with attributes -->
{{ ui.header(attrs={"class": "main-header"}) }}
```
///

## Footer Component

The `footer` component creates page footers that provide consistent information and navigation elements at the bottom of pages. Footers typically contain site information, legal notices, secondary navigation, contact information, and other elements that users might need but don't require prominent placement.

Footer components handle various content types and layout requirements, ensuring that important but less frequently accessed information remains accessible to users. They provide consistent positioning and styling for footer content while maintaining visual harmony with the overall page design. The component ensures that footer elements remain accessible and properly formatted across different page types and content lengths.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic footer component -->
{{ ui.footer() }}

<!-- Footer with attributes -->
{{ ui.footer(attrs={"class": "main-footer"}) }}
```
///

## Subtitle Item Component

The `subtitle_item` component creates subtitle elements that provide additional context or secondary information related to main headings or content sections. Subtitles help create more detailed information hierarchies and provide additional context without competing with primary headings for attention.

Subtitle components are particularly useful for pages with complex information structures where additional descriptive text helps users understand the context or purpose of content sections. The component handles appropriate sizing, positioning, and styling that distinguishes subtitles from main headings while maintaining visual harmony with the overall design. Subtitles often appear below main headings or as secondary labels for content sections.

/// details | Usage Example
    type: example

```jinja2
<!-- Basic subtitle item -->
{{ ui.subtitle_item("Additional information") }}

<!-- Subtitle item with attributes -->
{{ ui.subtitle_item("Section subtitle", attrs={"class": "section-subtitle"}) }}
```
///
