from __future__ import annotations

from typing import Any

from playwright.sync_api import Page


def test_homepage(doc_screenshot: Any, page: Page):
    page.goto("/")
    doc_screenshot("homepage_normal")


def test_about(doc_screenshot: Any, page: Page):
    page.goto("/about")
    doc_screenshot("aboutpage_normal")
