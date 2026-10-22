# tasks.md — td022-crossvol-review-20261022

- [ ] T1 准入：`任务审计台账.md` 新行（PASS＋准入证据；高风险、三轮复核、TG-003／004／008）
- [ ] T2 逐项裁定表：77 项标注 `FALSE-POSITIVE`／`REAL`＋错位成因，落 `script/_td022_cv_verdict_20261022.csv`
- [ ] T3 批前快照：全树 .md 数、BEGIN/END 各家族计数、`ROW_MINE`／`DEEP_ANALYSIS` 多重集、逐文件 sha256
- [ ] T4 空壳删除：断言两文件仅标题＋BEGIN 后删除，记录删除前全文 sha256
- [ ] T5 补 BEGIN：`130.0.18`、`130.0.19` 首条目前插入同形 BEGIN，回读断言各 +1 行且位置正确
- [ ] T6 断言：BEGIN/END 总数守恒、按章数值序零残余、非标记行逐字不变、锚多重集不变、无 BOM／CRLF
- [ ] T7 镜子同步：`sync_outline_mirror.py --check`（必要时 `--write`）、`audit_mirror_ingest.py`
- [ ] T8 新脚本：`脚本与命令/audit_anchor_pair_order.py`（`--check`／`--csv`／`--selftest` 正负样本）
- [ ] T9 判据固化：`TD-022-成对锚处置判据书.md` 补 D4 修订（作用域＝章、排序键＝节号数值序、伪报教训）
- [ ] T10 门禁登记：`audit_gate_registry.py`（第三十四件＋STAGE_MAP）、`脚本与命令/README.md`、`流程规则.md` 二级索引
- [ ] T11 台账归位：补 159 批 changelog、去重线批号消歧、本批 changelog 一行
- [ ] T12 复核：RV 三轮（方案复算／应用后回读／收口复验），写 `任务复核台账.md`
- [ ] T13 门禁全跑：`audit_anchor_pairs --check`、`audit_anchor_pair_order --check`、`sync_outline_mirror --check`、`audit_mirror_ingest`、`audit_disk_terminology`、`audit_md_quote_glyphs`、`audit_md_bold_spacing`、`audit_gate_registry`、`audit_task_lifecycle`、`audit_engineering_practice`、`sync_refactor2026_baseline --check`、`_longline_status --check`
- [ ] T14 收口：changelog、两台账回填、`checklist.md` 全勾、规格归档指针

## 依赖

T2 → T3 → T4／T5 → T6 → T7 → T8／T9 → T10 → T11 → T12 → T13 → T14。

## 变更记录（滚动基线，TG-002）

| 序号 | 日期 | 变更 | 理由 | 影响面 |
| ---- | ---- | ---- | ---- | ------ |
| 1 | 2026-10-22 | 初稿（由原“77 项逐对处置”改为“复核＋4 条真实缺陷”） | 复核发现 77 项中 75 项为排序伪报，另 2 条真实项漏登记 | 本批 |
