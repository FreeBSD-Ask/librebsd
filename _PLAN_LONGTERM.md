# 长线总账（Live）· 防会话中断唯一入口

> **读这一份就够**：本文件是**三线**（shenyue 复核 / mail2d H3 / mail2d H1）的**唯一长期入口**，
> 新会话读到本文件即可续接，无须任何先前对话记忆。
> 细节归档（SOP 全文、裁定取证、坑速查完整版）在 `_PLAN_20260921.md`，本文件只留**活数据与命令**。
> 上游分线规程：`shenyue/review/_LONGRUN_PLAN.md`（复核线）、`script/_db_row_mining/_H3_RESUME.md`（H3 断点续跑书）、
> `script/_db_row_mining/_H1_LONGTERM.md`（H1 长线档案，含 H1 全套 SOP 与宿主分派口径）。
> **冲突时以台账实测值为准，永不以本文档数字为准**（本文档是台账的副本，已实测漂移 3 次，见 §七）。

---

## 〇、一句话现状（2026-09-21 19:48 实测）

| 线 | 游标（台账实测） | 下一批 |
|---|---|---|
| **shenyue 复核** | A 类 **692/692 全闭环**（16 批）｜B 类 **550/748**（0027 已落账 seq 27）｜C 类 **0/1972** | `BATCH-0028`（B pos 551–600，O-2082 起） |
| **mail2d H2** | `freebsd-bugs` **2000/192683**（b171＋b172/b173/b174）｜`-ports` **21000/191637**（b151–b157）｜`-net` **45000/73645**｜`-chat` **43869/43869 已整库闭环** | `fbug_b173` ✅ 全链闭环 `cee1e72ec`（327 块 +1635 行）；`fbug_b174` 328 条已 register CL-RM-154743–155070，叙述 4/5 包已落 262 行违规 0、p1 重派中；`fpo_b156` **702 条已 register CL-RM-155072–155773**，9 叙述包 3 落盘＋4 在途＋2 重派；`fpo_b157` 五片已回、p1 重派在途 |
| **mail2d H3** | `freebsd-hackers` **42000/201463（20.85%）**（fhk_b021 已完全收口，255 块入纲 6 宿主，commit `54119d159`）；`-current`/`-doc`/`-stable` **0** | `fhk_b022` 已预建＋4 读手在途（19:20 派，全批 2013 年、容器行 0）＋ `fcu_b001` 续读 3 路在途 → `fdoc_b001`／`fstb_b001` |
| **mail2d H1** | `freebsd-questions` **76000/472235（16.10%）**；**37 批已提交**，b038 在途 | `fq_b038` 叙述 5 包 3 路在途（候选 145 已落库 CL-RM-153855–153999）→ `fq_b039` |

**H1 真值**（`script/_db_row_mining/_H1_LONGTERM.md` 为入口，台账 `_h1_state.json` 为状态机）：
`freebsd-questions` 全库 **472,235** 封，共 **237 批**（÷2000，末批 b237 为 n=235），
**37 批 committed** + b038 `registered`（候选 145 条、正文 145/145）+ 199 批 pending；
宿主 `921,10016,10017,923,924`；密度带 **3–8%**；下一批 offset **76000**。

**H3 四库真值**（`script/_db_row_mining/mail2d_read_ledger.json`，实测 2026-09-21 19:10）：

| 库 | 全库 | 已判读 | 剩余 | ≈批数 | 宿主口径 |
|---|---:|---:|---:|---:|---|
| `freebsd-hackers` | 201463 | **42000** | 159463 | ≈80 | **13 键**（885,916,986,1058,1067,1069,1229,1588,1648,10018,10110,12413,12417） |
| `freebsd-current` | 205027 | 0 | 205027 | ≈103 | **15 键**（含 fcu 专属 1016/1039/1316） |
| `freebsd-doc` | 72663 | 0 | 72663 | ≈37 | 待实判（P1） |
| `freebsd-stable` | 72164 | 0 | 72164 | ≈37 | 待实判（分支章，P1） |

