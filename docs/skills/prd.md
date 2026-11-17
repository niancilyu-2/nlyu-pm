# /nlyu-pm:prd

The PRD skill. It writes an engineering handoff grounded in the product's code and has an
independent reviewer check it before you sign it off.

## What it produces

`outputs/03-prd.md`, the PRD, with status `ready-for-engineering-review`, and
`outputs/03-prd-review.md`, the review with each finding and how you settled it.

## Before you start

A product that is set up. The PRD needs an opportunity and a flow. It takes them from
the discovery brief and the prototype when they exist. For whichever is missing, Claude
asks you for it in a short intake, and the PRD says which inputs were typed in.

## How a run goes

1. **Find the code that would change.** Anything Claude opened is `Verified` with a
   path. Anything it did not open is `Inferred`.
2. **Draft the PRD.** Problem and evidence, goals and non-goals, the flow and its states,
   requirements, acceptance criteria, risks, open questions, and an appendix for
   engineering.
3. **Scope check-in.** You approve or edit, and pick the two customer quotes.
4. **Independent review.** A reviewer that has not seen the conversation checks that
   every requirement traces to evidence, every technical claim holds, and every
   acceptance criterion can be tested.
5. **Settle each finding.** Fix it, turn it into a question for engineering, or accept it
   with a note. Blocking findings must be fixed.
6. **Handoff check-in.** You approve the result and confirm the open questions.

## Rules it follows

- Architecture, implementation design, and estimates belong to engineering.
- No estimates, story points, delivery dates, or costs.
- A question stays open for engineering only if its answer would not change scope,
  behaviour, or acceptance criteria.
- Every requirement points back to an opportunity and its evidence.

## Where the details live

`plugins/nlyu-pm/skills/prd/SKILL.md` is the skill, `agents/prd-reviewer.md` the
reviewer, `resources/prd-review-checklist.md` what it checks, and
`resources/templates/03-prd.md` the template.

## In Codex

Run it as `$prd`. The reviewer runs as a separate subagent, and the skill checks
afterwards that it changed no file.
