from typing import Any

import pytest
from playwright.sync_api import Page


@pytest.mark.integration
def test_homepage(doc_screenshot: Any, page: Page):
    page.goto("/")
    doc_screenshot("home-home")


@pytest.mark.integration
def test_about(doc_screenshot: Any, page: Page):
    page.goto("/about")
    doc_screenshot("home-about")
