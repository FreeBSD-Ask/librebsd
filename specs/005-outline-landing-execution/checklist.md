# Checklist: 05 大纲落地生产执行（验收检查点）

**语义**：验收检查点——每项可由“通过／不通过”二值判定；生成时一律 `[ ]`，勾选权归复核人。追溯括注（来源：spec FR-x／Task N＝specs/005 tasks.md 任务号）。史料类判据含证据锚点（路径＋行数＋哈希／主键）。

## 层一：实现完整性

- [ ] Check 1: `映射/title-standardization.tsv` 在盘且行数==（2.1b 改名数＋2.4a 补录数＋1 表头）；非补录行逐行 `sha256_before==sha256_after`（来源：FR-001／T011–T012）
- [ ] Check 2: 2.1b 后旧树复扫六类机械违规计数全 0，扫描输出（含反引号文件名计数 0）留档 `script/_landing_production_20261024/`（来源：FR-001／T012）
- [ ] Check 3: `映射/title-review.tsv` 行数==21,032（表头＋21,031），且 2.1c 期间 `git log` 无任何因语义建议产生的改名提交（来源：FR-002／T013）
- [ ] Check 4: `映射/path-overlong.tsv` 与四类复测输出一致；>260 未裁决行对应文件未出现在任何迁移面（来源：FR-003／T014）
- [ ] Check 5: 旧树派生三件再生后 `audit_keyword_index.py` 与 `audit_mirror_ingest.py` 输出各含 PASS；`映射/README.md` 含冻结声明段（来源：FR-004／T015）
- [ ] Check 6: `映射/mapping.tsv` 数据行==37,484、表头 16 列、初始全 PENDING、`source_id` 唯一且形如 `S-%06d`（来源：FR-005／T020）
- [ ] Check 7: `映射/target-catalog.md` 三元组（75/523/3,705）与 `映射/targets.tsv` 逐项相等；`映射/review/packs/` 恰 24 件（来源：FR-006／T021–T022）
- [ ] Check 8: 任一已完成子批的 `judgments/<卷>-<子批>-{A,B,C}.tsv` 三件在盘：source_id 集合相等、strategy 列分别恒 A/B/C、文件内 grep 不到他趟标识（来源：FR-008／contracts §2）
- [ ] Check 9: 合并输出后全表八状态计数之和==37,484（以 `mapping.duckdb` 或直数重算，不引用合并器缓存）（来源：FR-009／T037）
- [ ] Check 10: 全部 `DISPUTED` 行与 `映射/disputes.tsv` 行双向一一对应（两向计数相等且抽样 source_id 匹配）（来源：FR-009）
- [ ] Check 11: `任务复核台账.md` 存在 ≥3 轮记录（卷级／全批／复验），每轮含轮次号、覆盖面、结论；收口行含 ykla 签收标记（人工目验）（来源：FR-012／T040–T043）
- [ ] Check 12: `任务审计台账.md` 本战役行回填收口证据路径；changelog 存在终态行（id 可定位）（来源：FR-012／T043）

## 层二：需求覆盖（FR/NFR 逐条）

- [ ] Check 13: FR-001——2.1b 六类清零＋SHA 相等＋台账含补录：Check 1/2 通过即满足
- [ ] Check 14: FR-002——建议表全覆盖且执行改名数==0：Check 3 通过即满足
- [ ] Check 15: FR-003/FR-004——路径复测入账与派生件冻结：Check 4/5 通过即满足
- [ ] Check 16: FR-005/FR-006/FR-007——台账精确生成、catalog/packs 齐、派生统计与 TSV 直数一致：Check 6/7＋`mapping.duckdb` 分布对照 mapping.tsv 直数相等（来源：T023）
- [ ] Check 17: FR-008/FR-009——三趟密封串行＋合并硬判据＋checkpoint：Check 8/9＋每子批 checkpoint JSON 在 `script/_landing_production_20261023/checkpoints/t5-*.json`（来源：T030–T036）
- [ ] Check 18: FR-010——先导子批分歧率实测值已写入执行计划附录台账；若 >50%，存在停盘与复盘记录（来源：T030）
- [ ] Check 19: FR-011——随机抽 30 条 CONFIRMED 回放：源文题面/主题词与目标节题面存在交集的违例数==0；全部 UNMAPPED 行 note 非空（来源：T040/T041）
- [ ] Check 20: FR-013——任选两个生成器各做二跑，diff==0；任选一个已中断子批从 checkpoint 续跑，已 CONFIRMED 行零变更（来源：T005/T037）
- [ ] Check 21: FR-014——每批收口五命令（audit_outline_landing --check/--selftest／task_lifecycle／gate_registry／sidecar_backup）输出留档且全 PASS（来源：T016/T024/T037）
- [ ] Check 22: FR-015——里程碑提交清单可查（B5 一次＋每卷各一次），>5 MB 件提交说明含 `APPROVED-BIGFILE:`（`git log --format=%B` 抽验）（来源：T024）
- [ ] Check 23: NFR-001——本战役全部批次日志与会话记录中无子代理（Agent 工具）派发痕迹（来源：spec NFR-001）
- [ ] Check 24: NFR-002/NFR-003——每批 `git status --porcelain` 面仅落 `映射/`／`script/`／台账文书路径；2.1b 之外旧树文件 SHA 零变更（抽查 200 件）（来源：spec NFR-002/003）

