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
- `tertiary_content_inner`: Inner content of the tertiary area
- `content_action`: Content-specific action buttons
- `content_toolbar`: Toolbar for content actions
- `content_footer`: Footer for content area

## Page-Specific Blocks

These blocks are available on specific page types and provide fine-grained control over page content:

### Dataset Pages (`package/read.html`)

- `package_header`: Dataset-specific header
- `package_social`: Social sharing buttons for dataset
- `package_description`: Dataset description area
- `package_tags`: Dataset tags display
- `package_resources`: Dataset resources section
- `package_info`: Dataset metadata information
- `package_license`: License information
- `package_organization`: Organization information
- `package_groups`: Groups information
- `package_activity`: Activity stream for dataset

### Dataset Search (`package/search.html`)

- `dataset_search_title`: Title for dataset search page
- `dataset_search_form`: Dataset search form
- `dataset_search_results`: Search results display
- `dataset_facets`: Facet filters for dataset search
- `dataset_search_adv_filters`: Advanced filters

### Organization Pages (`organization/read.html`)

- `organization_header`: Organization header
- `organization_description`: Organization description
- `organization_content`: Main organization content
- `organization_facets`: Organization-specific facets
- `organization_menu`: Organization navigation menu

### Group Pages (`group/read.html`)

- `group_header`: Group header
- `group_description`: Group description
- `group_content`: Main group content
- `group_facets`: Group-specific facets
- `group_menu`: Group navigation menu

### User Pages (`user/read.html`)

- `user_header`: User header
- `user_about`: User about section
- `user_content`: Main user content
- `user_menu`: User navigation menu
- `user_followers`: User followers section
- `user_activity`: User activity stream

### Dashboard Pages (`user/dashboard.html`)

- `dashboard_header`: Dashboard header
- `dashboard_activity_stream`: Activity stream for dashboard
- `dashboard_datasets`: User's datasets
- `dashboard_organizations`: User's organizations
- `dashboard_groups`: User's groups

### Admin Pages (`admin/index.html`)

- `admin_content`: Main admin content area
- `admin_tabs`: Administrative tabs
- `admin_system_info`: System information display

### Home Page (`home/index.html`)

- `home_header`: Home page header
- `home_introduction`: Introduction section
- `home_main`: Main home page content
- `home_sidebar`: Home page sidebar
- `home_tertiary`: Tertiary content area for home page

### About Page (`home/about.html`)

- `about_header`: About page header
- `about_main`: Main about page content
- `about_sidebar`: About page sidebar

### Error Pages (`error_document_template.html`)

- `error_title`: Error page title
- `error_message`: Error message display
- `error_content`: Main error page content

## Block Relationships

Many blocks work in relationship with each other:

- `primary_content` contains `primary_content_inner`
- `secondary_content` contains `secondary_content_inner`
- `content_action` appears in context of specific content types
- `page_header` contains `page_title` and `breadcrumbs`

## Overriding Blocks

To override a block in a child template:

```jinja2
{% block title %}My Custom Page Title{% endblock %}

{% block content %}
    <div class="my-custom-content">
        {{ super() }}  {# Include parent content #}
        <!-- Additional custom content -->
    </div>
{% endblock %}
```

The `super()` function can be used to include content from the parent template while adding custom content.

## Best Practices

1. Use `super()` when you want to extend rather than replace parent content
2. Maintain semantic structure when overriding blocks
3. Respect accessibility features when customizing navigation blocks
4. Keep related content together within appropriate blocks
5. Use consistent styling patterns across similar block types
