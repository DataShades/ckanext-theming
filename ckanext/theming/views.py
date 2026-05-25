from __future__ import annotations

import os

from flask import Blueprint, current_app

import ckan.plugins.toolkit as tk

bp = Blueprint("theming", __name__, url_prefix="/theming")

__all__ = ["bp"]


@bp.route("/")
def index():
    return tk.redirect_to("theming.component")


@bp.route("/component")
@bp.route("/component/<component>")
def component(component: str | None = None):
    templates = sorted(current_app.jinja_env.list_templates(filter_func=lambda s: s.startswith("theming/components/")))
    available_components = [os.path.splitext(os.path.basename(tpl))[0] for tpl in templates]

    if component and component not in available_components:
        return tk.abort(404, tk._("Component not found"))

    if not component and available_components:
        component = available_components[0]

    extra_vars = {"component": component, "available_components": available_components}
    return tk.render("theming/component.html", extra_vars)