四库合计已判读 **42000／551317（7.62%）**，剩余 ≈255 批（÷2000）。

🔴 **token 配额硬停（2026-09-21 18:38–18:50 实测，本会话 5 路子代理全部 `token plan
entitlement exhausted` 失败）**：fcu_b001 读手 4 路（21–25 分钟各死一次）＋ shenyue
seg-33 评审员（37.8 分钟）。**失败发生在写盘之后**——磁盘产物完整可用，但收尾 JSON
回报全丢。**新会话开工第一件事是确认配额是否恢复**；未恢复则**只能主代理 solo**
（见 §四 止损阶梯末级），不得再派子代理（派了也是 20+ 分钟零回报）。
⚠️ 并行会话同时在跑 H1／H2／H4／shenyue 多条线，配额是**全会话池**，多线并发会互相挤爆。

**H2 四库真值**（`script/_db_row_mining/_RESUME_H2.md` 为断点入口，台账 `_db_row_mining/mail2d_read_ledger.json`）：

| 库 | 全库 | 已判读 | 剩余 | records（行序） |
|---|---:|---:|---:|---|
| `freebsd-ports` | 191637 | 15000 | 176637 | `[(0,15000)]` fpo_b151–b155 |
| `freebsd-bugs` | 192683 | 1000 | 191683 | `[(0,500)]` b171 ＋ `[(137970,138470)]` b172 |
| `freebsd-net` | 73645 | 45000 | 28645 | `[(0,45000)]` fn_b156–b170；queued `[(45000,48000)]` fn_b171 |
| `freebsd-chat` | 43869 | 43869 | **0** | `[(0,43869)]` fch_b137–b150，**已整库闭环** |

⚠️ `_HANDOFF_H2.md` §二 三处数据已过期（ports/net/chat 的「已读 0」皆非）——**以本表为准**，
订正详情见 `_RESUME_H2.md` §一。freebsd-bugs 的 pk 空间年份同质，**下一批直接按 offset 138470 跳**，
勿从 0/500 线性回退（见 `_HANDOFF_H2.md` §9.6）。

**shenyue 台账真值**（`shenyue/review/_ledger.jsonl`）：**27 行**、verify **0 fails**、
B 游标 pos **550**（O-2073，下一位 O-2082）、B 类剩余 **198 条（4 批）**。

🔴 **本会话裁定（2026-09-21 18:00）**：会话模型适配 **1M 上下文 token**（GLM-5.2 xhigh）；
**允许多个子代理**（沿用 §四 3–4 评审员／波，`run_in_background` + 8 分钟止损）。
1M 上下文下主代理可读 KB 级探针输出，但**仍不读** R 条目正文／23 MB jsonl（铁律不变）。
BATCH-0027 已由主代理建 `URL_CORPUS.md`（48 条可达入口，含 Darwin／DragonFly／tuhs／freebsd 新增），
4 评审员（seg-21..24）已派，断点 `_progress-BATCH-0027.json` status=IN_PROGRESS_4_REVIEWERS_DISPATCHED。

---

## 一、中断恢复三步法（新会话第一件事）

1. **读本文档 §〇 与 §五**，定两条线的在途状态。
2. **读两条台账定真游标**（不信本文档，见 §七）：
   - H3：`C:/Python314/python.exe -c "import json;d=json.load(open('script/_db_row_mining/mail2d_read_ledger.json'));print({k:(v['read_judged'],v['queued_spec']) for k,v in d['items'].items() if k.startswith('freebsd')})"`
   - shenyue：`shenyue/review/_ledger.json`（行数、seen、next_batch_no、B/C 游标 pos）
