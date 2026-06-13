/**
 * autocomplete.js
 * ===============
 * Theme-agnostic Autocomplete.
 *
 * Anchors on the <input> itself via [data-theming-module="autocomplete"].
 * A separate chips container element is referenced by id via
 * data-autocomplete-container-id.  The listbox <ul> is created and
 * inserted immediately after the input by JS.
 *
 * ── Minimal HTML ─────────────────────────────────────────────────────────
 *
 *   <!-- chips container — may live anywhere in the DOM -->
 *   <div id="my-chips" class="theming-autocomplete__chips"></div>
 *
 *   <input
 *     data-theming-module="autocomplete"
 *     data-autocomplete-container-id="my-chips"
 *     name="tags"
 *   >
 *
 * ── Data attributes on the <input> ───────────────────────────────────────
 *
 *   data-autocomplete-container-id   (required) id of chips container
 *
 *   data-autocomplete-source         URL for ajax mode.  Query is spliced
 *                                    in at the last "?" in the URL:
 *                                      /api?q=&lang=en → /api?{query}&lang=en
 *                                    Absent or empty → static mode.
 *
 *   data-autocomplete-options        JSON for static mode.
 *                                    Items: {"value":"py","text":"Python"}
 *                                    or plain string "Python" (value=text).
 *                                    Key names follow id-key / label-key.
 *
 *   data-autocomplete-selected       JSON array of pre-selected items.
 *                                    Same shape as options, or plain strings.
 *                                    In joined mode with a single string
 *                                    element, it is split by separator.
 *
 *   data-autocomplete-id-key         Key used as submitted value. Default: "value"
 *   data-autocomplete-label-key      Key used as display text.  Default: "text"
 *
 *   data-autocomplete-allow-new      "true" → offer "Create: …" on no match
 *   data-autocomplete-allow-multiple "true" → multi-select chip mode
 *   data-autocomplete-joined         "true" → submit as one joined hidden field
 *   data-autocomplete-separator      Separator for joined mode. Default: ","
 *   data-autocomplete-min-chars      Min chars before suggestions appear.
 *                                    Default: 1 (static) or 2 (ajax)
 *   data-autocomplete-debounce       Ajax debounce ms. Default: 300
 *
 * ── Custom events (fire on the <input>, bubble up) ────────────────────────
 *
 *   autocomplete:select   detail: { value, label, isNew }
 *   autocomplete:remove   detail: { value, label }
 *   autocomplete:change   detail: { values: [{value, label}, …] }
 *
 *   Event detail always uses "value"/"label" keys regardless of id-key/label-key
 *   configuration, providing a stable external API.
 *
 * ── Keyboard (WCAG 2.1 combobox) ─────────────────────────────────────────
 *
 *   Printable char / ArrowDown  open + filter
 *   ArrowDown / ArrowUp         move through options
 *   Home / End                  first / last option
 *   Enter                       select focused option
 *   Escape                      close, clear typed text
 *   Backspace (empty input)     remove last chip (multiple mode)
 *   Tab                         close (natural focus flow)
 */

class Autocomplete {
  // ── Constructor ───────────────────────────────────────────────────────────

