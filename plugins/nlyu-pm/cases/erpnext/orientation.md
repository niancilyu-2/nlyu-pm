# ERPNext orientation

## What the product is

ERPNext is a free, open-source business management system (an "ERP": software that keeps a company's stock, purchasing, sales, and money records in one place). It runs in a web browser. Its screens are built on the Frappe framework, a separate open-source toolkit that supplies the building blocks of every screen: forms, list views, workflows (approval chains), and role-based permissions (rules about who may see or change a record). Companies self-host it or use the paid Frappe Cloud version. Typical users are small and mid-sized manufacturers, distributors, retailers, and service firms.

You will read both pinned repositories but only propose changes to ERPNext.

## Who the persona is

An inventory or procurement operations manager, holding the ERPNext roles Stock Manager and Purchase Manager, often as one person in a small or mid-sized company. They work in ERPNext most of the day, own the accuracy of stock counts and purchase records, and are the person colleagues escalate to when something looks wrong: a quantity that does not match the shelf, a purchase order stuck waiting for someone, a receipt without paperwork. Their mandate is to resolve those exceptions without weakening controls or auditability: any fix must leave a clear trail of who changed what and why, and must not let anyone bypass required approvals. They know ERPNext's vocabulary (Stock Entry, Material Request, Purchase Order, Workflow) but are not developers.

## The three lanes

**Inventory quantity and valuation exceptions** (`inventory-quantity-and-valuation-exceptions`). Product area: the Stock module as a Stock Manager uses it to check or correct a quantity or valuation: stock entries, stock reconciliations, transfer-type material requests, serial and batch bundles, repost item valuation, and the Stock Ledger, Stock Balance, and Stock Ageing reports. Surface: desktop web at 1440x900. Repo folders: `sources/primary/erpnext/stock/doctype/` (one folder per record type, each with a `.json` layout, `.py` server logic, and `.js` form behaviour), `sources/primary/erpnext/stock/report/`, `sources/primary/erpnext/stock/stock_ledger.py`, and `sources/primary/erpnext/controllers/stock_controller.py`.

**Purchase-approval exceptions** (`purchase-approval-exceptions`). Product area: purchase orders and purchase-type material requests that are stuck in, rejected by, or bypassing an approval step, as a Purchase Manager sees them on ERPNext screens. The Frappe workflow engine and ERPNext Authorization Rule are fixed machinery: read them, do not change them. Surface: desktop web at 1440x900. Repo folders: `sources/primary/erpnext/buying/doctype/`, `sources/primary/erpnext/setup/doctype/authorization_rule/`, `sources/primary/erpnext/controllers/buying_controller.py`, plus `sources/companion/frappe/workflow/`, `sources/companion/frappe/model/workflow.py`, and `sources/companion/frappe/public/js/frappe/form/workflow.js`.

**Stock and Buying daily worklists** (`stock-and-buying-daily-worklists`). Product area: the ERPNext-owned Stock and Buying workspace sidebars, number cards, dashboard charts, and list-view defaults that a Stock Manager or Purchase Manager lands on and moves between during a day, in the v16 persistent-sidebar layout. Role, role profile, and permission configuration are out of scope. Surface: desktop web at 1440x900. Repo folders: `sources/primary/erpnext/workspace_sidebar/`, `sources/primary/erpnext/desktop_icon/`, `sources/primary/erpnext/dock/`, the `workspace/`, `number_card/`, and `dashboard_chart/` folders inside `erpnext/stock` and `erpnext/buying`, `erpnext/setup/workspace/`, the two `*_list.js` files, plus `sources/companion/frappe/public/js/frappe/views/workspace/` and `sources/companion/frappe/public/js/frappe/ui/`.

## Repository map

Both repositories are Python server code plus JavaScript forms; the Desk UI comes from the Frappe framework.

The pinned commits are ERPNext v16 (v16.0.0 released 2026-01-12): a persistent 220px left sidebar carries the app switcher, module links, search, notifications, and the user menu, home is a grid of desktop icons, and there is no top bar apart from an optional announcement strip.

Primary, `sources/primary/` (frappe/erpnext):
- `erpnext/stock`: stock record types, reports, dashboards, and the Stock workspace.
- `erpnext/buying`: purchasing record types, reports, and the Buying workspace.
- `erpnext/setup`: company, item group, UOM, authorization rules, and the home workspace.
- `erpnext/public`: ERPNext's own JavaScript form controllers and small stylesheet additions.
- `erpnext/controllers`: shared server logic that buying and stock documents inherit.
- `erpnext/workspace_sidebar`: JSON definitions of the left sidebar per module.
- `erpnext/desktop_icon`: JSON definitions of module icons on the home screen.
- `erpnext/dock`: JSON definition of the icon rail entries, one per module sidebar.

Companion, `sources/companion/` (frappe/frappe):
- `frappe/public`: Desk JavaScript (forms, lists, toolbar, sidebar, workspaces), SCSS design tokens, and icons.
- `frappe/desk`: server side of forms, lists, workspaces, notifications, and search.
- `frappe/workflow`: the workflow engine record types and the visual workflow builder page.
- `frappe/core`: users, roles, role profiles, permission rules, and the Permission Manager page.
- `frappe/model`: the document lifecycle, including where workflow and permission checks are applied.

The partial download also keeps files directly inside `frappe/`, so `frappe/permissions.py` and `frappe/hooks.py` will appear.

## Where to start public research

1. **Community forum, discuss.frappe.io.** Highest volume of real user questions. Search the lane's nouns ("stock reconciliation", "serial and batch bundle", "repost", "stock balance", "material request", "purchase order workflow", "workspace sidebar", "number card"); sort by latest and read the replies, not just the opening post.
2. **GitHub issues, frappe/erpnext.** Filter by labels `stock` and `buying`; try `is:issue is:open "material request"`. Note which issues were closed as "working as intended" versus fixed.
3. **Official docs, docs.frappe.io/erpnext.** Read the Stock and Buying manual pages for your lane's record types first; they say what the product is supposed to do.
4. **GitHub issues, frappe/frappe.** For workflow, permission, list-view, and sidebar behaviour, search here instead of the ERPNext repo.
5. **Release notes, github.com/frappe/erpnext/releases.** Scan the last few releases for anything touching your lane so you do not propose what already shipped.
6. **Review sites.** Use for tone and recurring themes only; ratings are not evidence.

**Public feeds.** The `feeds:` block in `case.yaml` lists keyless URLs checked with plain HTTP on 2026-09-17: GitHub issue search for both repos (neither has Discussions), discuss.frappe.io `search.json`, Lemmy, the `#erpnext` Mastodon tag, Hacker News, GitHub and Docker Hub adoption counts, and four competitor pricing pages with Wayback lookups. Replace `{query}` with a lane term and `{yyyymmdd}` with a date one year back. The scout skill walks them in the order given in the research guide.

## Cautions

- Use public information only. Do not import data, screenshots, or process descriptions from a real employer or client.
- Excluded topics: tax, payroll, accounting policy, regulatory or compliance claims, anything that changes accounting ledger entries, and country-specific compliance. If a finding leads there, note it and stop.
- ERPNext is GPL-3.0 and Frappe is MIT. That permits reading; it does not permit copying source files, snippets, or icon assets into your outputs. Describe, do not paste.
- Both repositories are pinned at 2026-09-17; the live product, demo, and docs may have moved on. Say which you are describing.
- The repositories contain `bench` commands, install scripts, and setup wizards. Do not run them; you are reading code, not installing an ERP.
- This is the advanced case. Two repositories, a framework layer, and an approval engine mean more places to get lost. Start from your lane's entry points and widen only when a specific question forces you to.