3. **找在途 tag**：`script/_db_row_mining/_batch_*.json` 中**有 spec 但无 claim_map** 的即在途；
   shenyue 侧看 `shenyue/review/_progress-BATCH-*.json` 的 `inflight` 段。
   → 按该批的断点文件定位缺失步 → 按 §三 SOP 续跑。

**幂等续接安全**：H3 的 `outline --write` 与 shenyue 的 `_s51_merge_partial.py` 均以「已落盘块」为权威，
重复 pk / oid 会被报出而拒收。**重派同一单元只是浪费，不会污染台账。**

---

## 二、中断免疫硬规则（七条，所有会话必须遵守）

1. **磁盘即记忆**：任何工作单元状态必须落文件；上下文被压缩/终止即全丢。**每批开工第一步写断点文件**
   （H3 追加 `_H3_PROGRESS.md` 段；shenyue 写 `shenyue/review/_progress-BATCH-<NNNN>.json` 含 dispatched 计划），
   最后一步才改完成态。
2. **游标只信台账，不信文档**：H3 信 `mail2d_read_ledger.json`；shenyue 信 `_ledger.json`。
3. **单批闭环粒度**：一个 checkpoint ＝ 一批完整闭环。**在途批每线不超过 1 批**。
4. **幂等续接**（见 §一）。
5. **原子提交 + pathspec**：每批闭环立即 `git commit -- <本批文件>`；commit 前 `git update-index --refresh`
   清 racy-stat 幻影。**禁 `git add -A`**（并行会话秒级卷走暂存件）；不 commit 他人改动。
6. **子代理限时 + 主代理兜底**：见 §四。
7. **主代理只做确定性活**：合并、落库、写回、门禁、提交、台账刷新——**一律脚本，不派子代理**。
   内容活（读手判读、叙述撰写、评审）才派子代理。

**上下文预算硬约束**：主代理**不读 20 MB+ 文件**、**不读** `<tag>_forread.txt`、
**不读** `section_record.jsonl`/`_local_rounds3.jsonl`/`local_matches.jsonl`（各 ≈23 MB）、**不读** R 条目正文。
一切数字来自脚本实测输出（KB 级）。

---

## 三、单会话工作单元（一个会话安全容量 ＝ H3 一批 **或** shenyue 一批）

### 3.1 H3 一批（`freebsd-hackers`／`freebsd-current` 通用）

```
 1. 读 _H3_PROGRESS.md 对应批段 + mail2d_read_ledger.json      ← 三源交叉定 offset
 2. _prep_batches.py <tag>:<offset>:2000 --lib <库> --hosts <池>  ← spec＋dump＋拆 4 份 digest
 3. 主代理补丁：spec 补 hosts（按本批年段从 _H3_HOST_POOL.md 实测选）＋ line_date=2026-09-18
 4. 派 4 路读手（run_in_background），每份 500 行 digest_partK.txt
 5. 限时监控；8 分钟无落盘即 TaskStop＋重派；全败则主代理直读
 6. _part_profile / _audit_cand_fidelity / _audit_author_match  ← 三源取真值，勿信读手自报
 7. _merge_parts.py <tag> 4   →   _mail2d_run_batch.py register --tag <tag> --apply
 8. body --tag <tag>   →   _split_narr.py <tag> 4   →   派叙述手（每波 ≤4）   →   _merge_narr.py
 9. _chk_mount_narr.py → _audit_narr_propernoun.py（可疑条仅回原文重写）
10. outline --write（**幂等二跑须 +0**）→ bookkeep --write → 等级门禁 → commit --apply
11. _build_read_ledger.py 刷新台账 → git commit（pathspec）→ 回写 _H3_PROGRESS.md
```

**作者对位门禁命中处置（fhk_b021 实证定式）**：命中后回 duckdb 取**完整正文**判本方口吻——
digest 仅 420 字窗口且 `from` 列是**回帖人**、正文被 `>` 引用块占满，这正是漂移根因。
该行作者有自述技术判断 → 改写为其本方口吻（L4）；仅纯转发/一句客套 → **剔除**。**严禁从被引者内容硬凑。**
门禁输出须先人工分流「from 列 40 字截断假阳（如 Wojtek Puchar）vs 真漂移」，不得整批改写。

