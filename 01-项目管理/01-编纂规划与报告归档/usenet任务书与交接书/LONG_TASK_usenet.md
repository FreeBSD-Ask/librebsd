# 长任务书 · usenet 全库行级史料挖掘

| 项 | 值 |
|---|---|
| 任务名 | usenet 全库行级史料挖掘（43 个新闻组） |
| 建立时间 | 2026-09-14 |
| 机读状态 | `script/_db_row_mining/long_task_state.json`（唯一权威，每轮末刷新） |
| 总规模 | **234,573 头** |
| 已完成 | **84,654 头（36.09%）** |
| 剩余 | **149,919 头** ≈ 375 段 |
| 已收官组 | **29 / 43** |

## 一、任务目标（验收标准）

把 `03-原始史料库/11-邮件列表史料/07-usenet/duckdb/usenet_mail.duckdb` 中 **43 个新闻组、全部 234,573 个邮件头**行级遍历完毕，产出可溯源的一手史料 claim 并注入 `05-卷册大纲`。

单段（400 头）完成的判据（**四项全绿方算收口**）：

1. `_validate_spec_sl.py <spec> 20 80` → `violations=0`
2. `_pipeline_check.py <dump> <c1> <lo> <hi>` → `不一致项 0 条`
3. `_verify_outline_landing.py <anchor>` → `判定: PASS`（未落地 0 / claim_id 不符 0 / 等级不符 0）
4. `audit_evidence_level_labels.py` → `判定：PASS`

外加：register 反查 N/N、四表 join N、分组全分配零重复、块脚本幂等二跑 0、supplement 二跑 append 0、changelog 真幂等。

## 二、执行协议（**每段拆 3 轮，禁止一轮做完**）

> 依据：2026-09-14 中断诊断——单段全读 ≈110K tokens、单轮 40–50 次工具调用，是中断主因。

### 轮 1 · 全读与候选
```
_dump_generic.py <list_id> <lo> <hi> > _ngNN_dump_sK_<date>.txt
→ 生成 review_logs/ngNN_sK_digest.txt（400 字，triage 用）
→ 生成 _ngNN_sK_forread.txt（1200 字，显式 sort(key=int(pk)) + assert 递增）
→ Read limit ≤ 100 行，分块通读（禁抽样）
→ 逐条写 _ngNN_sK_cand_raw.txt（pk|L3/L4|摘要，20–80 字）
→ _validate_spec_sl.py 复检 + 语义对齐核验（回查 dump 全文）
```
**产出**：候选稿。**不做收口。**

### 轮 2 · 收口前半
```
cp _ngNN_sK_cand_raw.txt review_logs/ngNN_sK_spec.txt
_pipeline_gen.py → ngNN_sK_c1.txt
_pipeline_check.py（须 0 不一致）
_pipeline_register.py <list_id> ngNN_sK <c1> --dry-run → 再正式跑
提取 MAPJSON → review_logs/ngNN_sK_claim_map.json（并用 _export_claim_map.py 交叉验证）
生成 assign.txt → 写 _ngNN_sK_hostmap.txt → 跑分布检查（各组须落 5–80）
_build_ngNN_sK.py → _groups_/_targets_.json
```
**产出**：claim_map + 分组 JSON。

### 轮 3 · 收口后半
```
_pipeline_blocks.py ... （dry → write → 幂等二跑须 0）
_pipeline_supplement.py ... （二跑须 append 0）
_changelog_ngNNsK_<date>.py（dry → write → 复跑须 no-op）
_verify_outline_landing.py + audit_evidence_level_labels.py（须双 PASS）
路径限定 git add（不 commit）
写 _staging_ngNN_sK.md → 更新 plan → 更新进度报告 → 追加 memory → present_files
```
**产出**：入纲块 + 全部记账 + 收官报告。

## 三、中断恢复协议（**新会话/新轮如何接手**）

1. **读** `long_task_state.json` 的 `queue[0]` → 得 `list_id / next_segment / next_window`。
2. **判断当前段处于哪一轮**（按磁盘产物推断，勿凭记忆）：
   - 无 `_ngNN_sK_cand_raw.txt` → 从**轮 1** 开始
   - 有候选稿、无 `review_logs/ngNN_sK_claim_map.json` → 从**轮 2** 开始
   - 有 claim_map、无 `_staging_ngNN_sK.md` → 从**轮 3** 开始
   - 有 `_staging_ngNN_sK.md` → 本段已收口，取 `queue[1]`
3. **所有步骤幂等**：重复执行 register / blocks / supplement / changelog 均会自动跳过，**可安全重跑**。
4. **并发安全**：并行会话持续写库与提交。开工前查 `git log -3` 与 DB `MAX(claim_id)`，取实时值；提交一律路径限定，不 commit。

## 四、执行队列（14 组待做，按优先级）

