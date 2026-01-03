/**
 * Global TypeScript definitions for CKAN theming and UI components.
 */
declare global {
  /** Namespace for theming-related types and interfaces. */
  namespace Theming {
    /**
     * Base parameters for UI components.
     *
     * @property attrs - HTML attributes to set on the element.
     * @property props - Properties to set on the element.
     * @property on - Event listeners to attach to the element.
     * @property [key: string] - Additional custom parameters.
     */
    interface IParams {
      attrs?: { [key: string]: string };
      props?: { [key: string]: any };
      on?: { [key: string]: Listener | ComplexListener };
      [key: string]: any;
    }

    /**
     * Parameters for button functionality.
     *
     * @property type - The type of button ("button", "submit", or "reset").
     * @property style - Additional style classes for the button.
     */
    interface IButtonParams extends IParams {
      type?: "button" | "submit" | "reset";
      style?: string;
    }

    /**
     * Parameters for modal functionality.
     *
     * @property dismissible - Whether the modal can be dismissed by clicking outside or pressing ESC.
     * @property dismissLabel - Content for the dismiss button.
     * @property style - Additional style classes for the modal.
     */
    interface IModalParams extends IParams {
      dismissible?: boolean;
      dismissLabel?: Content;
      style?: string;
    }

    /**
     * Parameters for notification functionality.
     *
     * @property style - Additional style classes for the notification.
     * @property dismissible - Whether the notification can be dismissed by the user.
     * @property timeout - Duration in milliseconds before the notification auto-dismisses.
     */
    interface INotificationParams extends IParams {
      style?: string;
      dismissible?: boolean;
      timeout?: number;
    }

    /**
     * Parameters for tooltip functionality.
     *
     * @property position - Position of the tooltip relative to the target element ("top", "bottom", "left", or "right").
     */
    interface ITooltipParams extends IParams {
      position?: "top"|"bottom"|"left"|"right";
    }

    /**
     * Parameters for popover functionality.
     */
    interface IPopoverParams extends IParams {}

    /**
     * Content type for UI components.
     */
    type Content = string | Node;

    /**
     * Simple event listener function.
     *
     * @param e - The event object.
     */
    type Listener = (this: HTMLElement, e: Event) => any;

    /**
     * Complex listener with options.
     *
     * @property listener - The event listener function.
     * @property options - Options for the event listener.
     */
    type ComplexListener = {
      listener: Listener;
      options: AddEventListenerOptions;
    };
  }

  /**
   * Extend the global Window interface to include the CKAN object.
   */
  interface Window {
    ckan: ICkan;
  }

  /**
   * Interface for the global CKAN object.
   *
   * @property sandbox - The sandbox environment.
   */
  interface ICkan {
    sandbox: ISandbox;
  }

  /**
   * Interface for the sandbox environment.
   *
   * @property setup - Method to initialize the sandbox with a callback function.
   * @property ui - Object containing UI components and utility functions.
   */
  interface ISandbox {
    setup: (callback: (sandbox: ISandbox) => void) => void;
    ui: IUi & { util: IUtil };
  }

  /**
   * Interface for utility functions.
   *
   * @property animateTimeout - Method to animate a progress element over a specified timeout.
   * @property applyListeners - Method to attach event listeners to an element.
   * @property applyProps - Method to set properties on an element.
   * @property applyAttrs - Method to set attributes on an element.
   */
  interface IUtil {
    /**
     * Animate a progress element over a specified timeout.
     *
     * @param el The target HTMLProgressElement.
     * @param start The starting value of the progress (0 to 1).
     * @param timeout The duration of the animation in milliseconds.
     */
    animateTimeout(
      el: HTMLProgressElement,
      start: number,
      timeout: number,
    ): void;

    /**
     * Attach event listeners to an element.
     *
     * @param el The target HTML element.
     * @param listeners An object containing event listeners to attach.
     */
    applyListeners(
      el: HTMLElement,
      listeners: { [key: string]: Theming.Listener | Theming.ComplexListener },
    ): void;

    /**
     * Set properties on an element.
     *
     * @param el The target HTML element.
     * @param props An object containing properties to set on the element.
     */
    applyProps(el: HTMLElement, props: { [key: string]: any }): void;

    /**
     * Set attributes on an element.
     *
     * @param el The target HTML element.
     * @param attrs An object containing attributes to set on the element.
     */
    applyAttrs(el: HTMLElement, attrs: { [key: string]: string }): void;
  }

  /**
   * Interface for UI components.
   *
   * @property modal - Method to create a modal element.
   * @property button - Method to create a button element.
   * @property notification - Method to create a notification element.
   * @property popover - Method to create a popover element.
   * @property tooltip - Method to create a tooltip element.
   * @property getModal - Method to retrieve an existing modal by ID.
   * @property getTooltip - Method to retrieve an existing tooltip by ID.
   * @property getPopover - Method to retrieve an existing popover by ID.
   * @property getNotification - Method to retrieve an existing notification by ID.
   */
  interface IUi {
    /**
     * Create a modal element.
     *
     * @param content The content of the modal.
     * @param title The title of the modal.
     * @param actions An array of action buttons for the modal.
     * @param params Configuration parameters for the modal.
     * @returns Modal instance.
     */
    modal: (
      content: Theming.Content,
      title: Theming.Content,
      actions: HTMLElement[],
      params?: Theming.IModalParams,
    ) => IModal;

    /**
     * Create a button element.
     *
     * @param content The content of the button.
     * @param params Configuration parameters for the button.
     * @returns The created button element.
     */
    button: (
      content: Theming.Content,
      params?: Theming.IButtonParams,
    ) => HTMLElement;

    /**
     * Create a notification element.
     *
     * @param content The content of the notification.
     * @param title The title of the notification.
     * @param props Configuration parameters for the notification.
     * @returns Notification instance.
     */
    notification: (
      content: Theming.Content,
      title: Theming.Content,
      props: Theming.INotificationParams,
    ) => INotification;

    /**
     * Create a popover attached to a target element.
     *
     * @param content The content of the popover.
     * @param props Configuration parameters for the popover.
     * @returns Popover instance.
     */
    popover: (
      content: Theming.Content,
      props: Theming.IPopoverParams,
    ) => IPopover;

    /**
     * Create a tooltip attached to a target element.
     *
     * @param content The content of the tooltip.
     * @param target The target element to which the tooltip is attached.
     * @param props Configuration parameters for the tooltip.
     * @returns Tooltip instance.
     */
    tooltip: (
      content: Theming.Content,
      target: HTMLElement,
      props: Theming.ITooltipParams,
    ) => ITooltip;

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
     * Initialize or retrieve a notification by ID.
     *
     * @param id ID of the notification element.
     * @return Notification instance or null if not found.
     */
    getNotification(id: string): INotification | null;
  }

  /**
   * Interface for Modal component.
   *
   * @param T - The type of the underlying HTML element (default is HTMLElement).
   * @property show - Method to display the modal.
   * @property close - Method to hide the modal.
   * @property destroy - Method to remove the modal from the DOM and clean up resources.
   * @property el - The underlying HTML element of the modal.
   */
  interface IModal<T = HTMLElement> {
    show: () => void;
    close: () => void;
    destroy: () => void;
    el: T;
  }

  /**
   * Interface for Notification component.
   *
   * @param T - The type of the underlying HTML element (default is HTMLElement).
   * @property show - Method to display the notification.
   * @property close - Method to hide the notification.
   * @property destroy - Method to remove the notification from the DOM and clean up resources.
   * @property el - The underlying HTML element of the notification.
   */
  interface INotification<T = HTMLElement> {
    show: () => void;
    close: () => void;
    destroy: () => void;
    el: T;
  }

  /**
   * Interface for Tooltip component.
   *
   * @param T - The type of the underlying HTML element (default is HTMLElement).
   * @property show - Method to display the tooltip.
   * @property close - Method to hide the tooltip.
   * @property destroy - Method to remove the tooltip from the DOM and clean up resources.
   * @property el - The underlying HTML element of the tooltip.
   */
  interface ITooltip<T = HTMLElement> {
    show: () => void;
    close: () => void;
    destroy: () => void;
    el: T;
  }

  /**
   * Interface for Popover component.
   *
   * @param T - The type of the underlying HTML element (default is HTMLElement).
   * @property show - Method to display the popover.
   * @property close - Method to hide the popover.
   * @property destroy - Method to remove the popover from the DOM and clean up resources.
   * @property el - The underlying HTML element of the popover.
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
