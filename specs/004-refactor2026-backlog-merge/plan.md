# Implementation Plan: 重构2026 建议书与待执行待办任务合并总账（spec 层）

**Branch**: `004-refactor2026-backlog-merge` | **Date**: 2026-10-09 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/004-refactor2026-backlog-merge/spec.md`

## Summary

主理人令要求在“重构2026/index.html”语境下**找出**有关建议书与待执行的**最近的 spec**，并把**待办任务合并**为单一可执行清单。

0 信任实读后认定：**最近的 spec ＝ `.trae/specs/converge-all-remaining-tasks/`**（2026-10-09《全量剩余任务合并总账》，Task 0／1 已闭环、Task 2–7 未勾）；次级＝`.trae/specs/finalize-refactor2026/`（剩余已并入）；建议书族＝`08-核查报告与多轮复核/重构2026/` 00–125 号文（最新 124／125）；总账文书＝`review_logs/毕其功于一役-总任务账-20261009.md`；唯一对账入口＝92 号文 §十一。

本计划的**技术路径**：以“**核定 → 合并 → 映射 → 分批执行**”四段推进。核定段产出可复核的来源清单与实测证据；合并段产出**去重·定档·定序·可判定**的单一清单，并与总账 Task/SubTask **逐条一一映射**；执行段严格走项目收束铁律（改内容源 → 装配 → 字体子集 → 再装配 → 门禁全量 → 三套浏览器回归 → 落账 → 版本递增 → 提交）。**本 spec 自身不施工内容层**；施工依项目宪法与批次纪律、经主理人批准后另批执行。

## Technical Context

**Language/Version**: Python 3.14.2（`C:/Python314/python.exe`，duckdb 脚本）；纯文本／门禁用 `…/binaries/python/versions/3.13.12/python.exe`；`audit_page_assets.py`／`font_subset_rebuild.py` 须 py314（fontTools＋brotli）

**Primary Dependencies**: DuckDB（`changelog.duckdb`／`historical_claims.duckdb` 等）；装配链 `assemble_index.py`；字体子集 `font_subset_rebuild.py`；门禁 audit 系脚本；浏览器回归三套

**Storage**: 内容源＝`08-核查报告与多轮复核/重构2026/data/outline.txt`（纯文本行式）；产物＝同目录 `index.html`（装配产物）；台账＝`changelog.duckdb`；对账＝92 号文 §十一

**Testing**: 门禁全量（audit 系，件数以 `audit_gate_registry.py` 现跑为准）＋三套浏览器回归（visual／full_matrix／fullsize）＋`sync_refactor2026_baseline.py --check`＋第十二件负向夹具 `tri_structure_negtest.py`

**Target Platform**: 本地仓库（Windows／Git Bash）；单体 HTML 交付

**Project Type**: 编纂工程（文档／史料库／目录页装配）——非软件产品；本 feature 为**台账合并与需求固化**

**Performance Goals**: 不适用（无运行时性能目标）；等价目标＝**每批收束 FAILED=0 且零口径漂移**

**Constraints**: 只改内容源、禁手改产物；同一内容源不可并行编辑；UTF-8 无 BOM／LF；禁直角引号与“谱系”词；提交路径限定；不 commit 他人改动／不 rebase／不 `--force`

**Scale/Scope**: 待执行面＝最近的 spec 之 Task 2–7（迁移本体 T4–T9／另案线／独立线／备核清零／★22 残留终校／总收官冻结）；口径规模以现跑为准

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| 宪法条 | 检查 | 结论 |
| ---- | ---- | ---- |
| I. 学术性是最高规则 | 本 spec 只做台账合并与需求固化，不动学术内容；执行段沿用 0 信任／两说并陈 | PASS |
| II. 规则唯一权威来源 | 本 spec 不新增规则、不复制条文；引用 `00-编纂规则与格式规范/01-规则/` | PASS |
| III. 考据三铁律 | FR-003／FR-011 明定 0 信任实测与未获一手不落卷 | PASS |
| IV. 改源文件铁律 | FR-007／FR-008 明定只改内容源、装配产物禁手改、口径由装配器派生 | PASS |
| V. 门禁“改完必跑” | FR-007／SC-006 明定门禁全量＋三套回归 FAILED=0；判据须自证 | PASS |
| VI. 数据库与存储纪律 | 不新建根目录路径；临时脚本只放 `script/`；库为唯一工作副本 | PASS |
| VII. spec 受既有批次纪律约束 | FR-012 明定“唯一任务书”边界，防双重台账；spec 为需求／口径层 | PASS |
| Execution Constraints｜验收场景写法 | 全部验收场景为 Given/When/Then 可判定句；需求↔任务↔检查点互指（FR-006） | PASS |
| Governance｜违规处置 | 与宪法／规则冲突时停止施工、交主理人裁决 | PASS |

**GATE 结论**：无违规，**PASS**。Phase 1 设计后复检：仍 PASS（设计未引入与宪法冲突的施工面）。

## Project Structure

### Documentation (this feature)

```text
specs/004-refactor2026-backlog-merge/
├── plan.md              # 本文件
├── research.md          # Phase 0 输出（来源定位与合并决策）
├── data-model.md        # Phase 1 输出（合并清单实体与映射）
├── quickstart.md        # Phase 1 输出（验证/执行引导）
├── contracts/           # Phase 1 输出（总账映射与落账契约）
│   └── backlog-ledger-contract.md
├── checklists/
│   └── requirements.md  # 规格质量清单（specify 自动件）
├── spec.md              # 需求规格
├── tasks.md             # 任务清单（去重定档定序）
└── checklist.md         # 验收检查点（二值可判定）
```

### Source Code (repository root)

本 feature **不新增源码**；执行段只触及既有内容源与派生件：

```text
08-核查报告与多轮复核/重构2026/
├── data/outline.txt          # 唯一内容源（执行段只改此处）
├── index.html                # 装配产物（禁手改；由 assemble_index.py 生成）
├── 00-总体重构方案.md … 125-重构2026收官总案-20261008.md   # 建议书族（只读）
├── review_logs/              # 执行记录与总账文书（只增）
│   └── 毕其功于一役-总任务账-20261009.md
└── script/                   # 临时脚本落点（可随时删除）

