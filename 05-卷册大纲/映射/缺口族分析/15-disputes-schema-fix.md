# disputes.tsv schema 修正与台账补齐方案

> 本文件只出方案，不写 `review/disputes.tsv`。依据 2026-10-25 只读对账；输入 SHA-256 见
> `script/_landing_gap_analysis_20261025/inputs.sha256`。所有计数均来自 `p03_datafix_build.py` 实测断言。

## 1. 现状与异常

| 项 | 实测 | 说明 |
| --- | --- | --- |
| 台账总行 | 6,023 | 唯一 `source_id` 亦为 6,023，无重复行 |
| 表头列数 | 7 | `source_id`、`pass_a`、`pass_b`、`pass_c`、`diff_summary`、`subtype`、`resolution` |
| 7 列行 | 4,893 | 含 47 条主表非 `DISPUTED` 的反向行 |
| 6 列行 | 1,130 | 缺 `resolution` 列，文件尾无制表符 |
| 主表 `DISPUTED` | 6,435 | 其中 459 行在台账无记录 |
| 空 `resolution` | 3,083 | 7 列行中 `resolution` 为空者；6 列行另计 1,130 行 |
| `resolution` 非空 | 1,810 | 7 列行中已有裁决文本者，迁移不改 |

### 1.1 6／7 列参差的成因

`disputes.tsv` 由多批脚本追加写入：文件表头现为 7 列，但早期批次追加行时只写 6 列
（`source_id`、`pass_a`、`pass_b`、`pass_c`、`diff_summary`、`subtype`），`resolution` 列在后续裁决批
才被逐行写入。追加写入不做回填，于是同一文件同时存在 6 列与 7 列行。该参差不是数据语义差异，
仅为列宽不一致；1,130 行的 `diff_summary` 全部为“三趟不一致”，`subtype` 分布为
adjacent 777、empty-vs-value 345、generic 8，
主表状态全部为 `DISPUTED`，其中 `review_state` 为空 886 行、`JUDGED` 244 行。
逐行读取时若按固定 7 列切分，6 列行会取到空值而不报错，属于“静默缺列”。

同类旁证：`subtype` 取值亦未归一，现存 9 种
（`adjacent`、`generic`、`empty-vs-value`、`lexical-gap`、`r1_adjacent`、`r2_anchor`、`rule_resolved`、
`rule-resolved`、`unknown`），其中 `r1_adjacent`／`r2_anchor` 是规则标签而非差异类型，
`rule_resolved`／`rule-resolved` 仅连字符不同。本批不改 `subtype` 值，只在 schema 中登记建议映射，
避免以格式修正之名改动判定语义。

## 2. 规范 schema（迁移后唯一形态）

- 编码 UTF-8 无 BOM，换行 LF，分隔符为一个制表符，首行为表头，禁止字段内裸制表符与换行。
- 固定 7 列，顺序与表头一致：
  1. `source_id`：`S-` 加六位数字，全局唯一，作为主键。
  2. `pass_a`：A 趟结果，节号或 `∅`；允许“节号｜说明”复合文本。
  3. `pass_b`：B 趟结果，同上。
  4. `pass_c`：C 趟结果，同上。
  5. `diff_summary`：三趟差异摘要，非空。
  6. `subtype`：现行全集见 §1.1；建议归一映射为
     `r1_adjacent`→`adjacent`、`r2_anchor`→`anchor`、`rule_resolved`→`rule-resolved`，
     `adjacent`、`generic`、`empty-vs-value`、`lexical-gap`、`rule-resolved`、`unknown` 保留。
  7. `resolution`：非空裁决文本，前缀限定命名空间
     `ruled:`、`restored:`、`retained:`、`historical:`、`pending:`、`judged:`。
- 落盘前校验：每行列数等于 7、主键唯一、`resolution` 非空、`subtype` 在登记全集内。

## 3. 迁移规则

### 3.1 4,213 行补 `resolution`

补列分两类：6 列行追加第 7 列（不改前 6 列任何字节），7 列空值行原地补第 7 列。
取值按主表 `review_state` 分流，只记录状态，不编造裁决结论：

