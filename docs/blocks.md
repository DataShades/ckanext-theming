---
icon: material/hammer-wrench
status: draft
---
# Template Blocks

CKAN theming system provides a comprehensive set of template blocks that allow themes to customize different parts of the page layout. These blocks are defined in the base templates and can be overridden by child templates to customize the appearance and content of specific sections.

## Generic Blocks (Available on All Pages)

These blocks are defined in `_base.html` and `_layout.html` templates and are available on all pages throughout the application:

### Page Structure Blocks

- `title`: Sets the page title in the `<title>` tag
- `meta`: Contains meta tags in the head section
- `head_extras`: Additional head content (CSS, favicons, etc.)
- `body_extras`: Additional attributes for the body tag
- `flash`: Displays flash messages
- `skip`: Skip navigation links for accessibility
- `masthead`: Site header/masthead section
- `skip_primary_nav`: Skip link for primary navigation
- `primary_nav`: Main navigation menu
- `content`: Main content area
- `footer`: Page footer content

### Layout Blocks

- `prelude`: Content before the main layout
- `layout`: The main layout structure
- `main_content`: The main content section
- `secondary_content`: Sidebar or secondary content area
- `tertiary_content`: Additional content area (if needed)
- `page_header`: Page-specific header content
- `page_title`: Page title display
- `breadcrumbs`: Breadcrumb navigation
- `actions_content`: Action buttons or links area

### Content Blocks

- `primary_content_inner`: Inner content of the main content area
- `secondary_content_inner`: Inner content of the secondary area
- `content_action`: Content-specific action buttons
- `content_toolbar`: Toolbar for content actions
- `content_footer`: Footer for content area

## Page-Specific Blocks

These blocks are available on specific page types and provide fine-grained
control over page content:

TBA
