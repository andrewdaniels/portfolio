import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

/**
 * CONTENT LIVES IN MARKDOWN.
 *   src/content/projects/*.md  → case studies (/projects/<file-name>)
 *   src/content/posts/*.md     → blog posts   (/blog/<file-name>)
 *   src/content/shots/*.md     → short work updates that appear in the feed
 * Set `draft: true` to hide anything without deleting it.
 */

const projects = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/projects' }),
  schema: z.object({
    title: z.string(),
    client: z.string().default(''),
    years: z.string().default(''),
    year: z.number(),
    category: z.string().default(''),
    summary: z.string().default(''),
    overview: z.string().default(''),
    outcome: z.string().default(''),
    cover: z.string().default(''),
    thumbs: z.array(z.string()).default([]),
    shots: z.array(z.string()).default([]),
    order: z.number().default(99),
    featured: z.boolean().default(false),
    /** "now" = something Andrew is building today */
    status: z.enum(['now', 'past']).default('past'),
    tagline: z.string().default(''),
    link: z.string().default(''),
    mockup: z.enum(['iso', 'uncomn']).default('iso'),
    draft: z.boolean().default(false),
  }),
});

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    excerpt: z.string().default(''),
    cover: z.string().default(''),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

const shots = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/shots' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    images: z.array(z.string()).default([]),
    project: z.string().default(''),
    draft: z.boolean().default(false),
  }),
});

export const collections = { projects, posts, shots };
