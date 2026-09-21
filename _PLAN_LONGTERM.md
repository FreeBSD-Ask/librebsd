# 长线总账（Live）· 防会话中断唯一入口

> **读这一份就够**：本文件是**三线**（shenyue 复核 / mail2d H3 / mail2d H1）的**唯一长期入口**，
> 新会话读到本文件即可续接，无须任何先前对话记忆。
> 细节归档（SOP 全文、裁定取证、坑速查完整版）在 `_PLAN_20260921.md`，本文件只留**活数据与命令**。
> 上游分线规程：`shenyue/review/_LONGRUN_PLAN.md`（复核线）、`script/_db_row_mining/_H3_RESUME.md`（H3 断点续跑书）、
> `script/_db_row_mining/_H1_LONGTERM.md`（H1 长线档案，含 H1 全套 SOP 与宿主分派口径）。
> Linux 邮件列表价值反推线（H6）：`03-原始史料库/11-邮件列表史料/05-linux-kernel/mining/02-遍历留痕/10-价值反推排序与选封管线.md`（价值反推排序+选封管线规程+五层面去重定义）
> **冲突时以台账实测值为准，永不以本文档数字为准**（本文档是台账的副本，已实测漂移 3 次，见 §七）。

---

## 〇、一句话现状（2026-09-22 02:0x 实测）

| 线 | 游标（台账实测） | 下一批 |
|---|---|---|
| **shenyue 复核** | A 类 **692/692 全闭环**（16 批）｜B 类 **550/748**（0027 已落账 seq 27）｜C 类 **0/1972** | `BATCH-0028`（B pos 551–600，O-2082 起） |
| **mail2d H2** | `freebsd-bugs` **2000/192683**（b171＋b172/b173/b174/b174e，b174e 落在既有区间内不扩张）｜`-ports` **24000/191637**（b151–b158，`[(0,24000)]` **连续无缝**）｜`-net` **45000/73645**｜`-chat` **43869/43869 已整库闭环** | **b171–b174＋b174e 五批全链闭环**（`6809bb8a2`／`cee1e72ec`／`27cfc5725`／**`333434176`**）＋ **fpo_b156/b157 已入纲**（`529468ce9`，+5055 行，裹挟留档）；**fpo_b158 在途**：449 条 register（`CL-RM-160230`–`161257`）、正文 449/449、8 包叙述拆件完成、**7 路缺口叙述手在途（226 条）**，未 outline／bookkeep／提交；audit **PASS 错标 0**；**b158 候选集对齐回改已留档**（merge 抢在 4 路读手回报前执行→463 实应 449；63 条改 `status='rejected'`、49 条补 register）。下一批 **`fpo_b159`（offset 24000）**；`fbug_b175`（offset 139470）；`fn_b172`（offset 48000，fn_b171 收口后） |
| **mail2d H3** | 四库 **50000/551317（9.07%）**：`freebsd-hackers` **44000/201463**（fhk_b021 完全收口 `54119d159`）｜`-current` **2000**（fcu_b001 全链收口 `fe4eb1aff`+`034401026`）｜`-doc` **2000**（fdoc_b001 全链收口 `8e330dc09`）｜`-stable` **2000**（fstb_b001 读手＋落库 `61c6e6b63`，**叙述在途**） | **12 路子代理波次在途（02:0x 派）**：8 路叙述手 `fstb_b001` p1–p8 ＋ 1 路 `fhk_b022` 专名订正 29 条 ＋ 3 路读手（`fcu_b002` part1a/1b、`fdoc_b002` part1a）。**下一批已按各自源库预建 spec＋digest＋32 半份**：`fhk_b023`(44000→，pk 1316741–1318740)、`fcu_b002`(2000→，1025424–1027444)、`fdoc_b002`(2000→，1108539–1110552)、`fstb_b002`(2000→，2576642–2578641)，四批容器行均 **0** |
| **mail2d H1** | `freebsd-questions` **76000/472235（16.10%）**；**37 批已提交**，b038 在途 | `fq_b038` 叙述 5 包 3 路在途（候选 145 已落库 CL-RM-153855–153999）→ `fq_b039` |
| **mail2d H5**（200K 派发线，`_h5_state.json` 28 库 101 批） | **全库闭环 10 个**（x11/ipfw/desktop/cu/acpi/smp/i386/sparc64/ppc＋tech-pkg 前两批）；freebsd-ppc 3 批 5185 条候选 | tech-pkg **批1 `h5tp_b528_1`**（`1c3015051`，1141 条 CL-RM-155774–156914）＋**批2 `h5tp_b528_2`**（`b34760350`，1477 条 CL-RM-158737–160213）均已 committed（check/outline 幂等/bookkeep/audit 全 PASS）；下一批 **`h5tp_b528_3`（offset 13500 n 431，尾批）** → tech-pkg 整库闭环后转余下 18 库；入口 `script/_db_row_mining/_HANDOFF_H5.md`（§十 台账＋缺陷）＋记忆 `h5-longhaul-200k-dispatch-20260921` |
| **mail2d H6** | Linux 邮件列表价值反推（九未处理库选封入库管线已建，未执行）；linux-man 实测密度 7.29% 全场第一 | 管线就绪（5 脚本+3 文档），待授权执行第一批 linux-man 入库 |

