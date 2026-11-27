# login 判定入藏战役收尾报告（specs/003-login-claim-outline）

**Date**: 2026-10-06 | **Status**: 全链闭环

## 终局数字

| 阶段 | 结果 |
|---|---|
| 判定（US1） | **6,604/6,604 = 100.00%**（滚动 40 路子代理，缺 1 补 1，禁止抽查；含全部广告/目录/刊头） |
| 二次复核（T013） | 67/67 分片，**6,604 逐条**，一致率 **98.97%**（6,536 一致 / 68 不一致） |
| 第三遍仲裁 | 68 项全部仲裁（两遍 verdict 翻转项逐条终审，58 项翻转） |
| 判定终态 | **claim_ingest 1,498 → 入藏 1,493 项三层齐备**（仲裁后终值）/ no_ingest 5,106 留痕 |
| claim 三层入藏（US2） | **SRC-login:\* 1,493 = 1,493 = 1,493 = 1,493 = 1,493**（raw_source/evidence/claim/source_chapter/claim_evidence 完全一致）；quote 抽检 100 条零改写；措辞门禁零违规 |
| claim_type 分布 | FACT 1,157 / INTERPRETATION 150 / CONTROVERSY 87 / ORIGIN_CLAIM 41 / FIRST_APPEARANCE 37 / COMPARISON 10 / CAUSAL_CLAIM 4 / MOTIVATION 3 / UNVERIFIED 3 / INFLUENCE_CLAIM 1 |
| 大纲注入（US3） | **1,484 块 written**（ROW_MINE 格式、一手刊文抬头、证据等级真值）；**证据等级门禁 PASS**（exit 0） |
| 归类缺口（US4） | 9 项无映射提案＋46 项 title 错位留档（claim 已入库，大纲挂载待续） |
| 红线 | 重构2026 目录零写入（本战役写入路径全在 script/、05-卷册大纲/、两 DuckDB）；login 库零删改；零二进制 |

## 执行架构（主理人定案）

- **滚动 40 路子代理（缺 1 补 1）**：67 分片 × ~100 篇；首波 40（分片 0-39）＋补位/尾波 27（分片 40-66）；分片 43 计费冻结即重派成功
- 每子代理运行 Python 判定引擎（`script/_login_claim_engine_20261006.py`，LLM 经旧线路 `_glm_line_20261006.py`，key 轮替统一治理）
- 二次复核：引擎 `--verify` 模式（独立提示词，逐条对照首判）

## 过程中修掉的坑（全部固化）

1. **并发台账撕裂**：40 进程并发 append 共享 JSONL（Windows 无原子保证）→ 改**每分片独立台账**＋收口合并（撕裂仅 1 行，重判自愈）
2. articles 表无 kind 列 → 从 seg_review_notes“kind=”标记派生
3. evidence.confidence 是 DOUBLE → 数值型
4. 写者补 BEGIN/COMMIT 批事务＋逐项异常隔离（DuckDB 逐句 autocommit 造成三层不一致）
5. WO-007 write_guard 是整文件覆写语义＋ROW_MINE 带前缀锚点须 existing_pks（b027 教训）
6. 02 遍复核的三坑：重转应用须连 review_notes 一起重置；staging 旧仲裁 verdict 占住 arbitrated 标记；清断点按 id 删连带误删 ARB 条目
7. chapter 编号体系错位（chapter_keywords 全局章号 vs chapter_index 卷内章号）→ **磁盘大纲子串模糊匹配**（100% 命中）
8. claim 序号≠章号（host 解析应走 source_chapter）

## 交付物

- 判定台账：`script/_login_claim_ledger_merged_20261006.jsonl`（6,604 行终态）
- claim 库：`historical_claims.duckdb`（SRC-login:* 1,493 项三层＋0.5K 措辞门禁）
- 大纲注入块：1,484 块分布于 05-卷册大纲 宿主章（written 清单 `script/_login_claim_outline_written_20261006.jsonl`）
- update_log：id=515 登记
- 四件 spec 件：`specs/003-login-claim-outline/`（spec/plan/tasks/checklist）

## 留档待续

- 归类缺口 9 项（无大纲映射提案）＋46 项 title 错位：claim 已入库，大纲挂载待下一手
- 重构2026 目录在战役窗口内有**其他并行会话**的变更（121 号文等），本战役写入路径与该目录零交集


## 加强复核（2026-10-06 追加，主理人令）

六维评估加强复核（30 条随机入藏 claim 逐条五维+门禁评判）**抓出 claim_id 碰撞严重 bug**：
- **碰撞根因**：writer 的 next_claim_seq 未自增——同卷所有文章共用同一 claim_id（13 个碰撞 claim 各挂 6-663 篇无关 evidence，全部 1,491 篇受影响）
- **修复**：删 13 碰撞 claim → 按台账逐篇重建 claim+重指 claim_evidence 1,491 条（claim_id 每卷续排唯一，CL-<卷>-<5位序号>）；writer 用后自增修复
- **修复后三层**：raw_source/evidence/claim/source_chapter/claim_evidence 各 **1,498 完全一致**、碰撞残留 0
- **修复后六维重跑**：pass 6 / conditional 17 / fail 6，均分 62.4（修复前 30 fail 均分 17.0）
- **6 fail 甄别**：全部为评审 prompt 800 字截断伪影（主张关键事实如 uuencode/RFC 976/1036/vi/McKusick 均在完整 quote 5,782 字中逐字可查）——配对正确，非数据缺陷
- update_log id=516（碰撞修复登记）

**最终三层终态：raw_source 1,498 = evidence 1,498 = claim 1,498 = source_chapter 1,498 = claim_evidence 1,498 完全一致、碰撞 0、门禁 PASS。**
