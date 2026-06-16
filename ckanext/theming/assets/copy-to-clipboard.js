/**
 * copy-to-clipboard.js
 * ====================
 * Copies text content to the clipboard when clicked.
 *
 * Usage:
 * <button data-theming-module="copy-to-clipboard" data-copy-to-clipboard-value="text to copy">Copy</button>
 * or
 * <button data-theming-module="copy-to-clipboard" data-copy-to-clipboard-selector="#target-element">Copy</button>
 *
 * Configuration:
 * data-copy-to-clipboard-value: Actual value to copy.
 * data-copy-to-clipboard-selector: CSS selector for the target element to copy textContent from.
 */

ckan.module("copy-to-clipboard", () => {
  return {
    options: {
      value: null,
      selector: null,
    },

    initialize() {
      this.root = this.el[0];
      this._onClick = this._onClick.bind(this);
      this.root.addEventListener("click", this._onClick);
    },

    _onClick(event) {
      event.preventDefault();
      const { value, selector } = this.options;
      let textToCopy = "";

      if (value !== null) {
        textToCopy = value;
      } else if (selector) {
        const target = document.querySelector(selector);
        if (target) {
          textToCopy = target.textContent;
        } else {
          console.warn(
            "CopyToClipboard: Target element not found for selector",
            selector,
          );
          return;
        }
      } else {
        console.warn("CopyToClipboard: Neither value nor selector specified.");
        return;
      }

      this._copyText(textToCopy);
    },

    _copyText(text) {
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard
          .writeText(text)
          .then(() => {
            this._onSuccess(text);
          })
          .catch((err) => {
            console.error("CopyToClipboard: Secure copy failed", err);
            this._fallbackCopy(text);
          });
      } else {
        this._fallbackCopy(text);
      }
    },

    _fallbackCopy(text) {
      try {
        const textarea = document.createElement("textarea");
        // Hide the textarea from view but keep it editable
        textarea.value = text;
        textarea.style.position = "fixed";
        textarea.style.top = "0";
        textarea.style.left = "0";
        textarea.style.width = "2em";
        textarea.style.height = "2em";
        textarea.style.padding = "0";
        textarea.style.border = "none";
        textarea.style.outline = "none";
        textarea.style.boxShadow = "none";
        textarea.style.background = "transparent";
        document.body.appendChild(textarea);
        textarea.focus();
        textarea.select();

        const successful = document.execCommand("copy");
        document.body.removeChild(textarea);

        if (successful) {
          this._onSuccess(text);
        } else {
          throw new Error("execCommand returned false");
        }
      } catch (err) {
        console.error("CopyToClipboard: Fallback copy failed", err);
      }
    },

    _onSuccess(text) {
      // Fire a custom event to notify external listeners of successful copying
      const event = new CustomEvent("copy-to-clipboard:success", {
        bubbles: true,
        detail: { text },
      });
      this.root.dispatchEvent(event);
    },
  };
});
