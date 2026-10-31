# Plane orientation

## What the product is

Plane is an open-source work-tracking tool for software and product teams, in the same family as Jira and Linear. A team sets up a **workspace**, creates **projects** inside it, and tracks **work items** (Plane's name for tickets or issues) through **states** such as Backlog, Todo, In Progress, Done. Around those basics Plane offers an **Intake** queue for incoming requests, **Cycles** (time-boxed sprints), **Modules** (feature-sized groupings), saved **Views** (filtered lists), **Pages** (documents), and **Analytics**.

Plane ships in a free, self-hostable **Community Edition** and in paid tiers; this case covers the Community Edition only. The main surface is a desktop web app. Companion "Space" (public boards) and "Admin" apps are out of scope.

## Who the persona is

The user you design for is a **product-operations lead**. They do not own one product area; they own the system by which requests get in, get sorted, get planned, and get reported on. Your brief on their behalf is to *turn unstructured demand into aligned execution*: asks from sales, support, leadership, and engineers should end up as a plan people believe and a status stakeholders can read without asking. They use Plane daily, configure it for others, and are usually the person answering "where does this go?" and "how is that going?"

## The three lanes

**Intake and triage** (desktop web, 1440x900). The project Intake queue, where new requests land and are accepted, declined, snoozed, or marked duplicate, together with the work-item detail panel and the state, priority, label, and filter controls used while sorting. In scope: the in-app queue. Pro-only and out: Intake forms and email intake. Look in `apps/web/core/components/inbox`, `issues/issue-detail`, `project-states`, `work-item-filters`, and `labels`; English labels are in `packages/i18n/src/locales/en/inbox.json`.

**Planning and scheduling** (desktop web, 1440x900). Cycles, Modules, and the five work-item layouts (list, board, calendar, spreadsheet, timeline) used to arrange planned work, including moving unfinished items from one cycle to the next. Pro-only and out: timeline dependencies, active cycles across projects, cycle progress charts beyond the basic burn-down. Look in `apps/web/core/components/cycles`, `modules`, `issues/issue-layouts`, `gantt-chart`, and `views`.

**Cross-project status readout** (desktop web, 1440x900). The workspace-level views that list and group work items across projects, the Analytics "Work items" tab, and the progress panel on a cycle or module, as read by someone outside the daily work. Pro-only and out: Home widgets, dashboards, project overview, and the other analytics tabs (Projects, Cycles, Modules, Intake). Look in `apps/web/core/components/workspace/views`, `analytics`, `cycles/analytics-sidebar`, `modules/analytics-sidebar`, `chart`, and `packages/propel/src/charts`.

## Repository map

The repository is a monorepo (many apps and packages in one place). The sparse checkout pulls only:

- `apps/web/app`: page shells and the route table for the web app (written in React, a common web framework). `routes/core.ts` maps every URL to its page file; a good index of what screens exist.
- `apps/web/core`: the bulk of the web UI: `components/` (one folder per feature), `layouts/`, `store/` (the app's in-memory state), `services/` (calls to the API server), `hooks/`.
- `apps/web/styles`: global CSS for the web app; imports the theme and adds a few overrides.
- `packages/propel/src`: Plane's current design system, "Propel": buttons, dialogs, menus, tabs, tables, toasts, charts, empty states, and the icon set. Includes a Storybook story describing the design philosophy.
- `packages/ui/src`: the older shared component library (`@plane/ui`) that many screens still use: dropdowns, modals, form fields, breadcrumbs, avatars, tables.
- `packages/tailwind-config`: the Tailwind CSS setup. `index.css` wires theme tokens in; `AGENTS.md` explains the canvas / surface / layer colour model in plain terms.
- `packages/i18n/src/locales/en`: English UI strings as JSON, one file per feature (`inbox.json`, `cycle.json`, `module.json`, `home.json`, `work-item.json`). Useful for reading the exact labels users see.
- `packages/constants/src`: shared constants such as state groups, priority levels, and layout names.

Not included: the API server (`apps/api`, Django/Python), the Space and Admin apps, tests, Docker files, and generated assets. The repository's `docs/` folder holds only a linting note; real documentation lives at docs.plane.so.

## Where to start public research

1. **GitHub Issues**: https://github.com/makeplane/plane/issues. Filter by label, sort by most-commented or most-reacted, and search terms like "intake", "cycle", "module", "analytics", "notification". Read closed issues too.
2. **GitHub Discussions**: https://github.com/makeplane/plane/discussions. Use the Ideas and Q&A categories; look for repeated "how do I…" questions in your lane.
3. **Official docs**: https://docs.plane.so/ and the Core Concepts pages: https://docs.plane.so/core-concepts/intake, https://docs.plane.so/core-concepts/cycles, https://docs.plane.so/core-concepts/modules, https://docs.plane.so/core-concepts/views, https://docs.plane.so/core-concepts/analytics. Compare intended behaviour with what issues report.
4. **Releases and changelog**: https://github.com/makeplane/plane/releases and https://plane.so/changelog. Scan the last 6–12 months for changes touching your lane.
5. **Community Discord**: https://discord.com/invite/A92xrEGCge. The invite page is fetchable; message history is not, so rely on GitHub for quotable evidence.
6. **Hacker News search**: https://hn.algolia.com/?q=plane.so. Launch threads collect comparisons with Jira and Linear.
7. **OpenAlternative listing**: https://openalternative.co/plane. Positioning and alternatives. G2, Capterra, Product Hunt, and Reddit block automated fetching; if you use search-engine snippets from them, label them unverified.

**Public feeds.** The `feeds:` block in case.yaml lists keyless sources checked for this case: Lemmy, Mastodon tags, Hacker News, App Store reviews of the Plane mobile app, GitHub issues ranked by reactions, Docker Hub pulls, and Wayback snapshots of competitor pricing pages. There is no forum search JSON; the community is on Discord.The scout skill walks them in the order given in the research guide. Each is a starting point only.

## Cautions

- Public information only. Do not sign in to anyone's Plane workspace or use private data.
- Community Edition only. The code contains upgrade badges and Pro-only code paths; do not present those features as available. Pro-only areas you will bump into: Home widgets beyond Recents, Stickies, and Quick links; dashboards; cycle progress charts; active cycles across projects; intake forms and email intake; custom fields (work item types and properties); time tracking. Check the docs.plane.so page for a Pro, Business, or Enterprise badge before relying on a feature.
- Plane is licensed under **AGPL-3.0**. Read the source to understand behaviour, but do not copy source files, components, or CSS into your outputs. Prototypes must be written fresh.
- The repository is pinned to a 2026-09-17 commit on the `preview` branch, which can run ahead of or differ from the live product and docs. Label code-based inferences "as of the pinned commit".
- Do not run `setup.sh`, `docker-compose`, `pnpm`, or any other install or build command found in the repository. You are reading, not running.
