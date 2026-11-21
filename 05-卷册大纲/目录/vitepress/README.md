# 目录页站点（VitePress · GitHub Pages）

《给我自由——一部 BSD 的历史》卷章节目录的静态站点。数据源与装配源**零改动**，站点只读消费。

- 部署地址：`https://freebsd-ask.github.io/librebsd/`（项目页，`base: '/librebsd/'`）
- 运行时：**bun**（禁 npm／npx／pnpm／yarn）
- 框架：`vitepress@2.0.0-alpha.21`（npm `next` 现行最新预发布；npm 上不存在 2.0.0-beta.x）

## 2026-11-20 批次：最大化适配装配页（ykla 令）

**范围裁定**（ykla 逐项裁定）：壳层保留 VitePress 默认主题（顶栏 nav／本卷 sidebar／右 aside／页脚），
**不复刻**左栏全量树、sticky 面包屑、阅读进度条、窄屏专用抽屉与检索面板；正文排印、溯源注、指标条、
工具面按 `05-卷册大纲/目录/index.html` 复刻。**配色排除墨水屏**（装配页 `theme-preset.js` 已把 eink 迁 light，站点同样无 eink 分支）。

| 面 | 站点实现 |
| -- | -------- |
| 配色两态 | light＝`--page #F9F5F0` 纸色；`.dark`＝OLED 纯黑（`#000` 底／`#7ee088` 字），令牌逐项照录 `doc.css` 的 `:root`／`html[data-theme="oled"]` |
| 卷段 | 卷题 h1（左 4px 竖线＋底线）、卷导言 `p.vol-overview`、卷级定位注 `p.vol-note` 常显、章目 `h3.chapter`＋“N 节／N 小节”徽标 |
| 章段 | 节＝h2、小节＝h3（保留标题语义，右栏“本页目录”仍可用），CSS 复刻悬挂缩进 `--hang 3.2em` 与等宽节号；小节注按装配页形态随全局“注”展开 |
| 溯源注 | 默认收起＋“注”徽标点开＋全局“注”开关＋三色左边框（迁移／分工／史料，构建期按 `doc.js` 同判据分类）＋图例；无脚本时（`html.js` 门控不生效）注文直接可读 |
| 指标条 | 5 格（卷／章／节／小节／溯源标注＝有注小节 1 797）＋每格 small 注＋版本号上标＋自校验胶囊（6 项：节号连续·章号连续·述评恒末／注分类／卷内章题唯一／ref 可解析／人名／年份） |
| 锚点 | 统一装配页式：`vol-N`／`vol-N-ch-M`／`vol-N-ch-M-sec-A-B`／`…-sub-K`（装配页深链可直落站点同锚） |
| 工具面 | 顶栏 nav：导出 6 格式（SUMMARY／JSON／CSV／TXT／PDF 打印／HTML 本体）、阅读版·研究版、节级时间线、结构修订史、跨卷关联图谱、全局注开关 |
| 检索 | VitePress 原生 localSearch（⌘K／Ctrl+K），索引在合并步重造为全站（23 895 条文档） |
| 鲁棒 | 打印／PDF 样式、OG 位图＋apple-touch-icon、CSP（meta）＋工具面数据 SHA-256 校验、章卷页无脚本可读 |

## 2026-11-21 续批：点击行为对齐装配页＋移动端顶栏

- **卷页＝装配式卷块**：`section.doc-block` 包裹（卷题 h1 点击折叠整块），章 `h3.chapter` 点击折叠本章节列表（FoldLayer.vue 复刻 doc.js 手势：拖选/选中保护、250ms 确认窗、双击兜底折回），节＝`ul.sections > li`（等宽节号＋悬挂缩进＋注徽标点开），小节＝`ul.subsections` 行内注；深链经章 id 锚保留。
- **首页目录树＝纯就地浏览**：章题、节行、小节行一律静态（`span`，非 `a`），点任意层级不跳页，与装配页单页就地浏览一致；跨页导航只保留侧边栏（卷/章）、localSearch 结果与检索框命中三项。卷页与章页仍各自承载全文，深链可直落 `#vol-N-ch-M-sec-A-B`。
- **顶栏移动端**：nav-bar 工具实例 ≤959px 隐藏（`opt-toolsbar--top`），工具收进汉堡抽屉（nav-screen 实例），顶栏不再溢出。
- **V6 双载体口径**：卷页与章页各为全量载体——src／sec-num 逐载体集合合计＝装配 `<main>`，站点总量＝2×装配。