| # | list | 新闻组 | 下一段 | 窗口 | 剩余 |
|---|---|---|---|---|---|
| 1 | 21 | comp.unix.shell | s7 | 78536–78648 | **112**（收官段） |
| 2 | 12 | comp.unix.admin | s2 | 30287–30674 | 388 |
| 3 | 35 | std.unix | s1 | 139588–139987 | 1,114 |
| 4 | 34 | sources.unix | s1 | 136111–136510 | 1,876 |
| 5 | 38 | unix.bsd.bsdi.misc | s13 | 147514–147913 | 5,198 |
| 6 | 22 | comp.unix.ultrix | s2 | 79049–79448 | 6,667 |
| 7 | 41 | unix.bsd.misc | s12 | 176957–177356 | 8,401 |
| 8 | 11 | comp.sys.sun | s11 | 18000–18399 | 10,252 |
| 9 | 15 | comp.unix.i386 | s1 | — | 6,662 |
| 10 | 40 | unix.bsd | s13 | — | 13,937 |
| 11 | 20 | comp.unix.questions | s12 | — | 21,794 |
| 12 | 23 | comp.unix.wizards | s12 | — | 28,406 |
| 13 | 44 | unix.bsd.openbsd.misc | s18 | — | 41,920 |
| 14 | 13 | comp.unix.aux | s3 | — | 3,192 |

> 队列优先级：① 收官在即（≤2,000）② 已开工中等库 ③ 未开工小库 ④ 大库。
> 窗口以 `long_task_state.json` 为准（plan 更新后自动重算）。

## 五、铁律（不可违反）

- **机器块** `DB_REF` / `DEEP_ANALYSIS` / `COL_SCAN` / `DB_POINTS` / `PODCAST_REVIEW` / `MAIL_INSIGHT` / `ROW_MINE` **一律不得修改**，只能 DEFERRED 并登记。
- 块头**证据等级必须从 DB 真值读**，严禁写死字面。
- 替换须**完整锚点 + count==1 断言**，先 dry-run 再 write，写后二次复验。
- **禁止**全字串替换、新建/移动/重命名源文件、在 `08-核查报告与多轮复核/` 下新增 .md。
- 格式：UTF-8 无 BOM、LF、中文弯引号、**禁用直角引号 `“”“”`**。
- 提交**路径限定**，不 commit，不提交 `SUMMARY.md`。

## 六、防中断参数（每轮必守）

| 项 | 上限 |
|---|---|
| Read `limit` | ≤ 100 行 |
| 单次 Write | ≤ 30 KB（超则分 2–3 批） |
| 长输出 | 一律 `| tail -n` |
| 子代理并发 | 收口期**不并发**；派发一次只发 1 路 |
| 轮末落盘 | `_staging_*.md` + plan + 进度报告 + memory（缺一不可） |

## 七、进度快照（**以 DB 真值为准**）

- **2026-09-14 深夜（DB 重建）**：已读 **94,368 / 234,573 = 40.23%**；**收官 21/43 组**；剩余 **140,205 头**（22 组待做）。
- 历史记录：曾因 plan 滞后误记 30/43 收官、36.14%，已按 DB 的 `raw_source.local_pk` 最大值修正。

### 执行队列（22 组待做）

| # | list | 新闻组 | 剩余 | 下一窗口 | span |
|---|---|---|---|---|---|
| 1 | 16 | comp.unix.internals | 1 | [45569, 45569] | 1 |
| 2 | 18 | comp.unix.misc | 1 | [47441, 47441] | 1 |
| 3 | 7 | comp.org.usenix | 3 | [8246, 8248] | 3 |
| 4 | 9 | comp.std.c | 4 | [12983, 12986] | 4 |
| 5 | 33 | os.386bsd.development | 4 | [135307, 135310] | 4 |
| 6 | 8 | comp.os.eunice | 5 | [8579, 8583] | 5 |
| 7 | 15 | comp.unix.i386 | 10 | [42478, 42487] | 10 |
| 8 | 31 | bugs.4bsd.ucb-fixes | 10 | [128995, 129004] | 10 |
| 9 | 36 | unix.bsd.386bsd.misc | 15 | [142599, 142613] | 15 |
| 10 | 32 | os.386bsd.bugs | 18 | [132157, 132174] | 18 |
| 11 | 3 | comp.bugs.2bsd | 21 | [846, 866] | 21 |
| 12 | 35 | std.unix | 314 | [140388, 140701] | 314 |
| 13 | 34 | sources.unix | 1,176 | [136812, 137211] | 400 |
| 14 | 38 | unix.bsd.bsdi.misc | 5,199 | [147513, 147912] | 400 |
| 15 | 22 | comp.unix.ultrix | 6,269 | [79449, 79848] | 400 |
| 16 | 41 | unix.bsd.misc | 8,401 | [176957, 177356] | 400 |
| 17 | 11 | comp.sys.sun | 10,255 | [17998, 18397] | 400 |
| 18 | 40 | unix.bsd | 13,968 | [158586, 158985] | 400 |
| 19 | 20 | comp.unix.questions | 21,794 | [54232, 54631] | 400 |
| 20 | 23 | comp.unix.wizards | 28,407 | [95649, 96048] | 400 |
| 21 | 44 | unix.bsd.openbsd.misc | 41,924 | [193405, 193804] | 400 |
| 22 | 13 | comp.unix.aux | 2,406 | [33075, 33474] | 400 |

> **开工前必须用 DB 复核**：`select max(cast(local_pk as bigint)) from raw_source where source_db='usenet_mail'`，
> 按源库 `messages` 的 `id→list_id` 分组；**某 list 的 max local_pk 大于等于其 `id_hi` 即已 CLOSED**。
> 磁盘产物（`_groups_ngNN_s_K.json` / `_staging_ngNN_s_K.md` / `review_logs/ngNN_s_K_claim_map.json`）比 plan 可信。
