from typing import Any

import pytest
from faker import Faker
from playwright.sync_api import Page

from ckan import types
from ckan.tests.helpers import call_action

from ckanext.theming.themes.bare.tests.conftest import ElementLocator


@pytest.mark.integration
def test_login(
    doc_screenshot: Any,
    page: Page,
):
    """Test user login page."""
    page.goto("/user/login")
    doc_screenshot("user-login")

    page.click("button[type='submit']")
    doc_screenshot("user-login-errors", full_page=False)


@pytest.mark.integration
def test_logout(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    login: Any,
):
    """Test user logout page."""
    login(user["name"])
    page.goto("/user/logout")
    doc_screenshot("user-logout")


@pytest.mark.integration
def test_register(
    doc_screenshot: Any,
    page: Page,
    faker: Faker,
):
    """Test user registration page."""
    page.goto("/user/register")
    page.fill("input[name='name']", faker.user_name())
    page.fill("input[name='email']", faker.email())
    page.fill("input[name='password1']", "test123")
    page.fill("input[name='password2']", "test123")
    doc_screenshot("user-register-form")


@pytest.mark.integration
def test_read(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    package_factory: types.TestFactory,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test user profile page."""
    package_factory.create_batch(3, user_id=user["id"])

    sidebar = locator.locate_sidebar()

    page.goto("/user/" + user["name"])
    doc_screenshot("user-read")

    doc_screenshot("user-read-sidebar", clip=sidebar.bounding_box())

    login(sysadmin["name"])
    page.reload()
    follow_btn = locator.locate_follow_button()
    if follow_btn.is_visible():
        follow_btn.scroll_into_view_if_needed()
        doc_screenshot("user-read-follow-button", clip=sidebar.bounding_box())


@pytest.mark.integration
def test_edit(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    login: Any,
    faker: Faker,
):
    """Test user edit profile page."""
    login(user["name"])
    page.goto("/user/edit")
    doc_screenshot("user-edit")


@pytest.mark.integration
def test_activity(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    faker: Faker,
):
    """Test user activity stream page."""
    login(user["name"])
    call_action("package_create", {"user": user["name"]}, name=faker.slug(), title=faker.sentence())

    page.goto("/user/activity/" + user["name"])
    doc_screenshot("user-activity")


@pytest.mark.integration
def test_followers(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    user_factory: types.TestFactory,
    sysadmin: dict[str, Any],
    login: Any,
):
    """Test user followers page."""
    login(sysadmin["name"])
    page.goto("/user/followers/" + user["name"])
    doc_screenshot("user-followers-empty")

    for follower in user_factory.create_batch(3):
        call_action("follow_user", {"user": follower["name"]}, id=user["id"])

    page.reload()
    doc_screenshot("user-followers-with-followers")


@pytest.mark.integration
def test_organizations(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    organization_factory: types.TestFactory,
):
    """Test user organizations page."""
    organization_factory.create_batch(3, users=[{"name": user["name"], "capacity": "member"}])

    page.goto("/user/" + user["name"] + "/organizations")
    doc_screenshot("user-organizations")


@pytest.mark.integration
def test_groups(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    login: Any,
    group_factory: types.TestFactory,
):
    """Test user groups page."""
    for group in group_factory.create_batch(3):
        call_action("member_create", id=group["id"], object_type="user", object=user["id"], capacity="member")

    login(user["name"])
    page.goto("/user/" + user["name"] + "/groups")
    doc_screenshot("user-groups")


@pytest.mark.integration
def test_list(
    doc_screenshot: Any,
    page: Page,
    user_factory: types.TestFactory,
    sysadmin: dict[str, Any],
    login: Any,
):
    """Test user list page."""
    user_factory.create_batch(5)

    page.goto("/user")
    doc_screenshot("user-list")

    page.goto("/user?q=" + sysadmin["name"])
    doc_screenshot("user-list-search")


@pytest.mark.integration
def test_api_tokens(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    api_token_factory: types.TestFactory,
    login: Any,
):
    """Test user API tokens page."""
    api_token_factory(user=user["name"])

    login(user["name"])
    page.goto("/user/" + user["name"] + "/api-tokens")
    doc_screenshot("user-api-tokens")


@pytest.mark.integration
def test_request_reset(
    doc_screenshot: Any,
    page: Page,
):
    """Test password reset request page."""
    page.goto("/user/reset")
    doc_screenshot("user-request-reset")


@pytest.mark.integration
def test_confirm_delete(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
):
    """Test user delete confirmation page."""
    login(sysadmin["name"])
    page.goto("/user/delete/" + user["name"])
    doc_screenshot("user-confirm-delete")
