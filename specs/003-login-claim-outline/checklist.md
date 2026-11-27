# Checklist: login 数据库全量逐条判定入 claim 库与 05-大纲

**Feature**: [spec.md](spec.md) | **Tasks**: [tasks.md](tasks.md) | **Created**: 2026-10-06

验收检查点：每项可由“通过／不通过”二值判定；不勾选（勾选权归复核人）。

## 一、实现完整性

- [ ] Check 1: 判定台账 `script/_login_claim_ledger_20261006.jsonl` 覆盖 6,604/6,604 行且 article_id 全唯一（来源：spec FR-001／Task T012）
- [ ] Check 2: 台账每行 verdict ∈ {claim_ingest, no_ingest} 且 reasons 数组非空、可回溯到 R1-R12/P 编号或七类不写判据（来源：spec FR-002／Task T007/T013）
- [ ] Check 3: 判定引擎/写者/大纲写者三脚本 `script/_login_claim_*_20261006.py` 全部 py_compile 通过且有断点续传逻辑（幂等键＝article_id）（来源：Task T003/T004/T005、FR-010）
- [ ] Check 4: 入藏写者事务批 200 行＋批前/批后行数断言＋隔离文件 `script/_login_claim_quarantine_20261006.jsonl` 机制存在（来源：Task T004、contracts/claim-ingest-contract.md）
- [ ] Check 5: 大纲写者 import WO-007（`00-编纂规则与格式规范/01-规则/脚本与命令/wo007_idempotency.py` 的 has_block/write_guard）且有写后门禁调用（来源：Task T005/T009、FR-005）
- [ ] Check 6: 试点批（T010）记录在案：≥1 篇广告＋≥1 篇目录噪声全链跑通并人工检视记录（来源：Task T010）
- [ ] Check 7: 本战役批量写入在 historical_claims.duckdb.update_log 有登记行（含批次/规模/备份指针）（来源：spec FR-009／Task T019）

## 二、需求覆盖

- [ ] Check 8: 广告条目逐条判定覆盖——台账中 kind='ad' 行数＝articles 表 kind='ad' 行数，每行有终态与理由（来源：spec FR-001、User Story 1 场景 2）
- [ ] Check 9: 目录噪声/刊头条目同等待遇——kind ∈ {toc,frontmatter} 全部有台账行（来源：spec FR-001）
- [ ] Check 10: 判定 claim_ingest 者三层齐备——raw_source（SRC-login:<id> 唯一＋content_hash）＋evidence（≥1）＋claim（claim_id 全库唯一）比例 100%（来源：spec FR-003、SC-002）
- [ ] Check 11: evidence.quote 与 login 库 body_text 逐字一致（抽检 ≥100 条零改写，原件笔误照录）（来源：spec FR-003、证据锚点可定位＋原文照录未改写判据）
- [ ] Check 12: claim 措辞门禁——L1 级证据的 claim_text 无"继承/影响/源自/借鉴"表述（抽检记录）（来源：spec FR-003、Task T018）
- [ ] Check 13: claim_type ∈ 十值枚举且 evidence_level ∈ L1-L5，无混用（source_layer 与 evidence_level 双轨方向正确）（来源：06 号 schema §2.4、Task T008）
- [ ] Check 14: 存疑主张以 UNVERIFIED/contested 合法入库且留反证处置记录，无默认确证（来源：spec FR-004）
- [ ] Check 15: 入 claim 者全部有 source_chapter 挂钩（行数 ≥ 台账 claim_ingest 行数；link_type ∈ used/mentioned/background）（来源：spec FR-005、SC-003）
- [ ] Check 16: 05-卷册大纲宿主章文件含 ROW_MINE 注入块且 WO-007 幂等验证通过（同条目二次写入零重复块）（来源：spec FR-005、Task T022）
- [ ] Check 17: 证据等级门禁 `audit_evidence_level_labels.py` 对写回块全绿（exit 0），块头等级与 claim 库 evidence_level 一致（来源：spec FR-005、Task T021）
- [ ] Check 18: 新建章文件（若触发）三步落位齐备：卷 00-总览.md 登记＋章文件夹/index.md＋SUMMARY.md 同步，子节五字段且史观映射 ≥5 条总纲；触发数量与理由留档（来源：spec FR-006／Task T024-T026；未触发则留档说明"零触发"）
- [ ] Check 19: 判定终态回写 login 库（若有）为差量 UPDATE 有痕（update_log/provenance 登记），零静默改写（来源：Task T014、FR-009）

