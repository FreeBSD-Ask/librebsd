# 脚本与命令索引

本文件索引 `00-编纂规则与格式规范/01-规则/脚本与命令/` 目录下所有可执行资源（脚本副本、程序命令说明、数据库操作 SQL），列出每条资源的文件名、用途说明与规则引用位置。本目录是规则文件（考据规则.md、写作规则.md、流程规则.md、主题规则.md、释读规则.md）引用的所有可执行资源的独立存储位置，与 `script/` 目录中的原脚本副本形成“规则自洽单元 + 历史脚本归档”的分工关系。

> **SQLite 时代工具脚本状态声明**：全部数据库升格 DuckDB 主存储层后，本目录中面向 SQLite 的工具脚本（`build_folder_databases.py`、`dedup_folder_databases.py`、`resolve_cross_references.py`、`audit_folder_db_integrity.py`、`cleanup_duplicate_sources.py`、`optimize_folder_databases.py`、`clean_wal.py` 等，以及各 `.sql` 操作模板）**不再适用于现行主存储层**——其操作对象（SQLite 库、FTS5 表、PRAGMA、WAL 文件）已随归档退出工作区。**代码仓库/邮件库检查类脚本同样适用本声明**：`check_date_anomalies.py`、`mail_dedup_verify.py`、`dedup_databases_global.py`、`sync_cross_references_after_cleanup.py` 等脚本内登记的 `.db` 路径（freebsd.db、netbsd.db、openbsd_mail.db 等）为 SQLite 时代路径，对应库已转为 `db/duckdb/<name>.duckdb` 或 `duckdb/<name>.duckdb`，这些脚本的 sqlite3 实现与路径登记随归档失效，不作路径改写。这些脚本与 SQL 保留作历史规则书登记（对应规则小节为 SQLite 时代规则），如需对 DuckDB 主库执行同类操作，走“DuckDB 分析层与主存储层规则”小节的 `sqlite2duckdb.py --optimize`/`--verify`；如需对归档 SQLite 执行操作，先解压 `ARCHIVE_FINAL_*.db.gz` 为临时库（用毕删除）。本声明不覆盖：`sqlite2duckdb.py`（现行 DuckDB 管理脚本）、`backup_databases.py`（备份轮换机制保留备用）、`sqlite12_to_duckdb_20260825.py`（DuckDB 转换历史脚本，SCOPE 路径为功能性登记，不作 .duckdb 改写）、`podcast_db_final_sync.py`（播客库收尾脚本）。

## 脚本文件

本目录现存 **52 个 `.py`**，分三类：①**固定脚本**（规则文件明确引用、长期频繁使用，直接存放于本目录，含现行门禁与运维脚本）；②**SQLite 时代工具脚本副本**（自 `script/` 目录复制，见下方状态声明）；③**历史一次性脚本**。**2026-09-18 起本目录整体纳入版本控制**（`.gitignore` 例外规则 `!00-编纂规则与格式规范/01-规则/脚本与命令/*.py`）——原「本目录整体不进版本库」的历史安排已废止，缘由与代价实证见「与 `script/` 目录的关系」小节。

