/**
 * autocomplete.js
 * ===============
 * Theme-agnostic Autocomplete.
 *
 * Works on an <input> element carrying [data-module="theming-autocomplete"].
 * The input itself is the visible combobox.
 *
 * ── Data attributes ───────────────────────────────────────────────────────
 *
 *   data-module-container-id   (required) id of chips container
 *
 *   data-module-source         URL for ajax mode. Query spliced at
 *                              last "?": /api?q=&x=1 → /api?{q}&x=1
 *                              Absent or empty → static mode.
 *
 *   data-module-options        JSON for static mode.
 *                              Items: {"value":"py","text":"Python"}
 *                              or plain string "Python" (value=text).
 *
 *   data-module-selected       JSON pre-selection.
 *
 *   data-module-id-key         Response key for value. Default: "value"
 *   data-module-label-key      Response key for label. Default: "text"
 *
 *   data-module-allow-new      "true" → offer "Create: …" on no match
 *   data-module-allow-multiple "true" → multi-select chip mode
 *   data-module-joined         "true" → submit as one joined hidden field
 *   data-module-separator      Separator for joined mode. Default: ","
 *   data-module-min-chars      Min chars before suggestions. Default: 1/2
 *   data-module-debounce       Ajax debounce ms. Default: 300
 *
 * ── Custom events (fire on the combobox input, bubble up) ─────────────────
 *
 *   autocomplete:select   detail: { value, label, isNew }
 *   autocomplete:remove   detail: { value, label }
 *   autocomplete:change   detail: { values: [{value, label}, …] }
 *
 * ── Keyboard (WCAG 2.1 combobox) ──────────────────────────────────────────
 *
 *   Printable char / ArrowDown  open + filter
 *   ArrowDown / ArrowUp         navigate options
 *   Home / End                  first / last option
 *   Enter                       select focused option
 *   Escape                      close, clear typed text
 *   Backspace (empty input)     remove last chip (multiple mode)
 *   Tab                         close (natural focus flow)
 */

