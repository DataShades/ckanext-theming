from __future__ import annotations
from typing import Any

from pytest_benchmark.fixture import BenchmarkFixture

import ckan.plugins.toolkit as tk
from faker import Faker
import pytest


@pytest.fixture(autouse=True)
def _setup(with_request_context: Any):
    pass


faker = Faker()
title = faker.sentence()
content = faker.text()


def render(name: str, title: str, content: str):
    return tk.render(
        f"benchmarks/{name}.html",
        {
            "title": title,
            "content": content,
        },
    )


@pytest.mark.parametrize(
    ("name",),
    [
        ["block"],
        ["direct_include"],
        ["macro_direct_include"],
        ["macro_include_with_context"],
        ["macro_include_without_context"],
        ["macro_inline"],
        ["macro_snippet"],
        ["snippet"],
    ],
)
def test_single(benchmark: BenchmarkFixture, name: str):
    benchmark(render, name=name, title=title, content=content)


@pytest.mark.parametrize(
    ("name",),
    [
        ["block_1k"],
        ["direct_include_1k"],
        ["macro_direct_include_1k"],
        ["macro_include_with_context_1k"],
        ["macro_include_without_context_1k"],
        ["macro_inline_1k"],
        ["macro_snippet_1k"],
        ["snippet_1k"],
    ],
)
def test_repeat(benchmark: BenchmarkFixture, name: str):
    benchmark(render, name=name, title=title, content=content)

@pytest.mark.parametrize(
    ("name",),
    [
        ["block_1k"],
        ["direct_include_legion"],
        ["macro_direct_include_legion"],
        ["macro_include_with_context_legion"],
        ["macro_include_without_context_legion"],
        ["macro_inline_legion"],
        ["macro_snippet_legion"],
        ["snippet_legion"],
    ],
)
def test_legion(benchmark: BenchmarkFixture, name: str):
    benchmark(render, name=name, title=title, content=content)