### 3.2 shenyue 一批复核

```
 1. 读 _LONGRUN_PLAN.md + _progress-BATCH-<NNNN>.json + review/_ledger.json
 2. 写 _progress-BATCH-<NNNN>.json（dispatched 计划）            ← 先登记
 3. _s50_batch_prep.py prep <cls>   →  派 3–4 评审员（每片 ≤7 oid，run_in_background）
 4. 限时监控；8 分钟无落盘即 TaskStop＋重派；全败则主代理 solo
 5. _s51_merge_partial.py merge <cls> <NNNN>
 6. _s52_audit_web_evidence.py --batch <cls> <NNNN>              ← 联网证据门禁
 7. _s25_ledger.py append <cls> <pos_lo> <pos_hi> <报告名>  →  _s25_ledger.py verify
 8. git commit（pathspec）→ 更新 _progress（完成态）
```

**联网证据门禁**：`WebSearch` 在本 provider **不可用**（Provider API kind openai-compatible 不编码
provider-native WebSearch）。**必须主代理先建 URL 语料再派评审员**：
走 Bing 两步 WebFetch（搜索页取 organic → 逐条 fetch 正文），产出 `review/.runs/BATCH-<NNNN>/URL_CORPUS.md`
（范式见 `BATCH-0025/URL_CORPUS.md`，75 行），明确标注已实测可达入口与被拦站点
（marc.info、openbsd-hack.net、ksp.kth.se 等）。**单条 12–36 次 fetch、8–18 分钟**；
DDG 有 bot 校验、archive.org 间歇离线；URL 不得含省略号。
派单必须附此语料并写明「子代理只能引用自己实测成功的 URL」，**不计成本不得减少联网**。
（B 0017–0023 六批 300 条 URL=0、0024 门禁 FAIL 30 项同源；修法是附可直取语料，不是加代理数。）

### 3.3 解释器

`C:/Python314/python.exe` 通用（duckdb 与文本脚本均可跑）。

---

## 四、子代理编排纪律（授权 3–8 路）

| 项 | 值 |
|---|---|
| 子代理/波 | **3–4 路**（mail2d 实测 ≥4 路易触发 429，取 4 为上限） |
| 并发总量 | 跨线不超过 8 路；**在途批每线不超过 1 批** |
| 派发方式 | `Agent` + `run_in_background: true`（并行，返回 agentId 供止损） |
| 止损 | `TaskOutput` 限时；**8 分钟无落盘即 `TaskStop` 并匿名重派一次**（换句柄名，勿复用 agentId）；重派仍败则转主代理 solo 清单 |
| 🔴 禁用 | **`CreateWorkflow` 跑长线**：actor 无 per-ask 超时，实测评审员 7+ 分钟 0 工具调用卡死零产出，脚本无法局部止损。`shenyue/.zcode/workflows/*.dwf.ts` **废弃不执行** |
| 自报数字 | **一律不信**（BATCH-0009 各片自报 206，实测 301） |
| 429 处理 | 记「本轮降为 X 路」，不重试整波，改主代理直读 |
| 命名避让 | shenyue 段文件用 `seg-<会话段号>`，防并行会话互相覆盖（BATCH-0024 已发生 seg-01/02 撞名事故） |

**读手/叙述手提示词必写四句**（零产出事故的唯一有效解，本线 16 路零事故实证）：
① 每次 Read 限 100–1200 行；② 每写约 20 行用 Write 增量落盘（覆盖写全文），不得写完才一次性落盘；
③ 转录与产出以行首 pk / oid 为准，禁用行号；④ 回报写出实际落盘行数、宿主/段分布、以及任何「摘要与原文不符」清单。

