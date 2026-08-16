# 重构 2026 准备进度复核报告

生成日期：2026-08-16

本报告为“重构 2026”准备阶段（阶段 0 备份 + 阶段 1 规则修订）只读复核结论，汇总备份层、规则层、数据库层三个并行子代理的实测复核结果，以及登记簿（folder_db_registry.csv、cross_db_references.csv）只读复核结果。

## 一、三类结论总表

| 类别 | 事项 | 实测状态 |
| --- | --- | --- |
| 已真实完成 | 阶段 1 规则修订（流程规则.md、主题规则.md、CLAUDE.md 的“12 卷 181 章”口径统一） | 已达成，无 182 章残留 |
| 已真实完成 | 阶段 2 Task 4“chapter 表整表重写”（313 → 181） | 实际已提前执行，chapter 表现存 181 行 |
| 已真实完成 | 备份目录 12 个 DB 完整性 | `PRAGMA integrity_check` 全部 ok |
| 已真实完成 | 7 个文件夹级库存在性与完整性 | 全部存在，integrity_check 全部 ok |
| 已真实完成 | 登记簿 historical_claims / causal_graph 两行 | 已登记，size_bytes 与活库一致 |
| 声称完成但漂移 | 阶段 0 备份 historical_claims.db | 备份 1.17 GB 与活库约 40 MB 严重不一致，备份已过期 |
| 声称完成但漂移 | 备份目录校验留痕 | 备份目录内无任何 sha256/checksum/manifest 文件，sha256 均为本次现算 |
| 声称完成但漂移 | spec tasks.md 状态与真实进度 | Task 2、阶段 2 Task 4 实际已完成但 spec 仍标记未完成 |
| 未完成 | spec tasks.md 状态回写 | 未回写 |
| 未完成 | 登记簿 staging 库补录 | 未登记（磁盘有 5 个 staging 库，CSV 无一行） |
| 未完成 | 流程规则.md 第 838 行旧 Schema 残留清理 | 未清理 |

## 二、逐层发现

### A. 备份层（阶段 0）

- git tag `pre-refactor-2026` 存在，为 annotated tag，指向 commit `d2f824c4586cc9fac360c6889ff44ef791e25b0b`；当前 HEAD `b5532d3…` 领先该 tag 150 个提交。
- 备份目录 `script/_backup_20260815_史学库续迁前/` 实测 15 个文件：12 个 DB + `folder_db_registry.csv` + `cross_db_references.csv` 齐备，另多出 1 个 `folder_db_registry.pre_rebuild.csv`（与 `folder_db_registry.csv` sha256 完全相同，字节级冗余副本）。
- 12 个 DB 全部 `PRAGMA integrity_check = ok`。
- 备份目录内无任何 sha256/checksum/manifest 留痕文件（sha256 均为本次现算）。
- 【高危漂移】备份 `historical_claims.db` = 1166766080 字节（约 1.17 GB），活库 `04-现代研究文献/historical_claims.db` = 42070016 字节（约 40 MB），二者不一致——活库在 08-15 备份后已发生“瘦身”（另有 `_backup_20260816_史学库瘦身前` 快照佐证）。以本备份回滚 historical_claims 会得到与活库差异巨大的旧版。

### B. 规则层（阶段 1）

- 流程规则.md（1400 行）：`grep "12 卷 181 章"` = 7（≥6 达标）；`grep "182 章"` = 0；第 107/1213/1280/1286/1291/1317/1331/1358 行口径全部为 181，无漂移（仅 1213/1286/1291/1331/1358 五处在括注格式上不统一）。
- 主题规则.md：第 69 行已为“12 卷 181 章（01b R47/R48/R49）”，全文件 `grep "182"` = 0。Task 2 实际已完成，与 spec tasks.md“未完成”标记矛盾。
- CLAUDE.md：第 7 行同时承载“19卷355章 磁盘实况 + 冻结基准 12 卷 181 章（01b R47/R48/R49）”双口径；命名约定口径在第 104 行（非 spec 预期的第 103 行，第 103 行为目录路径行）。`grep "182 章"` = 0。
- 次要残留：流程规则.md 第 838 行 metadata_interfaces“16 张（含 author_index/build_status/citation_frequency）”与第 1202 行现行“10（+chapter_metadata +timeline_records +build_citation_records）”口径冲突，属旧 Schema 遗留。

### C. 数据库层（迁移前状态）

