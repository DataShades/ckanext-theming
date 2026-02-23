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
    group_factory: types.TestFactory,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test group list page."""
    group_factory.create_batch(3)
    page.goto("/group")
    doc_screenshot("group-index")

    page.goto("/group?q=nonexistent")
    doc_screenshot("group-index-search-empty")

    login(sysadmin["name"])
    page.goto("/group")
    button = locator.locate_add_group_button()
    button.scroll_into_view_if_needed()
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

    main = locator.locate_main_content()
    sidebar = locator.locate_sidebar()

    page.goto("/group/" + group["name"])
    doc_screenshot("group-read")

    datasets = page.get_by_text("datasets")
    datasets.scroll_into_view_if_needed()
    doc_screenshot("group-read-datasets", clip=main.bounding_box())

    doc_screenshot("group-read-sidebar", clip=sidebar.bounding_box())

    login(sysadmin["name"])
    page.reload()
    button = locator.locate_edit_group_button()
    button.scroll_into_view_if_needed()
    doc_screenshot("group-read-edit-button", clip=main.bounding_box())


@pytest.mark.usefixtures("clean_index")
def test_about(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
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
    faker: Faker,
):
    """Test group creation page."""
    login(sysadmin["name"])
    page.goto("/group/new")
    page.fill("input[name='title']", faker.sentence())
    page.fill("textarea[name='description']", faker.paragraph())
    doc_screenshot("group-new-form")


@pytest.mark.usefixtures("clean_index")
def test_edit(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
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
):
    """Test group members page."""
    call_action("group_member_create", {"user": sysadmin["name"]},
                id=group["id"], username=user["name"], role="member")

    page.goto("/group/members/" + group["name"])
    doc_screenshot("group-members")


@pytest.mark.usefixtures("clean_index")
def test_member_new(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
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
):
    """Test group manage members page."""
    call_action("group_member_create", {"user": sysadmin["name"]},
                id=group["id"], username=user["name"], role="member")

    login(sysadmin["name"])
    page.goto("/group/member_manage/" + group["name"])
    doc_screenshot("group-manage-members")


@pytest.mark.usefixtures("clean_index")
def test_admins(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
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
    faker: Faker,
):
    """Test group activity stream page."""
    login(sysadmin["name"])
    call_action("group_patch", {"user": sysadmin["name"]},
                id=group["id"], title=faker.sentence())
    call_action("group_patch", {"user": sysadmin["name"]},
                id=group["id"], description=faker.paragraph())

    page.goto("/group/activity/" + group["name"])
    doc_screenshot("group-activity")


@pytest.mark.usefixtures("clean_index")
def test_changes(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    faker: Faker,
):
    """Test group changes page."""
    login(sysadmin["name"])
    call_action("group_patch", {"user": sysadmin["name"]},
                id=group["id"], description=faker.paragraph())

    page.goto("/group/changes/" + group["name"])
    doc_screenshot("group-changes")


@pytest.mark.usefixtures("clean_index")
def test_followers(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    user_factory: types.TestFactory,
    sysadmin: dict[str, Any],
    login: Any,
):
    """Test group followers page."""
    login(sysadmin["name"])
    page.goto("/group/followers/" + group["name"])
    doc_screenshot("group-followers-empty")

    for user in user_factory.create_batch(3):
        call_action("follow_group", {"user": user["name"]}, id=group["id"])

    page.reload()
    doc_screenshot("group-followers-with-followers")


@pytest.mark.usefixtures("clean_index")
def test_confirm_delete(
    doc_screenshot: Any,
    page: Page,
    group: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
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
):
    """Test group delete member confirmation page."""
    call_action("group_member_create", {"user": sysadmin["name"]},
                id=group["id"], username=user["name"], role="member")

    login(sysadmin["name"])
    page.goto("/group/member_delete/" + group["name"])
    doc_screenshot("group-confirm-delete-member")


class ElementLocatorGroup(ElementLocator):
    def locate_add_group_button(self):
        """Locate the 'Add Group' button."""
        return self.page.get_by_role("link", name="Add Group")

    def locate_edit_group_button(self):
        """Locate the 'Edit' button on group page."""
        return self.page.get_by_role("link", name="Edit")


@pytest.fixture
def locator(page: Page):
    return ElementLocatorGroup(page)
