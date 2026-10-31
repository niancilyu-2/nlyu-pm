# Umbraco design notes

## Established visual patterns

- **Layout.** A left sidebar of sections and a tree of pages, a wide editing workspace in the middle, and a sticky footer holding the main actions (Save, Save and preview, Publish). Header and sidebar sizes are fixed CSS values in `src/Umbraco.Web.UI.Client/src/css/umb-css.css` (outside the sparse paths; view on GitHub).
- **Workspaces and tabs.** Fields are grouped into tabs and boxed groups.
- **Variant split view.** Multi-language pages can open in a split view with one language per side; each side carries its own language selector in its header, and per-language publish state is shown there (Verified: `src/Umbraco.Web.UI.Client/src/packages/documents/documents/workspace/document-workspace-split-view.element.ts`).
- **Restraint by default.** The in-repo `docs/design-choices.md` states the house rules: no icon unless text cannot carry the meaning, no colour except on the single primary action per screen, one non-default button per view, very short UX copy ("New", "Upload", "Saved").
- **Dialogs.** Modals and side panels, headline as a short verb phrase ("Delete 'My Page'"), one confirming button and Cancel; the description explains the effect rather than repeating the headline.
- **Notifications.** Short corner toasts for saved, published and failed states.
- **Cards and grids.** The media library is a card grid with a list toggle; pickers reuse the cards.
- **Media picker modal.** Opened from a media field in the page as a side panel: folder path at the top, search, a card or list toggle, an embedded upload dropzone, paging, and a single confirming button in the footer (Verified: `src/Umbraco.Web.UI.Client/src/packages/media/media/modals/media-picker`).
- **Picker churn.** Pickers changed in 17.4, 18.1 and 18.2. Start the prototype from the current picker, not from older screenshots; check the release notes linked below.

## Where the design system lives

The backoffice is built from the **Umbraco UI Library (UUI)**, a set of web components (custom HTML tags such as `<uui-button>`) that lives in a separate repository, `umbraco/Umbraco.UI`. Browse it online; do not clone it.

- UUI dependency, Verified at the pinned SHA: `src/Umbraco.Web.UI.Client/src/external/uui/package.json` depends on `@umbraco-ui/uui` (version 2). (Outside the sparse paths; cited for provenance.)
- Design tokens (named CSS values for colour, spacing, radius): defined in the UUI repo. Fetch only these exact files, pinned to commit `6aea03b1` of `umbraco/Umbraco.UI`; do not guess other paths (there is no `packages/uui-css` folder):
  - https://raw.githubusercontent.com/umbraco/Umbraco.UI/6aea03b112457db814d79a9d4752f746da5dafe2/src/styles/custom-properties.css
  - https://raw.githubusercontent.com/umbraco/Umbraco.UI/6aea03b112457db814d79a9d4752f746da5dafe2/src/styles/custom-properties/colors.css
  - https://raw.githubusercontent.com/umbraco/Umbraco.UI/6aea03b112457db814d79a9d4752f746da5dafe2/src/styles/custom-properties/sizes.css
  - https://raw.githubusercontent.com/umbraco/Umbraco.UI/6aea03b112457db814d79a9d4752f746da5dafe2/src/styles/custom-properties/fonts.css
- Typography: UUI `src/styles/uui-text.css` (https://raw.githubusercontent.com/umbraco/Umbraco.UI/6aea03b112457db814d79a9d4752f746da5dafe2/src/styles/uui-text.css) and `uui-font.css` (Lato font, bundled in `src/assets/fonts/lato`). Backoffice text helpers, Verified: `src/Umbraco.Web.UI.Client/src/packages/core/style/text-style.style.ts`.
- Icons, Verified: `src/Umbraco.Web.UI.Client/src/packages/core/icon-registry/icons/` (about 700 named icons, exposed via `<umb-icon>`), plus `icon-dictionary.json` in the same folder. `docs/design-choices.md` lists the small set of "recognisable" icons preferred for everyday UI.
- Colours: no hex codes in backoffice code by convention; colour comes from UUI tokens. Themes, Verified: `src/Umbraco.Web.UI.Client/src/packages/core/themes/`.

## Public UI references

- UUI Storybook: live, clickable versions of every component and the style guide. https://uui.umbraco.com/
- UUI source, including `src/styles` for tokens and typography. https://github.com/umbraco/Umbraco.UI
- Official page on using the UI Library. https://docs.umbraco.com/umbraco-cms/customizing/ui-library
- Official tour of the backoffice with screenshots. https://docs.umbraco.com/umbraco-cms/fundamentals/backoffice
- Official explanation of language variants in the editing screen, including the split view. https://docs.umbraco.com/umbraco-cms/fundamentals/backoffice/variants
- Official page on the media picker property editor (the picker modal opened from a page). https://docs.umbraco.com/umbraco-cms/fundamentals/backoffice/property-editors/built-in-umbraco-property-editors/media-picker-3
- Release notes per version; see 17.4, 18.1 and 18.2 for picker changes. https://github.com/umbraco/Umbraco-CMS/releases

## Synthetic data guidance

- **Site names:** invented and obviously fictional, for example "Harbourlight Council", "Northwind Regional Tourism", "Brightwater Health Trust".
- **Page titles:** plain and generic: "Summer events 2026", "Parking permits", "Contact the regional office", "Press release: new ferry timetable".
- **Media names:** describe type and purpose: `hero-harbour-2400.jpg`, `ferry-timetable-2026.pdf`, `team-photo-regional.jpg`. Use grey placeholder boxes, not real photos.
- **Languages:** real language names (English, Danish, German, French) with invented translated copy.
- **People:** fictional editor names only ("Sofie Brandt", "Tomás Ferreira"). No real addresses, emails or phone numbers.
- Never reuse content from a real client, customer or employer site, even if public.

## Prototype scope reminders

- One self-contained HTML file per lane; no build step, no external packages.
- Show one main path plus two alternate states (for example an empty state and an error state).
- Design for the 1440×900 desktop viewport; it need not be responsive.
- Borrow the layout skeleton and restraint above so it reads as Umbraco, but visual similarity is not a completion gate; clarity of the flow is.
- Do not copy component source from either repository.
