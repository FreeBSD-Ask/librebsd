# 自动化执行记忆 — usenet 行级挖掘（810b448d）

## 2026-09-14 20:24（首次执行，被用户中断）
批次未收口。完成 4 个 P0 段次的 dump；ng19_s6、ng21_s3 候选已产出并收紧至 `bad=0`；
ng12_s6 读手被用户中断；ng35_s5 未开读。

## 2026-09-14 21:20–22:1x（用户批准续做，收口 2 段）

**收口结果（全部硬性验收通过）**

| 段次 | 窗口 | 头数 | 候选 | 注册 | 入纲块 | 宿主 | CL-RM | changelog |
|---|---|---|---|---|---|---|---|---|
| ng19_s6 | 49442–49613 | 172 | 102（L4=47/L3=55） | 101 | 101（L4=46/L3=55） | 11 | 040014–040114 | id=1446 / eo=1437 |
| ng21_s3 | 76936–77335 | 400 | 199（L4=51/L3=148） | 188 | 188（L4=46/L3=142） | 13 | 040115–040302 | id=1447 / eo=1438 |

- 验收：check 0 不一致；register 反查 101/101、188/188，四表 join 同数；
  块脚本 dry→write→**幂等二跑 0 块**；supplement 追加 101/188，**二跑 append 0**；
  changelog **真幂等**（复跑 no-op）；门禁 `audit_evidence_level_labels.py` **PASS（错标 0，全库 34,442 块）**；
  入纲落地复验 `_verify_outline_landing.py` 两段均 PASS（未落地 0 / claim_id 不符 0 / 等级不符 0）。
- staging：`_staging_ng19_s6.md`、`_staging_ng21_s3.md` 各一行。
- list 19 由此 **全组读完转 CLOSED**（29/43）。

**未完成**：ng12_s6、ng35_s5 dump 已备，读手连续两次派发触发 `429 too many requests`（按铁律未重试）。

## 关键环境事实（每次接手必读）
- **子代理派发受 429 限制**：与并行会话争用配额。本会话 2 次派读手均 429，但**分组子代理 2 次均成功**——
  读手任务（读 1.6 万行）消耗远高于分组。429 后立即停派、登记、转做主会话串行工作（gen/check/register/块/记账）。
- **并行会话会整批提交**：本会话按 SOP 只 `git add` 未 commit，但工作树被并行会话以提交信息「1」整体提交
  （本批改动随之落库，非本会话提交）。判定落地须用 `git show HEAD:<path>` 或 `_verify_outline_landing.py` 复核。
- **小库 next_id 陈旧**：`usenet_newsgroups_plan.json` 只对大库（11/20/23/38/40/41/44）更新 next_id，
  小库（12/13/18/19/21/26/27/34/35）的 next_id 不可信；段次覆盖只能从 `evidence.anchor` 的 `ng<NN>_s<K>` 反推。
- 段窗口公式：`lo = id_lo + 400*(k-1)`，`hi = min(id_lo + 400*k - 1, id_hi)`（三处实测校验）。
- **list 34（sources.unix）dump 19.8MB / 657k 行**，必须走 digest 发行版级合并，不可派普通读手。
- 摘要 **20–80 汉字**是实际验收口径（已收口 spec 自检 `bad=0`），但 `_pipeline_check.py` 只拦 <15 字；
  读手极易超 80，必须在提示词内写明并附自检脚本；Git Bash 的 `awk length()` 按字节计数会误报，须用 Python `len()`。

## 本会话新增可复用脚本（`script/_db_row_mining/`）
- `_verify_cand_20260914b.py`：候选文件复验（编码/换行/字段/升序/等级/长度 20–80/禁用字符），读手自检用。
- `_extract_claimmap.py`：从 register 的 stdout 提取 `MAPJSON:` 行落盘为 claim_map.json
  （**register 不写文件，子代理常漏落盘，这是历史坑**）。
- `_mk_assign.py <anchor>`：生成分组用的 `review_logs/<anchor>_assign.txt`（仅 claim_map 内 pk + 摘要）。
- `_verify_outline_landing.py <anchor>...`：入纲落地复验（块是否落地 / claim_id 是否一致 / 等级是否与库真值一致）。
- `_coverage_by_segment.py` / `_coverage_baseline.py`：覆盖率基线重算（段次口径为准，max-pk 口径会高估）。

