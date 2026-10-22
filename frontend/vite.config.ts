import react from '@vitejs/plugin-react';
import { defineConfig, lazyPlugins } from 'vite-plus';
import { tanstackRouter } from '@tanstack/router-plugin/vite';

// https://vite.dev/config/
export default defineConfig({
  fmt: {
    singleQuote: true,
    ignorePatterns: ['dist/**', '**/routeTree.gen.ts'],
  },
  lint: {
    plugins: ['oxc', 'typescript', 'unicorn', 'react'],
    categories: {
      correctness: 'error',
      suspicious: 'warn',
    },
    env: {
      builtin: true,
      browser: true,
    },
    ignorePatterns: ['dist'],
    options: {
      typeAware: true,
      typeCheck: true,
    },
    // Add this back so Oxlint knows about the vite-plus plugin
    jsPlugins: [
      {
        name: 'vite-plus',
        specifier: 'vite-plus/oxlint-plugin',
      },
    ],
    rules: {
      'react/only-export-components': ['error', { allowConstantExport: true }],
      'vite-plus/prefer-vite-plus-imports': 'error',
      'react/react-in-jsx-scope': 'off',
    },
  },
  plugins: lazyPlugins(() => [
    tanstackRouter({
      target: 'react',
      autoCodeSplitting: true,
    }),
    react(),
  ]),
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
});
