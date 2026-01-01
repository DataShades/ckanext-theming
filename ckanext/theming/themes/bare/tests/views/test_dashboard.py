from __future__ import annotations

import pytest
from playwright.sync_api import Page, expect

import ckan.plugins.toolkit as tk


@pytest.mark.usefixtures("with_plugins")
class TestDashboard:
    """Test dashboard pages."""

    def test_dashboard_datasets_loads(self, page: Page):
        """Test that the dashboard datasets page loads successfully."""
        page.goto(tk.url_for("dashboard.datasets"))
        expect(page.locator("body")).to_be_visible()

    def test_dashboard_groups_loads(self, page: Page):
        """Test that the dashboard groups page loads successfully."""
        page.goto(tk.url_for("dashboard.groups"))
        expect(page.locator("body")).to_be_visible()

    def test_dashboard_organizations_loads(self, page: Page):
        """Test that the dashboard organizations page loads successfully."""
        page.goto(tk.url_for("dashboard.organizations"))
        expect(page.locator("body")).to_be_visible()


routes = (
    "dashboard.datasets",
    "dashboard.groups",
    "dashboard.organizations",
)
