# Quickstart — 验证与执行引导

**Feature**: `004-refactor2026-backlog-merge` | **Date**: 2026-10-09

> 本件给出**可运行的验证场景**，证明合并清单成立、映射无冲突、单批收束可复现。
> 前置：仓库根 `D:\librebsd`；Windows／Git Bash；`C:/Python314/python.exe` 可用。

## 前置检查

```bash
# 1. feature 目录四件齐备
ls specs/004-refactor2026-backlog-merge/{spec.md,plan.md,tasks.md,checklist.md}

# 2. 唯一任务书存在且未勾项可见
ls .trae/specs/converge-all-remaining-tasks/tasks.md

# 3. 内容源存在（唯一内容真身）
ls "08-核查报告与多轮复核/重构2026/data/outline.txt"
```

## 场景 1：定位复核（对应用户故事 US1）

**目标**：证明“最近的 spec”认定唯一且可复核。

```bash
# 列出两套 spec 落点及其 mtime，确认认定对象时间最新
ls -ld specs/ .trae/specs/
ls -l  .trae/specs/converge-all-remaining-tasks/
ls -l  .trae/specs/finalize-refactor2026/

# 确认排除项主题无关（不得触及重构2026）
grep -n "重构2026" specs/003-login-claim-outline/spec.md
```

**预期**：`.trae/specs/converge-all-remaining-tasks/` 三件 mtime 为 2026-10-09；`specs/003` 仅在“不得涉及重构2026 文件夹（只读）”语境下命中。

## 场景 2：合并清单对账（对应用户故事 US2）

**目标**：证明本 spec `tasks.md` 与唯一任务书一一映射、无新增施工面。

```bash
# 本 spec 的映射键
grep -oE "converge:T[0-9]+(\.[0-9]+)?" specs/004-refactor2026-backlog-merge/tasks.md | sort -u

# 唯一任务书的 Task/SubTask 编号
grep -oE "Task [0-9]+" .trae/specs/converge-all-remaining-tasks/tasks.md | sort -u
grep -oE "SubTask [0-9]+\.[0-9]+" .trae/specs/converge-all-remaining-tasks/tasks.md | sort -u
```

**预期**：本 spec 的映射键集合 ⊆ 唯一任务书编号集合；唯一任务书中未勾 Task（2／3／4／5／6／7）在本 spec 均有对应条目。

## 场景 3：单批收束验收（对应用户故事 US3）

**目标**：证明任一批执行后收束铁律全绿、落账完备。

```bash
# 3.1 口径零漂移
"C:/Python314/python.exe" <sync_refactor2026_baseline.py> --check

# 3.2 门禁全量（件数以 registry 现跑为准）
"C:/Python314/python.exe" <audit_gate_registry.py>

# 3.3 三套浏览器回归（visual / full_matrix / fullsize）→ 须 FAILED=0

# 3.4 落账核对：changelog 与 92 号文 §十一 均有本批行
#     changelog：按 max(id) 与本批登记核对
#     92 号文：grep 本批 batch_id
```

**预期**：`--check` 报零未处置漂移；门禁与三套回归 FAILED=0；changelog 新增本批行；92 号文 §十一 出现本批对账行；页面版本号递增；prebak 备份存在。

## 场景 4：双重台账防线（对应用户故事 US4）

**目标**：证明任一事项仅在一处处于“在途”。

```bash
# 抽取两份台账的在途项，检查交集为空
grep -n "^- \[ \] Task" .trae/specs/converge-all-remaining-tasks/tasks.md
grep -n "converge:T" specs/004-refactor2026-backlog-merge/tasks.md
```

**预期**：无同一事项在两份台账同时为“待施工／在途”；被并入 spec 均带“并入／勾销”标注。

## 验收判据索引

| 场景 | 覆盖需求 | 对应检查点 |
| ---- | ---- | ---- |
| 1 定位复核 | FR-001／FR-002 | checklist 实现完整性层 |
| 2 合并对账 | FR-004／FR-005／FR-006 | checklist 需求覆盖层 |
| 3 单批收束 | FR-007／FR-008／FR-009／FR-010 | checklist 边界与异常层 |
| 4 双重台账 | FR-012／FR-013／FR-014 | checklist 既有功能未回归层 |
