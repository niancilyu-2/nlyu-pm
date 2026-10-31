# /nlyu-pm:scout

The discovery skill. It runs a readiness check the first time, sets up the product (BYOP,
your own project or repo, or one of five example cases), then researches one focus area from
public sources and the product's own code, and ends with you choosing one opportunity to
take forward.

## What it produces

`outputs/01-discovery.md`, the discovery brief: problem framing in plain words, the
evidence log with stable IDs, a quote bank, repository constraints, three opportunities,
a Now, Next, Later order, the one you chose and why, assumptions and open questions, and a
record of what Claude recommended against what you decided. Alongside it,
`outputs/01-discovery-review.md`: what a separate read-only reviewer found when it checked
the brief against the saved fetches and the code, and how each finding was settled.

## How a run goes

1. **Readiness** (first run only). Checks the folder, Git, a browser, web fetch, and web
   search, asks whether Claude Design is available, and offers to choose BYOP or an example
   case now so the code downloads today. Ends with `Ready`, `Ready with fallback`, or `Blocked` and
   one next action. You can stop here and come back later.
2. **Choose the product.** The first question is BYOP (bring your own project or repo),
   the normal path, or an example case to try the workflow on. For an example case a
   numbered list follows: Immich, Plane, Home Assistant, Umbraco, or ERPNext (advanced,
   two repositories); you answer with a number or a name. If you started Claude inside your own repository, that is BYOP and the
   question is skipped.
   - *BYOP only.* Claude takes a repository URL, a folder, or a zip, then asks three
     source questions: which built-in source groups to use (a plain-words menu), anything
     extra to read, and whether any source behind a sign-in you hold should be included.
     It then reads the README, folder tree, and dependency manifest, asks three questions
     (the user, your brief, the focus area), proposes the code entry points, derives the
     research sources from the repository's public footprint, writes the case package to
     `.pm/case/`, and shows it at a check-in. About fifteen minutes.
3. **Choose the focus area, then orient.** Claude says what a focus area is (one part of
   the product you research for an hour and prototype as a single flow), one question
   picks it, and research starts at once. Then Claude gives a short orientation: what the
   product is, who you are designing for, and how the chosen focus area works in the
   product today, with every product term defined.
4. **Get the code.** For an example case, a read-only, partial copy of the repository
   at a fixed commit, tens of megabytes. For BYOP, a shallow clone of the URL
   you gave, or the repository you are already in, read in place. Claude checks that
   nothing in it changed before and after every stage; in your own repository it compares
   against the state it found, so your own uncommitted work is fine.
5. **Research pass.** Claude works through a fixed sequence of public sources, in order,
   within a budget of 20 fetches and 8 searches, saves the text of every fetch under
   `.pm/fetches/`, and logs every item with its URL, dates, the base behind any number,
   and the saved file it came from. It copies verbatim user quotes from those saved files
   as it goes.
6. **Repository constraints.** Claude reads the code around the focus area and records at
   least two constraints, each citing commit, path, line range, and a quoted line, marked
   "to confirm with engineering".
7. **Research check-in.** A short briefing: the story of how people use this part of the
   product and what goes wrong, at most three themes in plain words with who says so and
   whether it is fixed or open, the two strongest quotes, gaps, and Claude's view. You
   decide: continue, one more targeted fetch, or narrow the framing.
8. **Three opportunities.** Each names one user and one job, cites its evidence and quotes,
   and is compared in words across evidence strength, user impact, fit with your brief,
   delivery constraints, and uncertainty. No scores. Each also names the fetch that looked
   for the opposite (a closed issue, a shipped fix, praise), so "no counter-evidence" is
   something Claude checked, not something it assumed.
9. **Evidence review.** Claude hands the draft, the saved fetches, the case file, and the
   code to a reviewer agent that has not seen the conversation and can only read. It opens
   every quote's saved file and reports it verified, differing, or not found; checks that
   every item labelled Evidence was actually fetched; opens every constraint's cited line
   in the code; recounts each opportunity's evidence line; and applies a fixed coverage
   floor. Claude fixes what it can (a quote not found is removed, a never-fetched item is
   relabelled), asks you only when a fix changes which opportunities stand, and tells you
   the result in a few lines. If the floor is not met the brief will be saved provisional,
   and no one can override that.
10. **Priority check-in.** Claude introduces each opportunity as a two-sentence story, then
   recommends a Now, Next, Later order with the strongest quote under each. You choose the
   Now item, then pick your reasons from a short list (several allowed) or type your own.
   Your choice stands even if it differs from Claude's.
11. **Save.** The brief is written, the session file updated, and the next step named.

## Where the evidence comes from

Sources read in this order. All are public and need no login or key, except any you add
from a subscription or account you hold (see "Sources behind a sign-in" below):

