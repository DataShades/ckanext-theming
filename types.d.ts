declare global {
  namespace Theming {
    /**
     *
     */
    interface IParams {
      attrs?: { [key: string]: string };
      props?: { [key: string]: any };
      on?: { [key: string]: Listener | ComplexListener };
      [key: string]: any;
    }

    /**
     *
     */
    interface IButtonParams extends IParams {
      type?: "button" | "submit" | "reset";
      style?: string;
    }

    /**
     *
     */
    interface IModalParams extends IParams {
      dismissible?: boolean;
      dismissLabel?: Content;
      style?: string;
    }

    /**
     *
     */
    interface INotificationParams extends IParams {
      style?: string;
      dismissible?: boolean;
      timeout?: number;
    }

    /**
     *
     */
      interface ITooltipParams extends IParams {
          position?: "top"|"bottom"|"left"|"right";
      }

    /**
     *
     */
    interface IPopoverParams extends IParams {}

    /**
     *
     */
    interface IAutocompleteParams extends IParams {}

    /**
     *
     */
    type Content = string | Node;

    /**
     *
     */
    type Listener = (this: HTMLElement, e: Event) => any;

    /**
     *
     */
    type ComplexListener = {
      listener: Listener;
      options: AddEventListenerOptions;
    };
  }

  /**
   *
   */
  interface Window {
    ckan: ICkan;
  }

  /**
   *
   */
  interface ICkan {
    sandbox: ISandbox;
  }

  /**
   *
   */
  interface ISandbox {
    setup: (callback: (sandbox: ISandbox) => void) => void;
    ui: IUi & { util: IUtil };
  }

  /**
   *
   */
  interface IUtil {
    /**
     *
     */
    animateTimeout(
      el: HTMLProgressElement,
      start: number,
      timeout: number,
    ): void;

    /**
     *
     */
    applyListeners(
      el: HTMLElement,
      listeners: { [key: string]: Theming.Listener | Theming.ComplexListener },
    ): void;

    /**
     *
     */
    applyProps(el: HTMLElement, props: { [key: string]: any }): void;

    /**
     *
     */
    applyAttrs(el: HTMLElement, attrs: { [key: string]: string }): void;
  }

  /**
   *
   */
  interface IUi {
    /**
     *
     */
    modal: (
      content: Theming.Content,
      title: Theming.Content,
      actions: HTMLElement[],
      params?: Theming.IModalParams,
    ) => IModal;

    /**
     *
     */
    button: (
      content: Theming.Content,
      params?: Theming.IButtonParams,
    ) => HTMLElement;

    /**
     *
     */
    notification: (
      content: Theming.Content,
      title: Theming.Content,
      props: Theming.INotificationParams,
    ) => INotification;

    /**
     *
     */
    popover: (
      content: Theming.Content,
      props: Theming.IPopoverParams,
    ) => IPopover;

    /**
     *
     */
    tooltip: (
      content: Theming.Content,
      target: HTMLElement,
      props: Theming.ITooltipParams,
    ) => ITooltip;

    /**
     *
     */
    autocomplete: (
      target: HTMLInputElement | HTMLSelectElement,
      props: Theming.IAutocompleteParams,
    ) => void;

    /**
     * Initialize or retrieve a modal by ID.
     *
     * @param id ID of the modal element.
     * @returns Modal instance or null if not found.
     */
    getModal(id: string): IModal | null;

    /**
     * Initialize or retrieve a tooltip by ID.
     *
     * @param id ID of the tooltip element.
     * @return Tooltip instance or null if not found.
     */
    getTooltip(id: string): ITooltip | null;

    /**
     * Initialize or retrieve a popover by ID.
     *
     * @param id ID of the popover element.
     * @return Popover instance or null if not found.
     */
    getPopover(id: string): IPopover | null;

    /**
     *
     */
    getNotification(id: string): INotification | null;
  }

  /**
   *
   */
  interface IModal<T = HTMLElement> {
    show: () => void;
    close: () => void;
    destroy: () => void;
    el: T;
  }

  /**
   *
   */
  interface INotification<T = HTMLElement> {
    show: () => void;
    close: () => void;
    destroy: () => void;
    el: T;
  }

  /**
   *
   */
  interface ITooltip<T = HTMLElement> {
    show: () => void;
    close: () => void;
    destroy: () => void;
    el: T;
  }

  /**
   *
   */
  interface IPopover<T = HTMLElement> {
    show: () => void;
    close: () => void;
    destroy: () => void;
    el: T;
  }
}
export {};
//# sourceMappingURL=script.d.ts.map
