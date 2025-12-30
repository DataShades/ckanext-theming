from __future__ import annotations

from typing import Any

import pytest
from flask_login import encode_cookie  # pyright: ignore[reportUnknownVariableType]
from playwright.sync_api import BrowserContext, Page

from ckan import types


@pytest.fixture
def browser_context_args(browser_context_args: dict[str, Any], ckan_config: dict[str, Any]):
    """Modify playwright's standard configuration of browser's context."""
    browser_context_args["base_url"] = ckan_config["ckan.site_url"]
    return browser_context_args


@pytest.fixture
def token_login(api_token_factory: Any, page: Page):
    """Provides a function for authentication using API token."""

    def authenticator(user: str | dict[str, Any], _page: Page | None = None):
        if _page is None:
            _page = page

        if isinstance(user, dict):
            user = user["name"]

        token: str = api_token_factory(user=user)["token"] if user else ""

        _page.set_extra_http_headers({"Authorization": token})

    return authenticator


@pytest.fixture
def login(page: Page, context: BrowserContext, ckan_config: types.FixtureCkanConfig, with_request_context: Any):
    """Provides a function for authentication by setting the remember cookie."""

    def authenticator(user: str | dict[str, Any], _page: Page | None = None):
        if _page is None:
            _page = page

        if isinstance(user, dict):
            user = user["name"]

        key = ckan_config["REMEMBER_COOKIE_NAME"]
        url = ckan_config["ckan.site_url"]

        if user:
            context.add_cookies([{"name": key, "value": encode_cookie(user), "url": url}])
        else:
            context.clear_cookies()

    return authenticator


@pytest.fixture
def screenshot(page: Page, request: pytest.FixtureRequest):
    """Fixture to take screenshots at in a test."""
    step = 1

    def func(name: str, _page: Page | None = None, **kwargs: Any):
        """Takes a screenshot and saves it to the test-results directory."""
        nonlocal step
        node = request.node  # pyright: ignore[reportUnknownVariableType]
        if _page is None:
            _page = page

        prefix: str = node.originalname[5:]  # pyright: ignore[reportUnknownVariableType]
        kwargs["path"] = f"screenshots/{prefix}__{step:04d}_{name}.jpeg"
        step += 1
        return _page.screenshot(**kwargs, full_page=True)

    return func
