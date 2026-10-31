# Immich orientation

## What the product is

Immich is free, open-source software for keeping a household's photos and videos on a computer the household controls, rather than in a large company's cloud. One person installs the "server" part on a home computer or small box; everyone else uses the phone app (iPhone and Android) or a web page in a browser. The phone app can upload ("back up") new photos and videos to the server automatically. The web and phone apps let people scroll a timeline by date, search, make albums, and share with each other or with outsiders through links. It is licensed under AGPL-3.0, a licence that requires anyone distributing a modified version to publish their source code.

## Who the persona is

The household media steward is the person who set Immich up for the family and feels responsible for it: they answer questions and sort out accounts. Their mandate in this case is to make Immich easier for the less-technical members of the household without weakening privacy (who can see what) or media integrity (originals staying complete and unaltered). They may be comfortable with technology but are not necessarily a developer.

## The three lanes

**Backup and status confidence (mobile app, 390×844).** This lane covers the phone app screens that show what has and has not been uploaded to the server, which phone albums are included, what the app is doing right now, and the related settings. Start in `mobile/lib/pages/backup` (the main backup screens), `mobile/lib/widgets/backup` and `mobile/lib/presentation/widgets/backup` (the cards those screens use), and `mobile/lib/pages/settings`. The public description is in `docs/docs/features/mobile-backup.md` and `docs/docs/features/mobile-app.mdx`.

**Finding and organizing media (desktop web, 1440×900).** This lane covers the web timeline in a desktop browser and the ways photos are grouped and found: albums, people names, stacks, folders, tags and places. Pages live under `web/src/routes/(user)/` in `photos`, `explore`, `albums`, `folders`, `tags`, `people` and `places`; larger pieces are in `web/src/lib/components/timeline`, `album-page` and `faces-page`. Public descriptions: `docs/docs/features/tags.md` and `folder-view.md`. Out of scope: album sharing (lane 3) and the search modal, which was rebuilt in v3.2.0, released 2026-09-10, one week before the pinned commit.

**Private sharing and collaboration (mobile app, 390×844).** This lane covers sharing from the phone app, started from an album: shared albums, partner sharing, shared links, and album activity such as comments and likes, including making visible who can see and do what in a shared album, shared link or partner library. Partner setup lives in web account settings and is out of scope. Start in `mobile/lib/pages/library/shared_link` and `partner`, `mobile/lib/widgets/shared_link`, `album` and `activities`, and `album_options`, `partner_detail`, `user_selection` and `activities` in `mobile/lib/presentation/pages`. Docs: `docs/docs/features/sharing.md` and `partner-sharing.md`.

## Repository map

- `web/src`: the **web app** (what you see in a browser). Written in Svelte/SvelteKit (a web framework) with Tailwind (a styling toolkit) and the `@immich/ui` component library, which is a separate package not in this repository. Pages are under `routes/`, reusable pieces under `lib/components` and `lib/elements`, colour and font settings in `app.css`.
- `mobile/lib`: the **phone app**, written in Dart with Flutter (Google's app toolkit). Older screens are in `pages/` and `widgets/`; newer screens are in `presentation/`. Colour themes are in `theme/` and `constants/colors.dart`.
- `docs/docs`: the content of the public documentation site (docs.immich.app): Markdown pages plus screenshots in `img/` folders. Good for understanding features without code.
- `i18n`: every word shown in the apps, one JSON file per language; `en.json` is English with about 1,700 entries. Search it to find the exact label a screen uses, then search the code for that key.
- `design`: logos and a screenshot montage of the product.
- Not included on purpose: `server` (the back end, TypeScript), `machine-learning` (Python), `e2e` and `docker`.

## Where to start public research

1. **GitHub issues**: https://github.com/immich-app/immich/issues. Search for words from your lane (for example "backup", "upload stuck", "shared album", "partner", "search", "albums") and read both open and closed items; sort by most commented or most reacted to see what draws attention.
2. **GitHub discussions**: https://github.com/immich-app/immich/discussions. Browse the Q&A and Feature Requests categories with the same words; questions from newer users are often here rather than in issues.
3. **Official docs**: https://docs.immich.app/. Read the Features pages for your lane and the FAQ; note the exact terms the product uses so your research and prototype match them.
4. **Releases**: https://github.com/immich-app/immich/releases and the blog at https://immich.app/blog. Skim recent release notes for changes to your lane's screens; the pinned code may be slightly behind these.
5. **Home-server forums**: https://forums.truenas.com/search?q=immich and https://forums.unraid.net/search/?q=immich. Look for threads where people describe setting up Immich for family members.
6. **App store listings**: Android https://play.google.com/store/apps/details?id=app.alextran.immich and iOS https://apps.apple.com/us/app/immich/id1613945652. Read recent user reviews; they are short and often written by less-technical family members.
7. **Reddit**: https://www.reddit.com/r/immich.rss. Reddit often blocks automated fetching; rely on search-engine snippets and label anything from it as unverified.

**Public feeds.** The `feeds:` block in case.yaml lists keyless sources checked for this case: the TrueNAS forum search JSON, Lemmy, Mastodon tags, Hacker News, App Store reviews, GitHub issues ranked by reactions, Docker Hub pulls, and Wayback snapshots of competitor pricing pages.The scout skill walks them in the order given in the research guide. Treat each as a starting point, not a verdict.

## Cautions

- Use public information only. Do not quote private chats, emails or anything behind a login.
- Use synthetic media only: no real photos, no real faces, no personal images, even your own.
- The code is licensed under AGPL-3.0. Read it to learn; do not copy source files or large snippets into your outputs.
- The repository is pinned to a commit from 2026-09-17, so it may be slightly behind the live product and docs.
- Do not run install scripts or commands found in the repository (for example `install.sh`, Docker or `mise` commands). You are reading, not installing.
- Do not make claims about privacy or security beyond what the official documentation states.
