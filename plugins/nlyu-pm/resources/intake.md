# Starting a stage without the one before it

`/nlyu-pm:prototype` and `/nlyu-pm:prd` depend on inputs, not on earlier stages having
run. When the approved file from the earlier stage exists, they use it and nothing here
applies. When it does not, they take the same inputs from the PM in a short intake, label
them honestly, and carry on. The full chain stays the strongest path, and a file built on
it says so; a file started from an intake says that instead.

## What must exist first

The product must be set up: `.pm/session.yaml` with a case and a focus area. If it is
not, say so and stop with the next action: run `/nlyu-pm:scout`, choose to continue past
readiness, and say "set up only". Scout sets up the product and the focus area, gets the
code, and stops before any research (about fifteen minutes for the PM's own repository,
less for an example case).

## When the earlier file is missing

Ask one question (header `Start`, "There is no approved <discovery brief | prototype>
yet. How do you want to start?") with two options: **Start here** (a short intake, a few
minutes; the result says which inputs were typed in rather than researched) and **Run
<the earlier stage> first** (the full path, recommended for a new product area). If the
earlier stage exists but is marked stale, this file does not apply: follow shared rules
section 6.

## The opportunity intake (no discovery brief)

1. If `.pm/evidence/backlog.md` holds opportunities or candidates for this focus area,
   offer them (at most four in the question, most signals first) with "describe a new
   one" as the last option. Choosing one that is not `Now` does not re-rank the backlog.
2. For a new one, ask in plain prose, one message: who is stuck, what they are trying to
   do, and what goes wrong today. Two or three sentences is enough.
3. Write it to the backlog as a new `OPP-###` with `Origin: PM-provided`, slot
   `Candidate`. Search `.pm/evidence/log.md` for signals that speak to it and attach
   them; compute the evidence line from those. If none attach, the line is
   `Evidence: none logged · PM-provided statement`.
4. Read back the opportunity and its evidence line in three lines. Record `D-###` with
   `checkin: intake`.

## The flow intake (no prototype)

1. Ask whether anything already shows the flow: a mock-up, a screenshot, a ticket, or a
   document. If so, the PM drops it in `.pm/inbox/` or pastes its text; read it.
2. Ask in plain prose for the main path as three to six steps, in the user's words.
3. Ask which two alternate states matter most (question tool, multi-select, the same five
   as the prototype stage: empty, error, permission, recovery, loading).
4. Save the result as `.pm/intake/flow.md`, headed `PM-provided, not prototyped`, with the
   actor, the job, the steps, the two states, and the name of any file it was read from.
5. Read it back in five lines. Record `D-###` with `checkin: intake`.

## What changes downstream

- **Labels.** Anything the PM typed at an intake is `PM-provided`, never `Evidence`. It
  becomes evidence only when a logged signal supports it.
- **Header.** The output file's `Based on` row names each input and where it came from,
  for example `OPP-007 (PM-provided, no discovery brief) · flow from .pm/intake/flow.md
  (not prototyped)`.
- **Quotes.** The PRD's customer quotes come from `.pm/evidence/quotes.md`. If no quote
  is attached to the opportunity, the block says "No verbatim customer evidence logged
  yet" and nothing is invented.
- **Constraints.** With no discovery brief there are no earlier `CON-###` to reopen; the
  PRD's first step records them fresh from the code, in the same format.
- **Review.** The reviewer still runs. Its prompt names which inputs are PM-provided and
  gives the paths that exist; it checks traceability against those and does not count the
  missing stage as a finding.
- **Status.** The PRD can still reach `ready-for-engineering-review`. Its status line
  adds the inputs in brackets, for example `ready-for-engineering-review (opportunity
  PM-provided, flow not prototyped)`.
- **Session file.** Set `stages.<stage>.inputs: intake` (`chain` when the earlier file
  was used). The earlier stage's own status stays as it was.

Evidence captured later with `/nlyu-pm:log` attaches to the same opportunity, so a file
started from an intake can be refreshed on stronger ground.
