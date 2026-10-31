# Plane design notes

## Established visual patterns

Plane's web app is a dense, tool-like interface in the Linear tradition: a collapsible left sidebar for navigation, a slim top header with breadcrumbs and view controls, and a main area that switches between list, kanban, calendar, spreadsheet, and gantt layouts. Work items open in a right-hand "peek" panel rather than a new page. Filters live in header dropdowns and appear as removable chips ("applied filters") above the content.

Colour is used sparingly: neutral backgrounds, one accent for primary actions, and small coloured icons for state (backlog, unstarted, started, completed, cancelled) and priority (urgent to none). Text is small (`text-13` body, `text-11` meta); corners are modestly rounded (`rounded-md`). Light, dark, and higher-contrast themes switch via a `data-theme` attribute.

The design system documents a **canvas / surface / layer** model: one app-wide canvas, top-level surfaces side by side, and layers stacking inside a surface for cards, dropdowns, and sidebars. Progress is shown with thin bars, small charts, and count tiles; empty states pair a short explanation with a primary button.

## Where the design system lives

- `packages/propel/src`: current design system "Propel" (`@plane/propel`): button, dialog, menu, tabs, table, toast, badge, pill, skeleton, tooltip, combobox. **Verified** at the pinned SHA.
- `packages/propel/src/design-system/design-system-philosophy.stories.tsx`: Storybook story explaining canvas/surface/layer, text and border tokens. **Verified**.
- `packages/propel/src/icons`: Plane's own icons (state, priority, cycle, module, intake, layouts); `lucide-react` is used elsewhere. **Verified**.
- `packages/propel/src/charts`: bar, line, area, pie, radar, scatter, and tree-map charts built on Recharts. **Verified**.
- `packages/propel/src/empty-state`: shared empty-state component. **Verified**.
- `packages/tailwind-config/index.css`: Tailwind entry importing the tokens; `AGENTS.md` beside it explains the colour model in plain language. **Verified**.
- Token *values* (hex colours, spacing) come from the published `@makeplane/propel` npm package and are **not in the repository** at this commit. Use the token *names* (`bg-surface-1`, `bg-layer-1`, `text-primary`, `text-secondary`, `border-subtle`, `bg-backdrop`) with sensible neutral values.
- `packages/ui/src`: older shared library (`@plane/ui`): dropdowns, modals, form fields, breadcrumbs, avatars. **Verified**.
- `apps/web/styles/globals.css`: app-level CSS and overrides. **Verified**.
- Dark mode: keyed off `[data-theme*="dark"]` and `[data-theme="dark-contrast"]` selectors (comment in `packages/tailwind-config/index.css`). **Verified**.

## Public UI references

- Product home with current screenshots. https://plane.so/
- Intake feature page. https://plane.so/intake
- Cycles feature page. https://plane.so/cycles
- The five work-item layouts, with screenshots. https://docs.plane.so/core-concepts/issues/layouts
- Workspace views page. https://docs.plane.so/core-concepts/views
- Analytics, "Work items" tab; the other tabs are Pro. https://docs.plane.so/core-concepts/analytics

## Synthetic data guidance

- Workspace: an invented company, for example **Northwind Labs** or **Harbor Collective**.
- Projects with short identifiers: **Atlas Mobile (ATL)**, **Billing Revamp (BILL)**, **Support Tooling (SUP)**, **Website (WEB)**.
- Members: invented names with `@example.com` emails, for example Priya Natarajan, Tomás Ferreira, Mei Okafor, Daniel Brandt. Never real Plane staff or contributors.
- Work items: plausible but fictional, for example "ATL-142 Push notifications silently fail on Android 15", "BILL-27 Proration rounding differs from invoice PDF", "SUP-8 Macro editor loses unsaved changes".
- Cycles named by date range ("Cycle 14 · 8–19 Sep"); modules by outcome ("Checkout redesign").
- Never real company data, real customer names, or real incident details.

## Prototype scope reminders

- One self-contained HTML file per prototype (inline CSS and JS; no build step).
- Show one main path end to end, plus two alternate states (for example empty, error, loading, filtered, or a permission-limited view).
- Match the lane viewport: desktop web, **1440×900**. Do not chase responsive behaviour.
- Visual similarity to Plane is not a completion gate. Borrow the layout skeleton and density so the idea reads as "in Plane", then spend the time on flow and copy.
- Do not paste source, CSS, or icons from the repository (AGPL-3.0).
