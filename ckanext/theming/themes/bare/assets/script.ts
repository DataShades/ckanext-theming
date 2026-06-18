/// <reference path="../../../../../types.d.ts" />

((ckan) => {
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

  function positionPopover(popoverEl: HTMLElement, targetEl: HTMLElement) {
    const targetRect = targetEl.getBoundingClientRect();
    const popoverRect = popoverEl.getBoundingClientRect();

    let top = targetRect.bottom + 8; // 8px margin
    let left = targetRect.left + (targetRect.width - popoverRect.width) / 2;

    const viewportWidth = window.innerWidth;
    const viewportHeight = window.innerHeight;

    if (left < 10) {
      left = 10;
    } else if (left + popoverRect.width > viewportWidth - 10) {
      left = viewportWidth - popoverRect.width - 10;
    }

    if (top + popoverRect.height > viewportHeight - 10) {
      // Show above target if not enough space below
      top = targetRect.top - popoverRect.height - 8;
    }

    if (top < 10) {
      top = 10;
    }

    popoverEl.style.position = "fixed";
    popoverEl.style.margin = "0";
    popoverEl.style.left = `${left}px`;
    popoverEl.style.top = `${top}px`;
  }

  function findPopoverElForTarget(targetEl: HTMLElement): HTMLElement | null {
    if (targetEl.hasAttribute("popover")) {
      return targetEl;
    }
    const onclickStr = targetEl.getAttribute("onclick") || "";
    const match = onclickStr.match(/document\.getElementById\(['"]([^'"]+)['"]\)/);
    if (match && match[1]) {
      const popoverEl = document.getElementById(match[1]);
      if (popoverEl) return popoverEl;
    }
    return null;
  }

  class Notification implements INotification {
    constructor(public el: HTMLElement) {}
    close() {
      this.el.style.display = "none";
    }
    show() {
      this.el.style.display = "";
    }
    destroy() {
      this.el.remove();
    }
  }

  class Tooltip implements ITooltip {
    constructor(public el: HTMLElement) {}
    close() {
      this.el.classList.remove("active");
    }
    show() {
      this.el.classList.add("active");
    }
    destroy() {
      this.el.classList.remove("active");
      delete this.el.dataset.tooltip;
      delete this.el.dataset.tooltipPosition;
    }
  }

  class Popover implements IPopover {
    private cleanupListeners: (() => void)[] = [];
    public target: HTMLElement | null = null;
    public trigger: string = "click";

    constructor(public el: HTMLElement, target?: HTMLElement, trigger?: string) {
      if (target) {
        this.target = target;
      }
      if (trigger) {
        this.trigger = trigger;
      }

      this.setupTriggerListeners();
      this.el.addEventListener("toggle", this.handleToggle);
    }

    private handleToggle = (e: Event) => {
      const event = e as ToggleEvent;
      if (event.newState === "open") {
        this.position();
        window.addEventListener("scroll", this.reposition, { passive: true });
        window.addEventListener("resize", this.reposition, { passive: true });
      } else {
        window.removeEventListener("scroll", this.reposition);
        window.removeEventListener("resize", this.reposition);
      }
    };

    private reposition = () => {
      if (this.el.matches(":popover-open")) {
        this.position();
      }
    };

    public position() {
      if (!this.target) return;
      positionPopover(this.el, this.target);
    }

    private setupTriggerListeners() {
      if (!this.target) return;

      const target = this.target;

      // Remove inline onclick handler to avoid conflicts
      target.removeAttribute("onclick");

      if (this.trigger === "hover") {
        let hoverTimeout: any;

        const show = () => {
          clearTimeout(hoverTimeout);
          this.show();
        };

        const hide = () => {
          clearTimeout(hoverTimeout);
          hoverTimeout = setTimeout(() => {
            if (!this.el.matches(":hover") && !target.matches(":hover")) {
              this.close();
            }
          }, 100);
        };

        target.addEventListener("mouseenter", show);
        target.addEventListener("mouseleave", hide);
        this.el.addEventListener("mouseenter", show);
        this.el.addEventListener("mouseleave", hide);

        this.cleanupListeners.push(() => {
          target.removeEventListener("mouseenter", show);
          target.removeEventListener("mouseleave", hide);
          this.el.removeEventListener("mouseenter", show);
          this.el.removeEventListener("mouseleave", hide);
        });
      } else if (this.trigger === "focus") {
        const show = () => this.show();
        const hide = () => this.close();

        target.addEventListener("focus", show);
        target.addEventListener("blur", hide);

        this.cleanupListeners.push(() => {
          target.removeEventListener("focus", show);
          target.removeEventListener("blur", hide);
        });
      } else {
        // default "click"
        const toggle = (e: MouseEvent) => {
          e.preventDefault();
          e.stopPropagation();
          if (this.el.matches(":popover-open")) {
            this.close();
          } else {
            this.show();
          }
        };

        target.addEventListener("click", toggle);
        this.cleanupListeners.push(() => {
          target.removeEventListener("click", toggle);
        });
      }
    }

    close() {
      try {
        this.el.hidePopover();
      } catch (err) {
        // ignore if already hidden
      }
    }

    show() {
      if (!this.el.parentElement) {
        document.body.appendChild(this.el);
      }
      try {
        this.el.showPopover();
        this.position();
      } catch (err) {
        // ignore if already shown
      }
    }

    destroy() {
      this.close();
      this.el.removeEventListener("toggle", this.handleToggle);
      window.removeEventListener("scroll", this.reposition);
      window.removeEventListener("resize", this.reposition);
      this.cleanupListeners.forEach(cleanup => cleanup());
      this.cleanupListeners = [];
      this.el.remove();
    }
  }

  const ui: IUi = {
    button(content: Theming.Content, params: Theming.IButtonParams = {}) {
      const btn = document.createElement("button");
      btn.append(content);
      btn.classList.add("btn", `btn-${params.style ?? "primary"}`);

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
      return btn;
    },

    modal(content: Theming.Content, params: Theming.IModalParams = {}) {
      const modal = document.createElement("dialog");
      modal.className = "modal";

      modal.addEventListener("close", () => result.destroy());

      if (params.dismissible) {
        (modal as any).closedBy = "any";
      }

      const modalContent = document.createElement("div");
      modalContent.className = "modal-content";
      modal.appendChild(modalContent);

      if (params.title || params.dismissible) {
        const headerEl = document.createElement("div");
        headerEl.className = "modal-header";

        if (params.title) {
          const titleEl = document.createElement("h2");
          titleEl.append(params.title);
          headerEl.appendChild(titleEl);
        }

        if (params.dismissible) {
          const closeBtn = document.createElement("button");
          closeBtn.type = "button";
          closeBtn.className = "modal-close-btn";
          closeBtn.innerHTML = "&times;";
          closeBtn.onclick = () => result.close();
          headerEl.appendChild(closeBtn);
        }

        modalContent.appendChild(headerEl);
      }

      const bodyEl = document.createElement("div");
      bodyEl.className = "modal-body";
      bodyEl.append(content);
      modalContent.appendChild(bodyEl);

      const actions = params.actions ? [...params.actions] : [];
      if (params.dismissLabel) {
        actions.unshift(
          ui.button(params.dismissLabel, {
            props: { onclick: () => result.close() },
            style: "secondary",
          }) as HTMLButtonElement,
        );
      }

      if (actions.length) {
        const footerEl = document.createElement("div");
        footerEl.className = "modal-footer";
        footerEl.append(...actions);
        modalContent.appendChild(footerEl);
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

    notification(content: Theming.Content, props: Theming.INotificationParams = {}) {
      let toastStack = document.querySelector(".toast-stack");
      if (!toastStack) {
        toastStack = document.createElement("div");
        toastStack.className = "toast-stack toast-stack-top-right";
        document.body.appendChild(toastStack);
      }

      const el = document.createElement("div");
      el.style.display = "none";
      el.className = `toast toast-${props.style ?? "info"}`;

      const result = new Notification(el);

      if (props.title || props.dismissible) {
        const headerEl = document.createElement("div");
        headerEl.className = "toast-header";

        if (props.title) {
          const titleEl = document.createElement("span");
          titleEl.append(props.title);
          headerEl.appendChild(titleEl);
        } else {
          const titleEl = document.createElement("span");
          headerEl.appendChild(titleEl);
        }

        if (props.dismissible) {
          const dismissBtn = document.createElement("button");
          dismissBtn.type = "button";
          dismissBtn.className = "modal-close-btn";
          dismissBtn.innerHTML = "&times;";
          dismissBtn.style.padding = "0";
          dismissBtn.style.lineHeight = "1";
          dismissBtn.style.fontSize = "1.25rem";
          dismissBtn.onclick = () => result.close();
          headerEl.appendChild(dismissBtn);
        }

        el.appendChild(headerEl);
      }

      const bodyEl = document.createElement("div");
      bodyEl.className = "toast-body";
      bodyEl.append(content);
      el.appendChild(bodyEl);

      if (props.delay) {
        const progress = el.appendChild(document.createElement("progress"));
        progress.className = "progress";
        progress.style.margin = "0";
        progress.style.borderRadius = "0";
        progress.style.height = "4px";
        progress.style.width = "100%";
        progress.max = props.delay;
        progress.value = props.delay;

        let timeoutId: any;
        let animationFrameId: any;
        const start = Number(new Date());

        const originalShow = result.show.bind(result);
        const originalClose = result.close.bind(result);

        result.show = () => {
          originalShow();

          timeoutId = setTimeout(() => result.close(), props.delay);

          function _animate() {
            const diff = Number(new Date()) - start;
            progress.value = (props.delay || 0) - diff;
            if (progress.value > 0) {
              animationFrameId = requestAnimationFrame(_animate);
            }
          }
          _animate();
        };

        result.close = () => {
          clearTimeout(timeoutId);
          cancelAnimationFrame(animationFrameId);
          originalClose();
        };
      }

      toastStack.appendChild(el);
      return result;
    },

    getNotification(id) {
      const el = document.getElementById(id);
      if (!el) {
        return null;
      }
      return new Notification(el);
    },

    tooltip(content: Theming.Content, props?: Theming.ITooltipParams) {
      if (!props || !props.target) {
        throw "Tooltip target is required";
      }
      if (typeof content !== "string") {
        throw "Only string tooltips are supported";
      }
      const target = props.target;
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

    popover(content: Theming.Content, props?: Theming.IPopoverParams) {
      const el = document.createElement("div");
      el.setAttribute("popover", "auto");

      const contentEl = document.createElement("div");
      contentEl.className = "popover-content";

      if (props && props.title) {
        const titleEl = document.createElement("h4");
        titleEl.append(props.title);
        contentEl.appendChild(titleEl);
      }

      const bodyEl = document.createElement("div");
      bodyEl.append(content);
      contentEl.appendChild(bodyEl);
      el.appendChild(contentEl);

      const target = props?.target;
      const trigger = props?.trigger || "click";

      return new Popover(el, target, trigger);
    },

    getPopover(id) {
      const targetEl = document.getElementById(id);
      if (!targetEl) {
        return null;
      }

      const popoverEl = findPopoverElForTarget(targetEl);
      if (!popoverEl) {
        if (targetEl.hasAttribute("popover")) {
          return new Popover(targetEl);
        }
        return null;
      }

      return new Popover(popoverEl, targetEl);
    },

    autocomplete(element: HTMLElement | string, params: Theming.IAutocompleteParams = {}) {
      const el = typeof element === "string"
        ? (document.getElementById(element) || document.querySelector(element)) as HTMLElement
        : element;

      if (!el) {
        throw new Error("Autocomplete element not found");
      }

      const existing = ui.getAutocomplete(el);
      if (existing) {
        return existing;
      }

      el.setAttribute("data-module", "theming-autocomplete");
      if (params.source) el.setAttribute("data-module-source", params.source);
      if (params.options) el.setAttribute("data-module-options", JSON.stringify(params.options));
      if (params.allowMultiple !== undefined) el.setAttribute("data-module-allow-multiple", String(params.allowMultiple));
      if (params.allowNew !== undefined) el.setAttribute("data-module-allow-new", String(params.allowNew));
      if (params.selected) el.setAttribute("data-module-selected", JSON.stringify(params.selected));
      if (params.idKey) el.setAttribute("data-module-id-key", params.idKey);
      if (params.labelKey) el.setAttribute("data-module-label-key", params.labelKey);
      if (params.joined !== undefined) el.setAttribute("data-module-joined", String(params.joined));
      if (params.separator) el.setAttribute("data-module-separator", params.separator);
      if (params.minChars !== undefined) el.setAttribute("data-module-min-chars", String(params.minChars));
      if (params.debounce !== undefined) el.setAttribute("data-module-debounce", String(params.debounce));

      // @ts-ignore
      window.ckan.module.initializeElement(el);

      const newInstance = ui.getAutocomplete(el);
      if (!newInstance) {
        throw new Error("Failed to initialize autocomplete module");
      }
      return newInstance;
    },

    getAutocomplete(id_or_el: string | HTMLElement) {
      const el = typeof id_or_el === "string"
        ? (document.getElementById(id_or_el) || document.querySelector(id_or_el)) as HTMLElement
        : id_or_el;

      if (!el) {
        return null;
      }

      // @ts-ignore
      const instances = window.ckan.module.instances["theming-autocomplete"] || [];
      const instance = instances.find((inst: any) => inst.el[0] === el);
      if (instance) {
        return new Autocomplete(el, instance);
      }
      return null;
    },
  };

  class Autocomplete implements IAutocomplete {
    constructor(public el: HTMLElement, public instance: any) {}

    select(value: string, label?: string) {
      this.instance.select(value, label || value);
    }

    unselect(value: string) {
      this.instance.remove(value);
    }

    onchange(callback: (values: string[]) => void) {
      const handler = (e: any) => {
        const values = e.detail.values.map((v: any) => v.value);
        callback(values);
      };
      this.el.addEventListener("autocomplete:change", handler);
    }

    destroy() {
      this.instance.teardown();
      // @ts-ignore
      const instances = window.ckan.module.instances["theming-autocomplete"] || [];
      const idx = instances.indexOf(this.instance);
      if (idx !== -1) {
        instances.splice(idx, 1);
      }
    }
  }

  // Tab Switching Logic
  document.addEventListener("click", (e) => {
    const target = e.target as HTMLElement;
    const tabLink = target.closest(".tab-link");
    if (!tabLink) return;

    const href = tabLink.getAttribute("href");
    const controls = tabLink.getAttribute("aria-controls");
    const targetId = controls || (href && href.startsWith("#") ? href.slice(1) : null);
    if (!targetId) return;

    const targetPane = document.getElementById(targetId);
    if (!targetPane || !targetPane.classList.contains("tab-pane")) return;

    // Prevent default navigation
    e.preventDefault();

    // Find the current tab list/nav
    const tabList = tabLink.closest(".tabs");
    if (tabList) {
      // Remove active from all items in this tab list
      tabList.querySelectorAll(".tab-item").forEach((item) => {
        item.classList.remove("active");
        const link = item.querySelector(".tab-link");
        if (link) {
          link.setAttribute("aria-selected", "false");
        }
      });
      // Add active to current item
      const tabItem = tabLink.closest(".tab-item");
      if (tabItem) {
        tabItem.classList.add("active");
        tabLink.setAttribute("aria-selected", "true");
      }
    }

    // Find the container (.tab-content) of the target pane to deactivate other panes in the same container
    const paneContainer = targetPane.closest(".tab-content");
    if (paneContainer) {
      paneContainer.querySelectorAll(".tab-pane").forEach((pane) => {
        pane.classList.remove("active");
      });
    } else {
      // Fallback: if not in .tab-content, find sibling panes
      const parent = targetPane.parentElement;
      if (parent) {
        Array.from(parent.children).forEach((child) => {
          if (child.classList.contains("tab-pane")) {
            child.classList.remove("active");
          }
        });
      }
    }

    // Show target pane
    targetPane.classList.add("active");
  });

  ckan.sandbox.setup((sb) => {
    sb.ui = sb.ui || {};
    const uiAny = sb.ui as any;
    uiAny.util = uiAny.util || {};
    Object.assign(sb.ui, ui);
    Object.assign(uiAny.util, util);
  });
})(window.ckan);
