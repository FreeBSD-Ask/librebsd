/**
 * VitePress 站点配置（参照 FreeBSD-Ask/librebsd 惯例：zh-CN、cleanUrls、metaChunk、zh themeConfig、sitemap）。
 * 侧边栏：结构取自 SUMMARY.md（GitBook 目录真值），显示题名取自 outline.txt（内容真值）；
 * 两者的号序与四数由 scripts/verify-assembly.ts 锁定一致，故此处的号键查找是安全的。
 *
 * 分卷构建：环境变量 VP_SHARD 控制本次构建的 srcDir／outDir（home＝站点壳页，vNN＝单卷页）。
 * 由 scripts/build-by-volume.ts 逐卷并行调用，产物按路径合并进 .vitepress/dist。
 */
import { defineConfig } from 'vitepress'
import { readOutline, readSummary, readUiStrings, SITE_ROOT } from '../scripts/lib/source'

const BASE = '/librebsd/'
const HOST = 'https://freebsd-ask.github.io'

/** 分卷开关：未设＝开发／整站模式（srcDir '.'）；设 home 或 vNN＝分片构建。 */
const SHARD = process.env.VP_SHARD
/** 隔离根模式（分卷并行）：根目录本身即内容根，产物目录由 VP_OUT 指定（绝对路径）。 */
const ISOLATED = process.env.VP_SRC_DOT === '1'
const isVol = !!SHARD && /^v\d+$/.test(SHARD)
const srcDir = ISOLATED ? '.' : !SHARD ? '.' : isVol ? `.build/${SHARD}` : '.build/home'
const outDir = process.env.VP_OUT ?? (!SHARD ? '.vitepress/dist' : `.build/out/${isVol ? SHARD : 'home'}`)

const ui = readUiStrings() as Record<string, string>
const tree = readOutline()
const summary = readSummary()

// SUMMARY 卷题 → 对应 outline 卷（按卷号）
const volTitleByNo = new Map(tree.vols.map((v) => [v.no, v.title]))
const chTitleByKey = new Map<string, string>()
for (const v of tree.vols) for (const c of v.chs) chTitleByKey.set(`${v.no}:${c.no}`, c.title)

const plainTitle = (t: string) => t.replace(/⟦en:([^⟧]*)⟧/g, '$1')

// 按 SUMMARY 的层级顺序重建侧边栏：卷（level0）→ 章（level1）。
// 按卷分表（key=/vNN/）：若挂全局单表，539 条链接会内联进 615 个页面，
// 单页 HTML 达 ~290 KB、整站产物 ~193 MB；分表后每页只带本卷章目。
const perVol: Record<string, Array<{ text: string; collapsed: boolean; items: Item[] }>> = {}
let volNo = 0
let curVolKey = ''
for (const node of summary) {
  if (node.level === 0) {
    volNo = Number(node.num ?? volNo + 1)
    curVolKey = `/v${String(volNo).padStart(2, '0')}/`
    const t = volTitleByNo.get(volNo)
    perVol[curVolKey] = [
      {
        text: `第${String(volNo).padStart(2, '0')}卷  ${t ? plainTitle(t) : node.text}`,
        collapsed: false,
        items: [],
      },
    ]
  } else if (node.level === 1 && perVol[curVolKey]) {
    const chNo = Number(node.num ?? 0)
    const t = chTitleByKey.get(`${volNo}:${chNo}`)
    perVol[curVolKey][0].items.push({
      text: `第 ${chNo} 章 ${t ? plainTitle(t) : node.text}`,
      link: `/v${String(volNo).padStart(2, '0')}/c${String(chNo).padStart(2, '0')}`,
    })
  }
}
// 卷页与章页共用本卷表：chapter 路径同样以 /vNN/ 为前缀
const sidebar = Object.keys(perVol).length ? perVol : undefined

if (!ui['shell.book_title']) {
  throw new Error('[config] ui-strings.json 缺 shell.book_title：书名是单一真值，不得 fallback')
}
const bookTitle = ui['shell.book_title'] as string
const t0 = tree.counts
const DESCRIPTION =
  `${bookTitle}：卷章节目录（${t0.vols} 卷／${t0.chs} 章／${t0.secs} 节／${t0.subs} 小节），据编译内容源实时生成`

