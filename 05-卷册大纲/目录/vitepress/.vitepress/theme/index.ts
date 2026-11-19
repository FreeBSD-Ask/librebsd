import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import CatalogApp from './components/CatalogApp.vue'
import DataPanel from './components/DataPanel.vue'
import './catalog-tokens.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('CatalogApp', CatalogApp)
    app.component('DataPanel', DataPanel)
  },
} satisfies Theme
