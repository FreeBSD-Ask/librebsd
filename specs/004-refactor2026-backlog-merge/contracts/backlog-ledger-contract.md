# Contract — 合并总账三契约

**Feature**: `004-refactor2026-backlog-merge` | **Date**: 2026-10-09

> 本契约约束“来源 → 合并清单 → 落账”三段的接口形态。任何合并条目违契约即**不合格**，须返工。

## §1 来源契约（Source Contract）

**输入**：任一被列为“待执行”的事项。
**义务**：

1. 该事项 MUST 携带**可定位的证据锚点**，形式为下列之一：
   - 文书路径（可含行号），如 `08-核查报告与多轮复核/重构2026/125-重构2026收官总案-20261008.md` §七；
   - 库锚点，形式“库名＋主键”，如 `historical_claims.duckdb` ＋ `claim_id`；
   - 载体实测，如 `重构2026/data/outline.txt` 行号。
2. MUST NOT 以**文书自述**或**子代理回报**单独作为“未闭环”的判据。
3. 锚点 MUST NOT 指向临时目录（`_tmp/`／`_audit_tmp/`／`script/` 下的临时件）。

**违例判定**：无锚点，或锚点为自述性描述 → FAIL。

## §2 映射契约（Mapping Contract）

**输入**：本 spec 的 `tasks.md` 与被并入的唯一任务书 `.trae/specs/converge-all-remaining-tasks/tasks.md`。
**义务**：

1. 本 spec 的每一条**施工类**任务 MUST 带 `ledger_map`，且能在唯一任务书中命中**唯一** Task/SubTask。
2. 唯一任务书中的每个未勾 Task/SubTask MUST 在本 spec 中至少出现一次（**无遗漏**）。
3. 本 spec MUST NOT 引入唯一任务书中不存在的**新增施工面**（纯文档类任务除外，如本 spec 的 US1／US2／US4 产出件）。
4. 同一事项 MUST NOT 在两份台账**同时**处于“在途”。

**违例判定**：映射缺失／一对多／多对一／新增施工面 → FAIL。

## §3 落账契约（Ledger Contract）

**输入**：任一批施工的收束动作。
**义务**（收束铁律，逐条 MUST）：

1. 改**唯一内容源** `08-核查报告与多轮复核/重构2026/data/outline.txt`（`index.html` 禁手改）。
2. 装配：`assemble_index.py`。
3. 字体子集：`font_subset_rebuild.py`（**视是否产生新字**；须先装配后重建，再装配）。
4. 门禁**全量**（件数以 `audit_gate_registry.py` 现跑为准）＋**三套浏览器回归** → 须 FAILED=0。
5. 落账：`changelog.duckdb`（经 update_log）＋ **92 号文 §十一**（唯一对账入口）＋ 98 号文 §十一。
6. 页面版本号**递增**（内容层变更）；零内容层变更者不递增，但须登记。
7. 备份：prebak **先行**，改动可回退。
8. 提交：**路径限定** `git commit -m <msg> -- <paths>`；不 commit 他人改动、不 rebase、不 `--force`。

**落账字段**（须齐备）：`batch_id`／`changelog_id`／`version`／`prebak`／`gates_result`／`reconciled_in`。

**违例判定**：任一条未满足 → FAIL，本批不得标记为 `已落账`。

## §4 文本纪律（横切契约）

- UTF-8 **无 BOM**、**LF** 行尾。
- **禁直角引号**（U+300C／U+300D）与**制表符**。
- 全库禁用“谱系”词（标题与注文一并；判据已固化于门禁）。
- 引号／反斜杠／`$` 等特殊字符的批处理一律走 `script/` 下脚本文件（禁 `python -c` 内联）。

## §5 冻结合约（Endgame Contract）

1. 结构冻结 MUST 待**内容层收编（Task 2）＋ 终校（Task 6 前置）**完成后执行。
2. 冻结后 MUST NOT 再动卷级结构。
3. 收官 MUST 落**冻结声明**，并刷新长线任务总登记表机读块（`_longline_status.py --write-block`）。
4. 被并入 spec MUST 统一勾销／标注并入（`finalize-refactor2026`／`execute-login-title-fix-and-figures-ocr`／`write-doubt-marker-taskbook-2026-09-30`／`mail2d-*`／`podcast-*`／`digest-linux-mining-legacy-phase3` 等）。
