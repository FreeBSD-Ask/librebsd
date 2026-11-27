# Implementation Plan: login 数据库全量逐条判定入 claim 库与 05-大纲

**Branch**: `003-login-claim-outline` | **Date**: 2026-10-06 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/003-login-claim-outline/spec.md`

## Summary

对 login 数据库 6,604 篇文章（含广告/目录/刊头全部形态）逐条遍历，按本书既有规则（《编纂原则清单》62 条、八项操作原则 R1-R12、十二项阈值、七类不写排查）判定其历史意义与价值；判定应入者按既有 schema 三层入藏 claim 数据库（historical_claims.duckdb：raw_source 注册＋evidence＋claim），并**同时**按规则同步 05-大纲（claim 库侧 source_chapter 挂钩＋磁盘侧 ROW_MINE 注入块）；既有大纲不足以归类的按“新增章节”扩展接口新建大纲文件；全程重构2026 目录只读（哈希基线终检）。

技术路线沿用主理人既定执行架构：Python 引擎直调 API（≤120 路、轮替存储 key、不派子代理），复用既有线路客户端与判定/入藏基建；0 信任原则与三次复查贯穿。

## Technical Context

**Language/Version**: Python 3.14（C:/Python314/python.exe，与本库既有战役一致）

**Primary Dependencies**: duckdb（Python 绑定 1.5.5）；既有判定/入藏客户端 `_glm_line_20261006.py`（api.senseaudio.cn + glm-5.3-flash + 存储 key 池轮替）；WO-007 幂等防护（`00-编纂规则与格式规范/01-规则/脚本与命令/wo007_idempotency.py`）；门禁脚本（audit_evidence_level_labels 等）

**Storage**: login-zazhi.duckdb（只读＋差量 UPDATE 有痕）；historical_claims.duckdb（L1-L3 入藏，纯增量）；判定台账 JSONL（script/ 下断点与幂等键载体）

**Testing**: 只读 SQL 断言（覆盖率/三层齐备/行数守恒）＋门禁脚本（audit_evidence_level_labels、audit_markdown_lint 触及时）＋重构2026 哈希基线比对

**Target Platform**: Windows（本机 16GB，多会话并存环境）

**Project Type**: 数据判定与入藏战役（非代码库工程；引擎/台账为 script/ 临时产物，四件 spec/plan/tasks/checklist 在 specs/003-login-claim-outline/）

**Performance Goals**: 判定吞吐 ≥100 篇/分钟（120 路）；入藏事务批 200 行/批带行数断言

**Constraints**: 重构2026 目录只读（零写入/零改动）；WO-007 大纲写入幂等；证据等级门禁全绿；0 信任＋三次复查；不计成本（主理人最高规则）；单写者纪律（claim 库本战役为唯一写入方或经既有纪律协调）

**执行架构（主理人 2026-10-06 新增要求）**：**滚动 40 路子代理（缺 1 补 1）**执行逐条判定与综合分析——每个子代理领取互斥分片运行 Python 判定引擎，分片完成即补领下一未完成分片；子代理失败/超时即重派；禁止抽查。判定判定/入藏的 LLM 调用仍经引擎的旧线路客户端（key 轮替统一治理）。取代本战役此前“不派子代理”表述（research.md D2 supersession note）。

**Scale/Scope**: 6,604 篇判定 × (1 台账行 + N 条 claim/evidence)；预期 claim 增量千级（判定应入率依内容而定）；大纲注入块千级；新建章 0-数个

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| 宪法条 | 检查 | 结果 |
| ------ | ---- | ---- |
| I 学术性最高规则 | 判定依据既有规则（62 条原则/12 阈值），双参 shigang.md＋lishidagang.md；正文不出现自指名称 | 通过（判定 prompt 与台账字段按此设计） |
| II 规则唯一权威来源 | 本 spec/plan 不新增规则，只引用 `00-编纂规则与格式规范/01-规则/` 与重构2026 设计文档（06/03/01 号） | 通过 |
| III 考据三铁律 | 0 信任（判定逐条留痕）；三次复查（判定→复核通道→仲裁/抽检）；不篡改（evidence.quote 原文照录，噪声照录） | 通过（FR-002/004） |
| IV 改源文件铁律 | 重构2026 为装配产物体系，本任务**只读**（FR-007/SC-005）；05-卷册大纲写入走 WO-007 幂等（不触碰 index.html） | 通过 |
| V 门禁改完必跑 | 写回带等级标注的注入块后跑 audit_evidence_level_labels；触及时跑 audit_markdown_lint | 通过（FR-005） |
| VI 数据库与存储纪律 | DuckDB 唯一工作副本；claim 库纯增量、login 库差量 UPDATE 有痕；落盘文件入库 sha256 去重；临时脚本只放 script/ | 通过（FR-008/009） |
| VII spec/task 批次纪律 | 按批连续推进（人在场会话），断点续传，不创建定时任务 | 通过（FR-010） |

## Project Structure

### Documentation (this feature)

```text
specs/003-login-claim-outline/
├── plan.md              # 本文件（$speckit-plan 输出）
├── research.md          # Phase 0 输出（决策记录）
├── data-model.md        # Phase 1 输出（判定台账/claim/evidence 字段级模型）
├── quickstart.md        # Phase 1 输出（终局验证指南）
├── contracts/           # Phase 1 输出（台账 JSONL 契约 / claim 入藏契约 / 注入块契约）
└── tasks.md             # Phase 2 输出（$speckit-tasks，非本件）
```

### Source Code (repository root)

```text
script/                              # 临时产物（可随时删除；固定脚本不入此）
├── _login_claim_engine_20261006.py  # 判定引擎（逐条遍历→台账）
├── _login_claim_writer_20261006.py  # 入藏写者（claim 库三层＋source_chapter）
├── _login_claim_outline_20261006.py # 大纲注入块写者（ROW_MINE 块，WO-007）
├── _login_claim_ledger_20261006.jsonl  # 判定台账（断点＋幂等键）
└── _login_claim_baseline_20261006.json # 重构2026 哈希基线（终检用）

05-卷册大纲/第N卷/第XX章-slug/       # 新建章文件（仅触发时，按扩展接口）
historical_claims.duckdb             # claim 库入藏（纯增量）
login-zazhi.duckdb                   # 判定终态回写（差量 UPDATE 有痕，如有）
```

**Structure Decision**: 本 feature 是数据战役而非代码工程——引擎/写者/台账为 script/ 临时产物（按 CLAUDE.md 临时文件规则），正式四件在 specs/003-login-claim-outline/；不入 05-卷册大纲 正文（仅注入块与受控新建章）。

## Complexity Tracking

> 宪法检查无违反项，本表留空。

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| （无） | | |
