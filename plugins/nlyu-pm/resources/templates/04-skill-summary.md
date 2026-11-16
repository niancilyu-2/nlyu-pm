# Skill summary: /<slug>

| Field | Value |
|---|---|
| Location | <skills-dir>/<slug>/SKILL.md |
| Job | <one sentence> |
| Trigger | Use when <…> |
| Invocation | manual only (`disable-model-invocation: true`; in Codex, `agents/openai.yaml`) |
| Run summary | <stage summary line, written at close> |

## What Claude does
- <…>

## What the PM retains
- <…>

## Test
- Prompt used: <public or synthetic input>
- Observed result: <pasted result summary, or "not tested">
- Review notes (trigger clarity / missing context / usefulness / unsupported assumptions / ownership / scope): <…>

## Revision
- <one revision made, or "none needed because …">

## Reuse
Copy the folder `<skills-dir>/<slug>/` into another project's skills folder (`.claude/skills/` for Claude Code, `.agents/skills/` for Codex).
Remove the `disable-model-invocation` line (in Codex, delete `agents/openai.yaml`) later if you want it chosen automatically.

## Decision record
| Check-in | Recommendation | Your decision | Reason |
|---|---|---|---|
| Scope check | | | |
| Ownership check | | | |
