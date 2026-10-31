# Home Assistant design notes

## Established visual patterns

- **Left sidebar plus content area** on tablet and desktop; on phones the sidebar collapses behind a menu button.
- **Cards on a light grey or dark background.** Almost everything on a dashboard is a rounded card with a small shadow, using the theme's radius tokens.
- **Tile cards** are the default building block: icon in a coloured circle, name and state text, optional quick controls (slider, buttons) underneath.
- **Sections layout**: cards grouped under headings in a responsive grid that reflows between phone, tablet and desktop widths.
- **Settings pages** use a data table on wide screens and a stacked list on narrow ones, with a filter pane, search field and top-right overflow menu.
- **Dialogs** have a header with close or back control, a title, scrolling content and bottom actions; on phones many open full-screen.
- **Status colour is sparing**: blue primary for active or selected, orange accent for attention, red for errors, grey for unavailable or disabled. `ha-alert` has info, warning, error and success variants.
- **Icons** are Material Design Icons; the interface supports light and dark mode plus user themes.

## Where the design system lives

Paths are inside `sources/primary`; all Verified at the pinned commit.

- `src/resources/theme/core.globals.ts`: Verified. Border radius scale (`--ha-border-radius-sm` to `-pill`), spacing scale (`--ha-space-1` = 4px to `--ha-space-20` = 80px), animation durations, reduced-motion override.
- `src/resources/theme/typography.globals.ts`: Verified. Roboto body font, monospace code font, 14px base, size scale `--ha-font-size-xs` to `-5xl`, weights, line heights.
- `src/resources/theme/color/color.globals.ts`: Verified. Named colours such as `--primary-color` and `--accent-color` (#ff9800), text and state colours, and a separate `darkColorStyles` block for dark mode.
- `src/resources/theme/color/` (`core.globals.ts`, `semantic.globals.ts`, `index.ts`): Verified. Primitive colour ramps (`--ha-color-primary-40` style) and the semantic layer built on them.
- `src/resources/theme/semantic.globals.ts` and `main.globals.ts`: Verified. Shadow levels for light and dark; header height (56px), text opacities, phone safe areas.
- `src/resources/theme/theme.ts`: Verified. Assembles the above into the global stylesheet.
- `src/resources/ha-icons.ts`, `src/resources/icon-metadata.ts`: Verified. Material Design Icons setup.
- `src/components/`: Verified. Shared `ha-*` components: `ha-card.ts`, `ha-button.ts`, `ha-dialog.ts`, `ha-alert.ts`, `ha-switch.ts`, `ha-list-item.ts`, `ha-settings-row.ts`, `ha-expansion-panel.ts`, `ha-bottom-sheet.ts`, plus `tile/`, `chips/`, `data-table/`, `ha-form/`, `trace/`.
- `src/panels/lovelace/cards/`: Verified. Every built-in dashboard card; shows how cards compose the components above.
- The repository's `gallery/` folder (not in the sparse checkout) is published as the design site linked below.

## Public UI references

- https://demo.home-assistant.io/: live, clickable demo of dashboards, settings and automations.
- https://design.home-assistant.io/: official design site: components, colours, typography, concepts.
- https://www.home-assistant.io/dashboards/: user docs for dashboards with current screenshots.
- https://www.home-assistant.io/dashboards/cards/: catalogue of card types with screenshots.
- https://www.home-assistant.io/dashboards/dashboards/: managing multiple dashboards and setting the default one.
- https://www.home-assistant.io/integrations/repairs/: the Repairs page, with screenshots of the issue list and fix flow.
- https://www.home-assistant.io/integrations/backup/: the Backup page, schedule, locations and restore.
- https://www.home-assistant.io/common-tasks/general/: the Updates page and the update-with-backup flow.
- https://www.home-assistant.io/docs/automation/troubleshooting/: the automation trace view, step by step.
- https://developers.home-assistant.io/docs/frontend/design/: short developer-facing design guidelines.

## Synthetic data guidance

- Home name "Willow House"; household members "Alex" and "Sam" only.
- Rooms: Living Room, Kitchen, Bedroom, Office, Hallway, Garden.
- Devices: Living Room Lamp, Kitchen Plug, Hallway Motion Sensor, Office Speaker, Bedroom Temperature Sensor, Garden Light.
- Entities: `light.living_room_lamp`, `switch.kitchen_plug`, `binary_sensor.hallway_motion`, `media_player.office_speaker`, `sensor.bedroom_temperature`, `light.garden_light`.
- Never real addresses, coordinates, Wi-Fi names, IP or MAC addresses; never camera imagery or photos of people.
- Never model locks, garage doors, alarms, heating or gas appliances, or medical devices.

## Prototype scope reminders

- One self-contained HTML file per prototype; no build step, no external scripts.
- One main path plus two alternate states (for example normal, something unavailable, and an error or empty state).
- Match the lane viewport: 1024x768 for Household dashboards and defaults, 390x844 for Repairs, backups, and recovery from updates, 1440x900 for Automation troubleshooting and safe edits.
- Borrow the patterns above so reviewers recognise the product, but visual similarity is not a completion gate; clarity of the flow is.