---

## 五、在途表（2026-09-21 19:30）

| 项 | 状态 | 句柄／产物 |
|---|---|---|
| `fhk_b021` 候选（256 条，L4 223／L3 33） | ✅ check 0 违规、越界 0 | `review_logs/fhk_b021_candidates.txt` |
| `fhk_b021` 作者对位 | ✅ 30 条命中 → **14 真缺陷已定点改写/剔除＋6 Wojtek 假阳不动** | `_fix_author_fhk_b021.py`、`review_logs/fhk_b021_fixdec_{a,b}.json` |
| `fhk_b021` register | ✅ **COMMITTED 256**，claim seq **CL-RM-153599–153854**，反查 256/256，四表 join 256 | `_batch_fhk_b021.json` 的 `claim_map` |
| `fhk_b021` body + 叙述拆件 | ✅ 正文 256/256（缺失 0），`narrpkg_p1..p4` 各 64 条 | `cands_body_p1..p4.txt`（年段 2012×216＋2013×40） |
| `fhk_b021` 叙述手 | 🔄 **4 路**（p2✅64／p4✅64 已完稿；p1 58/64 推进中；p3 重派后待首落盘） | 首派 p1/p3 卡死（p1 写 39 行后停滞 18 分钟、p3 全程 20 分钟零落盘），17:55 止损并匿名重派（p1 `agent_6415cad4`／p3 `agent_a1e1f4d1`）；产出 `mount_narr_p1..p4.tsv` |
| `fcu_b001`（offset 0，pk 246–1025423） | ⏸ 已预建待派读手（**容器行 301/2000＝15.1%，读手一律不收**；年段 2008×1645／2010×53／2018×51／2002×47／2003×20／2017×1） | `_batch_fcu_b001.json`、`review_logs/fcu_b001_container_pks.txt` |
| shenyue `BATCH-0025` | ✅ 已落账 seq 25、verify 0 fails | `shenyue/review/_ledger.json` |
| shenyue `BATCH-0026` | ✅ 已落账 seq 26、verify 0 fails（门禁残留 67 项 C28+E32 体例漏项登记 _WEB_DEBT_REGISTER.md §八，只登记不追补） | `shenyue/review/_ledger.json` |
| shenyue `BATCH-0027` | ✅ **已落账 seq 27、门禁 PASS 零残留**（B pos 501–550、O-1891→O-2073，50 块、来源池 150 行）；四片 seg-21..24 全齐（13/13/12/12，0 占位符，counts 13/13/12/12）；0026 的 C/E 体例漏项教训已写死进派单，本批一次过 | `shenyue/review/逐条建议书-B-BATCH-0027.md`（1161 行）、`_sourcebank-B-0027.jsonl`（150 行）、`_ledger.jsonl` +1 |
| shenyue `BATCH-0028` | ⏸ 未开工（B pos 551–600、O-2082 起；剩余 4 批 0028–0031，B 类尾批 0031 为 48 条） | `_a_order.json` 的 `order.B` |
| `fbug_b173`（bugs offset 138470） | ✅ **全链闭环 `cee1e72ec`**：327 块入 88.1/88.6/88.7，+1635 行恰 = 327×5，0 删除；outline 幂等二跑 +0、bookkeep 三零 PASS、等级门禁 PASS | `_RESUME_H2.md` §二「fbug_b173 全链闭环记录」 |
| `fbug_b174`（bugs offset 138970，pk 1047668–1048166） | 🔄 328 条 **register COMMITTED**（`CL-RM-154743`–`155070`，反查 328/328）→ body 328/328 → 5 叙述包。**p2/p3/p4/p5 已落 262 行、违规 0**（p3 由压缩员 158→139）；**p1 被双写抹成 1 字节，重派在途**。收齐后 `_merge_narr.py fbug_b174 5 881,886,887` → 收口，提交应 +**1640** 行。**16 条读手增量不进本批**，另开 tag | `_NARR_TASK_fbug_b174.md`、`fbug_b174_extra_cand.txt`、`fbug_b174_summary_changed.txt` |
| `fpo_b156`（ports offset 15000，pk 1567555–1570595，n=3000） | 🔄 **702 条** → `_s62_merge_multi.py fpo_b156 6` **0 违规** → `check` PASS（L4 518／L3 184，摘要 25–80／avg 64.0）→ **register COMMITTED 702**（`CL-RM-155072`–`155773`，反查 702/702、四表 join 702）→ body 702/702（727 399 B）→ `_split_narr.py fpo_b156 9` 各 78。**宿主 6 键已实测校准**：891/892/894/906/907/909，**禁 883**（2004 期）。p3/p4/p5 ✅ 已落盘；p1/p2 静默死亡已重派；p6–p9 在途。收齐后 `_merge_narr.py fpo_b156 9 891,892,894,906,907,909` → 收口，提交应 +**3510** 行 | `_NARR_TASK_fpo_b156.md`、`review_logs/fpo_b156_cand_p*.txt` |
| `fpo_b157`（ports offset 18000，pk 1570596–1573653，n=3000） | 🔄 **五片已回**：p2 ✅43／p3 ✅57／p4 ✅50／p5 ✅29／p6 ✅83；**p1 重派在途**。收齐后 `_s62_merge_multi.py fpo_b157 6` → check → register → body → `_split_narr` → 叙述（宿主同 b156 六键） | `review_logs/fpo_b157_cand_p*.txt`、`_READ_TASK_fpo_b157.md` |
| H2 下一批候选 | ⏸ `fbug_b175`（offset **139470**，按段跳到 161000 块尾）；`fpo_b158`（offset **21000**）；`fn_b172`（offset **48000**，fn_b171 收口后） | `_RESUME_H2.md` §三 |
| `fdoc_b001`／`fstab_b001` | ⏸ 未预建（P1，待 P0 两库推进后再派） | — |
| H3 `fhk_b021`（hackers offset 40000，pk 1312727–1314738） | ✅ **完全收口**：候选 **255 条**（原 256，剔除 1312976——from/subject/thread_refs 全空且 message_id 为合成号 `<no-id-...>`，库中 `status='rejected'`）→ 摘要对位订正 **20 改＋1 剔除**＋叙述改 **7 条** → outline **255 块入 6 宿主**（106.9 +237／124.17 +4／124.13 +2／164.8 +4／158.8 +4／106.7 +4）→ bookkeep 缺块 0／claim_id 不符 0／重复 0 → 等级门禁全库 **PASS**（3279 md／134282 抬头／0 错／0 悬空）→ commit `54119d159` → 台账 `freebsd-hackers` **42000** | `script/_db_row_mining/review_logs/fhk_b021_*`、`_fix_cand_fhk_b021_p2.py`、`_fix_narr_fhk_b021_pn.py`、`_outline_fhk_b021.py` |
| H3 `fcu_b001`（current offset 0，pk 2462–1025423，容器行 301/2000） | 🔄 **续读 3 路已派（19:20）**：p1（剩 305 行，续 `pk>6324`）／p3（剩 100 行，续 `pk>1024811`）／p4（剩 400 行，续 `pk>1025023`），**p2 已读完**；追加写勿覆盖旧行（旧 8／253／125／26 条）。⚠ p1 大部分行落在容器行清单内，候选数不会高属正常。句柄见 `_DISPATCH_20260921_1920.json` | `_READ_TASK_fcu_b001.md`（§十 断点表）、`review_logs/fcu_b001_candidates_part1..4.txt` |
| H3 `fhk_b022`（hackers offset 42000，pk 1314739–1316740） | 🔄 **已预建＋4 读手已派（19:20）**：spec `_batch_fhk_b022.json`（已补 `pk_range`／`line_date=2026-09-18`／`containers=0`）、dump 2000 行、digest 拆 4 份各 500 行、任务书 `_READ_TASK_fhk_b022.md`（含 §五.1 摘要归属铁律）。**本批全为 2013 年、容器行 0**（判据实测：0 行符合「≥3 处行首 `From `＋`From owner-`＋>20KB」；该判据已在 fcu_b001 上复算 301/301 完全吻合，可复用）。p1 1314739–1315238／p2 1315239–1315738／p3 1315739–1316240／p4 1316241–1316740 | `_DISPATCH_20260921_1920.json`、`review_logs/fhk_b022_digest_part1..4.txt` |