| 文件名 | 用途说明 | 规则引用位置 |
| ------ | -------- | ------------ |
| [auto_ingest_new_pdfs.py](auto_ingest_new_pdfs.py) | 新增 PDF/EPUB/CAJ 文献自动检测入库，含全量检测、`--dry-run` 仅检测、`--file <相对路径>` 单文件入库三种模式 | 流程规则.md “新增文献自动检测规则” → “自动检测触发条件”小节 |
| [cleanup_duplicates_and_errors.py](cleanup_duplicates_and_errors.py) | 重复与错误文档清理脚本：扫描 `references` 表与文件系统，识别 SHA-256 精确重复、标题+作者+年份模糊重复、文件损坏、文件不存在、文件过小五类问题，生成待删除清单 `pending_deletion.jsonl`，含 `--execute` 执行删除、`--sample-only` 抽样复核两种模式 | 流程规则.md “重复与错误文档清理规则” → “清理流程”小节 |
| [scan_all_gaps_v4.py](scan_all_gaps_v4.py) | 全书 12 卷拆分模式章节编号缺口扫描；规则登记此脚本存在两类 bug（浮点解析 bug、格式识别 bug），导致 2026-07-26 报告的“66 处 Type B 缺口”全部为误报 | 流程规则.md “编号缺口登记” → “2026-07-26 编号缺口全面核查结论”小节 |
| [rename_volume_dirs_20260726.py](rename_volume_dirs_20260726.py) | 12 个卷文件夹从“第N卷/”重命名为“第NN卷-中文slug/”格式，与章文件夹“第XX章-slug/”格式统一 | 流程规则.md “序号调整例外”小节示例 |
| [fix_remaining_volume_refs_20260726.py](fix_remaining_volume_refs_20260726.py) | 修复原脚本负向回顾断言遗漏的 4 处“：”后路径引用 | 流程规则.md “序号调整例外”小节示例 |
| [build_folder_databases.py](build_folder_databases.py) | 文件夹级数据库构建脚本：将 7 个一级文件夹中的文本类文件（.md/.txt/.csv/.json）转换为 SQLite 数据库，每个数据库含 5 张通用表（files/blocks/blocks_fts/cross_references/update_log）及若干文件夹专属扩展表，提供 FTS5 全文检索；支持 `--folder`/`--all`/`--rebuild`/`--add-file`/`--update-file` 五种模式 | 流程规则.md “其他文件夹转数据库规则” → “构建脚本 5 模式”小节 |
| [dedup_folder_databases.py](dedup_folder_databases.py) | 文件夹级数据库去重脚本：在 7 个文件夹级 SQLite 数据库构建前后执行去重核验，`--pre` 模式扫描源文件计算 SHA-256 识别精确/模糊/跨文件夹重复，`--post` 模式核验各数据库 files 表的 file_path/sha256/content_hash 唯一性，重复记录仅标记不删除 | 流程规则.md “其他文件夹转数据库规则” → “处理前后去重流程”小节 |
| [resolve_cross_references.py](resolve_cross_references.py) | 跨库交叉引用解析器：扫描 7 个文件夹级 SQLite 数据库的 blocks.block_content，识别 wikilink/markdown_link/footnote/chapter_ref/spec_ref/db_ref/external_url 七类交叉引用，解析目标并写入各库 cross_references 表，汇总跨库引用至 cross_db_references.csv，输出失效链接清单至 broken_links.md；支持 `--all`/`--db` 两种模式 | 流程规则.md “其他文件夹转数据库规则” → “交叉引用解析规则”小节 |
| [audit_folder_db_integrity.py](audit_folder_db_integrity.py) | 文件夹级数据库完整性复核脚本：对比每个数据库 `files` 表与文件夹下实际 `.md/.txt/.csv/.json` 文件清单，输出三维度审计报告（dangling_db_records / unindexed_disk_files / sha256_mismatch）；支持 `--db <db_name>`/`--all`/`--dry-run` 三种模式 | 流程规则.md “其他文件夹转数据库规则” → “完整性复核与重复源文件清理”小节 |
| [cleanup_duplicate_sources.py](cleanup_duplicate_sources.py) | 精确重复副记录源文件清理脚本：根据 `files.duplicate_type='exact'` 的副记录，执行双重 SHA-256 校验后删除副记录源文件，保留主记录；实现 sacred 源材料/git 仓库/二进制文件/模糊重复例外；支持 `--db <db_name>`/`--all`/`--dry-run` 三种模式 | 流程规则.md “其他文件夹转数据库规则” → “完整性复核与重复源文件清理”小节 |
| [dedup_databases_global.py](dedup_databases_global.py) | 跨库全局去重脚本：对 7 个文件夹级数据库执行跨库三级去重（SHA-256 精确 `global_exact` / content_hash 内容级 `global_content` / 标题+首段模糊 `fuzzy_global`），副记录标记 `status='merged'` 并新增 `duplicate_of_db`/`duplicate_of_global_file_id` 字段；支持 `--dry-run`/`--exact`/`--content`/`--fuzzy`/`--all`/`--upgrade-schema` 六种模式 | 流程规则.md “其他文件夹转数据库规则” → “跨库全局去重”小节 |
| [sync_cross_references_after_cleanup.py](sync_cross_references_after_cleanup.py) | 交叉引用同步脚本：在重复源文件清理与跨库全局去重完成后，扫描 `05-卷册大纲/`、`10-交叉索引/`、`11-元数据接口/` 下所有 `.md/.csv/.json` 文件（`06-正式书稿/` 已因禁止编纂正文而移除，不再扫描），将指向已删除/已合并副记录的引用更新为指向主记录；支持 `--dry-run`/`--all` 两种模式 | 流程规则.md “其他文件夹转数据库规则” → “交叉引用同步”小节 |
| [optimize_folder_databases.py](optimize_folder_databases.py) | 文件夹级数据库优化脚本：对 7 个数据库执行 Schema 优化（创建 schema_meta 表 + 9 个预定义索引 + 删除空扩展表 + 回填 update_log）、幽灵块清理（删除 deleted 文件的 blocks/blocks_fts 行，sacred 例外）、VACUUM 空间回收三种操作；支持 `--schema`/`--ghost-blocks`/`--vacuum`/`--all`/`--dry-run` 五种模式 | 流程规则.md “数据库 Schema 优化规则” → “Schema 优化与空间回收”小节 |
| [backup_databases.py](backup_databases.py) | 数据库常设备份与轮换脚本：对 16 个非邮件正式库执行 SQLite 在线备份（`Connection.backup()`，安全处理 WAL），备份即轮替压缩为 `.db.gz`（gzip level 6 + CRC 回读校验），每库按“当次/1日/2日/3日/7日”5 槽独立轮换保留，备份后自动 integrity_check + SHA-256（指解压内容）清单落盘；支持 `--all`/`--db <db_name>`/`--prune-only`/`--list` 四种模式（prune/list 兼容 `.db` 与 `.db.gz`）；备份目录为根目录一级文件夹 `12-数据库备份/`；4 个邮件合并库随 DuckDB 升格移出范围（SQLite 原库以 ARCHIVE_FINAL_*.db.gz 永久归档于各自子目录，prune 不触碰） | 流程规则.md “数据库备份保留规则” |
| [sqlite2duckdb.py](sqlite2duckdb.py) | SQLite → DuckDB 转换、优化与主存储层管理脚本：15 库（11 代码仓库库 + 4 邮件合并库）的 DuckDB 主库管理——转换（`--all`/`--db`，自动跳过 FTS5 虚拟表及影子表，行数三向校验）、优化（`--optimize`：CHECKPOINT 压实 + ART 索引（commits/commit_files 的 commit_hash、messages 的 message_id）+ ANALYZE 统计 + manifest 刷新）、校验（`--verify`：在档库比 SQLite 源、已归档库比 manifest）、状态（`--list`：在档最新/过期/已归档）；归档库转换须先自 `12-数据库备份/<name>/ARCHIVE_FINAL_*.db.gz` 恢复；同步日志 `script/_duckdb_sync_log.jsonl`；DuckDB 依赖：`pip install duckdb`（PoC 实测 dragonfly.db 856MB→131MB，聚合查询加速 6~180 倍） | 流程规则.md “DuckDB 分析层与主存储层规则” |
| [podcast_db_final_sync.py](podcast_db_final_sync.py) | 播客两库 SQLite→DuckDB 收尾脚本（触发条件：转录进程退出）：对 `bsdnow_podcast`/`bsd_podcasts_external` 执行前置检查（integrity_check、无 -wal/-shm 伴生）→ 逐表增量同步至同目录 `.duckdb`（跳过 FTS5 虚拟表及影子表，全 VARCHAR 落库）→ 行数三向校验 → 全部一致后归档 `.db` 为 `ARCHIVE_FINAL_<ts>.db.gz`（SHA-256 清单 + CRC 回读）→ 删除工作区 `.db` 及伴生文件；支持 `--sync-only`（仅同步不归档）/`--check`（仅前置检查）；日志 `script/_podcast_final_sync_log.jsonl` | 流程规则.md “DuckDB 分析层与主存储层规则” → “播客库收尾流程”小节 |
| [sync_gitbook_summary.py](sync_gitbook_summary.py) | **GitBook 总导航 `05-卷册大纲/SUMMARY.md` 生成/同步脚本（固定脚本，2026-09-15 重建，直接存放于本目录）**：原 `script/_sync_gitbook_summary.py` 已缺失，本器依 流程规则.md「GitBook 目录同步规则」重建。采用**结构同步**语义——结构（卷/章/条目集合与顺序）以 `05-卷册大纲/` 磁盘实况为唯一真值完全重算，标题对已在 SUMMARY 中的文件逐字沿用（零改写）、仅新增文件取节文件 H1；头部（`# Summary` + 引言引文）与尾部（`<!-- USER-EDIT:开始 -->`…`<!-- USER-EDIT:结束 -->`，含第20卷块与读者指引）逐字保留。章内条目顺序：`概述.md`(2 空格) → 节文件 `N.M[-K]-*.md`（数值序，4 空格）→ 其他非节 .md → `index.md`（本章索引，恒末）；卷根非章 .md（`V*-新增-*.md`）紧随卷链接列出。`--check`（默认）输出与现行文件的逐行 diff、`--write` 写盘；已实测**幂等**（复跑 0 差异）。**重要说明**：现行 SUMMARY 的节标题与磁盘节文件 H1 已**系统性失同步**（数百处，如 5.8 为 H1＋正文首段合并的长题、3.10 多出 `**`、27.9 缺节号前缀），整文件重生成会一次性改写这些标题——属**独立的一致性工程**，本器刻意以「结构同步」规避之；如需标题归一，须另立专项批准后以 `--regen-titles` 类模式执行 | 流程规则.md “GitBook 目录同步规则” → “同步执行方式”小节 |
| [sync_refactor2026_baseline.py](sync_refactor2026_baseline.py) | 重构2026 大纲目录口径同步脚本（固定脚本，直接存放于本目录）：解析 `08-核查报告与多轮复核/重构2026/index.html` 页首 `doc-metrics` 块提取权威三元组（总卷数/总章数/总节数），扫描 `重构2026/*.md` 三维度——维度一口径三元组 `N卷M章K节`（marker-drift 标记块内过时 / present-stale 标记块外现在时态旧口径 / exempt 历史快照与数据基线）、维度二 ref-stale（指向已归档目录文件且无归档标注）、维度三 pending-stale（未消解 `\| ⬜ \|` 待填单元格且无取代声明）；`--check`（默认）输出漂移报告并以退出码表示是否存在未处置漂移、`--sync` 仅重写 `BEGIN/END 口径基准` 标记块内基准行并刷新日期戳（幂等，标记块外零改动）、`--list` 打印当前权威基准；维度二/三对头部含日期/已被取代等历史声明的文件整体豁免；可选 `--verbose` | 流程规则.md “重构大纲目录口径同步规则” |
| [audit_data_integrity.py](audit_data_integrity.py) | 重构2026 目录页 DATA 数据完整性审计（固定脚本，直接存放于本目录）：解析 `重构2026/index.html` 内嵌 `var DATA = {...}`（persons 人名数组/refs 文献/revisions），对 persons[].n 数组审计四维——①JSON 残片（含 `"value"` 与 `}`/`]` 或以 `{` 开头）判错、②邮箱/账户形态条目（BSD committer 邮箱属有效身份史料，仅提示不判错不删除）、③内部标识串（`person_id_(legacy\|new):`、`freebsd_account`、`openbsd_account`、`netbsd_account`、`dragonflybsd_account` 等前缀）判错、④整个人 n 数组清洗后无人类可读姓名判错；退出码 0/1；目录页修改 DATA 段后必须先跑本门禁 | 流程规则.md “重构大纲目录口径同步规则” → “DATA 数据完整性门禁”小节 |
| [font_subset_rebuild.py](font_subset_rebuild.py) | 重构2026 目录页字体子集重建与 cmap 审计（固定脚本，2026-09-12 起）：扫描 `重构2026/index.html` 全部可见字符（正文+src 注文+DATA 浮层文本），从字体源 tgz（`script/_font_embed_20260905/lxgw-wenkai-screen-webfont-1.7.0.tgz`）合并分片后按页面字符集子集化写回单片 woff2（**font-display:swap 固定**——主理人裁定「无论加载时间最终必须加载新字体」，swap 保证字体就绪后必切换；丢弃 GSUB/GPOS/GDEF 布局表与孤儿替换 glyph）；cmap 审计区分「源字体本无（系统 fallback，允许）」与「源有但重建丢失（回归，退出码 1 禁止写回）」；`--check` 仅审计不写回；大纲内容增改引入新汉字后必须重跑本脚本；依赖 fonttools+brotli（venv） | 流程规则.md “重构大纲目录口径同步规则”（待登记小节） |
| [embed.py](embed.py) | 重构2026 目录页数据装配脚本（固定脚本，直接存放于本目录）：把 `重构2026/data/catalog.json`（语义数据中枢）序列化后重写 `index.html` 的 `var DATA = {...};` 行（发布态装配，单体 HTML 不变、DATA 行外零触碰、幂等、SHA-256 摘要输出），**并同步刷新 og:description／meta description／JSON-LD 口径三元组与数据块开标签 `data-integrity`**（`sha256-` ＋去空白 base64 文本摘要，与前端 `DecompressionStream` 装载器的校验口径一致）；`--check` 三项——①catalog 与内嵌 DATA 内容字段漂移（`$schema`/`version` 为源元数据不参与比较）、②og/meta/JSON-LD 口径同步、③数据块 `data-integrity` 自洽；catalog 或口径修改后运行装配再跑门禁。**2026-09-18 修复两处缺陷**：装配改写数据块正文却不同刷 `data-integrity`（前端校验失败将整体降级、数据层失效）、JSON-LD 同步因旧正则要求两键间仅 `,` 而对现行 `},{"@type":…` 形态恒为 no-op（`--check` 亦因“可否再替换”判据恒报通过） | 流程规则.md “重构大纲目录口径同步规则” → “DATA 数据完整性门禁”小节 |
| [audit_index_structure.py](audit_index_structure.py) | **重构2026 目录页结构自检门禁（固定脚本，2026-09-18 立，第七件改后必跑门禁）**：不依赖浏览器做十一项静态自检——A 编码（无 BOM／CRLF／替换字符／直角引号）／**A2 空格形制（流程规则 L1532：U+3000 须为 0；卷题「第N卷」＋2 个半角空格＋题名；章题「第 N 章」与节序号后有且只有 1 个半角空格，不得连空两格；2026-09-18 补入）**／B 卷锚点 1..N 连续唯一且卷题序数一致／C 卷内章号连续唯一、章题与锚点一致、章题全局唯一／D 章节号连续、节题非空（src 注不计入题文）／E 述评恒末（**若有**「本章书目述评」节须居章末；无述评的正章仅列参考，合 27 号文「有则设、无则不设」）／F 口径六处（doc-metrics／og／meta／footer／JSON-LD／实测）一致／G 标签平衡（section／ul／li／span／h3／h2／div／p）／H 锚点唯一与静态站内链接可达（排除 JS 拼接模板）／I doc-metrics 小字自洽（正章＋卷末述评章＝总章数）／**J 内容层 class ↔ 格式层选择器（内容层／页壳静态标记所用 class 须在 `assets/doc.css`／`assets/modern.css` 中有对应规则；2026-09-18 补入）**；`--path` 可指定文件（如备份件交叉验证）；0 异常 exit 0，否则 exit 1 | 流程规则.md “重构大纲目录口径同步规则” → “DATA 数据完整性门禁”小节（改后必跑八件之一）；CLAUDE.md 修改规范“目录页结构自检门禁（2026-09-18 新增，第七件）” |
| [assemble_index.py](assemble_index.py) | **重构2026 目录页装配器（固定脚本，2026-09-18 立，第八件改后必跑门禁）**：四层解耦的**唯一写者**——读 6 类源（内容层 `data/outline.txt`／格式层 `assets/doc.css`／现代化层 `assets/modern.css`／行为层 `assets/theme-preset.js`＋`assets/doc.js`／数据层 `data/catalog.json`＋`data/schema.jsonld`／页壳 `assets/page.template.html`）装配为单文件 `index.html`；口径数字**由内容源派生**（`{{N_VOL}}`／`{{N_CH}}`／`{{N_SEC}}` 等占位符），不手工维护。无参运行为装配（幂等）；`--check` 重装到内存与磁盘 `index.html` 逐字节比对，不一致即 FAIL（exit 1）。复用 `embed.py` 的 `encode_blob`／`integrity_of`／`serialize_content` | 流程规则.md “重构大纲目录四层解耦与装配规则”；CLAUDE.md 修改规范“目录页四层解耦与装配（2026-09-18 新增，第八件）” |
| [audit_evidence_level_labels.py](audit_evidence_level_labels.py) | **大纲注入块「证据等级」门禁（固定脚本，2026-09-14 立，第六件改后必跑门禁）**：审计 `05-卷册大纲/` 全部 md 中块头 `（证据等级：Lx，来源：`db.table.id`）` 是否与引用项真实等级一致——引用 `historical_claims.duckdb.claim` 者以 `claim.evidence_level` 为逐条真值严格核验（错标或悬空即 FAIL、退出码 1）；其余无逐条等级字段的来源库仅报告族内分布（族内单一值标 INFO，不作判定）。设立缘由：2026-09-14 核查发现全库 439 处块头等级错标（L3 被块脚本模板字面常量写死为 L4），波及 list12/16/18/19/23/38/40/41/44 共 69 个宿主文件；本门禁为该缺陷的常设阻断措施。凡向 `05-卷册大纲/` 写回带等级标注的注入块后必跑 | 流程规则.md “大纲注入块证据等级门禁”小节（待登记） |
| [audit_sequence_continuity.py](audit_sequence_continuity.py) | **目录页节号／章号连续性门禁（固定脚本，第三件改后必跑门禁）**：四维审计 `重构2026/index.html`——①文档序节号递增；②章号一致性；③章号连续；④**「本章书目述评」恒居章末**（2026-09-10 v2 重写为 h3 锚点切章版；旧版 `</ul>` 切章逻辑遇空行／跨章结构会错切，已废弃）。0 问题 exit 0，否则 exit 1 | 流程规则.md “DATA 数据完整性门禁”→“触发条件”（九件门禁之一）；CLAUDE.md 修改规范 |
| [xref_audit.py](xref_audit.py) | **目录页交叉引用门禁（固定脚本，2026-09-12 立，第五件改后必跑门禁）**：逐条审计 src 标注中的「第X卷第Y章」引用；**历史层引用豁免**（前后 25 字符含迁入／并入／归卷／自原／自第／移入／历史层／待考，或前后 8 字符含「；」成组溯源），**现行层分工注须有效**，悬空即 FAIL（exit 1）。结构重编号后必跑 | 流程规则.md “DATA 数据完整性门禁”→“触发条件”（九件门禁之一）；CLAUDE.md 修改规范“目录页交叉引用门禁（2026-09-12 新增，第五件）” |
| [wo007_idempotency.py](wo007_idempotency.py) | **大纲写入幂等防护模块（固定脚本，2026-09-11 起强制）**：`has_block()` 11 类块查重（禁止重复追加自动增补块）／`ensure_absent()` 幂等写入／`normalize_dbnames()` 库名规范化（`*.db`→`*.duckdb`）／`write_guard()` 写盘统一入口（UTF-8 无 BOM ＋ LF）。任何脚本向 `05-卷册大纲/` 写入自动增补块前必须经本模块 | CLAUDE.md 修改规范“大纲写入幂等防护（WO-007）”；`05-卷册大纲/.writing_rules.md` |
| [audit_markdown_lint.py](audit_markdown_lint.py) | **文档格式门禁（固定脚本，2026-09-20 立，第十件·文档格式类）**：对**活动文件显式清单**（`CLAUDE.md`／`00-…/01-规则/*.md`／`01-规则/脚本与命令/*.md`／`重构2026/7[0-9]-*.md`／`重构2026/tests/*.md`／`12-重构大纲书目述评/index.md`）跑 `markdownlint-cli2`，0 问题 exit 0，否则 exit 1，依赖缺失或版本不符 exit 2。**版本钉定** `markdownlint-cli2 0.22.1 / markdownlint 0.40.0`（计数随版本漂移）；`--list` 打印闸面、`--all` 全审计面统计（仅可见性，恒 exit 0）、`--allow-version` 放行非钉定版本。**防衰减护栏**：闸面模式零匹配即 FAIL（防假绿）；`重构2026/` 编号 > 79 的 `.md` 即 FAIL（防 `7[0-9]-*.md` 随号文增长静默失效）。**判据非空**：`--selftest` 在系统临时目录搭隔离夹具，实测 9 项分支（T0 夹具覆盖闸面模式／T1 正常／T2 号文护栏／T3 零匹配／T4a 版本不符／T4b 放行／T5 依赖缺失／T6 `--list`／T7 注入缺陷）**9/9 通过**。**设立缘由**：`markdownlint-cli2` 长期「已文档化但未接入任何门禁」（CLAUDE.md 写了运行命令却无人跑），缺陷静默累积——2026-09-20 实测审计面 89 文件 5,487 条，其中 MD060 占 4,859 条（88.6%） | 流程规则.md “文档格式门禁（2026-09-20 立）”；CLAUDE.md「Lint 配置」与修改规范“文档格式门禁（2026-09-20 新增，第十件·文档格式类）” |
| [fix_md060_delimiters.py](fix_md060_delimiters.py) | **MD060 分隔行修复器（固定脚本，2026-09-20 立）**：按**表头行显示宽度**（CJK 记 2 宽）重算表格分隔行——无冒号 `W−2`／单侧冒号 `W−3`／双侧冒号 `W−4` 个 dash，使管道符位置与表头对齐（`aligned_delimiter` 判据）；**只改分隔行**，不动表头与数据行，跳过围栏代码块内伪表格，反引号内与转义 `\|` 不计为分隔符。`markdownlint --fix` 不会修此类问题（实测确认）。缺省 dry-run，`--apply` 写盘。**实测**：2026-09-20 以本器修 `研究缺口.md`（4 处分隔行）与 `tests/查漏补缺复盘-2026-09-11.md`（1 处），两文件 MD060 归零 | CLAUDE.md「Lint 配置」→「MD060 表格列风格规则」 |
| [audit_page_assets.py](audit_page_assets.py) | **重构2026 页面资产层完整性门禁（固定脚本，2026-09-18 立，第九件改后必跑门禁）**：以 `重构2026/` 树内**非装配产物**的页面资产为对象，覆盖既有八件门禁的共同盲区（八件皆以「产物 index.html」或「大纲 .md」为审计对象，页面级附加件本身无护栏）。四类不变量——**A** 装配源清单（四层 8 源存在且非空）；**B** 内嵌字体子集（B1 `assets/doc.css` 中 `@font-face` 恰 1 片且为 `data:font/woff2` URI／B2 内嵌 woff2 可解析／**B3 覆盖度核心判据**：页面字符集凡**源字体有而内嵌件缺失**者即回归 FAIL，源本无者 INFO 允许／B4 源字体覆盖清单 `data/font-source-cmap.txt` 自洽并与字体源 tgz 交叉核验）；**C** 品牌派生件（C1 logo 真矢量无 `<image>`／base64 光栅／C2 favicon 含 16／32／48 三帧／C3 页面内嵌件与磁盘件逐字节一致）；**D** 自包含性（D1 零 `http(s)` 外链与 `@import`／D2 数据块 `data-integrity` 与内容 SHA-256 一致）；**E** 测试夹具口径（E1 口径串／E2 溯源注计数／E3 `tests/README.md` 断言清单 T 编号集与 `visual_regression.mjs` `record()` 双向吻合）。0 异常 exit 0，否则 exit 1，依赖缺失 exit 2。**依赖 fontTools＋brotli**，须以 `C:/Users/ykla/.workbuddy/binaries/python/envs/default/Scripts/python.exe` 运行；`--root` 指定被审计树根，`--refresh-source-cmap` 重建 B4 基准。**判据非空**：立时以 12 个注入缺陷负向用例实测，12/12 命中且退出码 1 | 流程规则.md “重构大纲目录页面资产层完整性门禁（2026-09-18 立）”；CLAUDE.md 修改规范“目录页页面资产层完整性门禁（2026-09-18 新增，第九件）” |
| [review_v2_full.py](review_v2_full.py) | **重构2026 加强复核套件（固定脚本，2026-09-20 第四十一批自 `/script` 提升）**：对 `重构2026/index.html` 做**全库独立复算**（不抽样），六族锚点——B 标签与结构、C 逐卷逐章逐节复算、D 口径六处与小字自洽、E 溯源注逐条、G 卷级 SPEC 逐字核（含旧题零残留）、H 关联文件（56 表全表逐条、述评 index 口径）、I 门禁自检、J 备份件与述评覆盖率、K 四层解耦一致性（源 ↔ 产物独立复算）；末行打印 `PASS/FAIL/INFO` 计数，FAIL 即 exit 1。**提升缘由**：原驻 `/script`（`.gitignore` 忽略）→ 未纳版本控制，第二十七批起跨 5 批静默失效而无人知、第四十一批再次踩到；经主理人 2026-09-20 批准提升。**每批目录重构后必跑并同步锚点** | 技能 `refactor2026-outline-restructure` §6.5「加强复核」；`script/_r66/review_v2_full.py` 为兼容壳（canonical 在本目录） |
| [sync_review_v2_anchors.py](sync_review_v2_anchors.py) | **加强复核套件锚点同步器（固定脚本，2026-09-20 第四十一批立）**：全卷替换／插卷批次后把 `review_v2_full.py` 的**六族锚点**同步到新结构——①口径族标量（卷/章/节、`li`/`ul.sections`/`h3.chapter`/`id`、卷末述评章、章级述评节、正章、卷分工注、溯源注/`@@`）②结构族（`vol-1..vol-N`、`range(1,N+1)`）③G 族 SPEC **由内容源机械重生成（不手抄）**＋`_gvol` 计数/卷题参数④OLD 零残留清单（只收「旧本独有」的（旧章号＋旧章题）对）⑤J 族备份件（本批 prebak ＋ git 交叉核验提交号）⑥关联族（述评 index 口径行）。批次差异表放 `review_v2_job_<name>.py`（本目录，**逻辑不动**）；`--list` 列可用 job、`--job <name>` dry-run、`--apply` 写盘。**⚠️ 一次性（非幂等）**：已同步态再跑会断言失败＝提示「已同步」。**形制陷阱**：`_gvol` 比对的是**含「第 M 章 」前缀**的章题与**含「M.K 」前缀**的节题，生成器切错会全卷 FAIL 而 detail 却报「逐字一致」 | 技能 `refactor2026-outline-restructure` §6.5「加强复核」；本批差异表见 `review_v2_job_r41.py` |
| [review_v2_job_r41.py](review_v2_job_r41.py) | **加强复核套件锚点同步 job（第四十一批：11 卷替换 ＋ 位置插卷，37 卷 352 章 3023 节）**：只放本批差异表（`GLOBAL` 全局串替换＋期望命中数、`J_OLD_START/END/NEW`、`SPEC_REPLACE`/`OLD_TAG`/`GVOL`/`SPEC_ADD`/`OLDVOL`/`ANCHOR`、`OLD_REF` 用 `<commit>:<path>` 指向本批改动前的提交），逻辑全在 `sync_review_v2_anchors.py`。新增批次照此复制改名并在 `JOB_FILES` 登记一行 | 同上 |

