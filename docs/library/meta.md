# Meta Macros

Meta macros provide structural components for the overall page layout including headers, footers, and account-related sections. These macros establish the global layout structure and branding elements of the application.

## `header_block`

Renders a complete header block for page branding, navigation, and primary site identification. The header block provides a consistent top section for all pages, typically containing the site logo, main title, and primary navigation.

**Use Cases:**

- Main site header
- Page branding
- Logo display
- Primary navigation container
- Site identification
- Account quick-links
- Search functionality placement

**Usage Context:**

Use at the top of all pages to provide consistent branding and navigation. This typically appears once per page and contains major site-level controls.

**Example:**

```
{{ ui.header_block(
  title="My Website",
  subtitle="Quality Services",
  content=ui.nav_wrapper(
    ui.nav_item("Home", href="/", active=true) +
    ui.nav_item("Services", href="/services") +
    ui.nav_item("Contact", href="/contact")
  )
) }}
```

**Recommendations:**

- Include site-identifying content (logo, title)
- Keep primary navigation limited to main sections
- Different themes provide various header implementations (Bootstrap: .header with navbar, Tailwind: bg-white shadow, Bulma: .hero.is-primary)
- Ensure consistent spacing and branding
- Include search functionality if appropriate
- Consider mobile-responsive behavior
- Position consistently across all pages

## `footer_block`

Renders a complete footer block for page-end content such as secondary navigation, legal information, and contact details. The footer provides a consistent bottom section for all pages with supplementary information.

**Use Cases:**

- Site-wide footer
- Legal information display
- Contact information
- Secondary navigation
- Copyright notices
- Social media links
- Site map links
- Privacy policy links

**Usage Context:**

Use at the bottom of all pages to provide consistent supplementary information and navigation. This appears once per page, at the lowest position.

**Example:**

```
{{ ui.footer_block(
  ui.link("Privacy Policy", href="/privacy") +
  ui.link("Terms of Service", href="/terms") +
  ui.text("© 2024 Company Name. All rights reserved.")
) }}
```

**Recommendations:**

- Include important but less-frequently-used links
- Different themes implement footers differently (Bootstrap: .footer, Tailwind: bg-gray-100, Bulma: .footer)
- Keep content relevant and concise
- Include accessibility links for screen readers
- Consider internationalization for copyright dates
- Use consistent styling with header branding

## `account_block`

Renders an account-related header or section block, typically used for user-specific content and controls. The account block handles user profile information, login/logout functionality, and other user-focused elements.

**Use Cases:**

- User dashboard headers
- Account profile sections
- Login/logout controls
- User-specific navigation
- Personal settings sections
- Notification displays
- User profile information
- Account management tools

**Usage Context:**

Use in areas where user-specific content or controls are needed, such as account pages, dashboards, or user profile sections.

**Example:**

```
{{ ui.account_block(
  title="My Account",
  subtitle="Manage your preferences",
  content=ui.link("Logout", href="/logout")
) }}
```

**Recommendations:**

- Include user profile information when applicable
- Different themes may customize account sections (Bootstrap: user dropdown, Tailwind: flex with avatar, Bulma: .media)
- Keep account-related controls prominent
- Ensure privacy and security considerations
- Include appropriate user identification
- Consider user role-specific content
- Provide clear path to account settings
