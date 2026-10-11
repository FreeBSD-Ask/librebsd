# View Transitions 执行记录（2026-10-11）

> 缘起：《主理人批准登记-全部遗留项-20261011》A2 按序施工＋主理人令（执行排序：View Transitions → CSP/TT → Popover → Highlight → 自定义元素）；本批＝第三批。
> 性质：承载层视觉增强（零内容层、零结构层）；规格 P1-10。
> 终版：版本 2026.10.11-15:59／页面 2,709,883 B。

## 一、改动面（3 件，prebak 1 件保留）

| # | 文件 | 改动点 |
| - | ---- | ------ |
| 1 | `assets/doc.js` | ①`__LB` 新增 `viewTransition(fn)`：`document.startViewTransition` 存在且非 `prefers-reduced-motion` → 原生交叉淡入；否则**同步执行**（零副作用降级；try/catch 兜底）；②主题切换 `apply(next)`、研/阅切换 `applyMode(n)` 两处点击包进该帮手；`localStorage` 写入留回调外（存储即时生效，不随动画延迟） |
| 2 | `tests/full_matrix_regression.mjs` | 研/阅断言补 150ms 等待——VT 回调异步落地，原同步读 className 将恒 false；判据语义不变＝“点击后类翻转”（夹具同步纪律内） |
| 3 | `data/ui-strings.json` | 版本 15:43→15:59 |

## 二、专项探针（`script/_vt_probe_20261011.mjs`，全绿）

| 场景 | 结果 |
| ---- | ---- |
| 正常路径 | `vtCalled=2`（主题＋研阅均经 startViewTransition）；`data-theme` light→dark 翻转 ✓；`read-mode` 翻转 ✓ |
| reduced-motion（Playwright `reducedMotion:'reduce'` 模拟） | `vtCalled=0`（正确绕过）＋**同步翻转** ✓——降级路径实测 |

## 三、门禁与回归（全绿）

- 门禁：07 装配零漂移｜09 数据完整性 0 处｜13 夹具新鲜度 FAIL 0｜10 md lint 0 问题｜12 门禁登记 FAIL 0｜18 版本号 PASS（15:59）。
- 浏览器四套：visual **23/23**｜full_matrix **628/628**（36 组合含研阅切换新时序）｜fullsize **27/27**｜探针口径 ✓。

## 四、登记不改（最小面裁定）

1. **图谱面板开启未包 VT**：dialog `showModal` 顶层动画为独立体系，包入将干扰 T7 回归截图时序——维持最小面。
2. **逐元素 `view-transition-name`**（指标卡／章题命名形变）：根级交叉淡入已覆盖规格意图；逐元素属后续可选增强，登记不阻塞。

## 五、留痕与落账

- prebak 1 件（`doc.js.prebak-vt-20261011`）；探针 `script/_vt_probe_20261011.mjs` 保留。
- 未跑：OAA 内容层审计（零内容源改动）；台账／快照／十维（不改 outline.txt）。
- changelog **id=2355**（entry_order=2049）；92 号文 §十一 顶插一行；《11 项缓办评估与施工序登记》第三批回写。
- 产物：2,709,295→**2,709,883 B**（+588 B），版本 15:43→**15:59**。

*编制：WorkBuddy，2026-10-11。*
