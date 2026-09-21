# 长线总账（Live）· 防会话中断唯一入口

> **读这一份就够**：本文件是**三线**（shenyue 复核 / mail2d H3 / mail2d H1）的**唯一长期入口**，
> 新会话读到本文件即可续接，无须任何先前对话记忆。
> 细节归档（SOP 全文、裁定取证、坑速查完整版）在 `_PLAN_20260921.md`，本文件只留**活数据与命令**。
> 上游分线规程：`shenyue/review/_LONGRUN_PLAN.md`（复核线）、`script/_db_row_mining/_H3_RESUME.md`（H3 断点续跑书）、
> `script/_db_row_mining/_H1_LONGTERM.md`（H1 长线档案，含 H1 全套 SOP 与宿主分派口径）。
> Linux 邮件列表价值反推线（H6）：`03-原始史料库/11-邮件列表史料/05-linux-kernel/mining/02-遍历留痕/10-价值反推排序与选封管线.md`（价值反推排序+选封管线规程+五层面去重定义）
> **冲突时以台账实测值为准，永不以本文档数字为准**（本文档是台账的副本，已实测漂移 3 次，见 §七）。

---

## 〇、一句话现状（2026-09-22 02:5x 实测，本轮：b175（313 claims）与 b159（395 claims）候选已注册入库、各 6 路叙述手在途；b160 读手 9/12 回报；b176／b161 预建 dump 完成）

