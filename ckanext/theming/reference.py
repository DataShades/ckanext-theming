"""Reference definitions for components used in the system."""

from __future__ import annotations

import dataclasses
import enum
import fnmatch
import os
from collections import defaultdict
from collections.abc import Mapping
from typing import Any, Dict

import msgspec


class Matcher(msgspec.Struct):
    pattern: str
    path: list[str]

    def matches(self, arg: str, endpoint: str):
        return fnmatch.fnmatch(f"{arg}:{endpoint}", self.pattern)

    def get(self, arg: str, endpoint: str, data: dict[str, dict[str, Any]]):
        if not self.matches(arg, endpoint):
            return None

        value = data
        for step in self.path:
            value = value[step]
        return value


class Source(msgspec.Struct):
    data: dict[str, dict[str, Any]]
    ignore: list[str]
    matchers: list[Matcher]
    args: dict[str, Any] = msgspec.field(default_factory=dict)


class Category(enum.Enum):
    ESSENTIAL = "essential"
    RECOMMENDED = "recommended"
    UNSTABLE = "unstable"
    CUSTOM = "custom"


@dataclasses.dataclass(frozen=True)
class Component:
    category: Category = Category.CUSTOM
    description: str = ""
    arguments: dict[str, MacroArgument] = dataclasses.field(default_factory=dict)


@dataclasses.dataclass(frozen=True)
class MacroArgument:
    description: str = ""
    type: str = "unknown"


@dataclasses.dataclass(frozen=True)
class Template:
    category: Category = dataclasses.field(default=Category.CUSTOM)


def get_source(filename: str | None = None) -> Source:
    if not filename:
        filename = os.path.join(os.path.dirname(__file__), "dump_source.yaml")

    with open(filename, "rb") as src:
        return msgspec.yaml.decode(src.read(), type=Source)


def make_params(endpoint: str, args: set[str], source: Source, defaults: Mapping[str, Any]):  # noqa: C901
    params: dict[str, Any] = {}
    for arg in args:
        for matcher in source.matchers:
            if value := matcher.get(arg, endpoint, source.data):
                params[arg] = value
                break
        else:
            if arg in source.data:
                params[arg] = source.data[arg]
            elif arg in defaults:
                params[arg] = defaults[arg]
            else:
                raise KeyError(f"{arg}:{endpoint}")
    return params


components: dict[str, Component] = defaultdict(Component)
with open(os.path.join(os.path.dirname(__file__), "components.yaml"), "rb") as src:
    components.update(msgspec.yaml.decode(src.read(), type=Dict[str, Component]))


templates: dict[str, Template] = defaultdict(Template)

with open(os.path.join(os.path.dirname(__file__), "templates.yaml"), "rb") as src:
    templates.update(msgspec.yaml.decode(src.read(), type=Dict[str, Template]))
