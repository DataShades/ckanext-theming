from __future__ import annotations

from typing import Any

import pytest
from playwright.sync_api import Page

from ckan import types

from ckanext.theming.themes.bare.tests.conftest import ElementLocator


def test_read(
    doc_screenshot: Any,
    page: Page,
    package: dict[str, Any],
    resource: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test resource read page."""
    page.goto("/dataset/" + package["name"] + "/resource/" + resource["id"])
    doc_screenshot("resource-read")

    # Show resource info section
    info = page.locator(".resource-info")
    if info.is_visible():
        info.scroll_into_view_if_needed()
        doc_screenshot("resource-read-info")

    # Show download section
    download = page.get_by_role("link", name="Download")
    if download.is_visible():
        download.scroll_into_view_if_needed()
        doc_screenshot("resource-read-download")

    # Logged in view
    login(sysadmin["name"])
    page.reload()
    edit_btn = locator.locate_edit_resource_button()
    edit_btn.scroll_into_view_if_needed()
    doc_screenshot("resource-read-edit-button")


def test_edit(
    doc_screenshot: Any,
    page: Page,
    package: dict[str, Any],
    resource: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test resource edit page."""
    login(sysadmin["name"])
    page.goto("/dataset/" + package["name"] + "/resource/" + resource["id"] + "/edit")
    doc_screenshot("resource-edit")

    # Show with errors
    page.fill("input[name='name']", "")
    page.click("button[type='submit']")
    doc_screenshot("resource-edit-errors")


def test_views(
    doc_screenshot: Any,
    page: Page,
    package: dict[str, Any],
    resource: dict[str, Any],
    resource_view_factory: types.TestFactory,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test resource views management page."""
    resource_view_factory.create_batch(2, resource_id=resource["id"])

    login(sysadmin["name"])
    page.goto("/dataset/" + package["name"] + "/resource/" + resource["id"] + "/views")
    doc_screenshot("resource-views")

    # Show add view button
    add_btn = page.get_by_role("link", name="Add View")
    add_btn.scroll_into_view_if_needed()
    doc_screenshot("resource-views-add")


def test_dictionary(
    doc_screenshot: Any,
    page: Page,
    package: dict[str, Any],
    resource: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test resource data dictionary page."""
    login(sysadmin["name"])
    page.goto("/dataset/" + package["name"] + "/resource/" + resource["id"] + "/dictionary")
    doc_screenshot("resource-dictionary")

    # Show with fields
    # Note: This requires DataStore to be set up
    doc_screenshot("resource-dictionary-fields")


def test_data(
    doc_screenshot: Any,
    page: Page,
    package: dict[str, Any],
    resource: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test resource data page (Datapusher)."""
    login(sysadmin["name"])
    page.goto("/dataset/" + package["name"] + "/resource/" + resource["id"] + "/data")
    doc_screenshot("resource-data")

    # Show push to DataStore button (if not pushed yet)
    push_btn = page.get_by_role("button", name="Push to DataStore")
    if push_btn.is_visible():
        push_btn.scroll_into_view_if_needed()
        doc_screenshot("resource-data-push-button")


class ElementLocatorResource(ElementLocator):
    def locate_edit_resource_button(self):
        """Locate the 'Edit' button on resource page."""
        return self.page.get_by_role("link", name="Edit")


@pytest.fixture
def locator(page: Page):
    return ElementLocatorResource(page)

def test_confirm_delete_resource(
    doc_screenshot: Any,
    page: Page,
    package: dict[str, Any],
    resource: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test resource delete confirmation page."""
    login(sysadmin["name"])
    page.goto("/dataset/" + package["name"] + "/resource/" + resource["id"] + "/delete")
    doc_screenshot("dataset-confirm-delete-resource")