## 三、边界与异常

- [ ] Check 20: 判定冲突并存入库验证：存在 claim_relation contradicts 边或 UNVERIFIED/contested 行（多版本并置，不择一淘汰）（来源：spec Edge Cases、FR-004）
- [ ] Check 21: 断点续传验证：中断重跑后台账行数无漂移、claim 库无重复行（幂等键回放记录）（来源：spec FR-010、SC-007）
- [ ] Check 22: 引擎/API 失败清单隔离在案（隔离文件/失败日志），失败项重派后清零（来源：spec Edge Cases、Task T012/T016）
- [ ] Check 23: chapter_target 有效性——台账 claim_ingest 行的 vol/ch 全部命中既有 54 卷 454 章口径或本战役新建章（无悬空章引用）（来源：contracts/ledger-contract.md）
- [ ] Check 24: 大纲归类边界——可属多章/多期者有 source_chapter 多值行与 claim_period 多值（六期交叠）（来源：spec Edge Cases）

## 四、既有功能未回归

- [ ] Check 25: 重构2026 目录零变更——文件清单＋SHA-256 与战役前基线（`script/_login_claim_baseline_20261006.json`）比对零差异（来源：spec FR-007、SC-005）
- [ ] Check 26: login-zazhi.duckdb 行数守恒——articles/issues/chunks/figures 与战役前基线一致（判定回写仅差量 UPDATE 有痕，零删行）（来源：spec FR-009、Task T002/T014）
- [ ] Check 27: claim 库行数守恒——claim/raw_source/evidence/source_chapter = 战役前基线 + 本战役纯增量（零既有行 UPDATE/DELETE）（来源：spec FR-009、Task T019）
- [ ] Check 28: 零二进制入库——historical_claims.duckdb 与 login-zazhi.duckdb 无 BLOB/VARBINARY 列变更（来源：spec FR-009、SC-006）
- [ ] Check 29: 既有大纲正文零改写——05-卷册大纲 宿主章文件 diff 仅含新增注入块（无既有叙述改动；新建章文件除外且按 Check 18 验证）（来源：contracts/outline-inject-contract.md 边界）
- [ ] Check 30: 执行架构合规——**滚动 40 路子代理（缺 1 补 1）**派发记录在案（分片清单＋派发/重派日志，全程无空转、失败子代理重派），判定/入藏的 LLM 调用经引擎旧线路客户端（key 轮替；共享日志 `_glm_line_20261006.log` 中 key 脱敏）（来源：spec FR-008、主理人 2026-10-06 新增要求）
- [ ] Check 31: 禁止抽查口径验证——判定台账 6,604/6,604 全量（无任何形式抽样/降采样），综合分析内容逐条在案（来源：spec FR-001、主理人 2026-10-06 新增要求）
- [ ] Check 32: 全量二次复核完成——台账全部判定行有第二遍独立复核（与首判独立提示词），两遍不一致行进入第三遍仲裁并有终态（来源：Task T013、三次复查流程）

## 追溯缺口说明

- spec 每条 FR（001-010）与 tasks 每条任务（T001-T029）均有对应检查点：FR-001→Check 1/8/9；FR-002→Check 2；FR-003→Check 10/11/12/13；FR-004→Check 14/20；FR-005→Check 15/16/17；FR-006→Check 18；FR-007→Check 25；FR-008→Check 30；FR-009→Check 7/26/27/28；FR-010→Check 21。无未覆盖缺口。
