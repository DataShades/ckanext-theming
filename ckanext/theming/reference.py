"""Reference definitions for components used in the system."""

from __future__ import annotations

import dataclasses
import enum
import fnmatch
import os
from collections import defaultdict
from collections.abc import Mapping
from typing import Any

import msgspec


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


def make_params(endpoint: str, args: set[str], source: dict[str, Any], defaults: Mapping[str, Any]):  # noqa: C901
    params: dict[str, Any] = {}
    data = source.get("data", {})
    matchers = source.get("matchers", [])
    for arg in args:
        for pattern, path in matchers:
            if not fnmatch.fnmatch(f"{arg}:{endpoint}", pattern):
                continue
            value = data
            for step in path:
                value = value[step]
            params[arg] = value
            break
        else:
            if arg in data:
                params[arg] = data[arg]
            elif arg in defaults:
                params[arg] = defaults[arg]
            else:
                raise KeyError(f"{arg}:{endpoint}")
    return params


components: dict[str, Component] = defaultdict(Component)
with open(os.path.join(os.path.dirname(__file__), "components.yaml"), "rb") as src:
    components.update(msgspec.yaml.decode(src.read(), type=dict[str, Component]))


templates: dict[str, Template] = defaultdict(Template)

with open(os.path.join(os.path.dirname(__file__), "templates.yaml"), "rb") as src:
    templates.update(msgspec.yaml.decode(src.read(), type=dict[str, Template]))
