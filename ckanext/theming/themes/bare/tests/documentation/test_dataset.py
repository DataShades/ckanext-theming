from __future__ import annotations

from typing import Any

import pytest
from playwright.sync_api import Page

from ckan import types
from ckanext.theming.themes.bare.tests.conftest import ElementLocator


@pytest.mark.usefixtures("clean_index")
def test_search(
    doc_screenshot: Any,
    page: Page,
    package_factory: types.TestFactory,
    resource: dict[str, Any],
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    package = package_factory.create_batch(3)[0]
    page.goto("/dataset")
    doc_screenshot("dataset-search-normal")

    page.goto("/dataset?q=" + package["title"])
    doc_screenshot("dataset-search-query-applied")

    page.goto("/dataset?res_format=" + resource["format"])
    doc_screenshot("dataset-search-facet-applied")

    login(sysadmin["name"])
    page.goto("/dataset")
    button = locator.locate_add_dataset_button()
    button.scroll_into_view_if_needed()
    doc_screenshot("dataset-search-add-button")


def test_read(
    doc_screenshot: Any,
    page: Page,
    package: dict[str, Any],
    resource_factory: types.TestFactory,
    sysadmin: dict[str, Any],
    login: Any,
    locator: ElementLocator,
):
    main = locator.locate_main_content()
    sidebar = locator.locate_sidebar()

    resource_factory.create_batch(3, package_id=package["id"])
    page.goto("/dataset/" + package["name"])
    doc_screenshot("dataset-read-normal")

    resources = page.get_by_role("button", name="resources")
    resources.scroll_into_view_if_needed()
    resources.click()
    doc_screenshot("dataset-read-resources", clip=main.bounding_box())

    page.reload()

    info = page.get_by_role("button", name="additional details")
    info.scroll_into_view_if_needed()
    info.click()
    doc_screenshot("dataset-read-additional-info", clip=main.bounding_box())

    login(sysadmin["name"])
    page.reload()
    button = locator.locate_edit_dataset_button()
    button.scroll_into_view_if_needed()
    doc_screenshot("dataset-read-manage-button", clip=main.bounding_box())

    login(sysadmin["name"])
    page.reload()

    button = locator.locate_follow_button()
    button.scroll_into_view_if_needed()

    doc_screenshot("dataset-read-follow-button", clip=sidebar.bounding_box())

    with page.expect_request("/dataset/follow/" + package["id"]):
        button.click()

    doc_screenshot("dataset-read-unfollow-button", clip=sidebar.bounding_box())
