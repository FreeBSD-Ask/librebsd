# 2026-08-18 kaoju_records 误删事故记录（已于同日恢复）

> 本记录为数据事故留痕（非史实考据），依 0 信任原则如实登记成因链、损失范围与恢复尝试，不隐瞒、不淡化。**结局：同日经回收站救援全部恢复，见文末“恢复结果”**。

## 查证来源

- 事故实测：`original_sources.db` `kaoju_records` 表由 570 条变为 3 条（保留 604 许可证考据 1 条原始记录 + 今日脚本自动抽取 603/605 各 1 条），569 条文本被 DELETE 且已提交（`script/_kaoju_damage_20260818.py` 实测）。
- 成因链（三因叠加）：
  1. 2026-08-17 深夜 FK 加固（refactor2026 detailed-plan 步骤 6 方案）将 568 条挂 deleted 墓碑的考据记录重指向 active 文件 `file_id=603`（`06-考据记录/index.md`）；
  2. 2026-08-18 `build_folder_databases.py --update-file` 刷新 `index.md` 时，其“级联刷新”设计逻辑含 `DELETE FROM kaoju_records WHERE file_id=?`（脚本第 2083-2109 行），恰好清空 file_id=603 的全部考据记录（568+1=569 条）；
  3. 当日备份清理（用户决策，删除 65 目录 42.59 GB）先行删除了含 `_backup_20260818_kaoju_fk/original_sources.db` 在内的全部数据库备份，事故后无备份可回滚。
- 责任认定：FK 加固方案选择“重指向 index.md”时未识别 `--update-file` 级联删除扩展表记录的交互风险，属方案设计疏漏（agent 责任）；备份删除为用户明示决策，但其与事故的时序叠加放大了后果。

## 交叉验证方法

- 恢复路径穷尽尝试（全部实测、如实登记）：
  1. 磁盘副本搜索：全项目仅剩 1 个 `original_sources.db`，无 `-wal`/`-journal` 残留（checkpoint 已落盘）；
  2. 跨库文本搜索：以被删记录特征串（"阴性结果：未发现明确挪用关系的方向""概念挪用，代码独立""第一轮 WebSearch 检索"）检索 `research_notes.db`（48.7 万 blocks）、`references_fulltext.db`（99 万 blocks）、`original_sources.db` blocks（50 块）——仅 `research_notes.db` file 1648（Linux 文化挪用研究正文，17 块）命中 4 块正文，可部分重建挪用研究主题的考据叙述；其余特征串 0 命中；
  3. 库内结构核查：`blocks` 表 50 块全挂 active 文件，601 个 deleted 墓碑无正文块（与 2026-08-01 源文件清理时"正文不入 blocks、抽取三字段入 kaoju_records 为唯一载体"的架构一致）；
  4. 卷影/文件恢复：物理盘为 SSD×2（TRIM），`vssadmin` 需管理员权限未获快照列表；rmtree 物理删除不进回收站；SSD+TRIM 下第三方恢复工具成功率趋近于零，未冒进执行。

## 存疑判定依据

- **损失实质**（事故时点评估，结局见文末“恢复结果”）：被删 569 条系 2026-08-01 源文件清理时从 601 个考据类 md 抽取的“查证来源/交叉验证方法/存疑判定依据”三字段摘要，是该批 2026-08-01 前考据内容的**唯一结构化留存形态**。本次事故后：
  - 可部分重建：Linux 文化挪用研究等主题的正文底稿仍在 `research_notes.db` blocks（如 file 1648），考据叙述可据正文重写；
  - 实质灭失：无正文冗余的主题之三字段文本（具体主题域分布因墓碑 folder_path 聚类查询失败未完成清点，[存疑脚注] 待专项清点后补充损失清单）；
  - 未受影响：`06-考据记录/` 现存 35 个考据 md（2026-08-04 后新增，含 604/605 两条在表记录）、`08-核查报告与多轮复核/` 全部报告、其余 15 个正式库。
- **处置约束**：事故后已停止对 `original_sources.db` 的一切写操作；`build_folder_databases.py` 的级联删除逻辑与“考据记录重指向 index.md”的叠加风险已识别，任何后续 FK/挂靠方案须先审计调用方级联行为。

## 恢复结果（2026-08-18 同日）

- **转机**：用户提示查询回收站，实测发现 2026-08-15 23:52 曾有两份 original_sources 数据库备份被删入回收站且未被清空（`$Recycle.Bin` 实体 `$R` 文件完好）：`original_sources.db.backup_20260812_pre_refactor`（11,206,656 B）与 `original_sources.db.tmp_fix`（11,177,984 B）——此前事故登记“不可恢复”时仅排查了项目目录内副本与 SSD 恢复工具，**漏查回收站**，属评估疏漏，如实更正。
- **验证**：两副本均 `integrity_check=ok`、`kaoju_records` 完整 570 条（id 1-570）、file_id 为原始墓碑挂靠（非 08-17 错误改指的 603）、样本内容与事故前逐字一致（`script/_recycle_verify_20260818.py` 实测）。
- **执行**：救出至 `script/_recovery_20260818/`（含事故态 3 条快照留档）；自 08-12 快照回插 id 1-569 共 569 条，id 570 与当前库逐字段一致保留当前版本；update_log 登记 `kaoju_records_restore`（`script/_kaoju_restore_20260818.py`）。
- **恢复后状态**：总数 572 条（原始 570 + 事故流程新增 571/572 两条抽取记录）；568 条回挂**原始 deleted 墓碑挂靠**——较事故前（08-17 全部改指 603）更忠实原始结构，且天然免疫 `--update-file index.md` 的级联误删（墓碑文件不再被 update-file 触发）；integrity=ok；`三字段非空 560 条`（与快照基线一致）。
- **遗留微冗余（如实登记）**：file_id=603 现有 2 条（原始 index.md 抽取记录 + 事故流程重抽的 id 572），语义为同一源文件两次抽取快照，保留不删；若未来再执行 `--update-file index.md`，二者将被级联删除并按新内容重抽，属脚本设计内行为。
