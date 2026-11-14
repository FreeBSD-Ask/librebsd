# 05-卷册大纲/映射 —— 映射层说明

本目录是《重构2026 目录落地 05-卷册大纲》战役的**映射层**：承载旧树到新树的清点台账、目标注册表、映射台账、布局清单、交叉对照与复核工作包。本批 spec 见 `.trae/specs/migrate-refactor2026-into-outline-20261023/`。

## 一、旧树快照性质

`旧大纲-20261023/`（仓库根级）是**迁移前旧 `05-卷册大纲/` 的全文快照**：24 个卷目录 + 4 个根级文件，共 37,486 个 `.md`（37,484 个小节 `.md` + 2 个根级 `.md`）与 2 个根级 JSON。

- **逐件取证入口**：Git 标签 `outline-pre-landing-20261023` 指向改名前的提交，可用 `git show outline-pre-landing-20261023:<旧路径>` 逐件取证原始全文。
- **消化口径**：按“最终只保留未迁移件”逐批消化——已映射（`CONFIRMED`）文件用 `git mv` 迁入新树，迁出即从旧树消失；`UNMAPPED`／`DISPUTED`／`TARGET_LOST`／`DUPLICATE`／`DISCARDED` 与空目录骨架留在旧树，待后续裁决。
- **只读纪律**：新树建设期间任何脚本或评审只读取旧树，不得改写内容或“顺手修正”；除已确认映射文件的迁出、以及 `TARGET_LOST`／`REMAP` 文件的回迁外，不得改名、删除或新增。**唯一既有例外**：spec SubTask 2.1b 已批准的机械标准化改名——2026-10-24 执行 6,291 件（6,118 反引号剥离＋173 模板名→H1 名），逐件 SHA 前后相等，台账见 `title-standardization.tsv`。
- **旧树派生件**：旧树 `SUMMARY.md`、`chapter_keywords.json`、`theme_index.json` 为**历史快照、非现行索引**，迁移开始后不再随迁出再生；不得以旧树索引校验新树。**兼容版再生已完成并冻结（2026-10-25，2.1a，ykla 令"偿还0-4的技术债务和遗留"）**：`SUMMARY.md` 已从当前旧树（2.1b 改名后状态）再生（41,233 行，四级嵌套与既有格式逐字节同构，数字序排序，反引号残留 0）；`chapter_keywords.json`／`theme_index.json` 验证**内容一致**——两件零文件名引用（.md 引用 grep 0 命中），改名系文件名层且 SHA 前后相等（`title-standardization.tsv` 6,291/6,291），meta 计数与现树一致（卷 24／章 449／节 3,274／小节 37,484）。再生器 `script/_tmp_regenerate_oldtree_summary.py`（只读旧树＋写 SUMMARY 一件）。**此后不再随新树或旧树变动再生；不得以旧树索引校验新树。**
- **语义改名建议冻结（2026-10-25，2.1c，ykla 裁决"全部留给 Task 7"）**：`title-review.tsv` 12,489 条（slug 12,274／truncated 108／artifact 103／junk 4；高 9／中 43／低 12,437）**全部不提前改名**，冻结为建议存档（FR-T2-02 执行改名数 0 维持）。**Task 7 承接**：迁移取全题（SubTask 7.2"编号前缀＋标准化标题原文"），slug 12,274 条按其标准化规则自然处理；artifact 103＋truncated 108＋junk 4 条（合计 215 条）**列入 Task 7 标准化规则必剥清单**，Task 7 开批时须纳入其标准化判据并走其全链门禁。

## 一之二、状态机（2026-10-24 修订，强制，选项 B）

**Task 5 期间 `status` 禁止写 `CONFIRMED`**，只允许 `PENDING`／`DISPUTED`／`UNMAPPED`／`DUPLICATE`。

判定结论一律写入 `review_a`／`review_b`／`review_c`／`review_state=JUDGED`／`target_id`（作**候选**目标）。
`CONFIRMED` 只能由 Task 8 在**落盘成功后**置位（目标节 `.md` 存在且 `layout.tsv` 有该行）。

| 阶段 | status 允许值 | `audit_outline_landing.py --check` 期望 |
| ---- | ---- | ---- |
| Task 5 判定中 | PENDING／DISPUTED／UNMAPPED／DUPLICATE | 17/17 PASS（L2、L7 必须 PASS） |
| Task 8 落盘后 | CONFIRMED（仅落盘成功者） | L2 无缺、L7 emptydest 0 |

