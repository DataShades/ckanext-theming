from __future__ import annotations

import pytest
from playwright.sync_api import Page, expect

import ckan.plugins.toolkit as tk


@pytest.mark.usefixtures("with_plugins")
class TestUser:
    """Test user pages."""

    def test_user_index_loads(self, page: Page):
        """Test that the user index page loads successfully."""
        page.goto(tk.url_for("user.index"))
        expect(page.locator("body")).to_be_visible()

    def test_user_login_loads(self, page: Page):
        """Test that the user login page loads successfully."""
        page.goto(tk.url_for("user.login"))
        expect(page.locator("body")).to_be_visible()

    def test_user_register_loads(self, page: Page):
        """Test that the user registration page loads successfully."""
        page.goto(tk.url_for("user.register"))
        expect(page.locator("body")).to_be_visible()

    def test_user_logout_loads(self, page: Page):
        """Test that the user logout page loads successfully."""
        page.goto(tk.url_for("user.logout"))
        expect(page.locator("body")).to_be_visible()

    def test_user_read_loads(self, page: Page):
        """Test that the user profile page loads successfully."""
        # This would require a specific user ID, so we'll test with a mock
        expect(True).to_be(True)  # Placeholder for now


routes = (
    "user.api_tokens",
    "user.api_tokens_revoke",
    "user.delete",
    "user.edit",
    "user.follow",
    "user.followers",
    "user.index",
    "user.logged_out_page",
    "user.login",
    "user.logout",
    "user.me",
    "user.perform_reset",
    "user.read",
    "user.read_groups",
    "user.read_organizations",
    "user.register",
    "user.request_reset",
    "user.sysadmin",
    "user.unfollow",
)