.trae/specs/
├── converge-all-remaining-tasks/   # 唯一任务书（施工台账真身）
└── finalize-refactor2026/          # 已并入（交叉核验源）
```

**Structure Decision**: 采用“单 feature 目录 ＋ 只读引用外部载体”结构。spec 四件全部落在 `specs/004-refactor2026-backlog-merge/`；施工对象保持原位（`data/outline.txt` 等），**不迁移、不复制**内容源，避免制造第二份真身。

## Complexity Tracking

> 本 feature 无宪法违规，无需豁免。下表仅登记**结构上必要的复杂度**及其理由。

| 复杂度 | 为何必要 | 更简方案为何不足 |
| ---- | ---- | ---- |
| 两套 spec 落点并存（`specs/` 与 `.trae/specs/`） | 历史成因；前者为 spec-kit 原生落点，后者为既有多批次台账 | 强行合并落点将改动他人已建目录，违反“不新建/不移动源文件”纪律 |
| 合并清单与总账 tasks **逐条映射**而非取代 | 防双重台账（宪法 §VII、项目防双写铁律） | 直接取代会使既有台账失据，且本 spec 无施工权 |
| 引用外部载体而非复制内容 | 口径唯一真身原则（`outline.txt` 唯一内容源） | 复制会制造第二份真身，必然漂移 |

## Phase 0：Outline & Research（输出 research.md）

- 定位“最近的 spec”：扫描 `specs/` 与 `.trae/specs/`，按 mtime／`change-id`／主理人令原文／勾选状态判定，排除主题不相关者。
- 核定待执行面：逐源（最近的 spec 未勾 Task／次级 spec 剩余／建议书族未闭环／`review_logs/` 总账与备核／长线 17 线）取证。
- 决策合并原则：去重取最大范围、定档、定序、前置、可判定验收。
- 记录**来源与证据锚点**（路径／行号／库名＋主键），全部落 `research.md`。

## Phase 1：Design & Contracts（输出 data-model.md／contracts/／quickstart.md）

- `data-model.md`：合并清单实体（条目／来源／档位／序位／前置／验收）、与总账 Task/SubTask 的映射、状态机（待施工→在途→已施工→已落账／销号／另案）。
- `contracts/backlog-ledger-contract.md`：三条契约——①**来源契约**（每项须带可定位证据锚点）；②**映射契约**（本 spec tasks ↔ 总账 Task/SubTask 一一映射，禁新增施工面）；③**落账契约**（每批收束顺序与落账字段）。
- `quickstart.md`：可运行的验证场景（定位复核、合并清单对账、单批收束验收）。

## Phase 2：Tasks（由 `$speckit-tasks` 输出 tasks.md）

按用户故事分相：US1 核定 → US2 合并 → US3 执行 → US4 双重台账防线；每条含 ID、[P]、[Story]、明确路径与可判定验收。
