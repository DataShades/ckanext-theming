/**
 * change-submit.js
 * ===============
 * Automatically submits a form when a 'change' event is detected.
 *
 * Usage:
 * <form data-theming-module="change-submit" data-change-submit-selector="select">
 *   <select name="sort">...</select>
 * </form>
 *
 * Configuration:
 * data-change-submit-selector: (Optional) CSS selector to filter which elements
 *                              trigger the submission. If omitted, any change
 *                              within the container triggers it.
 */

class ChangeSubmit {
  constructor(element) {
    this.root = element;
    this.form = element.tagName === 'FORM' ? element : element.closest('form');
    this.selector = element.dataset.changeSubmitSelector || null;

    this._onChange = this._onChange.bind(this);
  }

  init() {
    if (!this.form) {
      console.warn('ChangeSubmit: No parent form found for', this.root);
      return;
    }
    this.root.addEventListener('change', this._onChange);
  }

  _onChange(event) {
    // If a selector is provided, only submit if the target matches
    if (this.selector && !event.target.matches(this.selector)) {
      return;
    }

    this.form.requestSubmit();
  }

  destroy() {
    this.root.removeEventListener('change', this._onChange);
  }
}

// Auto-init
document
  .querySelectorAll('[data-theming-module|="change-submit"]')
  .forEach(el => new ChangeSubmit(el).init());
