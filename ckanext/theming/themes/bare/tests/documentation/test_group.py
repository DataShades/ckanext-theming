from __future__ import annotations

from typing import Any

import pytest
from playwright.sync_api import Page

from ckan import types

from ckanext.theming.themes.bare.tests.conftest import ElementLocator


@pytest.mark.usefixtures("clean_index")
def test_index(
    doc_screenshot: Any,
    page: Page,
    group_factory: types.TestFactory,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test group list page."""
    group_factory.create_batch(3)
    page.goto("/group")
    doc_screenshot("group-index")

    # Test with search
    page.goto("/group?q=nonexistent")
    doc_screenshot("group-index-search-empty")

    # Test with add button (logged in)
    login(sysadmin["name"])
    page.goto("/group")
    doc_screenshot("group-index-with-add-button")


@pytest.mark.usefixtures("clean_index")
def test_read(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    package_factory: types.TestFactory,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test group read page."""
    package_factory.create_batch(3, groups=[{"id": group["id"]}])

    page.goto("/group/" + group["name"])
    doc_screenshot("group-read")

    # Show datasets section
    datasets = page.get_by_text("Datasets")
    datasets.scroll_into_view_if_needed()
    doc_screenshot("group-read-datasets")

    # Show sidebar info
    sidebar = locator.locate_sidebar()
    doc_screenshot("group-read-sidebar", clip=sidebar.bounding_box())


@pytest.mark.usefixtures("clean_index")
def test_about(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test group about page."""
    page.goto("/group/about/" + group["name"])
    doc_screenshot("group-about")


@pytest.mark.usefixtures("clean_index")
def test_new(
    doc_screenshot: Any,
    page: Page,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test group creation page."""
    login(sysadmin["name"])
    page.goto("/group/new")
    doc_screenshot("group-new-empty")

    # Fill in basic fields
    page.fill("input[name='title']", "Test Group")
    page.fill("textarea[name='description']", "This is a test group")
    doc_screenshot("group-new-filled")


@pytest.mark.usefixtures("clean_index")
def test_edit(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test group edit page."""
    login(sysadmin["name"])
    page.goto("/group/edit/" + group["name"])
    doc_screenshot("group-edit-form")


@pytest.mark.usefixtures("clean_index")
def test_members(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    user: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test group members page."""
    # Add a member first
    login(sysadmin["name"])
    page.goto("/group/member_new/" + group["name"])
    page.fill("input[name='username']", user["name"])
    page.select_option("select[name='role']", "member")
    page.click("button[type='submit']")

    page.goto("/group/members/" + group["name"])
    doc_screenshot("group-members")


@pytest.mark.usefixtures("clean_index")
def test_member_new(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test group add member page."""
    login(sysadmin["name"])
    page.goto("/group/member_new/" + group["name"])
    doc_screenshot("group-member-new")


@pytest.mark.usefixtures("clean_index")
def test_manage_members(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    user: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test group manage members page."""
    # Add a member first
    login(sysadmin["name"])
    page.goto("/group/member_new/" + group["name"])
    page.fill("input[name='username']", user["name"])
    page.select_option("select[name='role']", "member")
    page.click("button[type='submit']")

    page.goto("/group/member_manage/" + group["name"])
    doc_screenshot("group-manage-members")


@pytest.mark.usefixtures("clean_index")
def test_admins(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test group administrators page."""
    page.goto("/group/admins/" + group["name"])
    doc_screenshot("group-admins")


@pytest.mark.usefixtures("clean_index")
def test_activity(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test group activity stream page."""
    page.goto("/group/activity/" + group["name"])
    doc_screenshot("group-activity")


@pytest.mark.usefixtures("clean_index")
def test_changes(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test group changes page."""
    # Make a change first
    login(sysadmin["name"])
    page.goto("/group/edit/" + group["name"])
    page.fill("textarea[name='description']", "Updated description")
    page.click("button[type='submit']")

    page.goto("/group/changes/" + group["name"])
    doc_screenshot("group-changes")


@pytest.mark.usefixtures("clean_index")
def test_followers(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    user: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test group followers page."""
    login(user["name"])

    # Follow the group first
    page.goto("/group/" + group["name"])
    follow_btn = page.get_by_role("button", name="Follow")
    if follow_btn.is_visible():
        follow_btn.click()

    login(sysadmin["name"])
    page.goto("/group/followers/" + group["name"])
    doc_screenshot("group-followers-with-followers")


@pytest.mark.usefixtures("clean_index")
def test_confirm_delete(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test group delete confirmation page."""
    login(sysadmin["name"])
    page.goto("/group/delete/" + group["name"])
    doc_screenshot("group-confirm-delete")


@pytest.mark.usefixtures("clean_index")
def test_confirm_delete_member(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    user: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test group delete member confirmation page."""
    # Add a member first
    login(sysadmin["name"])
    page.goto("/group/member_new/" + group["name"])
    page.fill("input[name='username']", user["name"])
    page.select_option("select[name='role']", "member")
    page.click("button[type='submit']")

    page.goto("/group/member_delete/" + group["name"])
    doc_screenshot("group-confirm-delete-member")


class ElementLocatorGroup(ElementLocator):
    def locate_edit_group_button(self):
        """Locate the 'Edit' button on group page."""
        return self.page.get_by_role("link", name="Edit")


@pytest.fixture
def locator(page: Page):
    return ElementLocatorGroup(page)
