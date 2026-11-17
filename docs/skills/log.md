# /nlyu-pm:log

The capture skill. It files one piece of product evidence in about two minutes: a call
note, a support thread, a message, a review, or a link. Use it any time, as often as you
like. It has no check-in and never ranks anything.

## What it produces

One to three new signals in the workspace's evidence base (`.pm/evidence/`), any verbatim
quote in the quote bank, the text itself saved under `.pm/fetches/` so the quote can be
checked later, and an updated evidence line on the opportunity it belongs to.

## Before you start

Only a workspace folder. If the product is set up, the note attaches to an opportunity in
your backlog. If it is not, the note is filed as unassigned and picked up when you set the
product up.

## How a run goes

Type the command and paste what you have:

```text
/nlyu-pm:log  Call with an ops lead: "we export to a spreadsheet every Friday because the dashboard can't filter by region"
```

A link works too, and so does the name of a file you dropped in `.pm/inbox/`.

1. **Take it in.** Claude works out what it is: a note from inside your company, text you
   copied from a public page, or a public link it fetches once.
2. **Save it.** A note from inside your company is saved with personal names, email
   addresses, phone numbers, and account numbers removed, and the speaker becomes a role
   ("an operations lead at a customer"). The original is not kept.
3. **Log it.** One signal per distinct claim, at most three, each with its source, its
   date, and what the note itself supports ("one customer"). The user's own words, up to
   40 of them, go in the quote bank. Your summary of what someone said is logged as a
   claim, not as a quote.
4. **Attach it.** To the opportunity it speaks to, as counter-evidence if it cuts against
   one, or as a new candidate if it fits none. If two opportunities fit equally, Claude
   asks which, and that is the only question.
5. **Report.** Three lines: what was filed, where it attached and that opportunity's
   evidence as it now stands, and, if the note cuts against the opportunity you are
   working on, a suggestion to run the weekly refresh.

## Rules it follows

- Notes from inside your company stay on your computer, are labelled
  `Evidence (internal)` everywhere they appear, and are never sent anywhere by the plugin.
- An excerpt, never an export. A spreadsheet of many customers' records is declined; you
  are asked for the one or two excerpts that matter.
- No password, token, or key, and nothing fetched behind a sign-in.
- Nothing is logged that the saved text does not support, and composed words never go in
  quotation marks.
- It never changes the order of your backlog, never edits a file under `outputs/`, and
  never marks a stage stale.

## Where the details live

`plugins/nlyu-pm/skills/log/SKILL.md` is the skill, and
`plugins/nlyu-pm/resources/evidence-base.md` describes the evidence base, the backlog,
and the saved files.

## In Codex

Run it as `$log`, with the note in the same message.
