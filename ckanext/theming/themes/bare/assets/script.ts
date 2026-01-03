/// <reference path="../types.d.ts" />

((ckan) => {
  const asNode = (value: any) =>
    value instanceof Node ? value : new Text(value);

  const util = {
    applyAttrs(el: HTMLElement, attrs: { [key: string]: string }) {
      Object.entries(attrs).forEach(([key, value]) =>
        el.setAttribute(key, value),
                                   );
    },

    applyProps(el: HTMLElement, props: { [key: string]: any }) {
      Object.entries(props).forEach(
        ([key, value]) => ((el as any)[key] = value),
      );
    },

    applyListeners(
      el: HTMLElement,
      listeners: { [key: string]: Theming.Listener | Theming.ComplexListener },
    ) {
      Object.entries(listeners).forEach(([key, value]) => {
        if (typeof value == "function") {
          el.addEventListener(key, value);
        } else {
          el.addEventListener(key, value.listener, value.options);
        }
      });
    },

    animateTimeout(el: HTMLProgressElement, start: number, timeout: number) {
      const diff = Number(new Date()) - start;
      el.value = timeout - diff;
      if (el.value > 0) {
        requestAnimationFrame(() => util.animateTimeout(el, start, timeout));
      }
    },
  };

  class Modal implements IModal<HTMLDialogElement> {
    constructor(public el: HTMLDialogElement) {}

    destroy() {
      this.el.remove();
    }

    show() {
      document.body.appendChild(this.el);
      this.el.showModal();
    }

    close() {
      this.el.close();
    }
  }

  class Notification implements INotification {
    constructor(public el: HTMLElement) {}
    close() {
      this.el.hidden = true;
    }
    show() {
      this.el.hidden = false;
    }
    destroy() {
      this.el.remove();
    }
  }

  class Tooltip implements ITooltip {
    constructor(public el: HTMLElement) {}
    close() {
      this.el.hidden = true;
    }
    show() {
      this.el.hidden = false;
    }
    destroy() {
      this.el.remove();
    }
  }
  class Popover implements IPopover {
    constructor(public el: HTMLElement) {}
    close() {
      this.el.hidePopover();
    }
    show() {
      document.body.appendChild(this.el);
      this.el.showPopover();
    }
    destroy() {
      this.el.remove();
    }
  }

  const ui: IUi = {
    button(content: any, params = {}) {
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

    modal(content, title: any, actions = [], params = {}) {
      const modal = document.createElement("dialog");

      modal.addEventListener("close", () => result.destroy());

      if (params.dismissible) {
        // does not work in safari
        (modal as any).closedBy = "any";
      }

      if (title) {
        modal.appendChild(document.createElement("h2")).append(title);
      }

      modal.appendChild(document.createElement("div")).append(content);

      if (params.dismissLabel) {
        actions.unshift(
          ui.button(params.dismissLabel, {
            props: { onclick: () => result.close() },
          }),
        );
      }

      if (actions.length) {
        modal.appendChild(document.createElement("div")).append(...actions);
      }

      const result = new Modal(modal);

      return result;
    },

    getModal(id) {
      const el = document.getElementById(id);
      if (!el) {
        return null;
      }
      return new Modal(<HTMLDialogElement>el);
    },

    notification(content, title, props = {}) {
      const containerId = "flash-messages";
      const container = document.getElementById(containerId);
      if (!container) {
        throw `Notification container(${containerId}) is not defined`;
      }

      const el = document.createElement("div");
      el.hidden = true;
      if (title) {
        el.appendChild(document.createElement("strong")).append(title);
      }
      el.appendChild(document.createElement("p")).append(content);

      if (props.dismissible) {
        el.appendChild(
          ui.button("x", { props: { onclick: () => el.remove() } }),
        );
      }

      if (props.timeout) {
        const progress = el.appendChild(document.createElement("progress"));
        progress.max = props.timeout;
        progress.value = props.timeout;
        const start = Number(new Date());

        setTimeout(() => el.remove(), props.timeout);
        util.animateTimeout(progress, start, props.timeout);
      }

      container.append(el);
      const result = new Notification(el);
      return result;
    },

    getNotification(id) {
      const el = document.getElementById(id);
      if (!el) {
        return null;
      }
      return new Notification(el);
    },

    tooltip(content, target, props = {}) {
      if (typeof content !== "string") {
        throw "Only string tooltips are supported";
      }
      target.dataset.tooltip = content;
      target.dataset.tooltipPosition = props.position || "bottom";
      return new Tooltip(target);
    },

    getTooltip(id) {
      const el = document.getElementById(id);
      if (!el) {
        return null;
      }
      return new Tooltip(el);
    },
    popover(content, props = {}) {
      const el = document.createElement("div");
      el.popover = "auto";
      el.append(content);
      return new Popover(el);
    },

    getPopover(id) {
      const el = document.getElementById(id);
      if (!el) {
        return null;
      }
      return new Popover(el);
    },
  };

  ckan.sandbox.setup((sb) => {
    sb.ui = sb.ui || {};
    sb.ui.util = sb.ui.util || {};
    Object.assign(sb.ui, ui);
    Object.assign(sb.ui.util, util);
  });
})(window.ckan);
