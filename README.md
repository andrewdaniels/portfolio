# andrewdaniels.design

Andrew Daniels' portfolio. It's a static [Astro](https://astro.build) site deployed on Netlify. Every content file is Markdown or JSON, so it can be edited by hand or by Claude, and each push to `main` redeploys the site.

## Where things live

| What | File(s) | URL |
|---|---|---|
| Case studies | `src/content/projects/<slug>.md` | `/projects/<slug>` |
| Blog posts | `src/content/posts/<slug>.md` | `/blog/<slug>` |
| Feed updates ("shipped" shots) | `src/content/shots/<slug>.md` | `/feed` |
| Bio, stats, clients, socials, contact budgets | `src/data/site.json` | everywhere |
| Work history | `src/data/work.json` | About sheet, home |
| Testimonials | `src/data/testimonials.json` | home |
| Images | `public/media/<project>/…` | `/media/…` |

## Common edits

- **New blog post:** add `src/content/posts/my-post.md` with `title`, `date` and `excerpt` front matter. It also shows up in the feed and the RSS feed.
- **New feed update:** add `src/content/shots/thing.md` with `title`, `date`, `images: [...]` and an optional `project: <slug>` link. Write the caption in the body.
- **New case study:** copy an existing project file. `order` sets its position. `status: "now"` puts it under "Building now". `draft: true` hides it.
- **Change the hero or bio copy:** edit `src/data/site.json`. The four hero quadrants are in `src/components/Hero.astro`.
- **Colors and fonts:** edit the tokens at the top of `src/styles/global.css`. Set `--font-display` to change the headline font.

## Run locally

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # outputs to dist/
```

## Notes

- Contact form submissions go to **Netlify Forms** (Netlify → Project → Forms).
- Old Webflow URLs keep working. `/projects/<slug>` is unchanged, and `/project`, `/about` and `/contact` are handled (see `netlify.toml`).
