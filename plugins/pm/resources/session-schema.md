# `.pm/session.yaml` schema

The PM never edits this file. Skills own it. Keep it flat, small, and valid YAML.
Before every write: read the whole file, change only the keys you own, keep `decisions`
append-only, then write the whole file back. If the file is unreadable, do not guess: show
the PM the error, offer to rebuild it from the approved output files, and record
that you did so under `notes`.

```yaml
schema: 2
plugin_version: "0.8.0"          # from plugin.json at the time of setup
created_at: "2026-10-01T09:12:00Z"
workspace: "/absolute/path/to/workspace"
workspace_mode: wrapper          # wrapper | in-repo              (see workspace.md)
outputs_dir: outputs             # outputs | pm-outputs           (pm-outputs only when outputs/ was already in use)

readiness:
  status: ready                  # ready | ready-with-fallback | blocked | not-run
  checked_at: "2026-10-01T09:14:00Z"
  git: ok                        # ok | missing
  web: ok                        # ok | unavailable            (fetch tool)
  search: ok                     # ok | unavailable            (web search tool)
  feeds: [fetch, search]         # which of the two worked
  reddit_rss: false              # opt-in; true only if the PM asked for Reddit RSS
  browser_test: confirmed        # confirmed | unconfirmed
  design: unknown                # available | unavailable | unknown  (PM typed /design)
  stopped_after_setup: true      # PM chose to stop after readiness
  notes: []

case:
  id: immich                     # null until chosen; a slug for a BYOP case
  source: prepared               # prepared | custom | provided   (shared rules section 10)
  dir: "${CLAUDE_PLUGIN_ROOT}/cases/immich"   # or .pm/case
  origin: null                   # BYOP only: the URL or local path the PM gave
  lane: backup-status-confidence # null until chosen
  chosen_at: "2026-10-01T09:20:00Z"
  preselected: true              # chosen during readiness; may be changed when Discovery starts

sources:
  - role: primary                # primary | companion
    owner_repo: immich-app/immich   # null when there is no GitHub or GitLab remote
    root: sources/primary        # where files are read: sources/primary, ".", or an absolute path
    clone_to: sources/primary    # null for in-place sources
    pinned_sha: 9994eb3bedc77a63e652cb4195d843433696d036   # null if the folder is not a git repository
    verified_sha: 9994eb3bedc77a63e652cb4195d843433696d036   # from git rev-parse HEAD after clone
    method: sparse-clone         # sparse-clone | shallow-clone | in-place | offline-copy | archive
    access: public               # public | private   (private: cloned with the PM's own existing credentials)
    archive_ref: null            # archive only: branch or tag and download date the PM gave
    dirty_at_start: false        # in-place only: the working tree had uncommitted changes
    baseline: ""                 # in-place only: porcelain output at stage start, plugin folders excluded
    moved_to: null               # in-place only: HEAD at a later stage if it differs from pinned_sha
    clean_at_start: true         # true | false | unknown
    clean_at_end: true

stage:
  current: discovery             # setup | discovery | prototype | prd | done
  status: in-progress            # not-started | in-progress | approved | stale

stages:
  discovery:
    status: approved             # not-started | in-progress | approved | stale
    output: outputs/01-discovery.md
    revision: 1                  # increments on each approved save
    approved_at: "2026-10-01T10:15:00Z"
    selected_opportunity: OPP-002
    provisional: false           # true when saved under a time cut or with weak coverage
    summary: "Discovery complete · 58 min · fetches 17/20 · searches 3/8 · items 24 · quotes 8 · gaps 1 · approved"
  prototype:
    status: not-started          # not-started | in-progress | awaiting-design | approved | stale
    output: outputs/02-prototype.md
    html: outputs/prototype/index.html
    path: null                   # design | html-fallback
    brief: .pm/design-brief.md
    revision: 0
    approved_at: null
    summary: null                # stage summary line, written at close
  prd:
    status: not-started
    output: outputs/03-prd.md
    review: outputs/03-prd-review.md
    revision: 0
    approved_at: null
    summary: null                # stage summary line, written at close
  capstone:                      # informational only; /pm:create-skill does NOT write this file
    note: "See outputs/04-skill-summary.md if present."

stale: []                        # e.g. [prototype, prd]

decisions:                       # append-only
  - id: D-001
    stage: discovery
    checkin: research-check      # case-check | research-check | priority-check | flow-check | prototype-check | scope-check | handoff-check
    claude_recommended: "Coverage is thin on mobile backup; continue with framing X"
    pm_decided: "Continue; accept the gap"
    reason: "Gap is documented; enough to prototype"
    at: "2026-10-01T09:50:00Z"

notes: []                        # free-text events worth remembering, newest last
```

Source overrides (added, dropped, or reordered research sources and a raised budget) live
in a separate file, `.pm/sources.yaml`, written by `/pm:scout` from what the PM said (for
BYOP, during the case build); its shape is in `research-guide.md`. An `add:` entry for a
source behind a sign-in carries `access: pm-held` and an `auth:` hint (a variable name or
tool name, never a value); the PM's terms confirmation for it is appended to `notes`. Each
change is also appended to `notes` here.

A file with `schema: 1` (written by plugin 0.7.x) is valid: treat a missing
`workspace_mode` as `wrapper`, `outputs_dir` as `outputs`, `case.source` as `prepared`,
`case.dir` as the plugin's case folder, `sources[].root` as `clone_to`, and `method:
sparse-clone` as itself. Rewrite the file as `schema: 2` on the next write.

## Rules of ownership

| Key | Written by |
|---|---|
| `schema`, `plugin_version`, `created_at`, `workspace`, `workspace_mode`, `outputs_dir`, `readiness`, `case`, `sources` | `/pm:scout` |
| `sources[].baseline`, `clean_at_start`, `clean_at_end`, `moved_to` | any stage skill, at its start and end |
| `stage`, `stale` | any stage skill that changes the current stage |
| `stages.discovery` | `/pm:scout` |
| `stages.prototype`, `readiness.design` | `/pm:prototype` |
| `stages.prd` | `/pm:prd` |
| `decisions`, `notes` | any skill (append only) |
| anything | never `/pm:create-skill` |
