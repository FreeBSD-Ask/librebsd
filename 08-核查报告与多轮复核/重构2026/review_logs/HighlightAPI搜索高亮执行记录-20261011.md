# Highlight API 搜索高亮执行记录（2026-10-11）

> 缘起：《主理人批准登记-全部遗留项-20261011》A2 按序施工＋主理人令（排序第六批：Highlight API 搜索）。
> 性质：承载层**新增能力**（规格 P0-3；现行检索为结果列表式、无页内高亮——本批补命中文本页内高亮，非优化替换）。
> 终版：版本 2026.10.11-16:34／页面 2,716,733 B。

## 一、改动面（3 件，prebak 2 件保留）

| # | 文件 | 改动点 |
| - | ---- | ------ |
| 1 | `assets/doc.js` | `runSearch` 收集命中节 id → `applySearchHighlight`：对命中节文本节点建 `Range`（TreeWalker，拒绝 `.note-badge/.t-more/.t-short/.sec-num/button` 控件文本），`CSS.highlights.set('search-hit', Reflect.construct(Highlight, ranges))`；上限 800 Range；**清空 query 或面板 close（dialog close 事件——Esc／遮罩统一走此）即 `CSS.highlights.delete`**；能力四重检测（`Highlight` 构造器／`CSS.highlights.set`／`::highlight()` 选择器支持），不支持引擎回退＝现状 |
| 2 | `assets/modern.css` | `@supports selector(::highlight(search-hit))` 守卫；`::highlight(search-hit)` accent 26% 底色（主题令牌 `color-mix`） |
| 3 | `data/ui-strings.json` ＋ 字体 | 版本 16:17→16:34；字体重建（注释新字符），B3 回归缺字 0 |

## 二、语义登记

- **exact 形态才定位**：loose（去空格）命中的节仅入结果列表、正文不高亮——与列表判定口径一致且诚实。
- **零 DOM 变更**：纯绘制层（Range＋::highlight），不插 `<mark>`、不改文本节点——导出／净化器／断言面零污染。
- **Firefox 回退＝现状**（无页内高亮），结果列表功能不变。

## 三、专项探针（`script/_hl_probe_20261011.mjs`，全绿）

| 项 | 结果 |
| -- | ---- |
| 输入 “unix” | 注册 size=1；**238 个 Range**；样例文本 'UNIX'；`<mark>` 注入 **0** |
| 清空 query | size 0 |
| Esc 关面板 | size 1→0，面板关闭 |
| 导出保真 | `exportSummaryText()` 逐字不变（202,792 → 202,792 字节） |

## 四、门禁与回归（全绿）

- 门禁：07 装配零漂移｜09 数据完整性 0 处｜第九件 PASS（B3 缺字 0）｜10 md lint 0 问题｜12 门禁登记 FAIL 0｜13 夹具新鲜度 FAIL 0｜18 版本号 PASS（16:34）。
- 浏览器四套：visual **23/23**｜full_matrix **628/628**｜fullsize **27/27**｜探针口径 ✓。

## 五、落账

- changelog **id=2358**（entry_order=2052）。
- 92 号文 §十一 顶插一行；《11 项缓办评估与施工序登记》第六批回写。
- prebak 2 件（`*.prebak-hl-20261011`）＋探针 `script/_hl_probe_20261011.mjs` 保留。
- 产物：2,713,281→**2,716,733 B**（+3,452 B），版本 16:17→**16:34**。

*编制：WorkBuddy，2026-10-11。*