**止损指令**：任一子代理 8 分钟无落盘即 `TaskStop` 并重派同一分件；全败则该分件转主代理直读。

---

## 六、长尾队列总账

| 序 | 战线 | 规模 | 单批 | 剩余批数 |
|---|---|---:|---|---:|
| **P0** | H3 `freebsd-hackers` | 159463 封 | 2000/批 | ≈80（b021 已收口，下一批 b022 offset 42000） |
| **P0** | H3 `freebsd-current` | 205027 封 | 2000/批 | ≈103（b001 已预建、在读 412 条待续） |
| **P1** | H3 `freebsd-doc` | 72663 封 | 2000/批 | ≈37 |
| **P1** | H3 `freebsd-stable` | 72164 封 | 2000/批 | ≈37 |
| **P2** | shenyue B 类 | **198 条**（748−550） | 50/批 | **4**（0028–0031，尾批 0031 为 48 条） |
| **P2** | H2 `freebsd-bugs` | 190683 封 | 500/批 | ≈382（**须按 offset 段跳**：139470→139970→…→161000 块尾，勿线性回退，空密度区会空烧约 276 批） |
| **P2** | H2 `freebsd-ports` | 170637 封 | 3000/批 | ≈57 |
| **P3** | H2 `freebsd-net` | 28645 封 | 3000/批 | ≈10（fn_b171 已预建 queued，part1 已完稿 190 条） |
| **P3** | shenyue C 类 | 1972 条 | 50/批 | **40**（0032–0071） |
| **P4** | shenyue 联网证据债务 | 实测 **747 条**（旧估 595 作废） | — | **已裁定「只登记不追补」**，台账 `_WEB_DEBT_REGISTER.md`（`5597bb3d7`）；裁定只登记，不重派评审员 |

