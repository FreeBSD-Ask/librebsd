# TUHS Wiki 入库 Claim 库与大纲实现方案

> 日期：2026-10-26
> 输入库：`03-原始史料库/16-TUHS-Wiki史料/tuhs_wiki.duckdb`（591 页、39,534 块、14,947,333 字符）
> 输出：`04-现代研究文献/historical_claims.duckdb` 与 `05-卷册大纲/` 的 ROW_MINE 块
> 性质：实现方案（不含执行）。写库、写纲须在本仓库会话内按门禁执行。

## 一、结论摘要

1. **claim 入库可先行**：`tuhs_wiki` 的 430 个 active 页面（232 wiki＋198 外链）均可转为 `raw_source`，按块抽取 claim 候选，走三轮回核后登记入 claim 库。
2. **大纲写入暂不具备宿主条件**：`05-卷册大纲/` 现有 3,705 个节占位（`.gitkeep`）而正文 `.md` 仅 1 个；`targets.tsv` 4,303 节点为元数据，`layout.tsv` 仅有表头。此时写 ROW_MINE 只能写进占位目录，属越线。方案把大纲阶段设为 **映射先行、写入等待宿主落地**。
3. **不改 claim 库 Schema**：复用 `claim`／`evidence`／`claim_evidence`／`raw_source`／`source_chapter_current`／`provenance_history`；候选、判读、映射台账放 `script/` 外部暂存，不新增表。
4. **不改 claim_id 命名空间**：复用 `CL-RM-\d{6}` 序列与 `register_waterlock.py` 水位锁；不新造 `CL-TW-` 前缀，避免与现有工具链（`outline_writer.py` 的 `CID_RE`、waterlock 的 `CL-RM-%` 过滤）分叉。
5. **大纲锚点需新增族**：现有 `ROW_MINE: <lib>.messages.<pk>` 与 `tuhs_wiki.blocks.<id>` 不同构，须新立 `tuhs_wiki` 线格式与写入器；未立规前不得写生产大纲。

## 二、现状基线

### 2.1 输入库口径

| 项目 | 数值 |
| ---- | ---- |
| wiki 页 active | 232 |
| 外链页 active | 198 |
| 外链页 failed | 160 |
| 外链页 needs_ocr_deferred | 1 |
| `fulltext_blocks` | 39,534 |
| 正文字符 | 14,947,333 |
| 排除项 | 39（source_code 36／book 2／media 1） |

- 失败外链无正文，**不进入 claim 候选**；其 URL 与失败原因保留在 `tuhs_wiki.links`／`crawl_log`，供覆盖度披露。
- `needs_ocr_deferred` 1 件不进入候选；单独 OCR 补库后可作为增量批次。

### 2.2 claim 库现状

| 项目 | 数值 |
| ---- | ---- |
| `claim` | 492,813 行 |
| `evidence` | 519,077 行 |
| `raw_source` | 518,488 行 |
| `claim_evidence` | 492,547 行 |
| `source_chapter_current` | 764 行 |
| 现行 claim_id | `CL-RM-000001`…`CL-RM-493722`（48.3 万行） |
| 历史前缀 | `CL-1`…`CL-23` 等旧卷编号前缀（不再新增） |

- `claim_type` 现行词表：`FACT`／`ORIGIN_CLAIM`／`COMPARISON`／`CONTROVERSY`／`CAUSAL_CLAIM`／`FIRST_APPEARANCE`／`MOTIVATION`／`INFLUENCE_CLAIM`／`INTERPRETATION` 等；**不新增词**。
- `status` 现行仅 `supported`／`rejected`；候选未过审不写 `claim`，留在暂存台账。
- `evidence_level` 现行 L1–L5；本线默认 L3，L4 须双人复核并有一手原件佐证。

### 2.3 大纲现状

