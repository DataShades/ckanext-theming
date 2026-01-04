from __future__ import annotations

from typing import Any

import pytest
from playwright.sync_api import Page, expect

import ckan.plugins.toolkit as tk


@pytest.mark.usefixtures("with_plugins")
class TestIndex:
    def test_title(self, page: Page, login: Any, sysadmin: dict[str, Any], title_builder: Any):
        """Test that the stats index page has the correct title."""
        login(sysadmin)
        page.goto(tk.url_for("stats.index"))

        expected = title_builder("Statistics")
        expect(page).to_have_title(expected)
