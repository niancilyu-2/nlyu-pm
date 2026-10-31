# PRD: <feature title>

| Field | Value |
|---|---|
| Status | draft / ready-for-engineering-review |
| Approved | <date and time, or not yet> |
| Revision | <n> |
| Product · case lane | <product> · <lane> |
| Source commits | <owner/repo @ sha>; <companion @ sha> |
| Based on | 01-discovery.md rev <n> (OPP-###) · 02-prototype.md rev <n> |
| Review | outputs/03-prd-review.md |
| Run summary | <stage summary line, written at close> |

## Summary for engineering
<Five sentences at most: what this changes for which user, why now (the strongest evidence), what is out of scope, the riskiest open question, and what you need from engineering first.>

## 1. Problem and desired outcome
- Problem: <…>
- Desired outcome: <…>
- Persona: <the role, not a synthetic name; synthetic names stay in the prototype>
- Supporting evidence: SIG-### … · CON-### …
- Voice of the customer, two quotes chosen by the PM from the discovery quote bank:

> "<verbatim>"

QUO-### · <role> · <date> · <URL>

> "<verbatim>"

QUO-### · <role> · <date> · <URL>

## 2. Goals, non-goals, and scope
- Goals: <…>
- Non-goals: <…>
- Scope boundary: <…>

## 3. Approved flow
- Main path: <from 02-prototype.md>
- Alternate state A: <…> · Alternate state B: <…>

## 4. Functional requirements
<Aim for at most 10. Each is one behaviour an engineer can build and a tester can check. If you need more, the scope is probably two PRDs.>
| ID | Requirement | Priority (must / should / could) | Traces to |
|---|---|---|---|
| REQ-001 | | | OPP-### · SIG-### · screen/state |

## 5. Acceptance criteria
<Aim for at most 15. One observable outcome each; no regression sweeps, no "everything else unchanged".>
| ID | Given / when / then | Verifies |
|---|---|---|
| AC-001 | | REQ-### |

## 6. States and behaviour
| State | Behaviour | Out of scope? |
|---|---|---|
| Loading | | |
| Empty | | |
| Error | | |
| Permission | | |
| Recovery | | |

## 7. Success measures and analytics needs
- Measure: <…> · How it would be measured: <an existing mechanism, verified with a path, or "new instrumentation, engineering-owned dependency">

## 8. Quality needs
- Accessibility: <…> · Performance: <…> · Privacy: <…> · Security: <…> · Reliability: <…>

## 9. Rollout, migration, compatibility, test considerations
<Where applicable; otherwise "none identified".>

## 10. Dependencies, risks, assumptions, open product questions
- Dependency: <…>
- Risk: <…>
- Assumption: <…>
- OPEN-###: <question> · owner · changes scope? yes/no

## 11. Decision record
| Check-in | Recommendation | Your decision | Reason |
|---|---|---|---|
| Scope check | | | |
| Handoff check | | | |

## Appendix A. Engineering impact
Every line labelled `Verified` (with path), `Inferred`, or `Engineering-owned`.

### Feasibility read
What the code says today, verified by reading it, not by running it.

| Constraint | Where (path, lines, commit) | Re-checked in this stage | What it means for this PRD | Status |
|---|---|---|---|---|
| CON-### | | yes / no longer matches (now Inferred) | | to confirm with engineering |

Touchpoints found: <n Verified, n Inferred>. Layers covered: <UI / state / permissions / API; say which were not read>.

Questions only engineering can answer:
- OPEN-###: <question> · <why the PM cannot settle it>
- OPEN-###: …


- Code touchpoints:
- API implications:
- Data and state implications:
- Permissions:
- Integration boundaries:
- Technical risks:
- Engineering-owned decisions:
