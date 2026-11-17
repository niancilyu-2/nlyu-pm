# /nlyu-pm:weekly

The weekly refresh. In about fifteen minutes it shows what changed since last time and
writes a digest with an update you can paste to stakeholders. It asks one question, at
the end.

## What it produces

`outputs/weekly/<year>-W<week>.md`: what changed, how the evidence behind each
opportunity moved, your decisions this week, a stakeholder update, and Claude's
recommendation.

## Before you start

A product that is set up. No stage has to be finished. If nothing is set up, run
`/nlyu-pm:scout` and say "set up only".

## How a run goes

1. **Gather what you captured** with `/nlyu-pm:log` since the last run.
2. **Re-read the public sources** on a small budget: what moved on the items your
   opportunities rest on, what is new, and what shipped.
3. **Recount the backlog.** Each opportunity's evidence is marked up, down, or unchanged,
   with the reason.
4. **Write the digest.**
5. **Ask once.** Keep the order, make the one change Claude recommends, or decide later.
   If you change what is first, any prototype or PRD built on the old choice is marked
   out of date.

## Rules it follows

- Every number carries its base, such as "551 upvotes, up from 498".
- The stakeholder update has no IDs or names, and paraphrases anything internal.
- Only you move an opportunity. Claude recommends.

## Where the details live

`plugins/nlyu-pm/skills/weekly/SKILL.md` is the skill, and
`resources/templates/05-weekly.md` the digest template.

## In Codex

Run it as `$weekly`. Research fetches may need you to approve network access.