**H1 真值**（`script/_db_row_mining/_H1_LONGTERM.md` 为入口，台账 `_h1_state.json` 为状态机）：
`freebsd-questions` 全库 **472,235** 封，共 **237 批**（÷2000，末批 b237 为 n=235），
**37 批 committed** + b038 `registered`（候选 145 条、正文 145/145）+ 199 批 pending；
宿主 `921,10016,10017,923,924`；密度带 **3–8%**；下一批 offset **76000**。

**H3 四库真值**（`script/_db_row_mining/mail2d_read_ledger.json`，实测 2026-09-22 01:2x）：

| 库 | 全库 | 已判读 | 剩余 | ≈批数 | 宿主口径 |
|---|---:|---:|---:|---:|---|
| `freebsd-hackers` | 201463 | **44000**（21.84%） | 157463 | ≈79 | **13 键**（885,916,986,1058,1067,1069,1229,1588,1648,10018,10110,12413,12417） |
| `freebsd-current` | 205027 | **2000** | 203027 | ≈102 | **15 键**（含 fcu 专属 1016/1039/1316） |
| `freebsd-doc` | 72663 | **2000** | 70663 | ≈36 | **13 键**（同 hackers，无 1016/1039/1316，有 12413） |
| `freebsd-stable` | 72164 | **2000** | 70164 | ≈36 | **13 键**（同 doc） |

四库合计已判读 **50000／551317（9.07%）**，剩余 501317 封 ≈ **251 批**（÷2000）。

🔴 **台账是 `status_source: spec-only` 口径**：游标随 `_batch_*.json` spec 预建即推进，**不等于 outline 已提交**。
此刻**尚未 outline 入纲**的：`freebsd-hackers` 44000（fhk_b022 专名订正在途）、`freebsd-stable` 2000（fstb_b001 叙述在途）；
**已入纲**：fcu_b001（565 块入 5 宿主）、fdoc_b001（297 块入 7 宿主，幂等二跑 +0）。

🔴 **token 配额硬停（2026-09-21 18:38–18:50 实测，本会话 5 路子代理全部 `token plan
entitlement exhausted` 失败）**：fcu_b001 读手 4 路（21–25 分钟各死一次）＋ shenyue
seg-33 评审员（37.8 分钟）。**失败发生在写盘之后**——磁盘产物完整可用，但收尾 JSON
回报全丢。**新会话开工第一件事是确认配额是否恢复**；未恢复则**只能主代理 solo**
（见 §四 止损阶梯末级），不得再派子代理（派了也是 20+ 分钟零回报）。
⚠️ 并行会话同时在跑 H1／H2／H4／shenyue 多条线，配额是**全会话池**，多线并发会互相挤爆。

**H2 四库真值**（`script/_db_row_mining/_RESUME_H2.md` 为断点入口，台账 `_db_row_mining/mail2d_read_ledger.json`）：

