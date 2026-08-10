# 脚本与命令索引

本文件索引 `00-编纂规则与格式规范/01-规则/脚本与命令/` 目录下所有可执行资源（脚本副本、程序命令说明、数据库操作 SQL），列出每条资源的文件名、用途说明与规则引用位置。本目录是规则文件（考据规则.md、写作规则.md、流程规则.md、主题规则.md、释读规则.md）引用的所有可执行资源的独立存储位置，与 `script/` 目录中的原脚本副本形成“规则自洽单元 + 历史脚本归档”的分工关系。

## 脚本文件

规则文件中引用的现存 Python 脚本副本（共 13 个 .py 副本，从 `script/` 目录复制，原文件保持不变）。

| 文件名 | 用途说明 | 规则引用位置 |
| --- | --- | --- |
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
| [sync_cross_references_after_cleanup.py](sync_cross_references_after_cleanup.py) | 交叉引用同步脚本：在重复源文件清理与跨库全局去重完成后，扫描 `05-卷册大纲/`、`10-交叉索引/`、`11-元数据接口/` 下所有 `.md/.csv/.json` 文件（`06-正式书稿/` 已随 2026-08-04 禁止编纂正文决策移除，不再扫描），将指向已删除/已合并副记录的引用更新为指向主记录；支持 `--dry-run`/`--all` 两种模式 | 流程规则.md “其他文件夹转数据库规则” → “交叉引用同步”小节 |
| [optimize_folder_databases.py](optimize_folder_databases.py) | 文件夹级数据库优化脚本：对 7 个数据库执行 Schema 优化（创建 schema_meta 表 + 9 个预定义索引 + 删除空扩展表 + 回填 update_log）、幽灵块清理（删除 deleted 文件的 blocks/blocks_fts 行，sacred 例外）、VACUUM 空间回收三种操作；支持 `--schema`/`--ghost-blocks`/`--vacuum`/`--all`/`--dry-run` 五种模式 | 流程规则.md “数据库 Schema 优化规则” → “Schema 优化与空间回收”小节 |

## 程序命令

规则文件中提到的外部程序调用规范，以独立 .md 文件形式存储。

| 文件名 | 用途说明 | 规则引用位置 |
| --- | --- | --- |
| [autocorrect-mdpadding-markdownlint-清理工具.md](autocorrect-mdpadding-markdownlint-清理工具.md) | AutoCorrect、`md-padding@latest`、`markdownlint2` 三个自动清理工具的调用规范、参数说明、约束（禁批量接受、修改前后各复核一次、最后总复核一次） | 流程规则.md “AutoCorrect 调用规范”、“三轮完整执行规则”小节；写作规则.md “中文引号强制规则”、“行间代码与代码块不可篡改规则”小节；主题规则.md “仅 FreeBSD 内容跨 BSD/UNIX/macOS 扩展规则”小节 |
| [tesseract-ocr-命令.md](tesseract-ocr-命令.md) | Tesseract OCR 命令 `tesseract <input.pdf> <output_basename> -l eng+chi_sim+fra+deu --psm 1` 调用规范、参数说明、OCR 校对规则、OCR 失败处理 | 流程规则.md “文献下载规则” → “OCR 后处理”小节 |
| [pandoc-epub转换命令.md](pandoc-epub转换命令.md) | pandoc 命令 `pandoc <input.epub> -t markdown_strict -o <output.md>` 调用规范、参数说明、与 Tesseract 的关系、校对规则 | 流程规则.md “文献下载规则” → “OCR 后处理”小节 |

## 数据库操作 SQL

规则文件中提到的所有数据库操作 SQL，含 changelog 去重查询与文献全文数据库多表操作。

