/// <reference path="../../../../../types.d.ts" />
/// <reference types="bootstrap"/>
((ckan) => {
    const asNode = (value) => value instanceof Node ? value : new Text(value);
    const util = {
        applyAttrs(el, attrs) {
            Object.entries(attrs).forEach(([key, value]) => el.setAttribute(key, value));
        },
        applyProps(el, props) {
            Object.entries(props).forEach(([key, value]) => (el[key] = value));
        },
        applyListeners(el, listeners) {
            Object.entries(listeners).forEach(([key, value]) => {
                if (typeof value == "function") {
                    el.addEventListener(key, value);
                }
                else {
                    el.addEventListener(key, value.listener, value.options);
                }
            });
        },
        animateTimeout(el, start, timeout) {
            const diff = Number(new Date()) - start;
            el.value = timeout - diff;
            if (el.value > 0) {
                requestAnimationFrame(() => util.animateTimeout(el, start, timeout));
            }
        },
    };
    const ui = {
        button(content, params = {}) {
            const btn = document.createElement("button");
            btn.append(content);
            if (params.type) {
                btn.type = params.type;
            }
            if (params.attrs) {
                util.applyAttrs(btn, params.attrs);
            }
            if (params.props) {
                util.applyProps(btn, params.props);
            }
            if (params.on) {
                util.applyListeners(btn, params.on);
            }
            [];
            return btn;
        },
        modal(content, title, actions = [], params = {}) {
            const modal = document.createElement("dialog");
            modal.addEventListener("close", () => result.el.remove());
            if (params.dismissible) {
                // does not work in safari
                modal.closedBy = "any";
            }
            if (title) {
                modal.appendChild(document.createElement("h2")).append(title);
            }
            modal.appendChild(document.createElement("div")).append(content);
            if (params.dismissLabel) {
                actions.unshift(ui.button(params.dismissLabel, {
                    props: { onclick: () => result.close() },
                }));
            }
            if (actions.length) {
                modal.appendChild(document.createElement("div")).append(...actions);
            }
            const result = {
                el: modal,
                show() {
                    document.body.appendChild(this.el);
                    this.el.showModal();
                },
                close() {
                    this.el.close();
                },
            };
            return result;
        },
        notification(content, title, props = {}) {
            const containerId = "flash-messages";
            const container = document.getElementById(containerId);
            if (!container) {
                throw `Notification container(${containerId}) is not defined`;
            }
            const el = document.createElement("div");
            el.classList.add("toast", "fade");
            if (title) {
                const header = el.appendChild(document.createElement("strong"));
                header.classList.add("toast-header");
                const text = header.appendChild(document.createElement("strong"));
                text.classList.add("me-auto");
                text.append(title);
                if (props.dismissible) {
                    header.appendChild(ui.button("", {
                        attrs: {
                            class: "btn-close",
                            "data-bs-dismiss": "toast",
                            "aria-label": "Close",
                        },
                    }));
                }
            }
            const body = el.appendChild(document.createElement("div"));
            body.append(content);
            body.classList.add("toast-body");
            if (props.timeout) {
                el.setAttribute("data-bs-delay", String(props.timeout));
            }
            else {
                el.setAttribute("data-bs-autohide", "false");
            }
            container.append(el);
            const toast = bootstrap.Toast.getOrCreateInstance(el);
            const result = {
                el,
                show() {
                    toast.show();
                },
                hide() {
                    toast.hide();
                },
                destroy() {
                    el.remove();
                },
            };
            return result;
        },
    };
    ckan.sandbox.setup((sb) => {
        sb.ui = sb.ui || {};
        sb.ui.util = sb.ui.util || {};
        Object.assign(sb.ui, ui);
        Object.assign(sb.ui.util, util);
    });
})(window.ckan);
