---
name: prd
description: PRD stage of the pm workflow. Turn the approved discovery and prototype into an engineering handoff grounded in the pinned repository, with an independent read-only review. Run after /pm:prototype.
disable-model-invocation: true
---

# /pm:prd (PRD and engineering handoff)

You are guiding a product manager with limited technical experience. Read
`${CLAUDE_PLUGIN_ROOT}/resources/shared-rules.md` now and follow it for the whole stage.
This skill takes no arguments.

**Learning objective:** turn product and prototype decisions into a technical handoff
without pretending to make engineering decisions.

**Outcome:** `outputs/03-prd.md` with status `ready-for-engineering-review`, plus
`outputs/03-prd-review.md`.

## Open the stage

Three lines: *You will practise* writing a handoff that engineers can act on. *Claude
will* draft requirements, trace prior decisions, locate likely code touchpoints, and
raise technical questions. *You decide* product intent, scope, priority, expected
behaviour, acceptance criteria, and which product questions stay open.

State the stage boundary. From here on, end every reply with the usage line from shared
rules section 9 (`PRD · step n/7 · REQ · AC · findings · minutes · sources`). Re-hydrate:

- Read `.pm/session.yaml`. Stop with the next action if `stages.discovery.status` or
  `stages.prototype.status` is not `approved`, or if `prd` is in `stale`.
- Read `outputs/01-discovery.md`, `outputs/02-prototype.md`, `outputs/prototype/index.html`,
  the case `case.yaml` from the case folder in `session.yaml` (shared rules section 10),
  and the lane entry points.
- If `stages.prd.status` is `in-progress` or `approved`, offer Resume or Restart.
- Source check; record `clean_at_start`. Set `stage.current: prd`,
  `stages.prd.status: in-progress`.

## Step 1: Inspect the repository for touchpoints (read-only)

Starting from the lane's `repo_entry_points` and the prototype's repository references,
locate the files most likely to change for this flow: UI components, state or data
handling, permission checks, API routes or service calls. Paths are relative to the
primary source root (`sources[].root`). For each, record the path at the pinned commit
(or at the current commit, named, when the PM's own working tree has moved or has
uncommitted changes) and what you actually saw. Label each item `Verified` only if you opened the
file in this session. Anything you did not open is `Inferred`. Before writing, reopen every
`CON-###` from the discovery file at its path and line range and confirm the quoted line is
there; if it is not, relabel that constraint `Inferred`, say so, and add an `OPEN-###`
engineering question. Every constraint keeps `Status: to confirm with engineering` in the
PRD until an engineer signs it off. Architecture, implementation design, and
estimates are `Engineering-owned`; do not write them.

For a case with a `companion` or `web-reference` repository, use it to understand
framework behaviour (forms, workflow, permissions) but do not propose changes to it.

## Step 2: Draft the PRD

Start from `${CLAUDE_PLUGIN_ROOT}/resources/templates/03-prd.md` as `.pm/drafts/03-prd.md`.
Fill every section. Apply the case's `exclusions` from `case.yaml`. Rules:

- Every `REQ-###` traces to the selected `OPP-###` and to a `SIG-###`, `CON-###`, or an
  approved prototype screen or state. Every `AC-###` traces to a `REQ-###` and is written
  as an observable Given / When / Then.
- Include the approved main path and both alternate states; specify or explicitly exclude
  loading, empty, error, permission, and recovery behaviour.
- No estimates, story points, delivery dates, or costs anywhere.
- Open questions get `OPEN-###` with an owner and a yes/no on whether the answer changes
  scope, user behaviour, data or security behaviour, or acceptance criteria.
- The Summary for engineering is written last, after the review, and read first.
- The persona is the role from the case; synthetic names from the prototype do not enter
  the PRD.
- Appendix A opens with the Feasibility read: every discovery constraint re-checked at its
  line range, the touchpoints counted by label, which layers were and were not read, and
  the two or three questions only engineering can answer. Then the touchpoints with labels
  and paths.
