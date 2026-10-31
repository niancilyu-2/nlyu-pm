# Design brief template (`.pm/design-brief.md`)

`/nlyu-pm:prototype` writes this file after the flow check-in. It is the single input to either
Claude Design (`/design`) or the HTML fallback, so both paths start from the same brief.
Keep it under 500 words. Fill every field; write `none` rather than leaving a blank.

```markdown
# Design brief: <case name> · <lane name>

## Context
- Product: <name, one line on what it is>
- Persona: <persona> · Mandate: <mandate>
- Selected opportunity: <OPP-###>: <one sentence>
- Discovery evidence this flow answers: <SIG-### list, one clause each>

## The flow
- Actor: <one actor>
- Job: <one job in the actor's words>
- Starts when: <trigger / entry point>
- Ends when: <observable end state>
- Main action: <the one thing the actor does>
- Main path (numbered, 3–7 steps): 1. … 2. … 3. …
- Alternate state A (<empty | error | permission | recovery | loading>): <what the actor sees and can do>
- Alternate state B (<…>): <…>

## Surface
- Surface: <mobile app | mobile web | tablet web | desktop web | desktop backoffice | terminal | api or library>
- Viewport: <width>×<height>
- Screens: <2–4 screen names in order>

## Look and feel
- Follow the product's established patterns: <2–4 bullets from design-notes.md: nav placement, color mode, density, key components>
- Repository references read (paths, pinned commit): <list>
- Public UI references: <URLs>
- Deliberate departures from the current UI: <list or none>

## Data
- All names, records, images, and media are synthetic. Placeholder imagery: neutral blocks or simple shapes.
- Example records to show: <3–6 short rows>

## Out of scope
- <bullets: other lanes, settings, admin, anything outside the main path and two states>

## Output contract
- One standalone file at `outputs/prototype/index.html`
- Opens from the file system with no server, install, or build step
- No external network requests (no CDN scripts, fonts, or images)
- Main path clickable end to end; both alternate states reachable
- Keyboard: Tab reaches every control; Enter/Space activates
```
