# Tasks: 05 大纲落地生产执行（主代理形态）

**Feature**: `005-outline-landing-execution` | **Date**: 2026-10-24
**映射约定**：每任务尾注 `（.trae X.Y）`＝`.trae/specs/migrate-refactor2026-into-outline-20261023/tasks.md` 对应 SubTask——该件仍是勾选面唯一真身，本清单为排程与验收视角。**全程零子代理（NFR-001）；判据契约见 [contracts/three-pass-review.md](./contracts/three-pass-review.md)。**

## Phase 1: Setup

- [ ] T001 批前基线冻结：记录 `git status --porcelain` 与 HEAD 至 `script/_landing_production_20261023/baseline-20261024.md`；复跑常备四件全绿；三源行数复核（inventory 37,487／targets 4,304／outline 75/523/3,705）
- [ ] T002 建断言脚本骨架于 `script/_landing_production_20261024/`（write_guard 统一走盘、UTF-8 无 BOM／LF、文件头 docstring）——行数/守恒/SHA/幂等四类断言器各一

## Phase 2: Foundational（阻断性前置）

- [ ] T003 [P] 三趟判定输入校验器：对 `映射/review/packs/<卷>-<子批>.tsv` 校验只读性、source_id 与 mapping 子集一致、无他趟引用字段，落 `script/_landing_production_20261024/check_pack.py`
- [ ] T004 [P] 合并器＋守恒断言＋checkpoint 写入器 `script/_landing_production_20261024/merge_three_pass.py`（实现 contracts §3 硬判据 1–5，含禁硬塞降级）。**DR-F4 前置断言**：目录解析须处理汉字数字卷头且解析节数==3,705；DISPUTED 须带 subtype（adjacent／empty-vs-value／generic）
- [ ] T005 [P] 幂等二跑校验器 `script/_landing_production_20261024/assert_idempotent.py`（对指定生成器二跑取 diff，断言 ==0）
- [ ] T006 2.1b 改名执行器 `script/_landing_production_20261024/rename_mech.py`（dry-run 默认；`normcase` 判同＋两段式 rename；逐件 SHA 前后断言；写 `映射/title-standardization.tsv` 六列）。**派生规则（DR-F1）**：新名＝保留现名 `编号-` 前缀＋标准化 H1 题面段——不得以 H1 空格形态替换连字符约定
- [ ] T007 [P] 2.4a 台账重建器 `script/_landing_production_20261024/rebuild_24a_ledger.py`（git blob `c90a3c62b`→`d6853f29c` 题面差异→补录行，change_type=outline_title_fullwidth；**DR 实测 168 行**）

## Phase 3: User Story 1 — Task 2 收尾（M1）

- [ ] T010 [US1] 2.1b dry-run：跑 T006 出改名清单，核对预期 6,291 件反引号（ADR-0015 口径），偏差即停（.trae 2.1b）
- [ ] T011 [US1] 2.1b 执行＋L0–L5：L3 逐件 SHA 相等回读；L4 二跑零增量＋`git checkout` 还原哈希复原演练；台账落 `映射/title-standardization.tsv`
- [ ] T012 [US1] 2.4a 补录并入台账（T007 输出）；旧树复扫六类==0；spec 2.4a 勾选收口（.trae 2.4a）
- [ ] T013 [US1] [P] 2.1c 语义建议表：21,031 条分片（200–500/片）主代理逐片出 `映射/title-review.tsv`，断点可续；执行改名数==0（.trae 2.1c）
- [ ] T014 [US1] [P] 2.1d 路径复测：四类扫描（>260／保留名／尾点尾空格／大小写冲突）写 `映射/path-overlong.tsv`；未裁决项标“不得迁移”（.trae 2.1d）
- [ ] T015 [US1] 2.1a 派生件再生：旧树 `sync_outline_mirror.py --write` 三件→`audit_keyword_index.py`／`audit_mirror_ingest.py` PASS→`映射/README.md` 冻结声明（.trae 2.1a）
- [ ] T016 [US1] M1 收口：quickstart M1 断言族全过；.trae 2.1a–d 勾选同步；里程碑提交（大文件带 `APPROVED-BIGFILE:`）

## Phase 4: User Story 2 — Task 4 映射设施（M2）

- [ ] T020 [US2] 生成 `映射/mapping.tsv`：37,484×16 全 PENDING、`S-%06d` 稳定 ID、SHA 分组（重复组预期 0，非 0 则代表件＋DUPLICATE）；三断言＋二跑零增量（.trae 4.1）。**DR-F3 规范序**：S-ID 按 relpath **数值感知自然序**分配（`001.2`＜`001.10`；10-23 sim 字典序作废）；在盘后再生只复用禁重排，须以第二独立实现复核 37,484 行全同
- [ ] T021 [US2] [P] 生成 `映射/target-catalog.md`：4,303 行，三元组与 `targets.tsv` 逐项相等（.trae 4.3）
- [ ] T022 [US2] [P] 生成 `映射/review/packs/<旧卷>.tsv` 24 件（源文摘要／旧路径／特殊结构标记）（.trae 4.3）
- [ ] T023 [US2] `mapping.duckdb` 只读派生器 `script/_landing_production_20261024/build_mapping_stats.py`：覆盖率/状态分布/目标节分布/重复统计；与 TSV 直数一致断言（.trae 4.4–4.6）
- [ ] T024 [US2] M2 收口：`_longline_status.py --check` 18 线一致且 landing05 切逐状态计数；里程碑提交（`APPROVED-BIGFILE:`）（.trae 4.5）

## Phase 5: User Story 3 — Task 5 主代理三判（M3–M4）

每波固定四步（contracts §1–§3）：三趟串行判定（A 题面语义／B 主题词／C 结构编号）→合并器→守恒断言＋checkpoint→分歧率打印。子批 ≤1,000 条。

- [ ] T030 [US3] 先导子批：W1 首两子批（约 300–500 条）三趟+合并；实测分歧率落 `01-项目管理/01-编纂规划与报告归档/05-大纲落地生产执行计划-20261024.md` 附录台账；>50% 或 C 趟系统性偏离即停盘复盘（research D4）。**DR 基线**：12 件干执行先导分歧率 58.3%（6/7 分歧为 adjacent 型）；复盘材料已备（邻近节互斥规则＋题面空趟以内容趟为锚两草案）
- [ ] T031 [US3] W1＝旧卷 01–04（约 5,334 条，按卷 4 子批）三判全量
- [ ] T032 [US3] W2＝旧卷 05–08（05 卷 9,454 拆 10 子批）
- [ ] T033 [US3] W3＝旧卷 09–12（09 卷 4,072 拆 5 子批）
- [ ] T034 [US3] W4＝旧卷 13–16
- [ ] T035 [US3] W5＝旧卷 17–20（20 卷 5,596 拆 6 子批）
- [ ] T036 [US3] W6＝旧卷 21–24
- [ ] T037 [US3] M4 全量断言：`PENDING==0`、八状态和==37,484、CONFIRMED 三路俱全、DISPUTED↔disputes.tsv 双向相等（.trae 5.0–5.7）

## Phase 6: User Story 4 — 复核与签收（M5）

- [ ] T040 [US4] 卷级复核轮（随每波收口执行，第四视角：守恒重算＋≥30 条 CONFIRMED 回放＋DISPUTED 全量归类＋checkpoint 对账）；结论按卷写 `01-项目管理/02-工程决策与技术债/任务复核台账.md`
- [ ] T041 [US4] 全批全量复核轮：跨卷一致性＋状态终态＋禁硬塞全抽（复核台账新轮次）
- [ ] T042 [US4] 整改复验轮：任一轮 FAIL 的整改后重跑；若全程零 FAIL，以加密度抽样复验轮补足 ≥3 轮
- [ ] T043 [US4] ykla 签收：收口行呈 ykla 本人签收（不得代签）；`任务审计台账.md` 回填收口证据；changelog 记终态（.trae 12.4 接口）

## Phase 7: Polish & Cross-Cutting

- [ ] T050 .trae spec 勾选面终局同步（Task 2／4／5 全勾）＋长线登记表 `landing05` 终态刷新＋`_longline_status.py --write-block`
- [ ] T051 清理 `script/_landing_production_20261024/` 一次性中间产物（断言器与执行器留存至战役收口）；收口报告（新旧计数对照／状态分布／分歧率／提交清单）

## Dependencies

```text
T001→T002→(T003,T004,T005,T006,T007) → T010→T011→T012→(T013∥T014)→T015→T016
→ T020→(T021∥T022)→T023→T024 → T030→T031→T032→T033→T034→T035→T036→T037
→ T041→T042→T043 → T050→T051；T040 随 T031–T036 各波收口插入
```

## Parallel Execution Examples

- T013（建议表分片）∥ T014（路径复测）——不同输出文件、无共享写面
- T021（catalog）∥ T022（packs）——同源 targets.tsv 只读
- 波内多子批的 A 趟可连续批量执行后统一转 B 趟（串行约束在三趟之间，不在子批之间）；但**同子批内 A→B→C 严格顺序**

## Implementation Strategy (MVP First)

**MVP＝Phase 3（US1，Task 2 收尾）**：解锁关键路径、独立可验（M1 断言族）、一至两个会话可完成。随后 M2 一次生成批；M3 先导子批为**停盘决策点**（ykla 可据实测分歧率裁定续跑或修指引）；M4 六波为长尾主体按波续航；M5 贯穿收口。每批通用纪律：批前 porcelain 基线→施工→断言→门禁五命令→L3/L4 留证→checkpoint→里程碑提交。
