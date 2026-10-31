# Short commands

Plugin skills always carry the plugin prefix, so the commands are `/nlyu-pm:scout`,
`/nlyu-pm:prototype`, `/nlyu-pm:prd`, and `/nlyu-pm:create-skill`. A PM can get the short
forms `/scout`, `/prototype`, `/prd`, and `/create-skill` in one workspace folder through
four small project skills that do nothing but run the plugin skill of the same name.

Readiness (check 2) asks once whether to add them. Write them only if the PM says yes,
and never overwrite a folder under `.claude/skills/` that already exists. Each forwarder
is `.claude/skills/<name>/SKILL.md` with exactly this content, `<name>` replaced by
`scout`, `prototype`, `prd`, or `create-skill`:

```markdown
---
name: <name>
description: Short form of /nlyu-pm:<name>. Runs only when the PM types /<name>.
disable-model-invocation: true
---

Run the plugin skill `nlyu-pm:<name>` now with the Skill tool, passing any text the PM
typed after the command through unchanged. Do nothing else first; the plugin skill owns
the whole stage from here.
```

Rules:

- The forwarders live in the workspace folder only. They are not installed globally,
  so a new folder gets the question again.
- In in-repo mode they are untracked files inside the PM's repository, like
  `outputs/` and `.pm/`; offer to add `.claude/skills/` to the same ignore entry.
- Status lines, summary lines, and file text keep the full command names, so a reader
  who did not add the short forms is never misled.
- If the PM declines, say that the full names work in every folder and move on.
