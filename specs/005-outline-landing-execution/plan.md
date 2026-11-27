# Implementation Plan: 05 大纲落地生产执行（Task 2 收尾／Task 4／Task 5，主代理形态）

**Branch**: `005-outline-landing-execution` | **Date**: 2026-10-24 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `specs/005-outline-landing-execution/spec.md`

## Summary

ykla 令（2026-10-24）：复核任务书并确认内容（已做，基线＝34/104、三源互证一致、mapping 实测 20.9 MB）、建立**完整符合本项目软件工程理论**的执行规划、**不计成本代价**、**子代理任务转主代理且不使用子代理**。

技术路径四段：**收尾（Task 2）→ 台账（Task 4）→ 三判（Task 5 主代理串行）→ 签收（复核轮次＋ykla）**。核心设计变更＝原“三路子代理独立复核”转译为**主代理三趟串行独立判定**：同包只读、输出分文件密封、三趟策略差异化（A 题面语义／B 主题词／C 结构编号）、合并器硬判据汇总（契约见 `contracts/three-pass-review.md`）；复核轮次以“时间分离＋第四视角”保障作者不复核自己。工程理论接线：每批走 L0–L5（写入面判定表见任务书 §七）、需求基线 batch-scoped（spec §六 FR/NFR）、追溯链四段（来源→FR→任务→证据）、审计双台账、门禁收口五命令＋常备四件。

## Technical Context

**Language/Version**: Python 3.14.2（`C:/Python314/python.exe`；TSV/断言/探针脚本）

**Primary Dependencies**: `05-卷册大纲/映射/` 台账族（inventory/targets 既有，mapping 等待产）；`_longline_status.py`（landing05 探针）；`audit_outline_landing.py`（L1–L17）；git（标签 `outline-pre-landing-20261023` 取证；里程碑提交）

**Storage**: 台账＝`05-卷册大纲/映射/*.tsv|*.md`；判定输出＝`映射/review/judgments/`；checkpoint＝`script/_landing_production_20261023/checkpoints/`；复核记录＝`01-项目管理/02-工程决策与技术债/任务复核台账.md`

**Testing**: 断言驱动（行数/守恒/SHA/幂等二跑）＋门禁（收口五命令＋常备四件）＋审计台账行；无浏览器回归面（不触目录页装配源）

**Target Platform**: 本地仓库（Windows／Git Bash）；specs/ 工作区不入库

**Project Type**: 编纂工程的数据迁移战役（非软件产品）；本 feature＝执行规格与批次计划固化

**Performance Goals**: 不适用运行时指标；等价目标＝每批断言全过＋门禁全绿＋二跑零增量

**Constraints**: 零子代理（NFR-001）；写入边界（NFR-002）；旧树只读除 2.1b；UTF-8 无 BOM／LF；弯引号；禁旁路备份；里程碑提交制

**Scale/Scope**: 37,484 子节×3 趟判定＋21,031 建议行＋6,291 改名；六波（W1–W6，05/09/20 卷切子批）

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| 工程实践规则面 | 检查 | 结论 |
| ---- | ---- | ---- |
| §0.3 作者不复核自己／L7 签收 | 单代理语境转译：判定轮与复核轮时间分离＋第四视角＋轮次显式记录；签收归 ykla 本人 | PASS |
| §2.1 需求基线与 ADR | 迁移决策已由 ADR-0015 覆盖（滚动基线 TG-002），本 feature 不改写入边界/所有权/新门禁→不新建 ADR | PASS |
| §3 L139 dry-run 口径 | 干执行只标“前置已核”；本 feature 验收一律生产实测 | PASS |
| L0–L5 阶段循环 | 任务书 §七 适用表逐任务接线（无写入面 L0＋L1；有写入面 L0–L5） | PASS |
| 任务审计 L1–L12 | 每批准入/复核/收口走 `audit_task_lifecycle.py`；台账轮替按规则 | PASS |
| 门禁接线（R1–R8） | 不新增门禁脚本；复用 audit_outline_landing/元门禁/旁路备份等既有件 | PASS |
| 写库门禁 | mapping.duckdb 只读派生优先；若落生产库须 claimdb_guard＋rotate＋登记 | PASS |
| 红线（正文/装配产物/旁路备份/自动化/根目录） | 不撰正文；不触装配产物；Git 留痕；人在场按批推进；无根目录新路径 | PASS |

**GATE 结论**：无违规，PASS。Phase 1 设计后复检：仍 PASS（三判契约与数据模型未引入新施工面或新门禁）。

## Project Structure

```text
specs/005-outline-landing-execution/
├── spec.md                      # 需求规格（本 feature）
├── plan.md                      # 本文件
├── research.md                  # Phase 0：三判形态决策与其余决策
├── data-model.md                # Phase 1：台账实体与状态机
├── contracts/
│   └── three-pass-review.md     # Phase 1：主代理三判执行契约
├── quickstart.md                # Phase 1：端到端验证指南
├── tasks.md                     # 执行任务清单（与 .trae spec 逐条映射）
└── checklists/
    ├── requirements.md          # 规格质量清单（已过）
    └── ../checklist.md          # 验收检查点（复核人勾选权）
```

生产落点（写入面）：`05-卷册大纲/映射/`（台账族＋review/）、`script/_landing_production_20261023/`（checkpoint）、`01-项目管理/02-工程决策与技术债/`（复核台账）。

## Milestones

| M | 内容 | 出口判据 | 对应 |
| -- | ---- | ---- | ---- |
| M1 | Task 2 收尾（B1–B4） | 六类==0；台账在盘；派生件冻结 | US1 |
| M2 | Task 4 设施（B5–B7） | mapping 三断言；探针切换 | US2 |
| M3 | 先导子批＋W1 | 分歧率实测落账；01–04 卷终态 | US3 |
| M4 | W2–W6 全量 | PENDING==0；守恒==37,484 | US3 |
| M5 | 复核轮次＋签收＋收口 | ≥3 轮＋ykla 签收＋门禁全绿 | US4/US5 |

## Phase 0 → research.md

决策清单：三判形态（子代理废止后的替代方案族比较与选型）、串行隔离的独立性论证与限制、提交节奏（里程碑制）、先导子批停盘阈、复核第四视角定义。全部 [NEEDS CLARIFICATION] 已闭合（用户令即答案），无残留研究项。

## Phase 1 → data-model.md / contracts / quickstart.md

实体与状态机（16 列 schema、八状态守恒、S-ID 规则）；三判契约（输入密封、策略定义、合并判据、复核轮次）；验证指南（断言命令族与期望输出）。

## Implementation Strategy

MVP＝US1（Task 2 收尾）：解锁关键路径且独立可验。随后 US2（一次生成批）→ US3 先导子批（停盘阈裁决点）→ 六波全量 → US4/US5 贯穿每批并终局收口。每批：批前 `git status --porcelain` 基线→施工→断言→门禁→L3/L4 留证→checkpoint→（里程碑批）提交＋长线刷新。
