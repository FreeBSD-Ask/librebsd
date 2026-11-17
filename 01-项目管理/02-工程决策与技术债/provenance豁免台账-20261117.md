# provenance_history 豁免台账（2026-11-17 建）

对象：`04-现代研究文献/historical_claims.duckdb` 的 `provenance_history` 表。
设立缘由：`audit_provenance_dupes.py`（数据库类门禁）在批 C 回填空 id 后（D2b＝0，PASS）仍存两类**存量形态**残量，
按该件口径“仅登记不阻断”；本台账为其显式登记处，防止残量静默腐烂。

## 一、已闭合项（留痕）

| 项 | 处置 | 证据 |
| -- | ---- | ---- |
| D2b 裁定日起空 id 3 310 行 | 2026-11-17 批 C 受控修库回填：空 id 12 246 行按（at，rowid）时序续编 2170—14415，另写 1 条 `provenance_id_backfill` 留痕行（14416） | 写前专项备份 `12-数据库备份/historical_claims/20261117_095034.duckdb.gz`（integrity=ok）；`claimdb_guard --db historical_claims` PASS；`rotate_guard_state pre/post` 已存档；复检 D2b＝0 |

## 二、存续豁免（登记不阻断，复审 2027-01-29）

| 编号 | 判据 | 残量 | 形态说明 | 不阻断理由 |
| ---- | ---- | ---- | -------- | ---------- |
| PE-01 | D3 source_id 空值 | 484 行（3.45%） | `claim_backfill` 482＋`claim_fix` 1＋本次留痕 1；detail 只含 claim 编号（CL-RM-xxxxxx），不含源编号，无法机械推导 source_id | 无推导路径；强行猜测即违反 0 信任。后续如需补齐，应回源逐条考据（人工），非本批范围 |
| PE-02 | D5 id 序列冲突 | 1 组 19 行（id=2014，均 2026-10-15） | 裁定日前存量形态；回填后新编号自 2170 起，与该组不冲突 | 改动将重写历史写入痕迹，违反审计表不可静默改写的口径；保留原样并登记 |

## 三、复审触发

- `audit_provenance_dupes.py` 判据变更（D2／D3／D5 口径调整）时重评；
- 任一残量增长（超过上表数字）时，视为新缺陷而非存量，不得沿用本豁免；
- 2027-01-29 定期复审（与 `13-软件工程/` 复审同日）。
