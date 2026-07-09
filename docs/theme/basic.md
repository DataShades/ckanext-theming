# Basic Theme Creation

A theme defines the visual identity of a CKAN instance. The simplest way to create a theme is to bootstrap it using the CLI and start mapping standard CKAN components.

---

## 3-Step Theme Setup

/// Note

Theme is a collection of files that must be registered inside an **existing
plugin**. We assume that you already have `ckanext-mytheme` extension. Switch
to the folder where you want to keep themes before proceeding with the
guide. For example:

```sh
cd ckanext-mytheme/ckanext/mytheme
```

In this way, theme folder will be created next to `plugin.py`.

///


### Bootstrap the Structure

Use the CKAN CLI to create a theme directory containing the default folder structure:
```bash
ckan theme create my_basic_theme
```

This creates `my_basic_theme/` directory and copies content of the `bare`
theme into it.

/// tip

You can copy any existing theme, not only the `bare` theme. To specify
other theme as a seed for creation, use `--base` parameter.

```bash
ckan theme create --base=midnight-blue-portable  my_basic_theme
```

The base theme must be available, i.e. the plugin that provides the theme
must be enabled.

///

### Register the Theme

In your extension's `plugin.py`, implement the `ITheme` interface and
register your theme by returning a list of `Theme` instances from
`register_themes()`.

Specify the name of the theme as a first argument to the `Theme`
constructor, and the absolute path to theme files as a second
argument.

```python title="plugin.py" hl_lines="11"
import os
import ckan.plugins as p
from ckanext.theming.interfaces import ITheme
from ckanext.theming.lib import Theme

class MyThemePlugin(ITheme, p.SingletonPlugin):

    def register_themes(self) -> list[Theme]:
        root = os.path.dirname(os.path.abspath(__file__))
        return [
            Theme("my_basic_theme", os.path.join(root, "my_basic_theme"))
        ]
```


/// note

Theme sometimes includes `theme.py` file with `make_theme` function, that
accepts theme name and simplifies theme registration.

For example, `bare` theme has such function to you can implement
`ITheme.register_themes` like this:

```py title="plugin.py" hl_lines="7"
from .my_basic_theme.theme import make_theme

class MyThemePlugin(ITheme, p.SingletonPlugin):

    def register_themes(self) -> list[Theme]:
        return [
            make_theme("my_basic_theme")
        ]
```

If you see `make_theme` function inside `theme.py` file, prioritize using
it for theme creation, as this function may do additional setup. For
example, `bare` theme registers emoji icons inside `make_theme`.

///

/// tip

If your extension contains multiple themes, or you just don't want to mix theme
files with plugin files, even though there is nothing wrong with it, you can
create theme inside the subfolder. Specify path to the theme's parent folder as
a second argument for the CLI command

```sh
ckan theme create my_basic_theme ./themes
```

Assuming you are inside `ckanext-mytheme/ckanext/mytheme` folder when
executing the command, you'll have
`ckanext-mytheme/ckanext/mytheme/themes/my_basic_theme` folder with all
templates and assets.

As you can guess, by default parent folder of the theme is set to `./`.

///

/// warning

Most likely, theme enables webassets inside `templates/base.html` or
`templates/page.html`.

Theme assets are always called as `theming/THEME_NAME/ASSET_NAME`. If you
created theme using `bare` theme as a base, you'll see something like
`#!django {% asset "theming/bare/..." %}`; if you used
`midnight-blue-portable` as a base, look for text with looking like
`#!django {% asset "theming/midnight-blue-portalbe/..."  %}`. Usually there
will be one asset for styles and one for scripts.

As you are using different name for the theme, `my_basic_theme`, you need
to rename assets to `"theming/my_basic_theme/..."`. Otherwise styles and
scripts won't be loaded and you'll see broken page.

///

### Activate the Theme

Make sure that `theming` and your theme plugin is enabled. Then activate newly
created theme via `ckan.ui.theme`.

```ini
ckan.plugins = ... my_theme_plugin theming
ckan.ui.theme = my_basic_theme
```

Do not forget to enable `theming` plugin - without it your theme will be
ignored.

/// note

Due to CKAN's plugin load order, it's recommended to put `theming` plugin
in the end of the plugins list, so that other extensions have a chance to
override templates provided by theme.

If you place theming plugin at the beginning of the plugins list, it will
have the highest priority and override any matching template from other
extensions.

The plugin that provides your theme can be placed anywhere, as it's
`theming` who actually activates the theme and registers all the
templates. But it's recommended to keep them together and treat combination
`my_theme_plugin theming` as a single unit that must never be separated.

///

---

## Minimal File Structure

A basic theme requires at least the following file structure to map macros and assets:

```
my_basic_theme/
 ├── templates/
 │   └── macros/
 │       └── ui.html       # Primary UI component macro mappings
 └── assets/
     └── webassets.yml     # Asset bundle config for theme css/js
```

---

## Implementing the `macros/ui.html`

The `templates/macros/ui.html` file serves as the main entry point for the
theming system. Whenever a template calls `#!django {{ ui.button(...) }}` or
`#!django {{ ui.card(...) }}`, the loader maps the call to a macro defined
inside this file.

Here is an example `ui.html` content.

```django title="templates/macros/ui.html"
{# Import base helper macros if needed, or define directly #}

{%- macro button(content, href, type="button", style="primary") -%}
    {%- if href -%}
        <a {{ ui.util.attrs(kwargs, {"class": "btn btn-" ~ style}) }} href="{{ href }}">
            {{ content }}
        </a>
    {%- else -%}
        <button {{ ui.util.attrs(kwargs, {"class": "btn btn-" ~ style}) }} type="{{ type }}">
            {{ content }}
        </button>
    {%- endif -%}
{%- endmacro -%}

{%- macro card(content, title) -%}
    <div {{ ui.util.attrs(kwargs, {"class": "card"}) }}>
        {%- if title -%}
            <div class="card-header">{{ title }}</div>
        {%- endif -%}
        <div class="card-body">{{ content }}</div>
    </div>
{%- endmacro -%}
```

/// tip

There are more then 100 components that every theme must implement. To check
what components are missing from the active theme, use CLI:

```sh
ckan theme component check
```

You can also get more details about the implemented component using `analyze` command. For
example, to get details of the `button` component:

```sh
ckan theme component analyze button
```

This command shows brief description of the component and its standard
attributes. If implementation contains more or less arguments than expected,
they will be marked via `+` and `-` signs in the command output.

///
