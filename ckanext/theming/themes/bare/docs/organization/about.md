# Organization About Page

View detailed information about an organization.

## Overview

The about page displays:
- Full organization description
- Contact information
- Organization metadata
- Related links
- Custom fields

## URL Pattern

```
GET /organization/about/{id}
```

**Examples:**
```
<<vars.site_url>>/organization/about/environmental-protection-agency
<<vars.site_url>>/organization/about/5f7f7d1e-8b3a-4c9e-9f1e-2d3c4b5a6e7f
```

## Purpose

The about page allows users to:
- Learn about the organization
- View contact details
- Understand organization's mission
- Access related resources
- See organizational structure

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| View details | Read org information | Main content |
| Edit org | Modify details (if authorized) | Edit button |
| Contact | Reach organization | Contact links |
| Back to org | Return to main page | Back link |

## Template

**File:** `templates/organization/about.html`

### Template Structure

```jinja
{% extends "organization/_base.html" %}

{%- block subtitle -%}
    {{ ui.subtitle_item(_('About')) }}
{%- endblock -%}

{%- block primary_content_inner %}
    <h2>{{ _('About') }} {{ group_dict.title or group_dict.name }}</h2>

    {% if group_dict.image_url %}
        {{ ui.image(group_dict.image_url, alt=group_dict.title, class='org-logo') }}
    {% endif %}

    {% if group_dict.description %}
        <div class="org-description">
            {{ h.render_markdown(group_dict.description) }}
        </div>
    {% endif %}

    <dl class="org-metadata">
        {% if group_dict.created %}
            <dt>{{ _('Created') }}</dt>
            <dd>{{ h.render_datetime(group_dict.created) }}</dd>
        {% endif %}

        {% if group_dict.is_organization %}
            <dt>{{ _('Type') }}</dt>
            <dd>{{ _('Organization') }}</dd>
        {% endif %}

        {% for extra in group_dict.extras %}
            <dt>{{ extra.key }}</dt>
            <dd>{{ extra.value }}</dd>
        {% endfor %}
    </dl>
{% endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `group_dict` | Organization dictionary |
| `group` | Organization object |

## Screenshot Placeholder

![Organization About](../screenshots/organization-about.png)

**What to show:**
- Organization logo/header
- Full description text
- Metadata section
- Contact information
- Custom fields

## Customization Notes

### Description Display

Customize description:
```jinja
{% block description %}
    <div class="about-description">
        {% if group_dict.description %}
            {{ h.render_markdown(group_dict.description) }}
        {% else %}
            <p class="no-description">{{ _('No description available') }}</p>
        {% endif %}
    </div>
{% endblock %}
```

### Contact Information

Add contact section:
```jinja
{% block contact_info %}
    <div class="contact-section">
        <h3>{{ _('Contact Information') }}</h3>

        {% if group_dict.email %}
            <p>{{ ui.icon('envelope') }} {{ ui.link(group_dict.email, 'mailto:' ~ group_dict.email) }}</p>
        {% endif %}

        {% if group_dict.url %}
            <p>{{ ui.icon('link') }} {{ ui.link(group_dict.url, group_dict.url) }}</p>
        {% endif %}

        {% if group_dict.phone %}
            <p>{{ ui.icon('phone') }} {{ group_dict.phone }}</p>
        {% endif %}
    </div>
{% endblock %}
```

### Custom Fields

Display organization extras:
```jinja
{% block custom_fields %}
    <div class="custom-fields">
        <h3>{{ _('Additional Information') }}</h3>
        <dl>
            {% for extra in group_dict.extras %}
                <dt>{{ extra.key }}</dt>
                <dd>{{ h.render_markdown(extra.value) }}</dd>
            {% endfor %}
        </dl>
    </div>
{% endblock %}
```

### Related Links

Add organization links:
```jinja
{% block related_links %}
    <div class="related-links">
        <h3>{{ _('Related Links') }}</h3>
        <ul>
            {% if group_dict.homepage %}
                <li>{{ ui.link(_('Homepage'), group_dict.homepage) }}</li>
            {% endif %}

            {% if group_dict.twitter %}
                <li>{{ ui.link(_('Twitter'), group_dict.twitter) }}</li>
            {% endif %}

            {% if group_dict.linkedin %}
                <li>{{ ui.link(_('LinkedIn'), group_dict.linkedin) }}</li>
            {% endif %}
        </ul>
    </div>
{% endblock %}
```

### Styling

About-specific styling:
```scss
.organization-about {
    .org-logo {
        // Logo display
        max-width: 300px;
        margin-bottom: 2rem;
    }

    .org-description {
        // Description text
        font-size: 1.1rem;
        line-height: 1.8;
        margin-bottom: 2rem;
    }

    .org-metadata {
        // Metadata list
        dt {
            font-weight: 600;
            margin-top: 1rem;
        }

        dd {
            margin-left: 0;
            color: #666;
        }
    }

    .contact-section {
        // Contact info
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 4px;
        margin-top: 2rem;
    }

    .custom-fields {
        // Extra fields
        margin-top: 2rem;
    }
}
```

## Related Pages

- [Organization Read](read.md) - Main organization page
- [Organization Edit](edit.md) - Edit organization
- [Organization Index](index.md) - List all organizations

## Best Practices

1. **Complete Info**: Show all available details
2. **Clear Structure**: Organize information logically
3. **Contact Access**: Make contact info visible
4. **Rich Content**: Support markdown formatting
5. **Custom Fields**: Allow extensibility
6. **Navigation**: Easy return to main page

## Extension Hooks

Extensions can modify about by:
- Adding custom metadata fields
- Adding organization hierarchy
- Adding related organizations
- Adding organization statistics
- Adding custom sections
