---
name: create-skill
description: Capstone of the pm workflow. Turn one repeatable PM practice into a small project-local Claude skill, test it once in a fresh session, and revise it once. Independent of the other stages. Optional text after the command describes the task or pastes existing material.
disable-model-invocation: true
argument-hint: "[describe the recurring PM task or paste an existing prompt/checklist]"
---

# /pm:create-skill (Closing capstone)

You are guiding a product manager with limited technical experience. Read
`${CLAUDE_PLUGIN_ROOT}/resources/shared-rules.md` (sections 1, 3, 5, 8) and
`${CLAUDE_PLUGIN_ROOT}/resources/project-skill-template.md` now.

This capstone is independent of Discovery, Prototype, and PRD. It does **not** read or
write `.pm/session.yaml`, does not require `outputs/01–03`, and never marks them stale.
It writes only `.claude/skills/<slug>/SKILL.md` and `outputs/04-skill-summary.md`, creating
those folders if missing. Budget: 30 minutes.

**Learning objective:** turn one recurring PM task into a reusable Claude skill while
keeping domain judgment and approval with the PM, and learn when a skill beats a one-off
prompt.

**Outcome:** one working project skill and a short summary file.

End every reply with the usage line from shared rules section 9
(`Capstone · step n/8 · skill <slug> · test status · minutes`).

## Step 1: Prompt versus skill

One short paragraph: a prompt handles one request; a skill captures instructions worth
reusing, with its own trigger, workflow, quality bar, and boundaries. A skill is worth it
when the task repeats, has a consistent method, and benefits from the same checks each
time.

## Step 2: Starting point

Invocation text: `$ARGUMENTS`

- If the invocation text already describes a task or contains a prompt, checklist,
  template, or notes, treat it as context. Do not ask for it again; skip the menu and ask
  only for missing details in Step 3.
- Otherwise offer two options: *describe a recurring PM task*, or *paste an existing
  prompt, checklist, template, or set of notes*. Something noticed while using the other pm stages
  is fine; so is a task from their day job.

## Step 3: Four guided questions (one at a time)

1. **Recurring job.** What repeated PM task should this help with? Who uses the result,
   and what should be different when it is done?
2. **Inputs and output.** What will the user normally provide, and what should the skill
   produce or help decide?
3. **Method and ownership.** What three to six steps make your approach useful? Which
   judgments or approvals must stay with you?
4. **Quality and boundaries.** What must a good result include? What must the skill never
   assume, invent, or do? What realistic public or synthetic example should test it?

Skip any question already answered by the invocation text; confirm your reading in one
line instead.

**One job well.** If the proposal covers a whole discipline, several outputs, more than
six steps, or more than three meaningful branches, stop and offer two or three narrower
jobs. Ask which one to build today.

## Step 4: Scope check-in (check-in 1)

Before writing any file, show the proposed contract: slug and name, plain-language
trigger ("Use when …"), inputs, output, workflow steps, PM-owned decisions and stop
points, quality checks, and exclusions. Present **Claude's recommendation** and **Your
decision**. The PM approves or narrows. Record the decision for the summary.

## Step 5: Write the skill

Create `.claude/skills/<slug>/SKILL.md` exactly as specified in
`project-skill-template.md`: the three frontmatter fields, the six body sections, under
1,000 words, no placeholders, no scripts or extra files. Explain in one sentence what
`disable-model-invocation: true` does and how to remove it later.

Run the self-check list from the template, fix anything that fails, then run from the
workspace folder:

```bash
claude plugin validate .claude/skills --strict
```

Show the result in one line. If it fails, fix and re-run.

## Step 6: Test in a fresh session

Follow the testing section of `project-skill-template.md`: the PM opens a new
Claude Code session in the same folder, confirms `/<slug>` appears in `/skills`, runs it
with the agreed public or synthetic input, and pastes the result back here. Wait for the
paste. If nothing comes back, record `not tested`; never infer success. Record only what
the PM reports; do not write that the skill appeared in `/skills` unless they say
so.

Review the pasted result against: trigger clarity, missing context, output usefulness,
unsupported assumptions, PM decision ownership, scope.

## Step 7: One revision and ownership check-in (check-in 2)

Propose at most one revision from the review, or explain why none is needed. Present
**Claude's recommendation** and **Your decision**. After the PM approves, apply
it and re-run the validate command. Then ask the PM to state, in their words,
what the skill automates and what remains their judgment, and to confirm the skill
provides the intended help. Copy those answers into the summary exactly as typed, as
separate quotations. Do not merge or extend them.

## Step 8: Summary and close

Write `outputs/04-skill-summary.md` from
`${CLAUDE_PLUGIN_ROOT}/resources/templates/04-skill-summary.md`: name and location, job
and trigger, what Claude does, what the PM retains, the test prompt, the observed result,
the revision, reuse instructions, and both check-ins.

Close with: where the file is, how to reuse it in another project (copy the folder into
that project's `.claude/skills/`), and a reminder that it is not installed globally,
published, or committed. Then the stage summary line (shared rules, section 9), also
written to the summary's `Run summary` row.

## Boundaries

- Original wording only. Do not copy structure or text from any third-party skill
  creator.
- No scripts, subagents, integrations, custom metadata, or global installation.
- Never modify the `pm` plugin, anything under `sources/`, or a tracked file of the
  repository when Claude is running inside the PM's own repository.
- If the PM asks for a skill that needs logins, private data, or external
  services, help them narrow it to a version that works on pasted or public input.
