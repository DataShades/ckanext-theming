from __future__ import annotations

import pytest
from playwright.sync_api import Page


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
