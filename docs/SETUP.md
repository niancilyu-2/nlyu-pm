# Setup

Do this once before your first run. It takes about 15 minutes in the Claude desktop app,
with no terminal and no coding knowledge. If you get stuck, note the step number and check
the Problems table at the end. If you would rather work in a terminal, see *Terminal path*
at the end of this page.

## What you need

- **A Mac or Windows laptop** that you can install software on. If it is a company
  laptop, you may need IT to allow the installs in steps 1 and 2.
- **A paid Claude subscription.** Claude Code is part of the Claude Pro plan, currently
  US$20 a month, and of the Max, Team, and Enterprise plans. The free plan does not
  include it. Check current prices at https://claude.com/pricing.
- **The Claude desktop app**, downloaded from https://claude.ai/download. The web
  version at claude.ai cannot run this plugin; the desktop app can, through its Code tab.
- **About 15 minutes.**

## Words used in this guide

| Word | What it means here |
|---|---|
| Code tab | The part of the Claude desktop app where Claude works inside a folder on your laptop. This is Claude Code. |
| Session | One conversation in the Code tab. You start a new one for each stage. |
| Prompt box | Where you type. Lines that start with a slash, such as `/nlyu-pm:scout`, are commands; everything else is plain English. |
| Plugin | An add-on that gives the Code tab the `/nlyu-pm:` commands used here. |
| Folder | A folder on your laptop. Everything Claude writes lands in the folder you pick in step 3. |
| Git | A free tool that downloads a product's code. Claude uses it for you; you never type Git commands. |
| Repository | A product's source code, stored on a site like GitHub. Claude reads it; it never changes it. |

## 1. Account and app

1. Subscribe to Claude Pro, or sign in to the account your company provides. Pro, Max,
   Team, and Enterprise all include Claude Code.
2. Download and install the Claude desktop app from https://claude.ai/download, open
   it, and sign in with that account.
3. Click the **Code** tab in the app. The first time, it may offer to set up Claude
   Code; accept.

## 2. Install Git

Claude downloads the product's code with Git, which the app does not include.

- **Windows.** Download Git for Windows from https://git-scm.com/downloads/win, run the
  installer, accept the defaults, then quit and reopen the Claude app.
- **macOS.** Nothing to do now. The first time Claude uses Git, macOS shows a dialog
  offering to install the command line tools. Click *Install*, wait for it to finish,
  then run `/nlyu-pm:scout` again.

Not sure whether Git is installed? Skip this step; the readiness check in step 6 tells
you.

## 3. Pick your workspace folder

- To try an example case: create an empty folder called `pm-workspace` on your Desktop.
- To work on your own product (BYOP, bring your own project or repo): use the top folder
  of a local copy of your repository, or an empty folder if you will give Claude a URL or
  a zip instead.

## 4. Open the folder in the Code tab

In the **Code** tab, start a new session and choose the folder from step 3 when the app
asks which folder to work in. If it asks whether you trust the folder, say yes.

## 5. Install the plugin

1. Open the app's **Settings**, then **Plugins**.
2. Click **Add**, then **Add marketplace**, then **Add from a repo**.
3. Paste `https://github.com/niancilyu-2/nlyu-pm` and confirm.
4. Find **nlyu-pm** in the plugin list and click **Install**. If it asks where to
   install, choose your user account so it is available in every folder.
5. Back in the session, type `/` in the prompt box and confirm `/nlyu-pm:scout` is in
   the list. If it is not, start a new session in the same folder and look again.

## 6. Run the readiness check

1. Type `/nlyu-pm:scout` and press Enter. It checks the folder and Git, tests web access,
   and ends with `Ready`, `Ready with fallback`, or `Blocked`. For `Blocked`, do the
   action it prints and run `/nlyu-pm:scout` again.
2. It also asks whether you want BYOP or an example case. Answer now so the code
   downloads today, or choose *decide later*.
3. When asked, choose *stop after setup*.

Claude asks permission the first time it fetches a website, runs Git, or writes a file.
Pick the option that stops asking for the session.

## Keys and commands

| To | Do |
|---|---|
| Send | Enter |
| New line without sending | Shift+Enter |
| See available commands | type `/` |
| Stop Claude mid-reply | Escape, or the stop button |
| Answer a multiple-choice question | click an option, or type your own answer |
| Move to the next stage | start a new session in the same folder |

## Checklist

- [ ] The Claude desktop app is installed and signed in
- [ ] `/nlyu-pm:scout` appears when you type `/`
- [ ] `/nlyu-pm:scout` reported `Ready` or `Ready with fallback`

## Running the stages

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

## Problems

| You see | Do |
|---|---|
| No **Code** tab in the app | Update the app from https://claude.ai/download, then sign in again |
| Sign-in says your plan does not include Claude Code | You are on the free plan or the wrong account. Sign out and sign in with a Pro, Max, Team, or Enterprise account |
| `/nlyu-pm:` commands missing | Settings, Plugins: check **nlyu-pm** is installed and enabled, then start a new session in the same folder |
| Readiness says Git is missing | Step 2, then run `/nlyu-pm:scout` again |
| Path-too-long error on Windows | Ask Claude in the session to run `git config --global core.longpaths true`, then `/nlyu-pm:scout` |
| Web search policy error | Ignore it. Send the error text to whoever manages your Claude account |
| Screen looks stuck | Escape or the stop button. If nothing changes, start a new session in the same folder and rerun the stage command |

Stage-by-stage walkthrough: [TEST-WALKTHROUGH.md](TEST-WALKTHROUGH.md).

## Terminal path

If you prefer the terminal, or use Claude Code on a machine without the desktop app:

1. Install Claude Code. Windows, in Terminal: `irm https://claude.ai/install.ps1 | iex`.
   macOS: `curl -fsSL https://claude.ai/install.sh | bash`. Open a new terminal and check
   with `claude --version`.
2. Install Git (step 2 above). On macOS, `git --version` in the terminal triggers the
   install dialog.
3. Open a terminal in your workspace folder, type `claude`, sign in through the browser
   page that opens, and say yes to trusting the folder.
4. Install the plugin by typing these two lines, one at a time:

   ```text
   /plugin marketplace add niancilyu-2/nlyu-pm
   /plugin install nlyu-pm@nlyu-pm
   ```

5. Run `/nlyu-pm:scout` as in step 6. Between stages, type `/clear` instead of starting a
   new session. `/exit` quits.

Terminal problems: `claude` not recognized means open a new terminal window; `'irm' is
not recognized` means you are in the old Command Prompt, so open *Terminal* instead.
