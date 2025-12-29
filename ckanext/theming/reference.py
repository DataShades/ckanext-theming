"""Reference definitions for components used in the system."""

from __future__ import annotations

import dataclasses
import enum
from collections import defaultdict


class Category(enum.Enum):
    ESSENTIAL = enum.auto()
    OPTIONAL = enum.auto()
    CUSTOM = enum.auto()


@dataclasses.dataclass(frozen=True)
class Component:
    category: Category = dataclasses.field(default=Category.CUSTOM)


components: dict[str, Component] = defaultdict(Component)

components.update(
    {
        "link": Component(Category.ESSENTIAL),
        "accordion": Component(Category.OPTIONAL),
    }
)