**原因**：Task 5 若直接写 `CONFIRMED`，该行在 `layout.tsv`（当前为空表）与目标节（当前 0 件）都无对应，
L2／L7 必然 FAIL。2026-10-24 已回退 53 条 `CONFIRMED` → `PENDING`（`review_state=JUDGED`，判定证据全部保留）。
回退后 `--check` 为 17/17 PASS。

**`review_state` 取值归一**：规范值为 `JUDGED`。执行方历史值 `merged` 视为同义（读入归一到 `JUDGED`），
不因取值差异判 FAIL；新写入一律用 `JUDGED`。`DISPUTED` 行须在 `review/disputes.tsv` 有对应行
（2026-10-24 实测：disputes 160 条 ↔ mapping DISPUTED 160 条，双向差集 0）。

## 二、映射层结构

| 路径 | 性质 | 产出任务 |
| ---- | ---- | -------- |
| `targets.tsv` | **目标注册表**（稳定节点 ID，改号/重排不换 ID） | Task 3 |
| `targets.prev.tsv` | 每次应用前的注册表快照 | Task 3／7 |
| `mapping.tsv` | **旧→新映射台账**（37,484 行，一文件一行） | Task 4 |
| `layout.tsv` | 目标路径与 P 序布局清单 | Task 7 |
| `crosswalk-section.tsv`／`crosswalk-chapter.tsv`／`crosswalk-volume.tsv`／`crosswalk-subsection.tsv` | 旧→新交叉对照（含多数映射与歧义标记） | Task 7 |
| `ref-rewrite.tsv`／`ref-unresolved.tsv`／`ref-sync.tsv` | 引用改写台账／未决挂账／同步留痕 | Task 7／11 |
| `review/` | 复核工作包（`packs/<旧卷>.tsv`、`disputes.tsv`） | Task 4／5 |
| `挂账清单/` | Task 6 四类挂账清单（`01-unmapped-by-volume-chapter.tsv` 旧卷×旧章 UNMAPPED 计数、`02-unmapped-no-target-detail.tsv` UNMAPPED 无目标明细（裁决入口）、`03-disputed-by-volume-chapter.tsv` 旧卷×旧章 DISPUTED 计数（分规则通过与规则未决）、`04-backlog-summary-by-volume.tsv` 分卷汇总；生成器 `script/_landing_production_20261024/_task6_backlog.py` 只读可复跑） | Task 6 |
| `缺口族分析/` | 结构缺口内容分析批数据表 26 件（01—05 旧 vol20 逐章与 395 分流、06—11 UNMAPPED 逐行分层与规则、12—16 D7/D8 数据修正方案、17—21 V-076 五章与三套节粒度映射、22—24 语言史章补证／设计／边界、25 对账表、26 题命中改判 422 行；生成器 `script/_landing_gap_analysis_20261025/` p00—p10 只读可复跑、二跑零增量；报告＝`01-项目管理/01-编纂规划与报告归档/05-大纲落地-结构缺口内容分析-20261025.md`） | 结构缺口内容分析批 20261025 |
| `reference/` | 18 件历史映射表（章级/节级映射表、关键词/文献/人物/时间线-章节映射表等），只作候选生成参考 | Task 2.5 |
| `drift/` | 目录变动漂移报告 | Task 3 |
| `title-standardization.tsv`／`title-review.tsv`／`path-overlong.tsv` | 标题标准化台账／杂质名待裁决／超长路径裁决 | Task 2 |
| `target-lost.tsv`／`remap.tsv` | 目标退役回迁挂账／拆分合并重映射挂账 | Task 13 |

## 三、清点台账三件（Task 1 产出）

