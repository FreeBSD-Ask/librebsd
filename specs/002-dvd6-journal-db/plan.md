# Implementation Plan: dvd6 期刊四库建库 → 全文库入库 → 入大纲

**Branch**: `002-dvd6-journal-db` | **Date**: 2026-10-05 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/002-dvd6-journal-db/spec.md`

## Summary

把 `dvd6/Website`（Dr. Dobb's Developer Library DVD-ROM Release 6 镜像）上四份期刊（DDJ、CUJ、SA、TPJ）的全部有意义内容结构化入库：在新建 `dvd6/Website/ddj/` 下按期刊建 4 个 DuckDB（元数据＋正文＋广告＋解压后的文本源码＋图片转写/base64，二进制禁入）；随后按项目规则把四库内容入 `references_fulltext.duckdb`（著录＋全文块＋留痕），最后入大纲授权两层（key_facts 原料层＋卷末书目述评层）。全链幂等、留痕、抽样逐字比对；按“不计成本”最高规则以子代理规模换质量。

## Technical Context

**Language/Version**: Python 3.14（`C:/Python314/python.exe`，本机既有；脚本一律 Python，遵守“PowerShell 转 Python”规则）

**Primary Dependencies**: Python `duckdb`；stdlib `zipfile`/`tarfile`（递归解压）、`base64`、`hashlib`；HTML 转文本用 stdlib `html.parser` 自写剥取器（保留 h1/h2/h3 层级与段落）；**禁止本地 OCR/转录模型依赖**——图片转写由会话内子代理 LLM 读图完成（Read 工具直读图片）

**Storage**: 4 个新建 DuckDB（`dvd6/Website/ddj/`）＋既有 `04-现代研究文献/05-参考文献全文数据库/references_fulltext.duckdb`（只按既有 schema 增量写）＋大纲文件（key_facts 库表＋`05-卷册大纲/第N卷/卷末书目述评.md`）

**Testing**: 项目惯例＝独立核验脚本（写读分离、多读共识）＋抽样逐字比对＋幂等重跑断言＋假绿防护（对空集合先断言非空）；不用 pytest

**Target Platform**: Windows 10/11 本机会话；仓库为 UNC（`\\DESKTOP-M5P610N\d\librebsd`）与 D: 映射双身份——脚本写 UNC、PowerShell 走 D:；Git Bash 用 `//DESKTOP-M5P610N/d/`

**Performance Goals**: 无时限目标（不计成本）；质量目标＝抽样逐字一致率 100%、二进制命中 0、幂等重跑 0 新增

**Constraints**: 二进制与压缩包原始字节禁入任何库；禁本地模型转图；禁记录文件路径类无意义字段；`script/` 临时脚本不入库（禁 `git add`）；DuckDB 写连接与只读验证分进程；并发会话共用 references 库须退避重试不杀进程

**Scale/Scope**: DDJ 22 个年包（1988–2009）、CUJ 17 年×12 月包（1990–2006）、SA 15 年（1992–2006）、TPJ 约 9 年按期包（1996–2005）；articles 树 CUJ 13,834 文件（DDJ 更大）；预计万级文章、十万级解压文本文件——全部入4库，无遗漏

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

`.specify/memory/constitution.md` 在 UNC 上不可读（幽灵条目），按项目实际治理文件（CLAUDE.md＋`00-编纂规则与格式规范/01-规则/`）执行门禁：

| 门禁 | 判定 |
|------|------|
| 最高规则“不计成本、不计代价，务必确保学术性” | PASS——FR-011 明示豁免子代理数量与复核轮数上限 |
| 0 信任原则＋三次复查＋多源交叉验证 | PASS——SC-002 抽样逐字比对、写读分离、回报不可信产物可信纪律写入 tasks |
| 禁止自动化/定时任务 | PASS——全链由在场会话同步驱动，子代理滚动派发 |
| 根目录禁止生成新路径 | PASS——`ddj` 建在 `dvd6/Website/` 下（既有原位置保留树内），`specs/` 已豁免 |
| 临时脚本规则 | PASS——全部脚本放 `script/`，不入库（禁 `git add`） |
| 镜像站挖掘与 OCR 流水线规则 | PASS——本件全文入库与大纲回写按该规则执行；差异点（禁本地模型、LLM 直转）为用户显式指令，优先于规则的 RapidOCR 替代路径 |
| REOCR 入大纲授权两层（key_facts＋书目述评；正文层禁止） | PASS——FR-009 照抄授权边界 |
| WO-007 写盘幂等（write_guard）＋证据等级门禁 | PASS——FR-009/FR-010 明示 |
| 不篡改（史料原文照录） | PASS——FR-004“正文照录不改字”；代码文本不重排 |

**Re-check after Phase 1 design**: 设计未新增规则文件、未触碰闸面文档、未引入新根路径、未引入本地模型——维持 PASS。

## Project Structure

### Documentation (this feature)

```text
specs/002-dvd6-journal-db/
├── plan.md              # 本文件
├── research.md          # Phase 0 输出
├── data-model.md        # Phase 1 输出
├── quickstart.md        # Phase 1 输出
├── contracts/           # Phase 1 输出（四库 schema 契约＋全文库对接契约）
└── tasks.md             # Phase 2 输出（$speckit-tasks 生成）
```

### Source Code (repository root)

```text
C:\ddj_stage\          # 本地暂存（主理人令：D: 是网络映射不算本地）——4 个 DuckDB（ddj/cuj/sa/tpj）
                       #   全部完成并核验后推送 → \\DESKTOP-M5P610N\d\librebsd\dvd6\Website\ddj\
dvd6/Website/
├── source/              # 只读输入：CUJ/ DDJ/ SA/ TPJ/ images/
└── articles/            # 只读输入：CUJ/ DDJ/ SA/ TPJ/ audio/ video/ forms/ images/

script/                  # 临时脚本（侦察、建库、规则补齐、入大纲、核验；不入库）
├── _ddj_recon_*.py      #   期号/文件清单/schema 侦察
├── _ddj_build_*.py      #   四库建库（解压、HTML 转文本、图片处置调度、refs/summaries/key_facts）
├── _ddj_verify_*.py     #   独立核验（逐字比对、二进制零命中、幂等）
└── _ddj_outline_*.py    #   key_facts 归属写回 ＋ 卷末书目述评 写入

05-卷册大纲/第N卷/卷末书目述评.md    # 增量写（Phase C；ref 锚点指向四库 refs）
```

**Structure Decision（2026-10-05 主理人修正后）**: 四库本身即本批内容的全文库——**不再写入 references_fulltext.duckdb**；四库按 references_fulltext 既有规则补齐 summaries（概述）/refs（GB/T 7714 著录）/key_facts（原料层），建在真本地 C:\ddj_stage，完成后推送 dvd6/Website/ddj/。脚本全部在 script/（不入库），大纲只动授权两层。

## Complexity Tracking

> 无 Constitution 违例，无需豁免记录。
