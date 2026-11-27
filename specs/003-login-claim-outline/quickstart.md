# quickstart.md — 终局验证指南（login 判定入藏战役）

**Feature**: specs/003-login-claim-outline | **Date**: 2026-10-06

## 前置条件

- login-zazhi.duckdb 完整（419 期 / articles 6,604 / 标题治理终态）
- historical_claims.duckdb 可写（claim 393,153 行基线已记录）
- 判定台账 `script/_login_claim_ledger_20261006.jsonl` 与引擎/写者脚本就位
- 重构2026 哈希基线 `script/_login_claim_baseline_20261006.json` 已采集

## 验证场景（全部只读 SQL＋门禁，按战役收口逐条跑）

### 1. 判定覆盖率 100%（SC-001）

```sql
-- 台账行数 = articles 行数，且含全部 kind
SELECT count(*) FROM read_csv('script/_login_claim_ledger_20261006.jsonl');  -- = 6604
SELECT kind, count(*) FROM articles GROUP BY 1;  -- 广告/toc/frontmatter 均有对应台账行
```

### 2. claim 三层入藏齐备（SC-002）

```sql
-- 抽样一条 SRC-login 的三层链
SELECT * FROM raw_source WHERE source_id = 'SRC-login:<id>';
SELECT e.* FROM evidence e JOIN raw_source r USING(source_id) WHERE r.source_db='login-zazhi';
SELECT c.* FROM claim c JOIN claim_evidence ce ON c.claim_id = ce.claim_id
  JOIN evidence e ON e.evidence_id = ce.evidence_id WHERE e.source_id = 'SRC-login:<id>';
-- quote 原文一致性抽检：evidence.quote 与 login 库 body_text 逐字比对
```

### 3. 05-大纲同步（SC-003）

```sql
SELECT * FROM source_chapter WHERE source_id = 'SRC-login:<id>';  -- 挂钩齐备
```
宿主章文件注入块抽查（ROW_MINE 块体格式＋等级真值）；门禁：
```
python 00-编纂规则与格式规范/01-规则/脚本与命令/audit_evidence_level_labels.py   # exit 0
```

### 4. 重构2026 零涉及（SC-005）

重采哈希清单与基线比对：
```
python script/_login_claim_baseline_check.py   # 零变更 exit 0（战役自产终检脚本）
```

### 5. 行数守恒与合规（SC-006）

```sql
SELECT count(*) FROM articles;    -- 6604 不变
SELECT count(*) FROM claim;       -- 393153 + 本战役增量
SELECT count(*) FROM information_schema.columns WHERE data_type IN ('BLOB','VARBINARY');  -- 0
SELECT * FROM update_log ORDER BY rowid DESC;  -- 本战役登记行齐全
```

### 6. 断点续传（SC-007）

在判定/入藏中途 kill 引擎后重跑：台账行数无漂移、claim 库无重复行（幂等键＝article_id）。

## 预期结果

全部场景通过＝战役收口；任一失败按 tasks.md 对应任务返工。