| 项目 | 现状 |
| ---- | ---- |
| 目标注册表 | `05-卷册大纲/映射/targets.tsv`，4,303 节点（75 卷／523 章／3,705 节） |
| 节宿主 | 0 个（3,705 个 `.gitkeep`；`目录`／`映射` 之外唯一 `.md` 为根级 `SUMMARY.md`，非节宿主） |
| 路径台账 | `layout.tsv` 仅表头，尚无 `dest_relpath` |
| 入纲写入器 | `outline_writer.py` 仅支持 `ROW_MINE: <lib>.messages.<pk>` 与 `CL-RM-\d{6}` |

**结论**：claim 映射可先产出 `outline_map.tsv`；**ROW_MINE 写入必须以“宿主 `.md` 已落地且节标题匹配”为前置门禁**，不得为赶进度创建占位正文或把块写进 `.gitkeep`。

## 三、总体流水线

```text
tuhs_wiki.duckdb（只读）
   │
   ├─ T1 来源登记  ──> raw_source（每 active 页 1 条）
   │
   ├─ T2 候选抽取  ──> candidates.jsonl（块级证据 + 主张草稿）
   │
   ├─ T3 三轮回核  ──> judgements/ + review_ledger.tsv
   │
   ├─ T4 登记入库  ──> claim / evidence / claim_evidence / provenance_history
   │
   ├─ T5 大纲映射  ──> outline_map.tsv（PENDING/CONFIRMED/DEFERRED_NO_HOST）
   │
   └─ T6 大纲写入  ──> ROW_MINE 块（仅 CONFIRMED 且宿主已落地）
```

各段相互独立验收：T1–T4 不依赖大纲；T5 不写库；T6 只消费 T4 的 claim 真值与 T5 的 CONFIRMED 行。

## 四、T1：来源登记（raw_source）

### 4.1 粒度

- **每 active 页 1 条 `raw_source`**，不按块拆。块级粒度由 `evidence.anchor` 承担。
- wiki 页与外部 active 页同表登记；失败页、延迟页不登记（无正文，登记会造成空壳来源）。
- 同一 URL 的多页引用只对应 1 个外链页，`raw_source` 亦只 1 条。

### 4.2 字段映射

| `raw_source` 字段 | 取值 |
| ---- | ---- |
| `source_id` | `SRC-other:tw-<sha1(page_key)[:16]>`（沿用现有 `other` 命名空间，避免未批准的新 namespace；若 ykla 批准可改 `SRC-wiki:`） |
| `namespace` | `other` |
| `source_db` | `03-原始史料库/16-TUHS-Wiki史料/tuhs_wiki.duckdb` |
| `source_table` | `pages` |
| `local_pk` | `page_key`（wiki 页为 DokuWiki ID；外链页为 `ext:<sha1>`） |
| `content_hash` | `pages.sha256_source` |
| `title` | `pages.title` |
| `source_type` | 按页面类别映射：wiki 页＝`reference_book`（汇编／参考）；外链 PDF 论文＝`academic_work`；手册／官方文档＝`official_doc`；访谈／回忆页＝`memoir_blog`；新闻／论坛＝`news` 或 `web_archive` |
| `carrier` | `wiki_markdown`／`external_html`／`pdf_text`／`pdf_ocr`（取 `pages.extraction_method`） |
| `source_layer` | wiki 页＝4；官方手册＝3；学术论文＝5；访谈／回忆＝4（P41 五层级，1 最强） |
| `tier_basis` | `tuhs_wiki:<extraction_method>;page=<page_key>` |
| `source_date` | `pages.wiki_last_modified`（wiki）或 `pages.last_modified`（外链）；缺失留空 |
| `date_precision` | `day`／`unknown` |
| `author`／`organization` | 仅当页面元数据可确证时填写，否则留空；不得从正文猜 |
| `first_hand` | 默认 0；仅当页面为逐字一手文档且审核确认时填 1 |
| `contemporary` | 依文档年代与事件年代判定；无确证填 0 |
| `retrospective` | 访谈／回忆页填 1，其余 0 |
| `provenance_url` | `pages.url` |
| `provenance_archive` | `fetch_mode='wayback'` 时填快照 URL／时间 |
| `acquired_at` | `pages.fetched_at` |
| `acquisition_method` | `tuhs_wiki_crawl_20261025` |
| `reliability_grade` | 初始 `U`（未评）；T3 复核后按《考据规则》评级回填 |
| `reliability_rationale` | 复核理由；初填页面类别与一手性判断 |
| `banned_source` | 0（除非命中既有封禁清单） |
| `doubt_flag` | 1 仅当页面内容自相矛盾或来源存疑 |
| `legacy_status` | `tuhs_wiki` |

