# 清理线长线计划（_PLAN_CLEANUP_20260923）

> 创建：2026-09-23（第 1 轮当日闭环）。本文件是存储库清理战役的长线计划与续跑入口，
> 与 `_PLAN_LONGTERM.md`（各史料战役）平行，互不覆盖。续跑新会话只需读本文件顶部。

## 〇、用户裁定口径（长期生效，后续轮次一律照此）

1. **逐个审阅必要性**：临时文件、不再使用的过时文件/脚本、过度备份、不再需要的备份才清；
   内容目录（书稿、史料、核查记录）与活跃战役状态一律不动。
2. **无论是否跟踪都要处理**（tracked / untracked 同口径）；tracked 文件清理后 git 显示删除即常态，可恢复。
3. **跳过目录**：`05-卷册大纲/`；`shenyue/jianyi_by_volume/`、`shenyue/jianyi_by_volume_next1/`（目录审阅任务在用）。
4. **24 小时不清理**：按调用时间判断，mtime 距今 < 24 小时的一律保留（含当日的分析件、临时目录、任务书副本）。
5. **并行会话甄别**：任何目录/文件 mtime 距今 < 2 小时＝HOT，禁触碰（有会话正在写）。
   处置前必查活跃交接书引用（见 §三 必留清单）。
6. **子代理**：允许 40 路随时可派（侦察/逐目录审阅用）；判读结论以磁盘为准，子代理回报一律复核。
7. **移入回收站**（非直接删除）：整批先移入 `_recycle_stage_YYYYMMDD/` 暂存并写
   `_MANIFEST_原始路径.txt`（记录原始位置对应关系），再用 PowerShell
   `[Microsoft.VisualBasic.FileIO.FileSystem]::DeleteDirectory(<stage>,'OnlyErrorDialogs','SendToRecycleBin')`
   一次性入回收站。恢复时从回收站还原暂存目录，按 manifest 放回。

## 一、第 1 轮（2026-09-23，本会话）已闭环

**清出 ≈10.1 GB**，全部经 `_recycle_stage_20260923` 入回收站：

| 组 | 数量 | 体积 | 内容 |
|---|---|---|---|
| script_dirs | 391 | 7.6G | `_backup_*` 340 个（含 09-07 两个大备份 4.5G，均被 git 历史/更新备份取代）；陈旧工作目录 44 个（_mail_analysis、_db_deep_analysis、_podcast_semantic_review、_git_recover_verify、_ov_whisper_* 模型 1G、build/dist 等）；误建目录（` _db_row_mining` 带空格、_d、script_inner） |
| script_files | 2501 | 1.6G | script/ 顶层过时一次性脚本与输出（mtime < 2026-09-20；排除 S-me* 交付物与活跃件） |
| duckdb_bak | 6 | 859M | 04-现代研究文献 过期 claim 回滚点（prebak-fqb038/039、before_fq_b048~b051，已被 09-23 最新回滚点取代） |
| root | 11 | 2.4M | 24h 前旧输出（_cand/_p2/_p3/_q/_hits 等 9 个）+ tmp_cls/ + .playwright-mcp/ |

**保留未动**（本轮甄别结论，后续轮沿用）：`script/_db_row_mining`（8.5G，mail2d 全线工作目录）、
`review_logs/`（根 + script 内，H2/H3 输出根，18:19 仍在写）、`shenyue/`（复核线 + jianyi 在用）、
`05-卷册大纲/`、`12-数据库备份/`（28G 专用备份区，见 §二 轮 3）、今日 24h 内全部分析件与临时目录、
`_t_b007/008/009.md`＋`_b007_copy.md`（b007–b009 任务书副本，当日在用）、`_p3_body/_p3_narr.txt`（H3 p3 叙述在用）、
`_final2827.md`、`subagents_fsdevel/`（fsdevel 54 条待入库）、`_tmpndb11/`、`_tmp_fix/`、`_fix7/`、`tmp_b51/`、
S-me* 交付物、`_PLAN_*`、`_usenet_keyword_hits.json`（keyword-hits 整改待批引用）、`_mine_*.json`（MAIL_INSIGHT 产物）、
`_既有缺陷清单.json`、`_watch_git.*`、全部交接/断点文件、04-现代研究文献 现役 .duckdb 与 09-23 回滚点。

