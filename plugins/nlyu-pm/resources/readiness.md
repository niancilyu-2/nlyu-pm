# Readiness check (first run of `/nlyu-pm:scout`)

Run this the first time `/nlyu-pm:scout` starts in a workspace, or whenever `readiness.status`
is `not-run` or `blocked`. It should take under ten minutes. Run it before you plan to start so
problems surface early.

Report only one of three words, then the next action:

| Result | Meaning |
|---|---|
| `Ready` | Everything works, including web search and Claude Design. |
| `Ready with fallback` | Fetch works but web search or Claude Design does not; the source ladder and the HTML path cover both. |
| `Blocked` | Something required is missing. State the single next action. |

## Checks, in order

1. **Plugin version.** Read `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json` and say
   "You are running the nlyu-pm plugin version X." (This is how a stale install is spotted.)
2. **Workspace folder and mode.** Apply the folder checks in `workspace.md` to decide
   between wrapper mode (an empty folder; an example case, or BYOP by URL, path, or zip)
   and in-repo mode (the PM started inside their own repository, which is BYOP). In in-repo mode confirm
   with the PM that this repository is the product. Create `.claude/skills/`,
   `outputs/prototype/`, `.pm/`, and in wrapper mode `sources/`. Write `.pm/session.yaml`
   with `readiness.status: not-run`, `workspace_mode`, and `outputs_dir` if it does not
   exist.
3. **Git.** Run `git --version`. Missing git is `Blocked`; the next action is to install
   Git for Windows or Xcode command-line tools, then rerun.
4. **Open a local HTML file.** Write a tiny file `outputs/readiness.html` (one heading that
   says "Your browser can open prototypes") and open it:
   `start outputs\readiness.html` on Windows, `open outputs/readiness.html` on macOS,
   `xdg-open` on Linux. Ask the PM whether a browser tab opened. Record
   `browser_test: confirmed | unconfirmed`. Unconfirmed is a warning, not a block;
   tell them they can double-click the file in their file manager later. Delete the file
   afterwards.
5. **Public web, two parts.** First, fetch one JSON feed you can verify, for example
   `https://hn.algolia.com/api/v1/search?query=open%20source&tags=story&hitsPerPage=1`. If the
   fetch tool is unavailable or denied, record `web: unavailable`; this is `Blocked`
   unless an offline research pack has been provided. Second,
   run one web search (for example the product's name plus one word). If it works, record `search: ok`. If
   it returns a policy or permission error, record `search: unavailable` and put the error
   text in `notes` only. In the reply say one plain line ("Web search is switched off for
   your account; research still works") instead of showing the error. This is a warning,
   not a block, because the source ladder works on fetch alone. Ask the PM to
   forward the note to their administrator afterwards.
   Record which of the two worked under `readiness.feeds`.
   While doing this, tell the PM: "Claude Code will ask permission the first time
   it fetches a new website or runs a git command. Choosing the option that stops asking
   for this session will save you many clicks later."
6. **Claude Design.** Explain in one sentence: Claude Design is an optional way to generate
   the prototype visually; it needs a Pro, Max, Team, or Enterprise plan, and on Enterprise
   an administrator must switch it on. Ask the PM to type `/design` on its own
   line and tell you what happened: a design tool started (`available`), an "unknown
   command" message appeared (`unavailable`), or they are unsure (`unknown`). Record it.
   `unavailable` or `unknown` means `Ready with fallback`, never `Blocked`.
7. **Choose the track (optional pre-selection).** In in-repo mode the product is already
   known: say "BYOP: this repository", record `case.source: custom`, and skip to step 8;
   the case itself is built when Discovery starts. In wrapper mode ask the fork question
   from `/nlyu-pm:scout` Step 2 (header `Product`, "Which product do you want to work on?")
   with its three options, BYOP, example case (easy), example case (advanced), plus a fourth,
   **Decide later** (nothing downloads today; `/nlyu-pm:scout` asks again when Discovery
   starts). Say that picking now means the code downloads today and that they may change
   their mind when Discovery starts. No table in the reply.
   - Example case: easy asks the second question with the four easy products, as in
     `/nlyu-pm:scout` Step 2; advanced is ERPNext. Run the clone procedure in `workspace.md` and
     record `case.id`, `case.source: prepared`, `case.dir`, and `case.preselected: true`.
   - BYOP: ask the two questions in `custom-case.md` Step A (which kind of source, then
     the URL or path in plain prose), record `case.source: custom`, the URL or path under
     `case.origin`, and `case.preselected: true`. Do not offer "stop for now" or "choose
     an example case instead" alongside them; the stop question comes after step 8. The clone, the source questions,
     and the case package are built when Discovery starts.
   - Decide later: skip.
8. **Save.** Write `readiness` into `session.yaml` with `checked_at`, set
   `stage.current: setup`, and print the result line.

## After a successful check

Ask: "Stop here and continue later, or go straight into Discovery now?"

- **Stop:** set `readiness.stopped_after_setup: true`. Tell them: next time, open this
  same folder in a new session (the Code tab, or a terminal running `claude`) and run
  `/nlyu-pm:scout`. It will resume at case selection.
- **Continue:** proceed to case selection in `/nlyu-pm:scout`.

## Rerunning readiness

If `/nlyu-pm:scout` starts and `readiness.status` is `ready` or `ready-with-fallback`, do not
repeat the checks. Print "Readiness: <status> on <date>" and continue. Repeat only when the
PM asks or when a check obviously fails during the stage (for example, web fetch
now denied).
