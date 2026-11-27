# Contract: 四库规则补齐与大纲对接（2026-10-05 主理人修正版）

> 原契约“references_fulltext.duckdb 增量写入”已按主理人令**整体删除**：四库本身即本批内容的全文库，不向 references_fulltext.duckdb 写任何行。

## Phase B′：按 references_fulltext 规则补齐四库

对每库（本地暂存 `C:\ddj_stage\<code>.duckdb`）新增三表，schema 与纪律如下：

1. **refs 著录**：每 article 恰一条；`bibliography_entry`＝GB/T 7714 期刊著录（作者. 题名[J]. 刊名, 年(期).）；id 稳定号 `<DB>-<序>`；幂等键 (article_id)。
2. **summaries 概述**：schema 同 references_fulltext.summaries（id/reference_id/summary/topic_keywords/important_excerpts/processing_status/processed_at）；summary＝中文 3–6 句、topic_keywords 顿号分隔、important_excerpts 原文照录摘引；reference_id 指向本库 refs.id；已有 toc_abstract/searchdescription 的 article 可作底稿但须改写为中文概述。
3. **key_facts 原料层**：schema 同 references_fulltext.key_facts 12 列；reference_id 0 悬空硬约束；id＝`kf-<db>-<ref>-<seq>`；fact_category 沿用既有类目；source_quote 原文照录；related_chapter 留待 Phase C 写回（跟新不跟旧）。
4. **留痕与幂等**：build_log 逐批记账；三表构建脚本可安全重跑（业务键先查后插）；写读分离。
5. **概述生成纪律**：子代理只读库内 body_text（不读源文件），产出 JSONL 主会话合并；禁臆造——概述不得引入正文没有的事实；“回报不可信、产物可信”照常适用。

## Phase C：大纲两层（授权范围不变，锚点格式更新）

1. **授权边界**：只写 key_facts 的 related_chapter 写回＋各卷 `卷末书目述评.md` 追加；**禁止** SUMMARY/章正文/任何成稿正文层。
2. **锚点**：新增 bullet 采用 `- **ref <DB>-<id>**｜` 体例（如 `ref DDJ-1027`），指向四库 refs.id——**偏离既有 `ref NNNN`（references_fulltext）体系，主理人 2026-10-05 修正案已确认**；key_facts 同步用本库 refs。
3. **判重**：书目述评追加以 `- **ref <DB>-` 前缀 bullet 匹配本批判重（既有 `ref NNNN` bullet 不触碰）；体例跟宿主实测。
4. **写盘**：统一 `write_guard()`（UTF-8 无 BOM、LF、has_block 幂等）。
5. **ref 悬空**：新增 bullet/key_facts 的 ref 必须回指四库 refs（0 悬空）；四库推送后核验双侧一致。

## 跨阶段共用纪律（不变）

- 独立核验写读分离、多读共识；对空集合先断言非空。
- 提交：pathspec 限定、`--no-gpg-sign`；`script/` 与 `*.duckdb` 不入 git。
- **推送门禁**：四库从 C:\ddj_stage 复制到 dvd6/Website/ddj 后，逐库字节级 sha256 比对＋双侧行数断言，全绿才算交付。
