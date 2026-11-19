# ADR-0021：目录页部署采用 VitePress，数据源直读原生实现，装配产物作验证对照件

- **状态**：已接受（2026-11-19 同日经 ykla 修订令由“装配产物直出”改定，修订过程见附表方案 E）
- **日期**：2026-11-19
- **裁决人**：ykla
- **执行者**：主代理
- **复审日期**：2027-02-19
- **替代关系**：无

## 1. 形式

- 形式：在 `05-卷册大纲/目录/vitepress/` 建独立 VitePress 站点（`public/` 与 `.vitepress/` 两目录分离）。站点**原生实现目录页功能**：数据层用 VitePress data loaders 构建期直读内容源 `data/outline.txt`（四级题名树＋注文＋卷注）与 `data/catalog.json`（人物／文献／修订 DATA 段）、文案层直读 `data/ui-strings.json`；主题令牌（light／oled／eink＋LXGW WenKai 字族）拆分自 doc.css／modern.css 并适配 `extends: DefaultTheme`；首页即目录浏览应用。装配产物 `index.html` 仅作**构建期装配验证对照件**——`bun run verify` 有序（节号，题名）对全量比对＋章题序列比对＋doc-metrics 口径数比对，不随站点部署。部署走 `.github/workflows/deploy-vitepress-pages.yml`（actions 三件套＋SHA 钉定）到 GitHub Pages 项目页 `https://freebsd-ask.github.io/librebsd/`（base `/librebsd/`）。
- 构建：**分卷构建再合并**（ykla 2026-11-19 令）。`scripts/build-by-volume.ts` 逐卷（1—12 页／卷，实测 6—8 s）独立构建，产物按路径合并进 `.vitepress/dist`；理由＝单进程 614 页一次构建 Wall time 与内存不可控、失败即全废；VitePress 临时目录固定于 `<root>/.vitepress/.temp`，同根并行会互删中间件（实测 `ENOENT … .temp/v01_c10.md.js`），故顺序执行。合并步整站再生两件派生文件：`hashmap.json`（客户端路由按源路径查页数据，取各分片并集，缺项会断跨卷跳转）、`sitemap.xml`（按合并后实际 HTML 全量重生成，分片自产的只覆盖自身）。`lastUpdated` 关闭：per-page git 历史查询 × 614 页不可接受，页面版本串改由 `ui-strings.json` 的 `shell.page_version` 提供（与装配页同源）。
- 边界：装配源（`index.html`、`assets/`、`data/`、`src/`、装配器与门禁）零改动；本批功能面不含导出／时间线／谱系图／字号档位／移动抽屉／noscript 全量镜像（留后续批，见 spec v2 §1 ③）。

## 2. 矛盾

- 不做的后果：目录页只能经本地 `serve_refactor2026.py`（8090 端口）预览，无公网只读入口；协作与审阅依赖本机在网。
- 受影响者：ykla（审阅与分享）；外部协作读者（无法在线核对大纲结构）。

## 3. 正面

- 能力：目录页获得公网静态托管；数据自内容源（outline.txt）原生渲染，装配批次 push 后 verify→build→deploy 自动链路；VitePress 主题基座（`extends: DefaultTheme`＋拆分令牌）为后续扩展（说明页、检索增强）预留。
- 受益者：ykla 与所有读者；后续工程批直接复用站点骨架与数据加载层。
- 验证方式：`bun run verify` exit 0（有序题名对全量一致＋口径四数一致）；`docs:build`／`docs:preview` 实测；工作流 SHA 钉定审读。

## 4. 负面

- 成本：数据层形成 outline.txt 的第二消费端（装配器之外）——由验证器把两端锁进同一判据；CI 每次约 10—14 分钟（76 分片顺序构建，实测全量约 9—12 分钟）。
- 风险：vitepress 2.0.0-alpha 预发布线 API 变动；data loader dev watch 跨 srcDir 相对路径的 HMR 行为；样式层与装配页可能漂移（验证器只锁题名与口径，不锁样式）。
- 边界：不承担正文发布（正文批仍受红线 1 约束）；不承担装配正确性（由既有九件门禁负责）。

## 5. 承担者

| 负面 | 承担者 | 承担时点 |
| ---- | ------ | -------- |
| 第二消费端与装配页的漂移监控 | 主代理 | 每批 `bun run verify`（CI 与本地） |
| alpha 版升级适配 | 主代理 | vitepress 升级批次 |
| Pages 开关与首推 | ykla | 仓库 Settings→Pages→Source 选 GitHub Actions 后首次部署 |

## 6. 过去依据

- 历史条件：目录页以单文件自包含为架构前提（第九件自包含性门禁），此前仅本地静态服务预览。
- 此前形式为何失效：无既有部署形式；本地服务无公网暴露、无自动化发布链，不满足“部署到 GitHub Pages”的目标。

