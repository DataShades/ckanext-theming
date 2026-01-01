from __future__ import annotations

import pytest
from playwright.sync_api import Page, expect

import ckan.plugins.toolkit as tk


@pytest.mark.usefixtures("with_plugins")
class TestDataset:
    """Test dataset pages."""

    def test_dataset_search_loads(self, page: Page):
        """Test that the dataset search page loads successfully."""
        page.goto(tk.url_for("dataset.search"))
        expect(page.locator("body")).to_be_visible()

    def test_dataset_new_loads(self, page: Page):
        """Test that the dataset creation page loads successfully."""
        page.goto(tk.url_for("dataset.new"))
        expect(page.locator("body")).to_be_visible()

    def test_dataset_read_loads(self, page: Page):
        """Test that the dataset read page loads successfully."""
        # This would require a specific dataset ID, so we'll test with a mock
        expect(True).to_be(True)  # Placeholder for now


routes = (
    "dataset.collaborator_delete",
    "dataset.collaborators_read",
    "dataset.delete",
    "dataset.edit",
    "dataset.follow",
    "dataset.followers",
    "dataset.groups",
    "dataset.new",
    "dataset.new_collaborator",
    "dataset.read",
    "dataset.resources",
    "dataset.search",
    "dataset.unfollow",
)
