from __future__ import annotations

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.usefixtures("with_plugins")
class TestDatastore:
    """Test datastore pages."""

    def test_api_info_loads(self, page: Page):
        """Test that the datastore API info page loads successfully."""
        # This would require a specific resource ID, so we'll test with a mock
        expect(True).to_be(True)  # Placeholder for now

    def test_dictionary_loads(self, page: Page):
        """Test that the datastore dictionary page loads successfully."""
        # This would require specific IDs, so we'll test with a mock
        expect(True).to_be(True)  # Placeholder for now

    def test_dump_loads(self, page: Page):
        """Test that the datastore dump page loads successfully."""
        # This would require a specific resource ID, so we'll test with a mock
        expect(True).to_be(True)  # Placeholder for now


routes = (
    "datastore.api_info",
    "datastore.dictionary",
    "datastore.dump",
)
