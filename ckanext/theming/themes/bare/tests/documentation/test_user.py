from __future__ import annotations

from typing import Any

import pytest
from playwright.sync_api import Page

from ckan import types

from ckanext.theming.themes.bare.tests.conftest import ElementLocator


def test_login(
    doc_screenshot: Any,
    page: Page,
):
    """Test user login page."""
    page.goto("/user/login")
    doc_screenshot("user-login")

    # Show with validation errors
    page.click("button[type='submit']")
    doc_screenshot("user-login-errors")


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


def test_register(
    doc_screenshot: Any,
    page: Page,
):
    """Test user registration page."""
    page.goto("/user/register")
    doc_screenshot("user-register-empty")

    # Fill in form
    page.fill("input[name='name']", "testuser")
    page.fill("input[name='email']", "test@example.com")
    page.fill("input[name='password1']", "test123")
    page.fill("input[name='password2']", "test123")
    doc_screenshot("user-register-filled")


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

    page.goto("/user/" + user["name"])
    doc_screenshot("user-read")

    # Show activity section
    activity = page.get_by_text("Activity Stream")
    activity.scroll_into_view_if_needed()
    doc_screenshot("user-read-activity")

    # Show sidebar
    sidebar = locator.locate_sidebar()
    doc_screenshot("user-read-sidebar", clip=sidebar.bounding_box())

    # Show follow button (logged in as different user)
    login(sysadmin["name"])
    page.reload()
    follow_btn = locator.locate_follow_button()
    if follow_btn.is_visible():
        follow_btn.scroll_into_view_if_needed()
        doc_screenshot("user-read-follow-button")


def test_edit(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test user edit profile page."""
    login(user["name"])
    page.goto("/user/edit")
    doc_screenshot("user-edit")

    # Show with errors
    page.fill("input[name='email']", "invalid-email")
    page.click("button[type='submit']")
    doc_screenshot("user-edit-errors")


def test_activity(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test user activity stream page."""
    # Create some activity
    login(user["name"])
    page.goto("/dataset/new")
    page.fill("input[name='title']", "Test Dataset")
    page.fill("textarea[name='notes']", "Description")
    page.click("button[type='submit']")

    page.goto("/user/activity/" + user["name"])
    doc_screenshot("user-activity")


def test_followers(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test user followers page."""
    # Follow the user
    login(sysadmin["name"])
    page.goto("/user/" + user["name"])
    follow_btn = page.get_by_role("button", name="Follow")
    if follow_btn.is_visible():
        follow_btn.click()

    page.goto("/user/followers/" + user["name"])
    doc_screenshot("user-followers-with-followers")

    # Test empty state
    new_user = sysadmin["name"] + "-new"
    page.goto("/user/followers/" + new_user)
    doc_screenshot("user-followers-empty")


def test_organizations(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    organization_factory: types.TestFactory,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test user organizations page."""
    organization_factory.create(users=[{"name": user["name"], "capacity": "member"}])

    page.goto("/user/" + user["name"] + "/organizations")
    doc_screenshot("user-organizations")

    # Test empty state
    page.goto("/user/" + sysadmin["name"] + "/organizations")
    doc_screenshot("user-organizations-empty")


def test_groups(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    group_factory: types.TestFactory,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test user groups page."""
    group_factory.create(users=[{"name": user["name"], "capacity": "member"}])

    page.goto("/user/" + user["name"] + "/groups")
    doc_screenshot("user-groups")

    # Test empty state
    page.goto("/user/" + sysadmin["name"] + "/groups")
    doc_screenshot("user-groups-empty")


def test_list(
    doc_screenshot: Any,
    page: Page,
    user_factory: types.TestFactory,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test user list page."""
    user_factory.create_batch(5)

    page.goto("/user")
    doc_screenshot("user-list")

    # Test with search
    page.goto("/user?q=" + sysadmin["name"])
    doc_screenshot("user-list-search")


def test_api_tokens(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    api_token_factory: types.TestFactory,
    login: Any,
    locator: ElementLocator,
):
    """Test user API tokens page."""
    api_token_factory(user=user["name"])

    login(user["name"])
    page.goto("/user/" + user["name"] + "/api-tokens")
    doc_screenshot("user-api-tokens")

    # Show create form
    create_form = page.locator("form")
    create_form.scroll_into_view_if_needed()
    doc_screenshot("user-api-tokens-create-form")


def test_request_reset(
    doc_screenshot: Any,
    page: Page,
):
    """Test password reset request page."""
    page.goto("/user/reset")
    doc_screenshot("user-request-reset")


def test_perform_reset(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
):
    """Test password reset perform page."""
    # Note: This requires a valid reset key, which is hard to generate in tests
    # We'll just test the general page structure
    page.goto("/user/reset/invalid-key")
    doc_screenshot("user-perform-reset-invalid-key")


def test_confirm_delete(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    """Test user delete confirmation page."""
    login(sysadmin["name"])
    page.goto("/user/delete/" + user["name"])
    doc_screenshot("user-confirm-delete")


class ElementLocatorUser(ElementLocator):
    def locate_edit_user_button(self):
        """Locate the 'Edit' button on user profile page."""
        return self.page.get_by_role("link", name="Edit")


@pytest.fixture
def locator(page: Page):
    return ElementLocatorUser(page)
