# /nlyu-pm:prototype

The prototype skill. It turns the opportunity you chose into one focused user flow, builds a
clickable prototype of it, and improves it once through a design critique.

## What it produces

`outputs/prototype/index.html`, a single self-contained file that opens from the file
system with no server or install, and `outputs/02-prototype.md`, the notes: the user and
job, the approved flow and states, the evidence it answers, the design brief, the
repository UI references used, the critique findings, the revision made, remaining
limitations, and the decision record.

## Before you start

The discovery brief must be approved. If you changed the chosen opportunity since, this
skill stops and asks you to rerun discovery first.

## How a run goes

1. **Confirm the flow.** Claude shows the quotes behind your chosen opportunity, then asks
   in short questions for one user, one job, where the task starts and ends, the main
   action, and the two alternate states that matter most (empty, error, permission,
   recovery, or loading).
2. **Flow check-in.** You approve or edit the flow before anything is built.
3. **Read the product's design.** Claude reads the repository's design tokens, shared
   components, and layouts, read-only, and notes what it verified against what it inferred.
   A product with no screens (a command-line tool, an API, a library) gets the same flow
   shown as a stepped transcript or request walkthrough.
4. **Design brief.** One page: context, the flow, the screen size, the look to follow,
   synthetic data, what is out of scope, and the file contract. Both build paths start from
   it.
5. **Choose the build path.** Claude Design if readiness found it available, otherwise a
   standalone HTML file. Both start from the brief.
6. **Claude Design.** Claude gives you one instruction: run `/design` with the brief,
   export a single HTML file to the prototype folder, then run `/nlyu-pm:prototype` again,
   which resumes here.
7. **HTML fallback.** Claude writes the HTML file itself and opens it.
8. **Walkthrough.** You and Claude click through the main path and both states, checking
   labels, navigation, keyboard use, whether each state is clear, and contrast. This is a
   design critique, not user testing.
9. **One revision.** Claude proposes one change tied to a discovery finding or a critique
   point. You approve it or pick a different one, and it is applied.
10. **Prototype check-in.** You approve the revised prototype and record any trade-offs.
11. **Save.** Notes written, session updated, next step named.

## Rules it follows

- One user, one job, one main path, two alternate states, on the screen size the focus
  area specifies. Nothing from other focus areas.
- The file makes no network requests and needs no build step, so it works offline and
  survives being emailed.
- All names, records, and images are synthetic. The product's visual patterns are followed
  where the repository supports them, and the notes say where the prototype differs.
- Visual similarity is not the bar. A clear, testable flow is.
- Every reply ends with a status line: step, build path, revision, minutes, source folder
  status.
- The stage closes with one summary line (minutes, path, walkthrough findings,
  revisions, status), repeated in the notes' header.

## Where the details live

`plugins/nlyu-pm/skills/prototype/SKILL.md` is the skill. The brief template is
`plugins/nlyu-pm/resources/design-brief.md`, the HTML contract and walkthrough checklist
`plugins/nlyu-pm/resources/prototype-html-guide.md`, and the notes template
`plugins/nlyu-pm/resources/templates/02-prototype.md`.
