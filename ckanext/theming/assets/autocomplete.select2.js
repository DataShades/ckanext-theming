/**
 * themes/select2/autocomplete.js
 * ================================
 * Select2 v4 adapter for the autocomplete component.
 *
 * ── How it fits the new structure ────────────────────────────────────────
 *
 * The macro emits:
 *
 *   <div id="{id}-chips" class="theming-autocomplete__chips"></div>
 *
 *   <select class="autocomplete__select"
 *           data-theming-module="autocomplete"
 *           data-autocomplete-container-id="{id}-chips"
 *           name="…" [multiple]>
 *     <option value="">placeholder</option>
 *     <option value="py" selected>Python</option>   ← SSR pre-selection
 *   </select>
 *
 * This adapter's element (this.root) IS the <select>.
 * Select2 is initialised directly on it.
 * Events fire on this.root so they bubble up normally.
 * The chips container is used only to mount the Select2 dropdown parent
 * so that CSS can scope the panel to the local stacking context.
 *
 * ── Auto-init ─────────────────────────────────────────────────────────────
 *
 *   // Replaces or supplements the base auto-init:
 *   document.querySelectorAll('[data-theming-module="autocomplete"]')
 *     .forEach(el => new Select2Autocomplete(el).init())
 *
 *   // Or on the NSW global:
 *   NSW.Autocomplete = Select2Autocomplete
 *
 * ── Data attributes (all on the <select>) ────────────────────────────────
 *
 *   Shared with base adapter:
 *     data-autocomplete-container-id     id of the chips/dropdown parent div
 *     data-autocomplete-source           ajax URL (absent → static)
 *     data-autocomplete-allow-new        "true" → Select2 tags mode
 *     data-autocomplete-allow-multiple   read from native [multiple] attr instead
 *     data-autocomplete-id-key           response key for value  (default "value")
 *     data-autocomplete-label-key        response key for label  (default "text")
 *     data-autocomplete-min-chars        minimumInputLength
 *     data-autocomplete-debounce         ajax delay ms
 *     data-autocomplete-joined           "true" → synthesise joined hidden field
 *     data-autocomplete-separator        separator for joined mode
 *
 *   Select2-specific (safe to ignore in other adapters):
 *     data-s2-theme       Select2 theme name, e.g. "bootstrap-5"
 *     data-s2-width       CSS width of Select2 container (default "100%")
 *     data-s2-close-on-select  "false" to keep dropdown open after pick
 *
 * ── Custom events (fire on the <select>, bubble up) ───────────────────────
 *
 *   autocomplete:select   detail: { value, label, isNew }
 *   autocomplete:remove   detail: { value, label }
 *   autocomplete:change   detail: { values: [{value, label}, …] }
 *
 * ── What is NOT supported ─────────────────────────────────────────────────
 *
 *   joined mode (data-autocomplete-joined):
 *     Select2 submits repeated params natively via the <select>.
 *     When joined=true this adapter synthesises a single joined hidden field
 *     on form submit as a shim — the repeated params are still present.
 *     If your server only reads the joined field, name it appropriately
 *     and ignore the repeated params.
 *
 * ── Dependencies ──────────────────────────────────────────────────────────
 *   jQuery  (Select2 requires it)
 *   Select2 CSS + JS  https://select2.org
 */

class Select2Autocomplete {
  constructor(element) {
    // element is the <select> itself
    this.root = element;

    this.$ = window.jQuery || window.$;
    if (!this.$) throw new Error("Select2Autocomplete requires jQuery");
    if (!this.$.fn.select2)
      throw new Error("Select2Autocomplete requires Select2");

    // Shared data-attribute contract
    this.containerId = this.root.dataset.autocompleteContainerId;
    this.source = this.root.dataset.autocompleteSource || null;
    this.isAjax = !!this.source;
    this.allowNew = this.root.dataset.autocompleteAllowNew === "true";
    // Multiple is read from the native attribute — the macro sets it there
    this.isMultiple = this.root.multiple;
    this.idKey = this.root.dataset.autocompleteIdKey || "value";
    this.labelKey = this.root.dataset.autocompleteLabelKey || "text";
    this.minChars = parseInt(
      this.root.dataset.autocompleteMinChars || (this.isAjax ? "2" : "0"),
      10,
    );
    this.debounce = parseInt(
      this.root.dataset.autocompleteDebounce || "300",
      10,
    );
    this.isJoined = this.root.dataset.autocompleteJoined === "true";
    this.separator = this.root.dataset.autocompleteSeparator || ",";

    // Select2-specific
    this.s2Theme = this.root.dataset.s2Theme || null;
    this.s2Width = this.root.dataset.s2Width || "100%";
    this.closeOnSelect = this.root.dataset.s2CloseOnSelect !== "false";

    this.$root = null; // jQuery wrapper for this.root
    this._joinedInput = null;
  }

  // ── Lifecycle ─────────────────────────────────────────────────────────────

