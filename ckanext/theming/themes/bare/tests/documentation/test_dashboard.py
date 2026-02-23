from __future__ import annotations

from typing import Any

import pytest
from playwright.sync_api import Page

from ckan import types

from ckanext.theming.themes.bare.tests.conftest import ElementLocator


@pytest.mark.usefixtures("clean_index")
def test_dashboard(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    package_factory: types.TestFactory,
    login: Any,
    locator: ElementLocator,
):
    """Test main dashboard page."""
    # Create some activity
    login(user["name"])
    package_factory.create(user_id=user["id"])

    page.goto("/dashboard")
    doc_screenshot("dashboard")

    # Show activity feed
    activity = page.locator(".activity-stream")
    if activity.is_visible():
        activity.scroll_into_view_if_needed()
        doc_screenshot("dashboard-activity")


@pytest.mark.usefixtures("clean_index")
def test_datasets(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    package_factory: types.TestFactory,
    login: Any,
    locator: ElementLocator,
):
    """Test dashboard datasets page."""
    package_factory.create_batch(3, user_id=user["id"])

    login(user["name"])
    page.goto("/dashboard/datasets")
    doc_screenshot("dashboard-datasets")

    # Test empty state
    # Create a new user without datasets
    page.goto("/dashboard/datasets")
    doc_screenshot("dashboard-datasets-empty")


@pytest.mark.usefixtures("clean_index")
def test_organizations(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    organization_factory: types.TestFactory,
    login: Any,
    locator: ElementLocator,
):
    """Test dashboard organizations page."""
    organization_factory.create(users=[{"name": user["name"], "capacity": "member"}])

    login(user["name"])
    page.goto("/dashboard/organizations")
    doc_screenshot("dashboard-organizations")

    # Test empty state
    page.goto("/dashboard/organizations")
    doc_screenshot("dashboard-organizations-empty")


@pytest.mark.usefixtures("clean_index")
def test_groups(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    group_factory: types.TestFactory,
    login: Any,
    locator: ElementLocator,
):
    """Test dashboard groups page."""
    group_factory.create(users=[{"name": user["name"], "capacity": "member"}])

    login(user["name"])
    page.goto("/dashboard/groups")
    doc_screenshot("dashboard-groups")

    # Test empty state
    page.goto("/dashboard/groups")
    doc_screenshot("dashboard-groups-empty")


class ElementLocatorDashboard(ElementLocator):
    def locate_dashboard_nav(self):
        """Locate dashboard navigation."""
        return self.page.locator("nav[aria-label='Dashboard']")


@pytest.fixture
def locator(page: Page):
    return ElementLocatorDashboard(page)
