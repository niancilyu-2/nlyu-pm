# Setup

Do this once before your first run. Pick the way you will run the plugin, then follow that
section's numbered steps; each has its own checklist and problems table. If you get stuck,
note the step number and check the problems table for your section.

## Three ways to run it

| Way | User profile |
|---|---|
| [**Claude desktop app** (Code tab)](#claude-desktop-app-about-15-minutes) | Recommended / non-technical users. |
| [**Claude Code in a terminal** (CLI)](#claude-code-in-a-terminal-cli-about-20-minutes) | Recommended / technical people. |
| **claude.ai in a browser** | Not recommended (complex install and project setup process). |

## What you need

- **A Mac or Windows laptop** that you can install software on. If it is a company
  laptop, you may need IT to allow the installs in your section.
- **A paid Claude subscription.** Claude Code is part of the Claude Pro plan, currently
  US$20 a month, and of the Max, Team, and Enterprise plans. The free plan does not
  include it. Check current prices at https://claude.com/pricing.
- **The Claude desktop app** from https://claude.ai/download, or, for the terminal way,
  Claude Code installed in step 3 of that section.

## Words used in this guide

| Word | What it means here |
|---|---|
| Code tab | The part of the Claude desktop app where Claude works inside a folder on your laptop. This is Claude Code. |
| Terminal | A plain text window on your laptop where you type a line and press Enter. The other place Claude Code runs. |
| Session | One conversation with Claude Code. You start a new one for each stage. |
| Command | A line that starts with a slash, such as `/nlyu-pm:scout`; everything else you type is plain English. |
| Plugin | An add-on that gives Claude Code the `/nlyu-pm:` commands used here. |
| Folder | A folder on your laptop. Everything Claude writes lands in the workspace folder you pick. |
| Git | A free tool that downloads a product's code. Claude uses it for you; you never type Git commands. |
| Repository | A product's source code, stored on a site like GitHub. Claude reads it; it never changes it. |
| Case and lane | A case is one prepared example product. A lane is one focus area inside it: a part of the product you research for an hour and prototype as a single flow. Your own product (BYOP) is the other choice. |

---

## Claude desktop app (about 15 minutes)

Recommended for non-technical users: a few clicks, no terminal.

### 1. Account and app

1. Subscribe to Claude Pro, or sign in to the account your company provides. Pro, Max,
   Team, and Enterprise all include Claude Code.
2. Download and install the Claude desktop app from https://claude.ai/download, open
   it, and sign in with that account.
3. Click the **Code** tab in the app. The first time, it may offer to set up Claude
   Code; accept.

### 2. Install Git

Claude downloads the product's code with Git, which the app does not include.

- **Windows.** Download Git for Windows from https://git-scm.com/downloads/win, run the
  installer, accept the defaults, then quit and reopen the Claude app.
- **macOS.** Nothing to do now. The first time Claude uses Git, macOS shows a dialog
  offering to install the command line tools. Click *Install*, wait for it to finish,
  then run `/nlyu-pm:scout` again.

Not sure whether Git is installed? Skip this step; the readiness check in step 6 tells
you.

### 3. Pick your workspace folder

- To try an example case: create an empty folder called `pm-workspace` on your Desktop.
- To work on your own product (BYOP, bring your own project or repo): use the top folder
  of a local copy of your repository, or an empty folder if you will give Claude a URL or
  a zip instead.

### 4. Open the folder in the Code tab

In the **Code** tab, start a new session and choose the folder from step 3 when the app
asks which folder to work in. If it asks whether you trust the folder, say yes.

### 5. Install the plugin

1. Open the app's **Settings**, then **Plugins**.
2. Click **Add**, then **Add marketplace**, then **Add from a repo**.
3. Paste `https://github.com/niancilyu-2/nlyu-pm` and confirm.
4. Find **nlyu-pm** in the plugin list and click **Install**. If it asks where to
   install, choose your user account so it is available in every folder.
5. Back in the session, type `/` in the prompt box and confirm `/nlyu-pm:scout` is in
   the list. If it is not, start a new session in the same folder and look again.
   From now on, type `/nl` and pick the command from the list; you never need to type
   the full name.

### 6. Run the readiness check

1. Type `/nlyu-pm:scout` and press Enter. It checks the folder and Git, opens a test page
   in your browser and asks whether it appeared, tests web access, and asks you to type
   `/design` and say what happened (all of this is normal). It ends with `Ready`, `Ready
   with fallback`, or `Blocked`. For `Blocked`, do the action it prints and run
   `/nlyu-pm:scout` again.
2. In an empty folder it then asks whether you want BYOP or an example case. Answer now so
   the code downloads today, or choose *decide later*. If you opened your own repository,
   it instead asks you to confirm that this repository is the product.
3. When asked, choose *stop after setup*.

Claude asks permission the first time it fetches a website, runs Git, or writes a file.
Pick the option that stops asking for the session.

### Keys and commands

| To | Do |
|---|---|
| Send | Enter |
| New line without sending | Shift+Enter |
| See available commands | type `/`, or `/nl` to show only this plugin's four commands, then pick one from the list |
| Stop Claude mid-reply | Escape, or the stop button |
| Answer a multiple-choice question | click an option, or type your own answer |
| Move to the next stage | start a new session in the same folder |

### Checklist

- [ ] The Claude desktop app is installed and signed in
- [ ] `/nlyu-pm:scout` appears when you type `/`
- [ ] `/nlyu-pm:scout` reported `Ready` or `Ready with fallback`

### Running the stages

Open your workspace folder in the Code tab (step 4), then run one stage per session:

| Stage | Type |
|---|---|
| Discovery | `/nlyu-pm:scout` |
| | new session |
| Prototype | `/nlyu-pm:prototype` |
| | new session |
| PRD | `/nlyu-pm:prd` |
| | new session |
| Skill builder (independent, any time) | `/nlyu-pm:create-skill` |

Every reply ends with a status line such as `Scout · step 5/10 · fetches 6/20 · 14 min`,
and every stage closes with a one-line summary of what it spent and produced.

### Problems

| You see | Do |
|---|---|
| No **Code** tab in the app | Update the app from https://claude.ai/download, then sign in again |
| Sign-in says your plan does not include Claude Code | You are on the free plan or the wrong account. Sign out and sign in with a Pro, Max, Team, or Enterprise account |
| `/nlyu-pm:` commands missing | Settings, Plugins: check **nlyu-pm** is installed and enabled, then start a new session in the same folder |
| Readiness says Git is missing | Step 2, then run `/nlyu-pm:scout` again |
| Path-too-long error on Windows | Ask Claude in the session to run `git config --global core.longpaths true`, then `/nlyu-pm:scout` |
| Web search policy error | Ignore it. Send the error text to whoever manages your Claude account |
| Screen looks stuck | Escape or the stop button. If nothing changes, start a new session in the same folder and rerun the stage command |


---

## Claude Code in a terminal (CLI, about 20 minutes)

Recommended for technical people. Same plugin and commands; type `/clear` between stages.

### 1. Account

Subscribe to Claude Pro, or use the account your company provides. Pro, Max, Team, and
Enterprise all include Claude Code. You sign in from the terminal in step 5.

### 2. Open a terminal

**Windows.** Press the Windows key, type `Terminal`, open it. The line should start
with `PS`.

**macOS.** Press Command and Space, type `Terminal`, press Enter.

A terminal shows a short line ending in a symbol such as `$` or `>`. That is where you
type. Type a command and press Enter to run it. Paste with Ctrl+V on Windows, Command+V
on macOS. Nothing you type here can break your laptop; the worst case is an error
message.

### 3. Install Claude Code

Paste one line and press Enter. It downloads Claude Code and may take a minute.

Windows:

```powershell
irm https://claude.ai/install.ps1 | iex
```

macOS:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Close the terminal, open a new one, and check:

```text
claude --version
```

You should see a version number such as `2.0.14`. If you see "not recognized" or
"command not found", see the Problems table.

### 4. Install Git

Check first:

```text
git --version
```

If you see a version number, skip to step 5. If not:

- **Windows.** Download Git for Windows from https://git-scm.com/downloads/win, run the
  installer, accept the defaults. Close and reopen the terminal.
- **macOS.** A dialog offers to install the command line tools. Click *Install* and wait
  for it to finish, then run the check again.

### 5. Sign in

Type `claude` and press Enter. Your browser opens a Claude sign-in page once; sign in with
the same account as the app and return to the terminal. When it asks whether you trust
the folder, say yes. Type `/exit` to leave.

### 6. Keys and commands

| To | Do |
|---|---|
| Send | Enter |
| New line without sending | Shift+Enter, or `\` then Enter |
| See available commands | type `/`, or `/nl` to show only this plugin's four commands, then pick one from the list |
| Stop Claude mid-reply | Escape |
| Clear the conversation | `/clear` |
| Quit | `/exit` |
| Reuse an earlier message | up arrow |
| Answer a multiple-choice question | arrow keys and Enter, or type your own answer |

Claude asks permission the first time it fetches a website, runs Git, or writes a file.
Pick the option that stops asking for the session.

Leave Shift+Tab alone. It changes permission modes.

### 7. Workspace folder and plugin

1. Pick the folder. To try an example case: create an empty folder called `pm-workspace`
   on your Desktop. To work on your own product (BYOP, bring your own project or repo):
   use the top folder of a local copy of your repository, or an empty folder if you will
   give a URL or a zip instead.
2. Open a terminal in it. Windows: right-click the folder, *Open in Terminal*. macOS:
   right-click the folder, *New Terminal at Folder*.
3. Type `claude`. Say yes to trusting the folder.
4. Type these two lines, one at a time, pressing Enter after each:

   ```text
   /plugin marketplace add niancilyu-2/nlyu-pm
   /plugin install nlyu-pm@nlyu-pm
   ```

5. Type `/` and confirm `/nlyu-pm:scout` is in the list.
6. Type `/nlyu-pm:scout`. It runs a readiness check and ends with `Ready`, `Ready with
   fallback`, or `Blocked`. For `Blocked`, do the action it prints and run `/nlyu-pm:scout`
   again. It also asks whether you want BYOP or an example case; answer now so the code
   downloads today, or choose *decide later*.
7. When asked, choose *stop after setup*.

### Checklist

- [ ] `claude --version` prints a version
- [ ] `git --version` prints a version
- [ ] `claude` starts without asking you to sign in
- [ ] `/nlyu-pm:scout` reported `Ready` or `Ready with fallback`

### Running the stages

Open a terminal in the folder you picked in step 7 (`pm-workspace`, or your repository), type `claude`, then:

| Stage | Type |
|---|---|
| Discovery | `/nlyu-pm:scout` |
| | `/clear` |
| Prototype | `/nlyu-pm:prototype` |
| | `/clear` |
| PRD | `/nlyu-pm:prd` |
| | `/clear` |
| Skill builder (independent, any time) | `/nlyu-pm:create-skill` |

Every reply ends with a status line such as `Scout · step 5/10 · fetches 6/20 · 14 min`.

### Problems

| You see | Do |
|---|---|
| `claude` not recognized | Close the terminal, open a new one. If it persists, rerun step 3 |
| `The token '&&' is not a valid statement separator` | You are in PowerShell. Use the Windows line in step 3 |
| `'irm' is not recognized` | You are in the old Command Prompt. Open *Terminal* instead |
| Browser sign-in does not complete | Copy the link from the terminal into your browser. On a company laptop, check whether a VPN blocks claude.ai |
| Sign-in says your plan does not include Claude Code | You are on the free plan or the wrong account. Type `/logout`, then sign in with a Pro, Max, Team, or Enterprise account |
| `/nlyu-pm:` commands missing | `/plugin marketplace update nlyu-pm`, then `/plugin install nlyu-pm@nlyu-pm` |
| Git missing | Step 4, then reopen the terminal and run `/nlyu-pm:scout` |
| Path-too-long error on Windows | `git config --global core.longpaths true`, then `/nlyu-pm:scout` |
| Web search policy error | Ignore it. Send the error text to whoever manages your Claude account |
| Screen looks stuck | Escape. If nothing changes, `/exit`, start `claude` again, rerun the stage command |


Stage-by-stage walkthrough: [TEST-WALKTHROUGH.md](TEST-WALKTHROUGH.md).
