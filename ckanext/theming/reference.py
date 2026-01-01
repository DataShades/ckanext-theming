"""Reference definitions for components used in the system."""

from __future__ import annotations

import dataclasses
import enum
from collections import defaultdict
from collections.abc import Callable
from typing import Any

import ckan.plugins.toolkit as tk


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


@dataclasses.dataclass(frozen=True)
class Route:
    plugin: str | None = None
    endpoint: str | None = None
    check_availability: Callable[[], bool] = _true
    view_args: set[str] = dataclasses.field(default_factory=set)
    authenticated: bool = True

    def make_params(self, endpoint: str, data: dict[str, Any]):  # noqa: C901
        params: dict[str, Any] = {}
        if "resource_id" in self.view_args:
            params["resource_id"] = data["resource"]["id"]

        if "user_id" in self.view_args:
            params["user_id"] = data["user"]["id"]

        if "view_id" in self.view_args:
            params["view_id"] = data["resource_view"]["id"]

        if "id" in self.view_args:
            if endpoint.startswith(("dataset", "resource", "datastore")):
                params["id"] = data["package"]["name"]

            elif endpoint.startswith("group"):
                params["id"] = data["group"]["name"]

            elif endpoint.startswith("organization"):
                params["id"] = data["organization"]["name"]

            elif endpoint.startswith("user"):
                params["id"] = data["user"]["name"]

            elif endpoint.endswith(("user_activity", "user_changes")):
                params["id"] = data["user"]["id"]

            elif endpoint.endswith(("group_activity", "group_changes")):
                params["id"] = data["group"]["id"]

            elif endpoint.endswith(("package_activity", "package_changes")):
                params["id"] = data["package"]["id"]

            elif endpoint.endswith(("organization_activity", "organization_changes")):
                params["id"] = data["organization"]["id"]

        return params


components: dict[str, Component] = defaultdict(Component)

