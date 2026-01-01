from __future__ import annotations

import pytest
from playwright.sync_api import Page, expect

import ckan.plugins.toolkit as tk


@pytest.mark.usefixtures("with_plugins")
class TestAdmin:
    """Test admin pages."""

    def test_admin_index_loads(self, page: Page):
        """Test that the admin index page loads successfully."""
        page.goto(tk.url_for("admin.index"))
        expect(page.locator("body")).to_be_visible()

    def test_admin_config_loads(self, page: Page):
        """Test that the admin config page loads successfully."""
        page.goto(tk.url_for("admin.config"))
        expect(page.locator("body")).to_be_visible()

    def test_admin_trash_loads(self, page: Page):
        """Test that the admin trash page loads successfully."""
        page.goto(tk.url_for("admin.trash"))
        expect(page.locator("body")).to_be_visible()

    def test_admin_reset_config_loads(self, page: Page):
        """Test that the admin reset config page loads successfully."""
        page.goto(tk.url_for("admin.reset_config"))
        expect(page.locator("body")).to_be_visible()


routes = (
    "admin.config",
    "admin.index",
    "admin.reset_config",
    "admin.trash",
)
