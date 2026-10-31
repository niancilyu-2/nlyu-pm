# Discovery review checklist (passed to `nlyu-pm:discovery-reviewer`)

The reviewer does not see the conversation. `/nlyu-pm:scout` sends it: the path of the
draft brief `.pm/drafts/01-discovery.md`, the folder `.pm/fetches/` with its `index.md`,
the case file (for `exclusions`), the source roots with their commits, the case id and
lane, and this checklist. The reviewer reads only; it returns findings as text.
`/nlyu-pm:scout` writes them to `outputs/01-discovery-review.md` and fixes what it can
before the priority check-in.

## What to check

1. **Quote verification.** Every `QUO-###` in section 4b names a saved fetch (`from
   F-###` or `from P-###` for pasted material). Open that file and confirm the quoted
   words appear in it, in order, with only the cuts the ellipses mark; spelling and
   grammar must match the source, not be corrected. Report each quote as `verified`,
   `differs`, `not found`, or `not checked (PM-held)`. Also flag: over 40 words, a handle
   or personal name instead of a role, no `supports SIG-###`, no URL or access date, or a
   source that is a search snippet. A quote marked `partial` must come from a file whose
   header says `truncated: yes`.
2. **Label audit.** Every `SIG-###` labelled `Evidence` has a URL that appears in
   `index.md`, a source type and rung, and an access date; an item whose URL was never
   fetched is `Inference` at best. A search snippet labelled `Evidence` is a finding.
   Every number carries its base ("12 of 3,877 ratings"); "many users" is a finding.
   Every `CON-###` names a path, a line range, a commit, one quoted line, and `Status: to
   confirm with engineering`; open the path under the source root and confirm the quoted
   line is there. Flag a quoted line that is not at the cited path.
3. **Triangulation and counter-evidence.** A theme labelled `recurring` cites items from
   two or more rungs; `concentrated` cites one source; `isolated` cites one item. Flag a
   label the cited items do not support. Each theme in the triangulation table has a
   counter-evidence entry that is a `SIG-###` or `looked (F-###), none`; "none found" with
   no fetch behind it is a finding. The "Who we heard from" paragraph is present and
   names who is missing. Contradictions between items are listed, not resolved by omission.
4. **Opportunity evidence lines.** For each `OPP-###`: the signal count equals the
   number of `SIG-###` cited, the source-type count equals the distinct rungs among them,
   the strongest-weight item is among those cited, the counter-evidence field names a
   fetch (`SIG-###` or `looked (F-###), none`), at least one cited quote is `verified` or
   `PM-held`, and the exclusions check names each case exclusion it was tested against.
   Flag an opportunity that an exclusion covers.
5. **Coverage floor.** Compute from the evidence log, not from the coverage table:

   | Floor | Minimum |
   |---|---|
   | Rungs with at least one `Evidence` item | 2 |
   | `Evidence` items in total | 5 |
   | `CON-###` whose quoted line was confirmed | 2 |
   | Quotes per opportunity that are `verified` or `PM-held` | 1 |

   Any row below its minimum gives the verdict `provisional required`; otherwise
   `approved allowed`. The floor is a rule, not a judgement: do not soften it for a
   product with a small public footprint, and say which row failed.

## Output format the reviewer must return

```markdown
## Summary
<2–3 sentences: overall state of the evidence, count of blocking and nonblocking findings, the floor verdict>

## Findings
| ID | Severity | Area | Finding | Where | Suggested disposition |
|---|---|---|---|---|---|
| RV-001 | blocking / major / minor | quote / label / constraint / triangulation / counter-evidence / opportunity / coverage | <one sentence> | <section or ID in the brief> | <fix in brief / needs the PM's call / accept with note> |

## Quote verification
| Quote | Saved file | Result | Note |
|---|---|---|---|
| QUO-001 | F-004 | verified / differs / not found / not checked (PM-held) | <what differs, if anything> |

## Coverage floor
| Floor | Minimum | Found | Met |
|---|---|---|---|

Verdict: approved allowed / provisional required (<which row failed>)

## Notes for the PM
<optional, ≤ 5 bullets, plain language>
```

Severity: `blocking` = must be fixed before status `approved`; `major` = misstates the
strength of the evidence and should be fixed or explicitly accepted; `minor` = editorial.
