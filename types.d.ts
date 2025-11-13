
declare global {
    namespace Theming {
        interface IParams {
            attrs?: { [key: string]: string; };
            props?: { [key: string]: any; };
            on?: {[key: string]: Listener | ComplexListener};
            [key: string]: any;
        }
        interface IButtonParams extends IParams {
            type?: "button" | "submit" | "reset";
            style?: string;
        }
        interface IModalParams extends IParams {
            dismissible?: boolean;
            dismissLabel?: Content;
            style?: string;
        }
        interface INotificationParams extends IParams {
            style?: string;
            dismissible?: boolean;
            timeout?: number;
        }

        type Content = string | Node;
        type Listener = (this: HTMLElement, e: Event) => any;
        type ComplexListener = {
          listener: Listener;
          options: AddEventListenerOptions;
        };

    }
    interface Window {
        ckan: ICkan;
    }
    interface ICkan {
        sandbox: ISandbox;
    }
    interface ISandbox {
        setup: (callback: (sandbox: ISandbox) => void) => void;
        ui: IUi;
    }
    interface IUi {
        util?: object;
        modal: (content: Theming.Content, title: Theming.Content, actions: HTMLElement[], params?: Theming.IModalParams) => IModal;
        button: (content: Theming.Content, params?: Theming.IButtonParams) => HTMLElement;
        notification: (content: Theming.Content, title: Theming.Content, props: Theming.INotificationParams) => INotification;
    }
    interface IModal<T = HTMLElement> {
        show: () => void;
        close: () => void;
        destroy: () => void;
        el: T;
    }
    interface INotification<T = HTMLElement> {
        dismiss: () => void;
        el: T;
    }
}
export {};
//# sourceMappingURL=script.d.ts.map
