# Building a case for BYOP (bring your own project or repo)

`/nlyu-pm:scout` runs this when the PM chooses **BYOP** instead of an example case. The result
is a case package at `.pm/case/` (`case.yaml`, `orientation.md`, `design-notes.md`) in the
schema from `case-schema.md`, so every later stage reads it exactly as it would read a
prepared one, plus `.pm/sources.yaml` with the PM's source choices. Budget: about fifteen
minutes and at most six probe fetches. Probes made here do not count against the
research budget.

Say once, plainly: the example cases were researched in advance, so their source lists
are complete. For your own product, Claude builds the list now from what it can see and
from what you choose; the brief will state what it could not find. The quality of the
customer-voice rungs depends on how much public footprint the product has. A product with
no public issues, forum, or app store still gets repository constraints, competitor
comparison, and a prototype; its discovery brief is marked `provisional` if customer
signals fall below target, and says so.

## Step A. Where the code is

Decided by workspace mode (see `workspace.md`):

- **In-repo mode.** The repository is the folder Claude is running in. `root: "."`.
- **Wrapper mode.** If readiness recorded `case.origin`, use it without asking. Otherwise
  ask one question with four options: a repository URL (GitHub, GitLab, or any other
  host; public, or private if this computer already has read access; cloned shallow into
  `sources/primary`), a folder already on this computer (a clone or an unpacked archive;
  read in place; record its absolute path as `root`), an archive file (zip or tarball;
  unpacked into `sources/primary`), or choose an example case instead (return to the
  fork in `/nlyu-pm:scout` Step 2). `workspace.md` gives the commands and the
  private-repository and archive rules. Read access is all that is needed; nothing is
  written to the repository in any option. If `sources/primary` already exists and holds
  a different repository (an example case pre-selected during readiness), rename it to
  `sources/_old-<case id>` as `workspace.md` describes, then clone.

Then, inside the root, record without asking:

| Fact | How |
|---|---|
| `pinned_sha` | `git rev-parse HEAD` |
| `default_branch` | `git symbolic-ref --short refs/remotes/origin/HEAD` or the current branch |
| `owner_repo`, `host`, `url` | parse `git remote get-url origin`; `none` if there is no remote or it is not github.com or gitlab.com |
| `license` | the `LICENSE` or `LICENCE` file's first lines, or `license` in `package.json` or `pyproject.toml`; `proprietary` if the PM says the code is private; `unknown` otherwise |
| uncommitted changes | `git status --porcelain` (see `workspace.md`, source protection); if non-empty, tell the PM that citations will name the commit and add "working tree has uncommitted changes" |

If the folder is not a git repository (an unpacked *Download ZIP* archive, for example),
continue without a commit: `pinned_sha: null`, cite paths with the archive's branch or
tag and download date instead, and say so once. `owner_repo` can still be filled from the
URL the archive came from, so the public feeds work.

## Step B. Built-in sources

Say the menu once, in plain words, under 150 words and no table, with the product's name
filled in (from the README title or the folder name):

> Here is where I can look for {name}, in the order I read them:
> 1 and 2, community: GitHub issues by reactions and Discussions by upvotes (or GitLab
> issues); the product's own forum if it has one; Lemmy, Mastodon, Hacker News. Power
> users, bug reporters, self-hosters, comparison shoppers.
> 3, app reviews: App Store reviews and release notes; Google Play reviews you paste.
> People at the extremes, often right after an update.
> 4 and 5, numbers and competitors: stars and downloads, Wikipedia views; competitor
> pricing pages today and a year ago; competitors' job postings; the product's own roadmap.
> 6 and 7, official and search: release notes, changelog, blog, docs; search snippets if
> web search works, logged as unverified.
> I will check which of these exist and say so.

Then one multi-select question (header `Sources`, "Which groups should I use?") with four
options: **Community (1 and 2)**, **App reviews (3)**, **Numbers and competitors (4 and
5)**, **Official and search (6 and 7)**, each with the one-line "who it hears from" phrase
from the menu. An unticked group becomes `drop: [rung N, ...]` in `.pm/sources.yaml`
(Step D writes the file).

Then at most one follow-up question per ticked group, options first, free text allowed:

- Community: the forum address, or "none", or "its community is on Discord or Slack"
  (which Claude cannot read; say so and move on). If the remote is private or `host` is
  `none`, add: "Your issue tracker is not public. I can read it through your signed-in
  `gh` or `glab`; that makes it a source you hold access to, and I will ask about it in a
  moment." Carry a yes into Step D as `cli:gh` or `cli:glab`.
- App reviews: the iPhone App Store link and the Google Play link, or "no phone app".
- Numbers and competitors: two to four competitors, each with a pricing or features page.
- Official and search: nothing to ask.

