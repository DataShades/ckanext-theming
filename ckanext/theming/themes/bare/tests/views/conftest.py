from __future__ import annotations

import re

import pytest
from playwright.sync_api import Page

from ckan import types


class ElementLocator:
    page: Page

    def __init__(self, page: Page):
        self.page = page

    def locate_breadcrumbs(self):
        """Locate the breadcrumbs element on the page."""
        return self.page.locator("nav[aria-label='Breadcrumb']")


@pytest.fixture
def locator(page: Page):
    return ElementLocator(page)


@pytest.fixture
def title_builder(ckan_config: types.FixtureCkanConfig):
    """Provides a function to build page titles based on CKAN configuration.

    Usage:
        def test_example(page: Page, title_builder):
            expected_title = title_builder("Section", "Page")
            assert page.title() == expected_title

    """
    delimiter = " " + ckan_config["ckan.template_title_delimiter"] + " "

    def builder(*parts: str, pattern: bool = False):
        value = delimiter.join(parts + (ckan_config["ckan.site_title"],))
        if pattern:
            value = re.compile(value)

        return value

    return builder
