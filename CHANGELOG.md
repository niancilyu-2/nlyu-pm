# Changelog

All notable changes to the `nlyu-pm` plugin are recorded here. Bump `version` in
`plugins/nlyu-pm/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`
whenever a changed build is distributed, otherwise existing installs will not refresh.
Update the version line in the README banner at the same time.

## 0.9.1 (2026-10-31)

- Product question has two options, BYOP or example case; the easy and advanced split is
  gone. An example case is then chosen from a numbered list of the five products, each
  described from its `case.yaml`, with ERPNext marked advanced; the PM answers with a
  number or a name, because the question tool shows at most four options. Readiness
  pre-selection follows the same shape. Shared rule added for lists of five or more.

## 0.9.0 (2026-10-31)

- New read-only agent `nlyu-pm:discovery-reviewer`, run by `/nlyu-pm:scout` as Step 9
  before the priority check-in. It verifies every quote against the text saved from its
  fetch, confirms every `Evidence` item was fetched in the session, opens every
  constraint's cited line in the code, checks recurrence labels and counter-evidence
  entries, recounts each opportunity's evidence line, and applies a fixed coverage floor
  (two rungs with evidence, five evidence items, two confirmed constraints, one verified
  quote per opportunity). Findings go to `outputs/01-discovery-review.md`; blocking ones
  are fixed, never deferred; a floor not met makes the brief `provisional` with no
  override. Checklist in `resources/discovery-review-checklist.md`, template
  `templates/01-discovery-review.md`.
- Scout saves what every research fetch returns under `.pm/fetches/` (`F-###.txt`,
  `P-###.txt` for pasted material, `S-###.txt` for searches, plus `index.md`) before
  logging from it. Quotes are copied from the saved file and their attribution line ends
  with `from F-###`; evidence items carry `Saved: F-###`. PM-held sources stay unsaved.
- Counter-evidence is earned: every opportunity's evidence line names the fetch that
  looked for the opposite (`SIG-###` or `looked (F-###), none`); "none found" without a
  fetch is not allowed.
- Scout is now 11 steps; status and summary lines updated (`quotes 8/9 verified`,
  `findings 3, blocking 1, all resolved`). `session.yaml` gains
  `stages.discovery.review` and `fetches`; `evidence-review` joins the check-in kinds.
  Shared rule added for saving fetches. README banner counts two reviewer agents.

## 0.8.5 (2026-10-31)

