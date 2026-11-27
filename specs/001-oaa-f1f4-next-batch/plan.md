# Implementation Plan: OAA F1–F4 四组交接书与下一批任务书

**Branch**: `001-oaa-f1f4-next-batch` | **Date**: 2026-10-01 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-oaa-f1f4-next-batch/spec.md`

## Summary

以**只读勘测**为先导，取 F1–F4 四组的磁盘真实进度（合并台账差集 ＋ 分片/判读盘面 ＋ 浮标），据此画出四份**组级交接书**（`script/_db_row_mining/audit_outline/_HANDOFF_F{1..4}.md`），并为每组写出**下一批任务书**（`01-项目管理/01-编纂规划与报告归档/`）。全过程不写大纲、不写数据库、不触碰任何在途批文件。

**取量时点（唯一真值锚）**：2026-10-01 02:22 `oaa_beacon.py --refresh`。

实测四组断点（与浮标 0 差）：

| 组 | 认领宿主 | 已审块 | 待审块 | 在途批 | 在途进度 |
| --- | ---: | ---: | ---: | --- | --- |
| F1 | 40 | 15,897 | 72,791 | `f1_b03`（88.5 单宿主） | 120/459 片＝2,760/10,543 块（26.2%） |
| F2 | 63 | 56 | 88,722 | `f2_b01`（173.1 单宿主） | 653/815 片＝15,013/18,725 块（80.2%） |
| F3 | 147（含避让 4） | 22,532 | 57,969（可审 48,859） | `f3_05`（122.9＋131.5＋121.3） | 8/255 片＝184/5,858 块（3.1%） |
| F4 | 830 | 20,768 | 71,545 | `f4b04`（第34/35章 16 宿主） | 71/93 片＝3,550/4,649 块（76.4%） |

## Technical Context

**Language/Version**: 不适用（本次为纯文档产出）；勘测脚本用 Python 3（`D:\librebsd` 现有解释器）

**Primary Dependencies**: 既有战役工具链（只读调用）：`oaa_beacon.py`、`oaa_fetch.py`、`shard_fetch.py`、`apply_fixes.py`、`oaa_register.py`、`oaa_verify.py`；勘测用自建只读脚本 `work/_fclaims_scan.py`、`work/_fnext_scan.py`

**Storage**: 文件系统 —— 大纲 `05-卷册大纲/**/*.md`（读）；台账 `audit_outline/processed*.jsonl`（读）；分片与判读 `audit_outline/shards|judgements/*.jsonl`（读）；产出为 Markdown

**Testing**: 无自动化测试；以“复算一致性”代替——同一数字须能从磁盘二次推出（见 checklist.md）

**Target Platform**: Windows（Git Bash 壳）；路径含中文，脚本内一律 `chr(92)` 归一化，禁 bash `for` 遍历中文路径

**Project Type**: 编纂工程文档（documentation）

**Performance Goals**: 每组勘测一次全量扫描 ≤3 min；四组合计 ≤6 min

**Constraints**: **只读**——不得写入 `05-卷册大纲/**`、`audit_outline/shards/**`、`audit_outline/judgements/**`、`processed_fN.jsonl`；`_BEACON.md`/`beacon.json` 的刷新属既定协议动作，只更新进度数字不改变认领边界

**Scale/Scope**: 大纲 350,280 个锚点、1,367 个认领宿主、四份交接书＋四份任务书＋一处主交接书回指

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- 本特性不写大纲正本、不写数据库 —— 符合“既有源文件不可擅改”。
- 本特性只新增文档（`specs/`、`_HANDOFF_F*.md`、任务书）与两个只读勘测脚本 —— 无破坏性动作。
- 在途批零触碰 —— 符合防双写纪律。
- 无违规项，无需 Complexity Tracking。

## Project Structure

### Documentation (this feature)

```text
specs/001-oaa-f1f4-next-batch/
├── spec.md              # 需求规格
├── plan.md              # 本文件
├── tasks.md             # 任务分解
├── checklist.md         # 验收检查点（二值判定）
└── checklists/
    └── requirements.md  # 规格质量清单（自动产物）
```

### Source Code (repository root) —— 本次实际改动面

```text
# 勘测（新增，只读脚本）
script/_db_row_mining/audit_outline/work/
├── _fclaims_scan.py     # 按认领清单逐宿主核 pending（新增）
└── _fnext_scan.py       # 按卷扫描 pending（新增，辅助）

# 交接书（新增，4 份）
script/_db_row_mining/audit_outline/
├── _HANDOFF_F1.md       # 新增
├── _HANDOFF_F2.md       # 新增
├── _HANDOFF_F3.md       # 新增
├── _HANDOFF_F4.md       # 新增
└── _HANDOFF_OAA.md      # 修改（§九 增补组级交接书索引＋刷新现场）

# 任务书（新增，4 份）
01-项目管理/01-编纂规划与报告归档/
├── 大纲邮件审计_F1-04-任务书-20261001.md
├── 大纲邮件审计_F2-b02-任务书-20261001.md
├── 大纲邮件审计_F3-06-任务书-20261001.md
└── 大纲邮件审计_F4-b05-任务书-20261001.md
```

**Structure Decision**: 沿用战役既成布局——交接书随台账放 `audit_outline/`（与 `_HANDOFF_OAA.md` 同目录），任务书放 `01-项目管理/01-编纂规划与报告归档/`（与 F1–F4 组任务书同目录）。不新建目录、不改组任务书。

## 下一批范围（四份任务书的标的）

| 任务书 | 组 | 宿主 | 块数（02:22 实测） | 片数 |
| --- | --- | --- | ---: | ---: |
| F1-04 | F1 | `92.1-2000-2003-年-4-0-Jails.md`（第05卷 第92章） | 9,509 | 414（23/片） |
| F2-b02 | F2 | `184.1-netbsd2130多平台扩展与稳定化20052007.md` | 12,919 | 562（23/片） |
| F3-06 | F3 | 第06卷余下 27 宿主（剔在途 122.9/131.5/121.3、剔避让 4） | ≈4,249 | ≈185（23/片） |
| F4-b05 | F4 | 第02卷余下 63 宿主（剔在途 `f4b04` 16 宿主；含 36.4 并行新增 1,650） | ≈4,460 | ≈90（50/片） |

**取量时点均为 2026-10-01 02:22**；开工时以 `oaa_beacon.py --status` 实测为准（大纲动态增长）。

## Phase 0 —— 研究结论（已就地取得）

| 问题 | 结论 | 证据 |
| --- | --- | --- |
| F2 是否已开工？ | 是——`f2_b00` 试点已闭环（`4d36a0c64`），`f2_b01` 在途 80.2% | `work/_f2_progress.md`、`shards/f2_b01_*` 815 片 |
| F1 是否只有 2 批？ | 否——`f1_b03` 已在途（459 片），故 F1 已开 3 批 | `judgements/f1_b03_s120.jsonl` 等 120 件 |
| F3-05 是否已开？ | 是——255 片已切、8 片已判 | `work/hosts_f3_05.txt`、`work/f3_05_all.jsonl` |
| F4 批四是否已开？ | 是——`f4b04` 93 片、71 片已判 | `work/f4b04_*.fetch.jsonl` 16 份 |
| 卷目录名与索引不一致 | 第12/17/18/20 卷磁盘名为 `macos的bsd遗产`/`政治制度与社区治理`/`全球社区地区bsd史`/`linux社区史与比较研究` | `ls 05-卷册大纲/` |
| 避让清单当前规模 | 9,110 块（原载 7,988，被并行会话增写） | 浮标 57,969 − 实算 48,859 |

## Phase 1 —— 交付设计

- **交接书固定五节**（FR-002）：①已闭环批次表 ②在途批现场 ③挂账移交清单 ④本组特有坑 ⑤下一手与断点真值。
- **任务书固定结构**：〇现场（在途批与该批关系）→ 一本批范围（逐宿主块数表）→ 二执行前置 → 三执行八步 → 四本批特有风险 → 五挂账口径 → 六验收标准 → 七收口序列。
- **交叉引用**：任务书引用组任务书 §三（标准八步），避免复制粘贴；交接书引用批报告路径。

## Complexity Tracking

无违规项。
