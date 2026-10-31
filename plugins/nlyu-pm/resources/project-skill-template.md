# Project skill template and self-check (skill builder)

`/nlyu-pm:create-skill` writes exactly one file: `.claude/skills/<slug>/SKILL.md`. Nothing else
goes in the folder in the first version: no scripts, no subagents, no extra files.

## Slug rules

- Lowercase kebab-case, letters, digits, and hyphens only; starts with a letter.
- At most 64 characters. Not `synced` (reserved). Not the name of an existing folder under
  `.claude/skills/`.
- The `name` field equals the folder name.

## Frontmatter

```yaml
---
name: <slug>
description: <Plain-language outcome in one sentence>. Use when <specific trigger>.
disable-model-invocation: true
---
```

Tell the PM: `disable-model-invocation: true` keeps the first version manual, so it
only runs when they type `/<slug>`. Removing that line later lets Claude pick the skill
automatically when a request matches the description.

## Body (target 300–700 words, hard limit 1,000)

```markdown
# <Skill title>

## Goal
<What this skill helps the PM produce or decide, for whom, and what is different when done.>

## What to provide
- <Input 1, e.g. "raw meeting notes pasted into the message">
- <Input 2, or "nothing else">
If something is missing, ask for it once; do not guess.

## Workflow
1. <Step>
2. <Step>
3. <Step>
(3–6 steps. Each step says what Claude does and what it shows the user.)

## PM decisions and stop points
- Stop and ask before <decision that must stay with the PM>.
- Show options; never pick <judgement> on the PM's behalf.

## Expected output and quality check
- Output shape: <headings or fields>
- A good result always includes: <bullets>
- Before finishing, check: <2–4 yes/no checks>

## Boundaries
- Never assume <…>. Never invent <…>. Never <…>.
- Use only what the user provided or public information; label anything inferred.
```

## Self-check before testing

Run through this list and fix anything that fails, then run
`claude plugin validate .claude/skills --strict` from the workspace folder (point it at the
**skills folder**, not the skill's own folder).

- [ ] Folder name equals `name`; slug passes the rules above.
- [ ] Description states an outcome **and** a trigger ("Use when …").
- [ ] `disable-model-invocation: true` present.
- [ ] Body under 1,000 words; every section present; no `TODO`, `TBD`, `<…>`, or `…` left.
- [ ] Workflow has 3–6 steps and at most 3 meaningful branches.
- [ ] At least one explicit PM decision or stop point.
- [ ] Boundaries name at least one thing the skill must never invent.
- [ ] No scripts, subagents, integrations, or custom frontmatter fields.

## Testing in a fresh session

The authoring conversation can hide missing instructions, so test from a **new** Claude
Code session in the same workspace folder:

1. Ask the PM to open a second session in the same folder: a new session in the desktop
   app's Code tab, or a second terminal window running `claude` (or quit this session,
   run `claude`, and later return with `claude --continue`).
2. In the new session, type `/skills` and confirm `/<slug>` is listed. Then run
   `/<slug>` with the agreed public or synthetic test input.
3. Copy the result and paste it back into the authoring session.

If no result comes back, record `Observed result: not tested` in the summary. Do not infer
success.

## Reuse

Copying the folder `.claude/skills/<slug>/` into another project's `.claude/skills/` makes
the skill available there. The first version is not installed globally, published,
committed, or added to the `nlyu-pm` plugin.
