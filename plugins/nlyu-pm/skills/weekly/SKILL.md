---
name: weekly
description: Weekly refresh stage of the nlyu-pm workflow. In about fifteen minutes, gather what was captured since last time, re-read the product's public sources on a small budget, show what changed and what it means for the backlog, and write a dated digest with a paste-ready stakeholder update. One decision at the end. Run about once a week on a product that is already set up.
disable-model-invocation: true
---

# /nlyu-pm:weekly (Weekly refresh)

You are giving a product manager a short, honest picture of what changed this week. Read
`<plugin-root>/resources/shared-rules.md` now and follow it, then
`<plugin-root>/resources/evidence-base.md`. This skill takes no arguments.

**Plugin root.** `<plugin-root>` in this skill and in every file it reads means the
plugin's top folder, the one that holds `resources/`, `cases/`, and `agents/`. It is two
folders above the folder this `SKILL.md` is in. Claude Code fills in the path here:
`${CLAUDE_PLUGIN_ROOT}`. If that shows a real path, use it; if it still shows a dollar
sign and braces (Codex and other hosts), work the path out from this file's location.
Resolve it once to an absolute path and use that wherever `<plugin-root>` appears.

**Stage objective:** keep the backlog tied to current evidence, so the next decision
starts from what is true this week, not from the last research pass.

**Outcome:** `outputs/weekly/<year>-W<week>.md`, an updated evidence base, and at most
one recorded decision.

Budget: fifteen minutes, 8 fetches, 3 searches (or `budget.weekly_fetches` and
`budget.weekly_searches` in `.pm/sources.yaml` when the PM raised them). The skill asks
nothing until its last step, so it can run while the PM does something else.

## Open the stage

Three lines: *You will* see what changed and decide whether the order still holds.
*Claude will* gather the week's notes, re-read the public sources, recount the evidence
behind each opportunity, and draft an update you can send. *You decide* whether anything
moves.

State the stage boundary. From here on, end every reply with the usage line from shared
rules section 9 (`Weekly · step n/6 · fetches · captured · new · moved · minutes ·
sources`). Then:

- Read `.pm/session.yaml`. If there is no case or no focus area, stop and say the product
  is not set up: run `/nlyu-pm:scout`, continue past readiness, and say "set up only". No earlier stage has to be
  approved; an approved discovery brief only makes the backlog richer.
- Read the case's `case.yaml` and its `feeds:` from the case folder (shared rules section
  10), `.pm/sources.yaml` if it exists, and the evidence base (build it from an older
  discovery brief first if `evidence-base.md` says to).
- Run the source check and record the result. Record the start time with `date`.

## Step 1: Set the window

The window starts at `weekly.last_run` in `session.yaml`. On a first run it starts at the
discovery brief's approval time, or seven days ago if there is no brief. It ends now. Get
the week label with `date +%G-W%V`. Say the window in one line.

## Step 2: Gather what was captured

From `.pm/evidence/log.md`, list every signal whose `Logged` date falls in the window and
was written by `/nlyu-pm:log`, with what it is attached to. Count them. List any
`unassigned` signals and attach them now that a product and a backlog exist, by the rules
in `evidence-base.md` ("Attaching a signal"). Do not ask the PM.

## Step 3: Re-read the public sources

Follow the limits and saving rules of `<plugin-root>/resources/research-guide.md` (save
every fetch before logging from it, one request per address, no sign-in, no loops).
Spend the budget in this order and stop when it is spent:

1. **What we already cited.** For the opportunities in `Now` and `Next`, re-read up to
   four of their strongest public items. Note what moved: the count (upvotes, reactions,
   comments, rating), whether it was closed or answered, and any maintainer or company
   reply. Write the base beside every number: "551 upvotes, up from 498".
2. **What is new.** Read up to three of the product's most active feeds for the focus
   area (the forum's recent or top threads, issues by reactions, the app store review
   feed) for items newer than the window start. Log each new item as a signal.
3. **What shipped.** Read the release notes or changelog once for anything in the window
   that touches the focus area. In in-repo mode also run, read-only,
   `git log --oneline --since=<window start> -- <the lane's entry point paths>` and name
   the commits that touch the flow. A fix that shipped is counter-evidence for the
   opportunity it answers; log it as such.

A source that refuses or rate-limits is a `GAP`; move on. Searches are for finding one
missing address, not for evidence; a snippet is never evidence.

## Step 4: Recount the backlog

For every opportunity and candidate in the focus area, recompute the evidence line from
its `Signals` line (`evidence-base.md`) and write `Last movement`: `up`, `down`, or
`unchanged`, with the reason in a few words ("2 new signals from app reviews", "main
complaint fixed in 2.4"). Check each new quote by finding its words in its saved file
before it is written; say in the digest that this check ran in the same session, not by
the independent reviewer. Do not move any opportunity between slots.

## Step 5: Write the digest

Write `outputs/weekly/<year>-W<week>.md` from
`<plugin-root>/resources/templates/05-weekly.md` (a second run in the same week writes
`<year>-W<week>-b.md`). Rules:

- **What changed** holds at most five lines, the most decision-relevant first, each with
  its IDs and its base.
- **Decisions this week** lists every `D-###` in `session.yaml` whose time falls in the
  window, in the PM's recorded words.
- **Stakeholder update** is at most 120 words of plain prose a non-specialist can read:
  what we learned, what we decided, what is next, what we need. No IDs, no personal
  names, nothing from an internal note in quotation marks (paraphrase it), at most one
  public quote, and no claim stronger than its evidence line.
- **Gaps** names what was not reached and who we still have not heard from.

## Step 6: Recommend, ask once, and close

Reply in under 200 words: the three changes that matter most, then **Claude's
recommendation** in two sentences with what would change it, then **Your decision**.
Ask one question (header `Backlog`, "Does anything move this week?") with at most three
options: **Keep the order**; the one change you recommend, if any (**Promote <title> to
Now**, or **Mark <title> as shipped**); and **Decide later**. The PM's own answer is
always possible.

- A change: record `D-###` with `checkin: weekly-check`, update the slots and `Slot
  history` in the backlog, and, if `Now` changed and a prototype or PRD was built on the
  old one, mark those stages stale (shared rules section 6) and name the skill to run.
- Keep, or decide later: record `D-###` the same way, with the PM's words.

Then save: `weekly.last_run`, `weekly.last_file`, and `weekly.runs` + 1 in
`session.yaml`; run the source check again. Close with where the file is and the stage
summary line (shared rules section 9), also written to the digest's `Run summary` row.

## If things go wrong

- Web unavailable: write the digest from captured notes and the code alone, say so in
  Gaps, and mark the file `provisional`.
- Nothing changed: say so in one line, still write the digest (it records that someone
  looked), and recommend keeping the order.
- No backlog yet (the product is set up but no discovery ran): report the week's notes
  and public changes for the focus area, list the candidates, and recommend
  `/nlyu-pm:scout` when there is enough to rank. Ask no question.
- Source folder changed: follow the source-protection steps in `workspace.md`.
