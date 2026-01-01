from __future__ import annotations

import pytest
from playwright.sync_api import Page, expect

import ckan.plugins.toolkit as tk


@pytest.mark.usefixtures("with_plugins")
class TestUtil:
    """Test utility pages."""

    def test_primer_page_loads(self, page: Page):
        """Test that the primer page loads successfully."""
        page.goto(tk.url_for("util.primer"))
        expect(page.locator("body")).to_be_visible()

    def test_custom_form_fields_page_loads(self, page: Page):
        """Test that the custom form fields page loads successfully."""
        page.goto(tk.url_for("util.custom_form_fields"))
        expect(page.locator("body")).to_be_visible()

    def test_internal_redirect_page_loads(self, page: Page):
        """Test that the internal redirect page loads successfully."""
        page.goto(tk.url_for("util.internal_redirect"))
        expect(page.locator("body")).to_be_visible()


routes = (
    "util.custom_form_fields",
    "util.internal_redirect",
    "util.primer",
)
