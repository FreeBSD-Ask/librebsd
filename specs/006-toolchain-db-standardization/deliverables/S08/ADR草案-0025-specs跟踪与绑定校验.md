# ADR 草案 0025：specs 入库跟踪与绑定校验器正式化

**状态**：草案（部分已被 ykla 2026-11-27/28 令实现）｜**日期**：2026-11-28｜**关联**：TG-020、G12

## 背景

2026-10-17 裁决 specs 不入库 → 2026-11-27 ykla 令推翻：`specs/` 不排除、入库跟踪（已落地：`.gitignore` `!/specs/**`＋AGENTS.md 改＋commit `6612acf73`）。绑定协议（`binding.md` §16）已有 BINDING.tsv＋临时校验器（B1—B8 PASS），但**正式门禁** `audit_task_spec_binding.py` 尚未建。

## 决定（建议）

1. specs 入库状态维持（ykla 已裁）。
2. 把临时校验器转正为 `脚本与命令/audit_task_spec_binding.py`（B1—B8＋--selftest 正反例），登记第十六件，入常备五项之外按批触发（specs/006 包或任务书改动后）。
3. BINDING.tsv 与任务书附录 C 的双向哈希继续作为跨会话漂移检测。

## 后果

- 正面：spec/任务书漂移可机检；260 个 .trae/specs 仍不入库的口径不变。
- 负面：每次 spec 改动须重算 39 个哈希＋刷新附录 C（脚本化后成本低）。
- 失效：BINDING 行数为 0 或 specs 退回忽略域 → 本 ADR 作废。
