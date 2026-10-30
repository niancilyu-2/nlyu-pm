# Setup

Do this once before your first run. It takes about 20 minutes. If you get stuck, note the
step number and check the Problems table at the end.

Claude Code is Claude running in a text window on your laptop. You type in plain English
and it replies in the same window. You will type a few commands that start with a slash, such as `/pm:scout`, and answer questions in ordinary sentences.

## 1. Account

You need a Claude Pro, Max, Team, or Enterprise account. If your company provides Claude,
use that sign-in.

## 2. Open a terminal

**Windows.** Press the Windows key, type `Terminal`, open it. The line should start
with `PS`.

**macOS.** Press Command and Space, type `Terminal`, press Enter.

Type a command at the prompt and press Enter to run it. Paste with Ctrl+V on Windows,
Command+V on macOS.

## 3. Install Claude Code

Paste one line and press Enter.

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

You should see a version number.

## 4. Install Git

Check first:

```text
git --version
```

If you see a version number, skip to step 5. If not:

- **Windows.** Download Git for Windows from https://git-scm.com/downloads/win, run the
  installer, accept the defaults. Close and reopen the terminal.
- **macOS.** A dialog offers to install the tools. Click *Install*.

## 5. Sign in

Type `claude` and press Enter. Your browser opens. Sign in and return to the terminal.
When it asks whether you trust the folder, say yes. Type `/exit`.

## 6. Keys and commands

| To | Do |
|---|---|
| Send | Enter |
| New line without sending | Shift+Enter, or `\` then Enter |
| See available commands | type `/` |
| Stop Claude mid-reply | Escape |
| Clear the conversation | `/clear` |
| Quit | `/exit` |
| Reuse an earlier message | up arrow |
| Answer a multiple-choice question | arrow keys and Enter, or type your own answer |

Claude asks permission the first time it fetches a website, runs Git, or writes a file.
Pick the option that stops asking for the session.

Leave Shift+Tab alone. It changes permission modes.

## 7. Workspace folder and plugin

1. Pick the folder. Example cases: create an empty folder called `pm-workspace` on your
   Desktop. BYOP (bring your own project or repo): use the top folder of a local copy of
   your repository, or an empty folder if you will give a URL or a zip instead.
2. Open a terminal in it. Windows: right-click the folder, *Open in Terminal*. macOS:
   right-click the folder, *New Terminal at Folder*.
3. Type `claude`. Say yes to trusting the folder.
4. Type these two lines, one at a time:

   ```text
   /plugin marketplace add niancilyu-2/nlyu
   /plugin install pm@nlyu
   ```

5. Type `/` and confirm `/pm:scout` is in the list.
6. Type `/pm:scout`. It runs a readiness check and ends with `Ready`, `Ready with
   fallback`, or `Blocked`. For `Blocked`, do the action it prints and run `/pm:scout`
   again. It also asks whether you want BYOP or an example case; answer now so the code
   downloads today, or choose *decide later*.
7. When asked, choose *stop after setup*.

## Checklist

- [ ] `claude --version` prints a version
- [ ] `git --version` prints a version
- [ ] `claude` starts without asking you to sign in
- [ ] `/pm:scout` reported `Ready` or `Ready with fallback`

## Running the stages

Open a terminal in the folder you picked in step 7 (`pm-workspace`, or your repository), type `claude`, then:

| Stage | Type |
|---|---|
| Discovery | `/pm:scout` |
| | `/clear` |
| Prototype | `/pm:prototype` |
| | `/clear` |
| PRD | `/pm:prd` |
| | `/clear` |
| Capstone (independent, any time) | `/pm:create-skill` |

Every reply ends with a status line such as `Scout · step 5/10 · fetches 6/20 · 14 min`.

## Problems

| You see | Do |
|---|---|
| `claude` not recognized | Close the terminal, open a new one. If it persists, rerun step 3 |
| `The token '&&' is not a valid statement separator` | You are in PowerShell. Use the Windows line in step 3 |
| `'irm' is not recognized` | You are in the old Command Prompt. Open *Terminal* instead |
| Browser sign-in does not complete | Copy the link from the terminal into your browser. On a company laptop, check whether a VPN blocks claude.ai |
| Sign-in says your plan does not include Claude Code | Wrong account. Type `/logout`, then sign in with the account that includes Claude Code |
| `/pm:` commands missing | `/plugin marketplace update nlyu`, then `/plugin install pm@nlyu` |
| Git missing | Step 4, then reopen the terminal and run `/pm:scout` |
| Path-too-long error on Windows | `git config --global core.longpaths true`, then `/pm:scout` |
| Web search policy error | Ignore it. Send the error text to whoever manages your Claude account |
| Screen looks stuck | Escape. If nothing changes, `/exit`, start `claude` again, rerun the stage command |

Stage-by-stage walkthrough: [TEST-WALKTHROUGH.md](TEST-WALKTHROUGH.md).
