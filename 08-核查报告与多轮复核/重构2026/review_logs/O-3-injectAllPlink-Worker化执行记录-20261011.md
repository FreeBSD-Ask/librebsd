# O-3 承载层：injectAllPlink 正则匹配 offload 到 Blob Worker 执行记录（2026-10-11）

> 缘起：《主理人批准登记-全部遗留项-20261011》O-3 批准执行项——
> setupToc／injectAllPlink 拆“Worker 预计算＋主线程套用”，消减主线程长任务阻塞。
> 性质：承载层运行时优化（零内容层、零结构层），改 doc.js＋page.template.html CSP。
> **本批含一次修正**（异步化破坏 ready 语义 → 门控修复），全过程见 §三；最终产物版本 2026.10.11-11:50。

## 一、基线实测（改造前）

用 Playwright 拦截 `document.documentElement.setAttribute('data-opt-ready', ...)` 精确测量：
- `data-opt-ready=1` 设置时刻（performance.now，5 次重载平均）：**≈ 1,780 ms**
- `loadEventEnd`（导航完成）：**≈ 225 ms**
- `__waitStable(300, ...)` 等待：**300 ms**
- 实际主线程初始化工作（setupToc＋injectAllPlink＋图谱＋搜索＋自校验等）：**≈ 1,255 ms**

其中 `injectAllPlink` 的正则匹配（TreeWalker 遍历 3,468 节文本节点 × 候选人名正则替换）为主要 CPU 瓶颈，适合 offload 到 Worker。

## 二、改动面（3 件，均已 prebak-o3-20261011 备份）

| # | 文件 | 改动点 |
| - | ---- | ------ |
| 1 | `assets/page.template.html` | CSP 加 `worker-src blob:`（允许 Blob Worker；原 CSP 无 worker-src 指令，Blob URL 会被拦截） |
| 2 | `assets/doc.js` | `injectAllPlink` 重构为 Blob Worker 异步版：①主线程 TreeWalker 收集 `ul.sections > li` 内文本节点，提取文本数组；②`postMessage` 给 Worker（texts＋firstCharIdx＋nmOrder）；③Worker 内做候选筛选＋正则替换，返回每节点 HTML＋nPlink 计数；④主线程接收后做 DOM 替换＋plink 点击事件绑定＋`__LB.nPlink` 赋值；⑤Worker 不可用或 `onerror` 时回退原同步逻辑（`injectAllPlinkSync`），保证功能不退化 |
| 3 | `data/ui-strings.json` | 页面版本 `2026.10.11-10:28` → `2026.10.11-11:16`（初版）→ `11:37`（门控修正）→ **`11:50`（字体子集重建后终版）** |
| 4 | `assets/doc.css` | 字体子集重建（§3.4）：692,510→**692,350 B**，含新增“阻”码位；产物可由 `font_subset_rebuild.py` 从现行 index.html＋字体源确定性再生（同日更早备份 `*.prebak-font58c-20261011` 在盘） |

### 设计要点

1. **Worker 代码内联为字符串数组**（`__plinkWorkerCode`），运行时 `new Blob([...], {type:'application/javascript'})` ＋ `URL.createObjectURL` 创建，不依赖外部 JS 文件（保持单体性）。
2. **语义等价**：Worker 内的候选筛选、排序（长度降序＋nmOrder）、正则构造（中文锚点前后不加边界、英文加 `(?![CJK A-Za-z0-9])`）、900 上限 break、既有 `<a>` 占位还原——全部与原同步逻辑逐行对应。
3. **异步化影响面最小**：仅 plink 点击事件绑定与 `__LB.nPlink` 赋值移入 `.then()` 回调；后续图谱、搜索、自校验等不依赖 plink，继续同步执行。
4. **回退三重保障**：`typeof Worker === 'undefined'` 检测、`new Worker()` try/catch、`worker.onerror` 回调——任一失败均走 `injectAllPlinkSync`。

## 三、性能收益与修正过程（改造后）

### 3.1 初版实测（无门控，语义有缺陷）

Playwright 5 次重载平均：
- `data-opt-ready=1`：**≈ 1,013 ms**（基线 1,780 ms，− 43%）
- 实际主线程初始化工作：**≈ 443 ms**（基线 1,255 ms，− 65%）

但此版 `data-opt-ready=1` 不再蕴含“plink 注入已完成”（Worker 异步未门控），**语义已破坏**——见 3.2。

### 3.2 修正：full_matrix 3 项失败与门控修复

- **发现**：三套件全量复跑时 `full_matrix_regression.mjs` 报 **FAILED=3**——412x915 视口三主题（light／dark／sys）100% 缩放下“人名浮层挂载”读到 `plink=0`（基线 449）。
- **实证**：专项竞态探针（`script/_o3_race_probe_20261011.mjs`，独立 context 冷载）——`data-opt-ready=1` 时 `plink=0`，+800 ms 后 `plink=449`。**ready 早于 plink 套用，竞态坐实**；140% 缩放组合此前“通过”系缓存热时序侥幸，非真通过。
- **修复**（doc.js 两处）：
  1. `injectAllPlink().then(...)` 提升为 `var __plinkDone = injectAllPlink().then(...)`（var 提升至 `__dataReady` 回调作用域）；
  2. 尾部 `__LB.decorateDialogs(); __waitStable(300, …)` 包进 `(__plinkDone || Promise.resolve()).then(...)`——**ready=1 的语义恢复为“plink 注入亦已完成”**（与基线同步版一致；try 块若提前抛出则 `__plinkDone` 为 undefined、走 `Promise.resolve()` 兜底等同原行为）。