| 线 | 游标（台账实测） | 下一批 |
|---|---|---|
| **shenyue 复核** | A 类 **692/692 全闭环**（16 批）｜B 类 **550/748**（0027 已落账 seq 27）｜C 类 **0/1972** | `BATCH-0028`（B pos 551–600，O-2082 起） |
| **mail2d H2** | `freebsd-bugs` **2000/192683**（b171＋b172/b173/b174/b174e，b174e 落在既有区间内不扩张）｜`-ports` **24000/191637**（b151–b158，`[(0,24000)]` **连续无缝**）｜`-net` **45000/73645**｜`-chat` **43869/43869 已整库闭环** | **bugs 四批＋ports 三批全链闭环**：`6809bb8a2`／`cee1e72ec`／`27cfc5725`／`333434176`／`529468ce9`（b156+b157 裹挟，+5055 行）／**`1029cb38c`**（b158，+2240 行＝448×5）；audit **PASS 错标 0**（140040 块头）。**b158 期间两起缺陷已处置并写死流程**：① merge 抢在 4 路读手回报前执行→候选 463 实应 449（63 条改 `status='rejected'`、49 条补 register）；② `_outline_*.py` 块头等级取自 `candidates.txt` 而 register 按 `source_id` 幂等静默保留陈旧等级→3 条 DB L4→L3 定点回改。**本轮（09-22 02:2x–02:5x）**：`fbug_b175` **313 claims 已注册**（`CL-RM-161638–161949`，L4 217／L3 96，摘要 28–78 字，四表 join 313 命中）＋ `fpo_b159` **395 claims 已注册**（`CL-RM-161950–162344`，L4 339／L3 56，摘要 35–80 字）；两批正文已生成、各 6 路叙述手在途（b175 p1–p6、b159 p1–p4 已派）。**b175 再度实证明细**：p4 读手在 merge 后 2 分钟又写 1 行（pk 1048473），首 merge 只收 312；重跑 merge（313）＋register 补录，**register 幂等实测跳过 312／增量写 1／join 313 全命中**——幂等补录通道验证可用。`fpo_b160` 读手 **9/12 回报**（p1 40／p2 35／p3 37／p4 42／p5 32／p6 33／p7 31／p8 35／p9 41，均 `_gate_cand.py` PASS；**p7 自 34 收严至 31、p8 自 62 收严至 35**，自行发现臆造风险后删除；🔴 **p5 首次静默死亡**——读完 250 行只写 23 条即中断，重派后 32 条并纠出前件 3 处发件人错配 1580816／1580832／1580836）；p10–p12 在途。已预建：**`fbug_b176`**（offset 139970，pk 1048668–1049168，全 1995，容器 0）、**`fpo_b161`**（offset 30000，pk 1582771–1585797，全 2006，容器 0），两批 pk 均与上批端点紧贴、单调递增、跨行重复 0 |
| **mail2d H3** | 四库 **50000/551317（9.07%）**：`freebsd-hackers` **44000/201463**（fhk_b021 `54119d159`＋fhk_b022 `de2f33277`）｜`-current` **2000**（fcu_b001 `fe4eb1aff`+`034401026`）｜`-doc` **2000**（fdoc_b001 `8e330dc09`）｜`-stable` **2000**（**fstb_b001 全链收口 `c90d1af83`**：516 块入 7 宿主 +2578 行） | **读手波次在途（02:4x 派）**：3 路 `fhk_b023` part4a/4b、`fdoc_b002` part4b（`fcu_b002` 已 **8/8 齐 440 条**；`fdoc_b002` 388＋4b 在途；`fhk_b023` 199＋2 片在途）。**`fstb_b002` 读手已解禁**（fstb_b001 已收口）。四批 spec＋digest＋32 半份已预建：`fhk_b023`(44000→，pk 1316741–1318740)、`fcu_b002`(2000→，1025424–1027444，**15 键宿主**)、`fdoc_b002`(2000→，1108539–1110552)、`fstb_b002`(2000→，2576642–2578641)，四批容器行均 **0** |
| **mail2d H1** | `freebsd-questions` **76000/472235（16.10%）**；**37 批已提交**，b038 在途 | `fq_b038` 叙述 5 包 3 路在途（候选 145 已落库 CL-RM-153855–153999）→ `fq_b039` |
| **mail2d H5**（200K 派发线，`_h5_state.json` 28 库 101 批） | **全库闭环 10 个**（x11/ipfw/desktop/cu/acpi/smp/i386/sparc64/ppc＋tech-pkg 三批＋freebsd-ppc 三批） | tech-pkg 批1 `1c3015051`（1141 条）＋批2 `b34760350`（1477 条）＋**批3 `h5tp_b528_3` `1204cc175`（152 条 CL-RM-161258–161409，1892=144／1852=8）已 committed**，+760＝152×5、幂等二跑 +0、bookkeep PASS、audit PASS 140815 块头 0 错标；**追溯订正 `4b3958771`**（叙述手 02:08 回报晚于提交，284538 由 185.2 改挂 189.2、284581 叙述删不可核断言，外科改挂 +6/−6）；🔴 **「漏读缺口」经比对判定为伪缺口，已整批 purge 回滚**：库首 1500 行（offset 0–1499，pk 270703–272459）并非未读——2026-09-11 另一会话已处理并 152 块入纲 **179.2**（commit `85a71de45` 及其前序提交）；本轮误判后建批 `h5tp_b528_0`（3 读手 374 条、register 281 条 CL-RM-162346–162626），比对发现 **93 条与 179.2 已入纲块完全重复**（同 pk，仅 claim 编号与宿主不同），继续推进会造 93 个跨章重复块并把同一时间窗拆散两章，故 `_purge_batch.py h5tp_b528_0 281 --apply` 四表全清（anchor 残留 0、库内 MAX 回落 162345），179.2 一行未动；✅ **tech-pkg 整库闭环终态＝13931 封全量、claim 2922 条＝入纲块 2922**（179.2=152／189.2=2666／185.2=48／187.6=37／188.2=19，零孤儿零重复），**直接转余下 18 库**；教训＝建批前必须先全库核对 claim 与 ROW_MINE 块的实际 pk 覆盖、不能只信本线 offset 游标；入口 `script/_db_row_mining/_HANDOFF_H5.md`（§10.1 台账＋§10.2 源数据缺陷＋§10.3 流程纪律＋§10.4 伪缺口教训＋§10.5 合并后重写纪律）＋记忆 `h5-longhaul-200k-dispatch-20260921` |
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
| H2 下一批候选 | 🟡 **`fpo_b159`（offset 24000 n 3000）已开批、12 读手在途（09-22 派）**——pk **1576714–1579742**（与 b158 端点 1576713 紧贴）、全 2005 年（03×959／05×699／06×693／11×644）、容器行 0；12 分片各 250 行约 121 KB、pk 完全不相交。🔴 **12 路全部回报前不得 merge**（b158 教训：merge 抢在 4 路读手回报前执行→候选 463 实应 449）。另 **`fbug_b175`（offset 139470 n 500）已开批待派**（pk 1048167–1048667 紧贴 b174 端点、全 1995 年 06×416／07×82、容器行 0、5 分片各 100 行约 47 KB 一次 Read 即可、任务书已写；预期收率 ≈65%）；`fn_b172`（offset **48000**，fn_b171 收口后） | `_batch_fpo_b159.json`、`_READ_TASK_fpo_b159.md`、`_READ_TASK_fbug_b175.md`、`_profile_batch.py`、`_RESUME_H2.md` §七 |
| `fpo_b157` 摘要误归因定点回改 | ✅ **9/9 已回改、回读一致、对齐复验 9/9**：`_check_author_mismatch3.py` 报 27 条「摘要首名与 digest 显示名完全不交」，逐条回 digest 全行复核＝**假阳 18＋真缺陷 9**（姓名误拼 1／姓名补全 1／转述主体错 6／主体＋内容双错 2，后者含 1571789「实谈 RPM 规格书许可，无 SIGSEGV」与 1573347「实为纯提问，Linimon 与 noip 均未出现」）。`_fix_b157_attrib_20260921.py --apply` 只改 `claim.claim_text`＋`evidence.fact_text`，**等级一律不动**：三条转述形态（1571202／1571789／1572671）拟降 L3，回正文原文后**撤回降级**——发件人各有自有动作／观察（Oliver 自述不能测 samba 并自行发问／Robin 自述已翻看 Gentoo ebuild 发现 LICENSE 声明／Oliver 自述已包安装并亲验 vchkpw 正常），符合 L4 判据；且大纲叙述句更完整且已标「转述」，故**大纲零改动**，等级三方一致。回改后全库等级门禁复跑 **PASS**（137237 块头／错标 0） | `_fix_b157_attrib_20260921.py`、`_check_author_mismatch3.py`、`_RESUME_H2.md` §七「b157 摘要误归因定点回改」 |
| `fpo_b158`（ports offset **21000**，pk 1573654–1576713，n=3000） | ✅ **全链闭环 `1029cb38c`**：候选 **448 条**（初判 463 → 对齐 449 → 撤臆造 448）→ register（`CL-RM-160230`–`161257`，含增量 49 条 `161209`–`161257`）→ 正文 448/448 → **3 条等级回改 DB L4→L3**（`160591`／`160599`／`160629`）→ 8 叙述包 **448 行违规 0** → 宿主 **891×0／892×369／894×43／906×2／907×19／909×15** → outline 89.2+1845／89.4+215／90.7+95／90.9+75／90.6+10、幂等二跑 **+0** → bookkeep 三零 PASS → **提交 +2240 行恰 = 448×5**，0 删除，仅 5 宿主文件 → audit **PASS**（140040 块头／错标 0）→ 台账 ports `read_effective 24000`、records `[(0,24000)]` **单段连续**。本批为**史料密度最高一批**：`perl symlinks in /usr/bin will be gone`×76、`New port with maintainer ports@`×50、`HEADS UP: pkg-plist strict enforcement`×41、`INDEX build failed`×34、`Why does everybody switch to dynamic plists?`×21、`bsd.sites.mk` 可覆写提案×17；噪声类 93 条占 3.1%。**891（89.1 制度初创节）零命中**——若 b159 亦零命中属正常 | `_batch_fpo_b158.json`、`_RESUME_H2.md` §七「fpo_b158 全链闭环」 |
| **b158 候选集对齐回改**（2026-09-21 23:2x） | 🔴 **缺陷**：`_s62_merge_multi.py fpo_b158 6` 于 22:44 执行时读手 p2/p3/p5 **仍在写分片**（mtime 22:51／22:47／22:45 均晚于合并时刻），抓到的是分片中途快照——落盘 **463** 行，六片最终判读并集实测 **449** 行。**差集双向**：63 行在 463 内但读手重判后撤回（摘要归因错配＋纯寒暄＋空正文，抽样 10 条回正文验证撤回有据）；49 行读手在合并后才新增判收。**处置** `_reconcile_b158_withdrawn.py --apply`：撤回 63 条**不 DELETE 改 `claim.status='rejected'`**（库内既有 3733 行 rejected，先例 fhk_b021 pk 1312976；`_mail2d_run_batch.py` 与 `audit_evidence_level_labels.py` **均不按 status 过滤**故门禁不受影响，且留档可回溯）；candidates 重建 449 行、register 补入 49 条、claim_map 裁孤儿 → 449。再撤 1 条臆造（pk 1575968）→ **448**。**须写死进流程的三条**：① 读手未全部回报前不得 merge 候选（等 completion 齐＋分片 mtime 静止）；② 读手自报数字一律不信（本轮 p5 自报 66 实 52、p7 自报 66 **文件不存在**、叙述手自报「越限 0」实测 20 条越限）；③ 不对写盘中的分片做抢救性改写（先 TaskStop＋核实 mtime 静止） | `_reconcile_b158_withdrawn.py`、`_reject_b158_noinv.py`、`_salvage_b158_narr.py`、`_split_b158_gaps.py`、`_redist_b158_narr.py`、`_RESUME_H2.md` §七「b158 候选集对齐」 |
| **register 幂等保留陈旧等级／摘要**（新坑，b158 发现） | 🔴 **`_outline_<tag>.py` 块头等级取自 `candidates.txt`（第 61–64 行）而非 claim 表**，故两者一旦不一致，audit 必 FAIL。本批首 register 时候选还是 463 的半截快照，把 3 条写成 L4；读手其后重判 L3；而 `register` 幂等键是 `source_id` + `content_hash`，**改等级不重算 hash，故二次 register 静默 SKIPPED**，DB 永远停在首次值 → audit FAIL 3 处「块头 ≠ claim.evidence_level」。**处置** `_fix_b158_levels.py --apply`：**改 DB 侧**（DB 是旧的那一边），outline **不动**（其块头与 TAIL 纪律句本就按 candidates.txt 的 L3 生成，是对的）。**教训**：读手重判发生在首 register 之后时，必须手工比对 `candidates.txt` 与 `claim.evidence_level` 并回改 DB——register 的 source_id 幂等会静默保留陈旧等级与摘要 | `_fix_b158_levels.py`、`_find_level_mismatch.py` |
| **b158 叙述禁字体检遗漏 `\` 与 `|`** | 🔴 `_merge_narr.py` 除 `「」*` 外**也禁 `|`**（b157 教训记的是「`\|` 为 candidates 分隔符故不查」，但 mount_narr 的叙述列确实要查）。本批 3 条踩中并已改写：`1574616`（`pre\|post-deinstall` → 「pre-deinstall 与 post-deinstall」）、`1575789`（`(i && j || k)` → 「加括号与不加括号的与或表达式」）、`1576445`（正则字面量 `m/\.$/` → 「将匹配尾句号的规则由 =~ 改为 !~」）；另 2 条长度越界（`1575816` 58 字、`1575968` 56 字）一并修正。**臆造条目删而非改（b157 先例第二次适用）**：pk 1575968 正文窗内只有 `Holger Kipp writes: > …` 引用块与 Kipp 自己论述，**发件人 Matthias Andree 本人立场在 digest 与 body 窗口内都不可见**，叙述手却写成「Andree 反驳 Kipp 称该单一符号链接确有必要」——逻辑自相矛盾，按先例删行不改写，`reviewed_by='b158-noinv-no-authorial-content-20260922'` | `_scan_narr_gate.py`、`_chk_two_rows.py`、`_reject_b158_noinv.py` |
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
| `fstb_b001`（stable offset 0，pk 2876–2576641） | ✅ **完全收口（commit `c90d1af83`，7 文件 +2578 行）**：516 块入 7 宿主（100.18 +381／88.5 +56／122.9 +48／106.9 +22／124.13 +6／105.8 +2／158.8 +1）、叙述 60–140／avg 96.4／违规 0、outline 幂等二跑 +0、bookkeep 三零 PASS、等级门禁 PASS（141440 块头／0 错标）、台账 0→2000。8 半份 → 516 条（L4 501／L3 15，25.8%）、register COMMITTED 516 seq 160693、body 516/516 | `_H3_PROGRESS.md` §7.6、`_fix_pn_fstb_b001.py`、`review_logs/fstb_b001_pn_triage.md` |
| `fstb_b001` 专名门禁（判据定形） | ✅ **48 命中 → 18 命中，18 条全为假阳性，30 条真臆造清零**（27 条 `_fix_pn_fstb_b001.py` 定点改写＋3 条叙述手自清）。四条判据＋**新判据「路径拼接假阳性」**（token 正则把整条路径当一个词：`2575344` 的 `usr/compat/linux/lib/ld-linux.so.1` 正文各组件俱全只是顺序不同）见 `_H3_PROGRESS.md` §7.6 | `_tmpaudit/fstb_b001_pn_v3.txt` |
| `fhk_b022`（hackers offset 42000） | ✅ **完全收口（commit `de2f33277`，+2520 行＝504×5）**：504 块入 5 宿主（158.8 +342／122.9 +99／106.9 +46／105.8 +11／124.13 +6）、专名 41 命中分流 12 假阳／29 真臆造改写、bookkeep 三零 PASS、等级门禁 PASS、台账 42000→44000 | `_H3_PROGRESS.md` |
| 下一批 4 spec 预建 | ✅ **已按各自源库建 spec＋dump＋digest 4 份＋32 半份，四批容器行均 0**：`fhk_b023` offset 44000 pk 1316741–1318740／`fcu_b002` offset 2000 pk 1025424–1027444／`fdoc_b002` offset 2000 pk 1108539–1110552／`fstb_b002` offset 2000 pk 2576642–2578641。宿主 13 键（`fcu_b002` 为 **15 键**）。**`--lib` 一次调用只认一个值** | `_prep_batches.py`、`_split_halves_p2.py`、`_prep_next4.log` |
| `fcu_b002` 读手 | ✅ **8/8 齐，440 条**。待 `_merge_parts.py fcu_b002 4` → `check` → `register` → `body` → `_split_narr` → 派叙述手（**15 键宿主**，2008–2009 年段） | `review_logs/fcu_b002_candidates_part1a..4b.txt` |
| `fdoc_b002` 读手 | 🔄 **7/8（388 条）**，part4b 在途（agent_14016c91） | `review_logs/fdoc_b002_candidates_part1a..4a.txt` |
| `fhk_b023` 读手 | 🔄 **6/8（199 条）**，part4a（agent_6ddf8724）／part4b（agent_5ca2e462）在途；本批 2013–2014 收口期密度低（10.8–14.8%） | `review_logs/fhk_b023_candidates_part1a..3b.txt` |
| `fstb_b002` 读手 | 🆕 **已解禁**（fstb_b001 已收口），spec 已建，待派 8 半份 | `_batch_fstb_b002.json` |
| shenyue `BATCH-0028/0029/0030` | ⏸ **并行会话在途，勿双写**（0030 已见 `.partial-B-BATCH-0030.md`／`.skeleton-B-BATCH-0030.md`） | `shenyue/review/.runs/BATCH-00*/` |

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
| 🔴 **`_outline_<tag>.py` 块头等级取自 `candidates.txt` 而非 claim 表** | 第 61–64 行按 `pk\|LEVEL\|摘要` 读候选文件，故候选与 DB 一旦不一致 audit 必 FAIL。**register 幂等键是 `source_id` + `content_hash`，改等级不重算 hash → 二次 register 静默 SKIPPED，DB 停在首次值**。b158 因此 audit FAIL 3 处（首 register 抓的是 463 半截快照写成 L4，读手其后重判 L3）。**处置**：读手重判在首 register 之后发生时，手工比 `candidates.txt` 与 `claim.evidence_level` 并**回改 DB**（DB 是旧的一侧），outline 不动——其块头与 TAIL 本就按 candidates.txt 生成 |
| 🔴 **读手未全部回报前不得 merge 候选** | b158 的 `_s62_merge_multi.py fpo_b158 6` 在 22:44 执行时 p2/p3/p5 仍在写分片（mtime 22:51／22:47／22:45），抓到中途快照→落盘 463、最终并集 449，**63 条错配行落库、49 条好行漏收**。判定：等所有读手 completion 通知齐＋分片 `mtime` 静止后再 merge。配套两条：**读手自报数字一律不信**（p5 自报 66 实 52、p7 自报 66 文件不存在、叙述手自报「越限 0」实测 20 条越限）；**不对写盘中的分片做抢救性改写**（先 TaskStop＋核实 mtime 静止） |
| 🔴 **`_merge_narr.py` 禁字符集含 `\|`，与 candidates 分隔符同名易漏查** | 除 `「」*` 外叙述列**也禁 `\|`**（b157 教训记「`\|` 是 candidates 分隔符故不查」，但 mount_narr 叙述列确实要查）；正则字面量 `\`（如 `m/\.$/`）同样踩线。b158 三条踩中（`1574616`／`1575789`／`1576445`）须改写为散文表述。另 `_merge_narr.py` 越限只打印不拦、照样写盘（见上行），故派单后必用 `_scan_narr_gate.py` 全库扫描，勿信自报 |
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
