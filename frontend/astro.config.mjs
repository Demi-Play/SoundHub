// @ts-check
import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
// import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [react()],
  vite: {
    server: {
      proxy: {
        '/api': 'http://localhost:8000',
        '/ws': {
          target: 'ws://localhost:8000',
          ws: true,
        },
      },
    },
  },
});

