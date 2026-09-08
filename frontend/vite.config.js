import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'
import tailwindcss from '@tailwindcss/vite'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), tailwindcss()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    host: '0.0.0.0',
    port: 8080,
    watch: {
      usePolling: true
    },
    proxy: {
      '/auth': {
        target: 'http://backend:8000',
        changeOrigin: true,
      },
      '/criaturas': {
        target: 'http://backend:8000',
        changeOrigin: true,
      },
      '/catalogos': {
        target: 'http://backend:8000',
        changeOrigin: true,
      },
      '/acciones': {
        target: 'http://backend:8000',
        changeOrigin: true,
      },
      '/habilidades': {
        target: 'http://backend:8000',
        changeOrigin: true,
      },
      '/inmunidades': {
        target: 'http://backend:8000',
        changeOrigin: true,
      },
      '/salvaciones': {
        target: 'http://backend:8000',
        changeOrigin: true,
      },
      '/resistencias': {
        target: 'http://backend:8000',
        changeOrigin: true,
      },
      '/sentidos': {
        target: 'http://backend:8000',
        changeOrigin: true,
      },
      '/batallas': {
        target: 'http://backend:8000',
        changeOrigin: true,
      }
    }
  }
})