| 文件 | 口径 |
| ---- | ---- |
| `inventory.tsv` | 旧树全部 `.md` 逐文件清单。列：`relpath`（相对仓库根）、`bytes`、`sha256`、`is_empty`（0 字节为 1）、`has_special_structure`（含 ROW_MINE 块／成对锚 BEGIN-END 注释／Markdown 表格则记类型，否则空）。37,486 数据行。 |
| `path-coupling.tsv` | 全库受 Git 跟踪文本文件（`.py`／`.md`／`.json`／`.js`／`.ts`／`.tsv`／`.html`／`.jsonld`／`.css`／`.mjs`／`.txt`）中含路径字面量 `重构2026` 或 `05-卷册大纲` 的行。列：`file`、`line_no`、`matched_text`（截断至 200 字符）、`category`（脚本／规则／号文／夹具／其他）。**排除** `旧大纲-20261023/` 与 `08-核查报告与多轮复核/重构2026/` 下的历史归档。 |
| `old-tree-normalization.tsv` | 旧树机械门禁违规逐文件登记。列：`relpath`、`violation_type`、`count`、`sample`。检查项：直角引号（U+300C／U+300D／U+300E／U+300F）、AI 不可见字符（Unicode Cf 全体 + Zs 除 U+0020）、CRLF 换行、Markdown 加粗空格、成对锚配平、重复锚。某类全 0 时留一行 `(全库)` 说明。 |

三件均为**只读扫描旧树**所得，不修改旧树任何文件；写盘 UTF-8 无 BOM、LF。

## 四、真值声明

- **映射真值**：`targets.tsv`（目标注册表）与 `mapping.tsv`（旧→新映射台账）是映射的**唯一真值**，均为纯文本 TSV。
- **派生副本**：`mapping.duckdb` 为**只读派生**，可随时从 TSV 重建，不作真值；若写入生产路径须走写库门禁（`claimdb_guard.py`＋`rotate_guard_state.py`）并在 `folder_db_registry.csv` 与 `schema_meta` 两处登记。
  **已建（2026-10-25 Task 4.4）**：`映射/mapping.duckdb`（37,484 行×16 列；表 `mapping`＋`schema_meta`＋视图 `v_status_dist`／`v_target_dist`／`v_coverage`／`v_dup_groups`）。建库链＝`rotate_guard_state.py pre`→构建（重建验证：同 TSV 二次入内存库行数/状态分布/覆盖率三项一致，二跑零增量）→`claimdb_guard.py --path` PASS（基线 `script/_claimdb_guard_path_state/path-c413ce6b8604a85bdff9e2fc.json`）→`post`→`folder_db_registry.csv` 登记。构建器 `script/_tmp_build_mapping_duckdb.py`（可复跑重建）；每次 mapping.tsv 波次并表后须重跑以刷新统计。
- **结构真值**：卷/章/节结构以 `05-卷册大纲/目录/data/outline.txt` 为唯一真值，新树是派生结果。

## 五、后续入口

- 本批 spec：`.trae/specs/migrate-refactor2026-into-outline-20261023/`（`spec.md`／`tasks.md`／`checklist.md`）。
- 施工计划：`01-项目管理/01-编纂规划与报告归档/05-大纲落地生产搬迁批计划-20261023.md`；执行排程：`05-大纲落地生产执行计划-20261024.md`（B1—B4／B5—B7／W1—W6）。
- 长线登记：`01-项目管理/01-编纂规划与报告归档/长线任务总登记表.md` 第 5 条与第 13 条（landing05，真值 `mapping.tsv`）。

## 六、本批施工记录（2026-10-24，M1＝Task 2 收尾）

| 批 | 产物 | 验收 |
| -- | ---- | ---- |
| B1（2.1b＋2.4a 台账） | `title-standardization.tsv`：6,291 改名行（SHA 前后相等）＋168 补录行＝6,459 数据行 | 复扫机械缺陷五类==0；dry-run 二跑==0（幂等）；与 ADR-0015 的 6,291 精确一致 |
| B2（2.1c 建议表） | `title-review.tsv`：12,489 行（junk 4／truncated 108／slug 12,274／artifact 103），**只出表零改名** | 剩余差集全覆盖；对账：ADR 21,031（B1 前口径）＝B1 机械修复 6,291＋本表 12,489＋分类口径差 2,251 |
| B3（2.1d 复测） | `path-overlong.tsv`：四类零命中（>260／保留名／尾点空格／大小写冲突） | 全零断言 PASS |
| B4（2.1a 冻结） | 冻结声明见 §一；再生尝试被工具自校验拒绝（415×`T_SECTION_SEQ`，见冻结声明） | **受阻待裁**：spec 2.1a 字面（再生＋审计 PASS）不可达，以“存量快照＋台账对照” interim 达成 |

生产脚本：`script/_landing_production_20261024/p01–p05`；断言与台账均留档。
