import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import CatalogApp from './components/CatalogApp.vue'
import DataPanel from './components/DataPanel.vue'
import FontScale from './components/FontScale.vue'
import NoteLayer from './components/NoteLayer.vue'
import ToolsMenu from './components/ToolsMenu.vue'
import './catalog-tokens.css'
import './outline.css'

/**
 * 壳层按 ykla 2026-11-20 裁定保留 VitePress 默认主题（顶栏／本卷 sidebar／右 aside／页脚），
 * 只把装配页的功能面与排印面接进来：
 *  · nav 右端槽位＝工具面（导出／阅读版／时间线／修订史／图谱／注）；
 *  · 移动端 nav 屏内菜单同槽位再挂一份（两个实例各自持状态，互不干扰）；
 *  · layout-bottom 单实例挂注徽标事件委托。
 */
export default {
  extends: DefaultTheme,
  Layout: () =>
    h(DefaultTheme.Layout, null, {
      'aside-outline-before': () => h(FontScale),
      'nav-bar-content-after': () => h(ToolsMenu),
      'nav-screen-content-after': () => h(ToolsMenu),
      'layout-bottom': () => h(NoteLayer),
    }),
  enhanceApp({ app }) {
    app.component('CatalogApp', CatalogApp)
    app.component('DataPanel', DataPanel)
    app.component('FontScale', FontScale)
  },
} satisfies Theme
