# Error Pages

Error handling and custom error pages.

## Overview

CKAN displays error pages for:
- 404 Not Found
- 403 Forbidden
- 500 Internal Server Error

## URL Patterns

Errors can occur on any URL:
```
/invalid-url              # 404
/protected-page           # 403
/crash-endpoint           # 500
```

## Purpose

Error pages:
- Inform users of problems
- Provide navigation options
- Maintain branding consistency
- Log errors for debugging

## Template

**File:** `templates/error_document_template.html`

### Structure

```jinja
{% extends "_layout.html" %}
{%- set _layout = _layout|default("content_focus") -%}

{%- block subtitle -%}
    {{ ui.subtitle_item(error_code ~ ' ' ~ error_message) }}
{%- endblock -%}

{%- block primary_content_inner %}
    <div class="error-page">
        <h1>{{ error_code }}</h1>
        <p>{{ error_message }}</p>

        {{ ui.button(_('Go Home'), href=h.url_for('home.index')) }}
    </div>
{%- endblock -%}
```

### Error Types

| Code | Message | Description |
|------|---------|-------------|
| 404 | Not Found | Resource doesn't exist |
| 403 | Access Denied | Permission required |
| 500 | Server Error | Application error |

## Screenshot Placeholder

![404 Error](../screenshots/error-404.png)
*Placeholder: Custom 404 error page with branding*

![403 Error](../screenshots/error-403.png)
*Placeholder: Access denied page*

![500 Error](../screenshots/error-500.png)
*Placeholder: Server error page*

## Customization Notes

### Custom Error Messages

```jinja
{% block error_content %}
    {% if error_code == 404 %}
        <p>{{ _("The page you're looking for doesn't exist.") }}</p>
    {% elif error_code == 403 %}
        <p>{{ _("You don't have permission to access this page.") }}</p>
    {% elif error_code == 500 %}
        <p>{{ _("Something went wrong. Please try again later.") }}</p>
    {% endif %}
{% endblock %}
```

### Helpful Links

```jinja
{% block error_links %}
    <div class="error-links">
        {{ ui.button(_('Go Home'), href=h.url_for('home.index')) }}
        {{ ui.button(_('Search'), href=h.url_for('dataset.search')) }}
        {{ ui.button(_('Contact Support'), href=h.url_for('contact') }}
    </div>
{% endblock %}
```

### Styling

```scss
.error-page {
    text-align: center;
    padding: 4rem 2rem;

    h1 {
        font-size: 6rem;
        color: #dc3545;
        margin-bottom: 1rem;
    }

    p {
        font-size: 1.25rem;
        color: #666;
        margin-bottom: 2rem;
    }

    .error-links {
        display: flex;
        gap: 1rem;
        justify-content: center;
    }
}
```

## Related Pages

- [Home](../home/home.md) - Return to home
- [Search](../dataset/search.md) - Search for content
