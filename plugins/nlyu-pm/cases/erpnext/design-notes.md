# ERPNext design notes

## Established visual patterns

ERPNext screens are Frappe "Desk" screens, so nearly every pattern is inherited. The pinned commits are ERPNext v16 (v16.0.0 released 2026-01-12, v16.35.0 on 2026-09-15). At 1440x900 you will see:

- A persistent left shell in two parts. ERPNext ships a Dock record (`erpnext/dock/erpnext/erpnext.json`), so a slim icon rail sits at the far left with the app logo, search, notifications with an unread badge, one icon per module sidebar (Stock is `package`, Buying is `shopping-cart`), and the user button; the rail can collapse to icons only. Next to it is the 220px body sidebar (`--sidebar-width`) whose header names the current module and whose rows are that module's links grouped by section (for Stock: transactions, Tools, Setup, Reports). There is no top bar; the only element above the page is an optional announcement strip.
- Home is a grid of desktop icons, one per module; clicking Stock or Buying opens that module's sidebar and workspace page. Workspaces are blocks of number cards, charts, shortcuts, and quick lists.
- Forms are centered at `--page-max-width: 900px`. The user Settings dialog (`ui/user_settings_dialog.js`) offers a compact or full width choice for forms; full width adds `body.full-width` and the choice persists per browser in local storage.
- List views: page head with title, view switcher, and primary action; a saved-layout dropdown (Default Layout, then global and personal layouts) with the filter controls sitting above the rows; 30px rows (`--list-row-height`), checkbox column, and a coloured status indicator per row set by the doctype's `*_list.js`, for example Draft, To Receive and Bill, Completed, Cancelled.
- Form views: page head with title, status and primary action; fields in tabs and sections; child tables (item lines) as an inline editable grid; a right-hand sidebar for assignments, tags and attachments; an activity timeline at the bottom recording saves, submits, comments and workflow actions.
- Submittable documents move Draft, Submitted, then Cancelled or Amended; amending creates a new numbered version rather than editing history.
- Base font is Inter, 16px root size. Light and dark themes switch via a `data-theme` attribute.
- The "Espresso" token set (colours, spacing, typography, shadows, borders, `.es-*` components such as `.es-badge`) is the current system; `.indicator-pill` is marked deprecated.

## Where the design system lives

Paths are relative to the sparse clone; "Verified" means confirmed at the pinned commit.

Frappe (companion), Desk CSS and tokens:
- `frappe/public/scss/espresso/`: `_colors`, `_spacing`, `_typography`, `_shadows`, `_borders` token partials. Verified.
- `frappe/public/css/espresso/`: compiled token CSS (`colors.css`, `spacing.css`, `typography.css`, `radius.css`, `effects.css`) and `components/`. Verified.
- `frappe/public/scss/common/css_variables.scss` and `frappe/public/scss/desk/css_variables.scss`: CSS variables for padding, margins, page max width (`--page-max-width: 900px`), input height, list row height (`--list-row-height: 30px`), breakpoints (`--xxl-width: 1440px`). Verified.
- `frappe/public/scss/desk/`: per-surface styles: `sidebar.scss`, `sidebar_header.scss`, `sidebar_panel.scss`, `dock.scss`, `desktop.scss`, `list.scss`, `filters.scss`, `form.scss`, `form_sidebar.scss`, `timeline.scss`, `dark.scss`. Verified.
- `frappe/public/scss/common/indicator.scss`, `buttons.scss`, `controls.scss`, `modal.scss`: status indicators, buttons, inputs, dialogs. Verified.

Frappe, shared JS components:
- `frappe/public/js/frappe/form/`: `form.js`, `toolbar.js`, `grid.js`, `workflow.js`, `sidebar/`, `footer/form_timeline.js`, `controls/`. Verified.
- `frappe/public/js/frappe/list/`: `list_view.js`, `list_filter/` (saved layouts menu), `list_settings.js`. Verified.
- `frappe/public/js/frappe/ui/`: `page.js`, `dialog.js`, `sidebar/` (`sidebar.js`, `sidebar_header.js`, `sidebar_panel.js`, `dock.js`), `toolbar/` (search dialog and the full-width toggle), `notifications/`, `theme_switcher.js`. Verified.
- `frappe/public/js/frappe/views/workspace/`: workspace rendering, with `blocks/number_card.js`, `blocks/chart.js`, `blocks/shortcut.js`. Verified.

Frappe, icons:
- `frappe/public/icons/lucide/icons.svg` (SVG sprite) and `frappe/public/icons/desktop_icons/`. Verified.

ERPNext (primary), module-specific UI:
- `erpnext/public/scss/erpnext.scss`: small overrides only. Verified.
- `erpnext/public/js/controllers/` and `erpnext/public/js/utils/`: shared stock and buying form behaviour, including the serial/batch selector dialog. Verified.
- `erpnext/public/icons/desktop_icons/` and `erpnext/public/images/`: module icons and illustrations. Verified.
- `erpnext/dock/erpnext/erpnext.json`, `erpnext/workspace_sidebar/*.json`, `erpnext/desktop_icon/*.json`: the rail entries, per-module sidebar links, and home icons ERPNext ships. Verified.

Public docs for the Desk UI: https://docs.frappe.io/framework/user/en/desk/, https://docs.frappe.io/framework/user/en/desk/workspace, and https://docs.frappe.io/framework/user/en/guides/desk. Release notes for the pinned major version: https://github.com/frappe/erpnext/releases/tag/v16.0.0.

## Public UI references

- Public demo site (opens on a login page). https://erpnext-demo.frappe.cloud/
- Purchase order form walkthrough. https://docs.frappe.io/erpnext/user/manual/en/purchase-order
- Stock entry form walkthrough. https://docs.frappe.io/erpnext/user/manual/en/stock-entry
- Workspace and sidebar customisation. https://docs.frappe.io/erpnext/user/manual/en/workspace
- Workflow states and actions on a form. https://docs.frappe.io/erpnext/user/manual/en/workflows
- Stock reconciliation walkthrough. https://docs.frappe.io/erpnext/user/manual/en/stock-reconciliation
- Serial and batch bundle. https://docs.frappe.io/erpnext/user/manual/en/serial-and-batch-bundle

## Synthetic data guidance

Use one fictional company, "Harborline Supply Co.", throughout. Warehouses: Main Store, Receiving Bay, Quarantine, Returns. Items: codes like `ITM-0042`, generic descriptions ("M8 hex bolt, zinc"), fake batch numbers. Suppliers: invented names ("Kestrel Fasteners Ltd"), no real addresses. Purchase orders: `PUR-ORD-2026-00017` style numbers, round quantities, one fictional currency. Users: fictional people with real ERPNext role names (Stock User, Stock Manager, Purchase User, Purchase Manager). Never use real supplier names, price lists, barcodes, or colleagues.

## Prototype scope reminders

- One single-file HTML prototype per lane: inline CSS and JS, no build step or external dependencies.
- Cover one main path plus two alternate states (empty, error, or another role's view).
- Lay out for 1440x900; do not design for mobile.
- Match the Desk's shape (persistent left sidebar, page head, list or form body, no top bar) so reviewers recognise it; visual similarity is not a completion gate.
- Do not copy CSS, JS, or icon files from either repository; approximate them.
