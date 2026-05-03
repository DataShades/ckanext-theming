from __future__ import annotations

from ckan import types

from ckanext.theming import lib


class TestUtils:
    def test_init(self, app: types.CKANApp):
        """Util class initialized in new UI."""
        theme = lib.Theme("test", None)
        ui = theme.build_ui(app.flask_app)  # pyright: ignore[reportAttributeAccessIssue]
        assert isinstance(ui.util, lib.Util)