## 程序命令

规则文件中提到的外部程序调用规范，以独立 .md 文件形式存储。

| 文件名 | 用途说明 | 规则引用位置 |
| ------ | -------- | ------------ |
| [autocorrect-mdpadding-markdownlint-清理工具.md](autocorrect-mdpadding-markdownlint-清理工具.md) | AutoCorrect、`md-padding@latest`、`markdownlint2` 三个自动清理工具的调用规范、参数说明、约束（禁批量接受、修改前后各复核一次、最后总复核一次） | 流程规则.md “AutoCorrect 调用规范”、“三轮完整执行规则”小节；写作规则.md “中文引号强制规则”、“行间代码与代码块不可篡改规则”小节；主题规则.md “仅 FreeBSD 内容跨 BSD/UNIX/macOS 扩展规则”小节 |
| [tesseract-ocr-命令.md](tesseract-ocr-命令.md) | Tesseract OCR 命令 `tesseract <input.pdf> <output_basename> -l eng+chi_sim+fra+deu --psm 1` 调用规范、参数说明、OCR 校对规则、OCR 失败处理 | 流程规则.md “文献下载规则” → “OCR 后处理”小节 |
| [pandoc-epub转换命令.md](pandoc-epub转换命令.md) | pandoc 命令 `pandoc <input.epub> -t markdown_strict -o <output.md>` 调用规范、参数说明、与 Tesseract 的关系、校对规则 | 流程规则.md “文献下载规则” → “OCR 后处理”小节 |