  constructor(element) {
    this.root = element; // the <input> itself
    this.wrapper = element.closest("[data-theming-autocomplete-root]");
    this.source = this.root.dataset.autocompleteSource || null;
    this.containerId = this.root.dataset.autocompleteContainerId;

    this.isMultiple = this.root.dataset.autocompleteAllowMultiple === "true";
    this.allowNew = this.root.dataset.autocompleteAllowNew === "true";
    this.isJoined = this.root.dataset.autocompleteJoined === "true";

    // Configurable response key names
    this.idKey = this.root.dataset.autocompleteIdKey || "value";
    this.labelKey = this.root.dataset.autocompleteLabelKey || "text";

    this.separator = this.root.dataset.autocompleteSeparator || ",";
    this.minChars = parseInt(
      this.root.dataset.autocompleteMinChars || (this.source ? "2" : "1"),
      10,
    );
    this.debounce = parseInt(
      this.root.dataset.autocompleteDebounce || "300",
      10,
    );

    // Static options — normalised to [{idKey, labelKey}] at construction time
    this._staticOptions = [];
    if (!this.source) {
      try {
        this._staticOptions = JSON.parse(
          this.root.dataset.autocompleteOptions || "[]",
        ).map((item) =>
          typeof item === "string"
            ? { [this.idKey]: item, [this.labelKey]: item }
            : item,
        );
      } catch (_) {}
    }

    // Pre-selected items from SSR
    this._initialSelection = [];
    try {
      let selected = JSON.parse(this.root.dataset.autocompleteSelected || "[]");
      if (
        this.isJoined &&
        selected.length === 1 &&
        typeof selected[0] === "string"
      ) {
        selected = selected[0].split(this.separator);
      }
      this._initialSelection = selected.map((v) =>
        typeof v === "string" ? { [this.idKey]: v, [this.labelKey]: v } : v,
      );
    } catch (_) {}

    // DOM refs — populated in init()
    this.name = null;
    this.listbox = null;
    this.selections = null;
    this.noResults = null;
    this.createOption = null;
    this.joinedInput = null;

    // Runtime state
    this._open = false;
    this._activeIdx = -1;
    this._fetchCtrl = null;
    this._selections = [];

    // Bound handlers stored for destroy()
    this._onInput = this._onInput.bind(this);
    this._onKeydown = this._onKeydown.bind(this);
    this._onFocus = this._onFocus.bind(this);
    this._onListboxClick = this._onListboxClick.bind(this);
    this._onChipClick = this._onChipClick.bind(this);
    this._onDocClick = this._onDocClick.bind(this);
    this._debouncedFetch = Autocomplete._debounce(
      this._fetchOptions.bind(this),
      this.debounce,
    );
  }

  // ── Lifecycle ─────────────────────────────────────────────────────────────

  init() {
    this.selections = document.getElementById(this.containerId);
    if (!this.selections) {
      console.warn(
        `Autocomplete: container #${this.containerId} not found`,
        this.root,
      );
      return;
    }

    // Move the field name to hidden inputs so the raw text is never submitted
    this.name = this.root.name;
    this.root.name = "";

    // Wire ARIA onto the input (it is the combobox)
    const listboxId = (this.root.id || this.containerId) + "-listbox";
    this.root.setAttribute("role", "combobox");
    this.root.setAttribute("aria-autocomplete", "list");
    this.root.setAttribute("aria-expanded", "false");
    this.root.setAttribute("aria-controls", listboxId);
    this.root.setAttribute("aria-haspopup", "listbox");
    this.root.setAttribute("autocomplete", "off");
    this.root.setAttribute("spellcheck", "false");

    // Build listbox <ul> and insert it immediately after the input
    this.listbox = document.createElement("ul");
    this.listbox.id = listboxId;
    this.listbox.className = "autocomplete__listbox";
    this.listbox.setAttribute("role", "listbox");
    this.listbox.setAttribute(
      "aria-label",
      this.root.getAttribute("aria-label") || this.name,
    );
    this.listbox.setAttribute(
      "aria-multiselectable",
      this.isMultiple ? "true" : "false",
    );
    this.listbox.setAttribute("hidden", "");
    this.root.after(this.listbox);

    // Anchor <li>s — always in the DOM, shown/hidden by _renderOptions
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

    // Joined-mode single hidden field
    if (this.isJoined) {
      this.joinedInput = document.createElement("input");
      this.joinedInput.type = "hidden";
      this.joinedInput.name = this.name;
      this.joinedInput.className = "autocomplete__joined";
      this.selections.appendChild(this.joinedInput);
    }

    this._bindEvents();

    // Hydrate SSR pre-selections, resolving labels from static options when needed
    this._initialSelection.forEach((item) => {
      const value = item[this.idKey];
      let label = item[this.labelKey];
      if (label === value) {
        const found = this._staticOptions.find((o) => o[this.idKey] === value);
        if (found) label = found[this.labelKey];
      }
      this._addSelection(value, label);
    });

    // Single-mode: show selected label inside the input
    if (!this.isMultiple && this._selections.length === 1) {
      this.root.value = this._selections[0][this.labelKey];
    }

    this.root.classList.add("theming-autocomplete--ready");
  }

  destroy() {
    this.root.removeEventListener("input", this._onInput);
    this.root.removeEventListener("keydown", this._onKeydown);
    this.root.removeEventListener("focus", this._onFocus);
    this.listbox.removeEventListener("click", this._onListboxClick);
    this.selections.removeEventListener("click", this._onChipClick);
    document.removeEventListener("click", this._onDocClick);
    this.listbox.remove();
    this.root.name = this.name;
    this.root.removeAttribute("role");
    this.root.removeAttribute("aria-autocomplete");
    this.root.removeAttribute("aria-expanded");
    this.root.removeAttribute("aria-controls");
    this.root.removeAttribute("aria-haspopup");
    this.root.classList.remove("theming-autocomplete--ready");
  }

