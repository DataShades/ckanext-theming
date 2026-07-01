/**
 * change-submit.js
 * =================
 * Automatically submits a form when a 'change' event is detected.
 *
 * Usage:
 * <form data-module="theming-change-submit" data-module-selector="select">
 *   <select name="sort">...</select>
 * </form>
 *
 * Configuration:
 * data-module-selector: (Optional) CSS selector to filter which elements
 *                       trigger the submission. If omitted, any change
 *                       within the container triggers it.
 */

ckan.module("theming-change-submit", () => {
  return {
    options: {
      selector: null,
      externalTracking: false,
    },

    initialize() {
      this.root = this.el[0];
      this.isForm = this.root.tagName === "FORM";
      this.isExternalTracking = this.options.externalTracking;

      this.form = this.root.form ||
                  (this.root.getAttribute("form") ? document.getElementById(this.root.getAttribute("form")) : null) ||
                  (this.isForm ? this.root : this.root.closest("form"));

      this._onChange = this._onChange.bind(this);

      if (this.isForm && this.isExternalTracking) {
        // Intercept global change events to catch external fields associated with this form
        document.addEventListener("change", this._onChange);
      } else {
        this.root.addEventListener("change", this._onChange);
      }
    },

    _onChange(event) {
      const { selector } = this.options;
      // If a selector is provided, only submit if the target matches
      if (selector && !event.target.matches(selector)) {
        return;
      }

      const form = event.target.form ||
                   (event.target.getAttribute("form") ? document.getElementById(event.target.getAttribute("form")) : null) ||
                   event.target.closest("form");

      if (this.isForm && this.isExternalTracking) {
        if (form === this.root) {
          this.root.requestSubmit();
        }
      } else {
        if (form) {
          form.requestSubmit();
        } else {
          console.warn("[theming-change-submit]: No parent or associated form found for change event");
        }
      }
    },

    teardown() {
      if (this.isForm && this.isExternalTracking) {
        document.removeEventListener("change", this._onChange);
      } else if (this.root) {
        this.root.removeEventListener("change", this._onChange);
      }
    },
  };
});
