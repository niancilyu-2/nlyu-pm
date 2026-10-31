# /pm:create-skill

The skill builder. It turns one repeatable practice of your own into a small Claude skill that
lives in your project, tests it once in a fresh session, and revises it once. It is
independent of the other three skills and needs none of their files.

## What it produces

`.claude/skills/<name>/SKILL.md`, a skill you can run as `/<name>` in that folder and copy
to other projects, and `outputs/04-skill-summary.md`: its job and trigger, what Claude does,
what stays with you, the test and its result, the revision, and reuse instructions.

## How a run goes

1. **Prompt versus skill.** One paragraph: a prompt handles one request; a skill captures a
   method worth reusing, with its own trigger, steps, quality bar, and boundaries.
2. **Starting point.** Describe a recurring task, or paste a prompt, checklist, or notes
   you already use. If you typed the task after the command, Claude skips this and asks
   only for what is missing.
3. **Four questions**, one at a time. The recurring job and who uses the result. What you
   provide and what comes out. The three to six steps that make your approach work, and
   which judgments must stay with you. What a good result must include, what the skill must
   never assume or invent, and a safe example to test it on. If the idea covers a whole
   discipline or several outputs, Claude offers two or three narrower jobs instead.
4. **Scope check-in.** Claude shows the proposed name, trigger, inputs, output, steps, your
   decision points, quality checks, and exclusions. You approve or narrow it before any
   file is written.
5. **Write and validate.** One file, under 1,000 words, manual invocation only so it cannot
   fire unexpectedly. Claude runs a self-check and the plugin validator.
6. **Test in a fresh session.** You open a second terminal in the same folder, confirm the
   skill is listed, run it on the agreed example, and paste the result back. Claude reviews
   it for trigger clarity, missing context, usefulness, unsupported assumptions, and
   ownership. If nothing comes back, the summary says "not tested".
7. **One revision and ownership check-in.** Claude proposes at most one change. You approve
   it, then state in your own words what the skill automates and what remains your call.
   Your words go into the summary exactly as typed.
8. **Summary.** Written, with reuse instructions.

## Rules it follows

- Runs only when you type it. The generated skill is manual too until you remove one line.
- No scripts, subagents, integrations, or custom metadata in the first version.
- Nothing is installed globally, published, or committed.
- Writes only the skill file and the summary. Never touches the session file.

## Where the details live

`plugins/pm/skills/create-skill/SKILL.md` is the skill and
`plugins/pm/resources/project-skill-template.md` the template and self-check.
