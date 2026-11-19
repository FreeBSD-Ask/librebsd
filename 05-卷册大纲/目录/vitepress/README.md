# 目录页站点（VitePress · GitHub Pages）

《给我自由——一部 BSD 的历史》卷章节目录的静态站点。数据源与装配源**零改动**，站点只读消费。

- 部署地址：`https://freebsd-ask.github.io/librebsd/`（项目页，`base: '/librebsd/'`）
- 运行时：**bun**（禁 npm／npx／pnpm／yarn）
- 框架：`vitepress@2.0.0-alpha.21`（npm `next` 现行最新预发布；npm 上不存在 2.0.0-beta.x）

## 数据分工（单一真值）

| 来源 | 供给 | 说明 |
| ---- | ---- | ---- |
| `../../SUMMARY.md` | **目录结构与侧边栏**（卷→章顺序、层级、号序） | GitBook 目录真值，用户指定“目录走 summary” |
| `../../data/outline.txt` | **显示真值**：四级题名、注文（组 2 257／有注小节 1 797）、卷导言、卷级定位注 | 装配器的内容源，题名含 `⟦en:X⟧` 语言标注 |
| `../../data/catalog.json` | DATA 段三视图（人物／文献／修订） | 与装配页 DATA 段同源 |
| `../../data/ui-strings.json` | 界面文案（书名、页面版本、指标标签） | 非正文文案真值 |
| `../../index.html` | **装配验证对照件**（不参与渲染、不部署） | `bun run verify` 的全量比对对象 |

`bun run verify` 的布尔判据＝**四数全等＋第五数（装配页“溯源标注”＝有注小节数，站内口径 1 797）＋号序逐位＋outline↔装配页 23 281 有序题名对逐位一致＋章题序列**；任一不符即失败并阻断构建。SUMMARY 只承担结构与号序判据，其**题名**与 outline 的漂移仅作 INFO 披露（站点显示取 outline，不受影响）——因为改题线会合法地让两者暂时不一致。注文口径：站内解析“注文组”2 257、“有注小节”1 797（＝装配页第五数），两数都披露。

## 命令

```bash
bun install          # 安装依赖（生成 bun.lock）
bun run sync         # 从 assets/doc.css 抽字体子集、复制 favicon → public/
bun run gen          # 由 outline.txt 生成 75 卷页 + 539 章页 → 站点根 vNN/（节号锚 {#_n-n}）
bun run verify       # 三源互证：SUMMARY ↔ outline ↔ 装配页 index.html
bun run docs:dev     # 本地开发（http://localhost:5173/librebsd/）
bun run build:vols   # 分卷构建再合并 → .vitepress/dist/（逐卷 6—8 s，全量约 10 分钟）
bun run docs:build   # sync + gen + build:vols（部署口径）
bun run build:vols --only 1-3  # 试点／排障：只构建壳页与指定卷
bun run docs:preview # 预览构建产物
```

## 目录角色

- `.vitepress/`：站点配置与主题（`theme/` 承载 `extends: DefaultTheme` ＋ 从 doc.css／modern.css 拆分的令牌 `catalog-tokens.css`）。
- `public/`：原样发布的静态件（`favicon.ico`、`fonts/lxgw-wenkai-screen-subset.woff2`），**生成件不入库**。
- `scripts/`：`lib/source.ts`（共享解析层）、`sync-assets.ts`、`gen-pages.ts`、`verify-assembly.ts`。
- `data/`：VitePress 构建期 data loaders（`book.data.ts`、`catalog.data.ts`），只在首页加载。

## 本批不做（留后续批）

谱系图（`bsd-family-tree.txt` 已不在库——`bcfe37828` 引入、`e75542ae6` 删除，无源数据可渲染；恢复须重新抓取，见 AGENTS.md 同行订正）、移动端抽屉（以响应式布局替代）、`noscript` 全量镜像（现为提示＋直链）、OG 位图（现为文本标签＋JSON-LD）、字体子集再生（只消费 doc.css 既存子集）。

## 已知限制

- `bun install` 偶报 `@docsearch/js` 单包 `ENOENT`（缓存复制失败）；本站不用 Algolia 搜索，构建不受影响。
- `SUMMARY.md` 的陈旧项已于 2026-11-19 用官方再生器 `sync_outline_mirror.py --write` 清零（`--check` 逐条双射 PASS，仅 1 行差异）；`sync_gitbook_summary.py` 在执行该行动时于现行文件上 `StopIteration`，但该器**已被规则明令停用**（`01-规则/大纲层级与目录规则.md` §27：“原 `sync_gitbook_summary.py`／`sync_chapter_keywords.py` 已停用，不适用于标准化树”），故不是缺陷、也不应据此改 SUMMARY——再生一律走 `sync_outline_mirror.py`。
- 首页目录树在展开卷／章时才渲染下层级，避免 19 363 节点全量入 DOM；侧边栏按卷分表（`/vNN/`），避免 539 条链接内联进每个页面。
- 功能面：字号五档（`FontScale.vue`，写入 `--cat-font-scale` 并持久化）、人物生卒时间线（DataPanel 第四个 tab）、打印／导出样式（`@media print` 隐藏导航与工具条）、`noscript` 提示＋卷页直链、OG 标签与 `schema.org/Book` JSON-LD（标题与四数取自数据源，缺 `shell.book_title` 直接抛错——书名单一真值，不设 fallback）。
- **分卷构建**（`scripts/build-by-volume.ts`）：逐卷独立构建再合并。VitePress 的临时目录固定为 `<root>/.vitepress/.temp`，同根并行会互删中间件（实测 `ENOENT … .temp/v01_c10.md.js`），故顺序执行；隔离根并行的方案需每根自带 `node_modules`，机制成本高于收益，未采用。合并步整站再生 `hashmap.json`（各分片并集，缺项会断跨卷跳转）与 `sitemap.xml`（按合并后实际 HTML 全量重生成）。
- `lastUpdated` 关闭：per-page git 历史查询 × 614 页不可接受；页面版本串由 `ui-strings.json` 的 `shell.page_version` 提供（与装配页同源）。