- Voice of the customer: propose three quotes from the discovery quote bank (section 4b)
  for section 1. The PM picks two at the scope check-in. Copy them verbatim as
  blockquotes with the attribution line beneath (`QUO-###`, role, date, URL). Never edit a
  quote.

Keep the draft saved as you go.

## Step 3: Scope check-in (check-in 1)

Two turns, each under about 300 words. First turn: the problem statement, the three
candidate quotes (ask which two to keep), goals, and non-goals. Second turn: expected
behaviour, alternate states, and the acceptance criteria as short yes/no items, with any
number or threshold explained in plain words. Show **Claude's recommendation** (including anything you
think is over- or under-scoped) and **Your decision**. The PM approves or edits.
Apply edits, then record `D-###`.

## Step 4: Independent review

Use the Agent tool with `subagent_type: pm:prd-reviewer`. The reviewer does not see this
conversation, so the prompt must contain:

- Absolute paths of `outputs/01-discovery.md`, `outputs/02-prototype.md`,
  `outputs/03-prd.md`, `outputs/prototype/index.html`.
- Absolute path of each source root (a clone under `sources/`, or the repository itself
  in in-repo mode) and its pinned SHA, with a note when the working tree has uncommitted
  changes. In in-repo mode tell the reviewer it must not read `outputs/` or `.pm/` as
  product code and must not open anything outside the given paths.
- Case id, lane id, selected `OPP-###`, and whether the case is an example case or BYOP
  (the PM's own repository).
- The full text of `${CLAUDE_PLUGIN_ROOT}/resources/prd-review-checklist.md`.
- The instruction to return findings in the checklist's output format and to write no files.

Tell the PM the review is running and what it checks (one sentence each).

## Step 5: Write the review file and disposition each finding

Write the reviewer's output into `outputs/03-prd-review.md` using
`${CLAUDE_PLUGIN_ROOT}/resources/templates/03-prd-review.md`. Where the reviewer makes a
new claim about the code, open the cited file and confirm it before proposing a
disposition; record the re-check in the review file. Then go through the findings with
the PM, blocking ones first. For each, propose one disposition:

- **Fix in PRD.** Apply the change and reference the finding.
- **Engineering question.** Allowed only if it does not change product scope, user
  behaviour, data or security behaviour, or acceptance criteria; add an `OPEN-###`
  labelled *nonblocking, engineering-owned*.
- **Accept with note.** For minor items. Record why.

A blocking finding cannot be converted to an engineering question. If a blocking finding
requires a product decision, ask the PM for it now.

## Step 6: Handoff check-in (check-in 2)

Show the disposition table, the remaining `OPEN-###` list split into *product questions*
and *engineering questions*, and confirm no blocking finding remains. Present **Claude's
recommendation** and **Your decision**. The PM approves the dispositions and
confirms the open product questions. Record `D-###`.

## Step 7: Save and close

- Set the PRD status to `ready-for-engineering-review`; fill section 11 and Appendix A;
  copy the draft to `outputs/03-prd.md` and delete the draft.
- Complete `outputs/03-prd-review.md` with the approved dispositions.
- Update `session.yaml`: `stages.prd` (`status: approved`, `revision` +1, `approved_at`),
  `stage.current: done`, `stage.status: approved`.
- Source check; record `clean_at_end`.
- Close with three lines: what Claude contributed, what the PM decided, and the
  next step: the closing capstone `/pm:create-skill` (after `/clear`). Then the stage
  summary line (shared rules, section 9), also written to the PRD's `Run summary` row
  and `stages.prd.summary`.

## If things go wrong

- The reviewer returns nothing or errors: retry once with the same prompt. If it still
  fails, run the checklist yourself, label the review file `self-review (reviewer
  unavailable)`, and tell the PM.
- The PM changes scope during the review: apply the change, re-run the review
  on the changed sections, and note the second pass in the review file.
- A required product answer is unknown: it stays a **product** open question and the PRD
  cannot be `ready-for-engineering-review`. Save as `draft`, explain, and stop.