| 库 | 全库 | 已判读 | 剩余 | records（行序） |
|---|---:|---:|---:|---|
| `freebsd-ports` | 191637 | **24000** | **167637** | `[(0,24000)]` fpo_b151–b158 **连续无缝** |
| `freebsd-bugs` | 192683 | **2000** | **190683** | `[(0,500)]` b171 ＋ `[(137970,139470)]` b172+b173+b174+b174e（b174e 在既有区间内，并集不扩张） |
| `freebsd-net` | 73645 | 45000 | 28645 | `[(0,45000)]` fn_b156–b170；queued `[(45000,48000)]` fn_b171 |
| `freebsd-chat` | 43869 | 43869 | **0** | `[(0,43869)]` fch_b137–b150，**已整库闭环** |

⚠️ `_HANDOFF_H2.md` §二 三处数据已过期（ports/net/chat 的「已读 0」皆非）——**以本表为准**，
订正详情见 `_RESUME_H2.md` §一。freebsd-bugs 的 pk 空间年份同质，**下一批直接按 offset 139470 跳**，
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

## 四、子代理编排纪律（09-21 主理人授权：至多 12 路）

| 项 | 值 |
|---|---|
| 子代理/波 | **3–4 路起，上限 12 路**（09-21 主理人解除子代理限制并授权至多 12 路并发；此前上限 3–8） |
| 并发总量 | 跨线不超过 12 路；**在途批每线不超过 1 批** |
| 派发方式 | `Agent` + `run_in_background: true`（并行，返回 agentId 供止损） |
| 止损 | `TaskOutput` 限时；**8 分钟无落盘即 `TaskStop` 并匿名重派一次**（换句柄名，勿复用 agentId）；重派仍败则转主代理 solo 清单 |
| 🔴 禁用 | **`CreateWorkflow` 跑长线**：actor 无 per-ask 超时，实测评审员 7+ 分钟 0 工具调用卡死零产出，脚本无法局部止损。`shenyue/.zcode/workflows/*.dwf.ts` **废弃不执行** |
| 自报数字 | **一律不信**（BATCH-0009 各片自报 206，实测 301） |
| 429 处理 | 记「本轮降为 X 路」，不重试整波，改主代理直读。mail2d 实测 ≥4 路易触发 429（全会话池配额），扩至 12 路时须以落盘条数为准、遇 429 即降 |
| 命名避让 | shenyue 段文件用 `seg-<会话段号>`，防并行会话互相覆盖（BATCH-0024 已发生 seg-01/02 撞名事故） |

**读手/叙述手提示词必写四句**（零产出事故的唯一有效解，本线 16 路零事故实证）：
① 每次 Read 限 100–1200 行；② 每写约 20 行用 Write 增量落盘（覆盖写全文），不得写完才一次性落盘；
③ 转录与产出以行首 pk / oid 为准，禁用行号；④ 回报写出实际落盘行数、宿主/段分布、以及任何「摘要与原文不符」清单。

---

