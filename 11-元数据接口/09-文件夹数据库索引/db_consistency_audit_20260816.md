# 非邮件数据库规则一致性与优化机会审计报告

> 审计日期：2026-08-16
> 审计范围：27 个非邮件数据库（排除 `03-原始史料库/11-邮件列表史料/` 下约 290 个邮件列表库）
> 审计方法：只读探测（`SELECT` / `PRAGMA` / `integrity_check`），未执行任何写库操作（无 INSERT/UPDATE/DELETE/ALTER/VACUUM/DROP）
> 数据来源：`script/_nonmail_db_audit_20260816.json`（实测） + `folder_db_registry.csv`（登记簿） + `dashboard.md`（历史看板）
> 说明：raw 大库（freebsd/netbsd/openbsd/dragonfly/bsd-derivatives/linux-kernel，>500MB）因体积过大，sha256 与 integrity_check 标注 SKIP，仅核验存在/大小/可打开/表结构/行数近似（MAX(rowid)）

---

## 一、审计范围

27 个非邮件数据库按职责分三类：

- **文件夹级数据库（7 个，Schema v1.4 通用架构）**：`sacred_sources`、`original_sources`、`research_notes`、`fact_checks`、`review_reports`、`cross_indexes`、`metadata_interfaces`
- **功能数据库（9 个）**：`changelog`、`资料数据库`、`phoronix_news`、`references_fulltext`、`doubts_standalone`、`causal_graph`、`historical_claims`、`bsdnow_podcast`、`bsd_podcasts_external`
- **代码仓库数据库（11 个，一手史料 raw）**：`freebsd`、`netbsd`、`openbsd`、`dragonfly`、`openzfs`、`bsd-derivatives`、`illumos-gate`、`openssh-apple`、`openssh`、`darwin`、`linux-kernel`

清单与 `folder_db_registry.csv` 非邮件条目一一对应，无遗漏、无误计入邮件库、无重复（registry 292 条 → 非邮件 27 条，与磁盘实况一致）。

---

## 二、27 库总览表

| # | 库名 | 大小 | schema_version（登记簿） | integrity | journal_mode | 异常标记 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | changelog | 2.3 MB | 0 | ok | delete | ⚠ sha 漂移、journal 非 WAL |
| 2 | sacred_sources | 4.6 MB | 1.4 | ok | delete | ⚠ 45 orphaned 未登记 |
| 3 | phoronix_news | 544 KB | 1.0 | ok | wal | ⚠ 无 schema_meta（用 db_meta） |
| 4 | 资料数据库 | 21.3 MB | 1.4 | ok | delete | ⚠ schema_meta 引用数陈旧 |
| 5 | freebsd | 3.23 GB | v2 | SKIP(raw) | delete | — |
| 6 | netbsd | 9.74 GB | v2 | SKIP(raw) | delete | — |
| 7 | openbsd | 915 MB | v2 | SKIP(raw) | delete | ⚠ commit_files 疑似异常 |
| 8 | dragonfly | 897 MB | v2 | SKIP(raw) | delete | ⚠ commit_files 疑似异常 |
| 9 | openzfs | 57.9 MB | 2 | ok | delete | ⚠ 版本写法 "2" |
| 10 | bsd-derivatives | 6.02 GB | v2 | SKIP(raw) | delete | — |
| 11 | illumos-gate | 104 MB | 2 | ok | delete | ⚠ 版本写法 "2" |
| 12 | openssh-apple | 270 KB | 2 | ok | wal | ⚠ 版本写法 "2" |
| 13 | openssh | 7.7 MB | v2 | ok | delete | — |
| 14 | darwin | 21.9 MB | v2 | ok | wal | — |
| 15 | linux-kernel | 2.85 GB | 2 | SKIP(raw) | delete | ⚠ 版本写法 "2" |
| 16 | bsd_podcasts_external | 19.3 MB | 1.0.0 | ok | wal | ⚠ outline_mappings=0 |
| 17 | bsdnow_podcast | 31.2 MB | 1.0.0 | ok | wal | ⚠ 转录完成度低 |
| 18 | original_sources | 14.9 MB | 1.4 | ok | delete | ⚠ 601 deleted 墓碑、碎片 |
| 19 | references_fulltext | 1.08 GB | 1.4 | ok | delete | ⚠ schema_meta 空值、碎片 |
| 20 | doubts_standalone | 89.7 MB | 1.0.0 | ok | wal | ⚠ registry 计数漂移 |
| 21 | causal_graph | 152 KB | 0.1 | ok | wal | ⚠ 9 业务表全空、sha 漂移 |
| 22 | historical_claims | 1.17 GB | 0.2 | ok | wal | ⚠ L1 巨大、上层空洞 |
| 23 | research_notes | 272 MB | 1.4 | ok | delete | ⚠ schema_meta 计数漂移 |
| 24 | fact_checks | 123 KB | 1.4 | ok | delete | ⚠ 空壳（全 deleted） |
| 25 | review_reports | 700 KB | 1.4 | ok | wal | ⚠ 计数漂移 |
| 26 | cross_indexes | 2.9 MB | 1.4 | ok | wal | — |
| 27 | metadata_interfaces | 3.5 MB | 1.4 | ok | delete | ⚠ chapter_metadata 仍 348 |

