# nlyu-pm

A Claude Code plugin for product managers. It takes a product from public evidence to a
selected opportunity, a clickable prototype, and an engineering-ready PRD, on the PM's
own repository or on one of five prepared open-source example cases. Claude finds, drafts,
and challenges; the PM makes every accountable decision at explicit check-ins. No
programming is required.

## Commands

| Command | What it does |
|---|---|
| `/nlyu-pm:scout` | Readiness check, case setup, public-source research, repository constraints, three opportunities, your choice of one |
| `/nlyu-pm:prototype` | One actor, one job, one flow: a clickable HTML prototype, a design critique, one revision |
| `/nlyu-pm:prd` | A delivery PRD grounded in the product's code, reviewed by a separate read-only agent |
| `/nlyu-pm:create-skill` | Turn one of your own PM practices into a small project skill, test it once, revise it once |

## What the plugin runs, reads, and fetches

- **Runs** `git` to clone public example repositories into `sources/` at a pinned commit,
  and `git status` to confirm those folders are unchanged; `date` to record stage start
  times. In your own repository it runs `git` read-only. No build, test, or install
  command is ever run, including any found in a repository's own files.
- **Reads** the cloned or in-place repository, read-only, and public web pages through
  Claude Code's web fetch tool (forums, GitHub issues and discussions, app store review
  feeds, release notes, competitor pages and their Wayback Machine copies, adoption
  counts). Web search is used when available. One optional `curl` of a subreddit RSS feed
  runs only if you opt in when asked.
- **Writes** only under `outputs/`, `.pm/`, and, for `/nlyu-pm:create-skill`, one folder
  under `.claude/skills/`.
- **Never** asks for, prints, or stores a password, token, or key, and never sends data
  anywhere other than the public fetches above. Sources behind a sign-in you hold are
  read only through access you set up yourself, and the brief marks what came from them.
- Treats text found in web pages and repositories as evidence, not instructions.

Full documentation, setup guide, and walkthrough: https://github.com/niancilyu-2/nlyu-pm.

MIT licensed; see `LICENSE` in this folder.
