import { getCollection } from 'astro:content';
import type { FeedEntry } from '../components/FeedItem.astro';

export async function getProjects() {
  const all = await getCollection('projects', (p) => !p.data.draft);
  return all.sort((a, b) => a.data.order - b.data.order);
}

export async function getPosts() {
  const all = await getCollection('posts', (p) => !p.data.draft);
  return all.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
}

/** Everything, newest first: blog posts, work updates ("shots") and case studies. */
export async function getFeed(): Promise<FeedEntry[]> {
  const [posts, shots, projects] = await Promise.all([
    getPosts(),
    getCollection('shots', (s) => !s.data.draft),
    getProjects(),
  ]);
  const items: FeedEntry[] = [
    ...posts.map((p) => ({
      kind: 'post' as const, id: p.id, title: p.data.title, text: p.data.excerpt, date: p.data.date,
      images: p.data.cover ? [p.data.cover] : [], href: `/blog/${p.id}`, meta: p.data.tags[0],
    })),
    ...shots.map((s) => ({
      kind: 'shot' as const, id: s.id, title: s.data.title, text: (s.body || '').trim(), date: s.data.date,
      images: s.data.images, href: s.data.project ? `/projects/${s.data.project}` : undefined,
    })),
    ...projects.map((p) => ({
      kind: 'project' as const, id: p.id, title: `${p.data.title}: ${p.data.overview || p.data.tagline}`,
      text: p.data.summary, date: new Date(Date.UTC(p.data.year, 0, 1)),
      images: [p.data.cover, ...p.data.thumbs].filter(Boolean).slice(0, 4),
      href: `/projects/${p.id}`, meta: p.data.years,
    })),
  ];
  return items.sort((a, b) => b.date.valueOf() - a.date.valueOf());
}
