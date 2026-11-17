# PRD review checklist (passed to `nlyu-pm:prd-reviewer`)

The reviewer does not see the conversation. `/nlyu-pm:prd` sends it: the paths of
`outputs/03-prd.md` and of whichever of `outputs/01-discovery.md` and
`outputs/02-prototype.md` exist, the source roots with their commits, the case id and
lane, the selected opportunity ID, and this checklist. When the PRD started from an
intake, the prompt says which inputs are PM-provided and gives `.pm/evidence/backlog.md`,
`.pm/evidence/quotes.md`, and `.pm/intake/flow.md` instead of the missing stage file.
The reviewer reads only; it returns findings as text. `/nlyu-pm:prd` writes them to
`outputs/03-prd-review.md`.

## What to check

**Inputs.** A missing discovery brief or prototype is not a finding when the prompt says
that input was typed in at an intake. Check instead that the PRD's `Based on` row and
status say so, that requirements trace to the backlog entry and the intake flow, and that
nothing the PM typed is labelled `Evidence`. Flag a PM-provided statement presented as
evidence, and say in the Summary which inputs were PM-provided.

1. **Traceability.** Every `REQ-###` links to the selected `OPP-###` and to at least one
   `SIG-###`, `CON-###`, or an approved prototype screen or state. Every `AC-###` links to a
   `REQ-###`. Flag orphans in either direction.
2. **Feasibility read present.** Appendix A opens with the Feasibility read: every
   `CON-###` from the discovery brief appears with its re-check result, layers not read are
   named, and engineering-only questions are listed. Flag a missing constraint or an
   appendix that reads as verified without saying which layers were left unread.
3. **Quote provenance.** Every quotation in the PRD carries a `QUO-###` that exists in
   `01-discovery.md` section 4b (or in `.pm/evidence/quotes.md`) with its source, and
   the wording matches that entry. Flag any
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
