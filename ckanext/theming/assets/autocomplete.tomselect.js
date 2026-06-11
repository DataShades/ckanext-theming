/**
 * themes/tomselect/autocomplete.js
 * ==================================
 * Tom Select adapter for the autocomplete component.
 *
 * ── How it fits the new structure ────────────────────────────────────────
 *
 * The macro emits one of two shapes depending on serialisation:
 *
 *   Multi / single (default):
 *     <div id="{id}-chips" class="theming-autocomplete__chips"></div>
 *     <select class="autocomplete__select"
 *             data-theming-module="autocomplete"
 *             data-autocomplete-container-id="{id}-chips"
 *             name="…" [multiple]>
 *       <option value="">placeholder</option>
 *       <option value="py" selected>Python</option>
 *     </select>
 *
 *   Joined / CSV mode:
 *     <div id="{id}-chips" class="theming-autocomplete__chips"></div>
 *     <input type="text"
 *            class="autocomplete__select"
 *            data-theming-module="autocomplete"
 *            data-autocomplete-container-id="{id}-chips"
 *            data-autocomplete-joined="true"
 *            data-autocomplete-separator=","
 *            name="…" value="py,js">
 *
 * This adapter's element (this.root) IS the <select> or <input>.
 * Tom Select is initialised directly on it.
 * Events fire on this.root.
 *
 * ── Auto-init ─────────────────────────────────────────────────────────────
 *
 *   document.querySelectorAll('[data-theming-module="autocomplete"]')
 *     .forEach(el => new TomSelectAutocomplete(el).init())
 *
 *   NSW.Autocomplete = TomSelectAutocomplete
 *
 * ── Data attributes (all on the <select> or <input>) ──────────────────────
 *
 *   Shared with base adapter:
 *     data-autocomplete-container-id     id of chips div (used as dropdown parent)
 *     data-autocomplete-source           ajax URL (absent → static)
 *     data-autocomplete-allow-new        "true" → Tom Select create mode
 *     data-autocomplete-allow-multiple   "true" OR native [multiple] attr
 *     data-autocomplete-id-key           option key for value  (default "value")
 *     data-autocomplete-label-key        option key for label  (default "text")
 *     data-autocomplete-min-chars        minimumInputLength for ajax
 *     data-autocomplete-debounce         ajax load debounce ms
 *     data-autocomplete-joined           "true" → delimiter mode on <input>
 *     data-autocomplete-separator        delimiter character
 *
 *   Tom Select-specific (safe to ignore in other adapters):
 *     data-ts-plugins     JSON array of plugin names, e.g. '["remove_button"]'
 *     data-ts-max-items   max selectable items (absent → unlimited for multiple, 1 for single)
 *     data-ts-max-options max options shown in dropdown (default 50)
 *     data-ts-render      JSON map of render function names, e.g. '{"option":"myFn"}'
 *                         Functions are resolved from window[name] at init time.
 *
 * ── Custom events (fire on the element, bubble up) ────────────────────────
 *
 *   autocomplete:select   detail: { value, label, isNew }
 *   autocomplete:remove   detail: { value, label }
 *   autocomplete:change   detail: { values: [{value, label}, …] }
 *
 * ── Joined / CSV mode ─────────────────────────────────────────────────────
 *
 *   Tom Select natively supports a `delimiter` option on <input type="text">.
 *   When the macro emits an <input> (joined mode), Tom Select handles the
 *   delimited string submission natively — no shim required.
 *
 * ── Dependency ────────────────────────────────────────────────────────────
 *   TomSelect must be available as window.TomSelect or imported first.
 *   https://tom-select.js.org
 */

class TomSelectAutocomplete {

  constructor(element) {
    // element is the <select> or <input> directly
    this.root = element

    this.TomSelect = window.TomSelect
    if (!this.TomSelect) throw new Error('TomSelectAutocomplete requires TomSelect')

    // Shared contract
    this.containerId = this.root.dataset.autocompleteContainerId
    this.source      = this.root.dataset.autocompleteSource || null
    this.isAjax      = !!this.source
    this.allowNew    = this.root.dataset.autocompleteAllowNew === 'true'
    // Multiple: prefer data attr; fall back to native [multiple] on <select>
    this.isMultiple  = this.root.dataset.autocompleteAllowMultiple === 'true'
                       || (this.root.tagName === 'SELECT' && this.root.multiple)
    this.idKey       = this.root.dataset.autocompleteIdKey    ?? 'value'
    this.labelKey    = this.root.dataset.autocompleteLabelKey ?? 'text'
    this.minChars    = parseInt(this.root.dataset.autocompleteMinChars ?? (this.isAjax ? '2' : '0'), 10)
    this.debounce    = parseInt(this.root.dataset.autocompleteDebounce ?? '300', 10)
    this.isJoined    = this.root.dataset.autocompleteJoined === 'true'
    this.separator   = this.root.dataset.autocompleteSeparator ?? ','

    // Tom Select-specific
    this.tsPlugins    = JSON.parse(this.root.dataset.tsPlugins    || '[]')
    this.tsMaxItems   = this.root.dataset.tsMaxItems
                        ? parseInt(this.root.dataset.tsMaxItems, 10)
                        : null
    this.tsMaxOptions = parseInt(this.root.dataset.tsMaxOptions ?? '50', 10)
    this.tsRender     = this.root.dataset.tsRender
                        ? JSON.parse(this.root.dataset.tsRender)
                        : null

    this.instance = null
  }

  // ── Lifecycle ─────────────────────────────────────────────────────────────