## 2026-11-22 补：一律纯目录（ykla 裁定）

- **不区分 filled 与否**：无论小节树件是 `skeleton`、`filled` 还是 `closed`，站点与装配页一律只发布目录（题名＋注文），不发布取证块正文、不显示填充状态。
- **清除遗留状态徽标**：`data/outline.txt` 中 42 处早批手工写的 `〔DOC_MINE×N〕`（V02 20 处／V05 19 处／另一卷 3 处，与 filled 耦合）已删除，装配页与站点小节目录行不再出现块计数；小节级注随之由 141 组降为 99 组（节级注 2 264 组与有注小节 1 797 不变）。

## 数据分工（单一真值）

| 来源 | 供给 | 说明 |
| ---- | ---- | ---- |
| `../../SUMMARY.md` | **目录结构与侧边栏**（卷→章顺序、层级、号序） | GitBook 目录真值，用户指定“目录走 summary” |
| `../../data/outline.txt` | **显示真值**：四级题名、注文（节级 2 264 组／小节级 99 组；有注小节 1 797）、卷导言、卷级定位注 | 装配器的内容源，题名含 `⟦en:X⟧` 语言标注 |
| `../../data/catalog.json` | DATA 段三视图（人物／文献／修订）＋ 工具面修订史／ref 校验 | 与装配页 DATA 段同源 |
| `../../data/ui-strings.json` | 界面文案（书名、页面版本、指标标签、工具面文案） | 非正文文案真值；随工具面数据原样下发 |
| `../../index.html` | **装配验证对照件**（不参与渲染、不部署） | `bun run verify` 的全量比对对象 |
| `../../assets/` | 字体子集、favicon、apple-touch-icon、logo.svg | 构建期抽到 `public/`，装配源零改动 |

`bun run verify` 的布尔判据＝**四数全等＋第五数（装配页“溯源标注”＝有注小节数 1 797）＋号序逐位＋outline↔装配页 23 281 有序题名对逐位一致＋章题序列＋V6 点名级结构断言**（装配页与站点生成源的锚点集合全等，`.vol-overview`／`.vol-note`／`.src`／`.sec-num` 四类计数相等）；任一不符即失败并阻断构建。SUMMARY 只承担结构与号序判据，其**题名**与 outline 的漂移仅作 INFO 披露——改题线会合法地让两者暂时不一致。

注文口径：站内解析节级注**2 264** 组、小节级注 **99** 组、有注小节 **1 797**（＝装配页第五数）。README 旧记的“2 257”为先前内容的旧值，现行以解析实测为准（该数随 outline 内容变动，不作判据）。

## 命令

```bash
bun install          # 安装依赖（生成 bun.lock）
bun run sync         # 从 assets/ 抽字体子集、复制 favicon／apple-touch-icon／logo.svg → public/
bun run gen          # 由 outline.txt 生成 75 卷页 + 539 章页 + public/data/catalog-data.json
bun run verify       # 三源互证＋V6 结构断言：SUMMARY ↔ outline ↔ 装配页 index.html
bun run docs:dev     # 本地开发（http://localhost:5173/librebsd/）
bun run build:vols   # 分卷构建再合并 → .vitepress/dist/（逐卷 6—8 s，全量约 10 分钟）
bun run docs:build   # sync + gen + verify + build:vols（部署口径）
bun run build:vols --only 1-3  # 试点／排障：只构建壳页与指定卷（检索索引仍为全量）
bun run docs:preview # 预览构建产物
```

## 目录角色

- `.vitepress/`：站点配置与主题（`theme/` 承载 `extends: DefaultTheme`；`catalog-tokens.css`＝doc.css 令牌全量映射，`outline.css`＝正文／注／指标／工具面板／打印复刻层）。
- `.vitepress/theme/components/`：`CatalogApp.vue`（首页目录应用）、`ToolsMenu.vue`（顶栏工具面）、`NoteLayer.vue`（注徽标委托）、`DataPanel.vue`、`FontScale.vue`。
- `.vitepress/theme/lib/tools.ts`：工具面数据装载（含 SHA-256 校验）与六格式导出、时间线、图谱构造。
- `public/`：原样发布的静态件（`favicon.ico`、`apple-touch-icon.png`、`logo.svg`、字体子集、`data/catalog-data.json` 与 manifest），**生成件不入库**。
- `scripts/`：`lib/source.ts`（解析层）、`lib/notes.ts`（注分类／锚点）、`lib/search-index.ts`（全站检索索引）、`sync-assets.ts`、`gen-pages.ts`、`verify-assembly.ts`、`build-by-volume.ts`。
- `data/`：VitePress 构建期 data loaders（`book.data.ts`、`catalog.data.ts`），只在首页加载。

