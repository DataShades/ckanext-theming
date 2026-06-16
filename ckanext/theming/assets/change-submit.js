/**
 * change-submit.js
 * =================
 * Automatically submits a form when a 'change' event is detected.
 *
 * Usage:
 * <form data-module="change-submit" data-module-selector="select">
 *   <select name="sort">...</select>
 * </form>
 *
 * Configuration:
 * data-module-selector: (Optional) CSS selector to filter which elements
 *                       trigger the submission. If omitted, any change
 *                       within the container triggers it.
 */

ckan.module("change-submit", () => {
  return {
    options: {
      selector: null,
    },

    initialize() {
      this.root = this.el[0];
      this.form = this.root.tagName === "FORM" ? this.root : this.root.closest("form");

      if (!this.form) {
        console.warn("[change-submit]: No parent form found for", this.root);
        return;
      }

      this._onChange = this._onChange.bind(this);
      this.root.addEventListener("change", this._onChange);
    },

    _onChange(event) {
      const { selector } = this.options;
      // If a selector is provided, only submit if the target matches
      if (selector && !event.target.matches(selector)) {
        return;
      }

      this.form.requestSubmit();
    },

    teardown() {
      if (this.root) {
        this.root.removeEventListener("change", this._onChange);
      }
    },
  };
});
