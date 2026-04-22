"""Reference definitions for components used in the system."""

from __future__ import annotations

import dataclasses
import enum
import fnmatch
from collections import defaultdict
from collections.abc import Mapping
from typing import Any


class Category(enum.Enum):
    ESSENTIAL = enum.auto()
    RECOMMENDED = enum.auto()
    CUSTOM = enum.auto()


@dataclasses.dataclass(frozen=True)
class Component:
    category: Category = dataclasses.field(default=Category.CUSTOM)


@dataclasses.dataclass(frozen=True)
class Template:
    category: Category = dataclasses.field(default=Category.CUSTOM)


def _true():
    return True


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

components.update(
    {
        # wrappers ############################################################
        "accordion_wrapper": Component(Category.ESSENTIAL),
        "account_nav_wrapper": Component(Category.RECOMMENDED),
        "activity_list": Component(Category.RECOMMENDED),
        "breadcrumb_wrapper": Component(Category.RECOMMENDED),
        "content_action_wrapper": Component(Category.RECOMMENDED),
        "content_nav_wrapper": Component(Category.RECOMMENDED),
        "facet_list": Component(Category.ESSENTIAL),
        "group_list": Component(Category.ESSENTIAL),
        "main_nav_wrapper": Component(Category.RECOMMENDED),
        "sidebar_nav_wrapper": Component(Category.RECOMMENDED),
        "menu_wrapper": Component(Category.ESSENTIAL),
        "nav_wrapper": Component(Category.ESSENTIAL),
        "organization_list": Component(Category.ESSENTIAL),
        "package_list": Component(Category.ESSENTIAL),
        "page_action_wrapper": Component(Category.RECOMMENDED),
        "panel_wrapper": Component(Category.RECOMMENDED),
        "pagination_wrapper": Component(Category.ESSENTIAL),
        "resource_list": Component(Category.ESSENTIAL),
        "tab_nav_wrapper": Component(Category.RECOMMENDED),
        "user_list": Component(Category.ESSENTIAL),
        # content #############################################################
        "activity": Component(Category.ESSENTIAL),
        "facet": Component(Category.ESSENTIAL),
        "license": Component(Category.ESSENTIAL),
        "group": Component(Category.ESSENTIAL),
        "organization": Component(Category.ESSENTIAL),
        "package": Component(Category.ESSENTIAL),
        "resource": Component(Category.ESSENTIAL),
        "user": Component(Category.ESSENTIAL),
        # containers ##########################################################
        "accordion": Component(Category.ESSENTIAL),
        "button_group": Component(Category.ESSENTIAL),
        "card": Component(Category.RECOMMENDED),
        "column": Component(Category.RECOMMENDED),
        "container": Component(Category.RECOMMENDED),
        "dropdown": Component(Category.ESSENTIAL),
        "grid": Component(Category.RECOMMENDED),
        "row": Component(Category.RECOMMENDED),
        "list": Component(Category.ESSENTIAL),
        "list_item": Component(Category.ESSENTIAL),
        "panel": Component(Category.RECOMMENDED),
        # sections ############################################################
        "facet_section": Component(Category.ESSENTIAL),
        "section": Component(Category.ESSENTIAL),
        "sidebar_section": Component(Category.ESSENTIAL),
        # feedback ############################################################
        "alert": Component(Category.ESSENTIAL),
        "confirm_modal": Component(Category.RECOMMENDED),
        "modal": Component(Category.ESSENTIAL),
        "popover": Component(Category.RECOMMENDED),
        "progress": Component(Category.RECOMMENDED),
        "spinner": Component(Category.RECOMMENDED),
        "toast": Component(Category.RECOMMENDED),
        "tooltip": Component(Category.ESSENTIAL),
        # elements ############################################################
        "avatar": Component(Category.ESSENTIAL),
        "badge": Component(Category.RECOMMENDED),
        "breadcrumb_divider": Component(Category.RECOMMENDED),
        "button": Component(Category.ESSENTIAL),
        "datetime": Component(Category.ESSENTIAL),
        "divider": Component(Category.RECOMMENDED),
        "empty": Component(Category.ESSENTIAL),
        "heading": Component(Category.ESSENTIAL),
        "icon": Component(Category.ESSENTIAL),
        "image": Component(Category.ESSENTIAL),
        "link": Component(Category.ESSENTIAL),
        "tag": Component(Category.ESSENTIAL),
        "text": Component(Category.ESSENTIAL),
        "video": Component(Category.RECOMMENDED),
        # data ################################################################
        "chart": Component(Category.RECOMMENDED),
        "code": Component(Category.RECOMMENDED),
        "definition_list": Component(Category.RECOMMENDED),
        "table": Component(Category.ESSENTIAL),
        "table_body": Component(Category.RECOMMENDED),
        "table_cell": Component(Category.RECOMMENDED),
        "table_head": Component(Category.RECOMMENDED),
        "table_row": Component(Category.RECOMMENDED),
        # form ################################################################
        "checkbox": Component(Category.ESSENTIAL),
        "extra_field": Component(Category.RECOMMENDED),
        "extra_fields_collection": Component(Category.RECOMMENDED),
        "field_errors": Component(Category.RECOMMENDED),
        "fieldset": Component(Category.RECOMMENDED),
        "file_input": Component(Category.ESSENTIAL),
        "form": Component(Category.ESSENTIAL),
        "form_annotation": Component(Category.ESSENTIAL),
        "field_info": Component(Category.ESSENTIAL),
        "form_actions": Component(Category.ESSENTIAL),
        "form_end": Component(Category.RECOMMENDED),
        "form_errors": Component(Category.ESSENTIAL),
        "form_start": Component(Category.RECOMMENDED),
        "hidden_input": Component(Category.ESSENTIAL),
        "input": Component(Category.ESSENTIAL),
        "markdown": Component(Category.ESSENTIAL),
        "markdown_popover": Component(Category.RECOMMENDED),
        "radio": Component(Category.ESSENTIAL),
        "range_input": Component(Category.RECOMMENDED),
        "select": Component(Category.ESSENTIAL),
        "select_box": Component(Category.ESSENTIAL),
        "select_option": Component(Category.ESSENTIAL),
        "submit": Component(Category.ESSENTIAL),
        "textarea": Component(Category.ESSENTIAL),
        # handles #############################################################
        "modal_close_handle": Component(Category.RECOMMENDED),
        "modal_handle": Component(Category.ESSENTIAL),
        "panel_handle": Component(Category.RECOMMENDED),
        "popover_handle": Component(Category.RECOMMENDED),
        # meta ################################################################
        "account": Component(Category.RECOMMENDED),
        "header": Component(Category.RECOMMENDED),
        "header_logo": Component(Category.RECOMMENDED),
        "footer": Component(Category.RECOMMENDED),
        "footer_main": Component(Category.RECOMMENDED),
        "footer_secondary": Component(Category.RECOMMENDED),
        "subtitle_item": Component(Category.ESSENTIAL),
        # navigation ##########################################################
        "breadcrumb": Component(Category.ESSENTIAL),
        "nav_item": Component(Category.ESSENTIAL),
        "main_nav_item": Component(Category.ESSENTIAL),
        "sidebar_nav_item": Component(Category.RECOMMENDED),
        "account_nav_item": Component(Category.ESSENTIAL),
        "content_nav_item": Component(Category.ESSENTIAL),
        "page_action": Component(Category.ESSENTIAL),
        "content_action": Component(Category.ESSENTIAL),
        "tab_handle": Component(Category.RECOMMENDED),
        "menu_item": Component(Category.ESSENTIAL),
        "pagination": Component(Category.ESSENTIAL),
        "pagination_item": Component(Category.ESSENTIAL),
        "dropdown_item": Component(Category.ESSENTIAL),
        # search ##############################################################
        "search_active_filters": Component(Category.RECOMMENDED),
        "search_advanced_controls": Component(Category.RECOMMENDED),
        "search_form": Component(Category.ESSENTIAL),
        "search_form_box": Component(Category.RECOMMENDED),
        "search_input": Component(Category.RECOMMENDED),
        "search_pagination_info": Component(Category.RECOMMENDED),
        "search_results_header": Component(Category.RECOMMENDED),
        "search_sort_control": Component(Category.RECOMMENDED),
        "search_submit_button": Component(Category.RECOMMENDED),
    }
)


templates: dict[str, Template] = defaultdict(Template)
templates.update(
    {
        "_footer.html": Template(Category.RECOMMENDED),
        "_page.html": Template(Category.RECOMMENDED),
        "error_document_template.html": Template(Category.ESSENTIAL),
        "_header.html": Template(Category.RECOMMENDED),
        "_base.html": Template(Category.RECOMMENDED),
        "_layout.html": Template(Category.RECOMMENDED),
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
        "layout/content_control.html": Template(Category.RECOMMENDED),
        "layout/default.html": Template(Category.RECOMMENDED),
        "layout/content_context.html": Template(Category.RECOMMENDED),
        "layout/content_focus.html": Template(Category.RECOMMENDED),
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