## 本批不做（留后续批）

左栏全量卷章树、sticky 面包屑与阅读进度条、窄屏专用抽屉、复刻式检索面板（改以 localSearch 承担跨页检索）、字号四档＋滑块菜单（沿用既有 `FontScale.vue`）、键盘快捷键、粘性卷章页眉、墨水屏配色（ykla 裁定排除）、`noscript` 全量镜像（现为注文可读＋卷页直链）、字体子集再生（只消费 doc.css 既存子集）。

## 已知限制

- `bun install` 偶报 `@docsearch/js` 单包 `ENOENT`（缓存复制失败）；本站不用 Algolia 搜索，构建不受影响。
- `SUMMARY.md` 的陈旧项已于 2026-11-19 用官方再生器 `sync_outline_mirror.py --write` 清零（`--check` 逐条双射 PASS，仅 1 行差异）；`sync_gitbook_summary.py` 在执行该行动时于现行文件上 `StopIteration`，但该器**已被规则明令停用**（`01-规则/大纲层级与目录规则.md` §27），故不是缺陷、也不应据此改 SUMMARY——再生一律走 `sync_outline_mirror.py`。
- **检索索引 17.8 MB（gzip 3.2 MB）**：localSearch 的索引是虚拟模块，各分片只索引本片页面，合并后客户端只会取到最后一片的索引；故合并步用与客户端 `loadLocalSearchIndex()` 同一 MiniSearch 口径从内容源重造全站索引（23 895 条文档），覆盖 chunk 文件名固定的数据 chunk（`config.mts` 的 `librebsd-stable-search-chunk` 插件保证文件名无内容哈希）。索引首次打开检索时才加载，不阻塞页面。
- **运行时基线＝bun（ykla 2026-11-17 令，禁 npm／node 启动）**：本仓在映射网络盘上，bun 下模块 `import.meta.url` 给出 UNC（`file://desktop-m5p610n/d/…`），vitepress 用自身 `import.meta.url` 推出的客户端入口随之为 `//host/…` 形态——vite/rolldown 把以 `//` 开头的 id 当协议相对 URL 外链，且 UNC 链上的 plugin-vue 主模块不挂样式子模块（探针实测 `hasStyleImport=false`），组件 CSS 成片缺失（实测 style 包仅 76 KB、`VPNavBar` 缺失）。修复＝`config.mts` 的 `librebsd-bun-unc-normalize` 插件（enforce:pre 的 resolveId 把绝对 UNC 源归一盘符形态，相对导入的 UNC importer 用盘符形态重新委托解析）；实测 style 包 76 550→125 929 B、`VPNavBar` 样式回归、UNC 链接归零。合并步以“HTML 出现 `href|src="//"`”与“style 包须含 `VPNavBar`”两判据锁死该形态，两判据与驱动进程无关。
- 首页目录树在展开卷／章时才渲染下层级，避免 19 363 节点全量入 DOM；侧边栏按卷分表（`/vNN/`），避免 539 条链接内联进每个页面。
- 分卷构建：逐卷独立构建再合并。VitePress 的临时目录固定为 `<root>/.vitepress/.temp`，同根并行会互删中间件（实测 `ENOENT … .temp/v01_c10.md.js`），故顺序执行。合并步整站再生 `hashmap.json`（各分片并集）、`sitemap.xml`（按合并后实际 HTML 全量重生成）与全站检索索引。
- `lastUpdated` 关闭：per-page git 历史查询 × 614 页不可接受；页面版本串由 `ui-strings.json` 的 `shell.page_version` 提供（与装配页同源）。
- CSP 为 meta 声明且 `script-src`／`style-src` 含 `'unsafe-inline'`（VitePress 内联脚本无法逐个加 nonce）；它只收敛 `object-src`／`base-uri`／`form-action`／`connect-src` 面，**不构成 nonce 级加固**。工具面数据文件另有 SHA-256 自校验（失败关闭）。
