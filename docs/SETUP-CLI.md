# Setup: Claude Code in a terminal (CLI)

The terminal route, for people comfortable with a command line. Do this once before your
first run; it takes about 20 minutes. If you would rather click than type, use the
[desktop app guide](SETUP.md) instead. If you get stuck, note the step number and check
the Problems table at the end.

## What you need

- **A Mac or Windows laptop** that you can install software on. If it is a company
  laptop, you may need IT to allow the installs in steps 3 and 4.
- **A paid Claude subscription.** Claude Code is part of the Claude Pro plan, currently
  US$20 a month, and of the Max, Team, and Enterprise plans. The free plan does not
  include it. Check current prices at https://claude.com/pricing.
- **About 20 minutes.**

## Words used in this guide

| Word | What it means here |
|---|---|
| Terminal | A plain text window on your laptop where you type a line and press Enter. Nothing happens until you press Enter. |
| Command | A line you type into the terminal. Commands for this plugin start with a slash, such as `/nlyu-pm:scout`. |
| Claude Code | Claude running inside that terminal. You type in plain English; it replies in the same window. |
| Plugin | An add-on that gives Claude Code the `/nlyu-pm:` commands used here. |
| Folder | A folder on your laptop, the same thing as a directory. All the files Claude writes land in the folder you pick in step 7. |
| Git | A free tool that downloads repositories. Claude Code uses it for you; you never type Git commands yourself. |
| Repository | A product's source code, stored on a site like GitHub. Claude reads it; it never changes it. |

## 1. Account

Subscribe to Claude Pro, or use the account your company provides. Pro, Max, Team, and
Enterprise all include Claude Code. You sign in from the terminal in step 5.

## 2. Open a terminal

**Windows.** Press the Windows key, type `Terminal`, open it. The line should start
with `PS`.

**macOS.** Press Command and Space, type `Terminal`, press Enter.

A terminal shows a short line ending in a symbol such as `$` or `>`. That is where you
type. Type a command and press Enter to run it. Paste with Ctrl+V on Windows, Command+V
on macOS. Nothing you type here can break your laptop; the worst case is an error
message.

## 3. Install Claude Code

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

## 4. Install Git

Check first:

```text
git --version
```

If you see a version number, skip to step 5. If not:

- **Windows.** Download Git for Windows from https://git-scm.com/downloads/win, run the
  installer, accept the defaults. Close and reopen the terminal.
- **macOS.** A dialog offers to install the command line tools. Click *Install* and wait
  for it to finish, then run the check again.

## 5. Sign in

Type `claude` and press Enter. Your browser opens a Claude sign-in page once; sign in with
the same account as the app and return to the terminal. When it asks whether you trust
the folder, say yes. Type `/exit` to leave.

## 6. Keys and commands

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

## 7. Workspace folder and plugin

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

## Checklist

- [ ] `claude --version` prints a version
- [ ] `git --version` prints a version
- [ ] `claude` starts without asking you to sign in
- [ ] `/nlyu-pm:scout` reported `Ready` or `Ready with fallback`

## Running the stages

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

## Problems

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