合计：27 库约 **26.6 GB**（其中代码仓库库约 23.9 GB，研究/功能库约 2.7 GB）。

---

## 三、规则一致性发现

### 3.1 schema_version 口径不统一（P1）

同类库版本格式不一致：

- **代码仓库库（11 个）**：`v2` 与 `2` 混用。`freebsd/netbsd/openbsd/dragonfly/bsd-derivatives/openssh/darwin` 记 `v2`，`openzfs/illumos-gate/openssh-apple/linux-kernel` 记 `2`。
- **功能库**：`phoronix_news=1.0`、`doubts_standalone=1.0.0`、播客两库 `1.0.0` 三者格式不一；`historical_claims=0.2`、`causal_graph=0.1`、`changelog=0`。
- **文件夹级库（7 个）+ 资料数据库 + references_fulltext**：统一 `1.4`，符合预期。

判定：schema_version 缺乏统一命名规范（是否带 `v` 前缀、是否三位版本号），属登记口径漂移，不影响库结构，但削弱登记簿可信度。

### 3.2 登记簿（registry）与实库一致性（P1）

逐库比对 sha256 前 16 位、size_bytes、active/deleted 计数：

| 库 | 漂移项 | 实测 vs 登记 |
| --- | --- | --- |
| changelog | sha256 | `7e60717f2802974d` vs `f362e909c210bacc`（活库，持续写入，正常漂移） |
| causal_graph | sha256 | `0c2815d4be4e136f` vs `8fa364dcb7b48e46`（151KB 库自 08-12 后被改写） |
| doubts_standalone | active_files | 实 3289 条记录（1987+1302）vs 登记 2999（迁移时旧值，漂移） |
| sacred_sources | orphaned | 实 45 orphaned 文件未在登记簿任何字段体现 |
| 6 个 heavy-raw 库 | sha256 | 未重算（SKIP），无法核验登记 sha 是否漂移 |

其余 20 库 size_bytes 与 sha256 与登记一致。raw 大库的 sha 是否漂移本次未核验（此前 freebsd 已实测漂移一次），建议后续单独核验。

### 3.3 模块化分层设计（一库一文件夹）违规（P1）

存在 3 处"一个文件夹含多个活动数据库"：

- `04-现代研究文献/` 根目录并存 `research_notes.db`、`historical_claims.db`、`causal_graph.db` 三库（另有 `05-参考文献全文数据库/`、`06-存疑数据库/` 子目录各一库）。
- `03-原始史料库/01-代码仓库史料/01-数据库本体/` 并存 `phoronix_news.db` 与 `资料数据库.db`。
- `03-原始史料库/01-代码仓库史料/08-跨项目对比/db/` 并存 `illumos-gate.db`、`openssh-apple.db`、`openssh.db` 三库。

其中 `04-现代研究文献/` 三库并存最需关注：`historical_claims.db`（1.17GB）与 `causal_graph.db`（151KB）同为重构2026 史学库，`causal_graph` 尚未独立成子目录。代码仓库"按项目分库"属预期设计，`08-跨项目对比` 三库按子项目拆分合理。

### 3.4 PRAGMA / integrity / journal_mode

- `integrity_check`：27 库中 21 个实测 `ok`，6 个 heavy-raw 库 SKIP（此前 dashboard 已确认全 ok）。无损坏库。
- `journal_mode`：**普遍漂移**。多数文件夹级库的 `schema_meta` 声明 `journal_mode=wal`，但实际持久化读取为 `delete`（`sacred_sources/original_sources/research_notes/fact_checks/metadata_interfaces/资料数据库/references_fulltext` 均如此）。仅 `review_reports/cross_indexes/doubts_standalone/播客两库/phoronix_news/openssh-apple/darwin` 实为 `wal`。

  说明：WAL 为会话级 PRAGMA，未在关闭时持久化则回退 delete。`dashboard.md` 曾声称"journal_mode=wal 已持久化到文件头"，与实测不符，属文档口径漂移。