ckan.module("theming-autocomplete", () => {
  return {
    options: {
      source: null,
      containerId: null,
      allowMultiple: false,
      allowNew: false,
      joined: false,
      idKey: "value",
      labelKey: "text",
      separator: ",",
      minChars: null,
      debounce: 300,
      options: [],
      selected: [],
    },

    initialize() {
      this.root = this.el[0];
      this.combobox = this.root;

      this._setupOptions();
      this._parseStaticAndInitialSelections();
      this._resetRuntimeState();

      // Find the autocomplete root
      this.autocompleteRoot = this.root.closest("[data-theming-autocomplete-root]");
      this._addedRootAttribute = false;
      if (!this.autocompleteRoot) {
        this.autocompleteRoot = this.root.parentElement;
        if (this.autocompleteRoot) {
          this.autocompleteRoot.setAttribute("data-theming-autocomplete-root", "");
          this._addedRootAttribute = true;
        }
      }

      this._bindHandlers();

      if (!this._createDOMElements()) return;

      this._bindEvents();
      this._hydrate();

      this.combobox.classList.add("theming-autocomplete--ready");
    },

    teardown() {
      this._unbindEvents();

      if (this.listbox) this.listbox.remove();
      if (this.storage) this.storage.remove();
      if (this.liveStatus) this.liveStatus.remove();
      if (this._addedSelections && this.selections) this.selections.remove();

      if (this._addedRootAttribute && this.autocompleteRoot) {
        this.autocompleteRoot.removeAttribute("data-theming-autocomplete-root");
      }

      if (this.root) this.root.name = this.name;
      this._removeComboboxAttributes();
    },

    // ── Setup & Scaffolding ──────────────────────────────────────────────────

    _setupOptions() {
      this.source = this.options.source || null;
      this.containerId = this.options.containerId;
      this.isMultiple = this.options.allowMultiple === true || this.options.allowMultiple === "true";
      this.allowNew = this.options.allowNew === true || this.options.allowNew === "true";
      this.isJoined = this.options.joined === true || this.options.joined === "true";

      this.idKey = this.options.idKey ?? "value";
      this.labelKey = this.options.labelKey ?? "text";

      this.separator = this.options.separator ?? ",";
      this.minChars = parseInt(
        this.options.minChars ?? (this.source ? "2" : "0"),
        10,
      );
      this.debounce = parseInt(this.options.debounce ?? "300", 10);
    },

    _parseStaticAndInitialSelections() {
      this._staticOptions = [];
      const rawOptions = this.options.options;
      if (!this.source && Array.isArray(rawOptions)) {
        this._staticOptions = rawOptions.map((item) =>
          typeof item === "string"
            ? { [this.idKey]: item, [this.labelKey]: item }
            : item,
        );
      }

      this._initialSelection = [];
      let selected = this.options.selected;
      if (Array.isArray(selected)) {
        if (this.isJoined && selected.length === 1 && typeof selected[0] === "string") {
          selected = selected[0].split(this.separator).filter(Boolean);
        }
        this._initialSelection = selected.map((v) =>
          typeof v === "string" ? { [this.idKey]: v, [this.labelKey]: v } : v,
        );
      }
    },

    _resetRuntimeState() {
      this.storage = null;
      this.listbox = null;
      this.selections = null;
      this.noResults = null;
      this.createOption = null;
      this.liveStatus = null;

      this._open = false;
      this._activeIdx = -1;
      this._fetchCtrl = null;
      this._selections = [];
      this._prevStorageValue = null;
    },

    _bindHandlers() {
      this._onInput = this._onInput.bind(this);
      this._onKeydown = this._onKeydown.bind(this);
      this._onFocus = this._onFocus.bind(this);
      this._onListboxClick = this._onListboxClick.bind(this);
      this._onChipClick = this._onChipClick.bind(this);
      this._onDocClick = this._onDocClick.bind(this);
      this._reposition = this._reposition.bind(this);
      this._debouncedFetch = this._debounce(
        this._fetchOptions.bind(this),
        this.debounce,
      );
    },

    _createDOMElements() {
      this.selections = this.containerId ? document.getElementById(this.containerId) : null;
      this._addedSelections = false;

      if (!this.selections) {
        if (!this.containerId) {
          this.containerId = (this.combobox.id || "autocomplete") + "-chips";
        }
        this.selections = document.createElement("div");
        this.selections.id = this.containerId;
        this.selections.className = "theming-autocomplete__chips";
        this.selections.setAttribute("hidden", "");

        // Append immediately after the autocomplete input element (this.root)
        this.root.after(this.selections);
        this._addedSelections = true;
      }

      this.name = this.root.name;
      this.root.name = ""; // prevent raw text from being submitted

      this._createStorageElement();
      this._setupComboboxAttributes();
      this._createListboxElement();
      this._createLiveStatusElement();

      return true;
    },

    _createStorageElement() {
      if (!this.isJoined) {
        this.storage = document.createElement("select");
        if (this.isMultiple) this.storage.multiple = true;
        this.storage.style.display = "none";
      } else {
        this.storage = document.createElement("input");
        this.storage.type = "hidden";
      }
      this.storage.name = this.name;
      this.root.after(this.storage);

      this._prevStorageValue = this._getStorageValue();
    },

    _setupComboboxAttributes() {
      this.combobox.setAttribute("role", "combobox");
      this.combobox.setAttribute("aria-autocomplete", "list");
      this.combobox.setAttribute("aria-expanded", "false");
      this.combobox.setAttribute("aria-haspopup", "listbox");
      this.combobox.setAttribute("autocomplete", "off");
      this.combobox.setAttribute("spellcheck", "false");
    },

    _createListboxElement() {
      const listboxId = (this.combobox.id || this.containerId) + "-listbox";
      this.listbox = document.createElement("ul");
      this.listbox.id = listboxId;
      this.listbox.className = "autocomplete__listbox";
      this.listbox.setAttribute("role", "listbox");
      this.listbox.setAttribute(
        "aria-label",
        this.combobox.getAttribute("aria-label") || this.name,
      );
      this.listbox.setAttribute(
        "aria-multiselectable",
        this.isMultiple ? "true" : "false",
      );
      this.listbox.setAttribute("hidden", "");
      document.body.appendChild(this.listbox);

      // Anchor <li>s
      this.createOption = document.createElement("li");
      this.createOption.hidden = true;
      this.createOption.setAttribute("role", "option");
      this.createOption.setAttribute("aria-selected", "false");
      this.createOption.className = "autocomplete__create-option";
      this.listbox.appendChild(this.createOption);

      this.noResults = document.createElement("li");
      this.noResults.innerHTML = "<em>No results</em>";
      this.noResults.hidden = true;
      this.noResults.setAttribute("role", "option");
      this.noResults.setAttribute("aria-selected", "false");
      this.noResults.setAttribute("aria-disabled", "true");
      this.noResults.className = "autocomplete__no-results";
      this.listbox.appendChild(this.noResults);
    },

    _createLiveStatusElement() {
      this.liveStatus = document.createElement("div");
      this.liveStatus.className = "autocomplete__live-status";
      // Screen-reader visually hidden utility styles
      this.liveStatus.style.position = "absolute";
      this.liveStatus.style.width = "1px";
      this.liveStatus.style.height = "1px";
      this.liveStatus.style.padding = "0";
      this.liveStatus.style.margin = "-1px";
      this.liveStatus.style.overflow = "hidden";
      this.liveStatus.style.clip = "rect(0, 0, 0, 0)";
      this.liveStatus.style.border = "0";
      this.liveStatus.setAttribute("aria-live", "polite");
      this.liveStatus.setAttribute("aria-atomic", "true");
      document.body.appendChild(this.liveStatus);
    },

    _hydrate() {
      // Hydrate pre-selections silently
      this._initialSelection.forEach((item) => {
        const value = item[this.idKey];
        let label = item[this.labelKey];
        if (label === value) {
          const found = this._staticOptions.find((o) => o[this.idKey] === value);
          if (found) label = found[this.labelKey];
        }
        this._addSelection(value, label, false, true);
      });
    },

    _removeComboboxAttributes() {
      if (this.combobox) {
        this.combobox.removeAttribute("role");
        this.combobox.removeAttribute("aria-autocomplete");
        this.combobox.removeAttribute("aria-expanded");
        this.combobox.removeAttribute("aria-haspopup");
        this.combobox.removeAttribute("aria-activedescendant");
        this.combobox.classList.remove("theming-autocomplete--ready");
      }
    },

    // ── Public API ────────────────────────────────────────────────────────────

    select(value, label) {
      this._addSelection(String(value), String(label));
    },
    remove(value) {
      this._removeSelection(String(value));
    },
    value() {
      return [...this._selections];
    },

    // ── Events ────────────────────────────────────────────────────────────────

    _bindEvents() {
      this.combobox.addEventListener("input", this._onInput);
      this.combobox.addEventListener("keydown", this._onKeydown);
      this.combobox.addEventListener("focus", this._onFocus);
      this.listbox.addEventListener("click", this._onListboxClick);
      this.selections.addEventListener("click", this._onChipClick);
      document.addEventListener("click", this._onDocClick);
      window.addEventListener("resize", this._reposition);
    },

    _unbindEvents() {
      if (this.combobox) {
        this.combobox.removeEventListener("input", this._onInput);
        this.combobox.removeEventListener("keydown", this._onKeydown);
        this.combobox.removeEventListener("focus", this._onFocus);
      }
      if (this.listbox) {
        this.listbox.removeEventListener("click", this._onListboxClick);
      }
      if (this.selections) {
        this.selections.removeEventListener("click", this._onChipClick);
      }
      document.removeEventListener("click", this._onDocClick);
      window.removeEventListener("resize", this._reposition);
    },

    _onFocus() {
      if (this.combobox.value.length >= this.minChars) {
        this._suggest(this.combobox.value);
      }
    },

    _onInput() {
      const q = this.combobox.value;
      if (q.length < this.minChars) {
        return true;
      }
      this.source ? this._debouncedFetch(q) : this._suggest(q);
    },

    _onKeydown(e) {
      const { key } = e;
      const options = this._visibleOptions();

      switch (key) {
        case "ArrowDown":
          e.preventDefault();
          if (!this._open) {
            this._suggest(this.combobox.value);
            break;
          }
          this._setActive(
            Math.min(this._activeIdx + 1, options.length - 1),
            options,
          );
          break;

        case "ArrowUp":
          e.preventDefault();
          this._setActive(Math.max(this._activeIdx - 1, 0), options);
          break;

        case "Home":
          if (this._open) {
            e.preventDefault();
            this._setActive(0, options);
          }
          break;

        case "End":
          if (this._open) {
            e.preventDefault();
            this._setActive(options.length - 1, options);
          }
          break;

        case "Enter":
          e.preventDefault();
          if (this._open && this._activeIdx >= 0 && options[this._activeIdx]) {
            this._selectOption(options[this._activeIdx]);
          }
          break;

        case "Escape":
          this._close();
          this.combobox.value = "";
          break;

        case "Backspace":
          if (
            this.combobox.value === "" &&
            this.isMultiple &&
            this._selections.length > 0
          ) {
            this._removeSelection(
              this._selections[this._selections.length - 1][this.idKey],
            );
          }
          break;

        case "Tab":
          this._close();
          break;

        default:
          break;
      }
    },

    _onListboxClick(e) {
      const opt = e.target.closest('[role="option"]');
      if (!opt || opt.getAttribute("aria-disabled") === "true") return;
      e.preventDefault();
      this._selectOption(opt);
    },

    _onChipClick(e) {
      const btn = e.target.closest(".autocomplete__chip-remove");
      if (!btn) return;
      const chip = btn.closest(".autocomplete__chip");
      if (chip) this._removeSelection(chip.dataset.value);
    },

    _onDocClick(e) {
      if (!this.combobox.contains(e.target) && !this.listbox.contains(e.target)) {
        this._close();
      }
    },

    // ── Static filter ─────────────────────────────────────────────────────────

    _suggest(query) {
      const q = query.trim().toLowerCase();
      const excluded = new Set(this._selections.map((s) => s[this.idKey]));

      const matched = this._staticOptions.filter((opt) => {
        if (this.isMultiple && excluded.has(opt[this.idKey])) return false;
        const display = String(
          opt[this.labelKey] ?? opt[this.idKey] ?? "",
        ).toLowerCase();
        return display.includes(q);
      });

      this._renderOptions(matched, query);
    },

    // ── Ajax fetch ────────────────────────────────────────────────────────────

    async _fetchOptions(query) {
      if (this._fetchCtrl) this._fetchCtrl.abort();
      this._fetchCtrl = new AbortController();

      const q = encodeURIComponent(query);
      const idx = this.source.lastIndexOf("?");
      const url = idx >= 0
        ? this.source.slice(0, idx) + q + this.source.slice(idx + 1)
        : this.source + q;

      this._setLoadingState(true);

      try {
        const res = await fetch(url, { signal: this._fetchCtrl.signal });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        let data = await res.json();
        if (data?.ResultSet?.Result) data = data.ResultSet.Result;

        const excluded = new Set(this._selections.map((s) => s[this.idKey]));
        const opts = data
          .map((item) =>
            typeof item === "string"
              ? { [this.idKey]: item, [this.labelKey]: item }
              : item,
          )
          .filter((opt) => !(this.isMultiple && excluded.has(opt[this.idKey])));

        this._renderOptions(opts, query);
      } catch (err) {
        if (err.name !== "AbortError") {
          console.error("Autocomplete fetch error:", err);
          this._renderOptions([], query);
        }
      } finally {
        if (!this._fetchCtrl || this._fetchCtrl.signal.aborted) {
          this._setLoadingState(false);
        }
      }
    },

    _setLoadingState(isLoading) {
      if (isLoading) {
        this.combobox.classList.add("autocomplete--loading");
        this.combobox.setAttribute("aria-busy", "true");
      } else {
        this.combobox.classList.remove("autocomplete--loading");
        this.combobox.removeAttribute("aria-busy");
      }
    },

    // ── Render Helpers ────────────────────────────────────────────────────────

    _renderOptions(opts, query) {
      this._clearOptions();

      const q = query.trim();
      this._buildOptionElements(opts, q);
      this._updateStatusElements(opts, q);
      this._announceStatus(opts.length);

      this._open = true;
      this.listbox.removeAttribute("hidden");
      this._reposition();

      this.combobox.setAttribute("aria-expanded", "true");
    },

    _clearOptions() {
      if (this.listbox) {
        this.listbox.querySelectorAll(".autocomplete__option").forEach((el) => el.remove());
      }
      this._activeIdx = -1;
      if (this.combobox) {
        this.combobox.removeAttribute("aria-activedescendant");
      }
    },

    _buildOptionElements(opts, q) {
      const prefix = this.combobox.id || this.containerId;
      opts.forEach((opt, i) => {
        const value = opt[this.idKey];
        const label = opt[this.labelKey] ?? value;
        const li = document.createElement("li");
        li.className = "autocomplete__option";
        li.id = `${prefix}-opt-${i}`;
        li.setAttribute("role", "option");
        li.setAttribute("aria-selected", "false");
        li.dataset.value = value;
        li.dataset.label = label;
        li.innerHTML = this._highlight(String(label), q);
        this.listbox.insertBefore(li, this.createOption);
      });
    },

    _updateStatusElements(opts, q) {
      const hasResults = opts.length > 0;
      this.noResults.hidden = hasResults || (this.allowNew && q.length > 0);
      this.createOption.hidden = !(this.allowNew && q.length > 0 && !hasResults);

      if (!this.createOption.hidden) {
        this.createOption.textContent = `Create: "${q}"`;
        this.createOption.dataset.value = q;
        this.createOption.dataset.label = q;
        this.createOption.dataset.isNew = "true";
      }
    },

    _announceStatus(count) {
      if (!this.liveStatus) return;
      if (count === 0) {
        this.liveStatus.textContent = this.allowNew && this.combobox.value.trim().length > 0
          ? "No matching options. Select to create new."
          : "No results found.";
      } else {
        this.liveStatus.textContent = `${count} result${count === 1 ? "" : "s"} found. Use up and down arrows to review.`;
      }
    },

    _reposition() {
      if (!this._open || !this.listbox || !this.root) return;
      const rect = this.root.getBoundingClientRect();
      this.listbox.style.left = rect.x.toFixed(0) + "px";
      this.listbox.style.width = rect.width.toFixed(0) + "px";

      if (rect.y > window.innerHeight / 2) {
        this.listbox.style.bottom = (window.innerHeight - window.scrollY - rect.y).toFixed(0) + "px";
        this.listbox.style.top = "auto";
      } else {
        this.listbox.style.top = (window.scrollY + rect.y + rect.height).toFixed(0) + "px";
        this.listbox.style.bottom = "auto";
      }
    },

    _highlight(label, query) {
      if (!query) return this._escape(label);
      const idx = label.toLowerCase().indexOf(query.toLowerCase());
      if (idx < 0) return this._escape(label);
      return (
        this._escape(label.slice(0, idx)) +
        `<strong>${this._escape(
          label.slice(idx, idx + query.length),
        )}</strong>` +
        this._escape(label.slice(idx + query.length))
      );
    },

    _escape(str) {
      return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#x27;");
    },

    // ── Selection management ──────────────────────────────────────────────────

    _selectOption(optEl) {
      const value = optEl.dataset.value;
      const label = optEl.dataset.label ?? optEl.textContent.trim();
      const isNew = optEl.dataset.isNew === "true";

      if (!this.isMultiple) {
        this._selections = [];
      }

      this._addSelection(value, label, isNew);
      this._close();
      if (this.isMultiple) {
        this.combobox.value = "";
      }
    },

    _addSelection(value, label, isNew = false, silent = false) {
      if (
        this.isMultiple &&
        this._selections.some((s) => s[this.idKey] === value)
      ) {
        return;
      }

      this._selections.push({ [this.idKey]: value, [this.labelKey]: label });

      if (this.isMultiple) {
        this._renderChip(value, label);
        this.selections.removeAttribute("hidden");
      } else {
        this.combobox.value = label;
      }

      this._syncHiddenFields(silent);

      if (!silent) {
        this.combobox.dispatchEvent(
          new CustomEvent("autocomplete:select", {
            bubbles: true,
            detail: { value, label, isNew },
          }),
        );
        this._dispatchChange();
      }
    },

    _removeSelection(value) {
      const item = this._selections.find((s) => s[this.idKey] === value);
      if (!item) return;

      this._selections = this._selections.filter((s) => s[this.idKey] !== value);

      if (this.isMultiple) {
        this.selections
          .querySelector(`.autocomplete__chip[data-value="${CSS.escape(value)}"]`)
          ?.remove();
        if (this._selections.length === 0) {
          this.selections.setAttribute("hidden", "");
        }
      } else {
        this.combobox.value = "";
      }

      this._syncHiddenFields();

      this.combobox.dispatchEvent(
        new CustomEvent("autocomplete:remove", {
          bubbles: true,
          detail: { value, label: item[this.labelKey] },
        }),
      );
      this._dispatchChange();
    },

    _dispatchChange() {
      this.combobox.dispatchEvent(
        new CustomEvent("autocomplete:change", {
          bubbles: true,
          detail: {
            values: this._selections.map((s) => ({
              value: s[this.idKey],
              label: s[this.labelKey],
            })),
          },
        }),
      );
    },

    _renderChip(value, label) {
      const chip = document.createElement("div");
      chip.className = "autocomplete__chip";
      chip.dataset.value = value;
      chip.innerHTML = `
      <span class="autocomplete__chip-label">${this._escape(label)}</span>
      <button type="button" class="autocomplete__chip-remove"
              aria-label="Remove ${this._escape(label)}">
        <span aria-hidden="true">&times;</span>
      </button>`;
      this.selections.appendChild(chip);
    },

    // ── Storage sync ──────────────────────────────────────────────────────────

    _getStorageValue() {
      if (!this.storage) return null;
      if (this.isJoined) return this.storage.value;
      if (this.storage.tagName === "SELECT") {
        return Array.from(this.storage.options)
          .filter((o) => o.selected)
          .map((o) => o.value)
          .join(",");
      }
      return this.storage.value;
    },

    _syncHiddenFields(silent = false) {
      if (this.isJoined) {
        this.storage.value = this._selections
          .map((s) => s[this.idKey])
          .join(this.separator);
      } else if (this.storage.tagName === "SELECT") {
        this.storage.innerHTML = "";
        this._selections.forEach((sel) => {
          const opt = document.createElement("option");
          opt.value = sel[this.idKey];
          opt.text = sel[this.labelKey];
          opt.selected = true;
          this.storage.appendChild(opt);
        });
      } else {
        // Single non-joined hidden input
        this.storage.value = this._selections.length
          ? this._selections[0][this.idKey]
          : "";
      }

      const currentVal = this._getStorageValue();
      if (currentVal !== this._prevStorageValue) {
        this._prevStorageValue = currentVal;
        if (!silent) {
          this.storage.dispatchEvent(new Event("change", { bubbles: true }));
        }
      }
    },

    _close() {
      this.listbox.setAttribute("hidden", "");
      this.combobox.setAttribute("aria-expanded", "false");
      this.combobox.removeAttribute("aria-activedescendant");
      this._open = false;
      this._activeIdx = -1;
      if (this._fetchCtrl) {
        this._fetchCtrl.abort();
        this._fetchCtrl = null;
      }
      this._setLoadingState(false);

      // If not multiple, ensure combobox value matches current selection
      if (!this.isMultiple) {
        this.combobox.value = this._selections.length
          ? this._selections[0][this.labelKey]
          : "";
      } else {
        this.combobox.value = "";
      }
    },

    _visibleOptions() {
      return Array.from(
        this.listbox.querySelectorAll(
          '[role="option"]:not([hidden]):not([aria-disabled="true"])',
        ),
      );
    },

    _setActive(idx, options) {
      if (!options.length) return;
      const clamped = Math.max(0, Math.min(idx, options.length - 1));

      if (this._activeIdx >= 0 && options[this._activeIdx]) {
        options[this._activeIdx].classList.remove("autocomplete__option--active");
        options[this._activeIdx].setAttribute("aria-selected", "false");
      }

      this._activeIdx = clamped;
      const active = options[clamped];
      active.classList.add("autocomplete__option--active");
      active.setAttribute("aria-selected", "true");
      this.combobox.setAttribute("aria-activedescendant", active.id);
      active.scrollIntoView({ block: "nearest" });
    },

    _debounce(fn, wait) {
      let timer;
      return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => fn(...args), wait);
      };
    },
  };
});
