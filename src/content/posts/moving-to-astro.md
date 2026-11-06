---
title: "I moved my site to Astro"
date: 2026-11-05
excerpt: "My portfolio is now an Astro site where every case study and post is a Markdown file. I write new ones by prompting them."
tags: ["Process", "AI"]
draft: false
---

My portfolio now runs on [Astro](https://astro.build). Every case study, post and work update on it is a Markdown file in a Git repo, and the site rebuilds whenever one of those files changes.

## Why Astro

- **It's fast.** Astro builds the site into plain HTML ahead of time. There's no app booting up in your browser, so pages load almost immediately. JavaScript only runs where something actually moves.
- **I can build anything.** The heroes for Uncomn and KnowHim are the same animations that run on those products' own sites. I copied the code over. No visual builder stands between an idea and the page.
- **I own the content.** Everything is text files with version history. I can read it, move it anywhere and undo any change.

## A content system made of text files

Before, my content lived in a small database. There were collections for projects, testimonials, work history and product highlights, each with its own set of fields. Adding a case study meant filling in every field, uploading images one at a time, then checking that the templates displayed it all correctly.

Now each case study is a single Markdown file. A few lines at the top hold the facts: client, years, scope and which images to show. The story goes underneath. Blog posts and the short updates in the feed work the same way.

## Prompting case studies together

Because the whole site is files, I can describe what I want and have Claude write it. "Add the V2 KnowHim screens and refresh the copy from the live site." "Write up the Uncomn widgets." "Move KnowHim to the top." It edits the files, I review the changes, and the site deploys.

The work I enjoy is still mine: deciding what to show, shaping the story and judging the details. What I've dropped is the busywork of moving content into a CMS. Case studies and articles now take me minutes to draft instead of an afternoon.

More soon.