- **修复验证**：竞态探针复跑——两项 `at-ready plink=449`；`full_matrix` **628/628 FAILED=0**。

### 3.3 最终 A/B 实测（同装配产物，Worker 路径 vs 强制同步回退）

`script/_o3_ab_probe_20261011.mjs`：A＝正常（Worker 路径）；B＝`window.Worker=undefined` 强制走 `injectAllPlinkSync` 回退（同页冷载 2 轮各测）：

| 指标（冷载） | A Worker 路径 | B 同步回退 | 对比 |
| ------------ | ------------- | ---------- | ---- |
| 主线程长任务总量 | ≈ 1,465 ms | ≈ 2,275 ms | **− 36%（约 −810 ms）** |
| 单次最长阻塞块 | 774／938 ms（首屏装配块） | 885／893 ms（plink 同步块） | plink 的 ~885 ms 连续阻塞**消解**，主线程套用仅 ~75–80 ms |
| `data-opt-ready=1` 时点 | ≈ 3,238 ms | ≈ 3,092 ms | **+ 146 ms**（冷载）／温载 1,780→1,870 ms（+90 ms） |

结论：**以就绪时点约 +5% 为代价，换取主线程在 plink 阶段少阻塞约 810 ms**（该窗口内页面可响应滚动／输入）；语义与功能与基线完全等价（plink=449、事件绑定、`__LB.nPlink` 断言点全同）。

### 3.4 字体子集连带（第九件 B3）

- O-3 新增注释引入页面新字符“阻”（“阻塞”），第九件 B3 报**回归缺字 3**：直角引号两枚（U+300C／U+300D，系本批修正注释误用，违写作规则）＋“阻”。
- 处置：①doc.js 注释的直角引号归一为弯引号“”（直角引号清零）；②`font_subset_rebuild.py` 重建（页面 2,070 字／源 13,889 字／子集 481.4 KB）→ doc.css 692,510→692,350 B → 重装配；复跑第九件 **PASS**（缺 57 全属源本无、允许）。

## 四、门禁与验证（最终态：版本 2026.10.11-11:50／页面 2,706,779 B）

| 项 | 结果 |
| -- | ---- |
| 07 装配结构（第八件） | **PASS**——67 卷 483 章 3468 节，口径六处一致，标签平衡，锚点 4047 无重复；`--check` 零漂移 |
| 09 数据完整性（第九件 D2） | **PASS**——data blob SRI 自洽（blob 338,208 B） |
| 第九件页面资产层 | **PASS**——B3 回归缺字 0（重建后）；A–E 全 PASS，INFO 1（缺 57 源本无） |
| 10 md lint | **PASS**——闸面 82 文件 0 问题 |
| 12 门禁登记（第十六件） | **PASS**——R1–R7，FAIL 0 |
| 13 夹具新鲜度 | **PASS**——合计 4 项 FAIL 0（豁免项照常断言“仍需要豁免”） |
| 18 版本号（第十八件） | **PASS**——口径 67/483/3468、注 1262、版本 2026.10.11-11:50 |
| 19 锚点解析（第十九件） | **PASS**——解析率 97%（4 处悬空为历史登记项，非本批引入） |
| 浏览器回归（四套） | **全绿**——`visual_regression` **23/23**；`full_matrix_regression` **628/628**（36 组合；修正前 FAILED=3 已修复）；`fullsize_regression` **27/27**；探针 `_probe_triple.mjs` 口径串 ✓（67 卷 483 章 3468 节） |
| 竞态／A/B 探针 | `_o3_race_probe_20261011.mjs`：`at-ready plink=449`（修复后）；`_o3_ab_probe_20261011.mjs`：长任务总量 −36% |

## 五、未跑项与理由

- **OAA 内容层审计未跑**：O-3 仅改运行时脚本（doc.js）与 CSP，不改大纲内容源（outline.txt）与邮件素材，OAA 审计针对内容层，与本次改动面无交集。
- **台账／快照／十维未重算**：本批不改 outline.txt 与任何内容源，台账/快照/十维无变动面。
- **十二维度量与前批持平**：页面级指标（体积 2,706,779 B，较批前基线 2,703,104 B ＋3,675 B）为承载层优化取舍，非内容层变动。

## 六、落账

- changelog **id=2352**（entry_order=2046，date=2026-10-11）——含修正补记。
- 92 号文 §十一 施工进度对账表顶插一行（O-3 行，含修正摘要）。
- 4 件 prebak 备份保留（3 件 `*.prebak-o3-20261011`＋1 件 `doc.js.prebak-o3fix-20261011`），不清理。
- 探针脚本保留于 `script/`（`_o3_perf_probe`／`_o3_race_probe`／`_o3_ab_probe`／`_o3_prebak`／`_o3_changelog_insert`，均 20261011 前缀）。

*编制：WorkBuddy，2026-10-11。*
