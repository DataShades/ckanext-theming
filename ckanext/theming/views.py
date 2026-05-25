from __future__ import annotations

import os

from flask import Blueprint, current_app

import ckan.plugins.toolkit as tk

from ckanext.theming import reference

bp = Blueprint("theming", __name__, url_prefix="/theming")

__all__ = ["bp"]


@bp.route("/")
def index():
    return tk.redirect_to("theming.component")


@bp.route("/component")
@bp.route("/component/<component>")
def component(component: str | None = None):
    templates = sorted(current_app.jinja_env.list_templates(filter_func=lambda s: s.startswith("theming/components/")))
    available_components = [name for tpl in templates if (name := os.path.splitext(os.path.basename(tpl))[0])]

    if component and component not in available_components:
        return tk.abort(404, tk._("Component not found"))

    if not component and available_components:
        component = available_components[0]

    extra_vars = {
        "component": component,
        "available_components": available_components,
        "ref": reference.components,
    }
    return tk.render("theming/component.html", extra_vars)


# account
# account_nav_item
# account_nav_wrapper
# activity
# activity_list
# alert
# avatar
# badge
# breadcrumb
# breadcrumb_divider
# breadcrumb_wrapper
# button
# button_group
# card
# chart
# checkbox
# code
# column
# confirm_modal
# container
# content_action
# content_action_wrapper
# content_nav_item
# content_nav_wrapper
# datetime
# definition_list
# divider
# dropdown
# dropdown_item
# empty
# extra_field
# extra_fields_collection
# facet
# facet_list
# facet_section
# field_errors
# field_info
# fieldset
# file_input
# footer
# footer_main
# footer_secondary
# form
# form_actions
# form_annotation
# form_end
# form_errors
# form_start
# grid
# group
# group_list
# header
# header_logo
# heading
# hidden_input
# icon
# image
# input
# license
# link
# list
# list_item
# main_nav_item
# main_nav_wrapper
# markdown
# markdown_popover
# modal
# modal_close_handle
# modal_handle
# nav_item
# nav_wrapper
# organization
# organization_list
# package
# package_list
# page_action
# page_action_wrapper
# pagination
# pagination_item
# pagination_wrapper
# popover
# popover_handle
# progress
# radio
# range_input
# resource
# resource_list
# row
# search_active_filters
# search_advanced_controls
# search_form
# search_form_box
# search_input
# search_results_text
# search_sort_control
# search_submit_button
# section
# select
# select_box
# select_option
# sidebar_nav_item
# sidebar_nav_wrapper
# sidebar_section
# spinner
# submit
# subtitle_item
# tab
# tab_wrapper
# table
# table_body
# table_cell
# table_head
# table_row
# tag
# textarea
# toast
# tooltip
# user
# user_list
# video
# #
