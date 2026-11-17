# Test walkthrough

How to run the whole flow yourself. Setup takes about 15 minutes and the three product
stages about three hours in all. Everything Claude produces is a file you can open in any
text editor.

Not installed yet? Do [SETUP.md](SETUP.md) first.

Using OpenAI Codex? Type `$scout`, `$prototype`, `$prd`, `$log`, `$weekly`, and
`$create-skill` instead of the `/nlyu-pm:` commands, and `/new` where this says `/clear`.
The prototype is always a standalone HTML file there.

## 1. Start

Open your `pm-workspace` folder, or the top folder of your own repository, in the Claude
desktop app's Code tab or in a terminal running `claude`.

## 2. Readiness

Type `/nlyu-pm:scout`. On the first run it checks the folder, Git, your browser, and web
access, asks you to type `/design` and say what happened, and offers to choose a product
now so the code downloads today. It ends with `Ready`, `Ready with fallback`, or
`Blocked`.

Choose *stop after setup* to continue another day, or *continue* to go straight on.

From here every reply ends with a status line such as
`Scout · step 5/11 · fetches 6/20 · 14 min · sources clean`. If it ever says
`sources CHANGED`, stop and note the step.

## 3. Pick a product and a focus area

The first question is your own product (BYOP, bring your own project or repo) or an
example case. A *case* is a prepared example product. A *lane* is one focus area inside
it, which you research and then prototype as a single flow.

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

Fullest research: Immich or Home Assistant. Quickest run: Plane, Intake and triage.

**BYOP.** Open the top folder of your repository, or choose *BYOP* and give a repository
URL, a folder path, or a zip. Read access is enough. Claude asks which sources to read,
who you design for, your brief, and the focus area, then shows the package at a check-in.
This takes about fifteen minutes, and nothing in your repository is modified.

## 4. Discovery: `/nlyu-pm:scout` (60 min)

Claude gives a short tour of the product, downloads the code, and shows the list of
sources it will read. Say "no" to take the list as shown, or add and skip sources. It
then works through them in order and collects user quotes as it goes.

1. **Research check.** What people say, the strongest quotes, and the gaps. You say
   continue, ask for one more look, or narrow the focus.
2. **Evidence review.** A separate read-only reviewer checks every quote and label
   against what was actually fetched. Claude tells you what it found and fixed. You
   decide something only if an opportunity has to be dropped.
3. **Priority check.** Three opportunities in Now, Next, Later order. You pick what goes
   first and why.

Files: `outputs/01-discovery.md`, `outputs/01-discovery-review.md`. Then start a new
session in the same folder (in a terminal, `/clear`).

## 5. Prototype: `/nlyu-pm:prototype` (60 min)

Claude shows the quotes behind your chosen opportunity and asks for one user, one job,
where the task starts and ends, and two alternate states. **Flow check-in:** approve or
edit.

Claude then builds the prototype. If Claude Design is available it gives you one
instruction to run `/design`; otherwise it writes the HTML file itself.

Open `outputs/prototype/index.html` from your workspace folder and click through it.
Claude walks the flow with you and proposes one change. **Prototype check-in:** approve
the revised version.

Files: `outputs/02-prototype.md`, `outputs/prototype/index.html`. Then a new session.

## 6. PRD: `/nlyu-pm:prd` (45 min)

Claude reads the earlier files and the code, then drafts the PRD. **Scope check-in:**
approve goals, behaviour, and acceptance criteria, and pick two customer quotes.

A separate read-only reviewer checks the draft. **Handoff check-in:** for each finding,
fix it, turn it into an engineering question, or accept it with a note. Blocking findings
must be fixed.

Files: `outputs/03-prd.md`, `outputs/03-prd-review.md`.

## 7. Skill builder: `/nlyu-pm:create-skill` (30 min, any time)

Bring one task you repeat, or paste a checklist you already use. Claude asks four
questions, shows the proposed skill at a check-in, then writes it.

To test, open a second session in the same folder, find your skill in `/skills`, run it
on sample input, and paste the result back. Claude proposes at most one revision.

Files: `.claude/skills/<name>/SKILL.md`, `outputs/04-skill-summary.md`.

## 8. Between cycles: `/nlyu-pm:log` and `/nlyu-pm:weekly`

**Log (2 min, any time).** Type `/nlyu-pm:log` and paste a call note, a support thread, a
review, or a link. Claude saves it, removes names and contact details from anything
internal, and attaches it to an opportunity in your backlog. No check-in.

**Weekly (15 min).** Type `/nlyu-pm:weekly`. Claude gathers the week's notes, re-reads the
public sources, and writes a digest with a stakeholder update you can paste. One question
at the end: keep the order, make the one change it recommends, or decide later.

Files: `outputs/weekly/<year>-W<week>.md`.

**Starting at a later stage.** For a small change you can run `/nlyu-pm:prototype` or
`/nlyu-pm:prd` directly once the product is set up (tell scout "set up only"). Each asks
for what the earlier stage would have supplied, and the file says which inputs you typed
in.

## 9. Problems

| You see | Do |
|---|---|
| `/nlyu-pm:` commands missing | Desktop app: Settings, Plugins, check **nlyu-pm** is installed and enabled, then a new session. Terminal: `/plugin marketplace update nlyu-pm`, then `/plugin install nlyu-pm@nlyu-pm` |
| Repeated permission prompts | Choose the option that stops asking for the session |
| `Blocked` | Do the action printed, then `/nlyu-pm:scout` again |
| Web search policy error | Continue. Send the error text to whoever manages your account |
| Path-too-long error on Windows | Ask Claude to run `git config --global core.longpaths true`, then `/nlyu-pm:scout` |
| `/design` does nothing | Claude builds the prototype as an HTML file |
| `sources CHANGED` in the status line | Stop and note the step. In your own repository it may be your own edit; Claude asks before assuming |
| BYOP and most research sources are empty | Expected for a private or new product. Claude uses the code, competitors, and anything you paste, and marks the brief provisional |
| Lost your place | Start a new session in the same folder and run the current stage command. It resumes from the files |
| Your new skill is not in `/skills` | Test from a new session in the same folder. If it is still missing, tell Claude |

## 10. Feedback

To report how a run went, open an issue on GitHub with what you finished, how long it
took, and anything confusing, with the step number. Check files from `outputs/` before
attaching them if you logged notes from inside your company or added a source behind a
sign-in.