## 数据库操作 SQL

规则文件中提到的所有数据库操作 SQL，含 changelog 去重查询与文献全文数据库多表操作。

| 文件名 | 用途说明 | 规则引用位置 |
| ------ | -------- | ------------ |
| [changelog-去重查询.sql](changelog-去重查询.sql) | `changelog.duckdb` `entries` 表去重查询：疑似重复条目查找、时间顺序分组统计、条目数一致性复核、合并/删除冗余条目 | 流程规则.md “changelog 去重规则” → “去重操作规范（SQL 查询辅助）”、“去重后验证要求”小节 |
| [references表操作.sql](references表操作.sql) | `references_fulltext.duckdb` `references` 表操作：SHA-256 精确去重查询、标题+作者+年份模糊去重查询、新增文献入库 INSERT、标记错误文件（`status='rejected'`）、标记已删除文件（`status='deleted'`，追加 `[DELETED YYYY-MM-DD]` 前缀） | 流程规则.md “新增文献自动检测规则” → “去重执行要求”、“元数据验证标准”小节；“重复与错误文档清理规则” → “错误文档判定标准”、“删除后验证”小节 |
| [reference_duplicates表操作.sql](reference_duplicates表操作.sql) | `reference_duplicates` 表操作：写入 SHA-256 精确重复（`exact`）、模糊重复（`fuzzy`）、文件损坏（`corrupted`）、文件无效（`invalid`）四类重复关系；查询主副本优先级 | 流程规则.md “新增文献自动检测规则” → “去重执行要求”小节；“重复与错误文档清理规则” → “重复文档判定标准”、“清理流程”小节 |
| [chapter_matches表操作.sql](chapter_matches表操作.sql) | `chapter_matches` 表操作：高/中/低三档置信度匹配写入（阈值 0.7/0.5）、人工确认后 UPDATE（更新 `primary_chapter`、`match_confidence`、`match_reason`）、按章号查询匹配文献 | 流程规则.md “新增文献自动检测规则” → “章节匹配置信度阈值”、“自动入库与人工复核关系”小节 |
| [chapter_reviews表操作.sql](chapter_reviews表操作.sql) | `chapter_reviews` 表操作：自动入库追加文献综述（`revised_by='auto_ingest'`）、人工确认追加（`revised_by='manual'`）、字数超长（>5000）查询、字数不足（<300）查询、综述存在性判断 | 流程规则.md “新增文献自动检测规则” → “综述追加程序”、“自动入库与人工复核关系”小节 |
| [folder_db_common_schema.sql](folder_db_common_schema.sql) | 7 个文件夹级数据库通用架构定义：5 张通用表（files/blocks/blocks_fts/cross_references/update_log）+ 文件夹专属扩展表的 CREATE 语句；所有 CREATE 语句使用 `IF NOT EXISTS`，可重复执行（幂等） | 流程规则.md “其他文件夹转数据库规则” → “通用 Schema”小节 |
| [folder_db_cross_references.sql](folder_db_cross_references.sql) | 文件夹级数据库交叉引用查询模板：按引用类型统计、按解析状态统计、按目标数据库汇总、失效链接查询、跨库引用查询等 SELECT 模板（非自动执行脚本，使用时须替换参数占位符） | 流程规则.md “其他文件夹转数据库规则” → “交叉引用解析规则”小节 |