## 7. 现在依据

- 测试／测量／故障／反馈：outline.txt 实测解析 75 卷／539 章／3 918 节／19 363 小节＋1 797 条节级注文＋75 条卷导言＋71 条卷级定位注（2026-11-19）；catalog.json＝DATA 段（人物 2 269／文献 5 605／修订 38）；字体子集单文件约 569 KB（含于 doc.css）；bun 1.4.4＋node v26.13.0 在机；vitepress npm `next`＝2.0.0-alpha.21（无任何 2.0.0-beta.x，用户所称“beta20”经查为记忆偏差，按“最新预发布”取值并披露）。
- 日期与环境：2026-11-19，Windows 10.0.26300，Git Bash。
- 证据路径：`.trae/specs/vitepress-pages-deploy-20261119/spec.md` §0（v2 修订记录）与 §2（标准文献四问）；`script/_bakref_freebsdask_config.mts`（参照件）；本批执行记录（README 收口段）。

## 8. 将来失效条件

- 条件一：outline.txt 内容源口径变更（如层级或注文语法改形）——解析器与验证器需同步改形。
- 条件二：仓库迁离 FreeBSD-Ask/librebsd 或改用用户根域——base 与 sitemap.hostname 需重定。

## 9. 0 信任校验

- 独立复现方式：`bun run verify` 任何人可复跑——以装配产物为对照件全量比对题名序列与口径数；站点渲染与装配页可并排目验。
- 交叉验证工具：验证器（bun）＋装配器自检（assemble_index.py --check）双链；门禁批（常备五件＋涉面）。
- 原始证据位置：本批执行记录（`05-卷册大纲/目录/vitepress/README.md` 收口段）与任务审计台账行。

## 10. 自由影响

- 退出：删除 `vitepress/` 目录与工作流文件即完全退出，装配源与站点零耦合、无迁移残留。
- 导出：`dist/` 为纯静态目录，可任意镜像托管（不限 GitHub Pages）。
- 离线：构建不依赖网络（bun install 除外）；站点运行时零外部请求。
- 默认值可撤销性：base／sitemap.hostname 集中在 config.mts 顶部常量，单点改回 `/` 即用户根域形态。

## 11. 安全和解

- 资产：目录页数据（公开书稿大纲）与站点配置。
- 对手：静态托管场景下无特权目标；主要暴露面为 CI（actions 供应链）。
- 攻击面：第三方 action——以 40 位 SHA 钉定（与 ci.yml 同口径）收敛；Pages 部署令牌作用域限于 github-pages environment。
- 信任边界：CI 只读仓库内容＋产 artifact；无 secrets 注入（deploy-pages 用 OIDC id-token）。
- 现有控制：paths 过滤限触发面；无缓存 action（减小投毒面）；构建脚本只读装配源。
- 残余风险：action SHA 自身被上游 force-push 覆盖（理论面）；接受。
- 证据：ci.yml 既有钉定先例；本工作流五 action 逐行 SHA＋版本注释。
- 代价：升级 action 需手动换 SHA（dependabot.yml github-actions 生态可提 PR）。
- 失效条件：GitHub Pages 政策变更（如强制构建器）→ 回流本 ADR。

## 12. 复审触发

- 时间：2027-02-19。
- 事件：vitepress 脱离 alpha（beta／stable）发布、outline.txt 语法口径变更、仓库迁移、后续批补功能面（导出／时间线等）开工。
- 复审动作：重跑 verify 与双通道构建；核对 data loader 语义；按需更新 base 与钉定版本。

## 附：替代方案与取舍

| 方案 | 正面 | 负面 | 为何未选 |
| ---- | ---- | ---- | -------- |
| A. 装配产物 iframe／重定向包装进 VitePress 首页 | 保留 VitePress 首页壳 | 首页非目录页本体；8.4 MB iframe 体验差 | 违背“index.html 作为首页”的字面目标 |
| B. 装配产物直出（v1 初案：dev 中间件＋buildEnd 复制装配 index.html） | 零实现成本、与装配页逐字节一致 | 首页非 VitePress 原生功能实现；站点层形同虚设 | **ykla 2026-11-19 修订令**：“不要直接复制既有 index.html，那只用来验证装配。要进行主题适配实现其功能。”——改为验证器（本 ADR 现行形式） |
| C. 装配产物入 `public/` 直接当静态根，不用 VitePress | 最简 | 无 VitePress 基座，后续扩展需另起炉灶 | 不符用户“结合 vitepress”要求 |
| D. 站点建在仓库根（`.vitepress/` 于根） | 路径最短 | 根目录禁新建路径（红线 8）；装配目录与站点混放，门禁面污染 | 站点下沉到目录页子目录 |