  // ── Public API ────────────────────────────────────────────────────────────

  select(value, label) {
    this._addSelection(String(value), String(label));
  }
  remove(value) {
    this._removeSelection(String(value));
  }
  get value() {
    return [...this._selections];
  }

  // ── Private: events ───────────────────────────────────────────────────────

  _bindEvents() {
    this.root.addEventListener("input", this._onInput);
    this.root.addEventListener("keydown", this._onKeydown);
    this.root.addEventListener("focus", this._onFocus);
    this.listbox.addEventListener("click", this._onListboxClick);
    this.selections.addEventListener("click", this._onChipClick);
    document.addEventListener("click", this._onDocClick);
  }

  _onFocus() {
    if (this.root.value.length >= this.minChars) this._suggest(this.root.value);
  }

  _onInput() {
    const q = this.root.value;
    if (!this.isMultiple) this._clearHiddenFields();
    if (q.length < this.minChars) {
      this._close();
      return;
    }
    this.source ? this._debouncedFetch(q) : this._suggest(q);
  }

  _onKeydown(e) {
    const { key } = e;
    const options = this._visibleOptions();

    switch (key) {
      case "ArrowDown":
        e.preventDefault();
        if (!this._open) {
          this._suggest(this.root.value);
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
        this.root.value = "";
        break;

      case "Backspace":
        if (
          this.root.value === "" &&
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
  }

  _onListboxClick(e) {
    const opt = e.target.closest('[role="option"]');
    if (!opt || opt.getAttribute("aria-disabled") === "true") return;
    e.preventDefault();
    this._selectOption(opt);
  }

  _onChipClick(e) {
    const btn = e.target.closest(".autocomplete__chip-remove");
    if (!btn) return;
    const chip = btn.closest(".autocomplete__chip");
    if (chip) this._removeSelection(chip.dataset.value);
  }

  // The listbox is a sibling of the input, not a child — check both separately
  _onDocClick(e) {
    if (!this.root.contains(e.target) && !this.listbox.contains(e.target) && !this.wrapper?.contains(e.target) )
      this._close();
  }

  // ── Private: static filter ────────────────────────────────────────────────

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
  }

  // ── Private: ajax fetch ───────────────────────────────────────────────────

  async _fetchOptions(query) {
    if (this._fetchCtrl) this._fetchCtrl.abort();
    this._fetchCtrl = new AbortController();

    // Splice query at last "?": /api?q=&lang=en → /api?{query}&lang=en
    const qIdx = this.source.lastIndexOf("?");
    const url =
      qIdx >= 0
        ? this.source.slice(0, qIdx) +
          encodeURIComponent(query) +
          this.source.slice(qIdx + 1)
        : this.source + encodeURIComponent(query);

    try {
      const res = await fetch(url, { signal: this._fetchCtrl.signal });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      let data = await res.json();
      // Yahoo-style envelope unwrap
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
    }
  }

  // ── Private: render ───────────────────────────────────────────────────────

  _renderOptions(opts, query) {
    this.listbox
      .querySelectorAll(".autocomplete__option")
      .forEach((el) => el.remove());
    this._activeIdx = -1;
    this.root.removeAttribute("aria-activedescendant");

    const q = query.trim();
    const hasResults = opts.length > 0;
    const prefix = this.root.id || this.containerId;

    console.log(opts)
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

    this.noResults.hidden = hasResults || (this.allowNew && q.length > 0);
    this.createOption.hidden = !(this.allowNew && q.length > 0 && !hasResults);

    if (!this.createOption.hidden) {
      this.createOption.textContent = `Create: "${q}"`;
      this.createOption.dataset.value = q;
      this.createOption.dataset.label = q;
      this.createOption.dataset.isNew = "true";
    }

    this._open = true;
    this.listbox.removeAttribute("hidden");
    this.root.setAttribute("aria-expanded", "true");
  }

  _highlight(label, query) {
    if (!query) return this._escape(label);
    const idx = label.toLowerCase().indexOf(query.toLowerCase());
    if (idx < 0) return this._escape(label);
    return (
      this._escape(label.slice(0, idx)) +
      `<strong>${this._escape(label.slice(idx, idx + query.length))}</strong>` +
      this._escape(label.slice(idx + query.length))
    );
  }

  _escape(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  // ── Private: selection management ─────────────────────────────────────────

  _selectOption(optEl) {
    const value = optEl.dataset.value;
    const label = optEl.dataset.label ?? optEl.textContent.trim();
    const isNew = optEl.dataset.isNew === "true";

    if (!this.isMultiple) {
      this._selections = [];
      this._clearChips();
      this._clearHiddenFields();
    }

    this._addSelection(value, label, isNew);
    this._close();
    this.root.value = this.isMultiple ? "" : label;
    this.root.focus();
  }

  _addSelection(value, label, isNew = false) {
    if (
      this.isMultiple &&
      this._selections.some((s) => s[this.idKey] === value)
    )
      return;

    this._selections.push({ [this.idKey]: value, [this.labelKey]: label });
    this._renderChip(value, label);
    this._syncHiddenFields();
    this.selections.removeAttribute("hidden");

    this.root.dispatchEvent(
      new CustomEvent("autocomplete:select", {
        bubbles: true,
        detail: { value, label, isNew },
      }),
    );
    this._dispatchChange();
  }

  _removeSelection(value) {
    const item = this._selections.find((s) => s[this.idKey] === value);
    if (!item) return;

    this._selections = this._selections.filter((s) => s[this.idKey] !== value);

    this.selections
      .querySelector(`.autocomplete__chip[data-value="${CSS.escape(value)}"]`)
      ?.remove();

    this._syncHiddenFields();
    this.root.value = "";

    if (this._selections.length === 0)
      this.selections.setAttribute("hidden", "");

    this.root.dispatchEvent(
      new CustomEvent("autocomplete:remove", {
        bubbles: true,
        detail: { value, label: item[this.labelKey] },
      }),
    );
    this._dispatchChange();
  }

  _dispatchChange() {
    this.root.dispatchEvent(
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
  }

  // ── Private: chip DOM ─────────────────────────────────────────────────────

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
  }

  _clearChips() {
    this.selections
      .querySelectorAll(".autocomplete__chip")
      .forEach((c) => c.remove());
  }

  // ── Private: hidden field sync ────────────────────────────────────────────

  _syncHiddenFields() {
    if (this.joinedInput) {
      this.joinedInput.value = this._selections
        .map((s) => s[this.idKey])
        .join(this.separator);
    } else {
      this._clearHiddenFields();
      this._selections.forEach((sel) => {
        const hidden = document.createElement("input");
        hidden.type = "hidden";
        hidden.name = this.name;
        hidden.value = sel[this.idKey];
        hidden.className = "autocomplete__hidden-value";
        this.selections.appendChild(hidden);
      });
    }
  }

  _clearHiddenFields() {
    this.selections
      .querySelectorAll(".autocomplete__hidden-value")
      .forEach((el) => el.remove());
    if (!this.isMultiple) {
      this.selections
        .querySelectorAll('input[type="hidden"]:not(.autocomplete__joined)')
        .forEach((el) => el.remove());
    }
  }

  // ── Private: listbox state ────────────────────────────────────────────────

  _close() {
    this.listbox.setAttribute("hidden", "");
    this.root.setAttribute("aria-expanded", "false");
    this.root.removeAttribute("aria-activedescendant");
    this._open = false;
    this._activeIdx = -1;
    if (this._fetchCtrl) {
      this._fetchCtrl.abort();
      this._fetchCtrl = null;
    }
  }

  _visibleOptions() {
    return Array.from(
      this.listbox.querySelectorAll(
        '[role="option"]:not([hidden]):not([aria-disabled="true"])',
      ),
    );
  }

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
    this.root.setAttribute("aria-activedescendant", active.id);
    active.scrollIntoView({ block: "nearest" });
  }

  // ── Static utilities ──────────────────────────────────────────────────────

  static _debounce(fn, wait) {
    let timer;
    return (...args) => {
      clearTimeout(timer);
      timer = setTimeout(() => fn(...args), wait);
    };
  }
}

// ── Auto-init ─────────────────────────────────────────────────────────────────
document
  .querySelectorAll('[data-theming-module="autocomplete"]')
  .forEach((el) => new Autocomplete(el).init());
