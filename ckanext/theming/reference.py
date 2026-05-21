"""Reference definitions for components used in the system."""

from __future__ import annotations

import dataclasses
import enum
import fnmatch
import os
from collections import defaultdict
from collections.abc import Mapping
from typing import Any

import yaml


class Category(enum.Enum):
    ESSENTIAL = "essential"
    RECOMMENDED = "recommended"
    UNSTABLE = "unstable"
    CUSTOM = "custom"


@dataclasses.dataclass(frozen=True)
class Component:
    category: Category = Category.CUSTOM
    description: str = ""
    arguments: dict[str, Any] = dataclasses.field(default_factory=dict)


@dataclasses.dataclass(frozen=True)
class MacroArgument:
    description: str = ""
    type: str = "unknown"


@dataclasses.dataclass(frozen=True)
class HtmlMacroArgument(MacroArgument):
    type: str = "HTML"


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
    components.update(
        {
            k: Component(
                category=Category(v["category"]),
                description=v.get("description", ""),
                arguments={name: MacroArgument(**details) for name, details in v.get("arguments", {}).items()},
            )
            for k, v in yaml.safe_load(src).items()
        }
    )

components.update({})


templates: dict[str, Template] = defaultdict(Template)
templates.update(
    {
        "_footer.html": Template(Category.RECOMMENDED),
        "_page.html": Template(Category.RECOMMENDED),
        "error_document_template.html": Template(Category.ESSENTIAL),
        "_header.html": Template(Category.RECOMMENDED),
        "_base.html": Template(Category.RECOMMENDED),
        "datapusher/resource_data.html": Template(Category.ESSENTIAL),
        "group/confirm_delete_member.html": Template(Category.ESSENTIAL),
        "group/members.html": Template(Category.ESSENTIAL),
        "group/confirm_delete.html": Template(Category.ESSENTIAL),
        "group/admins.html": Template(Category.ESSENTIAL),
        "group/edit.html": Template(Category.ESSENTIAL),
        "group/index.html": Template(Category.ESSENTIAL),
        "group/new.html": Template(Category.ESSENTIAL),
        "group/about.html": Template(Category.ESSENTIAL),
        "group/new_group_form.html": Template(Category.ESSENTIAL),
        "group/changes.html": Template(Category.ESSENTIAL),
        "group/read.html": Template(Category.ESSENTIAL),
        "group/member_new.html": Template(Category.ESSENTIAL),
        "group/activity_stream.html": Template(Category.ESSENTIAL),
        "group/followers.html": Template(Category.ESSENTIAL),
        "group/_base.html": Template(Category.RECOMMENDED),
        "group/manage_members.html": Template(Category.ESSENTIAL),
        "group/_edit_base.html": Template(Category.RECOMMENDED),
        "group/snippets/info.html": Template(Category.ESSENTIAL),
        "macros/ui.html": Template(Category.ESSENTIAL),
        "macros/ui/snippets/activity.html": Template(Category.ESSENTIAL),
        "macros/ui/snippets/facet.html": Template(Category.ESSENTIAL),
        "macros/ui/snippets/group.html": Template(Category.ESSENTIAL),
        "macros/ui/snippets/license.html": Template(Category.ESSENTIAL),
        "macros/ui/snippets/organization.html": Template(Category.ESSENTIAL),
        "macros/ui/snippets/package.html": Template(Category.ESSENTIAL),
        "macros/ui/snippets/resource.html": Template(Category.ESSENTIAL),
        "macros/ui/snippets/search_form.html": Template(Category.ESSENTIAL),
        "macros/ui/snippets/user.html": Template(Category.ESSENTIAL),
        "admin/trash.html": Template(Category.ESSENTIAL),
        "admin/config.html": Template(Category.ESSENTIAL),
        "admin/index.html": Template(Category.ESSENTIAL),
        "admin/confirm_reset.html": Template(Category.ESSENTIAL),
        "admin/_base.html": Template(Category.RECOMMENDED),
        "admin/snippets/confirm_delete.html": Template(Category.ESSENTIAL),
        "package/confirm_delete.html": Template(Category.ESSENTIAL),
        "package/edit.html": Template(Category.ESSENTIAL),
        "package/resource_views.html": Template(Category.ESSENTIAL),
        "package/group_list.html": Template(Category.ESSENTIAL),
        "package/search.html": Template(Category.ESSENTIAL),
        "package/resources.html": Template(Category.ESSENTIAL),
        "package/new.html": Template(Category.ESSENTIAL),
        "package/resource_edit.html": Template(Category.ESSENTIAL),
        "package/changes.html": Template(Category.ESSENTIAL),
        "package/edit_view.html": Template(Category.ESSENTIAL),
        "package/read.html": Template(Category.ESSENTIAL),
        "package/new_resource_not_draft.html": Template(Category.ESSENTIAL),
        "package/new_resource.html": Template(Category.ESSENTIAL),
        "package/_resource_edit_base.html": Template(Category.ESSENTIAL),
        "package/new_view.html": Template(Category.ESSENTIAL),
        "package/activity_stream.html": Template(Category.ESSENTIAL),
        "package/followers.html": Template(Category.ESSENTIAL),
        "package/_base.html": Template(Category.RECOMMENDED),
        "package/resource_read.html": Template(Category.ESSENTIAL),
        "package/resource_history.html": Template(Category.ESSENTIAL),
        "package/history.html": Template(Category.ESSENTIAL),
        "package/confirm_delete_resource.html": Template(Category.ESSENTIAL),
        "package/_edit_base.html": Template(Category.RECOMMENDED),
        "package/snippets/resource_form.html": Template(Category.ESSENTIAL),
        "package/snippets/info.html": Template(Category.ESSENTIAL),
        "package/snippets/_search_facets.html": Template(Category.ESSENTIAL),
        "package/snippets/search_htmx.html": Template(Category.ESSENTIAL),
        "package/snippets/_resource_view.html": Template(Category.ESSENTIAL),
        "package/snippets/_search_results.html": Template(Category.ESSENTIAL),
        "package/snippets/package_form.html": Template(Category.ESSENTIAL),
        "package/snippets/_package_metadata_fields.html": Template(Category.ESSENTIAL),
        "package/snippets/_package_basic_fields.html": Template(Category.ESSENTIAL),
        "package/collaborators/confirm_delete.html": Template(Category.ESSENTIAL),
        "package/collaborators/collaborator_new.html": Template(Category.ESSENTIAL),
        "package/collaborators/collaborators.html": Template(Category.ESSENTIAL),
        "snippets/csrf_input.html": Template(Category.ESSENTIAL),
        "snippets/follow_button.html": Template(Category.ESSENTIAL),
        "snippets/activity_stream.html": Template(Category.ESSENTIAL),
        "home/_about_text.html": Template(Category.ESSENTIAL),
        "home/index.html": Template(Category.ESSENTIAL),
        "home/about.html": Template(Category.ESSENTIAL),
        "home/robots.txt": Template(Category.ESSENTIAL),
        "ckanext/stats/index.html": Template(Category.ESSENTIAL),
        "development/primer.html": Template(Category.ESSENTIAL),
        "user/dashboard_datasets.html": Template(Category.ESSENTIAL),
        "user/dashboard.html": Template(Category.ESSENTIAL),
        "user/api_tokens.html": Template(Category.ESSENTIAL),
        "user/confirm_delete.html": Template(Category.ESSENTIAL),
        "user/edit.html": Template(Category.ESSENTIAL),
        "user/new_user_form.html": Template(Category.ESSENTIAL),
        "user/logout.html": Template(Category.ESSENTIAL),
        "user/read_groups.html": Template(Category.ESSENTIAL),
        "user/dashboard_organizations.html": Template(Category.ESSENTIAL),
        "user/new.html": Template(Category.ESSENTIAL),
        "user/read_organizations.html": Template(Category.ESSENTIAL),
        "user/perform_reset.html": Template(Category.ESSENTIAL),
        "user/request_reset.html": Template(Category.ESSENTIAL),
        "user/logout_first.html": Template(Category.ESSENTIAL),
        "user/read.html": Template(Category.ESSENTIAL),
        "user/edit_user_form.html": Template(Category.ESSENTIAL),
        "user/activity_stream.html": Template(Category.ESSENTIAL),
        "user/followers.html": Template(Category.ESSENTIAL),
        "user/_base.html": Template(Category.RECOMMENDED),
        "user/dashboard_groups.html": Template(Category.ESSENTIAL),
        "user/_edit_base.html": Template(Category.RECOMMENDED),
        "user/login.html": Template(Category.ESSENTIAL),
        "user/list.html": Template(Category.ESSENTIAL),
        "user/snippets/info.html": Template(Category.ESSENTIAL),
        "user/snippets/news_feed.html": Template(Category.ESSENTIAL),
        "user/snippets/api_token_create_form.html": Template(Category.ESSENTIAL),
        "user/snippets/api_tokens_revoke.html": Template(Category.ESSENTIAL),
        "user/snippets/api_token_list.html": Template(Category.ESSENTIAL),
        "datastore/dictionary.html": Template(Category.ESSENTIAL),
        "datastore/snippets/api_info.html": Template(Category.ESSENTIAL),
        "datastore/snippets/_dictionary_view.html": Template(Category.ESSENTIAL),
        "organization/bulk_process.html": Template(Category.ESSENTIAL),
        "organization/confirm_delete_member.html": Template(Category.ESSENTIAL),
        "organization/members.html": Template(Category.ESSENTIAL),
        "organization/confirm_delete.html": Template(Category.ESSENTIAL),
        "organization/admins.html": Template(Category.ESSENTIAL),
        "organization/edit.html": Template(Category.ESSENTIAL),
        "organization/new_organization_form.html": Template(Category.ESSENTIAL),
        "organization/index.html": Template(Category.ESSENTIAL),
        "organization/new.html": Template(Category.ESSENTIAL),
        "organization/about.html": Template(Category.ESSENTIAL),
        "organization/changes.html": Template(Category.ESSENTIAL),
        "organization/read.html": Template(Category.ESSENTIAL),
        "organization/member_new.html": Template(Category.ESSENTIAL),
        "organization/activity_stream.html": Template(Category.ESSENTIAL),
        "organization/_base.html": Template(Category.RECOMMENDED),
        "organization/manage_members.html": Template(Category.ESSENTIAL),
        "organization/_edit_base.html": Template(Category.RECOMMENDED),
        "organization/snippets/info.html": Template(Category.ESSENTIAL),
    }
)
