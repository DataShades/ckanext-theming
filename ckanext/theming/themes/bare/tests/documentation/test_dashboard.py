from __future__ import annotations

from typing import Any

import pytest
from faker import Faker
from playwright.sync_api import Page

from ckan import types
from ckan.tests.helpers import call_action

from ckanext.theming.themes.bare.tests.conftest import ElementLocator


@pytest.mark.usefixtures("clean_index")
def test_dashboard(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    package_factory: types.TestFactory,
    login: Any,
    locator: ElementLocator,
    faker: Faker,
):
    """Test main dashboard page."""
    login(user["name"])
    call_action("package_create", {"user": user["name"]},
                name=faker.slug(), title=faker.sentence())

    page.goto("/dashboard")
    doc_screenshot("dashboard")

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
    faker: Faker,
):
    """Test dashboard datasets page."""
    login(user["name"])
    call_action("package_create", {"user": user["name"]},
                name=faker.slug(), title=faker.sentence())
    call_action("package_create", {"user": user["name"]},
                name=faker.slug(), title=faker.sentence())
    call_action("package_create", {"user": user["name"]},
                name=faker.slug(), title=faker.sentence())

    page.goto("/dashboard/datasets")
    doc_screenshot("dashboard-datasets")

    new_user = user_factory.create()
    login(new_user["name"])
    page.goto("/dashboard/datasets")
    doc_screenshot("dashboard-datasets-empty")


@pytest.mark.usefixtures("clean_index")
def test_organizations(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    organization_factory: types.TestFactory,
    login: Any,
):
    """Test dashboard organizations page."""
    organization_factory.create(users=[{"name": user["name"], "capacity": "member"}])

    login(user["name"])
    page.goto("/dashboard/organizations")
    doc_screenshot("dashboard-organizations")

    page.goto("/dashboard/organizations")
    doc_screenshot("dashboard-organizations-empty")


@pytest.mark.usefixtures("clean_index")
def test_groups(
    doc_screenshot: Any,
    page: Page,
    user: dict[str, Any],
    group_factory: types.TestFactory,
    login: Any,
):
    """Test dashboard groups page."""
    group_factory.create(users=[{"name": user["name"], "capacity": "member"}])

    login(user["name"])
    page.goto("/dashboard/groups")
    doc_screenshot("dashboard-groups")

    page.goto("/dashboard/groups")
    doc_screenshot("dashboard-groups-empty")


class ElementLocatorDashboard(ElementLocator):
    def locate_dashboard_nav(self):
        """Locate dashboard navigation."""
        return self.page.locator("nav[aria-label='Dashboard']")


@pytest.fixture
def locator(page: Page):
    return ElementLocatorDashboard(page)
