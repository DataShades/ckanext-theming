from __future__ import annotations

from typing import Any

import pytest
from faker import Faker
from playwright.sync_api import Page

from ckan import types
from ckan.tests.helpers import call_action

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
    faker: Faker,
):
    """Test admin config page."""
    login(sysadmin["name"])
    page.goto("/ckan-admin/config")
    doc_screenshot("admin-config")

    form = page.locator("form")
    form.scroll_into_view_if_needed()
    doc_screenshot("admin-config-form")


@pytest.mark.usefixtures("clean_index")
def test_confirm_reset(
    doc_screenshot: Any,
    page: Page,
    sysadmin: dict[str, Any],
    login: Any,
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
    pkg = package_factory.create()
    login(sysadmin["name"])
    call_action("package_delete", {"user": sysadmin["name"]}, id=pkg["id"])

    page.goto("/ckan-admin/trash")
    doc_screenshot("admin-trash")

    page.click("button[name='action'][value='package']")
    doc_screenshot("admin-trash-confirm-delete")


class ElementLocatorAdmin(ElementLocator):
    def locate_admin_nav(self):
        """Locate admin navigation."""
        return self.page.locator("nav[aria-label='Admin']")


@pytest.fixture
def locator(page: Page):
    return ElementLocatorAdmin(page)