## 五、在途表（2026-09-22 02:0x）

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
| `fbug_b174`（bugs offset 138970，pk 1047667–1048166） | ✅ **全链闭环 `27cfc5725`**：328 条 register COMMITTED（`CL-RM-154743`–`155070`）→ 5 叙述包 **328 行违规 0**（62–140／avg 102.7）→ 宿主 881×275／886×9／887×44 → outline 幂等二跑 +0 → bookkeep 三零 PASS → **提交 +1640 行 = 328×5**，0 删除，仅 3 宿主文件。**16 条读手增量不进本批**，另开 tag | `_NARR_TASK_fbug_b174.md`、`fbug_b174_extra_cand.txt` |
| `fpo_b156`（ports offset 15000，pk 1567555–1570595，n=3000） | ✅ **全链闭环（裹挟入 `529468ce9`）**：702 条 → check PASS（L4 518／L3 184）→ register COMMITTED 702（`CL-RM-155072`–`155773`）→ 9 叙述包 **702 行违规 0**（60–140／avg 89.0）→ 宿主 891×117／892×570／894×3／906×2／907×7／909×3 → **702×5 = 3510 行**。⚠ 提交范围归属错误已留档 | `_NARR_TASK_fpo_b156.md`、`_RESUME_H2.md`「提交裹挟说明」 |
| `fpo_b157`（ports offset **18000**，pk 1570596–1573653，n=3000） | ✅ **全链闭环（`529468ce9`）**：309 条（剔除幽灵 pk **1571399**，源库与 digest 均无）→ register COMMITTED 309（`CL-RM-156915`–`157223`，反查 309/309、四表 join 309）→ 5 叙述包 **309 行违规 0**（63–140／avg 93.0）→ 宿主 891×60／892×220／894×1／906×15／907×7／909×6 → **309×5 = 1545 行** | `review_logs/fpo_b157_cand_p*.txt`、`_check_author_mismatch3.py`、`_fix_b157_attrib_20260921.py` |
| `fbug_b174e`（bugs offset 138970，n=500，b174 pk 区间内 16 条增量） | ✅ **全链闭环 `333434176`**：16 条 register（`CL-RM-160214`–`160229`）→ 正文 16/16 → 2 叙述包 **16 行违规 0**（87–139／avg 115.9）→ 宿主 881×10／887×6（886 零命中）→ outline 88.1+10／88.7+6、幂等二跑 **+0** → bookkeep 三零 PASS → **提交 +80 行恰 = 16×5**，0 删除，仅 2 宿主文件 → audit PASS → 台账 records 不变（区间并集），read_effective 仍 2000 | `_NARR_TASK_fbug_b174e.md`、`_batch_fbug_b174e.json`、`_RESUME_H2.md` §七「b174e 增量闭环」 |
| H2 三批次等级门禁 | ✅ **`audit_evidence_level_labels.py` PASS 错标 0**（原 FAIL 3：b174 等级互串 2 条＋b156 大纲滞后 1 条，已定点修 DB＋大纲，见 `_RESUME_H2.md`） | `_fix_level_20260921_d.py`、`_verify_narrs.py` |
| H2 下一批候选 | ⏸ **`fpo_b159`（offset 24000 n 3000）**——fpo_b158 已占用 `[21000,24000)`，台账实测 `[(0,24000)]` 连续，⚠️ **勿从 21000 起**。宿主沿用 891/892/894/906/907/909（禁 883，b156/b157/b158 三批同画像、2005 年段）。另 `fbug_b175`（offset **139470**）；`fn_b172`（offset **48000**，fn_b171 收口后） | `_batch_fpo_b158.json`、`mail2d_read_ledger.json`、`_RESUME_H2.md`「台账空洞误报已清除」／「b158 候选集对齐」 |
| `fpo_b157` 摘要误归因定点回改 | ✅ **9/9 已回改、回读一致、对齐复验 9/9**：`_check_author_mismatch3.py` 报 27 条「摘要首名与 digest 显示名完全不交」，逐条回 digest 全行复核＝**假阳 18＋真缺陷 9**（姓名误拼 1／姓名补全 1／转述主体错 6／主体＋内容双错 2，后者含 1571789「实谈 RPM 规格书许可，无 SIGSEGV」与 1573347「实为纯提问，Linimon 与 noip 均未出现」）。`_fix_b157_attrib_20260921.py --apply` 只改 `claim.claim_text`＋`evidence.fact_text`，**等级一律不动**：三条转述形态（1571202／1571789／1572671）拟降 L3，回正文原文后**撤回降级**——发件人各有自有动作／观察（Oliver 自述不能测 samba 并自行发问／Robin 自述已翻看 Gentoo ebuild 发现 LICENSE 声明／Oliver 自述已包安装并亲验 vchkpw 正常），符合 L4 判据；且大纲叙述句更完整且已标「转述」，故**大纲零改动**，等级三方一致。回改后全库等级门禁复跑 **PASS**（137237 块头／错标 0） | `_fix_b157_attrib_20260921.py`、`_check_author_mismatch3.py`、`_RESUME_H2.md` §七「b157 摘要误归因定点回改」 |
| `fpo_b158` 开批（ports offset **21000** n 3000） | 🔄 **已开批、6 读手在途**：dump 3000 行 pk **1573654–1576713**（**全 2005 年** 2005-01-01~12-31、容器行 0）→ 实测为本库**史料密度最高一批**：`perl symlinks in /usr/bin will be gone`×76、`New port with maintainer ports@`×50、`HEADS UP: pkg-plist strict enforcement`×41、`INDEX build failed`×34、`Why does everybody switch to dynamic plists?`×21、`bsd.sites.mk` 可覆写提案×17、`pkg_create` 新功能×15、PostgreSQL 端口拆分×14、`local_startup` rc.d MFC×14；噪声类实测 93 条占 3.1%。宿主沿用 b156/b157 六键 891/892/894/906/907/909（禁 883）。6 分片各 500 行约 241–247 KB | `_batch_fpo_b158.json`（pk_range 已补）、`_READ_TASK_fpo_b158.md`、`review_logs/fpo_b158_digest_part1..6.txt` |
| b174 等级误判 2 条回改 | ✅ **CL-RM-154885／154921 由 L3 改 L4**，回读 6/6、audit **PASS**（137802 块头／错标 0）。**上次的等级互串修复只改对了一半**——154884 改对、154885 改错。本次逐条回 digest＋摘要＋**大纲叙述句**三方比对后定性：154884 叙述含 Khera 自有动作（给 lo0 加别名绕过并 `netstat -p ip` 验证）故维持 L4；154885 是 Henrich 自有调试、154921 是 Grillo 自有经历与建议，均应为 L4。摘要文本不动 | `_fix_b174_levels_20260921.py`、`_RESUME_H2.md` §七「b174 等级误判 2 条回改」 |
| `fdoc_b001`／`fstab_b001` | ⏸ 未预建（P1，待 P0 两库推进后再派） | — |
| H3 `fhk_b021`（hackers offset 40000，pk 1312727–1314738） | ✅ **完全收口**：候选 **255 条**（原 256，剔除 1312976——from/subject/thread_refs 全空且 message_id 为合成号 `<no-id-...>`，库中 `status='rejected'`）→ 摘要对位订正 **20 改＋1 剔除**＋叙述改 **7 条** → outline **255 块入 6 宿主**（106.9 +237／124.17 +4／124.13 +2／164.8 +4／158.8 +4／106.7 +4）→ bookkeep 缺块 0／claim_id 不符 0／重复 0 → 等级门禁全库 **PASS**（3279 md／134282 抬头／0 错／0 悬空）→ commit `54119d159` → 台账 `freebsd-hackers` **42000** | `script/_db_row_mining/review_logs/fhk_b021_*`、`_fix_cand_fhk_b021_p2.py`、`_fix_narr_fhk_b021_pn.py`、`_outline_fhk_b021.py` |
| H3 `fcu_b001`（current offset 0，pk 2462–1025423，容器行 301/2000） | 🔄 **续读 3 路已派（19:20）**：p1（剩 305 行，续 `pk>6324`）／p3（剩 100 行，续 `pk>1024811`）／p4（剩 400 行，续 `pk>1025023`），**p2 已读完**；追加写勿覆盖旧行（旧 8／253／125／26 条）。⚠ p1 大部分行落在容器行清单内，候选数不会高属正常。句柄见 `_DISPATCH_20260921_1920.json` | `_READ_TASK_fcu_b001.md`（§十 断点表）、`review_logs/fcu_b001_candidates_part1..4.txt` |
| H3 `fhk_b022`（hackers offset 42000，pk 1314739–1316740） | 🔄 **已预建＋4 读手已派（19:20）**：spec `_batch_fhk_b022.json`（已补 `pk_range`／`line_date=2026-09-18`／`containers=0`）、dump 2000 行、digest 拆 4 份各 500 行、任务书 `_READ_TASK_fhk_b022.md`（含 §五.1 摘要归属铁律）。**本批全为 2013 年、容器行 0**（判据实测：0 行符合「≥3 处行首 `From `＋`From owner-`＋>20KB」；该判据已在 fcu_b001 上复算 301/301 完全吻合，可复用）。p1 1314739–1315238／p2 1315239–1315738／p3 1315739–1316240／p4 1316241–1316740 | `_DISPATCH_20260921_1920.json`、`review_logs/fhk_b022_digest_part1..4.txt` |