| 文件名 | 用途说明 | 规则引用位置 |
| --- | --- | --- |
| [changelog-去重查询.sql](changelog-去重查询.sql) | `changelog.db` `entries` 表去重查询：疑似重复条目查找、时间顺序分组统计、条目数一致性复核、合并/删除冗余条目 | 流程规则.md “changelog 去重规则” → “去重操作规范（SQL 查询辅助）”、“去重后验证要求”小节 |
| [references表操作.sql](references表操作.sql) | `references_fulltext.db` `references` 表操作：SHA-256 精确去重查询、标题+作者+年份模糊去重查询、新增文献入库 INSERT、标记错误文件（`status='rejected'`）、标记已删除文件（`status='deleted'`，追加 `[DELETED YYYY-MM-DD]` 前缀） | 流程规则.md “新增文献自动检测规则” → “去重执行要求”、“元数据验证标准”小节；“重复与错误文档清理规则” → “错误文档判定标准”、“删除后验证”小节 |
| [reference_duplicates表操作.sql](reference_duplicates表操作.sql) | `reference_duplicates` 表操作：写入 SHA-256 精确重复（`exact`）、模糊重复（`fuzzy`）、文件损坏（`corrupted`）、文件无效（`invalid`）四类重复关系；查询主副本优先级 | 流程规则.md “新增文献自动检测规则” → “去重执行要求”小节；“重复与错误文档清理规则” → “重复文档判定标准”、“清理流程”小节 |
| [chapter_matches表操作.sql](chapter_matches表操作.sql) | `chapter_matches` 表操作：高/中/低三档置信度匹配写入（阈值 0.7/0.5）、人工确认后 UPDATE（更新 `primary_chapter`、`match_confidence`、`match_reason`）、按章号查询匹配文献 | 流程规则.md “新增文献自动检测规则” → “章节匹配置信度阈值”、“自动入库与人工复核关系”小节 |
| [chapter_reviews表操作.sql](chapter_reviews表操作.sql) | `chapter_reviews` 表操作：自动入库追加文献综述（`revised_by='auto_ingest'`）、人工确认追加（`revised_by='manual'`）、字数超长（>5000）查询、字数不足（<300）查询、综述存在性判断 | 流程规则.md “新增文献自动检测规则” → “综述追加程序”、“自动入库与人工复核关系”小节 |
| [folder_db_common_schema.sql](folder_db_common_schema.sql) | 7 个文件夹级数据库通用架构定义：5 张通用表（files/blocks/blocks_fts/cross_references/update_log）+ 文件夹专属扩展表的 CREATE 语句；所有 CREATE 语句使用 `IF NOT EXISTS`，可重复执行（幂等） | 流程规则.md “其他文件夹转数据库规则” → “通用 Schema”小节 |
| [folder_db_cross_references.sql](folder_db_cross_references.sql) | 文件夹级数据库交叉引用查询模板：按引用类型统计、按解析状态统计、按目标数据库汇总、失效链接查询、跨库引用查询等 SELECT 模板（非自动执行脚本，使用时须替换参数占位符） | 流程规则.md “其他文件夹转数据库规则” → “交叉引用解析规则”小节 |

## 未实现脚本登记

规则文件中以示例或调用形式提及，但 `script/` 目录中实际不存在的脚本。本目录不为这些脚本创建占位文件，仅作登记。

| 脚本名 | 用途说明 | 规则引用位置 | 状态 |
| --- | --- | --- | --- |
| `renumber_subsections_120.py` | 第 120 章子节编号从 116.X 重排为 120.X | 流程规则.md “序号调整例外”小节示例 | 规则引用但未实现 |
| `renumber_subsections_vol5.py` | 第五卷子节编号重排 | 流程规则.md “序号调整例外”小节示例 | 规则引用但未实现 |

## 与 `script/` 目录的关系

- **`script/` 目录**：项目根目录下的临时脚本与中间文件归档（2026-08-11 修订：仅放置可临时、随时删除的中间过程产物，不放置长期频繁使用的固定脚本；历史遗留脚本保留原样，不主动清理）
- **`脚本与命令/` 目录**：规则文件夹下的规则引用可执行资源副本（本目录），仅收录规则文件中明确引用的可执行资源（长期频繁使用固定脚本的正式存放位置），与规则文件形成“规则 + 可执行资源”的完整自洽单元
- **副本关系**：本目录下 13 个 .py 文件均为 `script/` 目录中对应文件的副本（内容完全一致），原 `script/` 目录中的源文件保持不变（注：截至 2026-08-11 复核，其中 11 个源文件在 `script/` 已缺失，见 `00-编纂规则与格式规范/01-规则/README.md` 与核查报告）
- **新增脚本流程**：当规则文件新增引用某脚本时，须将该脚本从 `script/` 复制副本到本目录，并在本 README 索引中追加条目

## 文件编码与格式

- 所有文件使用 UTF-8 无 BOM 编码
- 所有文件使用 LF 换行符
- 所有 .py 副本文件保留原脚本的 shebang 与编码声明（如有）
