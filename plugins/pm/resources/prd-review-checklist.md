# PRD review checklist (passed to `pm:prd-reviewer`)

The reviewer does not see the conversation. `/pm:prd` sends it: the paths of
`outputs/01-discovery.md`, `outputs/02-prototype.md`, `outputs/03-prd.md`, the source
roots with their commits, the case id and lane, the selected opportunity ID, and this
checklist.
The reviewer reads only; it returns findings as text. `/pm:prd` writes them to
`outputs/03-prd-review.md`.

## What to check

1. **Traceability.** Every `REQ-###` links to the selected `OPP-###` and to at least one
   `SIG-###`, `CON-###`, or an approved prototype screen or state. Every `AC-###` links to a
   `REQ-###`. Flag orphans in either direction.
2. **Feasibility read present.** Appendix A opens with the Feasibility read: every
   `CON-###` from the discovery brief appears with its re-check result, layers not read are
   named, and engineering-only questions are listed. Flag a missing constraint or an
   appendix that reads as verified without saying which layers were left unread.
3. **Quote provenance.** Every quotation in the PRD carries a `QUO-###` that exists in
   `01-discovery.md` section 4b with a URL, and the wording matches that entry. Flag any
   quote that appears only in the PRD or differs from the bank.
4. **Unsupported technical claims.** Every technical statement is labelled `Verified`,
   `Inferred`, or `Engineering-owned`. For `Verified`, open the cited path under the source
   root given in the prompt and confirm it exists and says what the PRD claims. For every `CON-###`, check that it names a
   path, a line range, a quoted line, and the status "to confirm with engineering"; flag any
   that do not. Flag invented file names, APIs, or data
   models. Flag estimates, story points, delivery dates or deadlines, or costs anywhere in the
   document.
5. **Missing states or permissions.** The approved main path and the two alternate states
   from `02-prototype.md` appear in the PRD. Loading, empty, error, permission, and
   recovery behaviour is either specified or explicitly marked out of scope. Role and
   permission behaviour is stated where the product has roles.
6. **Untestable acceptance criteria.** Each `AC-###` describes an observable outcome a
   tester could confirm without interpreting intent. Flag vague words ("fast", "intuitive",
   "appropriate") without a measurable condition, and flag any criterion that is a
   regression sweep rather than one observable outcome.
7. **Scope conflicts.** Goals, non-goals, and requirements agree with each other and with
   the approved discovery and prototype scope. Flag requirements that belong to another
   lane or that widen scope beyond the prototype.
8. **Delivery risks.** Note relevant risks visible from the repository or the PRD itself:
   data migration, breaking changes to existing behaviour, privacy or security implications,
   accessibility gaps, and dependencies on other components. Do not propose architecture.
9. **Blocking open questions.** Any `OPEN-###` whose answer would change product scope,
   user behaviour, data or security behaviour, or acceptance criteria must be flagged as
   **blocking**. Others are nonblocking engineering questions.

## Output format the reviewer must return

```markdown
## Summary
<2–3 sentences: overall readiness, count of blocking and nonblocking findings>

## Findings
| ID | Severity | Area | Finding | Where | Suggested disposition |
|---|---|---|---|---|---|
| RV-001 | blocking / major / minor | traceability / feasibility / quote / technical-claim / states / acceptance / scope / risk / open-question | <one sentence> | <section or ID in 03-prd.md> | <fix in PRD / convert to engineering question / accept with note> |

## Verified touchpoints
| Path | Exists | Matches claim |
|---|---|---|

## Notes for the PM
<optional, ≤ 5 bullets, plain language>
```

Severity: `blocking` = must be resolved before status `ready-for-engineering-review`;
`major` = should be addressed or explicitly accepted; `minor` = editorial.
