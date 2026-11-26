---
title: "How I build websites now: Claude, GitHub, and Netlify or Cloudflare"
date: 2026-11-26
excerpt: "A step-by-step for non-technical folks. You describe what you want, Claude writes the site, GitHub keeps every version, and Netlify or Cloudflare puts it online."
tags: ["Process", "AI"]
draft: false
---

You describe what you want. Claude writes the site. GitHub keeps every version. Netlify or Cloudflare puts it online and updates it every time you approve a change.

No page builder, no monthly site-builder bill, and you own all of it.

## Sites I've built this way

Every one of these is the same stack: **Claude** builds it, **GitHub** stores it, and **Netlify or Cloudflare** publishes it. No Webflow, no WordPress, no Squarespace. I review, I approve, and it ships.

### [YWAM Costa Tropical](https://ywamct.com)

A bilingual site for a discipleship school in Spain, in English and Spanish. Claude · GitHub · Cloudflare.

![YWAM Costa Tropical homepage](/media/posts/build-your-website-with-claude/ywamct.webp)

### [ChurchCalls.ai](https://churchcalls.ai)

An AI receptionist for churches. Moved off Webflow to plain files. Claude · GitHub · Cloudflare.

![ChurchCalls.ai homepage](/media/posts/build-your-website-with-claude/churchcalls.webp)

### [KnowHim](https://knowhim.app)

A prayer app for you and your people. The site is plain HTML with no build step. Claude · GitHub · Netlify.

![KnowHim homepage](/media/posts/build-your-website-with-claude/knowhim.webp)

### [Uncomn](https://uncomn.co)

A discipleship platform for churches and small groups. Claude · GitHub · Netlify.

![Uncomn homepage](/media/posts/build-your-website-with-claude/uncomn.webp)

### [Optimal Coffee](https://optimalcoffee.app)

A brew journal for coffee nerds. Claude · GitHub · Netlify.

![Optimal Coffee app screens](/media/posts/build-your-website-with-claude/coffee.webp)

### [YWAM Base](/projects/ywambase)

One app to run a YWAM base. The case study, like everything on this site, was written by prompting Claude. Claude · GitHub · Netlify.

![YWAM Base dashboard](/media/posts/build-your-website-with-claude/ywambase.webp)

## How the pieces fit

Think of it like a document with track changes, wired to a printer.

- **You** say what you want in plain English.
- **Claude** writes and edits the files.
- **GitHub** saves every version. Nothing is ever lost.
- **Netlify or Cloudflare** publishes the latest approved version.

You never touch code if you don't want to. Your job is to describe, look at the preview, and say "yes, ship it."

## 1. Create a GitHub account

GitHub is where your website's files live. It's free.

