# /nlyu-pm:create-skill

The skill builder. It turns one PM practice of your own into a small reusable skill,
tests it once, and revises it once. It is independent of the other skills.

## What it produces

`.claude/skills/<name>/SKILL.md`, your skill, and `outputs/04-skill-summary.md`, which
records what it does, how it was tested, and what stays your call.

## How a run goes

1. **Starting point.** Describe a task you repeat, or paste a prompt or checklist you
   already use.
2. **Four questions**, one at a time: the job, what goes in and comes out, your steps,
   and what a good result looks like.
3. **Scope check-in.** Claude shows the proposed skill. You approve or narrow it.
4. **Write.** One file, run only when you type it.
5. **Test in a new session.** You run the skill on a safe example and paste the result
   back.
6. **One revision.** You approve it, then say in your own words what the skill automates
   and what remains your judgment.

## Rules it follows

- One job per skill. If the idea is too broad, Claude offers narrower ones.
- No scripts, integrations, or global install.
- If you do not test it, the summary says "not tested".

## Where the details live

`plugins/nlyu-pm/skills/create-skill/SKILL.md` is the skill, and
`resources/project-skill-template.md` the template.

## In Codex

Run it as `$create-skill`. The skill is written to `.agents/skills/<name>/` and run as
`$<name>`.
