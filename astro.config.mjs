import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://andrewdaniels.design',
  trailingSlash: 'ignore',
  build: { format: 'directory' },
});