---

### 五之补 · 2026-09-22 02:0x 波次（本节取代上表中 H3 各行的在途描述）

| 项 | 状态 | 句柄／产物 |
|---|---|---|
| `fcu_b001`（current offset 0） | ✅ **完全收口**：565 块入 5 宿主，commit `fe4eb1aff`＋`034401026`，台账 0→2000 | `script/_db_row_mining/_H3_PROGRESS.md` |
| `fdoc_b001`（doc offset 0） | ✅ **完全收口**：297 块入 7 宿主（100.18 +283／106.9 +5／122.9 +3／124.13 +2／164.8 +2／124.17 +1／105.8 +1），outline 幂等二跑 +0、bookkeep 三零 PASS、等级门禁 PASS、commit `8e330dc09` +1485 行，台账 0→2000 | `_H3_PROGRESS.md`、`_tmpaudit/fdoc_b001_pn.txt`（0 命中） |
| `fstb_b001`（stable offset 0，pk 2875–2576641） | 🔄 **读手＋落库收口**（commit `61c6e6b63`）：8 半份 → 516 条（L4 501／L3 15，收率 25.8%）、违规 0、register COMMITTED 516 seq 160693、body 516/516（609 KB）、split N=8 | `review_logs/fstb_b001_narrpkg_p1..p8.txt`＋`_cands_body_p1..p8.txt` |
| `fstb_b001` 叙述 | 🔄 **8 路叙述手在途（02:0x 派）**。产出 `fstb_b001_narr_p1..p8.tsv`，**merge 前须改名为 `fstb_b001_mount_narr_p1..p8.tsv`** | 句柄 agent_f56c5632(p1)／014ca2a7(p2)／93affcc4(p3)／7d3fcf27(p4)／fac61ff7(p5)／b0652d33(p6)／7b871456(p7)／031d31d2(p8) |
| `fhk_b022`（hackers offset 42000） | 🔄 **叙述已 merge 504 条违规 0**（宿主 1588×342／1229×99／1069×46／1058×11／12413×6，60–140／avg 105.2）；**专名门禁 41 命中已分流：12 假阳保留／29 真臆造在订正** | `review_logs/fhk_b022_mount_narr_p1..p7.tsv`、`_tmpaudit/fhk_b022_pn.txt`、订正句柄 agent_a02105f4 |
| `fhk_b022` 专名订正 29 条 | 🔄 **1 路在途**。12 假阳 pk（勿动）：1314885/1315205/1315348/1315349/1315436/1315474/1315619/1315701/1315802/1316141/1316349/1316699；29 待改 pk：1314792/1314833/1314973/1314981/1314984/1314986(p1)、1315052/1315182/1315206/1315244/1315256/1315287(p2)、1315443/1315566/1315574(p3)、1315742/1315790(p4)、1316144(p5)、1316170/1316293/1316383/1316449/1316505(p6)、1316560/1316649/1316651/1316688/1316704/1316722(p7) | 订正后：`_merge_narr.py fhk_b022 7 <13 键>` → `_audit_narr_propernoun.py fhk_b022 1..7` → outline→bookkeep→门禁→commit |
| 下一批 4 spec 预建（02:0x） | ✅ **已按各自源库建 spec＋dump＋digest 4 份＋32 半份，四批容器行均 0**：`fhk_b023` offset 44000 pk 1316741–1318740／`fcu_b002` offset 2000 pk 1025424–1027444／`fdoc_b002` offset 2000 pk 1108539–1110552／`fstb_b002` offset 2000 pk 2576642–2578641。宿主 13 键。**注意 `--lib` 一次调用只认一个值**，已改由 `_split_halves_p2.py` 配套 | `_prep_batches.py`（已修位参解析 bug）、`_split_halves_p2.py`、`_prep_next4.log` |
| `fcu_b002`／`fdoc_b002` 读手 | 🔄 **3 路在途（02:0x）**：fcu_b002 part1a（agent_8675a290）、part1b（agent_33957cb9）、fdoc_b002 part1a（agent_1a17ef57）；各 250 行，产出 `_candidates_part1a/b.txt` | `_READ_TASK_fcu_b001.md` 口径复用 |
| shenyue `BATCH-0028` | ⏸ **并行会话在途，勿双写**（B pos 551–600） | `shenyue/review/.runs/BATCH-0028/` |

