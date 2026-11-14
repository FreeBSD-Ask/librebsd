# D7／D8 数据修正方案小结（2026-10-25）

> 本批只出方案，不写 `mapping.tsv` 与 `review/disputes.tsv`。四张方案表与两份说明均在
> `05-卷册大纲/映射/缺口族分析/`；生成器 `script/_landing_gap_analysis_20261025/p03_datafix_build.py`
> 只读输入、可复跑、二跑零增量。所有计数由脚本断言，非估算。

## 1. 16 条章级 `target_id` 重判

- 现状：16 行全部 `status=DISPUTED`、`review_state=JUDGED`、`note=再分配（2026-10-25）`，`target_id` 为
  `V13-2`、`V19-1`、`V21-1`、`V12-3` 四类章号，落在章级而非节级，不能作为布局输入。
- 结论分布：改判节级 13 条、转 `UNMAPPED` 1 条、待复核 2 条。
- 置信分布：高 5 条、中 9 条、低 2 条。
- 主要错位：V19 组 9 条中 7 条改判到 `V19-1`／`V19-2` 的具体节（UNIX 战争起点、SVR1—3 功能扩展、
  OSF 成立与技术路线、AT&T-Sun 阵营、SVR4 技术整合），1 条（`S-002792`）转 `UNMAPPED`，1 条待复核；
  V13 组 3 条改判 `V13-4.4.1`／`V13-4.4.2`／`V13-2.2.1`；V12 组 2 条改判 `V12-3.3.1` 与 `V14-1.1.3`，
  另 1 条待复核；V21 组 1 条改判 `V21-2.2.3`。`S-002792` 无任何 `V19` 节覆盖，转 `UNMAPPED`；
  `S-002339`（2.8 与 2.10 时段混杂）、`S-002796`（SVR4 驱动接口细节）无单节可完整承接，标“待复核”，不落首节。
- 落表：`12-chapter-level-targets.tsv`，16 行逐条给 `candidate_sections`（`S-xxxxxx` 与节号）、
  `proposed_target`、`evidence`、`confidence`、`action`。

## 2. 459 条台账补录

- 定义：主表 `status=DISPUTED` 而 `disputes.tsv` 无同一 `source_id` 的行；全部在旧第 05 卷，全部 `JUDGED`。
- `subtype` 分布：`anchor` 451 条、`adjacent` 8 条、
  `unknown` 0 条（由 `note` 关键词 `r2_anchor`／`r1_adjacent` 映射）。
- `diff_summary`：取主表 `note` 原文，均为“三规则通过（r2_anchor／r1_adjacent；选项 B 2026-10-24）”。
- `resolution`：统一 `ruled:三规则通过`。`pass_a`／`pass_b`／`pass_c` 原样取主表 `review_a`／`review_b`／`review_c`，
  459 行的三趟均有值，`evidence` 记 `target_id` 与 `note` 以便逐行追溯。
- 落表：`13-disputes-backfill.tsv`，459 行。

## 3. 47 条反向行规范化

- 定义：`disputes.tsv` 有行而主表状态非 `DISPUTED`；30 条 `UNMAPPED`（旧第 06 卷）、17 条 `PENDING`
  （旧第 06 卷 6、第 15 卷 8、第 13 卷 2、第 14 卷 1）。47 行均为 7 列且 `resolution` 为空。
- 处置分布：保留并补 `resolution` 17 条（主表 `PENDING`，有 `target_id`，
  补 `retained:pending→<target_id>`）；标历史行 30 条（主表 `UNMAPPED` 无落点，
  补 `historical:unmapped`）。
- 落表：`14-disputes-normalization.tsv`，47 行；只补 `resolution`，不改主表状态。

## 4. schema 修正影响

- 6／7 列参差：4,893 行 7 列、1,130 行 6 列（缺 `resolution`）。迁移后统一 7 列。
- 补列影响：4,213 行（6 列 1,130 + 7 列空值 3,083），其中
  6 列 886 行与 7 列 562 行写 `pending:未消解`，
  6 列 244 行与 7 列 2,474 行写 `judged:已判定待回填`；不伪造裁决文本。
- 空 `resolution` 清理：7 列中 3,083 行空值（反向 47 + `DISPUTED` 3,036），
  随规范化与补列一并补齐。
- `subtype` 取值未归一（现存 9 种，含 `r1_adjacent`／`r2_anchor`／`rule_resolved`／`rule-resolved`），
  本批只登记建议映射，不改数据。
- 详见 `15-disputes-schema-fix.md`。

## 5. 台账守恒

补录前 `6,023 = 5,976（主表 DISPUTED 在台账） + 47（反向行）`；
补录后 `6,482 = 6,023 + 459 = 6,435（主表 DISPUTED） + 47（反向行）`。
列宽守恒 `6,482 = 4,893 + 1,130 + 459`；
`resolution` 非空守恒 `6,482 = 1,810（原有非空） + 4,213（补列） + 459（补录）`。

## 6. 自检结果

- 16 条章级行全部在册，且 `proposed_target` 的 `S-xxxxxx` 均存在于 `targets.tsv` 且为 `sec` 级。
- 459 条与 47 条计数精确等于主表／台账对账结果。
- 补录后台账 6,482 行，7 列 100%。
- 四张方案表不改任何原表；生成器只读 `mapping.tsv`、`targets.tsv`、`disputes.tsv`。
- 文本规范：UTF-8 无 BOM、LF；中文引号用“”或‘’，无直角引号。