## 2026-09-14 22:2x – 09-15 00:1x（主理人授权自行 commit + 加快频次，收口 4 段）

| 段次 | 窗口 | 头数 | 候选 | 注册 | 块 | 宿主 | CL-RM | changelog | commit |
|---|---|---|---|---|---|---|---|---|---|
| ng12_s6 | 30287–30674 | 388 | 304 | 302 | 302（L4=112/L3=190） | 18 | 040691–040992 | id=1450 | `8ccd08944` +1517 |
| ng35_s5 | 139588–139987 | 400 | 389 | 389 | 389（L4=105/L3=284） | 15 | 041371–041759 | id=1453 | `208a7fb4f` +2354 |
| ng13_s5 | 32275–32674 | 400 | 264 | 264 | 264（L4=149/L3=115） | 20 | 042748–043011 | id=1456 | `61a20e110` +1328 |
| ng35_s6 | 139988–140387 | 400 | 299 | 299 | 299（L4=37/L3=262） | 15 | 043952–044250 | id=1460 | 被并行会话「？」抢先提交 `79ad99ad3`（已复核在 HEAD） |

- **list 12（comp.unix.admin）s6 收尾 → 全组满读**。
- 四段全部：check 0 不一致 / 反查 N/N / 四表 join N / 块二跑 0 / supplement 二跑 0 / changelog 真幂等 /
  门禁 PASS / `_verify_outline_landing.py` PASS。
- **ng35_s7（末段 314 头）读手被用户中断**，dump 已备、候选未产。list 35 仅余此段即可满读。

## 2026-09-15 00:05–01:00（本线再收 2 段；自动化已被取消）

| 段次 | 窗口 | 头数 | 候选 | 注册 | 块 | 宿主 | CL-RM | changelog | commit |
|---|---|---|---|---|---|---|---|---|---|
| ng35_s7 | 140388–140701 | 314 | 187 | 187 | 187（L4=48/L3=139） | 11 | 045083–045269 | id=1469 | `f0714a6ca` +955 |
| ng13_s7 | 33075–33474 | 400 | 279 | 279 | 279（L4=166/L3=113） | 17 | 045283–045561 | id=1473 | `bb882f9bc` +1438 |

- **list 35（std.unix，2714 头）七段读完，全组收官**。P0 仅余 list 13（s8–s13）与 list 34（s3–s5，digest 路径）。
- 两段全部通过：check 0 不一致 / 反查 N/N / 四表 join N / 块二跑 0 / supplement 二跑 0 /
  changelog 真幂等 / 门禁 PASS / `_verify_outline_landing.py` PASS。

## 🚫 自动化已全部取消（重要）

- 用户 00:05 对本会话说「批准自动化，按10分钟推进」；但并行会话于 **00:14 依用户指令「取消所有自动化任务」
  清空了全部自动化**，含我新建的「D（错峰 :05）」。本会话复核 `automation_update list` 返回 **`[]`**。
- **结论：不要再重建自动化**，改为会话内连续推进（与并行会话的现行做法一致）。
- **10 分钟粒度不可实现**（实测）：调度器仅支持 DAILY/HOURLY/WEEKLY/MONTHLY/YEARLY，`FREQ=MINUTELY` 被拒；
  `BYMINUTE` 被接受但**不生效**（nextRunAt = 创建时刻 +1 小时）。实际粒度由创建时刻的分钟决定。

## 下次执行
1. **优先 list 13 s8（33475–33874）**，其次 list 13 s9–s13；list 34 须走 digest 发行版级合并。
2. 先查 `evidence.anchor` 与 dump 现状避开并行会话在途段。
   **覆盖率主口径已改为 plan.json 的 `read_done` 求和**（并行会话已把 plan.json 升级为逐组精确台账）；
   `_coverage_by_segment.py` 因依赖 `remaining` 字段而失真，待同步。
3. register 撞 duckdb 文件锁须退避重试（间隔 8 秒），不可杀对方进程。
2. ng12_s6 / ng35_s5 的 dump 已备，直接重派读手（模板见本会话）。
3. 收口顺序：spec → `_fix_cand_chars.py` → gen → check → register → `_extract_claimmap.py`
   → `_mk_assign.py` → 分组子代理 → `_pipeline_blocks.py --write` → 二跑 → supplement → changelog
   → 门禁 → git add → staging → 更新 `_LONGTERM_PLAN.md`。