## 未实现脚本登记

规则文件中以示例或调用形式提及，但 `script/` 目录中实际不存在的脚本。本目录不为这些脚本创建占位文件，仅作登记。

| 脚本名 | 用途说明 | 规则引用位置 | 状态 |
| ------ | -------- | ------------ | ---- |
| `renumber_subsections_120.py` | 第 120 章子节编号从 116.X 重排为 120.X | 流程规则.md “序号调整例外”小节示例 | 规则引用但未实现 |
| `renumber_subsections_vol5.py` | 第五卷子节编号重排 | 流程规则.md “序号调整例外”小节示例 | 规则引用但未实现 |

## 缺失脚本登记

规则文件引用但 `script/` 目录与 `脚本与命令/` 目录均不存在、且 git 历史（`/script` 在 .gitignore 中未纳入版本控制，可追溯提交有限）中无记录、全部备份目录（`script/_backup_*`、`script/_staging/*`）中亦无副本的脚本。**本登记仅作如实记录，不臆造脚本内容。**

### A. 已从规则删除的核心验证脚本（8 个）

以下 8 个脚本完全缺失且无法恢复，经用户决策**已从规则文件删除引用**，相关验证改为人工执行（详见流程规则.md“大纲节号连续性规则”“Frontmatter 元数据一致性规则”“GitBook 目录同步规则”“结构性变更后验证清单”各节）。

