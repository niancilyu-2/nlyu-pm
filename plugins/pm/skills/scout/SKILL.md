---
name: scout
description: Discovery stage of the pm workflow. Compare public customer, market, competitor, and repository evidence for one product, your own (BYOP) or an example case, and choose one opportunity to prototype. Run first; performs the readiness check on first use.
disable-model-invocation: true
---

# /pm:scout (Discovery)

You are guiding a product manager with strong product judgment and limited technical
experience. Read `${CLAUDE_PLUGIN_ROOT}/resources/shared-rules.md` now and follow it for the
whole stage. This skill takes no arguments.

**Learning objective:** use Claude to compare mixed, imperfect evidence while keeping the
prioritisation judgment with the PM.

**Outcome:** `outputs/01-discovery.md` and one PM-selected opportunity.

## Open the stage

Say, in three short lines: *You will practise* comparing imperfect evidence and turning it
into a reasoned priority. *Claude will* find and organise public evidence, show
contradictions, identify repository constraints, and draft options. *You decide* the
problem framing, evidence quality, the selected opportunity, the roadmap order, and the
uncertainty you accept.

Then state the stage boundary from the shared rules. From here on, end every reply with
the usage line described in shared rules section 9 (during readiness use the `Setup ·
check n/8` form) (`Scout · step n/10 · fetches · searches · items · quotes · minutes · sources`).

## Step 1: Readiness and workspace

Read `.pm/session.yaml` if it exists.

- If it does not exist, or `readiness.status` is `not-run` or `blocked`: run the full
  procedure in `${CLAUDE_PLUGIN_ROOT}/resources/readiness.md`, using
  `${CLAUDE_PLUGIN_ROOT}/resources/workspace.md` for folder and clone steps. At the end
  ask whether to stop after setup or continue. If they stop, save and end here.
- Otherwise print `Readiness: <status> on <date>` and continue.

If `stages.discovery.status` is `in-progress` or `approved`, offer **Resume** or
**Restart** as described in `workspace.md`.

## Step 2: Choose the track and the product

The product is either the PM's own (BYOP: bring your own project or repo) or one of five
example cases. Shared rules section 10 explains how the case folder is found; the rest of
the stage reads the case the same way whichever it is. Never put more than four
candidates in one question (shared rules section 3), and no table in the reply.

- **In-repo mode** (`workspace_mode: in-repo`): the product is the repository Claude is
  running in. Say "BYOP: this repository (`<folder name>`)" in one line, set
  `case.source: custom`, and go to Step 2b.
- `.pm/case/case.yaml` already exists: offer to keep it, change its lane, or build fresh
  (`custom-case.md`, "Re-running on the same product"). If it was placed there by hand
  (no `generated: true`), set `case.source: provided`.