## 2026-09-14 23:26–09-15 00:1x（本会话：收口 3 段，全部硬性验收通过）

**批次选取**：先查 `evidence.anchor` + `review_logs/` 在途产物，**避开并行会话在途段**
（ng21_s7 于 23:26 出现 dump/forread/digest；ng35_s6 dump 在；ng44_s18 已 staging），
取 P0→P1 的**干净未开段**：ng13_s6、ng34_s3（未做）、ng22_s2、ng38_s13。

| 段次 | 窗口 | 头数 | 候选 | 注册 | 块 | 宿主 | CL-RM（实测） | changelog |
|---|---|---|---|---|---|---|---|---|
| ng13_s6 | 32675–33074 | 397 | 397（L4=169/L3=228） | 397 | 397 | 18 | 043012–043408 | id=1457 / eo=1448 |
| ng22_s2 | 79049–79448 | 398 | 398（L4=131/L3=267） | 398 | 398 | 20 | **043554–043951** | id=1458 / eo=1449 |
| ng38_s13 | 147514–147913 | 400 | 400（L4=107/L3=293） | 400 | 400 | 12 | 044251–044650 | id=1462 / eo=1453 |

**验收（三段全绿）**：spec 20–80 字 0 违规；对齐核验 MISS=0；gen/check 0 不一致；
register 反查 N/N 且四表 join N；块脚本 dry→write→**幂等二跑 0**；supplement 追加 N、**二跑 append 0**；
changelog **真幂等**；门禁 `audit_evidence_level_labels.py` **PASS**；`_verify_outline_landing.py` **PASS**；
git 仅路径限定 `add`（18/20/12 宿主），未 commit，暂存无 `SUMMARY.md`。

## 本会话关键新发现（已写入技能）

1. **U+FFFD 源库乱码**：`_pipeline_check.py` 报「异常字符」实为源存档缺陷（全库 dump 7,730 处），
   ng38_s13 的 pk 147612 FROM 即含之。已把 `_pipeline_gen.py` / `_pipeline_check.py` 头字段消毒
   扩展为「`|`→`/` + `U+FFFD`→`?`」（两侧各加 `_hdr()`，**必须同步改**）。
   安全性依据：register 以源库 `from_name` 覆盖 FROM，**不入 DB**。已对 3 个旧段回归复检仍 0。
2. **CL-RM 区间禁止推断**：ng22_s2 实测 `043554~043951`，而非按 ng13_s6 末号推断的 `043409~`——
   并行会话在中间插了 145 条。staging 初稿曾写错，已修正。**必须从 MAPJSON 取 min/max**。
3. **覆盖率口径改版**：`usenet_newsgroups_plan.json` 已升级为逐组精确台账（含散点旧批），
   主口径＝`sum(read_done)`＝**94,769 / 234,573 = 40.40%**（含本会话 ng38_s13 的 400 头；
   并行会话 23:57 重算得 94,369 / 40.23%，未含该段）；满读组 **22 / 43**。
   **`_coverage_by_segment.py` 已失真**（依赖 plan.json 的 `remaining`，改版后漏判：实测 32.08% / 100% 组 28），待同步。

## 本会话新增可复用脚本（`script/_db_row_mining/`）

- `_mk_forread.py <lid> <lo> <hi> <anchor> [fr] [dg]`：一次产 forread（1200 字）+ digest（400 字），
  内置 `sort(key=int(pk))` + 严格递增 assert + 越窗 assert。
- `_align_check.py <dump> <cand>`：通用对齐核验器，**以 dump 全文为判据**，带泛词白名单，输出 MISS/WEAK。
- 每段导 `_ngNN_sK_hosts.txt` 供 `git add -- $(cat ...)`。

## 下次执行

1. 先跑主口径基线（`sum(read_done)`，勿再用 `_coverage_by_segment.py` 的百分比）并查 `evidence.anchor`
   避开并行会话在途段（当前在途：ng21_s7 轮3、ng35_s6/s7）。
2. **P0 余**：ng35_s7（140388–140701，314 头，收官段）、ng34_s3–s5（**digest 发行版级合并，勿派普通读手**）、
   ng13_s7–s13（7 段）。**P1 余**：ng38_s14+、ng22_s3+、ng41_s12、ng15_s1（未开工）。
3. 三次子代理派发（读手/分组）本会话**全部一次成功无 429**，模板见技能「派发子代理的实测模板要点」。
