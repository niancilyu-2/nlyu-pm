# Test walkthrough

How to run the whole flow yourself. Readiness takes about 15 minutes and Discovery about
60, plus about 15 to build the case when you bring your own product. The three product
stages take about three hours in all; the skill builder is an independent 30-minute
exercise. Everything Claude produces lands in files you can open in any text editor.

Not installed yet? Do [SETUP.md](SETUP.md) first.

## 1. Start

Open your `pm-workspace` folder (or, for BYOP, the top folder of your repository) in the
Claude desktop app's Code tab, or in a terminal by typing `claude` there.

## 2. Readiness

Type `/nlyu-pm:scout` (type `/nl` and pick it from the list). On the first run it:

1. prints the plugin version
2. checks the folder and decides whether it is your own repository or an empty workspace
3. checks Git
4. opens a test page in your browser and asks whether it appeared
5. fetches one public page and tries one web search
6. asks you to type `/design` and say what happened
7. offers to choose BYOP or an example case now so the download happens today
8. prints `Ready`, `Ready with fallback`, or `Blocked`

Choose *stop after setup* to continue another day, or *continue* to go straight on.

From here every reply ends with a status line:
`Scout · step 5/11 · fetches 6/20 · searches 0/8 · items 5 · quotes 3/8 · 14 min · sources clean`.
If it ever says `sources CHANGED`, stop and note the step.

## 3. Pick a track, a case, and a lane

Three words. The *track* is which product you work on: your own (BYOP, bring your own
project or repo) or an example case. A *case* is one prepared example product. A *lane*
is one focus area inside it, a part of the product you research for an hour and prototype
as a single flow. The first question is the track. Five example cases with three lanes
each, fifteen combinations. An example case takes two choices (example case, then which
one from a numbered list); ERPNext is marked advanced and downloads two repositories.
BYOP takes one choice.

| Case | You play | Lane | Prototype screen | Download |
|---|---|---|---|---|
| **Immich** | Household media steward | Backup and status confidence | Phone, 390×844 | one repo, about 30 MB |
|  |  | Finding and organizing media | Desktop, 1440×900 |  |
|  |  | Private sharing and collaboration | Phone, 390×844 |  |
| **Plane** | Product-operations lead | Intake and triage | Desktop, 1440×900 | one repo, about 20 MB |
|  |  | Planning and scheduling | Desktop, 1440×900 |  |
|  |  | Cross-project status readout | Desktop, 1440×900 |  |
| **Home Assistant** | Household co-admin | Household dashboards and defaults | Tablet, 1024×768 | one repo, under 60 MB |
|  |  | Repairs, backups, and recovery from updates | Phone web, 390×844 |  |
|  |  | Automation troubleshooting and safe edits | Desktop, 1440×900 |  |
| **Umbraco** | Content-operations editor | Draft to publish | Desktop backoffice, 1440×900 | one repo, under 60 MB |
|  |  | Pick and reuse media from the page | Desktop backoffice, 1440×900 |  |
|  |  | Languages and variants | Desktop backoffice, 1440×900 |  |
| **ERPNext** (advanced) | Inventory or procurement manager | Inventory quantity and valuation exceptions | Desktop, 1440×900 | two repos, under 60 MB each |
|  |  | Purchase-approval exceptions | Desktop, 1440×900 |  |
|  |  | Stock and Buying daily worklists | Desktop, 1440×900 |  |

Research differs a little by case. Immich, Home Assistant, Umbraco, and ERPNext have a
searchable forum; Plane's community is on Discord, which Claude cannot read. Immich,
Plane, and Home Assistant have a phone app, so App Store reviews are included. ERPNext has
no GitHub Discussions board.

Fullest research demo: Immich or Home Assistant. Quickest run: Plane, Intake and triage.

**BYOP.** Either open the top folder of a local copy of your repository (in the Code tab,
or a terminal running `claude`; Claude asks you to confirm it is the product), or choose *BYOP* at the first question and
give a repository URL, a folder path, or a zip file. Read access is enough; a private URL
works if your computer is already signed in, and otherwise Claude asks you to run the
clone line yourself or to use a zip. Claude then asks which built-in source groups to use,
whether there is anything else to read, and whether any source behind a sign-in you hold
should be included, and writes your answers to `.pm/sources.yaml`. It reads the README and
folder tree, asks who you design for, what your brief is, and which focus area, proposes
the code entry points, lists which research sources exist for this product, and shows the
package at a **case check-in**. About fifteen minutes before research starts. Nothing in your repository
is modified; `outputs/` and `.pm/` are the only new folders, and Claude offers to hide
them from `git status`.

## 4. Discovery: `/nlyu-pm:scout` (60 min, plus 15 to build a BYOP case)

