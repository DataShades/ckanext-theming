from typing import Any

import pytest
from faker import Faker
from playwright.sync_api import Page

from ckan import types
from ckan.tests.helpers import call_action

from ckanext.theming.themes.bare.tests.conftest import ElementLocator


@pytest.mark.integration
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


@pytest.mark.integration
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


@pytest.mark.integration
def test_about(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
):
    """Test organization about page."""
    page.goto("/organization/about/" + organization["name"])
    doc_screenshot("organization-about")


@pytest.mark.integration
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


@pytest.mark.integration
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


@pytest.mark.integration
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


@pytest.mark.integration
def test_members(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    user: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
):
    """Test organization members page."""
    call_action(
        "organization_member_create",
        {"user": sysadmin["name"]},
        id=organization["id"],
        username=user["name"],
        role="member",
    )

    page.goto("/organization/members/" + organization["name"])
    doc_screenshot("organization-members")


@pytest.mark.integration
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


@pytest.mark.integration
def test_manage_members(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    user: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
):
    """Test organization manage members page."""
    call_action(
        "organization_member_create",
        {"user": sysadmin["name"]},
        id=organization["id"],
        username=user["name"],
        role="member",
    )

    login(sysadmin["name"])
    page.goto("/organization/manage_members/" + organization["name"])
    doc_screenshot("organization-manage-members")


@pytest.mark.integration
def test_confirm_delete_member(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    user: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
):
    """Test organization delete member confirmation page."""
    call_action(
        "organization_member_create",
        {"user": sysadmin["name"]},
        id=organization["id"],
        username=user["name"],
        role="member",
    )

    login(sysadmin["name"])
    page.goto("/organization/member_delete/" + organization["name"] + "?user=" + sysadmin["name"])
    doc_screenshot("organization-confirm-delete-member")


@pytest.mark.integration
def test_admins(
    doc_screenshot: Any,
    page: Page,
    organization: dict[str, Any],
    sysadmin: dict[str, Any],
):
    """Test organization administrators page."""
    page.goto("/organization/admins/" + organization["name"])
    doc_screenshot("organization-admins")


@pytest.mark.integration
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
    call_action("organization_patch", {"user": sysadmin["name"]}, id=organization["id"], title=faker.company())
    call_action("organization_patch", {"user": sysadmin["name"]}, id=organization["id"], description=faker.paragraph())

    page.goto("/organization/activity/" + organization["name"])
    doc_screenshot("organization-activity")


@pytest.mark.integration
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