components.update(
    {
        # wrappers ############################################################
        "accordion_wrapper": Component(Category.ESSENTIAL),
        "account_nav_wrapper": Component(Category.RECOMMENDED),
        "activity_wrapper": Component(Category.RECOMMENDED),
        "breadcrumb_wrapper": Component(Category.RECOMMENDED),
        "content_action_wrapper": Component(Category.RECOMMENDED),
        "content_nav_wrapper": Component(Category.RECOMMENDED),
        "dropdown_wrapper": Component(Category.ESSENTIAL),
        "facet_wrapper": Component(Category.ESSENTIAL),
        "group_wrapper": Component(Category.ESSENTIAL),
        "main_nav_wrapper": Component(Category.RECOMMENDED),
        "menu_wrapper": Component(Category.ESSENTIAL),
        "nav_wrapper": Component(Category.ESSENTIAL),
        "organization_wrapper": Component(Category.ESSENTIAL),
        "package_wrapper": Component(Category.ESSENTIAL),
        "page_action_wrapper": Component(Category.RECOMMENDED),
        "panel_wrapper": Component(Category.ESSENTIAL),
        "resource_wrapper": Component(Category.ESSENTIAL),
        "tab_wrapper": Component(Category.ESSENTIAL),
        "user_wrapper": Component(Category.ESSENTIAL),
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
        "card": Component(Category.ESSENTIAL),
        "column": Component(Category.ESSENTIAL),
        "container": Component(Category.ESSENTIAL),
        "grid": Component(Category.ESSENTIAL),
        "list": Component(Category.ESSENTIAL),
        "list_item": Component(Category.ESSENTIAL),
        "panel": Component(Category.ESSENTIAL),
        # sections ############################################################
        "facet_section": Component(Category.ESSENTIAL),
        "section": Component(Category.ESSENTIAL),
        "sidebar_section": Component(Category.ESSENTIAL),
        # feedback ############################################################
        "alert": Component(Category.ESSENTIAL),
        "confirm_modal": Component(Category.RECOMMENDED),
        "modal": Component(Category.ESSENTIAL),
        "popover": Component(Category.ESSENTIAL),
        "progress": Component(Category.ESSENTIAL),
        "spinner": Component(Category.ESSENTIAL),
        "toast": Component(Category.ESSENTIAL),
        "tooltip": Component(Category.ESSENTIAL),
        # elements ############################################################
        "avatar": Component(Category.ESSENTIAL),
        "badge": Component(Category.ESSENTIAL),
        "breadcrumb_divider": Component(Category.RECOMMENDED),
        "button": Component(Category.ESSENTIAL),
        "datetime": Component(Category.ESSENTIAL),
        "divider": Component(Category.ESSENTIAL),
        "heading": Component(Category.ESSENTIAL),
        "icon": Component(Category.ESSENTIAL),
        "image": Component(Category.ESSENTIAL),
        "link": Component(Category.ESSENTIAL),
        "tag": Component(Category.ESSENTIAL),
        "text": Component(Category.ESSENTIAL),
        "video": Component(Category.ESSENTIAL),
        # data ################################################################
        "chart": Component(Category.RECOMMENDED),
        "code": Component(Category.ESSENTIAL),
        "definition_list": Component(Category.ESSENTIAL),
        "table": Component(Category.ESSENTIAL),
        "table_body": Component(Category.ESSENTIAL),
        "table_cell": Component(Category.ESSENTIAL),
        "table_head": Component(Category.ESSENTIAL),
        "table_row": Component(Category.ESSENTIAL),
        # form ################################################################
        "autocomplete": Component(Category.ESSENTIAL),
        "checkbox": Component(Category.ESSENTIAL),
        "extra_field": Component(Category.ESSENTIAL),
        "extra_field_multiplicator": Component(Category.ESSENTIAL),
        "extra_fields_collection": Component(Category.ESSENTIAL),
        "field_errors": Component(Category.ESSENTIAL),
        "file_input": Component(Category.ESSENTIAL),
        "form": Component(Category.ESSENTIAL),
        "form_actions": Component(Category.ESSENTIAL),
        "form_end": Component(Category.ESSENTIAL),
        "form_errors": Component(Category.ESSENTIAL),
        "form_start": Component(Category.ESSENTIAL),
        "hidden_input": Component(Category.ESSENTIAL),
        "input": Component(Category.ESSENTIAL),
        "markdown": Component(Category.ESSENTIAL),
        "radio": Component(Category.ESSENTIAL),
        "range_input": Component(Category.ESSENTIAL),
        "select": Component(Category.ESSENTIAL),
        "select_box": Component(Category.ESSENTIAL),
        "select_option": Component(Category.ESSENTIAL),
        "submit": Component(Category.ESSENTIAL),
        "textarea": Component(Category.ESSENTIAL),
        # handles #############################################################
        "modal_close_handle": Component(Category.RECOMMENDED),
        "modal_handle": Component(Category.ESSENTIAL),
        "panel_handle": Component(Category.ESSENTIAL),
        "popover_handle": Component(Category.ESSENTIAL),
        # meta ################################################################
        "account": Component(Category.RECOMMENDED),
        "header": Component(Category.RECOMMENDED),
        "footer": Component(Category.RECOMMENDED),
        "subtitle_item": Component(Category.ESSENTIAL),
        # navigation ##########################################################
        "breadcrumb": Component(Category.ESSENTIAL),
        "nav_item": Component(Category.ESSENTIAL),
        "main_nav_item": Component(Category.ESSENTIAL),
        "account_nav_item": Component(Category.ESSENTIAL),
        "content_nav_item": Component(Category.ESSENTIAL),
        "page_action": Component(Category.ESSENTIAL),
        "content_action": Component(Category.ESSENTIAL),
        "tab_handle": Component(Category.ESSENTIAL),
        "menu_item": Component(Category.ESSENTIAL),
        "pagination": Component(Category.ESSENTIAL),
        "dropdown_item": Component(Category.ESSENTIAL),
        # search ##############################################################
        "search_active_filters": Component(Category.ESSENTIAL),
        "search_advanced_controls": Component(Category.RECOMMENDED),
        "search_form": Component(Category.ESSENTIAL),
        "search_input": Component(Category.ESSENTIAL),
        "search_pagination_info": Component(Category.ESSENTIAL),
        "search_results_header": Component(Category.ESSENTIAL),
        "search_sort_control": Component(Category.ESSENTIAL),
        "search_submit_button": Component(Category.ESSENTIAL),
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


routes: dict[str, Route] = defaultdict(Route)
routes.update(
    {
        "activity.dashboard": Route(plugin="activity"),
        "activity.dashboard_testing": Route(plugin="activity"),
        "activity.group_activity": Route(plugin="activity", view_args={"id"}),
        "activity.group_changes": Route(plugin="activity", view_args={"id"}),
        "activity.organization_activity": Route(plugin="activity", view_args={"id"}),
        "activity.organization_changes": Route(plugin="activity", view_args={"id"}),
        "activity.package_activity": Route(plugin="activity", view_args={"id"}),
        "activity.package_changes": Route(plugin="activity", view_args={"id"}),
        "activity.user_activity": Route(plugin="activity", view_args={"id"}),
        "admin.config": Route(),
        "admin.index": Route(),
        "admin.reset_config": Route(),
        "admin.trash": Route(),
        "dashboard.datasets": Route(),
        "dashboard.groups": Route(),
        "dashboard.organizations": Route(),
        "dataset.collaborator_delete": Route(
            check_availability=lambda: tk.config["ckan.auth.allow_dataset_collaborators"],
            view_args={"id", "user_id"},
        ),
        "dataset.collaborators_read": Route(
            check_availability=lambda: tk.config["ckan.auth.allow_dataset_collaborators"],
            view_args={"id", "user_id"},
        ),
        "dataset.delete": Route(view_args={"id"}),
        "dataset.edit": Route(view_args={"id"}),
        "dataset.followers": Route(view_args={"id"}),
        "dataset.groups": Route(view_args={"id"}),
        "dataset.new": Route(),
        "dataset.new_collaborator": Route(
            check_availability=lambda: tk.config["ckan.auth.allow_dataset_collaborators"],
            view_args={"id"},
        ),
        "dataset.read": Route(view_args={"id"}),
        "dataset.resources": Route(view_args={"id"}),
        "dataset.search": Route(),
        "datastore.api_info": Route(plugin="datastore", view_args={"resource_id"}),
        "datastore.dictionary": Route(plugin="datastore", view_args={"id", "resource_id"}),
        "group.about": Route(view_args={"id"}),
        "group.admins": Route(view_args={"id"}),
        "group.delete": Route(view_args={"id"}),
        "group.edit": Route(view_args={"id"}),
        "group.followers": Route(view_args={"id"}),
        "group.index": Route(),
        "group.manage_members": Route(view_args={"id"}),
        "group.member_new": Route(view_args={"id"}),
        "group.members": Route(view_args={"id"}),
        "group.new": Route(),
        "group.read": Route(view_args={"id"}),
        "organization.about": Route(view_args={"id"}),
        "organization.admins": Route(view_args={"id"}),
        "organization.bulk_process": Route(view_args={"id"}),
        "organization.delete": Route(view_args={"id"}),
        "organization.edit": Route(view_args={"id"}),
        "organization.followers": Route(view_args={"id"}),
        "organization.index": Route(),
        "organization.manage_members": Route(view_args={"id"}),
        "organization.member_new": Route(view_args={"id"}),
        "organization.members": Route(view_args={"id"}),
        "organization.new": Route(),
        "organization.read": Route(view_args={"id"}),
        "home.index": Route(),
        "home.about": Route(),
        "resource.delete": Route(view_args={"id", "resource_id"}),
        "resource.edit": Route(view_args={"id", "resource_id"}),
        "resource.edit_view": Route(view_args={"id", "resource_id"}),
        "resource.edit_view:view_selected": Route(
            endpoint="resource.edit_view", view_args={"id", "resource_id", "view_id"}
        ),
        "resource.new": Route(view_args={"id"}),
        "resource.read": Route(view_args={"id", "resource_id"}),
        "resource.view": Route(view_args={"id", "resource_id"}),
        "resource.view:view_selected": Route(endpoint="resource.view", view_args={"id", "resource_id", "view_id"}),
        "resource.views": Route(view_args={"id", "resource_id"}),
        "stats.index": Route(plugin="stats"),
        "user.api_tokens": Route(view_args={"id"}),
        "user.delete": Route(view_args={"id"}),
        "user.edit": Route(view_args={"id"}),
        "user.followers": Route(view_args={"id"}),
        "user.index": Route(),
        "user.logged_out_page": Route(authenticated=False),
        "user.login": Route(authenticated=False),
        "user.login:authenticated": Route(endpoint="user.login"),
        "user.perform_reset": Route(view_args={"id"}, authenticated=False),
        "user.read": Route(view_args={"id"}),
        "user.read_groups": Route(view_args={"id"}),
        "user.read_organizations": Route(view_args={"id"}),
        "user.register": Route(authenticated=False),
        "user.request_reset": Route(authenticated=False),
        "util.primer": Route(),
    }
)