| 脚本名 | 原用途说明 | 原规则引用位置 | 现处理 |
| ------ | ---------- | -------------- | ------ |
| `analyze_section_gaps.py` | 全书节号缺口扫描 | 流程规则.md “大纲节号连续性规则”→“检测命令”、“结构性变更后验证清单”第 3 项 | 已删除引用，改人工核查 |
| `verify_summary_frontmatter.py` | frontmatter chapter/id/volume 一致性检测 | 流程规则.md “Frontmatter 元数据一致性规则”→“检测命令”、“结构性变更后验证清单”第 4 项 | 已删除引用，改人工核查 |
| `verify_summary_renumber.py` | 章号连续性+链接存在性+磁盘↔SUMMARY 双向吻合检测 | 流程规则.md “结构性变更后验证清单”第 1、2、6、7 项 | 已删除引用，改人工核查 |
| `batch_update_overviews.py` | 批量更新概述.md 节索引 | 流程规则.md “大纲节号连续性规则”→“修复方式”、“结构性变更后验证清单”第 8 项 | 已删除引用，改人工更新 |
| `_regen_summary_after_renumber.py` | 从磁盘重建大纲 SUMMARY（348 章） | 流程规则.md “结构性变更后验证清单”→“触发场景”、“相关脚本索引” | 已删除引用，改人工重建 |
| `_sync_gitbook_summary.py` | 重新生成 `05-卷册大纲/SUMMARY.md` | 流程规则.md “GitBook 目录同步规则”→“同步执行命令” | 已删除引用，改人工同步 |
| `_delete_source_files.py` | 源文件清理脚本（数据库唯一内容载体） | 流程规则.md “其他文件夹转数据库规则”→“源文件清理规则”→“清理脚本用法” | 已删除引用，改人工清理 |
| `sync_script_copies.py` | 确保 `script/` 与 `脚本与命令/` 两处副本一致（SHA-256 校验） | 流程规则.md “其他文件夹转数据库规则”→“精简与重构记录”（2026-07-31） | 已删除引用 |

