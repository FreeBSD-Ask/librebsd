# 20260909 新闻组needs_recheck存量清理考据

## 考据对象与范围

- 清理对象：`script/_db_row_mining/review_logs/` 下 7 份 `usenet_ng__23_triage_s*_c0*.jsonl` 台账中全部 `needs_recheck` 标记 708 条，另含审读日志 08-31 节所记 p001/p004 时代遗留 12 条（pk 79/87/94/99/104/109/111/112/116/122/123/234），合计 720 条。
- 口径基线：spec `db-row-traversal-mining-2026-08-29` 三态判定（候选/已审读无价值/待复核）——待复核不得丢弃，本次为其终态化。

## 查证来源

- 一手史料：usenet_mail.duckdb messages 原始正文（复读视图 `_nr_review_view_20260909.txt` 每行 pk|date|from|subject|bodylen|head240；候选 11 条另经全文/中段 Pass B）。
- 台账与落库实况：7 份 triage jsonl；historical_claims.duckdb 四表（raw_source/evidence/claim/claim_evidence）。
- 落库产物：`_register_ng23_nr_20260909.py`（CL-RM-014882~014892）；处置台账 `review_logs/usenet_ng__23_needs_recheck_resolved_20260909.txt`。

## 交叉验证方法

1. **对账优先**：先以 raw_source.source_db='usenet_mail' 对 708 条逐 pk 对账，确认 507 条已由先期落库批次转正（09-09 批次 849 条及更早批次）；再以四表 join 反向核验该 507 条 claim 链完整（**无孤儿 raw_source**）。审读日志所记“505 条待复核”确认为三态时点快照而非真实待办。
2. **终审复读**：未落库 201 条（A 组）+ 早期遗留 12 条（B 组）生成紧凑视图逐条过目；对 88741-88740 段 167 条直接援引本会话当日 c011 全行审读判定（passA_23_s88541_c001.txt 视图为证，非重复读取）。
3. **重投机械验证**：4 对疑似同文重投（87606/87604、87721/87663、87725/87711、87726/87613）经 body 全等比对，**4/4 字节级全等**，判 merged，不重复立张。
4. **Pass B 定向深读**：87816（McGeady 源码分发说明）读全文后立张；88829 经中段深读判为设计哲学文不立张（其涉及的 exec 关标准描述符提议已由 88851 转述行覆盖）。
5. **转正落库复核**：11 条候选（全 L4）引文同串校验（11/11）、单事务写入、写后反查（11/11）、四表 join（11/11）。

## 存疑判定依据

- **empty 3 条**（87640/87668/87702）：库内正文长度 2 字符，属数据不存在而非内容缺失——按“待转录/数据不存在登记挂起”惯例永久挂起，不算未处置项。
- **c011 段 167 条 no_value 的判定效力**：援引同日（2026-09-09）本会话对该 200 行切片的逐行审读记录，其中 30 条已立张、170 条判无价值，台账的 197 条 recheck 与之完全对齐（197=30+167），无遗漏行。
- **竞争口径并存**：osh 释名（87550 operator shell 说与 87912 dmr 裁定 V6 shell 说）两说均入主张库，供大纲辨析字段择用；不因 dmr 权威而弃前者（前者为 BTL 内部使用实况，后者为命名史权威口径）。
- 处置终态分布：**landed 519 / no_value 194 / merged 4 / empty 3 = 720**，needs_recheck 存量清零。

## 关联留痕

- 审读日志：`script/_db_row_mining/review_logs/usenet_mail.md`（2026-09-09 needs_recheck 存量清理收口节）
- changelog：id=1170（2026-09-09）
- 处置台账：`review_logs/usenet_ng__23_needs_recheck_resolved_20260909.txt`（720 行逐条终态）
- 转正候选：`review_logs/usenet_ng__23_comp.unix.wizards_candidates_nr.txt`（11 条）
- 脚本：`_nr_census_20260909.py`、`_nr_precheck_20260909.py`、`_nr_build_view_20260909.py`、`_nr_passB_verify_20260909.py`、`_nr_cand_meta_20260909.py`、`_nr_resolve_ledger_20260909.py`、`_register_ng23_nr_20260909.py`、`_wrapup_nr_20260909.py`
