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

## 下次执行
1. 先跑 `_coverage_by_segment.py` 并查 `evidence.anchor` 确认段次归属，避开并行会话在途段
   （当前在途：ng35_s4；悬空：ng21_s2）。
2. ng12_s6 / ng35_s5 的 dump 已备，直接重派读手（模板见本会话）。
3. 收口顺序：spec → `_fix_cand_chars.py` → gen → check → register → `_extract_claimmap.py`
   → `_mk_assign.py` → 分组子代理 → `_pipeline_blocks.py --write` → 二跑 → supplement → changelog
   → 门禁 → git add → staging → 更新 `_LONGTERM_PLAN.md`。
