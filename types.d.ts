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
     */
    interface IModalParams extends IParams {
      title?: Content;
      actions?: HTMLElement[];
      dismissible?: boolean;
      dismissLabel?: Content;
    }

    /**
     * Parameters for notification functionality.
     *
     * @property style - Additional style classes for the notification.
     * @property dismissible - Whether the notification can be dismissed by the user.
     * @property title - Title text displayed in the notification header.
     * @property delay - Time in milliseconds before auto-hide.
     */
    interface INotificationParams extends IParams {
      style?: string;
      dismissible?: boolean;
      title?: Content;
      delay?: number;
    }

    /**
     * Parameters for tooltip functionality.
     *
     * @property position - Position of the tooltip relative to the target element ("top", "bottom", "left", or "right").
     */
    interface ITooltipParams extends IParams {
      position?: "top" | "bottom" | "left" | "right";
      target: HTMLElement;
    }

    /**
     * Parameters for popover functionality.
     */
    interface IPopoverParams extends IParams {
      trigger?: string;
      target: HTMLElement;
      title?: string | null;
    }

    /**
     * Parameters for autocomplete functionality.
     */
    interface IAutocompleteParams extends IParams {
      source?: string;
      options?: Array<string | { [key: string]: any }>;
      allowMultiple?: boolean;
      allowNew?: boolean;
      selected?: Array<string | { [key: string]: any }>;
      idKey?: string;
      labelKey?: string;
      joined?: boolean;
      separator?: string;
      minChars?: number;
      debounce?: number;
    }

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
    sandbox: ISandboxFactory;
  }

  /**
   * Interface for the sandbox environment.
   *
   * @property setup - Method to initialize the sandbox with a callback function.
   * @property ui - Object containing UI components.
   */
  interface ISandboxFactory {
    setup: (callback: (sandbox: ISandbox) => void) => void;
    (): ISandbox;
  }
  interface ISandbox {
    ui: IUi;
    notify: any;
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
    modal: (content: Theming.Content, params?: Theming.IModalParams) => IModal;

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
      props?: Theming.INotificationParams,
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
      props?: Theming.IPopoverParams,
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
      props?: Theming.ITooltipParams,
    ) => ITooltip;

    /**
     * Initialize autocomplete on the given element, or return existing autocomplete instance.
     *
     * @param element The input or select element to bind autocomplete to.
     * @param params Configuration parameters for the autocomplete.
     * @returns Autocomplete instance.
     */
    autocomplete(element: HTMLElement | string, params?: Theming.IAutocompleteParams): IAutocomplete;

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

    /**
     * Retrieve an existing autocomplete instance by ID or element.
     *
     * @param id_or_el The element or ID of the autocomplete element.
     * @returns Autocomplete instance or null if not found.
     */
    getAutocomplete(id_or_el: string | HTMLElement): IAutocomplete | null;
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

  /**
   * Interface for Autocomplete component.
   *
   * @param T - The type of the underlying HTML element (default is HTMLElement).
   * @property select - Method to programmatically select a value.
   * @property unselect - Method to programmatically unselect a value.
   * @property onchange - Method to subscribe to selection changes.
   * @property destroy - Method to clean up resources.
   * @property el - The underlying HTML element.
   */
  interface IAutocomplete<T = HTMLElement> {
    select(value: string, label?: string): void;
    unselect(value: string): void;
    onchange(callback: (values: string[]) => void): void;
    destroy(): void;
    el: T;
  }
}
export {};