Claude asks for the track, the case, then the lane, gives a short tour, downloads the
repository, asks for two or three search words, shows the list of sources it will read in
order with who each one hears from and what does not exist for this product (for BYOP,
the list you confirmed when the case was built), and asks once whether to add or skip any (say "no" to take the list as shown; say "also read the Stack Overflow
tag" or "skip app reviews" to change it, now or at any later point). Then it works through the sources in order: forum,
GitHub discussions by upvotes, GitHub issues by reactions, Lemmy, Mastodon, Hacker News,
App Store reviews, adoption numbers, competitor pages against their copy from a year ago,
release notes. It shows one number or quote per source and collects user quotes as it
goes.

Two check-ins, with a review between them:

1. **Research check.** Coverage, a triangulation table, the two strongest quotes,
   contradictions, gaps. You say continue, ask for one more fetch, or narrow the framing.
2. **Evidence review** (no decision from you unless a finding changes which opportunities
   stand). A separate read-only reviewer checks every quote against the text saved when
   it was fetched, every Evidence label against what was fetched, every constraint against
   the code, and a fixed coverage floor. Claude reports what it found and fixed in a few
   lines; a floor not met means the brief is saved provisional.
3. **Priority check.** Three opportunities in Now, Next, Later order with a quote under
   each. You pick the Now item, then your reasons (several allowed, or your own words).

Check: every claim is labelled Evidence, Inference, Assumption, or Constraint; every
Evidence item has a link, dates, and a saved file; `outputs/01-discovery-review.md` lists
every quote as verified, differing, or not found; Claude's recommendation and your
decision are separate blocks.

Files: `outputs/01-discovery.md`, `outputs/01-discovery-review.md`, `.pm/fetches/`,
`.pm/session.yaml`. The stage closes with a summary line: minutes, fetches, items, quotes
verified, gaps, findings, status. Then start a new session in the
same folder (in a terminal, type `/clear`).

## 5. Prototype: `/nlyu-pm:prototype` (60 min)

Claude shows the quotes behind your chosen opportunity and asks: one actor, one job, where
the task starts and ends, the main action, two alternate states. **Flow check-in:** approve
or edit.

Claude reads the product's design files and writes a brief. Then one of two paths:

- **Claude Design available.** Claude prints one instruction: type `/design`, paste the
  brief, ask Design to export a single HTML file to `outputs/prototype/index.html`, then
  run `/nlyu-pm:prototype` again.
- **Not available.** Claude writes the HTML file itself and opens it.

In your workspace folder, open `outputs/prototype/` and double-click `index.html`
(Finder or File Explorer). Click through the main path, use the demo
buttons to see the two alternate states, try Tab to move between controls.

Claude walks the flow with you, lists findings, and proposes one change tied to evidence.
**Prototype check-in:** approve the revised version, note any trade-offs.

Files: `outputs/02-prototype.md`, `outputs/prototype/index.html`. Then a new session in
the same folder (in a terminal, `/clear`).

## 6. PRD: `/nlyu-pm:prd` (45 min)

Claude reads the earlier files, looks at the code for likely touchpoints, and drafts the
PRD. **Scope check-in:** approve goals, non-goals, behaviour, alternate states, acceptance
criteria, and pick two of three customer quotes.

A separate read-only reviewer checks the draft and returns findings. **Handoff check-in:**
for each finding, fix it in the PRD, turn it into an engineering question, or accept it
with a note. Blocking findings must be fixed.

Check: technical statements are labelled Verified with a file path, Inferred, or
Engineering-owned; no estimates, delivery dates, or story points; status reads
`ready-for-engineering-review`.

Files: `outputs/03-prd.md`, `outputs/03-prd-review.md`. Then a new session in the same
folder (in a terminal, `/clear`).

## 7. Skill builder: `/nlyu-pm:create-skill` (30 min, any time)

Independent of the other stages; run it in the same folder whenever you like. Bring one
repeated task from your job, or paste a checklist you already use.

Claude asks four questions, shows a proposed skill at the **scope check-in**, then writes
`.claude/skills/<name>/SKILL.md` and validates it. Claude Code asks permission before
writing that file even if you allowed edits earlier; choose Yes.

To test: open a second session in the same folder (a new Code tab session, or a second
terminal running `claude`), type `/skills` and
find your command, run it with sample input. Paste the result back into the first session.
Claude proposes at most one revision and asks what the skill automates and what stays with
you.

Files: `.claude/skills/<name>/SKILL.md`, `outputs/04-skill-summary.md`.

## 8. Problems

| You see | Do |
|---|---|
| `/nlyu-pm:` commands missing | Desktop app: Settings, Plugins, check **nlyu-pm** is installed and enabled, then a new session. Terminal: `/plugin marketplace update nlyu-pm`, then `/plugin install nlyu-pm@nlyu-pm` |
| Repeated permission prompts | Choose the option that stops asking for the session |
| `Blocked` | Do the action printed, then `/nlyu-pm:scout` again |
| Web search policy error | Continue. Send the error text to whoever manages your account |
| A source returns 403 or 429 | Claude logs a gap and moves on |
| Path-too-long error on Windows | Ask Claude to run `git config --global core.longpaths true`, then `/nlyu-pm:scout` |
| `/design` does nothing | Claude uses the HTML path |
| `sources CHANGED` in the status line | Stop and note the step. In your own repository, it may be your own edit in another window; Claude asks before assuming |
| BYOP and most research sources are empty | Expected for a private or new product. Claude says so up front, uses the code, competitors, anything you paste, and any source you set up with your own sign-in, and marks the brief provisional |
| Lost your place | Start a new session in the same folder (in a terminal, `/clear`), then the current stage command. It resumes from the files |
| Your new skill not in `/skills` | Test from a new session in the same folder. If it is still missing, tell Claude; the skill's folder name and its `name` line must match, and Claude fixes that for you |

## 9. Feedback

If you want to report how a run went, open an issue on GitHub with, per stage:

1. Finished? How long?
2. One thing Claude did that helped, one decision you kept.
3. Anything confusing or wrong, with the step number.

Attach files from `outputs/` if you can. They contain public information and made-up
data, plus items marked `PM-held access` if you added a source behind a sign-in; check
those before sharing.