### 4.3 登记顺序与幂等

1. 以 `source_id` 为自然键，`WHERE NOT EXISTS` 插入；已存在则只更新 `reliability_*`／`doubt_flag`。
2. 先登记来源，再登记 claim；`evidence.source_id` 必须命中已登记来源。
3. 每批写 `provenance_history`：`event_type='tuhs_wiki_source_register'`，`detail` 记页数与批次。

## 五、T2：候选抽取

### 5.1 抽取单元

- 以 `fulltext_blocks` 为最小单元；相邻同页段落可合并为一个“证据窗”（≤1,200 字符）。
- 跳过：纯标题块、纯代码块、纯表格分隔、`media_placeholder`、`page_break`。
- 每个证据窗产出 0–3 条原子主张；无法拆成原子命题的段落不强行生成。

### 5.2 候选 JSONL 字段

```json
{
  "page_key": "people:dennis_ritchie",
  "block_id": 12345,
  "block_index": 7,
  "source_id": "SRC-other:tw-0123456789abcdef",
  "claim_text": "……",
  "claim_type": "FACT",
  "time_start": "1972",
  "time_end": "1972",
  "time_precision": "year",
  "evidence_level": "L3",
  "quote": "……",
  "quote_lang": "en",
  "confidence": 0.86,
  "rationale": "……"
}
```

### 5.3 文本纪律

- `claim_text` 30–80 字（与 ROW_MINE 摘要口径一致；claim 库现行均值 63.1 字）。
- `quote` 必须为 `fulltext_blocks.block_content` 的**连续子串**，20–240 字；机器判据：`quote in block_content` 且去空白后仍为子串。
- 不得改写、不得拼接跨块、不得把编者按／引用块当一手陈述。
- `claim_type` 只用现行词表；无法归类者不生成，留人工判读。
- 时间解析：只接受正文明确出现的年份／年月／日期；`time_precision` ∈ `year`／`month`／`day`／`period`／空。
- `evidence_level`：wiki 页默认 `L3`；`L4` 仅限逐字一手文档且 T3 双人确认；不得写 L5（L5 保留给代码来源）。

### 5.4 去重

- 文本归一（小写、去空白与标点）后 SHA-1；同页同块同文本只留 1 条。
- 跨页近似重复（Levenshtein ≥0.90）标 `duplicate_of`，合并证据而非新增 claim。
- 同一主张多页出现时，主 claim 保留最早／最一手来源，其余作为 `claim_evidence` 的多来源支撑。

## 六、T3：三轮回核

### 6.1 三轮回核设计

1. **机器轮（R0）**：逐条断言 `quote` 子串、`claim_text` 不含原文没有的数字／人名、`evidence_level` 与来源类别一致、时间格式合法、`source_id` 存在。
2. **独立复核轮（R1）**：复核者不得为抽取者；逐条判 `keep`／`fix-text`／`reject`／`doubt`；L4 及任何跨来源合并必须双人。
3. **抽检轮（R2）**：按命名空间分层抽样（每层 ≥10%，L4 100%），对 claim 与 quote 逐字比对；发现系统性偏差则整批退回。

### 6.2 判读台账

`script/_tuhs_ingest/judgements/<batch>.jsonl`：

```json
{"key": "people:dennis_ritchie#12345#<sha1>", "verdict": "keep",
 "claim_text": "……", "quote": "……", "reason": "……", "reviewer": "r1:<id>", "at": "……"}
```