### B. 历史一次性脚本（约 20 个，2026-07 至 08 期间执行完毕，未留存副本）

| 脚本名 | 用途说明 | 规则引用位置 |
| ------ | -------- | ------------ |
| `audit_research_gaps.py` | 审计全部 M.N 节文献/史料字段缺口 | 研究缺口.md 头部声明 |
| `gen_research_gap_doc.py` | 生成/更新研究缺口清单 | 研究缺口.md 头部声明、5.3 复用脚本 |
| `insert_literature.py` / `insert_literature2.py` | 文献入库（materials + references） | 研究缺口.md 5.3 复用脚本 |
| `fill_macos_gaps.py` | 批量补 macOS 相关章史料 | 研究缺口.md 5.3 复用脚本 |
| `resolve_daikao.py` | 批量消解待考注释 | 研究缺口.md 5.3 复用脚本 |
| `refactor_folder_db_schema.py` | 文件夹级数据库 Schema v1.0→v1.1 精简 | 流程规则.md “精简与重构记录” |
| `refactor_research_notes_retry2.py` | research_notes.db 锁定后第二次清理 | 流程规则.md “精简与重构记录” |
| `embed_b_to_outlines.py` / `embed_reports_to_outlines.py` / `embed_tech_to_chapters.py` | B 系列结论/分析报告/技术结论嵌入大纲 | 功能对比与数据库回写规则.md “分析结果写入大纲规范” |
| `_gen_catalog_30_categories.py` | 参考文献总目 30 类别导出 | 流程规则.md “参考文献总目与数据库同步回填” |
| `_fix_from_catalog.py` | 总目→数据库字段回填 | 流程规则.md “参考文献总目与数据库同步回填” |
| `_scan_banned_outline_20260805.py` / `_tier_banned_refs_20260805.py` / `_mark_ref1592_banned_20260805.py` / `_reg_official_refs_2511_2515_20260805.py` / `_reg_official_refs_2516_2519_20260805.py` | 2026-08-05 禁引来源清理首轮执行脚本 | 考据规则.md “文献分级 source_tier 与禁引来源清理规则”→“四、2026-08-05 首轮执行结果” |

