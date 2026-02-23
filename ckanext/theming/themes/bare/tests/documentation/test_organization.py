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
    organization_factory: types.TestFactory,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test organization list page."""
    organization_factory.create_batch(3)
    page.goto("/organization")
    doc_screenshot("organization-index")

    page.goto("/organization?q=nonexistent")
    doc_screenshot("organization-index-search-empty")

    login(sysadmin["name"])
    page.goto("/organization")
    button = locator.locate_add_organization_button()
    button.scroll_into_view_if_needed()
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

    main = locator.locate_main_content()
    sidebar = locator.locate_sidebar()

    page.goto("/organization/" + organization["name"])
    doc_screenshot("organization-read")

    datasets = page.get_by_text("datasets")
    datasets.scroll_into_view_if_needed()
    doc_screenshot("organization-read-datasets", clip=main.bounding_box())

    doc_screenshot("organization-read-sidebar", clip=sidebar.bounding_box())

    login(sysadmin["name"])
    page.reload()
    button = locator.locate_edit_organization_button()
    button.scroll_into_view_if_needed()
    doc_screenshot("organization-read-edit-button", clip=main.bounding_box())


@pytest.mark.usefixtures("clean_index")
def test_about(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
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
    faker: Faker,
):
    """Test organization creation page."""
    login(sysadmin["name"])
    page.goto("/organization/new")
    page.fill("input[name='title']", faker.company())
    page.fill("textarea[name='description']", faker.paragraph())
    doc_screenshot("organization-new-form")


@pytest.mark.usefixtures("clean_index")
def test_edit(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
):
    """Test organization edit page."""
    login(sysadmin["name"])
    page.goto("/organization/edit/" + organization["name"])
    doc_screenshot("organization-edit-form")

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
):
    """Test organization members page."""
    call_action("organization_member_create", {"user": sysadmin["name"]},
                id=organization["id"], username=user["name"], role="member")

    page.goto("/organization/members/" + organization["name"])
    doc_screenshot("organization-members")

    page.goto("/organization/members/nonexistent")
    doc_screenshot("organization-members-empty")


@pytest.mark.usefixtures("clean_index")
def test_member_new(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
):
    """Test organization add member page."""
    login(sysadmin["name"])
    page.goto("/organization/member_new/" + organization["name"])
    doc_screenshot("organization-member-new")

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
):
    """Test organization manage members page."""
    call_action("organization_member_create", {"user": sysadmin["name"]},
                id=organization["id"], username=user["name"], role="member")

    login(sysadmin["name"])
    page.goto("/organization/member_manage/" + organization["name"])
    doc_screenshot("organization-manage-members")


@pytest.mark.usefixtures("clean_index")
def test_admins(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    sysadmin: dict[str, Any],
):
    """Test organization administrators page."""
    page.goto("/organization/admins/" + organization["name"])
    doc_screenshot("organization-admins")

    page.goto("/organization/admins/nonexistent")
    doc_screenshot("organization-admins-empty")


@pytest.mark.usefixtures("clean_index")
def test_activity(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    faker: Faker,
):
    """Test organization activity stream page."""
    login(sysadmin["name"])
    call_action("organization_patch", {"user": sysadmin["name"]},
                id=organization["id"], title=faker.company())
    call_action("organization_patch", {"user": sysadmin["name"]},
                id=organization["id"], description=faker.paragraph())

    page.goto("/organization/activity/" + organization["name"])
    doc_screenshot("organization-activity")


@pytest.mark.usefixtures("clean_index")
def test_changes(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    faker: Faker,
):
    """Test organization changes page."""
    login(sysadmin["name"])
    call_action("organization_patch", {"user": sysadmin["name"]},
                id=organization["id"], description=faker.paragraph())

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
):
    """Test organization delete member confirmation page."""
    call_action("organization_member_create", {"user": sysadmin["name"]},
                id=organization["id"], username=user["name"], role="member")

    login(sysadmin["name"])
    page.goto("/organization/member_delete/" + organization["name"])
    doc_screenshot("organization-confirm-delete-member")


class ElementLocatorOrg(ElementLocator):
    def locate_add_organization_button(self):
        """Locate the 'Add Organization' button."""
        return self.page.get_by_role("link", name="Add Organization")

    def locate_edit_organization_button(self):
        """Locate the 'Edit' button on organization page."""
        return self.page.get_by_role("link", name="Edit")


@pytest.fixture
def locator(page: Page):
    return ElementLocatorOrg(page)