- 台账是唯一判读真值；`claim` 表只落 `keep` 且两轮一致的条目。
- `reject`／`doubt` 不写 claim；`doubt` 汇总到批报告，必要时开 `controversy`。
- 每批统计：候选数、keep／fix／reject／doubt 数、L4 数、去重数、覆盖率。

### 6.3 0 信任与来源独立性

- 同一事实若仅有 wiki 页本身支撑，按 L3 处理；wiki 页转述的 Wikipedia／论坛内容不得升为 L4。
- `source_independence` 登记重复／派生关系（`duplicate_title`／`derivative`／`mirror`），防止把同一来源的多个副本当独立证据。
- 任何“据某人之口”式主张，若 quote 本身是二手转述，`evidence_level` 不得高于 L3。

## 七、T4：登记入库

### 7.1 事务与批次

- 每批 **≤50 条 claim**，单事务写入；任一行失败整批回滚。
- 批次号 `tuhs-bNNN`；`created_by='llm:tuhs_wiki'`；`reviewed_by='r1:<id>,r2:<id>'`。
- 写前：`claimdb_guard.py --db historical_claims` PASS；`rotate_guard_state.py pre`；`register_waterlock.py probe` → `acquire`。
- 写后：行数与预期相等、`claim_id` 连续无撞号、每条 claim 至少有 1 条 evidence、`claim_evidence` 双向行数一致、`provenance_history` 每 claim 至少 1 条；随后 `release`、`rotate_guard_state.py post`。

### 7.2 ID 分配

- 复用 `CL-RM-\d{6}`：每批 `probe` 取当前最大号，按 `max+1` 连续分配；**禁止硬编码**，禁止并行会话自行取号。
- 不新造 `CL-TW` 前缀；批次信息放 `created_by`／`provenance_history`／source 字段。

### 7.3 插入字段

| 表 | 字段取值 |
| ---- | ---- |
| `claim` | `claim_id`＝waterlock 号段；`claim_text`＝复核后文本；`claim_type` 现行词表；`time_*` 按候选；`evidence_level` 复核值；`wording_gate='attribution_allowed'`（不能独立成立者 `contextual_only`）；`status='supported'`；`created_by='llm:tuhs_wiki'`；`reviewed_by` 复核者；`created_at`／`updated_at` 同批时间 |
| `evidence` | `evidence_id='EV-TW-<6位序号>'`（新前缀，仅本线；不占用 `EV-KF`／`EV-M` 号段）；`source_id`；`anchor='block:tuhs_wiki:<block_id>'`；`quote` 原文；`quote_lang`；`fact_text` 可空；`evidence_kind='quote'`；`confidence`；`extracted_by='llm:tuhs_wiki'`；`extraction_review='confirmed'` |
| `claim_evidence` | `claim_id`；`evidence_id`；`role='supporting'`；`strength='strong'`／`medium`；`disposition` 空；`search_log_ref` 指判读台账 key |
| `provenance_history` | `source_id`；`seq` 按该来源递增；`event_type` ∈ `tuhs_wiki_source_register`／`tuhs_wiki_claim_register`／`tuhs_wiki_review`／`tuhs_wiki_merge`；`detail` 含批次与 claim_id；`at` 同批时间；`id` 前向递增，禁回填 |

- `evidence_id` 新前缀 `EV-TW-` 属本线命名空间，需在批前由 ykla 确认；若不批准，则沿用 `EV-KF-` 续号（但会与既有 key_facts 来源混淆，推荐前者）。
- `fact_text` 不重复 `claim_text`；如填，须为原文摘句。
- `evidence.quote` 与 `claim_text` 均不得含直角引号；英文原文引号保留原样。

### 7.4 幂等与回滚

- 自然键：`(source_id, anchor, sha1(claim_text))`；写入前查重，已存在则跳过并记 `update_log`（claim 库 `update_log` 表）。
- 回滚：本批 `provenance_history`＋`claim_evidence`＋`evidence`＋`claim` 按批次标记反向删除；删除前必须有 `12-数据库备份/historical_claims/` 专项正式备份。
- 不使用文件级旁路副本；Git 只用于脚本与规则，不用于数据库回滚。

