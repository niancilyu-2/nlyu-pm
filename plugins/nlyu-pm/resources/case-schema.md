# Case package schema

A case is the product package every stage reads: one `case.yaml`, one `orientation.md`,
one `design-notes.md`, together in one folder. The five example cases live under
`${CLAUDE_PLUGIN_ROOT}/cases/<id>/`. A BYOP case (the PM's own project or repo) is
generated into `.pm/case/` by the procedure in `custom-case.md`, or placed there by hand. All three are
read the same way; see shared rules section 10 for how a stage finds the case folder.

The contract below is what the stages depend on. An example case may carry extra keys
(for example `regression_case`); a generated case must carry at least the required ones.

## `case.yaml`

```yaml
id: my-product                       # required · slug, lowercase, hyphens
name: My Product                     # required
tier: core | advanced | custom       # required · custom = generated for BYOP
persona: <the user the PM designs for, as a role>          # required
mandate: <the PM's brief on that user's behalf, one line>  # required
product_summary: >-                  # required · two to four sentences, plain words
  ...
generated: true                      # custom cases only
generated_at: "2026-10-22T09:40:00Z" # custom cases only
repositories:                        # required · at least one entry with role: primary
  - role: primary | companion | web-reference
    owner_repo: owner/repo           # null when there is no GitHub or GitLab remote
    url: https://github.com/owner/repo   # null for a local-only repository
    host: github | gitlab | other | none  # custom cases; example cases are github
    default_branch: main
    pinned_sha: <full sha>           # the commit every path citation refers to
    pinned_at: "2026-10-22"
    license: MIT                     # or "proprietary" or "unknown"
    clone_to: sources/primary        # wrapper mode clone target; null when not cloned
    root: sources/primary            # where the files are read from: sources/primary, ".", or an absolute path
    sparse_paths: []                 # folders to check out; empty means the whole tree
    web_paths: []                    # web-reference only: exact URLs that may be fetched
    note: ""
lanes:                               # required · one to three
  - id: focus-area-slug
    name: Focus area name
    surface: desktop web | mobile app | mobile web | tablet web | desktop backoffice | terminal | api or library
    viewport: { width: 1440, height: 900 }   # terminal and api surfaces still name a frame size for the HTML prototype
    territory: >-                    # what is in and out, in one paragraph
      ...
    repo_entry_points:               # paths relative to the primary root, or starting with sources/<role>/
      - src/...
exclusions: []                       # required · may be the generic set from custom-case.md
synthetic_data_rules: []             # required · may be the generic set from custom-case.md
public_channels: []                  # pointers for the PM: issues, docs, releases, forum, review sites
feeds:                               # required · every key present; null or [] means "does not exist for this product"
  github_issues_top: ...
  github_issues_top_html: ...
  github_issues_top_companion: null
  github_issues_top_companion_html: null
  github_discussions_top: ...
  gitlab_issues_top: null            # GitLab-hosted products; see custom-case.md
  forum_search_json: ...
  forum_top_json: ...
  forum_tag_top_json: []
  lemmy_search: ...
  lemmy_communities: []
  mastodon_tags: []
  hackernews_search: ...
  hackernews_comments: ...
  app_store_reviews: []
  app_store_lookup: []
  play_store_page: null
  adoption: []
  wikipedia_pageviews: []
  roadmap:
    own: []
    competitor_jobs: []
  competitors: []
  reddit_rss_optional: null
  pm_provided_public_material: false # custom cases: true when the PM has said they will paste public reviews or posts
  extra: []                          # optional: added sources in the shape used by .pm/sources.yaml `add:` (research guide), including `access` and `auth` for a source behind a sign-in; for a case author who knows a source the standard keys do not cover
```

Rules the stages rely on:

- Every `feeds:` key exists. A missing key is a bug; `null` or `[]` is a documented absence.
- `{query}` in a template is replaced with a URL-encoded lane term, `{yyyymmdd}` with a
  date about a year ago, `{start}` and `{end}` with `YYYYMM01` month bounds.
- `repo_entry_points` are relative to the primary `root` unless they start with
  `sources/`. Paths cited in `CON-###` and in the PRD use the same convention.
- `pinned_sha` is the commit every citation names, even when the files are read from a
  working tree with uncommitted changes (the session records that separately).

## `orientation.md`

Sections, in this order, each with a heading: what the product is (two to four
sentences), who the persona is, the lanes (one paragraph each: surface, viewport, what is
in and out, where to look in the code), a repository map (what the main folders hold, in
plain words), where to start public research (numbered list of URLs), cautions (licence,
paid tiers, things not to run). Define every product term the first time it appears. Offer
no opinion on what the problems are. Under 900 words.

## `design-notes.md`

Sections, in this order: established visual patterns (layout, colour use, density, key
components, dialogs, notifications), where the design system lives (paths at the pinned
commit, each marked **Verified** or **Inferred**; exact URLs when it lives in another
repository), public UI references (URLs), synthetic data guidance, prototype scope
reminders (one file, main path plus two states, viewport, do not copy source). When
nothing in the repository defines tokens or shared components, say so and point the
prototype at the neutral defaults in `prototype-html-guide.md`. Under 700 words.

## Writing a case by hand

Anyone can prepare a case package for a product they want a group to work on: copy an
example case folder, replace every field, verify each feed URL once in a browser, and
place the folder at `.pm/case/` in the workspace (or add it under the plugin's `cases/`
for distribution). `/nlyu-pm:scout` detects a case at `.pm/case/` and offers it first.
