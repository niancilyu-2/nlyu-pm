# /nlyu-pm:prototype

The prototype skill. It turns one opportunity into a single user flow, builds a clickable
prototype of it, and improves it once.

## What it produces

`outputs/prototype/index.html`, one file that opens with a double-click, and
`outputs/02-prototype.md`, the notes: the user and job, the flow and its states, the
critique, the revision, and your decisions.

## Before you start

A product that is set up. With an approved discovery brief, the prototype builds on the
opportunity you chose. Without one, Claude asks you to pick an opportunity from your
backlog or describe one in a few sentences, and the notes say it was typed in.

## How a run goes

1. **Confirm the flow.** Claude shows the quotes behind the opportunity and asks for one
   user, one job, where the task starts and ends, and the two alternate states that
   matter most.
2. **Flow check-in.** You approve or edit before anything is built.
3. **Match the product's look.** Claude reads the product's existing design, read-only.
4. **Design brief.** One page that the build starts from.
5. **Build.** In Claude Design if it is available, where you run `/design` with the
   brief. Otherwise Claude writes the HTML file itself.
6. **Walkthrough.** You and Claude click through the main path and both states.
7. **One revision.** Claude proposes one change. You approve it or pick another.
8. **Prototype check-in.** You approve the result.

## Rules it follows

- One user, one job, one flow, two alternate states.
- All names and data are made up.
- The walkthrough is a design critique, not user testing.
- No code is copied out of the product's repository.

## Where the details live

`plugins/nlyu-pm/skills/prototype/SKILL.md` is the skill, with the HTML rules in
`resources/prototype-html-guide.md` and the notes template in
`resources/templates/02-prototype.md`.

## In Codex

Run it as `$prototype`. The prototype is always the standalone HTML file.
