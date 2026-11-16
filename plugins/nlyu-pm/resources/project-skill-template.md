# Project skill template and self-check (skill builder)

`/nlyu-pm:create-skill` writes exactly one file: `<skills-dir>/<slug>/SKILL.md`. Nothing else
goes in the folder in the first version: no scripts, no subagents, no extra files.
`<skills-dir>` is `.claude/skills` in Claude Code and `.agents/skills` in Codex (shared
rules section 11). Codex is the one exception to "one file": it also gets the small
policy file described under Frontmatter.

## Slug rules

- Lowercase kebab-case, letters, digits, and hyphens only; starts with a letter.
- At most 64 characters. Not `synced` (reserved). Not the name of an existing folder under
  `<skills-dir>`.
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

**Codex.** Codex ignores that frontmatter line (keep it anyway, so the folder works
unchanged if copied to Claude Code). Write one more file,
`<skills-dir>/<slug>/agents/openai.yaml`, with exactly:

```yaml
policy:
  allow_implicit_invocation: false
```

Tell the PM: this keeps the first version manual, so it only runs when they type
`$<slug>`. Deleting that file later lets Codex pick the skill automatically.

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

Run through this list and fix anything that fails. Then, in Claude Code only, run
`claude plugin validate .claude/skills --strict` from the workspace folder (point it at the
**skills folder**, not the skill's own folder). Codex has no such command; the list is
the check.

- [ ] Folder name equals `name`; slug passes the rules above.
- [ ] Description states an outcome **and** a trigger ("Use when …").
- [ ] `disable-model-invocation: true` present. In Codex, `agents/openai.yaml` present too.
- [ ] Body under 1,000 words; every section present; no `TODO`, `TBD`, `<…>`, or `…` left.
- [ ] Workflow has 3–6 steps and at most 3 meaningful branches.
- [ ] At least one explicit PM decision or stop point.
- [ ] Boundaries name at least one thing the skill must never invent.
- [ ] No scripts, subagents, integrations, or custom frontmatter fields; no file other
      than `SKILL.md` (and, in Codex, `agents/openai.yaml`).

## Testing in a fresh session

The authoring conversation can hide missing instructions, so test from a **new** session
of the same host in the same workspace folder:

1. Ask the PM to open a second session in the same folder: a new session in the desktop
   app's Code tab, or a second terminal window running `claude` (or quit this session,
   run `claude`, and later return with `claude --continue`). In Codex: a new thread in
   the Codex app, or a second terminal window running `codex` (later `codex resume`).
2. In the new session, type `/skills` and confirm the skill is listed. Then run
   `/<slug>` (Claude Code) or `$<slug>` (Codex) with the agreed public or synthetic test
   input.
3. Copy the result and paste it back into the authoring session.

If no result comes back, record `Observed result: not tested` in the summary. Do not infer
success.

## Reuse

Copying the folder `<skills-dir>/<slug>/` into another project's skills folder
(`.claude/skills/` for Claude Code, `.agents/skills/` for Codex) makes the skill
available there. The first version is not installed globally, published,
committed, or added to the `nlyu-pm` plugin.
