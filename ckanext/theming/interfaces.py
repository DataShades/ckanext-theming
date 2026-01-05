from __future__ import annotations

from typing import TYPE_CHECKING

from ckan.plugins import Interface

if TYPE_CHECKING:
    from ckanext.theming.lib import UI, Theme


class ITheme(Interface):
    """Allow extensions to provide custom themes for CKAN."""

    def register_themes(self) -> list[Theme]:
        """Register themes provided by extension.

        Example::

            def register_themes(self):
                from ckan.lib.theme import Theme

                return {
                    Theme("mytheme", "/path/to/mytheme"),
                    Theme(
                        "myothertheme",
                        "/path/to/myothertheme",
                        parent="templates",
                    ),
                }

        :returns: themes provided by the extension
        :rtype: list

        """
        return []

    def get_additional_theme_ui_sources(self) -> list[str]:
        """Get additional UI macro files for themes.

        Extensions can use this hook to provide additional files that themes
        can use. The returned list should contain paths to the macro
        files. These paths will be made available to all themes. Themes can
        then include these macros in their own UI definitions. This allows for
        sharing common UI components across multiple themes. For example, an
        extension might provide a set of standard UI components that themes can
        utilize.

        """
        return []

    def patch_theme_ui(self, theme: Theme, ui: UI):
        """Customize the UI for a theme.

        This method is called for each theme UI instance is created via
        :py:meth:`~ckanext.theming.lib.Theme.build_ui`. Extensions can use this
        hook to add custom UI components or modify existing ones.

        Example::

            def build_theme_ui(self, theme, ui):
                ui.add_component("divider", lambda *args, **kwargs: Markup("<hr/>"))

        :param theme: The theme being built
        :type theme: :py:class:`~ckan.lib.theme.Theme`
        :param ui: The UI object to customize
        :type ui: :py:class:`~ckanext.theming.lib.UI`

        """
