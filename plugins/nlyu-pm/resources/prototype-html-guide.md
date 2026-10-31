# Standalone HTML prototype: contract and skeleton

Used when Claude Design is unavailable, when it does not produce a reusable file, or when
the PM prefers it. The PRD stage relies on this file, never on a Design share link.

## Contract

- Exactly one file: `outputs/prototype/index.html`. CSS and JavaScript are embedded.
- Opens by double-click from the file system (`file://`) in current Chrome, Edge, or Safari.
- **No network requests of any kind**: no CDN scripts, web fonts, icon fonts, remote images,
  analytics. Use system fonts and inline SVG.
- **No `fetch()` or module imports**; browsers block them from `file://`.
- No build step, no framework. Plain HTML, CSS custom properties, and a small amount of
  vanilla JavaScript for screen switching and state.
- Sized to the lane viewport. Center a fixed-size frame (for example 390×844) on a neutral
  page background so it looks right on any laptop screen.
- All text, names, records, and imagery are synthetic. Placeholder imagery is a solid block
  or simple SVG shape with a short label.
- Main path clickable end to end. Both alternate states reachable by a visible control or a
  small "demo controls" bar (for example: *Show empty state*, *Show error*).
- Keyboard: every control is a `<button>`, `<a href>`, or form field, never a clickable
  `<div>`; visible focus ring; Enter/Space activate. Screen changes move focus to the new
  screen's heading. The error state's message carries `role="alert"`.
- Obvious contrast: body text at least 4.5:1 against its background.
- Top-right corner shows a tiny label: `Prototype · synthetic data`.

## Skeleton

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Prototype: <case> · <lane></title>
<style>
  :root {
    /* Take names and values from design-notes.md where verified; otherwise neutral defaults */
    --bg: #f6f7f9; --surface: #ffffff; --text: #1a1a1a; --muted: #5b5f66;
    --primary: #2f5bea; --primary-text: #ffffff; --border: #d9dce1;
    --danger: #b3261e; --success: #1f7a3f; --radius: 10px;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  }
  body { margin: 0; background: #e9ebef; color: var(--text); display: grid; place-items: center; min-height: 100vh; }
  .frame { width: 390px; height: 844px; background: var(--bg); border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; position: relative; }
  .screen { display: none; height: 100%; flex-direction: column; }
  .screen.active { display: flex; }
  header { padding: 16px; background: var(--surface); border-bottom: 1px solid var(--border); }
  main { padding: 16px; flex: 1; overflow: auto; }
  button.primary { background: var(--primary); color: var(--primary-text); border: 0; border-radius: var(--radius); padding: 12px 16px; font-size: 16px; }
  button:focus-visible, a:focus-visible { outline: 3px solid #ffbf47; outline-offset: 2px; }
  .badge { position: absolute; top: 8px; right: 8px; font-size: 11px; background: #fff; border: 1px solid var(--border); border-radius: 999px; padding: 2px 8px; color: var(--muted); }
  .demo { position: fixed; bottom: 12px; left: 50%; transform: translateX(-50%); display: flex; gap: 8px; }
  .demo button { font-size: 12px; }
</style>
</head>
<body>
  <div class="frame">
    <span class="badge">Prototype · synthetic data</span>

    <section class="screen active" id="s1" aria-labelledby="h1">
      <header><h1 id="h1" tabindex="-1">Screen 1 title</h1></header>
      <main>
        <!-- content -->
        <button class="primary" data-go="s2">Main action</button>
      </main>
    </section>

    <section class="screen" id="s2" aria-labelledby="h2">
      <header><h1 id="h2" tabindex="-1">Screen 2 title</h1></header>
      <main><!-- content --></main>
    </section>

    <section class="screen" id="empty" aria-labelledby="hE">
      <header><h1 id="hE" tabindex="-1">Nothing here yet</h1></header>
      <main><p>Explain the empty state and offer the one useful next step.</p><button class="primary" data-go="s1">Start</button></main>
    </section>

    <section class="screen" id="error" aria-labelledby="hX">
      <header><h1 id="hX" tabindex="-1">Something went wrong</h1></header>
      <main><p role="alert">Say what happened in plain words and how to recover.</p><button class="primary" data-go="s1">Try again</button></main>
    </section>
  </div>

  <div class="demo" aria-label="Demo controls">
    <button data-go="s1">Main path</button>
    <button data-go="empty">Show empty state</button>
    <button data-go="error">Show error state</button>
  </div>

<script>
  function go(id) {
    document.querySelectorAll('.screen').forEach(s => s.classList.toggle('active', s.id === id));
    const h = document.querySelector('#' + id + ' h1'); if (h) h.focus();
  }
  document.addEventListener('click', e => {
    const t = e.target.closest('[data-go]'); if (t) go(t.getAttribute('data-go'));
  });
</script>
</body>
</html>
```

Adjust `.frame` to the lane viewport (for example `1440px × 900px`; for desktop surfaces
drop the fixed frame and use the full window with a max-width). Replace neutral tokens with
values you verified in the repository, and list the source paths in `02-prototype.md`.

## Non-graphical surfaces (terminal, API or library)

A product with no screens still gets a clickable prototype of the same shape: one main
path, two alternate states, synthetic data, one file. What changes is what a "screen" is.

- **Terminal.** Each step is a panel showing the command the actor types and the output
  they see, in a monospace block, with a short caption in plain words above it. The main
  action is a button labelled with the command ("Run `tool sync --dry-run`"). Alternate
  states are the empty result and the error output with its recovery hint. Use the
  1200×800 frame and a light background; do not imitate a particular terminal theme.
- **API or library.** Each step is a panel with the request (or call) on the left and the
  response on the right, both synthetic, with a one-line caption saying what the actor
  learns from it. Alternate states are an empty collection and an error response with the
  field or permission that caused it. A short "what the developer sees in their editor"
  panel is acceptable for a library when the flow is about discoverability.

Everything else in the contract holds: no network, buttons not divs, focus moves to the
new panel's heading, `role="alert"` on the error, the badge in the corner. The walkthrough
checklist below applies unchanged; "labels" means captions and command names.

## Walkthrough checklist (PM design critique, not customer validation)

Go through the main path once and each alternate state once, and check:

- Labels: every button says what happens next; no internal jargon.
- Navigation: the actor always knows where they are and how to go back.
- Keyboard: Tab order follows reading order; nothing is reachable only by mouse.
- State clarity: loading, empty, error, permission, and recovery are visibly different
  and each offers a next step.
- Contrast: body text and primary buttons pass a quick 4.5:1 check.
- Scope: nothing on screen belongs to another lane.

Record one row per area, pass or a specific finding, then propose one revision tied to
discovery evidence or a finding, and let the PM approve or choose a different revision.
