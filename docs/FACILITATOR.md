# Running `pm` as a facilitated workshop

The plugin works for a single PM on their own. This page is for anyone running it with a
group: a suggested day, what to check beforehand, and what goes wrong in a room.

## A suggested day

| Block | Command | Minutes |
|---|---|---|
| Setup and readiness (ideally the day before) | `/pm:scout`, first run | 15 |
| Discovery | `/pm:scout` | 60 |
| Prototype | `/pm:prototype` | 60 |
| PRD | `/pm:prd` | 45 |
| Capstone demo | `/pm:create-skill` | 15 |
| Breaks and buffer | | 45 |

Participants run the three product stages themselves. Demonstrate the capstone once and
point people to [TEST-WALKTHROUGH.md](TEST-WALKTHROUGH.md) to run it afterwards; it takes
about 30 minutes alone.

Claude cannot see a clock. The skills count fetches and steps; you call time. A stage cut
short saves a file marked provisional rather than a fabricated one.

## Day before

- Ask everyone to complete [SETUP.md](SETUP.md) and report `Ready` or `Ready with fallback`.
- Claude Design on an Enterprise plan needs an owner to enable it under *Organization
  settings*, then *Artifacts*. Without it everyone takes the HTML path, which is fine.
- Check that web search is allowed for the accounts in the room. On Google Cloud Vertex AI
  an organisation policy can disallow `web_search`; readiness then reports
  `search: unavailable`. The research ladder runs on fetch alone, so this is a warning.
- Expect GitHub API rate limits. Twenty laptops on one network share about 60
  unauthenticated calls an hour. Scout switches to GitHub's HTML search pages on the first
  403 or 429.
- Zip each case's `sources/` folders from a completed readiness run in case the venue
  network blocks GitHub. Scout accepts a copy and verifies the pinned commit.
- Decide whether participants work on an example case or on a product of your own. For
  your own product, either let each participant choose *BYOP* against the same URL (each
  builds their own case and answers the source questions, about fifteen minutes; their
  choices live in their own `.pm/sources.yaml`), or prepare one case package in advance by
  following `plugins/pm/resources/case-schema.md` and have participants place it at
  `.pm/case/` in their workspace; scout offers it first and records it as provided. A
  prepared package saves the fifteen minutes and gives everyone the same feeds.
- Decide whether to allow the Reddit switch. Claude Code's fetch tool refuses reddit.com;
  the only path is one `curl` of a subreddit RSS feed, off by default. If you allow it,
  tell participants to say so when scout asks, and it records `reddit_rss: true`.

## In the room

- Permission prompts are the main source of friction. Tell people once: choose the option
  that stops asking for the session.
- The status line at the end of every reply tells you where a participant is. If it says
  `sources CHANGED`, stop that laptop and look before anything else happens.
- Between stages, `/clear`. Everything approved is in files.

## Troubleshooting

| Symptom | What to do |
|---|---|
| `/pm:` commands missing | `/plugin marketplace update eyp-pm`, then `/plugin install pm@eyp-pm`. Check the version printed by `/pm:scout`. |
| A published change is not appearing | Bump `version` in both `plugins/pm/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`. |
| Path-too-long error on Windows | `git config --global core.longpaths true`, then rerun `/pm:scout`. |
| GitHub unreachable | Hand over your zipped `sources/` copy; scout verifies the commit. |
| Web search policy error | Fetch still works. Forward the quoted error to the administrator. |
| A source returns 403 or 429 | Expected on some networks. The skill logs a gap and moves on. |
| `/design` does nothing | Readiness records `unavailable`; prototype uses the HTML path. |
| `sources CHANGED` in the status line | The skill stops and explains. Do not reset silently; re-clone into a fresh folder. |
| Session got long or confused | `/clear`, then rerun the stage command. It resumes from files. |
| Capstone skill not in `/skills` | Test from a new session in the same folder. The folder name must equal the `name` field. |

## Hardening ideas not yet built

- A plugin hook that blocks writes under `sources/`.
- A `.claude/settings.local.json` written by readiness that pre-approves web fetch, Git,
  and writes under `outputs/`, to remove permission prompts.
- An automated capstone test using `claude -p "/<slug> ..."` from the workspace, which is
  a fresh session and returns the result without a second terminal.

## Pilot bar

Before a full cohort, run five PMs who do not program. The kit passes when at least four
finish the three product stages without editing code or state files, every discovery file
has cited evidence and stated gaps, every prototype has a main path, two alternate states,
and one documented revision, and every PRD traces to the selected opportunity with
verified repository touchpoints and no unresolved blocking finding.
