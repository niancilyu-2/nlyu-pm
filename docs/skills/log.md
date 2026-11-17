# /nlyu-pm:log

The capture skill. It files one piece of product evidence in about two minutes. Use it
any time. It has no check-in and never ranks anything.

## What it produces

New entries in the workspace's evidence base, the text saved so any quote can be checked
later, and an updated evidence count on the opportunity it belongs to.

## Before you start

Only a workspace folder. If the product is not set up yet, the note is filed as
unassigned and picked up later.

## How a run goes

Type the command and paste what you have:

```text
/nlyu-pm:log  Call with an ops lead: "we export to a spreadsheet every Friday because the dashboard can't filter by region"
```

A link works too, and so does a file you dropped in `.pm/inbox/`.

1. **Save it.** A note from inside your company is saved with names, emails, phone
   numbers, and account numbers removed. The original is not kept.
2. **Log it.** Up to three claims, each with its source and date. The person's own words
   go in the quote bank. Your summary of what someone said is logged as a claim, not a
   quote.
3. **Attach it.** To the opportunity it speaks to, as counter-evidence if it cuts against
   one, or as a new candidate if it fits none.
4. **Report.** Three lines: what was filed, where it attached, and whether it cuts against
   what you are working on.

## Rules it follows

- Notes from inside your company stay on your computer and are labelled internal
  wherever they appear.
- An excerpt, never an export of many people's records.
- No password, token, or key, and nothing fetched behind a sign-in.
- It never changes the order of your backlog.

## Where the details live

`plugins/nlyu-pm/skills/log/SKILL.md` is the skill, and `resources/evidence-base.md`
describes the evidence base and backlog.

## In Codex

Run it as `$log`, with the note in the same message.