| 情形 | 行数 | 写入值 | 理由 |
| --- | --- | --- | --- |
| 6 列行、`review_state` 为空 | 886 | `pending:未消解（6 列历史行补列 2026-10-25）` | 主表未消解，台账不得显示为已裁决 |
| 6 列行、`review_state=JUDGED` | 244 | `judged:已判定待回填（6 列历史行补列 2026-10-25）` | 判定已完成但原裁决文本未写入 |
| 7 列行、`DISPUTED` 且未消解 | 562 | `pending:未消解（2026-10-25 补列）` | 与 1,702 条未消解主表行口径一致 |
| 7 列行、`DISPUTED` 且 `JUDGED` | 2,474 | `judged:已判定待回填（2026-10-25 补列）` | 已判定但裁决文本缺失 |
| 7 列行、反向 `PENDING` | 17 | `retained:pending→<target_id>（2026-10-25）` | 见 §3.3 与 14 号表 |
| 7 列行、反向 `UNMAPPED` | 30 | `historical:unmapped（2026-10-25 标历史行）` | 见 §3.3 与 14 号表 |

合计补列 4,213 行（6 列 1,130 + 7 列空值 3,083）。不设按 `diff_summary`／`subtype` 的额外例外：
6 列行 `diff_summary` 全为“三趟不一致”，`subtype` 差异不改变补列取值。
补列后 `resolution` 空行归零，非空 6,023 行；1,702 条未消解主表行中
1,448 行原为空值（6 列 886 + 7 列 562），
其余 254 行已写“待裁决”类非空文本，迁移不改。

### 3.2 459 条补录行

按 `13-disputes-backfill.tsv` 逐行追加，`resolution` 统一为 `ruled:三规则通过`，`diff_summary` 取主表 `note`，
`subtype` 由 `note` 关键词映射（`r2_anchor`→`anchor`、`r1_adjacent`→`adjacent`）。
补录行不带历史标记，其 `evidence` 列仅存在于方案表，不进入台账；台账列仍为 7 列。

### 3.3 47 条反向行

保留不删。`14-disputes-normalization.tsv` 给出 `proposed_resolution`：

- 主表 `PENDING` 17 行（均 `JUDGED` 且有 `target_id`）→ `retained:pending→<target_id>（2026-10-25 保留待落盘）`；
- 主表 `UNMAPPED` 30 行（`review_state` 为空且无 `target_id`）→ `historical:unmapped（2026-10-25 标历史行）`。

两类均补上非空 `resolution`，消除 7 列行中的空值，同时不改主表状态。
`14-disputes-normalization.tsv` 中的 `∅` 表示原字段为空，不是字面值；`current_resolution` 47 行全为 `∅`。

### 3.4 写盘顺序

1. 备份现台账并记录 SHA-256；
2. 先补 1,130 行列宽（纯追加列）；
3. 补 7 列 `DISPUTED` 空值 3,036 行；
4. 补 47 条反向行 `resolution`；
5. 最后按 `source_id` 升序追加 459 条补录行；
6. 跑列数、唯一性、非空与枚举校验；
7. 重算 SHA-256 并与 `mapping.tsv` 对账 `6,435 + 47`。

## 4. 守恒算式

补录前：

```
台账 6,023 = 主表 DISPUTED 且台账有行 5,976 + 反向行 47
6,023 = 5,976 + 47
```

补录后：

```
台账 6,482 = 6,023 + 补录 459
6,482 = 6,435（主表 DISPUTED） + 47（反向行）
```

列宽守恒：

```
6,482 = 7 列原有 4,893 + 6 列补列 1,130 + 新补录 459
6,482 = 4,893 + 1,130 + 459
```

`resolution` 非空守恒：

```
6,023（补列后旧台账） = 原有非空 1,810 + 补列 4,213
6,482（补录后） = 1,810 + 4,213 + 补录 459
```

补录后 7 列占比 100%，6 列行 0，`resolution` 空行 0。

## 5. 边界声明

- 本方案不改 `mapping.tsv`、`targets.tsv`、`disputes.tsv`、`outline.txt` 与旧树。
- 459 条补录只补台账，不改变主表 `status=DISPUTED` 与 `review_state=JUDGED`。
- 47 条反向行只补 `resolution`，不把主表 `UNMAPPED`／`PENDING` 改为 `DISPUTED`。
- 4,213 行补列不写具体裁决结论；`judged:` 前缀明确标注“待回填”，供后续裁决批处理。