- historical_claims.db（34 张表）：`chapter` = 181 行（非 spec 期望 313）；旧 313 行已整体归档至 `chapter_backup_313` 表；`source_chapter` = 27094、`entity` = 4454 与期望一致；schema_meta 存在 `dual_track_encoding_warning` 键；historical_period 六期 P1–P6 完整。
  - 【关键结论】`chapter` 表已被重写为 181，说明 refactor2026 阶段 2 Task 4“chapter 表整表重写”实际已提前执行（313→181 已完成），spec tasks.md 却仍标记为未完成。
- causal_graph.db：12 张表齐全（8 张 causal_ 业务表 + chain_cross_ref + schema_meta + sqlite_sequence + update_log，合计 9 张业务表）；schema_version = 0.1；`dual_track_encoding_warning` 键存在。
- 7 个文件夹级库（sacred_sources / original_sources / research_notes / fact_checks / review_reports / cross_indexes / metadata_interfaces）全部存在，`PRAGMA integrity_check` 全部 ok。

### D. 登记簿层

- `folder_db_registry.csv` 总行数 292（不含表头）；`cross_db_references.csv` 总行数 17（不含表头）。
- historical_claims.db 已登记：size_bytes = 42070016（与活库实测一致）、schema_version = 0.2、built_at = 2026-08-12T00:00:00、sha256 = `ecd3103da796f3eb`。Task 11 SubTask 11.4 声称需新增的该行实际已存在。
- causal_graph.db 已登记：size_bytes = 151552（与活库实测一致）、schema_version = 0.1、built_at = 2026-08-12T00:00:00、sha256 = `8fa364dcb7b48e46`。该行同样已存在。
- 邮件列表库：CSV 已登记 4 个聚合库（openbsd_mail、dragonfly_mail、other-bsd_mail、usenet_mail）；freebsd 与 netbsd 邮件列表无聚合库（磁盘亦无对应 `freebsd_mail.db` / `netbsd_mail.db`），其细分库（freebsd 系与 netbsd 系各百余个）已分别登记。SubTask 11.1 所称“6 个邮件列表库”与磁盘实况（4 个聚合库 + 细分库）存在口径差异，须以磁盘实况为准。
- 代码仓库库：11 个业务库（freebsd、netbsd、openbsd、dragonfly、openzfs、bsd-derivatives、illumos-gate、openssh-apple、openssh、darwin、linux-kernel）全部已登记。
- staging 库：未登记。磁盘 `script/_staging/bio_research_20260808/` 下有 5 个 `staging_*.db`，但 CSV 中无任何 staging 行。
- 字段缺失：`built_at` 空值 278 行（仅 14 行有值）；`source_files_status` 空值 9 行；`sha256` 空值 0 行（全表均有值）；`schema_version` 空值 0 行。
- `cross_db_references.csv` 已含 causal_graph 与 historical_claims 的双向 namespace 引用 4 条（namespace_EV_evidence_id、namespace_CL_claim_id、namespace_IC_influence_claim_id、namespace_AR_linked_arrow_id），resolution_status 均为 resolved。

## 三、待整改项清单

### P0（高危，放行前必须处理）

1. historical_claims.db 备份与活库版本漂移：备份 1.17 GB 已过期，须先重新备份活库约 40 MB 版本后方可作为回滚源。

### P1（影响 spec 可信度，建议尽快回写）

2. spec tasks.md 与实际进度脱节：Task 2（主题规则.md 口径统一）、阶段 2 Task 4（chapter 表 313→181 重写）实际已完成但未勾选，须回写 spec 状态。

### P2（低危，可择机处理）

3. 备份目录缺 sha256 留痕文件（建议补 `sha256sum` manifest）。
4. 流程规则.md 第 838 行旧 Schema 残留（“16 张”与第 1202 行“10”口径冲突）。
5. 备份目录多出 `folder_db_registry.pre_rebuild.csv` 冗余副本（与正本 sha256 相同）。
6. 登记簿 staging 库未登记（磁盘 5 个 `staging_*.db` 未入 CSV）。

## 四、放行判断

阶段 1（规则修订）已真实完成，可放行。

阶段 0（备份）主体完成，但存在 historical_claims.db 备份过期隐患（备份 1.17 GB 与活库约 40 MB 差异巨大）。须先重新备份活库当前版本，确认 `chapter` = 181 的活库形态已固化，方可放行“阶段 2—阶段 8”迁移。