1. Go to [github.com/signup](https://github.com/signup).
2. Enter your email, a password and a username. Keep the username simple. It shows up in links.
3. Enter the code they email you.
4. When it asks about plans, pick **Free**.

Then make an empty home for your site:

1. Click the **+** in the top right, then **New repository**.
2. Name it after your site, like `my-church-site`.
3. Choose **Private** and tick **Add a README file**.
4. Click **Create repository**. A "repository" (repo) is just a folder with history.

## 2. Pick a host: Netlify or Cloudflare

The host takes the files in GitHub and turns them into a live website. Both have free plans, both rebuild the site every time GitHub changes, and both give you preview links. I use both. Netlify is the easiest for a first site. Cloudflare is great if your domain already lives there.

**Netlify**

1. Go to [app.netlify.com/signup](https://app.netlify.com/signup).
2. Click **Sign up with GitHub**. This is the easy way, because it links the two for you.
3. Approve the GitHub permission screen.
4. Answer the quick welcome questions.

**Or Cloudflare**

1. Go to [dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up) and create a free account.
2. Confirm your email. You'll connect GitHub in step 5.

## 3. Connect Claude to GitHub

You'll need a paid Claude plan (Pro or higher), which includes Claude Code. That's the version of Claude that can work inside your repo.

1. Go to [claude.ai/code](https://claude.ai/code) and sign in.
2. When it asks, click **Connect GitHub** and install the Claude GitHub app.
3. Give it access to the repo you made in step 1. You can choose just that one.
4. Pick your repo. Now Claude can read and change your site's files.

## 4. Ask Claude for your first site

Be specific about who it's for and what people should do. Paste in your real info: service times, address, what you offer. The more real content, the better the first draft. Write it like you'd brief a designer:

> Build a simple, fast website for Grace Community Church in Austin. Pages: Home, About, Visit (Sundays 9 and 11am, 412 Oak St), Events and Give. Clean and modern, lots of white space, our logo colour is navy. Plain HTML and CSS, no build step.

Claude writes the pages, pushes them to a branch and opens a pull request so you can review before anything goes live.

### Give Claude a notes file

The trick that makes this work long term is a file called `CLAUDE.md` in your repo. Claude reads it every time. Put your rules in it once and you stop repeating yourself. Here's the top of the real one for uncomn.co:

```md
# Uncomn marketing site — notes for Claude

- Standing brief: `CONTEXT.md`. Design system: `DESIGN.md`. How the site
  builds and deploys: `README.md`.
- Type is Figtree everywhere on the web (site, mockups, docs). Headings
  are bold (700).
```

And a rule from the YWAMCT one, so the team can't accidentally publish half-done work:

```md
5. Publish only when the tech lead says so (e.g. "publish it").
The Spanish site must always match the English one.
```

You can ask Claude to write this file for you: "Create a CLAUDE.md with our brand colours, tone and the rule that nothing goes live without my OK."

## 5. Put it online

**On Netlify**

1. In GitHub, open Claude's pull request and click **Merge pull request**.
2. In Netlify, click **Add new project**, then **Import an existing project**.
3. Choose **GitHub**, then pick your repo.
4. Leave the settings as they are, or ask Claude to add a `netlify.toml` that sets them.
5. Click **Deploy**. In under a minute you'll get a link like `my-church-site.netlify.app`.

That settings file is short. This is the real one behind uncomn.co:

```toml
[build]
  command = "node build.js"
  publish = "dist"
```

For a plain HTML site like knowhim.app it's even simpler: `publish = "."` and no command at all.

**On Cloudflare**

1. Merge Claude's pull request in GitHub, same as above.
2. In the Cloudflare dashboard, open **Workers & Pages** and click **Create**.
3. Choose to connect a Git repository, sign in with GitHub and pick your repo.
4. Leave the build settings blank for a plain HTML site, or ask Claude what to enter.
5. Click **Deploy**.

ywamct.com and churchcalls.ai both run this way. If a screen doesn't match these steps, paste a screenshot to Claude and ask what to click.

### Use your own domain

1. In Netlify, open your project, then **Domain management**, then **Add a domain**. In Cloudflare, open your project and go to **Custom domains**.
2. Type the domain you own.
3. Your host shows you the DNS records to add where you bought the domain. If that part scares you, ask Claude to walk you through it.
4. HTTPS (the padlock) turns on by itself.

## 6. Make changes forever after

This is the part that sold me. Updating the site is a sentence.

> Add our Christmas Eve services (4pm and 6pm) to the top of the home page, and take down the Easter banner.

1. Ask Claude for the change.
2. Open the preview link your host adds to the pull request. Check it on your phone.
3. Happy? Click **Merge**. Netlify or Cloudflare publishes it automatically.
4. Not happy? Tell Claude what's off. Nothing goes live until you merge.

A real example: a few days ago Claude redesigned the uncomn.co homepage on its own branch. I reviewed it, merged it, and Netlify had it live in 9 seconds. If anything ever breaks, every past version is still in GitHub, and you can roll back with one click on either host.

## What it costs

- **GitHub:** free.
- **Netlify or Cloudflare:** free to start. Most small sites never leave the free tier.
- **Claude:** a Pro plan.
- **Domain:** about $10–20 a year.

Check each site for current pricing.

## Why I'd pick this over a site builder

- **You own it.** It's just files. Move them anywhere, any time.
- **It's fast.** Plain HTML loads almost instantly.
- **Nothing is off limits.** No template is boxing you in. If you can describe it, Claude can build it.
- **You can't really break it.** Every change is reviewable and reversible.

Want help setting this up for your church, ministry or business? [Get in touch](/contact).
