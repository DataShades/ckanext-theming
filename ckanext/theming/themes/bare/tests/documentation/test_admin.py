from __future__ import annotations

from typing import Any

import pytest
from playwright.sync_api import Page

from ckanext.theming.themes.bare.tests.conftest import ElementLocator


@pytest.mark.usefixtures("clean_index")
def test_index(
    doc_screenshot: Any,
    page: Page,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test admin panel page."""
    login(sysadmin["name"])
    page.goto("/ckan-admin")
    doc_screenshot("admin-index")

    # Show admin tools section
    tools = page.locator(".admin-tools")
    if tools.is_visible():
        tools.scroll_into_view_if_needed()
        doc_screenshot("admin-index-tools")


@pytest.mark.usefixtures("clean_index")
def test_config(
    doc_screenshot: Any,
    page: Page,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test admin config page."""
    login(sysadmin["name"])
    page.goto("/ckan-admin/config")
    doc_screenshot("admin-config")

    # Show form fields
    form = page.locator("form")
    form.scroll_into_view_if_needed()
    doc_screenshot("admin-config-form")


@pytest.mark.usefixtures("clean_index")
def test_confirm_reset(
    doc_screenshot: Any,
    page: Page,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test admin confirm reset configuration page."""
    login(sysadmin["name"])
    page.goto("/ckan-admin/reset_config")
    doc_screenshot("admin-confirm-reset")


@pytest.mark.usefixtures("clean_index")
def test_trash(
    doc_screenshot: Any,
    page: Page,
    sysadmin: dict[str, Any],
    package_factory: types.TestFactory,
    login: Any,
    locator: ElementLocator,
):
    """Test admin trash page."""
    # Create and delete a dataset
    pkg = package_factory.create()
    login(sysadmin["name"])
    page.goto("/dataset/delete/" + pkg["name"])
    page.click("button[type='submit']")

    page.goto("/ckan-admin/trash")
    doc_screenshot("admin-trash")

    # Show confirm delete dialog
    page.click("button[name='action'][value='package']")
    doc_screenshot("admin-trash-confirm-delete")


class ElementLocatorAdmin(ElementLocator):
    def locate_admin_nav(self):
        """Locate admin navigation."""
        return self.page.locator("nav[aria-label='Admin']")


@pytest.fixture
def locator(page: Page):
    return ElementLocatorAdmin(page)
