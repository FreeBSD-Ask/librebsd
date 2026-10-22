# checklist.md — td023-merge-266-20261022

## 前置与方案

- [x] 取证：尾部 11 个非空行 0 独有内容；字段序列 `[1,2,3,4,5,5]`
- [x] 方案：删 L50–66（17 行），保留 L1–49；主理人 2026-10-22 批准
- [x] dry-run：A1–A3 PASS（67→50 行）
- [x] 审计台账准入行（高风险）

## 执行与断言

- [x] 文件 67 → 50 行
- [x] A1 被删 11 个非空行全部在保留部分有同文行
- [x] A2 字段序列 `[1,2,3,4,5]`
- [x] A3 题解 1／`###` 2 互异／`####` 1
- [x] A4 文件无注释锚（锚门禁不受影响）
- [x] A5 仅该 1 文件改动、无增删、树 37,486 不变
- [x] A6 无 BOM／LF
- [x] 派生件再生：`chapter_keywords.json`／`theme_index.json`；`sync_outline_mirror --check` 零漂移

## 门禁

- [x] `audit_anchor_pairs --check` 0
- [x] `audit_anchor_pair_order --check` 0
- [x] `audit_md_quote_glyphs` 0／`audit_md_bold_spacing` 0／`audit_markdown_lint` 0
- [x] `sync_refactor2026_baseline --check` 0

## 复核（3 轮）

- [x] R1 主理人批准方案
- [ ] R2 应用后逐行回验（子代理）
- [ ] R3 结构语义独立复核（子代理）

## 台账与收口

- [ ] TD-023 偿还证据补合并结果
- [ ] changelog 一行
- [ ] 审计台账收口四段齐；复核台账 R1–R3
- [ ] 第12卷单笔提交＋派生件＋文档
- [ ] 归档 `008-td023-merge-266-20261022`

## 已知限制

- 仅合并结构；不补字段、不改措辞、不调小节顺序。
- 其余 23 个缺口文件（22 件补字段、1 件字段 6 待核）不在本批。