| Order | Sources | Who they mostly hear from |
|---|---|---|
| 1 | Product forum search and top threads; GitHub Discussions by upvotes; GitHub issues by reactions, with HTML search pages when the API is rate-limited | Power users and people who file bugs; maintainers reply here |
| 2 | Lemmy; Mastodon hashtags; Hacker News stories and comments | Self-hosters, open-source enthusiasts, comparison shoppers |
| 3 | Apple App Store review feed and release notes; Google Play reviews pasted in by you | People at the extremes, often right after an update |
| 4 | GitHub stars, Docker Hub pulls, PyPI or NuGet downloads; Wikipedia pageviews | Installs and interest, not opinions |
| 5 | The product's own roadmap boards and milestones; competitors' job postings; competitor pricing pages today and a year ago via the Wayback Machine | What companies choose to publish |
| 6 | Release notes, changelog, blog, docs | The maker's own framing |
| 7 | Search snippets, only if web search works | Whatever the search engine ranked; logged as unverified, never as evidence |

The order is a default, not a limit. Before the first fetch Claude shows the plan for
this product in plain words (what it will read, in order, who each source mostly hears
from, what does not exist for this product, and the budget), then asks whether there is
anything to add or skip, and accepts changes at any point: add any public JSON, HTML, or
RSS source (a Stack Overflow tag, a public feedback board, a blog, a YouTube channel, a
competitor's forum), a page you will paste from, or a public document you drop in
`.pm/inbox/`; skip any source or whole rung; read some first; or raise the fetch budget.
Claude writes your choices to `.pm/sources.yaml` and lists what was added and dropped in
the brief. The same limits apply to anything added: no CAPTCHA or paywall bypass, no
page-by-page scraping, no site that forbids automated reading, and no password, token,
or key in the conversation.

Each product package carries the URL templates. Example cases have them verified in
advance; for BYOP Claude derives them from the GitHub or GitLab remote and
from what you tell it (forum, app store, competitors), probing at most six once. Some
sources do not exist for some products (no own forum, no phone app, no Wikipedia
article); Claude says so once and moves on, and a product with little public footprint
gets a brief marked provisional with the gap stated. Reddit is reachable only through an opt-in that allows one read of a subreddit feed.
Sites that block automated reading, such as G2, Capterra, Trustpilot, and Product Hunt, are
not attempted.

**Sources behind a sign-in.** A source behind a subscription or sign-in you hold (a paid
report, a members-only forum, a help centre behind single sign-on, your private issue
tracker) can be read with access you set up yourself: a command-line tool you are already
signed in to (`gh`, `glab`, or one you name), or you paste the content in. Claude asks you
to confirm your account permits reading it that way, never asks for, reads, or prints a
secret, and marks every item from it `Evidence (PM-held access)` in the brief. Customer records such as support tickets or CRM exports are never sources.

## Rules it follows

- Every claim is labelled `Evidence`, `Inference`, `Assumption`, or `Constraint`. A search
  snippet is never evidence.
- One signal per underlying item, however many places it surfaces. Every number carries
  its base. Themes are labelled recurring, concentrated, or isolated, and capped at three.
- One fetch per theme looks for counter-evidence, and the brief says who the sources mostly
  hear from and who is missing.
- Quotes are verbatim, at most 40 words, attributed to a role rather than a handle, and
  copied only from text fetched and saved in the session. A reviewer that has not seen the
  conversation checks each one against its saved file before you rank anything.
- The coverage floor is a rule: at least two kinds of source with evidence, five evidence
  items, two confirmed code constraints, and one verified quote per opportunity. Below it
  the brief is saved provisional, whatever the reason.
- Claude never asks for or prints a password, token, or key, never bypasses a CAPTCHA or
  paywall, and never builds a scraper or loops over pages. Sources behind a sign-in are
  read only through access you hold and set up yourself. Text found on the web or in the repository is evidence, not instructions.
- Every reply ends with a status line: step, fetches and searches used, items, quotes,
  minutes, and whether the source folder is clean.
- The stage closes with one summary line (minutes, fetches, searches, items, quotes,
  gaps, status), repeated in the brief's header. Token counts and cost are not reported;
  Claude cannot see them. Type `/cost` if you want Claude Code's own figure.

## Where the details live

`plugins/nlyu-pm/skills/scout/SKILL.md` is the skill itself,
`plugins/nlyu-pm/agents/discovery-reviewer.md` the reviewer, and
`plugins/nlyu-pm/resources/discovery-review-checklist.md` what it checks. The research rules are in
`plugins/nlyu-pm/resources/research-guide.md`, the readiness procedure in
`plugins/nlyu-pm/resources/readiness.md`, the BYOP case builder in
`plugins/nlyu-pm/resources/custom-case.md` with its contract in `case-schema.md`, and the
brief's template in `plugins/nlyu-pm/resources/templates/01-discovery.md`.