### 3.5 schema_meta 键集合与内部计数漂移（P1）

`schema_meta` 中 `active_files`/`deleted_files` 与 `files.status` 实测存在多处内部漂移：

| 库 | schema_meta 声称 | files.status 实测 |
| --- | --- | --- |
| sacred_sources | active=8, deleted=0 | active=8, **orphaned=45**（新增状态未登记） |
| original_sources | active=1, deleted=601 | active=**3**, deleted=601 |
| research_notes | active=1789, deleted=0 | active=**1791**, deleted=6, merged=3 |
| review_reports | deleted=50 | deleted=**53** |
| cross_indexes | active=2, deleted=51 | active=3, deleted=51 |

另：`资料数据库` schema_meta 内 `references_semantics` 记"16879 条"，实测 `references` 表 17355 条，内部陈旧；`references_fulltext` schema_meta 多个键（active_files/deleted_files/last_optimize_at 等）为空字符串，未填充。

---

## 四、大小/内容符合预期评估

### 4.1 大小异常（P2）

- **historical_claims.db（1.17 GB）**：职责为"史学主张库"，体量偏大。实测 `raw_source=2,635,799`（263 万行，L1 史料注册层）+ `evidence=26,898` + `source_chapter=27,094`，L1 层占绝对主体；L3/L4/L5 层（`interpretation/narrative_unit/narrative_citation` 等 13 张表）全为 0 行。属"L1 巨大、上层空洞"，1.17GB 主要由 raw_source 与 evidence 文本撑起。
- **fact_checks.db（123 KB）**：全 deleted 空壳（41 文件 deleted、0 blocks），事实核查职能已迁移至 `资料数据库.fact_check_records(49)` 与 08-核查报告 Markdown，应退役。
- **causal_graph.db（152 KB）**：9 张因果图业务表全 0 行，仅 DDL 骨架，数据导入延后至阶段 4。
- **references_fulltext.db（1.08 GB）**：`fulltext_blocks=992,226`（近百万块）为 4,077 篇全文的块级索引，体量与内容相符，非异常。
- 代码仓库库体积（freebsd 3.23GB / netbsd 9.74GB / bsd-derivatives 6.02GB / linux-kernel 2.85GB）为 raw commit 数据，符合一手史料定位。

### 4.2 表/行计数与空表/占位（P2）

- `historical_claims` 13 张上层表空（interpretation、narrative_unit、claim_entity、claim_period、claim_relation、entity_relation、evidence_entity、interp_claim、interp_evidence、narrative_citation、provenance_history、source_independence、source_period、cross_ref、controversy_position），属"建库未填"。
- `causal_graph` 9 张业务表空。
- `fact_checks` 无 `fact_check_records` 表（已删），cross_references 17 条指向占位。
- `bsd_podcasts_external` `outline_mappings=0`，与库声明"大纲映射"用途不符（内容缺口）。
- `bsdnow_podcast` `episodes=676` vs `transcripts=53`，转录完成度约 7.8%（其余期数未转写）。

### 4.3 口径脱节（P0，已在 refactor2026 在册）

- **historical_claims.db**：`chapter=181`（已对齐冻结基准）、`chapter_backup_313=313`（旧口径备份表未删）、`source_chapter=27,094`（仍 348 章口径，未迁移）。三者并存，内部章号口径三轨。
- **metadata_interfaces.db**：`chapter_metadata=348`，仍未对齐 12 卷 181 章冻结基准（与 historical_claims.chapter=181 脱节）。

### 4.4 冗余与备份残留

- 数据库目录内 `.tmp_fix`、`.db.bak*`、`.backup*` 残留：**已清理**（本次扫描 0 命中），此前 refactor2026 登记的 15 个 .tmp_fix（约 23.1GB）与 references_fulltext 437MB 备份已不存在。
- `script/` 下 `_backup_*` 目录 + `_staging` 累积约 **31.14 GB**，其中 `_staging` 6.49 GB、`_backup_20260811_173517_db_cleanup` 7.25 GB、`_backup_20260815_史学库续迁前` 2.53 GB 等。按项目规则"临时文件放置 script/ 且不清理"，此部分属用户既定保留范围，不计入优化执行，但登记备查。

---

## 五、合并/拆分/体积/条目优化机会（只读识别，未执行）

### P0（结构性，均已在 refactor2026-db-reorganize-2026-08-15 在册）

