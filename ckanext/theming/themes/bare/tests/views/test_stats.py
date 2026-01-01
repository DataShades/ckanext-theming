from __future__ import annotations

import pytest
from playwright.sync_api import Page, expect

import ckan.plugins.toolkit as tk


@pytest.mark.usefixtures("with_plugins")
class TestStats:
    """Test statistics pages."""

    def test_stats_index_loads(self, page: Page):
        """Test that the stats index page loads successfully."""
        page.goto(tk.url_for("stats.index"))
        expect(page.locator("body")).to_be_visible()


routes = ("stats.index",)