## 八、T5：大纲映射

### 8.1 前置门禁 H0

写入前逐节检查：

1. `targets.tsv` 中 `status='active'` 的节节点存在；
2. 磁盘上该节宿主 `.md` 存在（非 `.gitkeep`）；
3. 宿主 H1 与 target `sec_no`＋`title` 一致；
4. 宿主所在章目录与 `vol_no`／`ch_no` 一致。

任一不满足 → `outline_map.status='DEFERRED_NO_HOST'`，**不创建占位文件、不写 `.gitkeep`**。当前 3,705 节中节宿主为 0，故大纲写入阶段应整体等待正文落地。

`host_relpath` 由目录扫描解析：卷目录按 `targets.tsv` 的 `vol_no`＋目录名前缀匹配，章目录按 `ch_no`＋前缀匹配，节文件按 `sec_no` 前缀匹配；解析不到即 `DEFERRED_NO_HOST`，**禁止按标题模糊猜文件名**。

### 8.2 候选生成

- 从 `05-卷册大纲/chapter_keywords.json` 与 `theme_index.json` 取该 claim 的关键词／人名／项目名，召回 top-5 节节点。
- 评分：关键词重叠 0.5、标题相似 0.3、实体／时间吻合 0.2；低于阈值的标 `UNMAPPED`。
- 一人多节时按“首次出现／主要事纪”择主节，最多 2 个次节；仅主节写块，次节记 `source_chapter_current` 或映射台账。
- 不得用旧 `source_chapter`（19 卷 355 章冻结快照）作为现行坐标；旧表不原地改。

### 8.3 映射台账

`script/_tuhs_ingest/outline_map.tsv`：

| 列 | 说明 |
| ---- | ---- |
| `claim_id` | claim 真值 |
| `target_node_id` | `targets.tsv` 的 `S-*` |
| `vol_no`／`ch_no`／`sec_no` | 现行坐标 |
| `host_relpath` | 相对 `05-卷册大纲/` 的宿主 `.md` |
| `confidence` | `high`／`medium`／`low` |
| `basis` | 关键词／标题／实体依据 |
| `status` | `PENDING`／`CONFIRMED`／`DEFERRED_NO_HOST`／`REJECTED`／`UNMAPPED` |
| `reviewer`／`reviewed_at` | 复核者与时间 |

- 只有 `CONFIRMED` 可进入 T6；`DEFERRED_NO_HOST` 保留待宿主落地后重跑。
- `source_chapter_current` 仅对 `CONFIRMED` 写入：`vol`／`ch`／`sec` 取现行坐标，`mapping_kind='tuhs_wiki_semantic'`，`confidence`，`basis='<node_id>；<依据>'`，`batch='tuhs-bNNN'`，`operator='tuhs-wiki-ingest'`。

## 九、T6：大纲写入

### 9.1 新锚点族

```text
<!-- ROW_MINE: tuhs_wiki.blocks.<fulltext_blocks.id> -->
```

- 与 `usenet_mail.messages.<pk>` 同层级，但 `<id>` 是 `tuhs_wiki.fulltext_blocks.id`（数字，唯一）。
- 新族须先写入 `ROW_MINE块体格式规则.md`（新增“TUHS Wiki 线”小节，含抬头／等级／纪律串映射），经 ykla 批准后才可生产写入。
- 现有 `outline_writer.py` 的锚点正则只认 `.messages.<pk>`，不得直接复用；须新建 `tuhs_wiki_outline_writer.py`，沿用三项契约（宿主权威解析、块级幂等、路径覆盖）与原子写盘。

### 9.2 块体（5 行）

```text
<!-- ROW_MINE: tuhs_wiki.blocks.12345 -->
**二手转述**（证据等级：L3，来源：`historical_claims.duckdb.claim.CL-RM-493723`；2026-10-26 tuhs_wiki 采纳）
（空行）
[1972 年，]摘要……引用时按 L3 纪律：以上为 TUHS Wiki 二手转述，非当事人一手证词，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
（空行）
```