## 二、后续轮次（按收益排序；每轮开工前重跑 §〇 判定）

- **轮 2：script/_db_row_mining 内部**（8.5G，活跃）——40 路子代理逐目录审；只清已完成批次的
  分件 tsv/dump/中间件与过期 .bak，交接书/台账/任务书/状态机/在途批次分件一律留；
  `_rebuild_test.duckdb` 类 test 件如仍在顶层可清。开工前核对 `_RESUME_H2/H1/H4.md`＋`_HANDOFF_H3/H5.md` 在途断点。
- **轮 3：12-数据库备份/**（28G）——40 路子代理逐备份审阅：git 重写离线包（git-history-backup-20260911）
  与 12-数据库备份/git-history-backup-20260911/ 等专属备份区按「备份目的是否已完成＋是否有更新替代」裁定；
  本轮未动，需用户确认口径后开工。
- **轮 4：04-现代研究文献/** 剩余（文献下载目录、.mimosa、historical_claims.duckdb.tmp 09-14 旧临时）——
  现役 .duckdb 与 09-23 回滚点不动；`*.bak-20260923-h5gk4/5/6` 等 24h 内件到期后可并入下一轮。
- **轮 5：shenyue/**（683M）——待 jianyi 目录审阅任务交付 `jianyi.md` 后开：`jianyi_by_volume`（旧轮）
  与 `jianyi_by_volume_next1`（新轮＋_audit）二选一留新，`_s7*_run.log`、`out2~out10` 等逐目录审；
  协议资产（_s25/_s50~_s56 等）与 review/ 交接件必留。
- **轮 6：03-原始史料库/**（209G，54.5 万文件）——纯史料区，只清各库 `raw/git/*/git/0.git/hooks/*.sample`
  类克隆残渣与 mining 区过期临时；动工前必须与各战役源库只读约定核对。

## 三、必留清单（本轮据全部交接书提取；清理裁定前逐条核对）

1. 交接/断点/计划件：根 `_PLAN_LONGTERM.md`、`_PLAN_20260921.md`；`script/_db_row_mining/_HANDOFF_*.md`（H1–H5、
   EVENTWINDOW、dakuA–E、MAIL2D 0917/0918、USENET_CLOSURE）、`_RESUME*.md`、`_READ_TASK_*`、`_NARR_TASK_*`、
   `_FQ_B062_SURGERY.md`、`_TASK_L3_LABEL_FIX.md`、`RUNBOOK_BATCH.md`、`shenyue/review/_交接书.md` 等。
2. 共享状态机：`mail2d_read_ledger.json`、`mail2d_catalog_by_size.json`、`_h1_state.json`、`_h5_state.json`、
   `long_task_state.json`、`_excluded_pks.tsv`、`_ngcfg.py`、`shenyue/review/_ledger.json(.jsonl)`、
   `04-现代研究文献/rowmine_traversal.duckdb`、`historical_claims.duckdb` 及其最近回滚点。
3. 源库（只读）：`03-原始史料库/11-邮件列表史料/` 各 .duckdb。
4. 活跃工具链：各交接书 §五/§十 点名的门禁/外科/合并脚本（多数在 `_db_row_mining`、`review_logs`，
   根目录 `script/_lm_*.py`、`_lap/_larc/_spax`、`_value_*_20260921`、`_jianyi_*.py` 均在用）。

## 四、纪律

- 每轮开工先 `git status`＋HOT 扫描（mtime<2h）＋交接书引用核对，三者全过才动。
- 移动一律经暂存目录＋manifest，禁止直接 Delete；回收站保留期由系统策略决定，manifest 是唯一恢复索引。
- tracked 文件清理后在提交信息中单独成段说明（不与内容提交混合）。
- 本文件由每轮收口会话更新「已闭环」表与下一轮断点。
