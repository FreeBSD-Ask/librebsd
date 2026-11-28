# ADR 草案 0023：28 库 schema_meta 标准落地与零声明约束评估

**状态**：草案（待 ykla 批后转正式）｜**日期**：2026-11-28｜**关联**：TG-018、S02 迁移批

## 背景与问题

Tier A 28 库 schema_meta 无一符合 proposed 标准（12 缺失＋10 列不规范）；243 表中 221 张零声明约束（含 historical_claims.claim、changelog.entries，`duckdb_constraints()` 实测）；注册表 built_at 缺 91.2%。

## 选项

A. 维持现状（应用层保证唯一性）——登记表继续漂移，剖析不可自动化。
B. 迁移批统一落地 schema_meta＋声明主键（推荐）——dry-run 先验证应用层 id 唯一性成立；不改变数据。
C. 只做记分卡不落 schema——指标不可持续复算。

## 决定（建议）

B。执行顺序：login-zazhi 重建（先）→ schema_meta 统一 → 主键声明 → 注册表字段修复（built_at/size_bytes/sha256 全量回填）。

## 后果

- 正面：剖析/记分卡/门禁可全自动；唯一性有库级兜底。
- 负面：迁移批写库须 guard＋waterlock＋专项备份槽；主键声明若与历史数据冲突须先清洗（dry-run 暴露）。
- 回退：ADR-0017 口径（跑档内 load.sql）。
