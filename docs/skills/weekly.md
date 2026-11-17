# /nlyu-pm:weekly

The weekly refresh. In about fifteen minutes it shows what changed since last time and
what that means for your backlog, and writes a dated digest with an update you can paste
to stakeholders. It asks one question, at the end.

## What it produces

`outputs/weekly/<year>-W<week>.md`: what changed, how the evidence behind each
opportunity moved, the decisions you made this week, a stakeholder update of at most 120
words, Claude's recommendation, and the gaps. The evidence base is updated with anything
new.

## Before you start

A product that is set up: readiness done, a product and a focus area chosen. No stage has
to be finished. An approved discovery brief only makes the backlog richer. If nothing is
set up, run `/nlyu-pm:scout` and say "set up only".

## How a run goes

1. **Set the window.** From the last weekly run to now. The first run starts at your
   discovery brief, or seven days back.
2. **Gather what you captured.** Every note filed with `/nlyu-pm:log` in the window, and
   anything filed before the product was set up, now attached.
3. **Re-read the public sources**, within 8 fetches and 3 searches. First the items your
   current and next opportunities already rest on: did the counts move, was anything
   closed or answered. Then what is new in the most active sources. Then what shipped,
   from the release notes, and in your own repository from the commits that touch the
   focus area.
4. **Recount the backlog.** The evidence line of every opportunity is recomputed and
   marked up, down, or unchanged, with the reason. Nothing changes slot.
5. **Write the digest.**
6. **Recommend and ask once.** Claude gives the three changes that matter, its
   recommendation and what would change it, then asks whether anything moves: keep the
   order, the one change it recommends, or decide later. If you change what is first and
   a prototype or PRD was built on the old choice, those are marked stale and Claude
   names the skill to run.

## Rules it follows

- The same limits as the research pass: every fetch saved, one request per address, no
  sign-in, no page-by-page scraping, a search snippet is never evidence.
- Every number carries its base, such as "551 upvotes, up from 498".
- New quotes are checked against their saved text in the same session, and the digest
  says this was not the independent reviewer.
- The stakeholder update uses no IDs and no personal names, paraphrases anything from
  inside your company, and claims nothing stronger than the evidence behind it.
- Only you move an opportunity. Claude recommends.

## Where the details live

`plugins/nlyu-pm/skills/weekly/SKILL.md` is the skill,
`plugins/nlyu-pm/resources/templates/05-weekly.md` the digest template, and
`plugins/nlyu-pm/resources/evidence-base.md` the evidence base and backlog.

## In Codex

Run it as `$weekly`. Research fetches may need you to approve network access.
