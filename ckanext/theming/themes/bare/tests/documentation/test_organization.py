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
    """Test organization list page."""
    group_factory.create_batch(3, is_organization=True)
    page.goto("/organization")
    doc_screenshot("organization-index")

    # Test with search
    page.goto("/organization?q=nonexistent")
    doc_screenshot("organization-index-search-empty")

    # Test with add button (logged in)
    login(sysadmin["name"])
    page.goto("/organization")
    doc_screenshot("organization-index-with-add-button")


@pytest.mark.usefixtures("clean_index")
def test_read(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    package_factory: types.TestFactory,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test organization read page."""
    package_factory.create_batch(3, owner_org=organization["id"])

    page.goto("/organization/" + organization["name"])
    doc_screenshot("organization-read")

    # Show datasets section
    datasets = page.get_by_text("Datasets")
    datasets.scroll_into_view_if_needed()
    doc_screenshot("organization-read-datasets")

    # Show sidebar info
    sidebar = locator.locate_sidebar()
    doc_screenshot("organization-read-sidebar", clip=sidebar.bounding_box())

    # Logged in view
    login(sysadmin["name"])
    page.reload()
    edit_btn = locator.locate_edit_organization_button()
    edit_btn.scroll_into_view_if_needed()
    doc_screenshot("organization-read-edit-button")


@pytest.mark.usefixtures("clean_index")
def test_about(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test organization about page."""
    page.goto("/organization/about/" + organization["name"])
    doc_screenshot("organization-about")


@pytest.mark.usefixtures("clean_index")
def test_new(
    doc_screenshot: Any,
    page: Page,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test organization creation page."""
    login(sysadmin["name"])
    page.goto("/organization/new")
    doc_screenshot("organization-new-empty")

    # Fill in basic fields
    page.fill("input[name='title']", "Test Organization")
    page.fill("textarea[name='description']", "This is a test organization")
    doc_screenshot("organization-new-filled")


@pytest.mark.usefixtures("clean_index")
def test_edit(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test organization edit page."""
    login(sysadmin["name"])
    page.goto("/organization/edit/" + organization["name"])
    doc_screenshot("organization-edit-form")

    # Show delete section
    delete_section = page.locator(".delete-section")
    if delete_section.is_visible():
        delete_section.scroll_into_view_if_needed()
        doc_screenshot("organization-edit-delete-section")


@pytest.mark.usefixtures("clean_index")
def test_members(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    user: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test organization members page."""
    # Add a member first
    login(sysadmin["name"])
    page.goto("/organization/member_new/" + organization["name"])
    page.fill("input[name='username']", user["name"])
    page.select_option("select[name='role']", "member")
    page.click("button[type='submit']")

    page.goto("/organization/members/" + organization["name"])
    doc_screenshot("organization-members")

    # Test empty state
    empty_org = user["name"] + "-empty-org"
    page.goto("/organization/members/" + empty_org)
    doc_screenshot("organization-members-empty")


@pytest.mark.usefixtures("clean_index")
def test_member_new(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test organization add member page."""
    login(sysadmin["name"])
    page.goto("/organization/member_new/" + organization["name"])
    doc_screenshot("organization-member-new")

    # Show role descriptions
    role_help = page.locator(".role-help")
    if role_help.is_visible():
        role_help.scroll_into_view_if_needed()
        doc_screenshot("organization-member-new-role-help")


@pytest.mark.usefixtures("clean_index")
def test_manage_members(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    user: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test organization manage members page."""
    # Add a member first
    login(sysadmin["name"])
    page.goto("/organization/member_new/" + organization["name"])
    page.fill("input[name='username']", user["name"])
    page.select_option("select[name='role']", "member")
    page.click("button[type='submit']")

    page.goto("/organization/member_manage/" + organization["name"])
    doc_screenshot("organization-manage-members")


@pytest.mark.usefixtures("clean_index")
def test_admins(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test organization administrators page."""
    page.goto("/organization/admins/" + organization["name"])
    doc_screenshot("organization-admins")

    # Test empty state
    empty_org = sysadmin["name"] + "-empty-org"
    page.goto("/organization/admins/" + empty_org)
    doc_screenshot("organization-admins-empty")


@pytest.mark.usefixtures("clean_index")
def test_activity(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test organization activity stream page."""
    page.goto("/organization/activity/" + organization["name"])
    doc_screenshot("organization-activity")


@pytest.mark.usefixtures("clean_index")
def test_changes(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test organization changes page."""
    # Make a change first
    login(sysadmin["name"])
    page.goto("/organization/edit/" + organization["name"])
    page.fill("textarea[name='description']", "Updated description")
    page.click("button[type='submit']")

    page.goto("/organization/changes/" + organization["name"])
    doc_screenshot("organization-changes")


@pytest.mark.usefixtures("clean_index")
def test_bulk_process(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    package_factory: types.TestFactory,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test organization bulk process page."""
    package_factory.create_batch(3, owner_org=organization["id"])

    login(sysadmin["name"])
    page.goto("/organization/bulk_process/" + organization["name"])
    doc_screenshot("organization-bulk-process")


@pytest.mark.usefixtures("clean_index")
def test_confirm_delete(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test organization delete confirmation page."""
    login(sysadmin["name"])
    page.goto("/organization/delete/" + organization["name"])
    doc_screenshot("organization-confirm-delete")


@pytest.mark.usefixtures("clean_index")
def test_confirm_delete_member(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    user: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test organization delete member confirmation page."""
    # Add a member first
    login(sysadmin["name"])
    page.goto("/organization/member_new/" + organization["name"])
    page.fill("input[name='username']", user["name"])
    page.select_option("select[name='role']", "member")
    page.click("button[type='submit']")

    page.goto("/organization/member_delete/" + organization["name"])
    doc_screenshot("organization-confirm-delete-member")


class ElementLocatorOrg(ElementLocator):
    def locate_edit_organization_button(self):
        """Locate the 'Edit' button on organization page."""
        return self.page.get_by_role("link", name="Edit")


@pytest.fixture
def locator(page: Page):
    return ElementLocatorOrg(page)
