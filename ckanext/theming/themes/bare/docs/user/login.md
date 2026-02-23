# User Login Page

User authentication page for logging into CKAN.

## Overview

The login page provides:
- Username/email and password fields
- Remember me option
- Password reset link
- Registration link
- Error messages for failed login

## URL Pattern

```
GET /user/login
POST /user/login
```

**Example:**
```
<<vars.site_url>>/user/login
<<vars.site_url>>/user/login?came_from=/dataset
```

## Purpose

The login page allows users to:
- Authenticate with credentials
- Access protected features
- Return to original page after login
- Reset forgotten password
- Create new account

## Actions Available

| Action | Description | Element |
|--------|-------------|---------|
| Login | Authenticate | Submit button |
| Remember me | Stay logged in | Checkbox |
| Reset password | Recover account | Reset link |
| Register | Create account | Register link |
| Cancel | Return to previous | Cancel link |

## Template

**File:** `templates/user/login.html`

### Template Structure

```jinja
{% extends "user/_base.html" %}

{%- block subtitle -%}
    {{ ui.subtitle_item(_('Login')) }}
{%- endblock -%}

{%- block primary_content_inner %}
    <h2>{{ _('Login') }}</h2>

    {% if g.user and g.user != 'loggedout' %}
        {{ ui.alert(_('You are already logged in as {user}').format(user=g.user), style='warning') }}
    {% endif %}

    {{ ui.form(method="POST") }}
        {{ ui.form_errors(error_summary) }}

        {{ ui.input(
            name='login',
            label=_('Username'),
            placeholder=_('Username or email'),
            value=request.params.login,
            errors=errors.login,
            required=true
        ) }}

        {{ ui.input(
            name='password',
            label=_('Password'),
            type='password',
            value='',
            errors=errors.password,
            required=true
        ) }}

        {{ ui.checkbox(
            name='remember',
            label=_('Remember me'),
            checked=request.params.remember
        ) }}

        {{ ui.form_actions() }}
            {{ ui.submit(_('Login')) }}
        {{ ui.form_actions() }}
    {{ ui.form() }}

    <div class="login-links">
        {{ ui.link(_('Forgot password?'), h.url_for('user.request_reset')) }}
        {{ ui.link(_('Register'), h.url_for('user.register')) }}
    </div>
{%- endblock -%}
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `error_summary` | Login error messages |
| `errors` | Field validation errors |
| `came_from` | Return URL after login |
| `g.user` | Current user (if any) |

## Screenshot Placeholder

![Login Page](../screenshots/user-login.png)

**What to show:**
- Login form centered
- Username/email field
- Password field
- Remember me checkbox
- Login button
- Forgot password link
- Register link
- Error messages (if any)

## Customization Notes

### Form Fields

Default login fields:
- Login (username or email)
- Password
- Remember me (optional)

### Custom Authentication

Add OAuth2/social login:
```jinja
{% block social_login %}
    <div class="social-login">
        <h3>{{ _('Or login with') }}</h3>

        {{ ui.button(_('Google'), href=h.url_for('user.google_login'), icon='google') }}
        {{ ui.button(_('GitHub'), href=h.url_for('user.github_login'), icon='github') }}
        {{ ui.button(_('Microsoft'), href=h.url_for('user.microsoft_login'), icon='microsoft') }}
    </div>
{% endblock %}
```

### Error Messages

Customize error display:
```jinja
{% block error_messages %}
    {% if error_summary %}
        {{ ui.alert(error_summary, style='danger') }}
    {% endif %}

    {% if errors.login %}
        {{ ui.alert(_('Invalid username or password'), style='danger') }}
    {% endif %}
{% endblock %}
```

### Remember Me

Persistent login:
```jinja
{% block remember_me %}
    <div class="remember-me">
        <label>
            {{ ui.checkbox(name='remember', checked=request.params.remember) }}
            <span>{{ _('Stay logged in for 30 days') }}</span>
        </label>
    </div>
{% endblock %}
```

### Return URL

Handle came_from parameter:
```jinja
{{ ui.hidden_input(name='came_from', value=came_from or h.url_for('home.index')) }}
```

### Styling

Login-specific styling:
```scss
.user-login {
    .login-form {
        // Form container
        max-width: 400px;
        margin: 2rem auto;
        padding: 2rem;
        border: 1px solid #eee;
        border-radius: 8px;
    }

    .login-links {
        // Links below form
        display: flex;
        justify-content: space-between;
        margin-top: 1.5rem;
        padding-top: 1.5rem;
        border-top: 1px solid #eee;
    }

    .social-login {
        // Social login buttons
        margin-top: 2rem;

        button {
            width: 100%;
            margin-bottom: 0.5rem;
        }
    }

    .remember-me {
        // Remember me checkbox
        margin: 1rem 0;

        label {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
    }
}
```

## Related Pages

- [Register](new.md) - Create account
- [Request Reset](request-reset.md) - Password recovery
- [Dashboard](../dashboard/dashboard.md) - After login destination
- [User Profile](read.md) - User profile page

## Best Practices

1. **Clear Errors**: Show specific error messages
2. **Remember Me**: Offer persistent login
3. **Return URL**: Redirect back after login
4. **Alternative Login**: Provide OAuth options
5. **Accessibility**: Ensure keyboard navigation
6. **Security**: Use HTTPS, CSRF protection

## Extension Hooks

Extensions can modify login by:
- Adding OAuth providers
- Adding CAPTCHA
- Adding 2FA support
- Adding SSO integration
- Adding login throttling