---

## 七、已知坑速查（勿重复踩）

| 坑 | 处置 |
|---|---|
| 🔴 文档数字漂移（**本文档亦不免**） | 已实测 3 处：①台账「记 38000」实为 40000；②`_HANDOFF_H3.md` 称 fhk_b021「15 键」实为 13 键；③`_HANDOFF_H2.md` 称「4 库/501834 封」实为 3 库/397965（`freebsd-chat` 已 completed）。**开工前必读台账 JSON** |
| 🔴 digest `from` 列＝回帖人、正文被引用块占满 | 读手把内容归给被引者 → 门禁命中后回 duckdb 取**完整正文**判本方口吻；纯转发则剔除（见 §3.1） |
| Wojtek Puchar 类 from 40 字截断 → 假阳性 | 门禁输出须人工分流「截断假阳 vs 真漂移」，不得整批改写 |
| 🔴 `_merge_parts.py` 摘要 20–80 字是**阻断级校验** | 超长即中止不写盘。须**先按「改动集＝原超长集」定点压缩至 ≤80 字再 merge**，压缩保留人名与版本号，禁从专名中间截断 |
| 候选文件整表重抄 | 必引入人名笔误。一律**脚本按 pk 定点替换**，断言 `hit == len(fixes)`，不符即中止不写盘 |
| 容器行（低 id 区 ≈15%） | 逐批读 `review_logs/<tag>_container_pks.txt`，读手一律不收 |
| 读手 pk 错位 | `fhk_b007` p4 偏移 8 位／`fhk_b008` p4 偏移 1 位。以行首 pk 转录，`_audit_author_match.py` 兜底 |
| lite 池叙述手臆造专名 | `fhk_b017` p1 实测 29 条臆造。`_audit_narr_propernoun.py` 筛，主会话只回原文重写可疑条 |
| 宿主预判号不存在 | `_HANDOFF_H3.md` 的 `1661/1673` 不在宿主池；**dump 后按年段从宿主池实测选宿主** |
| `_prep_batches.py` 尾部 ValueError | `--lib`/`--hosts` 取值被当 spec 解析；spec 与 digest 已正确生成，忽略 traceback 但须事后校验 spec 的 hosts/line_date |
| `_fetch_body` 覆盖输出 | 两次调用写同一文件致第一份丢失 → 已加 `OUTNAME` 参数 |
| 台账 append 非原子 | 读两遍核对；append 后立即 verify |
| 并行会话整索引提交卷走暂存件 | pathspec 提交；commit 前 `git update-index --refresh`；racy-stat 幻影先 refresh |
| 同文件并发 Edit 静默覆盖 | 编辑同一文件必须串行 |
| shenyue 报告内嵌多余页脚 | `_s25_ledger.py` 用 `re.search` 首匹配取 `NEXT:`，中段残留页脚会致 append 被拒。落账前删净中段页脚 |
| `.gitignore` 全局 `*.py` | 新脚本默认被忽略；`script/_db_row_mining/` 整目录只提宿主 md，工作工具按 gitignored 保留 |
| 等级门禁脚本路径 | **不在工作区根**，实为 `00-编纂规则与格式规范/01-规则/脚本与命令/audit_evidence_level_labels.py` |
| Bash 写 `.py` 被 hook 拦截 | 用 Write 工具写脚本 |
| mail2d register 覆盖 claim_map | `cmd_register` 增量重跑会把 53 缩到 15 致 check 断言崩；已加 `merge_claim_map`（四场景单测过），修法只存磁盘 |