  init() {
    const config = this._buildConfig()
    this.instance = new this.TomSelect(this.root, config)
    this._bindEvents()
    this.root.classList.add('theming-autocomplete--ready')
  }

  destroy() {
    if (this.instance) {
      this.instance.destroy()
      this.instance = null
    }
    this.root.classList.remove('theming-autocomplete--ready')
  }

  // ── Public API ────────────────────────────────────────────────────────────

  select(value, label) {
    if (!this.instance) return
    if (!this.instance.options[value]) {
      this.instance.addOption({ [this.idKey]: value, [this.labelKey]: label })
    }
    this.instance.addItem(String(value), /* silent= */ true)
  }

  remove(value) {
    if (!this.instance) return
    this.instance.removeItem(String(value), /* silent= */ true)
  }

  get value() {
    if (!this.instance) return []
    return this.instance.items.map(v => {
      const opt = this.instance.options[v]
      return {
        value: String(v),
        label: opt ? (opt[this.labelKey] ?? opt.text ?? String(v)) : String(v),
      }
    })
  }

  // ── Private: config builder ───────────────────────────────────────────────

  _buildConfig() {
    const isInputMode = this.root.tagName === 'INPUT'   // joined / CSV mode

    // Resolve the dropdown parent — Tom Select appends its dropdown to <body>
    // by default; scoping it to the container keeps CSS and z-index sane.
    const container = this.containerId
      ? document.getElementById(this.containerId)
      : this.root.parentElement

    const cfg = {
      // Tom Select uses "value" and "text" keys internally regardless of
      // our idKey/labelKey config — we normalise in the load function and
      // the valueField/labelField options bridge the two.
      valueField:   'value',
      labelField:   'text',
      searchField:  ['text'],

      plugins:     this.tsPlugins.length ? this.tsPlugins
                   : this.isMultiple ? ['remove_button'] : [],
      maxItems:    this.tsMaxItems ?? (this.isMultiple ? null : 1),
      maxOptions:  this.tsMaxOptions,
      create:      this.allowNew,
      openOnFocus: true,

      // Scope the dropdown panel to our container element
      ...(container ? { dropdownParent: container } : {}),

      // Joined/CSV mode: delimiter on <input type="text">
      ...(isInputMode && this.isJoined ? {
        delimiter: this.separator,
        persist:   false,
      } : {}),
    }

    // Custom render functions resolved from window scope
    if (this.tsRender) {
      cfg.render = {}
      for (const [key, fnName] of Object.entries(this.tsRender)) {
        if (typeof window[fnName] === 'function') cfg.render[key] = window[fnName]
      }
    }

    if (this.isAjax) {
      cfg.load      = this._buildLoadFn()
      cfg.shouldLoad = query => query.length >= this.minChars
      cfg.preload   = false
    } else {
      // Static options already in the DOM — Tom Select reads them automatically.
      // Disable the load callback entirely.
      cfg.shouldLoad = () => false
    }

    return cfg
  }

  _buildLoadFn() {
    // Tom Select calls load(query, callback) — we replicate the base adapter's
    // URL-splicing convention and key normalisation.
    return (query, callback) => {
      if (query.length < this.minChars) { callback(); return }

      // Splice query at last "?": /api?q=&lang=en → /api?{query}&lang=en
      const q   = encodeURIComponent(query)
      const idx = this.source.lastIndexOf('?')
      const url = idx >= 0
        ? this.source.slice(0, idx) + q + this.source.slice(idx + 1)
        : this.source + q

      fetch(url)
        .then(res => { if (!res.ok) throw new Error(`HTTP ${res.status}`); return res.json() })
        .then(data => {
          // Yahoo envelope unwrap — matches base adapter
          if (data?.ResultSet?.Result) data = data.ResultSet.Result

          // Normalise to Tom Select's internal {value, text} shape
          const opts = data.map(item =>
            typeof item === 'string'
              ? { value: item, text: item }
              : { value: item[this.idKey], text: item[this.labelKey] ?? item[this.idKey] }
          )
          callback(opts)
        })
        .catch(err => {
          console.error('TomSelectAutocomplete fetch error:', err)
          callback()
        })
    }
  }

  // ── Private: event bridge ─────────────────────────────────────────────────

  _bindEvents() {
    this.instance.on('item_add', (value) => {
      const opt   = this.instance.options[value]
      const label = opt ? (opt[this.labelKey] ?? opt.text ?? String(value)) : String(value)
      // Tom Select sets opt.$order on created tags; there's no reliable
      // public "isNew" flag — check if option existed before the item was added.
      const isNew = !!opt?.created

      this.root.dispatchEvent(new CustomEvent('autocomplete:select', {
        bubbles: true,
        detail:  { value: String(value), label, isNew },
      }))
      this._dispatchChange()
    })

    this.instance.on('item_remove', (value) => {
      const opt   = this.instance.options[value]
      const label = opt ? (opt[this.labelKey] ?? opt.text ?? String(value)) : String(value)

      this.root.dispatchEvent(new CustomEvent('autocomplete:remove', {
        bubbles: true,
        detail:  { value: String(value), label },
      }))
      this._dispatchChange()
    })
  }

  _dispatchChange() {
    this.root.dispatchEvent(new CustomEvent('autocomplete:change', {
      bubbles: true,
      detail:  { values: this.value },
    }))
  }
}


// ── Auto-init ─────────────────────────────────────────────────────────────────
document
  .querySelectorAll('[data-theming-module="autocomplete-tomselect"]')
  .forEach((el) => new TomSelectAutocomplete(el).init());
