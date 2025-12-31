from __future__ import annotations

import re
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
    """Provides a function for authentication using API token.

    Usage:
        def test_example(page: Page, token_login):
            token_login("myuser")

    This will set the Authorization header for subsequent requests made by the page. To
    log out, call token_login with `None` or empty string, e.g., `token_login(None)`.
    """

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
    """Provides a function for authentication by setting the remember cookie.

    Usage:
        def test_example(page: Page, login):
            login("testuser")
            page.goto("http://example.com/protected")

    This will set the remember cookie for 'testuser', allowing access to protected pages. To
    log out, call login with `None` or empty string, e.g., `login(None)`.
    """

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
    """Fixture to take screenshots during a test.

    Usage:
        def test_example(page: Page, screenshot):
            page.goto("http://example.com")
            screenshot("homepage")

    This will save a screenshot to 'screenshots/{test_name}__0001_homepage.jpeg'. Each
    subsequent call to screenshot within the same test will increment the step number.
    """
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


@pytest.fixture
def title_builder(ckan_config: types.FixtureCkanConfig):
    """Provides a function to build page titles based on CKAN configuration.

    Usage:
        def test_example(page: Page, title_builder):
            expected_title = title_builder("Section", "Page")
            assert page.title() == expected_title

    """
    delimiter = " " + ckan_config["ckan.template_title_delimiter"] + " "

    def builder(*parts: str, pattern: bool = False):
        value = delimiter.join(parts + (ckan_config["ckan.site_title"],))
        if pattern:
            value = re.compile(value)

        return value

    return builder