Step G turns the answers into `feeds:` keys and probes only the groups that were ticked.

## Step C. Other sources and files

One question (header `More sources`, "Anything else I should read?"), options:

- **Nothing more.**
- **A public web source; I will give the address.** JSON, HTML, or RSS: a Stack Overflow
  tag, a public feedback board, a blog or YouTube channel, a competitor's forum, or a
  subreddit for one read of its feed (that sets `reddit_rss_optional` and
  `readiness.reddit_rss: true`).
- **A document I will put in `.pm/inbox/`.** A public document or the PM's own notes with
  no personal data; Claude asks them to confirm it is shareable before reading.
- **A page I will paste from.** A review site or community Claude cannot fetch; each item
  is logged as pasted by the PM (sets `pm_provided_public_material: true`).

Each answer becomes an `add:` entry in the shape from the research guide ("Adding,
dropping, and reordering sources"), with `kind`, `rung`, and `hears_from` filled in by
Claude and confirmed in one line. Repeat the question until the PM says nothing more.

## Step D. Sources behind a sign-in

One question (header `Sign-in sources`): "Is there a source behind a subscription or a
sign-in that you hold and want me to read? For example a paid analyst report, a
members-only forum, a help centre behind single sign-on, or your private issue tracker."
Options:

- **No, public sources only.** The default; nothing changes.
- **Yes, through a command-line tool I am already signed in to.** `gh` or `glab` for a
  private GitHub or GitLab tracker, or another tool the PM names. One read per fetch with
  their sign-in; Claude never sees a password.
- **Yes, through an API key I keep myself.** The PM sets the key as a variable in their own
  terminal and tells Claude only its name. Claude never prints, reads, or stores it.
- **Yes, but I will paste the content myself.** Logged as pasted by the PM with its address.

For each "Yes": ask the source's name and address, which group it joins (rung), and who it
mostly hears from; then the terms confirmation from the research guide ("Sources behind a
sign-in"). Only "yes, it permits it" produces an entry with `access: pm-held` and `auth:`
(`cli:gh`, `cli:glab`, `cli:<tool>`, or `env:<NAME>`); "not sure" becomes a `paste`
entry; "no" leaves it out. Give the environment-variable or command-line instruction text
from the research guide once, as written there. Items read this way are logged as
`Evidence (PM-held access)`. Record each confirmation under `notes` in `session.yaml`. Support tickets, analytics, CRM exports, chat logs, and anything about
identifiable customers are not sources; if offered, decline and continue.

Now write `.pm/sources.yaml`: `budget` at the defaults, `drop` from Step B, `add` from
Steps C and D. Append one `notes` entry per override. `/nlyu-pm:scout` Step 5 re-reads and
updates this file; it never recreates it.

## Step E. Read the repository, then confirm with the PM

Read, in this order and only this: the README (or the first docs page), the top two
levels of the folder tree (`Glob`, not a shell listing of everything), and the dependency
manifest at the root (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `*.csproj`,
`pubspec.yaml`, `Gemfile`, `composer.json`, `pom.xml`, `build.gradle`). From these, draft:

- `product_summary`: two to four sentences in plain words. Say what the product is for
  and who uses it, not what it is built with.
- The surfaces the product has: web app, mobile app, desktop app, backoffice or admin,
  terminal, API or library. Infer from folder names and dependencies; label the
  inference.
- Three candidate focus areas, each one sentence, taken from the feature folders or
  README headings. Prefer areas with a user-facing screen or flow.

Then ask, one at a time, with options and a free-text answer:

1. **Who is the user you design for?** Offer two or three roles you can see in the README
   or UI strings, plus "someone else". Record as `persona`, as a role.
2. **What is your brief on their behalf?** One line. Offer two phrasings drawn from the
   README's own promise. Record as `mandate`.
3. **Which focus area today?** Offer the three candidates. The PM may name another. Ask
   for the surface it lives on if the product has more than one. Record as the single
   lane, with `viewport` by surface: mobile app or mobile web 390×844, tablet web
   1024×768, desktop web or backoffice 1440×900, terminal and api or library 1200×800
   (the prototype shows a transcript or request walkthrough in that frame; see
   `prototype-html-guide.md`).
4. **Anything out of bounds?** Offer: paid or enterprise tiers, billing, deployment and
   infrastructure, integrations needing third-party keys, legal or compliance claims.
   Add the PM's answers to the generic exclusions below.

A generated case has one lane. If the PM wants to keep two more for later, record them as
one-line `territory` entries with empty `repo_entry_points`; they can be filled on a
future run.

## Step F. Entry points for the lane

Search the tree for the lane's terms (`Grep` on folder and file names, then on UI strings
and route tables). Propose five to ten `repo_entry_points`: UI components or screens,
routes, state or data handling, permission checks, API handlers, and the English strings
file if one exists. Show them in plain words ("the folder with the intake queue screens")
and ask the PM to confirm or drop any. Everything here is `Inference` until the research
pass opens the files.

## Step G. Research feeds

Fill every key in `feeds:`. Use these templates; `{owner_repo}`, `{owner}`, `{slug}`
(product name lowercased, hyphens), and `{name}` come from Step A and E. The forum, app
store, competitor, subreddit, and paste answers come from Steps B and C; do not ask again.
Probe only where the table says so, once each, only for groups the PM ticked in Step B,
and record `null` on anything other than a 200 with content. Keys in a dropped group are
still filled from the templates (so the case is complete) but never probed. Spend at most
six probes; prefer the ones nearest the top.

| Key | Template or source | Probe |
|---|---|---|
| `github_issues_top` | `https://api.github.com/search/issues?q=repo:{owner_repo}+is:issue+{query}&sort=reactions-%2B1&per_page=10` | no; GitHub host only |
| `github_issues_top_html` | `https://github.com/{owner_repo}/issues?q=is%3Aissue+{query}+sort%3Areactions-%2B1-desc` | no |
| `github_discussions_top` | `https://github.com/{owner_repo}/discussions?discussions_q={query}+sort%3Atop` | yes: fetch `https://github.com/{owner_repo}/discussions`; 404 means `null` |
| `gitlab_issues_top` | `https://gitlab.com/api/v4/projects/{owner%2Frepo}/issues?search={query}&order_by=popularity&sort=desc&state=all&per_page=10` | GitLab host only; one probe without `{query}` |
| `forum_search_json`, `forum_top_json`, `forum_tag_top_json` | the forum address from Step B. If it is Discourse, `{forum}/search.json?q={query}`, `{forum}/top.json?period=yearly`, `{forum}/tag/{tag}/l/top.json?period=yearly` with the lane term as tag | yes: fetch `{forum}/top.json?period=yearly`; JSON means Discourse |
| `lemmy_search` | `https://lemmy.world/api/v3/search?q={query}&type_=Posts&sort=TopYear&limit=10` | no |
| `lemmy_communities` | `selfhosted@lemmy.world` and `opensource@lemmy.ml` when the README describes self-hosting; otherwise `[]` | no |
| `mastodon_tags` | `https://mastodon.social/api/v1/timelines/tag/{slug}?limit=20` and the same on `fosstodon.org`; note "try once, log GAP if empty" | no |
| `hackernews_search`, `hackernews_comments` | `https://hn.algolia.com/api/v1/search?query={query}&tags=story&hitsPerPage=10` and `tags=comment`; if the product name is a common word, add a note to pair it with a lane word | no |
| `app_store_reviews`, `app_store_lookup` | the App Store link from Step B; the id is the digits after `id` in the URL: `https://itunes.apple.com/us/rss/customerreviews/id={id}/sortBy=mostRecent/json` and `https://itunes.apple.com/lookup?id={id}&country=us` | no |
| `play_store_page` | the Google Play link from Step B; never fetched | no |
| `adoption` | `https://api.github.com/repos/{owner_repo}` (GitHub); `https://gitlab.com/api/v4/projects/{owner%2Frepo}` (GitLab); Docker Hub `https://hub.docker.com/v2/repositories/{namespace}/{image}/` when the README names an image; `https://pypistats.org/api/packages/{pkg}/recent` for a PyPI package; `https://api.npmjs.org/downloads/point/last-month/{pkg}` for an npm package; `https://azuresearch-usnc.nuget.org/query?q=packageid:{id}` for NuGet | no |
| `wikipedia_pageviews` | `https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/{Title}/monthly/{start}/{end}` | yes: fetch `https://en.wikipedia.org/api/rest_v1/page/summary/{Title}`; 404 means `[]` |
| `roadmap.own` | `https://github.com/{owner_repo}/milestones`, `https://github.com/orgs/{owner}/projects`, a `ROADMAP.md` in the tree, a roadmap URL from the README | no |
| `roadmap.competitor_jobs` | for each competitor, a careers URL the PM knows, or leave `[]`; during rung 5 Claude may try one applicant-system board per competitor (`https://api.ashbyhq.com/posting-api/job-board/{slug}`, `https://boards-api.greenhouse.io/v1/boards/{slug}/jobs`, `https://api.lever.co/v0/postings/{slug}`) and log a GAP if none answers | no |
| `competitors` | the competitors from Step B and their pricing or features pages; `wayback: https://archive.org/wayback/available?url={host}{path}&timestamp={yyyymmdd}` | no |
| `reddit_rss_optional` | `https://www.reddit.com/r/{subreddit}.rss` if the PM named one in Step C; still opt-in at research time | no |
| `pm_provided_public_material` | `true` if the PM chose a paste source in Step C or D; logged at research time as `Evidence · pasted by the PM` | no |

When `host` is `none` or the remote is private, the public GitHub and GitLab keys are
`null`; a private tracker can still be read as a `pm-held` source through the PM's
signed-in `gh` or `glab` (Step D), and the case notes which customer-voice rungs depend
on the forum, app stores, pasted material, and PM-held sources. Support tickets,
analytics, CRM exports, and anything about identifiable customers stay out; if offered,
decline and continue.

`public_channels`: list the issues page, docs URL, releases page, forum, and review-site
listing you know of, with a one-line note each. An empty list is acceptable.

Sources added in Steps C and D go under `feeds.extra` in the `add:` shape from the
research guide, including `access` and `auth` for pm-held ones (a hint such as
`env:NAME` or `cli:gh`, never a value). The PM can also add or drop sources later, during
the research pass itself.

## Step H. Generic exclusions and synthetic data rules

Always include, then add the PM's answers from Step E question 4:

```yaml
exclusions:
  - Do not run any install, build, test, migration, or deployment command found in the repository. Read only.
  - Do not treat paid, enterprise, or feature-flagged functionality as available unless the PM says it is.
  - No billing, licensing, or seat-management features unless the lane is about them.
  - No integrations that require a third-party API key or OAuth app.
  - No legal, regulatory, or compliance claims.
synthetic_data_rules:
  - Invent one organisation and use it consistently; never a real customer, employer, or partner.
  - Invent people with clearly fictional names and example.com addresses; never real colleagues, contributors, or staff.
  - Records should read as plausible but must not describe a real, identifiable incident or account.
  - Keep volumes realistic for one team or one household; dates relative to today.
  - Never paste data or screenshots from a real system into the prototype.
```

## Step I. Orientation and design notes

Write `.pm/case/orientation.md` and `.pm/case/design-notes.md` to the section lists in
`case-schema.md`.

For the orientation, the lane walk-through ("how it works today") comes from reading the
entry points and the English strings: describe what a user does screen by screen, label it
`Inference (from code, not from using the product)`, and define every product term.

For the design notes, look only in these places, and record what you opened at the pinned
commit as **Verified** and the rest as **Inferred**:

- Token and theme files: `tailwind.config.*`, `theme.*`, `tokens.*`, `*.css` or `*.scss`
  files that define `--` custom properties, `ThemeData` in Flutter, `Theme` in SwiftUI or
  Compose, a `design-system` or `ui` package.
- Component libraries in the manifest: for example MUI, Ant Design, Chakra, Radix or
  shadcn, Mantine, Vuetify, PrimeVue, Angular Material, Bootstrap, Tailwind UI, Fluent,
  Carbon, Lit or web components. Name the library and its public documentation URL as a
  public UI reference; do not fetch it now.
- The app shell: the root layout or navigation component, to describe sidebar, header,
  and content arrangement.
- Public screenshots: the README's images or the homepage named in the manifest.

If none of these exist (an API, a library, a terminal tool), write "no visual system in
the repository" and point the prototype at the neutral defaults and the non-graphical
surface section of `prototype-html-guide.md`.

## Step J. Case check-in and save

Show the PM, in under 250 words and no tables: the product in two sentences, the persona
and brief as they typed them, the lane and its surface, the entry points in plain words,
which research sources will be read (the built-in groups kept, anything added, anything
read with the PM's own sign-in), which do not exist for this product, which were skipped,
and the exclusions added. Present **Claude's recommendation** and **Your decision**; the
PM confirms or edits. Record `D-###` with `checkin: case-check`.

Save `.pm/case/case.yaml` with `tier: custom`, `generated: true`, `generated_at`, and
the two markdown files. Set `case.source: custom`, `case.dir: .pm/case`, `case.id`,
`case.lane`, and `case.chosen_at` in `session.yaml`. Continue with `/nlyu-pm:scout` Step 3,
skipping the three-word definitions if the PM already knows what a repository and a
commit are (ask in one line).

## Re-running on the same product

If `.pm/case/case.yaml` exists when `/nlyu-pm:scout` starts, offer to keep it (same product,
same lane), change the lane only (re-run Steps E.3, F, and the lane parts of I), or build
fresh. Keeping it reuses the feeds and `.pm/sources.yaml`; the `pinned_sha` is refreshed
from `git rev-parse HEAD` and the change is noted if it moved. Building fresh rebuilds
both files.