  init() {
    this.$root = this.$(this.root);

    // Resolve the dropdown parent.
    // IMPORTANT: do NOT use the chips container — it carries a `hidden`
    // attribute when empty, and appending Select2's dropdown into a
    // hidden element makes it invisible no matter what CSS says.
    // Use the always-visible wrapper instead.
    const wrapper = this.root.closest("[data-theming-autocomplete-root]");
    const $parent = wrapper ? this.$(wrapper) : this.$root.parent();

    const config = this._buildConfig($parent);
    this.$root.select2(config);

    if (this.isJoined) this._installJoinedShim();

    this._bindEvents();
    this.root.classList.add("theming-autocomplete--ready");
  }

  destroy() {
    this.$root?.select2("destroy");
    this._joinedInput?.remove();
    this._joinedInput = null;
    this.root.classList.remove("theming-autocomplete--ready");
  }

  // ── Public API ────────────────────────────────────────────────────────────

  select(value, label) {
    if (!this.$root) return;
    // For ajax mode ensure the option exists in the <select> before selecting
    if (this.isAjax && !this.$root.find(`option[value="${value}"]`).length) {
      this.$root.append(new Option(label, value, false, false));
    }
    const current = this.$root.val() || [];
    const next = this.isMultiple
      ? [...(Array.isArray(current) ? current : [current]), value]
      : value;
    this.$root.val(next).trigger("change");
  }

  remove(value) {
    if (!this.$root) return;
    const current = this.$root.val() || [];
    const next = Array.isArray(current)
      ? current.filter((v) => v !== value)
      : "";
    this.$root.val(next).trigger("change");
  }

  get value() {
    if (!this.$root) return [];
    const raw = this.$root.val() || [];
    const vals = Array.isArray(raw) ? raw : [raw].filter(Boolean);
    return vals.map((v) => {
      const opt = this.$root.find(`option[value="${v}"]`);
      return { value: String(v), label: opt.length ? opt.text() : String(v) };
    });
  }

  // ── Private: config ───────────────────────────────────────────────────────

  _buildConfig($parent) {
    const placeholderOpt = this.root.querySelector('option[value=""]');

    const cfg = {
      width: this.s2Width,
      placeholder: placeholderOpt?.textContent ?? "Search…",
      allowClear: true,
      closeOnSelect: this.closeOnSelect,
      minimumInputLength: this.minChars,
      tags: this.allowNew,
      dropdownParent: $parent,
    };

    if (this.s2Theme) cfg.theme = this.s2Theme;

    if (this.isAjax) {
      cfg.ajax = {
        // Splice query at last "?" matching base adapter URL convention
        url: (params) => {
          const q = encodeURIComponent(params.term ?? "");
          const idx = this.source.lastIndexOf("?");
          return idx >= 0
            ? this.source.slice(0, idx) + q + this.source.slice(idx + 1)
            : this.source + q;
        },
        dataType: "json",
        delay: this.debounce,
        // URL already contains the query — no extra data params needed
        data: () => ({}),
        processResults: (data) => {
          // Yahoo envelope unwrap — matches base adapter behaviour
          if (data?.ResultSet?.Result) data = data.ResultSet.Result;
          return {
            results: data.map((item) =>
              typeof item === "string"
                ? { id: item, text: item }
                : {
                    id: item[this.idKey],
                    text: item[this.labelKey] ?? item[this.idKey],
                  },
            ),
          };
        },
        cache: true,
      };
    }

    return cfg;
  }

  // ── Private: events ───────────────────────────────────────────────────────

  _bindEvents() {
    this.$root.on("select2:select", (e) => {
      const { id: value, text: label, isTag } = e.params.data;
      this.root.dispatchEvent(
        new CustomEvent("autocomplete:select", {
          bubbles: true,
          detail: {
            value: String(value),
            label: String(label),
            isNew: !!isTag,
          },
        }),
      );
      this._dispatchChange();
    });

    this.$root.on("select2:unselect", (e) => {
      const { id: value, text: label } = e.params.data;
      this.root.dispatchEvent(
        new CustomEvent("autocomplete:remove", {
          bubbles: true,
          detail: { value: String(value), label: String(label) },
        }),
      );
      this._dispatchChange();
    });
  }

  _dispatchChange() {
    this.root.dispatchEvent(
      new CustomEvent("autocomplete:change", {
        bubbles: true,
        detail: { values: this.value },
      }),
    );
  }

  // ── Private: joined-mode shim ─────────────────────────────────────────────

  /**
   * When joined=true: synthesise a single hidden field containing all values
   * joined by separator, updated on every change.
   * The <select> still submits its own repeated params; the server should
   * prefer the joined field if it needs that format.
   */
  _installJoinedShim() {
    const form = this.root.closest("form");
    if (!form) return;

    this._joinedInput = document.createElement("input");
    this._joinedInput.type = "hidden";
    this._joinedInput.name = this.root.name + "__joined";
    form.appendChild(this._joinedInput);

    // Keep it in sync on every selection change
    this.$root.on("select2:select select2:unselect", () => {
      this._joinedInput.value = this.value
        .map((s) => s.value)
        .join(this.separator);
    });
  }
}

// ── Auto-init ─────────────────────────────────────────────────────────────────
document
  .querySelectorAll('[data-theming-module="autocomplete-select2"]')
  .forEach((el) => new Select2Autocomplete(el).init());
