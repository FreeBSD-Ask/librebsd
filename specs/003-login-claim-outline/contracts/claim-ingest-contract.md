# claim 库三层入藏契约（claim-ingest-contract）

**Feature**: specs/003-login-claim-outline | **Date**: 2026-10-06

对判定 `claim_ingest` 的条目，向 historical_claims.duckdb 三层入藏（字段见 [../data-model.md](../data-model.md) §2-5）。事务批 200 行＋批前/批后行数断言（纯增量，违规整批回滚进隔离）。

## L1 raw_source（注册制）

- `source_id` = `SRC-login:<article_id>`，全库唯一；`source_db='login-zazhi'`、`source_table='articles'`、`local_pk=article_id`；
- `content_hash` = SHA-256(body_text)（入藏时计算，审计可回验）；
- `source_layer` = 2（P41 五层级：一手印刷档案层）；`banned_source` 不适用（;login:/UNIX News 为 P42 邮件列表中心主义认可的一等史料载体）。

## L2 evidence

- `evidence_id` = `EV-login:<article_id>:<seq>`；`anchor` = `login-zazhi:articles:<article_id>`；
- `quote` = body_text **原文照录零改写**（噪声/原件笔误照录——不篡改铁律）；
- `fact_text` = 判定引擎提炼的事实性要点（支撑拟议 claim，不多源表述混入）。

## L3 claim

- `claim_id` = `CL-<卷>-<序号>` 按所映射卷续排（全库唯一）；
- `claim_type` ∈ 十值枚举；`evidence_level` ∈ L1-L5（**L5 最强**——与 source_layer 方向相反，禁混用）；
- `wording_gate`：L1 级证据的 claim 禁写"继承/影响/源自/借鉴"（07 号措辞门禁）；
- `status` ∈ proposed/supported/contested/refuted/superseded；refuted/UNVERIFIED 合法入库不物理删除。

## L3 挂钩

- `claim_evidence`（role：supporting/contradicting，反证带 disposition）；
- `source_chapter`（vol/ch/sec，link_type ∈ used/mentioned/background，多值多行）；
- `claim_period`（六期多值，交叠为设计特性）；`claim_entity`（subject/object 角色）。

## 事务与断言

- 批 200 行：BEGIN → n0/n1 行数断言 → COMMIT；违例 ROLLBACK＋整批隔离；
- update_log 登记（批次/规模/备份指针）；纯增量（既有行零 UPDATE）。
