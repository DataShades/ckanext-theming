from __future__ import annotations

from typing import TYPE_CHECKING

from ckan.plugins import Interface

if TYPE_CHECKING:
    from ckan.lib.theme import Theme


class ITheme(Interface):
    """Allow extensions to provide custom themes for CKAN."""

    def register_themes(self) -> dict[str, Theme]:
        """Register themes provided by extension.

        The returned dictionary must map theme names to
        :py:class:`~ckan.lib.theme.Theme` objects.

        Example::

            def register_themes(self):
                from ckan.lib.theme import Theme

                return {
                    "mytheme": Theme("/path/to/mytheme"),
                    "myothertheme": Theme(
                        "/path/to/myothertheme",
                        extends="templates",
                    ),
                }

        :returns: themes provided by the extension
        :rtype: dict

        """
        return {}
