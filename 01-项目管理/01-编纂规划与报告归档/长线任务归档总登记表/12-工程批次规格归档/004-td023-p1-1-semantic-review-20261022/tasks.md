# tasks.md — td023-p1-1-semantic-review-20261022

- [x] T1 准入：`任务审计台账.md` 新增本行，任务 ID＝本目录名，风险级别＝普通
- [x] T2 全量分组：920 条 → 141 组，落 `script/_td023_judge_20261022.csv`
- [x] T3 行段结构判定：`C1 空壳重复` 920 条、`C2 带正文` 0 条（分类器含正负夹具自检）
- [x] T4 正文保真回溯：基线 `0b9e4382d` 减删除行 vs 当前树，正文多重集丢失 0、新增 0
- [x] T5 判定表落盘：`script/_td023_verdict_20261022.csv`（141 组，全部 `可删（无正文可失）`）
- [x] T6 六分片切分：`script/_td023_shard1..6_20261022.csv`（15/15/14/14/14/15 文件）
- [ ] T7 分片 1–5 复核子代理（5 路并发）逐组重算
- [x] T8 分片 6 主代理独立实现复核（`script/_td023_shard6_check.py`）
- [x] T9 报告落盘：`01-项目管理/02-工程决策与技术债/TD-023-P1-1语义抽审报告-20261022.md`，并登记 `index.md`
- [x] T10 台账回填：TD-023 状态、changelog、审计台账收口行、复核台账两轮
- [x] T11 门禁：`audit_task_lifecycle`、`audit_engineering_practice`、`audit_md_quote_glyphs`、`audit_md_bold_spacing`、`_longline_status --check`、`sync_refactor2026_baseline --check`
- [x] T12 收口：checklist 全勾、规格归档指针

## 变更记录

| 序号 | 日期 | 变更 | 理由 | 影响面 |
| ---- | ---- | ---- | ---- | ------ |
| 1 | 2026-10-22 | 初稿 | TD-023 只读判定口径 | 本批 |