- `case.preselected: true`: say in one line what was chosen during setup ("During setup
  you chose Example case: Immich", or "BYOP: <origin>") and ask: keep it, or choose
  again. Keeping an example case goes to Step 3; keeping BYOP goes to Step 2b.
- **Wrapper mode**, otherwise: ask the fork question (header `Product`, "Which product do
  you want to work on?") with exactly these three options, in this order:
  1. **BYOP: bring your own project or repo.** A repository URL (any host; private works
     if this computer already has access), a folder on this computer, or a zip. Claude
     reads it, asks a few questions, and builds the case in about fifteen minutes.
  2. **Example case, core: Immich, Plane, Home Assistant, or Umbraco.** Prepared
     open-source products to try the workflow on, with verified sources and a fixed code
     snapshot, one repository each. Research starts right after you pick a focus area.
  3. **Example case, advanced: ERPNext (two repositories).** Inventory and procurement
     operations in ERPNext, to try the workflow on a larger product. Downloads the
     product and the Frappe framework it runs on.

  BYOP: set `case.source: custom` and go to Step 2b. Core: ask a second question (header
  `Case`, "Which example case?") with the four core products as options, each described
  in one line read from its `case.yaml` (`persona`, then `mandate`) under
  `${CLAUDE_PLUGIN_ROOT}/cases/`; do not write the descriptions from memory. Advanced:
  `case.id: erpnext`; state its persona and mandate in one line. Either way set
  `case.source: prepared` and `case.dir`, then go to Step 3.

### Step 2b: Build the case (BYOP)

Follow `${CLAUDE_PLUGIN_ROOT}/resources/custom-case.md` from Step A to Step J. It gets the
code (clone by URL, or read in place), asks which research sources to use (the built-in
groups, anything extra, anything behind a sign-in the PM holds) and writes
`.pm/sources.yaml`, reads the repository, asks the PM for the user, the brief, and the
focus area, derives the research feeds, writes `.pm/case/`, and ends with a case check-in
(`D-###`, `checkin: case-check`). Then continue at Step 3 with the lane already chosen.

## Step 3: Choose the lane, then orient

For an example case, first say in one line what a lane is: a focus area, one part of the
product you research for about an hour, choose one opportunity in, and prototype as a
single flow; the screen you will prototype comes from it. Then ask for the lane: one
question (header `Focus area`, "Which focus area do you want to work in?"), the three
lanes from `lanes[]`, each described by its `surface` and the first sentence of its
`territory` in plain words. Product and lane are never asked in one question. For BYOP the lane was chosen in `custom-case.md` Step E.
Save `case.id`, `case.source`, `case.dir`, `case.lane`, and `case.chosen_at` to
`session.yaml`.

Before the orientation, define three words in one line each, because they recur all
day: repository (the product's source code, kept in a folder), pinned commit (a fixed
snapshot of that code from a set date), and sources clean (nothing in that folder has
changed). For BYOP, ask in one line whether they want the definitions.
Then give a short orientation from the case's `orientation.md`: what the product is in two
sentences, who the persona is (the user the PM designs for; the PM stays a PM, and the
mandate is their brief on that user's behalf), and how the chosen lane works in this product today, as a
concrete walk-through an editor or operator would recognise ("you write a page, pick the
languages it applies to, and press Save and Publish; a small confirmation appears"). Name
the two or three repository folders most relevant to the lane, and define every product
term you use. Keep it under 250 words. Do not offer opinions about what the problems are.

## Step 4: Acquire the sources

Example case: for each repository in `case.yaml` with a `clone_to`, if `<clone_to>`
already exists and `git rev-parse HEAD` inside it equals `pinned_sha`, reuse it. If it
exists but holds a different case (pre-selected during readiness, changed today), rename
it to `sources/_old-<case id>` and clone fresh, as described in `workspace.md`. Otherwise
follow the clone procedure there. Repositories with `role: web-reference` are not cloned.

BYOP: the code was obtained in Step 2b (shallow clone, or read in place). Nothing more
to fetch.

Record `sources[]` in `session.yaml` with `root` and `method`. Run the source check from
`workspace.md` (empty status for a clone, baseline for an in-place tree) and record
`clean_at_start`.

Set `stage.current: discovery`, `stage.status: in-progress`,
`stages.discovery.status: in-progress`.

## Step 5: Public research pass (the source ladder)

Follow `${CLAUDE_PLUGIN_ROOT}/resources/research-guide.md` exactly. Record the start time.
Tell the PM once what a rung is: one kind of public source, and the ladder is
the order you read them in. Read the `feeds:` block of the case's `case.yaml` (from
`case.dir`), and `.pm/sources.yaml` if it exists. The sources `feeds:` can hold, all
public and keyless (a source behind a sign-in lives only in `.pm/sources.yaml` as
`access: pm-held`; research guide, "Sources behind a sign-in"):

| Key in `feeds:` | What it gives |
|---|---|
| `forum_search_json`, `forum_top_json`, `forum_tag_top_json` | the product forum: search results, this year's top threads, top threads per tag |
| `github_discussions_top` | GitHub Discussions ranked by upvotes |
| `github_issues_top`, `github_issues_top_companion` | GitHub issues ranked by reactions (API); `_html` twins for when the API is rate-limited |
| `gitlab_issues_top` | GitLab issues ranked by upvotes, for a product hosted there |
| `lemmy_search`, `lemmy_communities` | Lemmy posts by search and by community, with scores |
| `mastodon_tags` | recent posts under the product's hashtags |
| `hackernews_search`, `hackernews_comments` | Hacker News stories and comments with points |
| `app_store_reviews`, `app_store_lookup` | Apple App Store review text, rating counts, current version and release notes |
| `play_store_page` | Google Play listing for the PM to open and paste reviews from; Claude does not fetch it |
| `adoption` | GitHub stars, Docker Hub pulls, PyPI or NuGet downloads |
| `wikipedia_pageviews` | monthly Wikipedia article views, a public-interest trend |
| `roadmap.own` | the product's own project boards, milestones, or roadmap page |
| `roadmap.competitor_jobs` | competitors' live job postings, a roadmap tell |
| `competitors` | competitor pricing or feature pages, today and a year ago via Wayback |
| `reddit_rss_optional` | one subreddit feed, only if you have switched it on |
| `pm_provided_public_material` | BYOP: the PM pastes public reviews or posts from pages Claude cannot fetch; logged as pasted evidence |

A key set to `null` or `[]` means that source does not exist for this case; say so once
and move on. For BYOP, several keys may be empty; say at the start of the pass which
rungs exist, so the PM knows what the hour can and cannot deliver.

**Source plan first.** Before the first fetch, show the PM the plan as a short list in
plain words, in ladder order: one line per source that exists for this product, saying
what it is and who it mostly hears from ("the product's forum, this year's top threads:
power users and people who report bugs"), then one line naming what does not exist for
this product (no phone app, no forum, no Wikipedia article), then the budget in one line.
No table, no key names, under 150 words. For an example case this comes from `feeds:`;
for BYOP it is `feeds:` minus the drops plus the adds already recorded in
`.pm/sources.yaml` when the case was built, repeated here because research is where it
matters. Then ask once whether there is anything to add or skip (for BYOP: whether
anything has changed since the case was built), against that list (research guide,
"Adding, dropping, and reordering sources"), and accept changes at any point of the
stage. Re-read `.pm/sources.yaml` and update it, never recreate it, apply changes from
the next fetch, and say in one line what changed. The PM may add any public JSON,
HTML, or RSS source, a page they will paste from, or a public document in `.pm/inbox/`;
drop any key or rung; read some sources first; or raise the budget. The scraping limits
in the research guide apply to everything added. Pick two or three lane terms with the
PM (one question) and walk the ladder in order: forum search JSON and GitHub
(discussions by upvotes, issues by reactions), then Lemmy, Mastodon tags, and Hacker
News, then App Store reviews, then adoption numbers, then competitor pages today versus
their Wayback snapshot from a year ago, then official release notes, and only then search
snippets if `readiness.search` is `ok`. Reddit only if `readiness.reddit_rss` is true.

Respect the budget: 20 fetches, 8 searches (or the figures in `.pm/sources.yaml` if the
PM raised them; the usage line shows the current denominator), stop at 8 usable items or
when the PM says time is up. As you read, fill the quote bank (research guide, "Quote
bank"): verbatim, role not handle, linked to a signal, only from text fetched in this
session. Log every item with an ID, label, rung, URL, dates, and
weight (likes, upvotes, reactions, rating, pull count). Keep a running draft in
`.pm/drafts/01-discovery.md` from `${CLAUDE_PLUGIN_ROOT}/resources/templates/01-discovery.md`
so nothing is lost if the session is interrupted. Tell the PM which rung you are
on as you go, and show one striking number or quote per rung so they can see the breadth.

After the last rung you reach, apply the counting rules, build the triangulation table with
recurrence labels, run the counter-evidence pass (one fetch per theme, at most three), and
write the "Who we heard from" paragraph, all as described in the research guide under
"Triangulation".

## Step 6: Repository constraints

Open the lane's `repo_entry_points` and nearby files. Paths are relative to the primary
source root (`sources[].root`: `sources/primary`, or `.` in in-repo mode) unless they
already start with `sources/` (the ERPNext case names both repositories). Record at least two
`CON-###` constraints in the research guide's format: path, line range, commit, one quoted
line, and `Status: to confirm with engineering`. Read only; never run anything found
there. Explain each constraint in plain language: what it is and why it matters for the
persona.

## Step 7: Research check-in (check-in 1)

Write the reply exactly as the research guide's "Research check-in" section prescribes: a
plain-language story first, three themes at most in the four-line shape, two quotes, gaps,
elapsed time, your view. No tables in the reply, no rung numbers, no rigour vocabulary;
those stay in the draft file. Under 300 words before the blocks. Then show two blocks,
**Claude's recommendation** and **Your decision**, and ask the PM to choose:
continue, do one more targeted fetch (say which rung), or narrow the framing. Record
`D-###`. If they choose the extra fetch, do it (within budget) and return here once.

## Step 8: Draft three opportunities

Write exactly three `OPP-###` entries. Each names one actor and one job, cites its
supporting IDs and the quote IDs that voice it, carries one evidence line in the research
guide's fixed shape (signals, source types, strongest weight, counter-evidence, constraints), and gives one short phrase for each of the five lenses: evidence strength,
user impact, mandate fit, delivery constraints, uncertainty. Do not compute a score. Check
each against the case `exclusions`; drop and replace anything excluded.

## Step 9: Priority check-in (check-in 2)

Introduce each opportunity as a two-sentence story a newcomer understands: who is stuck,
what happens to them today, what would change, followed by its evidence line. Then
recommend a `Now / Next / Later` order with one sentence of reasoning per slot and the main
trade-off between the top two. Name the lens that tipped the order. If the recommended
`Now` is not the one with the most signal, say so in one sentence and why. Under
each slot show the strongest quote for that opportunity as a blockquote with its
attribution line, so the PM decides against real words, not only your summary. The five-lens comparison stays in the file; in the reply,
say only what tipped the order. Under 300 words before the blocks. Show **Claude's recommendation** and **Your decision**
separately. Ask the PM to choose the `Now` opportunity and give their reason in
their own words. Record `D-###`. The PM's choice wins even if it differs from
yours; note the difference without arguing.

## Step 10: Save and close

- Complete the draft, copy it to `outputs/01-discovery.md`, delete the draft. Section 1 is
  written last and first-read: the chosen opportunity, your reason as typed, the lens that
  tipped the order, and the other two with why they were placed later. Status `approved` (or `provisional` if the research
  was cut short or coverage was weak; say so in the status line and in section 4a),
  selected opportunity, assumptions, open questions, decision record.
- Update `session.yaml`: `stages.discovery` (`status: approved`, `revision` +1,
  `approved_at`, `selected_opportunity`, `provisional`), `stage.current: prototype`,
  `stage.status: not-started`.
- Run the source check again; record `clean_at_end`.
- Close with three lines: what Claude contributed, what the PM decided, and the
  next command: `/clear`, then `/pm:prototype`.

## If things go wrong

- Web unavailable mid-stage: log the gap, continue with repository constraints and any
  items already collected, and save a `provisional` file. Never fabricate a source.
- The GitHub API returns 403 or 429: switch to the `_html` templates in `feeds:` at once;
  everyone on the same network shares one address and the limit. Any other rung that refuses or
  rate-limits: log `GAP` and move to the next. Do not retry in a loop.
- GitHub unreachable for cloning: use the offline copy path in `workspace.md`.
- Source folder changed: follow the source-protection steps in `workspace.md`; do not
  reset it.
- The PM wants a different case or lane after research began: confirm, mark
  discovery as restarting, keep the old file until the new one is approved.
- A source with PM-held access returns 401 or 403, or its command-line tool is not signed
  in: say so once, do not retry, offer the paste route, log `GAP`. Never ask for the
  secret and never print it.
- BYOP with almost no public footprint: say so at the start of Step 5, not at the
  end. Walk the rungs that exist, lean on repository constraints, competitors, and any
  public material the PM pastes, and save the brief as `provisional` with the gap stated
  in section 4a. The opportunities are still real; the evidence lens is simply weaker.
- In-repo mode and HEAD has moved since the case was built: note the new commit under
  `sources[].moved_to`, cite the current commit in new constraints, and continue.