export default defineConfig({
  lang: 'zh-CN',
  title: bookTitle,
  description: DESCRIPTION,
  base: BASE,
  srcDir,
  outDir,
  // 隔离根模式下产物写在根外（.build/out/<分片>），需显式允许并清空
  emptyOutDir: true,
  // 站点根下的 README 不是内容页（站点说明见该文件本身）
  srcExclude: ['README.md', 'node_modules/**', '.build/**'],
  cleanUrls: true,
  metaChunk: true,
  // 分片构建下，小节页的“上/下一小节”与面包屑可能跨卷——该目标页在别的分片，本片判死链属必然假阳。
  // 故只对**跨卷**链接放行（逐卷生成 `^/vNN(/|$)` 规则），本卷内死链仍严格 FAIL；
  // 跨卷路由是否存在，由合并步的“预期路由集合 == 实际产物”全等断言兜底（全集构建）。
  ignoreDeadLinks: isVol
    ? tree.vols
        .filter((v) => v.no !== Number(SHARD!.slice(1)))
        .map((v) => new RegExp(`^/v${String(v.no).padStart(2, '0')}(/|$)`))
    : false,
  // 关掉 per-page git 取时：本仓历史深、文件多，614 页各跑一次 git 是不可接受的开销；
  // 页面版本串改由 ui-strings.json 的 shell.page_version 提供（与装配页同源），口径不丢。
  lastUpdated: false,
  sitemap: { hostname: HOST },
  head: [
    ['link', { rel: 'icon', href: `${BASE}favicon.ico` }],
    ['link', { rel: 'apple-touch-icon', sizes: '180x180', href: `${BASE}apple-touch-icon.png` }],
    ['link', { rel: 'canonical', href: `${HOST}${BASE}` }],
    // 主题色与装配页同源：纸色／OLED 纯黑两态（按配色方案切换，不写品牌粉）
    ['meta', { name: 'theme-color', content: '#F9F5F0' }],
    ['meta', { name: 'theme-color', media: '(prefers-color-scheme: dark)', content: '#000000' }],
    ['meta', { name: 'mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black-translucent' }],
    ['meta', { name: 'apple-mobile-web-app-title', content: ui['shell.app_title'] ?? '给我自由' }],
    // 溯源注默认收起只在 html.js 时生效：无脚本（或脚本被拦）时注文直接可读，满足 noscript 可读
    ['script', {}, 'document.documentElement.classList.add("js")'],
    // 内容安全策略：静态托管无法设 HTTP 头，只能 meta。VitePress 大量内联脚本，故 script/style
    // 保留 'unsafe-inline'（诚实披露：此 CSP 只收敛 object/base/form/connect 面，不做 nonce 级加固）。
    [
      'meta',
      {
        'http-equiv': 'Content-Security-Policy',
        content:
          "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; font-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'none'",
      },
    ],
    ['meta', { name: 'referrer', content: 'no-referrer' }],
    // 社交分享与结构化数据（对应装配页的 OG 面；标题／描述取数据源，不硬编码口径）
    ['meta', { property: 'og:type', content: 'book' }],
    ['meta', { property: 'og:site_name', content: bookTitle }],
    ['meta', { property: 'og:title', content: bookTitle }],
    ['meta', { property: 'og:description', content: DESCRIPTION }],
    ['meta', { property: 'og:url', content: `${HOST}${BASE}` }],
    ['meta', { property: 'og:locale', content: 'zh_CN' }],
    ['meta', { property: 'og:image', content: `${HOST}${BASE}apple-touch-icon.png` }],
    ['meta', { property: 'og:image:width', content: '180' }],
    ['meta', { property: 'og:image:height', content: '180' }],
    ['meta', { property: 'og:image:alt', content: `${bookTitle}（书名标志）` }],
    ['meta', { name: 'twitter:card', content: 'summary' }],
    [
      'script',
      { type: 'application/ld+json' },
      JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'Book',
        name: bookTitle,
        inLanguage: 'zh-CN',
        url: `${HOST}${BASE}`,
        description: DESCRIPTION,
      }),
    ],
  ],
  markdown: {
    image: { lazyLoading: true },
    lineNumbers: false,
    config(md) {
      // 行内 code 加 v-pre，避免 {{ }} 被当成 Vue 插值
      const d = md.renderer.rules.code_inline!
      md.renderer.rules.code_inline = (tokens, idx, opts, env, self) => {
        tokens[idx].attrSet('v-pre', '')
        return d(tokens, idx, opts, env, self)
      }
    },
  },
  themeConfig: {
    siteTitle: bookTitle,
    // logo 由 VitePress 自动加 base，此处不得再拼 BASE（否则 /librebsd/librebsd/…）
    logo: { src: '/favicon.ico', width: 24, height: 24 },
    socialLinks: [{ icon: 'github', link: 'https://github.com/FreeBSD-Ask/librebsd' }],
    outline: { label: '本页目录', level: [2, 3] },
    docFooter: { prev: '上一页', next: '下一页' },
    sidebarMenuLabel: '目录',
    returnToTopLabel: '回到顶部',
    darkModeSwitchLabel: '主题',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式',
    langMenuLabel: '多语言',
    // 跨页检索：VitePress 原生 localSearch（⌘K／Ctrl+K）。分片构建下各片索引互不相通，
    // 故合并步由 scripts/build-by-volume.ts 用同一 MiniSearch 口径重造全站索引并覆盖索引 chunk。
    search: {
      provider: 'local',
      options: {
        detailedView: true,
        translations: {
          button: { buttonText: '检索', buttonAriaLabel: '检索' },
          modal: {
            displayDetails: '展开详情',
            resetButtonTitle: '清除检索',
            backButtonTitle: '关闭检索',
            noResultsText: '无匹配结果',
            footer: {
              selectText: '选择',
              navigateText: '切换',
              closeText: '关闭',
            },
          },
        },
      },
    },
    lastUpdated: { text: '最后更新于', formatOptions: { dateStyle: 'long', timeStyle: 'short' } },
    notFound: {
      title: '页面未找到',
      quote: '此页尚未落入站点，请回到目录检索。',
      linkLabel: '返回首页',
      linkText: '返回首页',
      code: '404',
    },
    nav: [
      { text: '目录', link: '/' },
      { text: '数据视图', link: '/#data' },
      { text: 'GitHub', link: 'https://github.com/FreeBSD-Ask/librebsd' },
    ],
    sidebar,
  },
  vite: {
    // 分卷构建时 srcDir 下沉到 .build/<分片>，Vite 的 publicDir 会跟着 srcDir 走而漏掉静态件；
    // 这里显式钉在站点根，保证 fonts／favicon 每片都进产物（合并时同名同内容自动去重）。
    publicDir: `${SITE_ROOT}/public`,
    plugins: [
      {
        // bun 在映射网络盘上把模块 URL 解成 UNC（import.meta.url＝file://desktop-m5p610n/d/...），
        // vitepress 用自身 import.meta.url 推出的客户端入口（APP_PATH/index.js）随之为 //host/... 形态；
        // vite/rolldown 把以 // 开头的 id 当协议相对 URL 外链，且 UNC 链上的 plugin-vue 主模块
        // 不挂样式子模块（探针实测 transform hasStyleImport=false）→ 组件样式成片缺失、
        // 产物 HTML 出现指向本机的 modulepreload。此钩子（enforce:pre，输入解析会过 resolveId）双向阻断：
        // ①绝对 UNC 源 → 归一盘符形态；②相对导入的 importer 为 UNC → 以盘符形态的 importer
        // 重新委托默认解析（skipSelf 防递归）。归一后整条客户端图取盘符 id，样式聚合恢复正常
        // （实测 style 包 76 550→125 929 B、VPNavBar 样式回归、UNC 链接归零；运行时基线仍为 bun）。
        name: 'librebsd-bun-unc-normalize',
        enforce: 'pre',
        resolveId(source, importer) {
          const UNC = /^\/\/[^/]+\/([A-Za-z])\/(.*)$/
          const m = UNC.exec(source)
          if (m) return `${m[1].toUpperCase()}:/${m[2]}`
          if (importer) {
            const im = UNC.exec(importer)
            if (im) {
              const r = this.resolve(source, `${im[1].toUpperCase()}:/${im[2]}`, { skipSelf: true })
              if (r) return r
            }
          }
          return null
        },
      },
      {
        // 检索索引 chunk 固定文件名：VitePress 的 chunkFileNames 是内容哈希，各分片索引不同 →
        // 文件名不同 → app chunk 指向不同 → 合并冲突。改为按模块名定名（无哈希），
        // 合并步再用全站索引覆盖数据 chunk（见 scripts/build-by-volume.ts）。
        name: 'librebsd-stable-search-chunk',
        outputOptions(o: { chunkFileNames?: unknown }) {
          const prev = o.chunkFileNames
          o.chunkFileNames = (chunk: { name?: string }) => {
            const n = chunk.name ?? ''
            if (/localSearchIndex/i.test(n)) return `assets/chunks/${n.replace(/[^\w.-]/g, '_')}.js`
            if (typeof prev === 'function') return (prev as (c: unknown) => string)(chunk)
            return 'assets/chunks/[name].[hash].js'
          }
          return o
        },
      },
    ],
    server: { fs: { allow: ['..', '../..'] } },
  },
})