---

## 八、待主理人裁定（3 项，均已实测取证，取证详见 `_PLAN_20260921.md` §五）

1. **来源池回填的诚实边界**：转写回填标记 `sourcebank_origin: backfill` 是否接受；§9.4 体例性豁免是否合法；
   B 0017–0023 真未检索条目是否须重派。**当前状态**：已按「只登记不追补」登记 `_WEB_DEBT_REGISTER.md`。
2. **权威游标纳入 git 跟踪**（2026-09-21 17:50 实测**扩大为两个洞**）：
   - (a) `shenyue/review/_ledger.json`（shenyue 权威游标）未被 git 跟踪，仅 `_ledger.jsonl` 在版本控制内；
     被并行会话误删只能从 `.jsonl` 全量重建。
   - (b) 🔴 **`.gitignore:310:/script` 使整个 `script/` 目录未被版本控制**——H3 线的交接书
     `_HANDOFF_H3.md`、断点文档 `_H3_PROGRESS.md`、叙述任务书 `_NARR_TASK_freebsd-hackers.md`
     **全部不在 git 内**（`git check-ignore` 实测确认），与 H1 线 `_HANDOFF_H1.md`／`_H1_PROGRESS.md`
     已被 `git add -f` 提升的既有做法不一致。H3 是唯一活跃主线的交接件却无历史可回溯。
   - **须裁定**：是否将上述游标与 H3 交接件 `git add -f` 纳入版本控制？建议纳入（可逆、低风险）。
   - **未擅自变更**：此为共享仓库的版本控制状态改动，且本项本就列在待裁定清单，故只登记不执行。
3. **`_s25_ledger.py` 的 `web_date` 硬编码** `"2026-09-20"`：改按批次实际联网日期传入，还是维持批次日？