| 目标 | 问题 | 建议动作 | 是否在册 |
| --- | --- | --- | --- |
| fact_checks.db | 全 deleted 空壳 | 退役（登记 status=retired，保留文件作索引） | 在册 |
| metadata_interfaces.db | chapter_metadata=348 未对齐 | 348→181 重写对齐冻结基准 | 在册 |
| historical_claims.db | source_chapter 27094 行 348 口径 | 348→181 映射迁移 | 在册 |
| historical_claims.db | chapter_backup_313 旧口径备份表 | 迁移收敛后删除备份表 | 部分在册 |
| causal_graph.db | 9 业务表空 | 数据导入延后阶段 4（本次不执行） | 在册 |

### P1（口径/一致性）

| 目标 | 建议动作 |
| --- | --- |
| 代码仓库库 schema_version | 统一 `v2` 写法（消除 `2`） |
| 功能库 schema_version | 统一三位版本号（`1.0.0` 或 `1.0`） |
| changelog.db / causal_graph.db | 登记簿 sha256 更新为实测值 |
| doubts_standalone.db | 登记簿 active_files 2999 → 3289 |
| schema_meta 计数漂移 | 5 库（sacred/original/research/review/cross）active/deleted 与 files.status 实测对齐 |
| sacred_sources orphaned | 登记簿/看板补充 45 orphaned 口径 |
| 模块化分层 | 登记 3 处多库并存，评估 historical_claims/causal_graph 独立成子目录 |
| journal_mode | 纠正 dashboard/看板"已持久化 WAL"的文档口径（或统一持久化策略） |
| 资料数据库 | schema_meta references_semantics 16879 → 17355 |

### P2（体积/条目优化）

| 目标 | 建议动作 | 预估 |
| --- | --- | --- |
| historical_claims.db（1.17GB） | 评估 raw_source 2.6M 行是否需全量留存或分库/归档；上层空洞表明确填充计划 | 可能大幅瘦身 |
| references_fulltext.db（1.08GB） | VACUUM 回收 freelist 5625 页（约 22MB）+ 补全 schema_meta 空值 | 约 22MB+ |
| original_sources.db | VACUUM 回收 freelist 919 页（约 3.6MB） | 约 3.6MB |
| bsd_podcasts_external.db | 补 outline_mappings（内容缺口）或修正库声明 | — |
| bsdnow_podcast.db | 明确剩余 623 期转录计划（转录完成度 7.8%） | — |
| 播客两库 | 同 schema 1.0.0、语义相近，评估是否合并为单一播客库 | — |
| commit_files 异常 | 核查 freebsd/openbsd/dragonfly 三库 commit_files MAX(rowid) 高度雷同（62,831,674 / 62,832,869 / 62,830,053）是否数据导入 bug | 需深入核查 |
| script/ 31.14GB 备份 | 按项目规则保留，仅登记；如需瘦身需用户另行授权 | — |

---

## 六、结论与后续建议

1. **数据库完整性与可用性**：27 库无损坏（21 个实测 integrity=ok，6 个 raw 大库此前已核验 ok），所有库可正常打开并查询。审计未发现数据损坏。
2. **核心结构性问题集中在重构2026 史学库链路**：`historical_claims.db`（chapter 181 + chapter_backup_313 + source_chapter 348 三轨）与 `metadata_interfaces.db`（chapter_metadata 348）的章号口径未完全收敛，与 `causal_graph.db` 空壳共同构成待完成的结构性任务，均已在 `refactor2026-db-reorganize-2026-08-15` 在册。
3. **规则一致性最突出的是 schema_version 格式不统一与 schema_meta 计数漂移**：属登记口径问题，非数据问题，建议在登记簿层面统一，不涉及库结构改动。
4. **可合并对象有限**：仅 `bsdnow_podcast` 与 `bsd_podcasts_external` 两库同构、语义相近，具备合并潜力；`fact_checks` 应退役而非合并；`causal_graph` 宜独立成子目录而非并入 historical_claims（命名空间已按 EV-/CL-/IC- 分离）。
5. **体积优化最大空间**：`historical_claims.db`（1.17GB，raw_source 2.6M 行占主体）与 `script/` 31.14GB 备份累积；前者需内容工程决策，后者按项目规则保留。

**本报告仅为审计结论，所有优化建议均未执行，待用户批准后另行实施。**

---

## 附：审计方法留痕

- 探测脚本：`script/_nonmail_db_audit_20260816.py`（只读，`file:...?mode=ro` 打开，仅 SELECT/PRAGMA）
- 实测数据：`script/_nonmail_db_audit_20260816.json`（27 库完整表/行数/schema_meta/files_status/journal_mode/integrity）
- sha256 与 integrity_check 对 6 个 >500MB raw 大库标注 SKIP，属审计边界，非数据问题。
