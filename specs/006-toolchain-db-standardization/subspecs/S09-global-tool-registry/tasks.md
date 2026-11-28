---
spec_id: S09
title: 全局工具表
task_book: 01-项目管理/01-编纂规划与报告归档/工具链与数据库标准化-任务书-20261127.md
task_book_anchor: 十一、全局工具表（S09 的设计约束）
version: 1.0.1
status: closed
goals: [8]
owner: ykla
created: 2026-11-27
updated: 2026-11-28
binding_id: TB-20261127-S09
---

# S09 任务清单：全局工具表

## 依赖

- S03 的工具分类
- S11 的清理机制
- D 路清点

## 任务

| ID | 状态 | 任务 | 产出 |
| -- | ---- | ---- | ---- |
| T-S09-001 | TODO | 定 schema 与字段来源。 | schema |
| T-S09-002 | TODO | 写四源合并规则。 | 合并规则 |
| T-S09-003 | TODO | 实现生成器。 | 生成器 |
| T-S09-004 | TODO | 实现校验器与 selftest。 | 校验器 |
| T-S09-005 | TODO | 跑全量生成，复核 stable／one-shot。 | 工具表 v0 |
| T-S09-006 | TODO | 建例外覆盖机制。 | 覆盖文件 |
| T-S09-007 | TODO | 写 dashboard 摘要。 | 摘要 |
| T-S09-008 | TODO | 复核：字段、覆盖、tracked 一致。 | 复核记录 |

## 完成判据

- 全部任务 DONE，且有证据路径。
- `checklist.md` 全部 PASS，或挂账有批准。
- 变更记入任务书 §19 与 `changelog.duckdb`（如触及入库件）。
- 绑定清单已重算（`BINDING.tsv` 与任务书附录 C）。

## 执行纪律

1. 单批单目标；每批有意图确证、验收判据、回退。
2. 写库另批；写前 guard＋waterlock；写后独立回读。
3. 不删、不移、不改结构；清理另批。
4. 标准引用回官方原文；不凭记忆。
5. 数字给测量命令与时点；不凭记忆报数。
6. 失败即停、复核、再决定；不连续重派。
7. 不设自动化；人在场按批推进。
