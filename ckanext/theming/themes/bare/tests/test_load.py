import pytest

from ckan import types

from ckanext.theming import lib


@pytest.fixture
def util():
    return lib.Util(lib.Theme("bare", None))


def test_init(app: types.CKANApp):
    """Util class initialized in new UI."""
    theme = lib.Theme("bare", None, ui_factory=lib.MacroUI)
    ui = theme.build_ui(app.flask_app)
    assert isinstance(ui.util, lib.Util)