**止损指令**：任一子代理 8 分钟无落盘即 `TaskStop` 并重派同一分件；全败则该分件转主代理直读。

---

## 六、长尾队列总账

| 序 | 战线 | 规模 | 单批 | 剩余批数 |
|---|---|---:|---|---:|
| **P0** | H3 `freebsd-hackers` | 159463 封 | 2000/批 | ≈80（b021 已收口，下一批 b022 offset 42000） |
| **P0** | H3 `freebsd-current` | 205027 封 | 2000/批 | ≈103（b001 已预建、在读 412 条待续） |
| **P1** | H3 `freebsd-doc` | 72663 封 | 2000/批 | ≈37 |
| **P1** | H3 `freebsd-stable` | 72164 封 | 2000/批 | ≈37 |
| **P1** | Linux 邮件列表价值反推 | 九库 2,540,000 封（未处理） | 单批约 200-500 封判读 | 约 5-10 批（linux-man 优先，约 46 页高价值） |
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
| 🔴 **体检脚本报零不可信** | `_check_author_mismatch2.py` 的 `latin_tokens()` 用 `re.split(r"[^a-z0-9.'\-]+",s)` 配 `not t.strip(".'-")` 过滤，实测对**所有**输入返回 `[]` → 3000 行全落「无法判定」而报「0 不符」（假阴性）。改 `re.findall(r"[a-z0-9]+",s)` 后真出 27 条。**任何报零的体检脚本先对一个已知阳性样本验证** |
| 摘要名提取的 CJK 边界 | `\u3000-\uFFEF` 漏 U+FF0E（全角句点），`Peter Czanik报告…` 句点被吞进人名。须 `ord()` 逐字判（3000–30FF／4E00–9FFF／FF00–FFF0） |
| digest 显示名无右括号 | `(Oliver Lehmann` 只有左括号，`\(([^()]*)\)` 匹配不到 → `find("(")`＋`rstrip(")").strip()` |
| 回改脚本取「旧文本」须查 DB | 候选文件把摘要截到 80 字，DB 存全文（1570990 全文 78 字含「…pure virtual method called」被截）→ `got_text == old` 断言必拦 |
| 修 `claim` 只改文本时大纲安全 | **前提：等级不动**。动等级则大纲块头「证据等级：Lx」与纪律句必须同步，否则等级门禁立刻 FAIL（见 §五「块头等级错标」）。判据写进回改脚本注释留档 |
| 转述≠必然降 L3 | L4 判据是「发件人自述自有行为／经验／判断」——转发他人内容**之外**还有自己的动作即仍为 L4。三条初判拟降 L3 经回正文撤回降级（见 §五 b157 回改行） |
| 体检脚本读候选文件而非 DB | `_check_author_mismatch3.py` 修完 DB 后仍报同一批「不交」，因候选文件是 register 前历史输入不回写。验修改须回 DB 比对 |
| 🔴 **行序 offset 记账勿靠推理相邻关系** | b157 spec offset 曾被误判「18000 与 b156 的 `[15000,18000)` 重叠」而改 21000，凭空造出 18000–21000「空洞」。实测两批 digest pk 端点 b156=1567555–1570595／b157=1570596–1573653 **完全连续**，实为相邻。若照误记从 24000 开 b158 会**真跳过 3000 行未读**。判定相邻只能实测 dump 产物 pk 端点——pk 是稀疏 bigint id，`offset+n` 与 pk 区间无可推导关系（实测 pk 跨度 3023/3041/3058 对应同为 3000 行） |
| 🔴 **判等级须三方比对，叙述句优先** | 等级门禁只能证明「DB 与大纲块头一致」，**不能证明两者都对**。b174 上次等级互串修复只改对一半（154884 改对、154885 改错），因门禁 PASS 长期不被发现。判等级时**大纲叙述句优先于 digest 截断正文与摘要**——叙述句由读过完整正文的叙述手所写，能看到 digest 预览截掉的部分（154884 只看 digest 会误判纯转述 L3，叙述句里的「给 lo0 加别名绕过并 netstat 验证」才是 L4 依据） |
| 修等级须一次改三处 | `claim.evidence_level` ＋ 大纲块头「证据等级：Lx」＋ 块尾纪律句。漏改纪律句不触发等级门禁（只查块头），但会留下语义自相矛盾的块 |
| 🔴 **`_merge_narr.py` 长度/禁字符是「非阻断级」** | 越限只打印不拦，**照样写盘**。fhk_b022 p2 实测 17 条超长（142–209）全落盘，须事后按 `_fix_narr_fhk_b022_p2b.py` 定点压缩再 merge。**阻断级**只有：缺文件、CRLF。`_merge_parts.py` 同理：**摘要越限（含禁字符）与尾标点是非阻断**，缺文件／BOM／CRLF／字段数／等级非法／pk 越界／跨份重复才是阻断 |
| 🔴 **duckdb `body` 列本身被截断** | freebsd-hackers 732 封恰在 1395–1405 字符（max 1703711）、freebsd-stable 274、freebsd-doc 217、freebsd-current 748。「全文正文」并非全文。**专名门禁分流判据**：命中且能在 `body`（精确或忽略大小写）找到 → 假阳保留；只在 `from_name`/`subject` 找到 → 假阳保留；`len(body)>=1395` → **截断假阳保留**；`len(body)<1390` 且三处皆无 → **真臆造，改写** |
| 🔴 **`_prep_batches.py` 一次只认一个 `--lib`** | `LIB` 在 `enumerate` 循环里被赋值最后一次，四库同批会全建到同一个源库（`dump`／`register` 就读错库）。**每库单独调用**。位参解析 bug 已修（原 `args=[a for a in sys.argv[1:] if not a.startswith("--")]` 把 `--lib`/`--hosts` 的**值**当 spec 喂给 `split(":")` → `ValueError: not enough values to unpack`）；预建后**必查 spec 的 `lib` 字段** |
| 🔴 **中文长度必须实测，不得手估** | 手估系统性偏低 5–40 字：fhk_b022 p2 四次 precheck 连续失败（141/145/180/151 → 142/153/141 → 147/152/141 → 141），每次按 `len()` 实印值再压。**压缩纪律**：只删枝节从句，绝不删版本号／路径／宏名／人名／等级归属；宁删重复标识符也不要改错标识符（本轮曾把 `kmem_map` 误打成 `kem_mem`，即臆造专名） |
| digest 分件 500 行不稳 → 拆 250 行半份 | `fhk_b022` p1/p2/p3 三份 500 行零落盘（读完用 1,021,646 token／947 秒后停在「Let me write the output file incrementally」）。**250 行/份是稳态**：`_split_halves_p1.py`（fhk_b022/fdoc_b001/fstb_b001）、`_split_halves_p2.py`（下一批四批，按行切） |
| 叙述手「派完即失联」须以磁盘为准 | 8 路叙述手 65 分钟零落盘即算死（不是超时，是进程已不在任务注册表）。**硬判据：开工后 5 分钟内必须有一次首落盘**（写前 8–10 条），之后每 10 条覆盖写全文。句柄不存在（`TaskStop` 报 `No task found`）＝已随会话中断消亡，直接重派即可 |
| 台账是 `spec-only` 口径 | `_build_read_ledger.py` 的游标从 `_batch_*.json` spec 推进，**spec 预建即推游标**，不等于 outline 已提交。预建下一批会把「已判读」抬高，勿据此宣称覆盖率。判据是 `review_logs/<tag>_claim_map.json` 是否存在 |

---

## 八、待主理人裁定（4 项，均已实测取证，取证详见 `_PLAN_20260921.md` §五）

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
4. **pk 1573347（CL-RM-157167）应否改 `status='rejected'`**：摘要误归因回改时查明本条实为 Marco van de Voort 的**两条纯提问**
   （「is it evil to leave behind .cfg.sample files?」「如何改 pkg_add 注册目录?」），不含量化或结论性陈述，
   本不该收录。是否比照 `fhk_b021` 剔除 pk 1312976 的先例改 `status='rejected'` 并从大纲移除对应块？
   **已回改摘要文本、未改 status，等裁定。**（`_fix_b157_attrib_20260921.py` 理由串已标 ⚠）
