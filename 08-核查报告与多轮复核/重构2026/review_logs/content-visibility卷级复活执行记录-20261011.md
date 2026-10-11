# content-visibility 卷级复活执行记录（2026-10-11）

> 缘起：《主理人批准登记-全部遗留项-20261011》A2——“11 项缓办并入 A1 同序列，按序施工”＋主理人令“继续处理下一批候选：content-visibility”（施工序第一优先件）。
> 性质：承载层运行时渲染优化（零内容层、零结构层）；改 `assets/modern.css`＋`assets/doc.js`（唯一产物 index.html 由装配器重装）。
> 终版：版本 2026.10.11-14:44／页面 2,707,782 B。

## 一、历史沿革与前置调查（先考古后动工）

| 时点 | 事实 |
| ---- | ---- |
| 2026-09-12 | 规格《网页技术现代化建议-20260912》P0-1：`.doc-block` 加 `content-visibility:auto; contain-intrinsic-size: auto 800px`（“1749 节页面最大的单项性能杠杆”） |
| 2026-09-13 | c-v 三根因查明：跳过态子树 offsetTop 不可靠；需 rebuildOffsets／j-k／抽屉点击三处联动，两处先行改造；规格原文入 changelog file_archive |
| 2026-09-16 | 首次实施（changelog id=1691：ready ~3s→~1.3s），后撤除（撤除时点 09-18 四层解耦与 09-19 之间；无独立撤除记录） |
| 2026-09-19 | P0 微优化 A/B 负结果全回滚＋“性能线关闭”（id=2048／2049；当时判据噪声带 ±850ms→后收紧 ±75ms） |
| 2026-10-11 | 主理人批准 11 项按序施工；本批次为第一件。doc.js 预留加固（“现态 no-op，为 c-v 复活预留”）与 j/k 改 scrollIntoView 均已在位 |

前置判定：预留加固系**零占位原型**遗留（`height < 40` 条件在有 intrinsic-size 时恒不命中）——复活必须同时改写该条件，否则量测在占位空间进行、offsets 失真。本批据此设计。

## 二、设计（含原型筛选）

**终设计（B1 系）**：
1. `modern.css`：`@supports (content-visibility: auto) { .doc-block { content-visibility: auto; contain-intrinsic-size: auto 2300px; } }`——2300px＝67 卷实测高中位（min 872／max 6,893／mean 2,648）；不支持特性即整块不生效（渐进增强）。
2. `doc.js rebuildOffsets`：量测前把**全部** c-v 卷临时置 `visible`（原 `<40` 条件废除）→ 量测 offsets（真实拓扑）→ 按实测高**逐卷**改写 `contain-intrinsic-size`（`auto <h>px`）→ 复原 `auto`。关键性质：**占位空间＝真实空间**——滚高零漂移、offsets 恒准、深链／TOC 高亮／进度条／夹具绝对位点全一致。

**原型筛选（交错 A/B、N=10、Performance.getMetrics 事件计数；先 A vs A 自检噪声带）**：
- A vs A（N=6）：LayoutMs ±2.8%｜LTsum ±0.1%｜LTmax ±12%｜ready ±1% → 装置可信。
- B1（恢复量测＋精确 intrinsic）vs B2（纯占位不恢复）：**B1 全指标更优**（B2 因占位高度失真引发滚高不稳与布局抖动：LayoutMs 933 vs 837、ready 3060 vs 2818）→ 占位优于零占位的直觉不成立，精确尺寸本身即收益。
- B1b（源级忠实版，直接把改动写进变体内 rebuildOffsets）≈ B1 → 定稿。

## 三、生产终测（pre vs post 同源逆补丁对测，N=10 交错，中位）

| 指标 | pre | post | Δ |
| ---- | --- | ---- | -- |
| readyMs | 3,651 | 3,121 | **−14.5%** |
| LayoutMs（冷载布局） | 1,536 | 858 | **−44.1%** |
| TaskMs（主线程任务） | 2,081 | 1,550 | **−25.5%** |
| 长任务合计 | 1,759 | 1,419 | **−19.3%** |
| 单次最长长任务 | 848 | 641 | **−24.4%** |
| RecalcMs | 52 | 357 | +586%（c-v 切换与尺寸写入的样式重算；净含于 TaskMs 之 −25.5% 内） |
| JS 堆 | 5.7 MB | 7.8 MB | +36.8% |
| 滚动相 LayoutMs（5 段滚动） | 83 | 95 | +12 ms（+14.5%） |

**诚实登记**：净收益集中于冷载（布局 −44%、就绪 −15%）；代价为样式重算与内存上升、滚动相 +12ms（绝对值极小）。本批为 2026-09-19“性能线关闭”后首个**以可信基准测出显著效应**的性能改动（c-v 属结构性而非微优化，事件计数与时长双口径一致）。

## 四、验证（全链）

| 项 | 结果 |
| -- | ---- |
| 门禁（8 项） | 07 装配零漂移｜09 数据完整性 0 处｜第九件 B3 回归缺字 0（**无需字体重建**）｜10 md lint 0 问题｜12 门禁登记 FAIL 0｜13 夹具新鲜度 FAIL 0｜18 版本号 PASS（14:44）｜19 锚点解析 97% |
| 浏览器四套 | visual **23/23**｜full_matrix **628/628**｜fullsize **27/27**｜探针口径 ✓（67 卷 483 章 3468 节）——均 FAILED=0 |
| 专项探针 | 67/67 卷 c-v 生效＋intrinsic 逐卷写实（样例 vol-1 `auto 2542px`）；滚高 180,467px（pre 180,369，**Δ+0.05%**）；plink=449（O-3 等价）；深链 `#vol-30-ch-5` 落点 top=131px（远卷跳过态正确跳转）；注展开 35→59px 正常 |
| 三引擎冒烟 | Chromium 全绿；Firefox／WebKit 可执行文件**本机未装**（环境所限未跑）——75 号文 §71 已实测三引擎均支持 `content-visibility`，且 `@supports` 守卫保证不支持时整块不生效 |
| 装置脚本 | `_cv_bench`／`_cv_height_probe`／`_cv_build_proto`／`_cv_build_b1b`／`_cv_build_pre`／`_cv_sanity_probe`／`_cv_xengine`／`_cv_find_spec` 等（`_cv_` 前缀 8 件＋早前 5 件，保留不清理） |

## 五、留痕与残余

- prebak 2 件：`doc.js.prebak-cv-20261011`、`modern.css.prebak-cv-20261011`（保留不清理）。
- 原型件 4 件：`script/_cv_proto/`（index_b1／b2／b1b／pre.html，保留）。
- 残余（登记不改）：①字号滑杆拖动时 offsets 与 intrinsic 同为旧值（**既有缺陷同族**——滑杆不改 mark offsetsDirty；缩放在 resize 路径上已由 onLayoutChange 重测覆盖）；②滚动相 +12ms；③JS 堆 +36.8%——三项均登记，不在本批扩改。
- 未跑项：OAA 内容层审计（零内容源改动，无交集）；台账／快照／十维（不改 outline.txt，无变动面）。

## 六、落账

- changelog **id=2353**（entry_order=2047，date=2026-10-11）。
- 92 号文 §十一 顶插一行；《11 项缓办评估与施工序登记》更新第一批状态。
- 产物：2,706,779→**2,707,782 B**（+1,003 B），版本 11:50→**14:44**。

*编制：WorkBuddy，2026-10-11。*