## 层三：边界与异常

- [ ] Check 25: 三趟中任一趟输出缺行（source_id 集合不等）时合并器拒绝合并并停批——以人工删除一行 A 输出做坏件注入验证，stdout 可见且零写入（来源：contracts §3.1／L5）
- [ ] Check 26: 拟 CONFIRMED 行目标节题面与源文无交集时被降级 DISPUTED（reason=hard-stuff-suspect）——以构造样本注入验证（来源：FR-011／contracts §3.3）
- [ ] Check 27: mapping.tsv 出现越界 status 值时断言器立即非零退出（坏值注入验证）（来源：data-model 状态机）
- [ ] Check 28: 同 SHA 重复组（若出现）恰 1 代表件、余者 DUPLICATE 且 note 记代表件 source_id（来源：FR-005）
- [ ] Check 29: checkpoint 续跑遇输入哈希变化（输入被动过）时拒绝续跑并报告，不静默重判（来源：FR-013／data-model 实体七）
- [ ] Check 30: 先导子批分歧率落在 40%±10（沙箱预期带）时有相邻节分化记录；复核指引含“区分同章相邻节”条目（来源：research D4／.trae 5.7）
- [ ] Check 31: 大文件（mapping.tsv≈20.9 MB、title-review.tsv）提交说明放行标记抽验通过；无 >5 MB 件未带标记入库（来源：FR-015）

## 层四：既有功能未回归

- [ ] Check 32: `sync_refactor2026_baseline.py --check` 零漂移（75 卷 523 章 3,705 节口径不动）（来源：US5）
- [ ] Check 33: `_longline_status.py --check` 18 条线一致；landing05 进度串在 M2 后为逐状态计数、M4 后 PENDING==0（来源：FR-014／T024/T037）
- [ ] Check 34: `05-卷册大纲/目录/index.html` 与 `data/outline.txt` 全程零改动（`git log -- <两路径>` 无本战役提交）（来源：写入边界）
- [ ] Check 35: 旧树内容字节保真：除 `映射/title-standardization.tsv` 在册改名件外，随机 200 件 SHA 与 `映射/inventory.tsv` 记载一致（来源：NFR-003）
- [ ] Check 36: 常备四件＋收口五命令在 M1/M2/M4/M5 四个时点输出全 PASS（留档）（来源：US5）
- [ ] Check 37: `.trae` spec 勾选面终态与本战役生产状态一致（Task 2/4/5 全勾且无跳勾）（来源：防双账边界／T050）
- [ ] Check 38: S-ID 分配可复现——第二独立实现按规范序（relpath 数值感知自然序）重derive，37,484 行 source_id↔relpath 与在盘 mapping.tsv 全同；mapping.tsv 在盘后任何再生对既有行零改写（来源：FR-005／DR-F3／T020）
- [ ] Check 39: 合并器目录解析起手断言“解析节数==3,705”在汉字数字卷头（第一～第七十五卷）下成立；人为注入阿拉伯数字卷头夹具时断言失败可见（来源：FR-008／DR-F4／contracts §3）
- [ ] Check 40: disputes.tsv 含 subtype 列且生产先导批的 adjacent 型占比有落账；DISPUTED 三型（adjacent／empty-vs-value／generic）计数和==DISPUTED 总数（来源：FR-009／DR-F5）
