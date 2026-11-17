# The evidence base and the backlog

One lasting record per workspace, shared by every skill. A discovery brief, a weekly
digest, and a PRD are views of it; none of them starts from an empty log. It lives under
`.pm/evidence/` and is created by whichever skill needs it first.

| File | Holds | Written by |
|---|---|---|
| `.pm/evidence/log.md` | every signal (`SIG-###`) and constraint (`CON-###`), newest last, append-only | `/nlyu-pm:scout`, `/nlyu-pm:log`, `/nlyu-pm:weekly` |
| `.pm/evidence/quotes.md` | the quote bank (`QUO-###`), each a blockquote with its attribution line | the same three |
| `.pm/evidence/backlog.md` | every opportunity (`OPP-###`) with its slot, evidence line, and history | `/nlyu-pm:scout`, `/nlyu-pm:log` (candidates and tallies only), `/nlyu-pm:weekly`, and the intake in `intake.md` |
| `.pm/fetches/` | the saved text behind every item, with `index.md` | whichever skill fetched or received it |

## IDs

IDs are workspace-wide and never reused. Before assigning a new `SIG`, `QUO`, `CON`, or
`OPP` number, read the highest one in `.pm/evidence/` and in any running draft, and
continue from it. An item that already has an ID keeps it everywhere it appears.

## A signal

The research guide's format ("Logging an item"), plus two lines:

```text
SIG-031 · Evidence (internal) · customer/community · call note
  Claim: An operations lead exports to a spreadsheet every Friday because the dashboard cannot filter by region.
  Source: internal call note · captured 2026-11-18
  Weight: one customer; said to be a weekly habit
  Saved: N-004
  Logged: 2026-11-18 by log
  Attached: OPP-002
```

`Logged` names the date and the skill (`scout rev 2`, `log`, `weekly 2026-W47`).
`Attached` names one opportunity, `candidate OPP-###`, or `unassigned`. A signal is never
edited after it is logged; a correction is a new line under it starting `Correction:`
with the date.

## Saved text

Every item points at a saved file, so a quote or label can be checked later:

| Prefix | What it is |
|---|---|
| `F-###` | a public page or feed fetched in a session |
| `P-###` | public material the PM pasted |
| `S-###` | search results (snippets are never quotes) |
| `N-###` | an internal note the PM gave `/nlyu-pm:log`, saved with personal details removed |

An `N` file has a header of `source:` (call note, support thread, chat message, meeting
notes, email excerpt), `captured:`, `redacted: yes`, and `truncated: no`.

## The backlog

One block per opportunity:

```text
OPP-002 · Now · Backup status at a glance
  For: household media steward · Job: confirm last night's photos are safe
  Problem: The app shows no clear sign that a backup finished, so people re-open it to check.
  Evidence: 6 signals, 3 source types · strongest: 551-upvote discussion · counter-evidence: looked (F-014), none · constraints: CON-002
  Signals: SIG-002, SIG-005, SIG-031 · Quotes: QUO-003, QUO-011
  Origin: discovery brief rev 1 (2026-10-01)
  Slot history: Now since 2026-10-01 (D-004)
  Last movement: 2026-W47 up, 2 new signals
```

- **Slots:** `Now`, `Next`, `Later`, `Candidate`, `Shipped`, `Dropped`. Only the PM moves
  an opportunity between slots, at a check-in that records a `D-###`. The one thing a
  skill may do alone is open a `Candidate`.
- **Origin** says where the opportunity came from: `discovery brief rev n`, `log`,
  `weekly <week>`, or `PM-provided` (typed by the PM at an intake, `intake.md`). An
  opportunity whose origin is `PM-provided` and whose `Signals` line is empty carries the
  evidence line `Evidence: none logged · PM-provided statement`; never invent a count.
- **Evidence line** is recomputed from the `Signals` line every time a signal is attached:
  the count, the distinct source types, the strongest weight, the counter-evidence entry
  (a `SIG-###`, `looked (F-###), none`, or `not yet looked`), and the constraints.
- **Last movement** is written by `/nlyu-pm:weekly`: `up`, `down`, or `unchanged`, with the
  reason in a few words.

## Attaching a signal

Compare the signal with the opportunities in the backlog for the focus area.

- It speaks to one: write `Attached: OPP-###`, add the ID to that opportunity's `Signals`
  line, and recompute its evidence line.
- It weakens or contradicts one (the thing already works, a fix shipped, someone prefers
  the current behaviour): attach it as that opportunity's counter-evidence.
- It fits none: open a `Candidate` with a one-line problem, its `Origin`, and the signal.
- There is no backlog yet: `Attached: unassigned`. The next skill that finds a backlog
  attaches it.

Attaching never moves an opportunity between slots.

## Who reads it

- `/nlyu-pm:scout` reads the log and the backlog before the research pass, so items
  already captured for the focus area count from the start, and appends its own at close.
- `/nlyu-pm:log` appends one to three signals and updates one tally.
- `/nlyu-pm:weekly` appends what changed, recomputes every evidence line, and writes the
  movement.
- `/nlyu-pm:prototype` and `/nlyu-pm:prd` read the opportunity and its quotes from here
  when there is no discovery brief (`intake.md`).

A workspace written before plugin 0.11.0 has no `.pm/evidence/` folder. The first skill
that needs it builds it from `outputs/01-discovery.md` if that file exists (its sections
3, 4b, 4c, and 4d), says so in one line, and continues.