### C. 副本源文件缺失（历史状态；2026-09-18 起不再具实质影响）

原登记：`脚本与命令/` 目录下 13 个 .py 副本中 11 个在 `script/` 的源文件已缺失。**现状（2026-09-18 复核）**：本目录 52 个 `.py` 中，仅 **3 个**在 `script/` 下存在同名文件——`assemble_index.py`（仅存于备份目录 `script/_r66/_bak_index_format_20260918/`）、`wo007_idempotency.py`（`script/_outline_audit_20260906/`）、`write_to_outlines.py`（`script/` 根）；其余 **49 个无同名对应**。

**该风险的处置（2026-09-18）**：本目录整体纳入版本控制后，**本目录自身即为权威副本**，「`script/` 原文件缺失导致不可恢复」的风险已消除——原登记的 11 个缺失副本其内容完整并已随本次纳管进入版本库。规则「副本关系」中「从 `script/` 复制、原文件保持不变」的旧约束相应废止，改见下节。

## 与 `script/` 目录的关系

- **`script/` 目录**：项目根目录下的临时脚本与中间文件归档（仅放置可临时、随时删除的中间过程产物，不放置长期频繁使用的固定脚本；历史遗留脚本保留原样，不主动清理）。仍由 `.gitignore` 的 `/script` 规则整体排除出版本控制
- **`脚本与命令/` 目录**：规则文件夹下的规则引用可执行资源（本目录），仅收录规则文件中明确引用的可执行资源（长期频繁使用固定脚本的正式存放位置），与规则文件形成「规则 + 可执行资源」的完整自洽单元。**本目录自 2026-09-18 起为权威存放位置并纳入版本控制**
- **🔴 纳管缘由与代价实证（2026-09-18）**：本目录原按「整体不进版本库」的历史安排（见 `.workbuddy/memory/2026-09-11.md`）由 `.gitignore` 的全局 `*.py` 规则排除。**该安排的代价已有实证**：见本文件「缺失脚本登记 → A. 已从规则删除的核心验证脚本（8 个）」——8 个规则引用的核心验证脚本因「`/script` 在 .gitignore 中未纳入版本控制，可追溯提交有限」而**永久丢失、无法恢复**，相关验证被迫改人工执行。八件门禁建立后，门禁脚本本身成为规则契约的一部分，不可再承受同类丢失。故于 `.gitignore` 增设**定向例外** `!00-编纂规则与格式规范/01-规则/脚本与命令/*.py`——保留「`script/` 临时脚本不入库」的原意，仅保护规则引用的固定脚本
- **副本关系（2026-09-18 起）**：本目录下的 `.py` 为**权威副本**，不再要求与 `script/` 保持同步（仅 3 个在 `script/` 有同名文件，且多为备份件）；反向同步（本目录 → `script/`）不执行
- **新增脚本流程**：当规则文件新增引用某脚本时，须将该脚本放入本目录，并在本 README 索引中追加条目；若为门禁脚本，还须在 `流程规则.md` 与 `CLAUDE.md` 修改规范中登记，并按「判据非空」纪律以负向用例实测后方可采信

## 文件编码与格式

- 所有文件使用 UTF-8 无 BOM 编码
- 所有文件使用 LF 换行符
- 所有 .py 副本文件保留原脚本的 shebang 与编码声明（如有）