- 抬头／纪律串按新线映射表：默认 L3 `二手转述`；L4 仅逐字一手文档用 `当事人自述`，纪律串不得含“一手”错标。
- 摘要 30–80 字，取自复核后 `claim_text`；日期前缀取 `claim.time_start`，无精确日期可省。
- 等级取 `claim.evidence_level` 真值，禁止字面硬编码；`claim_id` 必须存在且等级一致。

### 9.3 写入器契约

- 宿主来自 `outline_map.tsv` 的 `host_relpath`，不按文件名猜；宿主 H1 必须匹配 target。
- 判重：扫描面内同 `tuhs_wiki.blocks.<id>` 锚点即跳过；同锚不同 claim 报警。
- 默认 dry-run；`--write --anchor tuhs-bNNN` 才写；同目录临时件→fsync→os.replace；任一宿主失败回滚整批。
- 写后断言：新增锚数＝计划数、每锚恰一次、旧锚保留、块文本可回读、UTF-8 无 BOM／LF。
- 失败路径 exit 2、零写入。

## 十、批次计划

| 阶段 | 内容 | 验收 |
| ---- | ---- | ---- |
| P0 试点 | 10 页（people／systems／anecdotes 各若干）→ 20–30 claim；T1–T4 全链 | quote 子串 100%、双人复核、claim/evidence/claim_evidence 行数守恒 |
| P1 小批 | 50 页／≤50 claim；跑通 waterlock、guard、provenance | 撞号 0、重复 0、回滚演练通过 |
| P2 全量 claim | 232 wiki 页分批；外链 active 页按需增量 | 覆盖率报告、失败页披露、claim 总量与批次台账一致 |
| P3 大纲映射 | 全量 CONFIRMED 候选；H0 门禁逐节检查 | CONFIRMED 均有宿主；DEFERRED 清单完整 |
| P4 大纲写入 | 按宿主落地批次写 ROW_MINE | 每批锚数守恒、块体 5 行、等级一致、门禁全绿 |

每批收口固定顺序：备份 → `claimdb_guard` → `rotate pre` → waterlock `acquire` → 事务写库 → 行数／ID／provenance 断言 → `release` → `rotate post` → 大纲映射 → 门禁 → changelog／批次台账。

## 十一、门禁与验收

### 11.1 claim 线

- `claimdb_guard.py --db historical_claims` PASS（写前）。
- `register_waterlock.py probe → acquire → register → release`（撞号 0）。
- 写后：`claim`／`evidence`／`claim_evidence` 行数增量＝计划数；每 claim ≥1 evidence；每 evidence 的 `source_id` 存在；`provenance_history` 每 claim ≥1 行；`audit_provenance_dupes.py` 无新增 FAIL。
- `evidence.quote` 子串判据 100%（机器复算）。
- 重复：`claim_text` 归一哈希重复 0；`(claim_id,evidence_id)` 重复 0。

### 11.2 大纲线

- 宿主 H0 门禁：target 存在、`.md` 存在、H1 匹配、章目录匹配。
- 写后：`audit_evidence_level_labels.py`（块头等级＝claim 真值）、`audit_outline_dup.py`（同锚重复 0）、`audit_anchor_pairs.py`／`audit_anchor_pair_order.py`（成对锚不受影响）、`audit_note_xref.py`／`xref_audit.py`（引用不悬空）、`audit_markdown_lint.py`、`audit_md_quote_glyphs.py`、`audit_md_bold_spacing.py`。
- 触及映射台账时加跑 `audit_outline_landing.py`。

### 11.3 验收口径

- claim 批次：候选→keep 转化率、L4 双人复核率、quote 保真率、去重率、覆盖率（active 页中有 claim 的页数／430）。
- 大纲批次：CONFIRMED 数、DEFERRED_NO_HOST 数、UNMAPPED 数、每宿主锚数、块体 5 行合规率。
- 所有数字写入批次台账与 `changelog.duckdb`；不写“约”“若干”等模糊值。

