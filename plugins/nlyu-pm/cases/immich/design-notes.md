# Immich design notes

## Established visual patterns

**Desktop web.** A left-hand navigation sidebar with the main content area to its right. The photo timeline is a dense grid of thumbnails grouped under date headings, with a scrubber along the right edge for jumping through time. A top bar holds search and account controls; the web search UI changed in v3.2.0 (released 2026-09-10), so do not copy the older search modal. Buttons and inputs use rounded corners (Tailwind `rounded-lg`), light grey fills on inputs, and a single accent colour: indigo `rgb(66, 80, 175)` in light mode and pale blue `rgb(172, 203, 250)` in dark mode. Icons are Material Design Icons (`@mdi/js`). Typography uses the "GoogleSans" font family. Empty pages show a simple line illustration with a short message. Sources: `web/src/app.css`, `web/src/lib/components/*`, `web/src/routes/(user)/sharing/+page.svelte`, `design/immich-screenshots.png`.

**Mobile app.** A Flutter app using Material 3 (Google's current design language). App bars have a centred title in the accent colour on a plain surface with no shadow; bottom sheets and dialogs use slightly tinted surfaces; snack-bar notices show bold accent-coloured text. Users can pick from ten colour presets (indigo default, deep purple, pink, red, orange, yellow, lime, green, cyan, slate grey) or follow the phone's own colours, so avoid hard-coding a single accent in prototypes. Sources: `mobile/lib/theme/theme_data.dart`, `mobile/lib/theme/color_scheme.dart`, `mobile/lib/constants/colors.dart`, screenshots in `docs/docs/features/img/`.

## Where the design system lives

- `web/src/app.css`: Verified. Web colour tokens, fonts, breakpoints and the dark-mode switch.
- `@immich/ui` (npm package, imported in `app.css`): Not in this repo; it is the shared component library from the separate `immich-app/ui` project.
- `web/src/lib/elements`: Verified. Small web building blocks (dropdown, search bar, skeleton loader, star rating, date input).
- `web/src/lib/components/shared-components`: Verified. Reusable web pieces such as empty-state placeholder and user avatar.
- `web/src/lib/components/sidebar` and `layouts`: Verified. Navigation sidebar and page frames.
- `web/src/lib/assets`: Verified. Fonts and empty-state SVG illustrations.
- `mobile/lib/theme`: Verified. Material 3 theme, colour presets and dynamic (system) colour.
- `mobile/lib/constants/colors.dart`: Verified. Brand colours: light `#4150AF`, dark `#ACCBFA`.
- `mobile/lib/widgets/common`: Verified. Shared mobile widgets.
- `mobile/fonts`: Verified as a directory; not in the sparse checkout.
- `design/`: Verified. Logos (SVG and PNG) and a product screenshot montage.
- `i18n/en.json`: Verified. English labels; use these exact words in prototypes.

## Public UI references

- Mobile backup screens. https://docs.immich.app/features/mobile-backup/
- Mobile app overview, sync indicators, free-up-space. https://docs.immich.app/features/mobile-app/
- Web and mobile sharing screens, shared links. https://docs.immich.app/features/sharing/
- Partner sharing flow. https://docs.immich.app/features/partner-sharing/
- Public demo of the web app. https://demo.immich.app/

## Synthetic data guidance

- People: invented first names with an initial ("Priya N.", "Jordan L.", "Sam O."); avatars are initials in coloured circles, never face images.
- Devices: "Jordan's phone", "Kitchen tablet", "Old iPhone".
- Albums: everyday but fictional titles ("Lake weekend 2025", "Birthday cake attempts", "School play").
- Dates: keep within 2024–2026; counts like "12,438 photos, 1,204 videos"; storage like "48.2 GB of 500 GB".
- Thumbnails: solid colour blocks, soft gradients or simple SVG shapes (circles, hills, a sun); no stock photos, no real faces, no maps of real addresses.
- Server and account names: "family-server.local", "steward@example.com".

## Prototype scope reminders

- One single-file HTML prototype per lane; inline CSS and JavaScript.
- Show one main path plus two alternate states (for example empty, error, loading, or permission-denied).
- Match the lane viewport exactly: 390×844 for the two mobile lanes, 1440×900 for desktop web.
- Reuse the accent colour, rounded corners and label wording above so it feels like Immich, but visual similarity is not a completion gate; clarity of the flow is.
