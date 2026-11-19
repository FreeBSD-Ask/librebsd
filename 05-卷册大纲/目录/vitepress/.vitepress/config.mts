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
        text: `第${String(volNo).padStart(2, '0')}卷　${t ? plainTitle(t) : node.text}`,
        collapsed: false,
        items: [],
      },
    ]
  } else if (node.level === 1 && perVol[curVolKey]) {
    const chNo = Number(node.num ?? 0)
    const t = chTitleByKey.get(`${volNo}:${chNo}`)
    perVol[curVolKey][0].items.push({
      text: `第 ${chNo} 章　${t ? plainTitle(t) : node.text}`,
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
  // 关掉 per-page git 取时：本仓历史深、文件多，614 页各跑一次 git 是不可接受的开销；
  // 页面版本串改由 ui-strings.json 的 shell.page_version 提供（与装配页同源），口径不丢。
  lastUpdated: false,
  sitemap: { hostname: HOST },
  head: [
    ['link', { rel: 'icon', href: `${BASE}favicon.ico` }],
    ['link', { rel: 'canonical', href: `${HOST}${BASE}` }],
    ['meta', { name: 'theme-color', content: '#b0004f' }],
    // 社交分享与结构化数据（对应装配页的 OG 面；标题／描述取数据源，不硬编码口径）
    ['meta', { property: 'og:type', content: 'book' }],
    ['meta', { property: 'og:site_name', content: bookTitle }],
    ['meta', { property: 'og:title', content: bookTitle }],
    ['meta', { property: 'og:description', content: DESCRIPTION }],
    ['meta', { property: 'og:url', content: `${HOST}${BASE}` }],
    ['meta', { property: 'og:locale', content: 'zh_CN' }],
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
    server: { fs: { allow: ['..', '../..'] } },
  },
})
