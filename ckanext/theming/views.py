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
@bp.route("/component/<component>", methods=["GET", "POST"])  # handle confirm_modal example
def component(component: str | None = None):
    templates = current_app.jinja_env.list_templates(
        filter_func=lambda s: s.startswith(("theming/components/", f"theming/examples/{component}/"))
    )

    available_components: list[str] = []
    examples: list[str] = []

    for tpl in templates:
        parts = tpl.split("/")
        if parts[1] == "components":
            available_components.append(os.path.splitext(parts[2])[0])
        elif parts[1] == "examples" and parts[2] == component:
            examples.append(os.path.splitext(parts[3])[0])

    if component and component not in available_components:
        return tk.abort(404, tk._("Component not found"))

    if not component and available_components:
        component = available_components[0]

    extra_vars = {
        "component": component,
        "available_components": available_components,
        "examples": examples,
        "ref": reference.components,
    }
    if component == "list":
        extra_vars["resources"] = tk.get_action("resource_search")({}, {"limit": 2, "query": "url:"})["results"]
        extra_vars["packages"] = tk.get_action("package_search")({}, {"rows": 2})["results"]
        extra_vars["users"] = tk.get_action("user_list")({}, {"limit": 2})[:2]
        extra_vars["organizations"] = tk.get_action("organization_list")({}, {"limit": 2, "all_fields": True})
        extra_vars["groups"] = tk.get_action("group_list")({}, {"limit": 2, "all_fields": True})

    return tk.render("theming/component.html", extra_vars)


# account
# activity
# activity_list
# avatar
# card
# chart
# code
# column
# container
# definition_list
# dropdown
# dropdown_item
# empty
# extra_field
# extra_fields_collection
# footer
# footer_main
# footer_secondary
# grid
# header
# header_logo
# license
# markdown_popover
# popover
# popover_handle
# progress
# row
# search_active_filters
# search_advanced_controls
# search_form
# search_form_box
# search_input
# search_results_text
# search_sort_control
# search_submit_button
# spinner
# submit
# subtitle_item
# toast
# tooltip
