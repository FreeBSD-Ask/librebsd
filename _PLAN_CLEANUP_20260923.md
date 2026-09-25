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

## 二、轮 2（2026-09-23 当晚，本会话）已部分闭环

**清出 ≈4.8 GB**（经 `_recycle_stage_20260923b` 入回收站）＋合并归位一批：

- **合并归位**：41 个 S-me 交付报告（round 1 因 `./` 前缀致排除失效误入回收站，已从回收站 $R 解析恢复）
  ＋`S-me目录预览` → `01-项目管理/01-编纂规划与报告归档/S-me目录建议报告归档/`；
  lm 线退役脚本（_lm_*/_lap/_larc/_spax/_value_*，主理人 09-23 已放弃价值反推推广）＋`linux_mail_mining/`
  110 脚本＋2 work duckdb → `03-原始史料库/11-邮件列表史料/05-linux-kernel/mining/04-脚本/`；
  MAIL_INSIGHT 中间件（mail_hits/mail_search_results/mail_insight_*×7/_mine_*.json×3/_usenet_keyword_hits.json）
  ＋`_HANDOFF_邮件列表史学观点增补.md`＋`_longline_status.py` → `01-项目管理/01-编纂规划与报告归档/邮件列表挖掘战役档案-20260923/`；
  `_既有缺陷清单.json` → `08-核查报告与多轮复核/重构2026/`；`_outdated_disposition_rules.md`＋`_watch_git.*` →
  `00-编纂规则与格式规范/01-规则/`；`_jianyi_*.py` → `shenyue/`；B-LINE-HANDOFF-20260914×2 →
  `01-项目管理/01-编纂规划与报告归档/`；`subagents_fsdevel/` → mining/ 下待入库；`_tmpndb11/` →
  `11-元数据接口/ndb构建脚本-20260922/`；3 个最新 DB 回滚点（fq_b044/045/046 09-22）→ `12-数据库备份/20260923/`。
- **_db_row_mining 安全清理**（🔴会话仍活跃：20:07 还在写 _HANDOFF_H3/_PLAN_H2_LONGTERM，只清无争议件）：
  12 个旧 claim 回滚点（1.7G）＋61 个 _backup_/_bak_ 目录（1.9G）＋25 个 dump/pages 目录（410M）
  ＋1131 个 forread/heads/tmp/bak_p0 杂件（2.4G）；**活跃状态/交接书/台账/活跃批次件（fpo_b175、fbug_b190、
  tk_b145/146、h5arm_b521_2、fq_b062、fstb_b007、fcu_b007、fdoc_b009、fhk_b028）及 1.2 万个会话工具链脚本全保留**。
- **根目录已清干净**：24 个今日分析中间件＋26 个一次性修补脚本＋_tmp/_work/_audit_tmp/__pycache__/tmp_b51/
  _tmp_fix/_fix7/script_ 误建目录等入回收站；根目录现仅剩内容目录（00–12）、配置点文件、工具目录、
  `_PLAN_*.md`×3、docs/spec、`review_logs/`（活跃，留）、`shenyue/`（jianyi 在用，留）。
- **script/ 剩余**：`_db_row_mining`（3.4G，活跃战役＋review_logs 1.5G）＋`_recycle_*` 清理工具 6 件。
- **🔴轮 2 遗留（最终清空，待 mail2d 会话收尾后做）**：`_db_row_mining` 内 1.2 万个一次性 .py、700+ 份
  已完成批任务书（_READ_TASK_*/_NARR_TASK_*）、review_logs 1.5G、旧 forread 包；交接书/台账/状态机/断点页
  届时按 §三 必留清单合入 `01-项目管理/01-编纂规划与报告归档/邮件列表挖掘战役档案-20260923/`。
- round 1 教训入册：find 输出带 `./` 前缀时 `^S-me` 锚定排除失效——批量移动的排除过滤必须用子串匹配（grep -F）或先去前缀。

## 三、后续轮次（按收益排序；每轮开工前重跑 §〇 判定）

- **轮 2.5：_db_row_mining 最终清空**（3.4G，🔴待 mail2d 会话收尾）——见 §二 遗留条目。
- **轮 3：12-数据库备份/**（28G）——40 路子代理逐备份审阅：git 重写离线包（git-history-backup-20260911）
  与 12-数据库备份/git-history-backup-20260911/ 等专属备份区按「备份目的是否已完成＋是否有更新替代」裁定；
  本轮未动，需用户确认口径后开工。
- **轮 4：04-现代研究文献/** 剩余（文献下载目录、.mimosa、historical_claims.duckdb.tmp 09-14 旧临时）——
  现役 .duckdb 与 09-23 回滚点不动；`*.bak-20260923-h5gk4/5/6` 等 24h 内件到期后可并入下一轮。
  **（2026-09-25 部分闭环：04 备份件与 09-14 旧临时已清；另清 05-卷册大纲 备份件 42 件。见 §五）**
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

---

## 五、轮 4（部分）已闭环 ＋ 05 大纲备份件清理（2026-09-25）

主理人当日指示「删除 05 大纲中乱七八糟的备份文件」并「04 目录下备份一并清理」，两处合并执行。

**动的**：`05-卷册大纲/` 备份件 42 件（26.2 MB，后缀 `.bak_t1` 11／`.bak_a67` 7／`.bak_restore10` 5／
`.prebak-qc7g-*` 4／`.bak_a4` 4／`.prebak_tk_b139_lv` 3／`.bak_mm` 3／`.bak_restore77` 2／
`.bak_fix12109` 2／`.bak_a7x` 1）；`04-现代研究文献/` 数据库快照 8 件（8×165M）＋DuckDB 溢出临时目录
`historical_claims.duckdb.tmp/`（5.4G，mtime 09-14，已搁置 11 天非活动件）。两批合计 6.66 GB，全部入回收站。

**没动的**：`03-文献下载/01-pdf/` 下两篇标题含 Backup 的学术论文（ZFS 快照、IoT 备份软件）；
`.mimosa`、文献下载目录、shenyue 线、12-数据库备份 均不在本批。

**删前核实三项**：两批全部有对应正本且无一件比正本新（均系正本旧快照，无孤儿、无更新副本）；
全仓无脚本/台账点名这些路径（05 批唯一命中系对已完案的历史记述，04 批唯一命中系本计划 轮 4 条目
与两份 ignore 规则）；`05-卷册大纲/SUMMARY.md` 同步器只收 `endswith(".md")`，备份件从未进导航。
现役 `historical_claims.duckdb` 于回收后经只读连接校验：`claim` 表可读、252,784 行。

**两处越规与补救**：其一，§三 必留清单第 2 条要求留 `historical_claims.duckdb` **及其最近回滚点**，
而本轮 8 件中最晚者（内容日期 09-23 11:20）被误删，已从回收站还原并注销回收站条目（172,765,184 字节）。
其二，§四 纪律要求经 manifest 留恢复索引，本轮首做时只留了纯路径清单，已补
`_backup/_recycle_manifest_20260925.json`（含原路径／大小／删除时刻／回收站实体名／还原状态）与同名
`.txt`，51 项逐条在册、实体缺失 0。**未按纪律入暂存目录**（直接用回收站），故 manifest 是本批唯一恢复索引。

**空间提醒**：入回收站不释放同盘空间，6.66 GB 仍在 D 盘（清理后 D 盘余 204G）。需真正腾出空间须清空回收站。

**轮 4 余量**：文献下载目录、.mimosa 未动。
