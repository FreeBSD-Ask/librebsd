# 判定台账 JSONL 行契约（ledger-contract）

**Feature**: specs/003-login-claim-outline | **Date**: 2026-10-06

台账文件＝`script/_login_claim_ledger_20261006.jsonl`（append-only，UTF-8 无 BOM＋LF）。每行一个 JSON 对象，字段见 [../data-model.md](../data-model.md) §1。

## 行契约

```jsonc
{
  "article_id": 123,              // 幂等键；∈ login-zazhi articles.article_id
  "identifier": "login_june-july-1978",
  "kind": "article|column|news|ad|toc|frontmatter|unknown",
  "verdict": "claim_ingest|no_ingest",
  "significance": "历史意义/价值摘要 ≤200 字",
  "reasons": ["R11", "R8", "七类不写:开发者回忆录合集"],  // 所引原则编号，非空
  "chapter_target": {"vol": 5, "ch": 91},   // claim_ingest 必填；no_ingest 可 null
  "claim_ids": ["CL-5-xxx"],      // 入藏后回填
  "judged_by": "llm:agent-login",
  "judged_at": "2026-10-06T…"
}
```

## 硬规则

1. **全量唯一**：article_id 唯一且覆盖 6,604/6,604（禁抽查；广告/目录/刊头同等待遇）。
2. **理由非臆造**：reasons 必须为可回溯的原则编号（R1-R12/P 编号/七类不写判据），no_ingest 时 reasons 非空。
3. **断点续传**：引擎按台账已有 article_id 跳过；重跑幂等（同 id 不产生第二行——重复行视为 bug 并隔离）。
4. **chapter_target 有效性**：vol/ch 必须命中既有 54 卷 454 章口径（或触发新建章流程）。