- Priority check-in asks two questions: which opportunity is Now (single choice), then
  why (multi-select, one option per lens, plus the PM's own words). The reason is recorded
  as the picked labels plus anything typed, verbatim. New shared rule: when several answers
  can be true at once, use multi-select and say "pick all that apply"; a reason is never a
  single-choice question with the real answer left to "Other".

## 0.8.4 (2026-10-31)

- BYOP source step. "Where is the code?" offers only URL, folder, or archive, and the
  URL or path is then asked for in plain prose, never as the "Other" box beside "stop for
  now" or "choose an example case instead". New shared rule: a value the PM must type is
  asked for in prose, not with the question tool.

## 0.8.3 (2026-10-31)

- The product question's example-case options are "Example case (Easy)" and "Example case
  (Advanced)" with shorter descriptions; docs say easy instead of core. The `tier: core`
  value in case files is unchanged.

## 0.8.2 (2026-10-31)

- Directory review fixes. The "API key in your own shell" route for sources behind a
  sign-in is removed: Claude never reads a key, token, or variable from the PM's machine.
  Such sources are read through a command-line tool the PM is already signed in to
  (`gh`, `glab`, or one they name) or pasted by the PM. The optional Reddit RSS read is
  described as a plain download. A plugin icon (a loop arrow) is added at `.claude-plugin/icon.png`.

## 0.8.1 (2026-10-31)

- Docs and rules review. The README contents link to Guardrails and limits is fixed;
  the setup guide is described as desktop-first everywhere; the hidden files Finder and
  Explorer create no longer block an empty workspace; runtime messages say "new session"
  instead of "open a terminal"; every "writes only" claim now names the `sources/`
  download; per-skill docs list the same steps the status line counts; track, case, and
  lane are defined; readiness warns about the browser tab and the `/design` question;
  problem tables give the desktop fix first; timings include the BYOP case build.
- Manifests: a display name, shorter descriptions, and searchable keywords for the plugin
  directory. "Learning objective" is now "Stage objective".

## 0.8.0 (2026-10-31)

- Plugin renamed from `pm` to `nlyu-pm` (the name `pm` is taken in Anthropic's plugin
  directory), so commands are `/nlyu-pm:scout`, `/nlyu-pm:prototype`, `/nlyu-pm:prd`, and
  `/nlyu-pm:create-skill`, and the plugin folder is `plugins/nlyu-pm/`. Entries below
  0.8.0 keep the old names they shipped with.
- Desktop-first setup: the Claude desktop app installs the plugin from Settings without
  a terminal; the terminal path stays as an alternative. The plugin folder gains its own
  README and LICENSE for directory submission.
- `/nlyu-pm:create-skill` is now called the skill builder in every doc, status line, and
  template (it was the capstone). The informational `session.yaml` key is
  `stages.skill_builder`.
- Stage summary line. Every stage closes with one line of what the run spent and
  produced (minutes from the recorded start, fetches and searches, item and quote counts,
  gaps, findings, status), repeated in the output file's `Run summary` header row and in
  `stages.<stage>.summary` of `session.yaml`. Token counts and cost are deliberately not
  reported, since Claude cannot observe them; the docs point to `/cost`.
- Repository renamed to `nlyu-pm`; install lines updated. Setup guide rewritten for
  non-technical readers: what you need, a short glossary, subscription and desktop-app
  guidance. The group-run page is removed and
  all wording is product-neutral: the plugin and its docs address a PM working alone or
  with a team.
- Which product, asked up front. The first question `/nlyu-pm:scout` asks (and readiness
  check 7 offers in advance) is which product: *BYOP: bring your own project or repo*,
  the normal path, or an example case to try the workflow on, *core* (Immich, Plane, Home
  Assistant, or Umbraco; a second question picks the product) or *advanced* (ERPNext).
  Example cases explain what a focus area is, then start research right after it is
  chosen. Readiness and case selection never offer more than four
  options per question, so all five example products are visible; the five-row table that
  rendered as four options plus "type something" is gone.
- BYOP. `/nlyu-pm:scout` recognises when Claude was started inside a repository (in-repo mode)
  and otherwise takes a URL, a local folder, or a zip. A new `custom-case.md` procedure
  builds a case package at `.pm/case/` from any repository: README, tree, and manifest
  read; persona, brief, and focus area asked; entry points proposed; research feeds
  derived from the GitHub or GitLab remote and from the forum, app store, and
  competitors the PM names; orientation and design notes written from the code with
  Verified and Inferred labels; a case check-in before research. Before that, three
  source questions: which built-in source groups to use (shown as a plain-words menu),
  anything extra (public JSON, HTML, or RSS, a document in `.pm/inbox/`, a page to paste
  from), and anything behind a sign-in the PM holds. The answers are written to
  `.pm/sources.yaml` during the case build, so the research pass only confirms them. A
  private URL works with the PM's existing credentials (Claude never asks for a token);
  a zip without git history is read as an unpinned archive with a stamp-file change
  check. About fifteen minutes before research starts.
- Sources behind a sign-in (PM-held access). A paid report, a members-only forum, a help
  centre behind single sign-on, or a private issue tracker can be read on any case
  through access the PM holds and sets up themselves: a command-line tool they are
  already signed in to (`gh`, `glab`) or an API key they export in their own shell and
  name to Claude. Claude never asks for, prints, or stores a secret; the PM confirms their
  account permits reading the content that way; items are labelled `Evidence (PM-held
  access)` and listed in the brief. Support tickets, analytics or CRM exports, and
  customer records stay out. CAPTCHA, paywall, and scraping limits are unchanged.
- One case contract. `case-schema.md` states what all three kinds of case share
  (example, BYOP-built, placed by hand). Every stage and the reviewer resolve the case
  through `case.dir` and read code from `sources[].root`, so nothing downstream knows
  which kind it is running on. Source protection compares the PM's own working tree
  against a recorded baseline instead of requiring it to be clean, and never edits a
  tracked file.
- Source overrides on any case. The PM can add any public JSON, HTML, or RSS source, a
  paste-from page, or a public document, drop keys or whole rungs, read some first, and
  raise the budget; scout shows the source plan in plain words before the first fetch,
  then asks. The brief lists what was added and dropped.
- Terminal and API surfaces get a non-graphical prototype shape. Session schema 2, with
  0.7.x files read as before.

## 0.7.7

- PRD opens with a five-sentence Summary for engineering; header splits status, approval,
  and revision; soft caps of 10 requirements and 15 criteria with one observable outcome
  each; success measures name their mechanism or a dependency; persona is the role, not a
  synthetic name. Claude re-checks any new code claim the reviewer makes before proposing
  a disposition.

## 0.7.6

- PRD engineering appendix opens with a Feasibility read: constraints re-checked at their
  line ranges, touchpoints by label, layers not read, engineering-only questions. The
  reviewer checks it is present.

## 0.7.5

- Prototype walkthrough records one row per checklist area, Claude's check and the PM's
  click-through side by side; error states carry role="alert"; no clickable divs. Design
  brief embeds collapsed with demoted headings. When the PM overrides a recommendation,
  Claude asks once for the reason before recording.

## 0.7.4

- Prototype reads only the design paths the case lists and never guesses URLs; a 404 falls
  back to neutral defaults. Umbraco design notes pin the exact UUI token files.

## 0.7.3

- Quotes are Markdown blockquotes with one attribution line beneath, in the brief, at
  check-ins, and in the PRD. Prose paraphrases; composed sentences are never shown in
  quotation marks.

## 0.7.2

- Discovery brief restructured answer-first: the decision (chosen opportunity, your reason,
  the tipping lens, the others and why they wait) comes first, then what was learned, the
  three opportunities in detail, the evidence, assumptions, and the decision record.
  "Claude's reasoning" is now "Reasoning"; decision records use Recommendation and Your
  decision columns.

## 0.7.1

- Each opportunity carries a one-line evidence summary, and the Now recommendation names
  the lens that tipped it and says when it departs from the densest signal.

## 0.7.0

- Lanes re-cut from an evidence audit of each product (forum, GitHub, reviews, release
  history). Immich: lane 2 boundary tightened. Plane: two lanes reshaped so nothing relies
  on Pro-only features. Home Assistant: lanes renamed around household defaults, recovery
  from updates, and automation troubleshooting. Umbraco: media lane narrowed to the picker,
  validation folded into draft-to-publish, localization stands alone. ERPNext: lanes name
  serial and batch handling and reposting, the navigation lane becomes Stock and Buying
  worklists, and notes corrected for v16 general availability.

## 0.6.2

- Check-ins read as plain-language briefings: story first, three themes in a four-line
  shape, quotes, gaps. Tables and rigour vocabulary stay in the draft file. Orientation
  walks through how the chosen lane works in the product today and defines every product
  term. Priority check-in introduces each opportunity as a two-sentence story.

## 0.6.1

- The plugin addresses the PM directly throughout, the stop-after-setup prompt says
  "continue later", the Reddit feed is a PM opt-in, and offline repository copies replace
  shared copies. Group-run material moved out of the plugin into the docs.

## 0.6.0

- Repositioned as a distributable skill package. README is a package front page with a
  flow diagram and a traceability diagram; group-run material split out of the README.
  Manifest descriptions updated.

## 0.5.1

- README rewritten as a PM-facing front page.
- Start time is written into the stage draft and re-read after a resume, so elapsed minutes
  survive a restart. Replies follow the same no-dash, no-arrow rule as files. Walkthrough
  notes the permission prompt when the capstone writes its skill file.

## 0.5.0

- Research rigour: skew per rung and a "Who we heard from" paragraph, counting rules with
  bases and one signal per underlying item, recurrence labels, a counter-evidence fetch per
  theme, and constraints that cite commit, path, line range, and a quoted line marked "to
  confirm with engineering". The PRD stage reopens each constraint before labelling
  anything Verified.

## 0.4.2

- Android reviews: `play_store_page` per case with an Android app; the PM pastes
  reviews from the browser and Claude logs them as PM-pasted evidence.

## 0.4.1

- Capstone repositioned as an independent take-home exercise; time budget adjusted.

## 0.4.0

- Five more keyless sources per case: forum top and per-tag lists, Hacker News comments,
  App Store lookup with release notes, Wikipedia pageviews, and a roadmap rung combining
  the product's own boards with competitors' job postings. Fetch budget raised to 20.
- Scout skill lists every source key and what it gives.

## 0.3.2

- GitHub issues rung falls back to HTML search pages when the shared-IP API limit is hit.

## 0.3.1

- Fixes from a cold-read review and a simulated PM run: drafts live in
  `.pm/drafts/` and are promoted on approval; clone reuse and case-switch handling; fetch
  budget arithmetic for competitor comparisons; coverage-based stop rule; schema and
  ownership corrections; plain-language definitions for repository, pinned commit, sources
  clean, and rung; check-ins capped at about 300 words and the PRD scope check split in two;
  record only observed PM actions; quote answers verbatim.

## 0.3.0

- Quote bank: verbatim user quotes (`QUO-###`) captured during the research pass from
  fetched text only, stored in the discovery file, shown at the priority and flow
  check-ins, and carried into the PRD as a PM-chosen "Voice of the customer" block. The
  reviewer checks quote provenance.

## 0.2.0

- Discovery source ladder: per-case `feeds:` block with verified keyless endpoints (Discourse
  search JSON, GitHub discussions and reaction-ranked issues, Lemmy, Mastodon tags, Hacker
  News, Apple App Store review feeds, adoption counts, Wayback competitor snapshots).
- Triangulation table in the discovery file and research check-in.
- Readiness tests web search separately from fetch and records a Reddit RSS opt-in switch.
- Usage line at the end of every reply: stage, step, budget used, elapsed time, source status.

## 0.1.0

- Initial release: `/pm:scout`, `/pm:prototype`, `/pm:prd`, `/pm:create-skill`.
- Read-only `pm:prd-reviewer` agent.
- Five case packages: Immich, Plane, Home Assistant, Umbraco, ERPNext.
