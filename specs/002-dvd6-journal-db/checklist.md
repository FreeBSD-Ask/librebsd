# Checklist: dvd6 期刊四库建库 → 全文库入库 → 入大纲（验收检查点）

**Feature**: specs/002-dvd6-journal-db | **Created**: 2026-10-05 | **依据**: spec.md（FR-001–FR-011、SC-001–SC-007、Edge Cases）、tasks.md（T001–T039）、quickstart.md

**语义**：每条由复核人二值判定（通过／不通过）；`[x]` 仅在复核通过后勾选。史料考据类判据（Check 15–22、28–33）含证据锚点与原文照录要求。

## 一、实现完整性（交付物存在且闭合）

- [ ] Check 1: 四库建成本地暂存 `C:\ddj_stage\`（ddj/cuj/sa/tpj.duckdb），推送后 `dvd6/Website/ddj/` 下存在同 4 库且 sha256 双侧一致，无第 5 个库（来源：spec FR-001／Task T005、T038）
- [ ] Check 2: 每库含 7 张表：journal_meta、issues、articles、source_files、ads、figures、build_log，列名与 contracts/ddj-db-schema.md 一致（来源：Task T005／contracts）
- [ ] Check 3: 侦察产物四件齐备：issues_inventory.json、articles_inventory.json、fulltext_schema.json、ads_rules.md 均在 `script/_ddj_out/` 且可被独立脚本回读（来源：Task T001–T004）
- [ ] Check 4: 四库 issues 期号集合与磁盘实测差集为空（CUJ 1990–2006 月包、DDJ 1988–2009 年包、SA 1992–2006、TPJ 全部 tpjNNNN 包），source/articles 两侧覆盖差异在 coverage_gap.md 有结论（来源：spec SC-001／Task T009–T012、T025）
- [ ] Check 5: 抽样 ≥12 期（每刊 ≥3 期）库内 articles 数＝articles 树该期实测文章数（来源：spec SC-002／Task T025）
- [ ] Check 6: 抽样 3 文 body_text 与源 HTML 转文本逐字一致（含标题层级与段落，无 HTML 标签残留）（来源：spec SC-002／Task T025）
- [ ] Check 7: 抽样 3 期 source_files 与解压文本逐字一致，archive_layer 记录外层包＋内层包层级（来源：spec FR-006／SC-002／Task T017–T020、T025）
- [ ] Check 8: ads 表非空且每条 ad 可归属到期（issue_id 非空），ad_kind 与 ads_rules.md 判据类目一致（来源：spec FR-005／Task T024）
- [ ] Check 9: figures 表无 uncertain 行；disposition=transcribed ⇒ transcription_text 非空；disposition=base64 ⇒ base64_data 可解码；skipped 行均有 disposition_reason（来源：spec FR-007／SC-004／Task T021–T023）
- [ ] Check 10: build_log 每批 note 记录处理数/跳过数/二进制命中数，总数与侦察清单闭合（来源：spec SC-007／Task T037）
- [ ] Check 11: 每库 refs 表行数＝articles 行数，著录为 GB/T 7714 期刊格式且期号/年份与 issues 一致（来源：spec FR-008／Task T027）
- [ ] Check 12: 每库 summaries 无缺行且含 topic_keywords 与 important_excerpts（原文照录）；key_facts.reference_id 全部回指本库 refs，悬空 0（来源：spec FR-008／Task T028–T029）
- [ ] Check 12b: 新增 卷末书目述评 bullet 采用 `- **ref <DB>-<id>**｜` 锚点且全部可回指四库 refs（来源：spec FR-009／Task T034）
- [ ] Check 13: 终报 script/_ddj_out/final_report.md 存在，含四刊覆盖表、体量统计、缺陷与豁免清单、存疑挂账（来源：Task T037）
- [ ] Check 14: feature 四件（spec/plan/tasks/checklist）与 research 追记已按 pathspec 限定提交，git show --stat 回读一致；script/ 与 *.duckdb 不在提交内（来源：Task T038）

## 二、需求覆盖（FR 逐条）

- [ ] Check 15: 库名与期刊一一对应且全部位于 ddj 文件夹——4 个库分别承载 DDJ/CUJ/SA/TPJ 全部内容，无合并无多建（来源：spec FR-001）
- [ ] Check 16: 全量遍历证明：issues_inventory（source 树）与 articles_inventory（articles 树）的每一条在库内有对应 issues 行，两树无被跳过的期（来源：spec FR-002）
- [ ] Check 17: 元数据完整：抽样文章的 title/subtitle/author/author_bio/section 五字段与源页逐项一致，section 与 TOC 分节名一致；TOC 未分节者的归类依据在 build_log 可查（来源：spec FR-003）
- [ ] Check 18: 正文照录未改写：抽样 body_text 与源页人工比对——无重排、无改字、无段落合并；目录页/编者论坛/读者来信/新产品栏内容有落库行（来源：spec FR-004；证据锚点：库表 article_id ↔ 源页文件名）
- [ ] Check 19: 广告存储：文字广告 ad_text 与源页逐字一致；图片广告有 figure_id 关联且 figures 行完整（来源：spec FR-005）
- [ ] Check 20: 源码解压关联：抽 3 个内嵌包，其全部文本叶子在 source_files 有行且 file_name 含包层级；article_id 为 NULL 的行在 build_log 记“未能建立映射”而非静默丢关联（来源：spec FR-006；证据锚点：archive_layer + file_name ↔ 解压实测）
- [ ] Check 21: 图片 LLM 直转无本地模型：抽 3 件 transcribed 图，其 transcription_text 与原图 Read 复核一致，且派单/留痕无任何本地 OCR 模型调用记录（来源：spec FR-007；证据锚点：figure_id + image_name ↔ 原图）
- [ ] Check 22: 艺术图 base64：抽 2 件 base64 图，解码字节 magic 头与 image_format 一致、与原文件字节一致（来源：spec FR-007；证据锚点：figure_id）
- [ ] Check 23: 无意义内容零记录：全库无完整磁盘路径字段值（assert_no_paths 0 命中）、无站点导航文本、无 .DS_Store 内容行（来源：spec FR-003／Task T007）
- [ ] Check 24: 幂等三连：四库重建重跑、规则补齐（refs/summaries/key_facts）重跑、大纲重跑各 0 新增 0 重复（重跑前后行数断言，判据非空）（来源：spec FR-010）
- [ ] Check 25: 大纲两层边界：SUMMARY.md 与任何章正文文件在本件 git diff 中 0 改动；改动面仅四库 key_facts.related_chapter＋各卷卷末书目述评.md（来源：spec FR-009）
- [ ] Check 26: 成本豁免执行：tasks 执行记录显示 40 路滚动派发与多轮复核真实发生（派单记录/回报归档可查），同时每次写盘有写前判据与写后独立回读断言（来源：spec FR-011）

## 三、边界与异常（Edge Cases 逐条）

- [ ] Check 27: 嵌套压缩包：CUJ 月包内作者 zip、DDJ 年包内 zip 全部展开到文本叶子，无“以嵌套包为记录终点”的行（来源：spec Edge Cases）
- [ ] Check 28: 二进制零命中：assert_no_binary 全库 0 命中；.exe/.scr/.DS_Store 仅以 build_log 命中数存在；正文文字内提及的文件名（如 RAHNER.EXE）随 body_text 保留（来源：spec Edge Cases／FR-006）
- [ ] Check 29: 编码混杂：抽样含高位字节的 source_files 行 encoding 字段非空且内容可读（无替换字符 U+FFFD），行尾统一 LF（来源：spec Edge Cases／research R4）
- [ ] Check 30: 图片判别纪律：壳图 skipped 清单与站点导航件实测一致；判别存疑者曾有 uncertain 挂账记录并已清零或复核定性，无“未判即入库”（来源：spec Edge Cases／research R5）
- [ ] Check 31: 整页图片广告按 Check 19/21 双路径处置，无“图片广告既无文本也无图挂”悬空（来源：spec Edge Cases）
- [ ] Check 32: 站点壳件零入库：forms/、zoom/、tree.htm、navbar.htm、border.htm 无内容行；.html.old 不产生重复文章行（来源：spec Edge Cases／Task T016）
- [ ] Check 33: SA 清单页并入：抽 2 组 aN_lN.htm，其内容在对应文章的 body_text 或 source_files 中逐字存在，且未另立 article 行（来源：spec Edge Cases／Task T015）
- [ ] Check 34: 覆盖缺口如实：articles 树未覆盖年份（DDJ 2003–2009 等）的 issues 行 toc_text 如实标注，无臆造目录内容（来源：spec Edge Cases／Task T009）
- [ ] Check 35: 期刊时间归一：抽样 3 期 year/month 结构化字段与 TITLE/tar 文件名实印月份一致，issue_label 保留原文（来源：spec Edge Cases）

## 四、既有功能未回归

- [ ] Check 36: references_fulltext.duckdb 零触碰：本件对其 0 写入（只读侦察＋写前备份 pre-ddj-20261005 除外），他线当日写入的 17 篇 DDJ 386 系列行未被我改（来源：主理人 2026-10-05 修正）
- [ ] Check 37: 卷末书目述评既有 bullet 逐字未动（新增仅为追加，本批 `- **ref <DB>-` 判重记录可查）；宿主卷其他节未动（来源：spec FR-009／Task T034）
- [ ] Check 38: 大纲门禁全绿：audit_disk_terminology.py（05-卷册大纲 改动后必跑）、audit_evidence_level_labels.py（如触及）、audit_markdown_lint.py（闸面触及件）退出码全 0（来源：Task T035）
- [ ] Check 39: script/ 临时脚本未入 git（git status 对 script/ 无新增跟踪文件），库文件 *.duckdb 不在版本控制（来源：CLAUDE.md 临时文件规则／Task T038）
- [ ] Check 40: 全链留痕可审计：任抽 1 条大纲 bullet 可经 ref → fulltext_blocks → 四库 source_files/articles → archive_layer+issue_label 追溯到源页面/解压文件，链条各环一致（来源：spec SC-007／quickstart 场景 7）
