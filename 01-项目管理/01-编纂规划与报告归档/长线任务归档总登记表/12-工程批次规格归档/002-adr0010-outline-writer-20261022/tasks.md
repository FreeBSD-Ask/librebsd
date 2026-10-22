# tasks.md — adr0010-outline-writer-20261022

- [x] T1 任务准入：`任务审计台账.md` 新行（PASS＋准入证据），风险级别高风险、复核轮次 3
- [x] T2 编写 `脚本与命令/outline_writer.py`：参数面（--root/--host/--claim-map/--outline-map/--work/--ledger/--allow-root/--narr/--candidates/--db/--lib/--tag/--ts/--scan-root/--labels/--label-map/--write/--check-only/--selftest）
- [x] T3 路径断言与生效路径打印（commonpath；allow-root 默认仓库根）
- [x] T4 宿主权威解析（claim_map hosts／outline_map；multi 由 narr 宿主列消歧；不猜文件名）
- [x] T5 块级锚点幂等（扫描面默认章节目录；--scan-root 可扩）
- [x] T6 写盘契约（临时件→fsync→os.replace；全或无回滚）
- [x] T7 写后断言（增量＝计划数、每键恰一次、旧锚保留、编码）
- [x] T8 失败路径 stdout 可见 + exit 2（坏 key／空正文／越界 pk／宿主未解析／claim 悬空）
- [x] T9 台账追加（全或无、字段同生产）
- [x] T10 `--selftest` 正／负样本
- [x] T11 沙箱 L0：生产前后聚合哈希（05-卷册大纲）＋claim 库只读元数据
- [x] T12 沙箱 L1：读入真实（ADR-0010 沙箱 20 pk claim_map／narr；--check-only 生产解析率）
- [x] T13 沙箱 L2：写入生产等价副本（第 097 章副本；--write）
- [x] T14 沙箱 L3：逐条内容回读（块头四要素＋摘要行逐字节）
- [x] T15 沙箱 L4：二跑 +0＋第 2/3 跑 stdout 逐字节一致＋还原哈希复原
- [x] T16 沙箱 L5：坏件三例（坏 key／空正文／越界路径）→ exit 2、stdout 可见、零写入
- [x] T17 验证报告：`script/_adr0010_verify_20261022/VERIFY.md`（命令＋原始输出＋判定）
- [x] T18 登记接线：registry 去重复件次号、补 STAGE_MAP、补 selftest；`脚本与命令/README.md` 行；`流程规则.md` 小节＋二级索引
- [x] T19 TD-015 更新＋`index.md` 偿还进度（附本批证据）；发现项登记（L3 抬头口径与 ROW_MINE 规则 §四 的差异披露）
- [x] T20 门禁：`audit_gate_registry.py`（R1–R8 全 PASS）、`audit_engineering_practice.py`、`audit_task_lifecycle.py`、`audit_markdown_lint.py`、`audit_md_quote_glyphs.py`、`audit_md_bold_spacing.py`、`sync_refactor2026_baseline.py --check`、`_longline_status.py --check`、`outline_writer.py --selftest`
- [x] T21 独立复核两轮（复核子代理：初稿、修复后复验）＋主理人签收（ADR-0010 批准令）
- [x] T22 收口：changelog（changelog.duckdb，prebak）＋两台账回填＋规格归档指针

## 依赖

T2–T10 → T11–T17（先有脚本后验证）→ T18（登记接线依赖脚本存在）→ T19（依赖证据）→ T20 → T21 → T22。

## 变更记录（滚动基线，TG-002）

| 序号 | 日期 | 变更 | 理由 | 影响面 |
| ---- | ---- | ---- | ---- | ------ |
| 1 | 2026-10-22 | 初稿 | TD-015 偿还前置（ADR-0010 执行件） | 本批 |
| 2 | 2026-10-22 | 复核驱动修订：F1–F9 修复（严格读／台账前置＋回滚／键校验／Abort 化／判重并入权威宿主＋跨文件披露／`--allow-narr-host`／ASCII pk／`--host` 未命中拒写） | 第 2 轮独立复核判 FAIL（RV-20261022-008） | T2–T8、T10、T12–T16 复跑；selftest 19 例 |
