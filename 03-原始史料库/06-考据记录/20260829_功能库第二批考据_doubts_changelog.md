# 功能库第二批行级遍历考据：doubts_standalone 与 changelog

日期：2026-08-29
Spec：db-row-traversal-mining-2026-08-29（Phase 2A 收口）

## 查证来源

- doubts_standalone.duckdb 三表 dump（_dump_doubts_resolve.jsonl / _dump_doubts_reviewlog.jsonl / _dump_doubt s_markers.jsonl，合计 5791 行，progress 已登记全量读取）
- changelog.duckdb entries 表 19 个页文件（_pg_chg_p1~p19.jsonl，929 行）
- 去重查证：historical_claims.duckdb 只读查询（claim/evidence/raw_source）
- 产物：claims_to_write_doubts_standalone.jsonl（14 条，CL-RM-000701~000714）、claims_to_write_changelog.jsonl（1 条，CL-RM-000801），已逐条写入并回读校验

## 交叉验证方法

1. doubts_standalone：先统计 resolution_status 全量分布（resolved 1968 / unresolvable 19），对 resolved 行按交叉验证结论标记抽取候选池 124 条，逐条人工过目判级；14 条采纳主张的 quote 用脚本断言严格取自源行 doubt_text 子串（同串校验）。关键事实溯源链均已在源行留有原考据 URL（如 mail-index.netbsd.org/netbsd-users/1994/12/23/0000.html、openssh.com/txt/release-7.4、apple-oss-distributions/xnu），本次采纳时对这些一手核验链复用并标注。
2. changelog：动作词全量分布 + 6 点抽样精读，确认 929 行中仅 1 行含外部史学事实（FreeBSD 1.0 发布 1993-11-01，Jordan Hubbard 一手公告），与既有主张（CL-RM-000004 为 5.0）不重复。
3. 全部写入逐条执行，写后回读校验（claim/evidence/claim_evidence 三表行数断言）。

## 存疑判定依据

- ARPA 资助 MAC 主张（CL-RM-000708）：具体合同编号与 DTIC 档案号因 DTIC 系统维护、MIT Libraries 物理档案（box 18-22）未数字化而保留存疑（源行原文已载明），主张文本中如实标注，仅采信三源交叉确证的资助事实与金额量级。
- UNIX 许可费主张（CL-RM-000709）：仅采信多源确证的 1983 年（$43,000/CPU 起）与 1989-1990 年（SVR4 $100,000）数字；“1985 年 20 万”“1987 年 40 万”经源行判定为疑似臆造，主张中明确禁止引用。
- changelog 库其余 928 行为编纂过程日志，无外部可考据事实，判无价值（非存疑）。
- 本批无 unresolvable 项新增。
