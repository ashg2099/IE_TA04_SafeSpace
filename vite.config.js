import { fileURLToPath, URL } from 'node:url';
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import vueJsx from '@vitejs/plugin-vue-jsx';
import vueDevTools from 'vite-plugin-vue-devtools';
import nightwatchPlugin from 'vite-plugin-nightwatch';
// https://vite.dev/config/
export default defineConfig({
    base: '/',
    plugins: [vue(), vueJsx(), vueDevTools(), nightwatchPlugin()],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url)),
        },
    },
    server: {
        proxy: {
            '/api': {
                target: 'http://54.79.69.184:5000',
                // target: 'http://localhost:5000',
                changeOrigin: true,
                rewrite: (path) => path,
            },
        },
    },
});