## 十二、工具清单（拟建）

| 脚本 | 作用 | 关键约束 |
| ---- | ---- | ---- |
| `tuhs_wiki_source_registry.py` | T1：active 页 → `raw_source` | 只读输入库；`SRC-other:tw-` 键；幂等 |
| `tuhs_wiki_claim_extract.py` | T2：块→候选 JSONL | quote 子串、30–80 字、现行 claim_type |
| `tuhs_wiki_review.py` | T3：判读台账合并、三轮回核统计 | 抽取者不得复核；L4 双人 |
| `tuhs_wiki_register.py` | T4：事务写 claim 库 | waterlock＋guard＋专项备份；≤50/批 |
| `tuhs_wiki_outline_map.py` | T5：候选映射 TSV | 只用 targets 现行坐标；不写库／不写纲 |
| `tuhs_wiki_outline_writer.py` | T6：ROW_MINE 块写入 | 新锚族；宿主 H0；原子写；dry-run 默认 |
| `tuhs_wiki_batch_verify.py` | 批次门禁聚合 | 行数、ID、quote、等级、锚数、编码 |

复用：`claimdb_guard.py`、`register_waterlock.py`、`rotate_guard_state.py`、`audit_provenance_dupes.py`、`audit_evidence_level_labels.py`、`audit_outline_dup.py`、`audit_anchor_pairs.py`、`audit_markdown_lint.py`、`audit_md_quote_glyphs.py`、`backup_databases.py`。

上述新脚本须在 `脚本与命令/README.md` 登记，并由 `流程规则.md`／`ROW_MINE块体格式规则.md` 引用；`tuhs_wiki_outline_writer.py` 若设为门禁，须入 `audit_gate_registry.py`。

## 十三、风险与未决

1. **大纲宿主未落地**：当前 3,705 节无正文宿主，T6 实际上只能在正文落地批之后启动；不得以占位文件绕过。
2. **外链覆盖缺口**：160 个外链页失败（DokuWiki 402、YouTube／Google Groups JS 空壳、404／410），这些页不产生 claim；覆盖度须在批次台账披露，不得用 wiki 页转述冒充原链内容。
3. **1 件延迟 OCR**：SGI IRIS 用户指南 24 MB／超 300 页；补 OCR 后作为增量来源，不阻塞首批。
4. **claim_type／status 词表**：只允许现行值；新增词须先改 `controlled_vocab` 并走规则／ADR。
5. **source_id 命名空间**：方案默认 `SRC-other:tw-`；若改 `SRC-wiki` 须先更新 `schema_meta.source_id_convention` 并全链同步。
6. **evidence_id 前缀**：方案建议 `EV-TW-`；若不批准则沿用 `EV-KF-` 续号，二者不可混用。
7. **L4 判定**：wiki 页是汇编载体，默认 L3；只有逐字一手文档且双人复核才可 L4，防止把“wiki 上的当事人自述转帖”误标一手。
8. **锚点族变更**：`tuhs_wiki.blocks.<id>` 须先入 `ROW_MINE块体格式规则.md` 并经 ykla 批准；未立规前 T6 不得开写。

## 十四、交付物清单

1. `script/_tuhs_ingest/` 暂存区：`candidates.jsonl`、`judgements/`、`review_ledger.tsv`、`outline_map.tsv`、`batch_<tag>.json`、`register_log.jsonl`。
2. claim 库新增行：`raw_source` 430 条（首批 active 页）、`claim`／`evidence`／`claim_evidence` 按批复核数、`provenance_history`、`source_chapter_current`（仅 CONFIRMED）。
3. 大纲 ROW_MINE 块：仅 `CONFIRMED`＋宿主 H0 通过者。
4. 批次报告：`08-核查报告与多轮复核/` 下按批次记录候选／keep／reject／doubt、覆盖度、门禁结果。
5. 规则更新：`ROW_MINE块体格式规则.md` TUHS Wiki 线、`流程规则.md` 本线写入器条款、`脚本与命令/README.md` 登记。
