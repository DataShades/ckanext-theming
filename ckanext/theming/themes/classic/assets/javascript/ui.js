/// <reference path="../../../../../../types.d.ts" />
var __classPrivateFieldSet = (this && this.__classPrivateFieldSet) || function (receiver, state, value, kind, f) {
    if (kind === "m") throw new TypeError("Private method is not writable");
    if (kind === "a" && !f) throw new TypeError("Private accessor was defined without a setter");
    if (typeof state === "function" ? receiver !== state || !f : !state.has(receiver)) throw new TypeError("Cannot write private member to an object whose class did not declare it");
    return (kind === "a" ? f.call(receiver, value) : f ? f.value = value : state.set(receiver, value)), value;
};
var __classPrivateFieldGet = (this && this.__classPrivateFieldGet) || function (receiver, state, kind, f) {
    if (kind === "a" && !f) throw new TypeError("Private accessor was defined without a getter");
    if (typeof state === "function" ? receiver !== state || !f : !state.has(receiver)) throw new TypeError("Cannot read private member from an object whose class did not declare it");
    return kind === "m" ? f : kind === "a" ? f.call(receiver) : f ? f.value : state.get(receiver);
};
((ckan) => {
    var _Modal_modal, _Notification_alert, _Notification_sandbox, _Tooltip_tooltip, _Popover_popover;
    function applyAttrs(el, attrs) {
        Object.entries(attrs).forEach(([key, value]) => el.setAttribute(key, value));
    }
    function applyProps(el, props) {
        Object.entries(props).forEach(([key, value]) => (el[key] = value));
    }
    function applyListeners(el, listeners) {
        Object.entries(listeners).forEach(([key, value]) => {
            if (typeof value == "function") {
                el.addEventListener(key, value);
            }
            else {
                el.addEventListener(key, value.listener, value.options);
            }
        });
    }
    class Modal {
        constructor(el) {
            this.el = el;
            _Modal_modal.set(this, void 0);
            // @ts-ignore
            __classPrivateFieldSet(this, _Modal_modal, bootstrap.Modal.getOrCreateInstance(el), "f");
        }
        destroy() {
            __classPrivateFieldGet(this, _Modal_modal, "f").dispose();
        }
        show() {
            __classPrivateFieldGet(this, _Modal_modal, "f").show();
        }
        close() {
            __classPrivateFieldGet(this, _Modal_modal, "f").hide();
        }
        static create(content, params = {}) {
            const html = `
        <div class="modal fade" tabindex="-1" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header"></div>
              <div class="modal-body"></div>
              <div class="modal-footer"></div>
            </div>
          </div>
        </div>`;
            document.body.insertAdjacentHTML("beforeend", html);
            const modal = document.body.lastElementChild;
            if (params.title) {
                modal
                    .querySelector(".modal-header")
                    ?.insertAdjacentHTML("beforeend", `<h5 class="modal-title">${params.title}</h5>`);
            }
            if (params.dismissible) {
                modal
                    .querySelector(".modal-header")
                    ?.insertAdjacentHTML("beforeend", `<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>`);
            }
            modal.querySelector(".modal-body")?.append(content);
            const actions = params.actions || [];
            if (params.dismissLabel) {
                actions.unshift(ui.button(params.dismissLabel, {
                    props: { onclick: () => result.close() },
                    style: "secondary",
                }));
            }
            if (actions.length) {
                modal.querySelector(".modal-footer")?.append(...actions);
            }
            const result = new Modal(modal);
            return result;
        }
        static byId(id) {
            const el = document.getElementById(id);
            if (!el) {
                return null;
            }
            return new Modal(el);
        }
    }
    _Modal_modal = new WeakMap();
    class Notification {
        constructor(el) {
            this.el = el;
            _Notification_alert.set(this, void 0);
            _Notification_sandbox.set(this, void 0);
            __classPrivateFieldSet(this, _Notification_sandbox, ckan.sandbox(), "f");
            __classPrivateFieldSet(this, _Notification_alert, __classPrivateFieldGet(this, _Notification_sandbox, "f").notify.initialize(el), "f");
            __classPrivateFieldGet(this, _Notification_alert, "f").hide();
            __classPrivateFieldGet(this, _Notification_sandbox, "f").notify.el.append(__classPrivateFieldGet(this, _Notification_alert, "f"));
        }
        close() {
            __classPrivateFieldGet(this, _Notification_alert, "f").hide();
        }
        show() {
            __classPrivateFieldGet(this, _Notification_alert, "f").show();
        }
        destroy() {
            __classPrivateFieldGet(this, _Notification_alert, "f").remove();
        }
        static create(content, props = {}) {
            const notify = ckan.sandbox().notify;
            const el = notify.create(props.title &&
                (typeof props.title === "string"
                    ? props.title
                    : props.title.textContent), typeof content === "string" ? content : content.textContent, props.style || "default");
            return new Notification(el[0]);
        }
        static byId(id) {
            const el = document.getElementById(id);
            if (!el) {
                return null;
            }
            return new Notification(el);
        }
    }
    _Notification_alert = new WeakMap(), _Notification_sandbox = new WeakMap();
    class Tooltip {
        constructor(el) {
            this.el = el;
            _Tooltip_tooltip.set(this, void 0);
            // @ts-ignore
            __classPrivateFieldSet(this, _Tooltip_tooltip, bootstrap.Tooltip.getOrCreateInstance(el), "f");
        }
        close() {
            __classPrivateFieldGet(this, _Tooltip_tooltip, "f").hide();
        }
        show() {
            __classPrivateFieldGet(this, _Tooltip_tooltip, "f").show();
        }
        destroy() {
            __classPrivateFieldGet(this, _Tooltip_tooltip, "f").dispose();
        }
        static create(content, props = { target: document.body }) {
            if (typeof content !== "string") {
                throw "Only string tooltips are supported";
            }
            props.target.dataset.bsTitle = content;
            if (props.position) {
                props.target.dataset.bsPlacement = props.position;
            }
            return new Tooltip(props.target);
        }
        static byId(id) {
            const el = document.getElementById(id);
            if (!el) {
                return null;
            }
            return new Tooltip(el);
        }
    }
    _Tooltip_tooltip = new WeakMap();
    class Popover {
        constructor(el) {
            this.el = el;
            _Popover_popover.set(this, void 0);
            // @ts-ignore
            __classPrivateFieldSet(this, _Popover_popover, bootstrap.Popover.getOrCreateInstance(el), "f");
        }
        close() {
            __classPrivateFieldGet(this, _Popover_popover, "f").hide();
        }
        show() {
            __classPrivateFieldGet(this, _Popover_popover, "f").show();
        }
        destroy() {
            __classPrivateFieldGet(this, _Popover_popover, "f").dispose();
        }
        static create(content, props = { target: document.body }) {
            props.target.dataset.bsContent =
                typeof content === "string" ? content : content.textContent;
            props.target.dataset.bsHtml = "true";
            if (props.title) {
                props.target.dataset.bsTitle = props.title;
            }
            if (props.trigger) {
                props.target.dataset.bsTrigger = props.trigger;
            }
            return new Popover(props.target);
        }
        static byId(id) {
            const el = document.getElementById(id);
            if (!el) {
                return null;
            }
            return new Popover(el);
        }
    }
    _Popover_popover = new WeakMap();
    const ui = {
        button(content, params = {}) {
            const btn = document.createElement("button");
            btn.append(content);
            btn.classList.add("btn", `btn-${params.style ?? "primary"}`);
            if (params.type) {
                btn.type = params.type;
            }
            if (params.attrs) {
                applyAttrs(btn, params.attrs);
            }
            if (params.props) {
                applyProps(btn, params.props);
            }
            if (params.on) {
                applyListeners(btn, params.on);
            }
            [];
            return btn;
        },
        modal: Modal.create,
        getModal: Modal.byId,
        notification: Notification.create,
        getNotification: Notification.byId,
        tooltip: Tooltip.create,
        getTooltip: Tooltip.byId,
        popover: Popover.create,
        getPopover: Popover.byId,
    };
    ckan.sandbox.setup((sb) => {
        sb.ui = sb.ui || {};
        Object.assign(sb.ui, ui);
    });
})(window.ckan);
