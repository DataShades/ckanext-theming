
export  class Notification implements INotification {
    #alert: any;
    #sandbox: ISandbox;
    constructor(public el: HTMLElement) {
      this.#sandbox = window.ckan.sandbox();
      this.#alert = this.#sandbox.notify.initialize(el);
      this.#alert.hide();
      this.#sandbox.notify.el.append(this.#alert);
    }
    close() {
      this.#alert.hide();
    }
    show() {
      this.#alert.show();
    }
    destroy() {
      this.#alert.remove();
    }
    static create(
      content: Theming.Content,
      props: Theming.INotificationParams = {},
    ): Notification {
      const notify = window.ckan.sandbox().notify;
      const el = notify.create(
        props.title &&
          (typeof props.title === "string"
            ? props.title
            : props.title.textContent),
        typeof content === "string" ? content : content.textContent,
        props.style || "default",
      );

      return new Notification(el[0]);
    }

    static byId(id: string): Notification | null {
      const el = document.getElementById(id);
      if (!el) {
        return null;
      }
      return new Notification(el);
    }
  }
