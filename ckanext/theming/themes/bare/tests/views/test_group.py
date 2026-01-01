from __future__ import annotations

import pytest
from playwright.sync_api import Page, expect

import ckan.plugins.toolkit as tk


@pytest.mark.usefixtures("with_plugins")
class TestGroup:
    """Test group pages."""

    def test_group_index_loads(self, page: Page):
        """Test that the group index page loads successfully."""
        page.goto(tk.url_for("group.index"))
        expect(page.locator("body")).to_be_visible()

    def test_group_new_loads(self, page: Page):
        """Test that the group creation page loads successfully."""
        page.goto(tk.url_for("group.new"))
        expect(page.locator("body")).to_be_visible()

    def test_organization_index_loads(self, page: Page):
        """Test that the organization index page loads successfully."""
        page.goto(tk.url_for("organization.index"))
        expect(page.locator("body")).to_be_visible()

    def test_organization_new_loads(self, page: Page):
        """Test that the organization creation page loads successfully."""
        page.goto(tk.url_for("organization.new"))
        expect(page.locator("body")).to_be_visible()


routes = (
    "group.about",
    "group.admins",
    "group.bulk_process",
    "group.delete",
    "group.edit",
    "group.follow",
    "group.followers",
    "group.index",
    "group.manage_members",
    "group.member_delete",
    "group.member_dump",
    "group.member_new",
    "group.members",
    "group.new",
    "group.read",
    "group.unfollow",
    "organization.about",
    "organization.admins",
    "organization.bulk_process",
    "organization.delete",
    "organization.edit",
    "organization.follow",
    "organization.followers",
    "organization.index",
    "organization.manage_members",
    "organization.member_delete",
    "organization.member_dump",
    "organization.member_new",
    "organization.members",
    "organization.new",
    "organization.read",
    "organization.unfollow",
)
