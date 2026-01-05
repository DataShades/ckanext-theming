from __future__ import annotations

from typing import Any

import pytest
from playwright.sync_api import Page

import ckan.plugins.toolkit as tk
from ckan.plugins import plugin_loaded
from ckan.types import FixtureCkanConfig, TestFactory

from ckanext.theming import reference


@pytest.mark.usefixtures("with_plugins", "clean_db", "clean_index")
class TestPages:
    def test_screenshots(  # noqa: PLR0913, C901
        self,
        page: Page,
        screenshot: Any,
        user_factory: TestFactory,
        package_factory: TestFactory,
        group_factory: TestFactory,
        organization_factory: TestFactory,
        resource_factory: TestFactory,
        resource_view_factory: TestFactory,
        ckan_config: FixtureCkanConfig,
        sysadmin: dict[str, Any],
        login: Any,
    ):
        page_size = ckan_config["ckan.datasets_per_page"]
        users = user_factory.create_batch(page_size + 1)
        groups = group_factory.create_batch(page_size + 1, users=[{"name": users[0]["id"], "capacity": "member"}])
        organizations = organization_factory.create_batch(
            page_size + 1, users=[{"name": users[0]["id"], "capacity": "member"}]
        )
        packages = package_factory.create_batch(page_size + 1, owner_org=organizations[0]["id"])
        resources = resource_factory.create_batch(2, package_id=packages[0]["id"])
        views = resource_view_factory.create_batch(2, resource_id=resources[0]["id"])

        for name, route in reference.routes.items():
            if route.plugin and not plugin_loaded(route.plugin):
                continue

            if not route.check_availability():
                continue

            login(sysadmin if route.authenticated else "")

            params = route.make_params(
                name,
                {
                    "resource": resources[0],
                    "package": packages[0],
                    "resource_view": views[0],
                    "group": groups[0],
                    "organization": organizations[0],
                    "user": users[0],
                },
            )

            url = tk.url_for(route.endpoint or name, **params)
            page.goto(url)
            screenshot(name)
