import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import CatalogApp from './components/CatalogApp.vue'
import DataPanel from './components/DataPanel.vue'
import FontScale from './components/FontScale.vue'
import './catalog-tokens.css'

export default {
  extends: DefaultTheme,
  // 字号档位挂进默认主题的侧栏顶部槽位（卷页／章页可见；首页另有页内控件）
  Layout: () => h(DefaultTheme.Layout, null, { 'aside-outline-before': () => h(FontScale) }),
  enhanceApp({ app }) {
    app.component('CatalogApp', CatalogApp)
    app.component('DataPanel', DataPanel)
    app.component('FontScale', FontScale)
  },
} satisfies Theme
