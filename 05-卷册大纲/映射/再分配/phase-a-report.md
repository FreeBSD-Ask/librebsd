# 阶段 A 报告：全量重审、主题聚合与新节点提案

生成器：`再分配/pipeline/p02_recheck.py`／`p03_aggregate.py`／`p04_registry.py`；方法与阈值见 `再分配/method.md`。阶段 A 只读旧树与既有判定，未创建任何节点、未改 `targets.tsv`／`outline.txt`／`index.html`／目录树。

本版为 RV-20261026-003 判 FAIL 后、按 ykla 2026-10-26 三项裁定的整改版：V-076 严格 1,301 行（撤销清单外 991 行）、D5-05／D5-08 零证据不接行、V-018 402 行按配额与主题拆分；同时撤销“虚拟目标优先复用”（F-1）、域约束全量清零（F-4）。

## 1. 输入与守恒

- 输入 `mapping.tsv` 37,484 行；`targets.tsv` 4,303 节点（75／523／3,705）。
- 六波行数：W01 5334；W02 14075；W03 7216；W04 3303；W05 7265；W06 291；合计 37484（＝37,484）。
- 阶段 A 处置守恒：37484；最终处置守恒：37484（逐行见 `reassign-final.tsv`）。
- `final_disposition` 取值全部落在规格 9 值枚举内：APPROVED_NEW_SECTION 1530、APPROVED_NEW_SUBSEC 2512、EXISTING_SECTION 814、THEMATIC_AGGREGATION 10339、UNMAPPED_KEEP 22289；`REVIEW` 仅作 `stage3_disposition` 中间态，最终表 0 行。

## 2. 六波处置分布

| 波 | 旧卷 | EXISTING_SECTION | REVIEW（中间态） | AGGREGATE_CANDIDATE | UNMAPPED_KEEP | DUPLICATE | 行数 |
|---|---|---|---|---|---|---|---|
| W01 | 01-04 | 138 | 307 | 4783 | 0 | 0 | 5334 |
| W02 | 05-08 | 138 | 2257 | 11662 | 0 | 0 | 14075 |
| W03 | 09-12 | 217 | 605 | 6375 | 0 | 0 | 7216 |
| W04 | 13-16 | 106 | 93 | 3104 | 0 | 0 | 3303 |
| W05 | 17-20 | 197 | 186 | 5495 | 0 | 0 | 7265 |
| W06 | 21-24 | 18 | 0 | 273 | 0 | 0 | 291 |
| 合计 | 01-24 | 814 | 3448 | 31692 | 0 | 0 | 37484 |

最终处置：APPROVED_NEW_SECTION 1530／APPROVED_NEW_SUBSEC 2512／EXISTING_SECTION 814／THEMATIC_AGGREGATION 10339／UNMAPPED_KEEP 22289（合计 37484）。中间态 `REVIEW` 全部按复核口径改判：低分带/候选冲突最高分 ≥0.18 且共词 ≥2 者落 `EXISTING_SECTION`，否则并入所属聚合簇，按簇归属落 `APPROVED_NEW_SUBSEC`／`THEMATIC_AGGREGATION`／`UNMAPPED_KEEP`。

## 3. 去重

- SHA-256 组 37,484 组各 1 行，同组重复 0 行，`DUPLICATE` 0 行（代表件规则已实现，本批无命中）。
- 近重复题面 829 组（同规范化题面、SHA 不同）：734 组题面显著；组内有 ≥MED 高置信落点者整组归该锚点（记 `near_dup_anchor`），无锚点者转主题聚合（`near_dup_no_anchor`），均不判 `DUPLICATE`；其余样板／污染题面或 >17 行组随行判定，见 `dedupe-near-groups.tsv`。
- `source_id` 重复：0。

## 4. 聚合、小节与高层级提案

- 聚合候选簇 5109 个，覆盖 35140 行；不足 5 行、主题不成立（编纂元数据／题面污染）或无合法父节且不足 20 行者 `UNMAPPED_KEEP`。
- 小节登记册 51 条（默认批准；父节均为 `targets.tsv` 的 sec 节点，且均满足“≥2 个专属词共词 + 强度守卫”；表示法为节目录下 `_bucket-*` 映射桶，不构成第四级页面）。
- 高层级提案 134 条：节 134／章 0／卷 0；无合法宿主的节簇退 `UNMAPPED_KEEP`（0 行）。全部待 Task 6 一次批准。
- 提案规模说明：按复核门槛（父节 ≥2 专属词＋强度守卫）与 RV-006 语言词退回后，节提案 134 条（较上一版 131 增 3 条：来源为旧章 321／325／311 的同题簇，**非语言退回行回流**；RV-20261026-007 更正），每条 ≥20 行、均有宿主章与证据行；须逐条批准或驳回，未批准一律不建。
- 节点去重：复用现有节点 0 条；新节点 134 个（`S-003706` 起连续，未与 `targets.tsv` 冲突）；登记册／提案包内同层同父同题重复 0 条。
- 提案题名取自旧节目录名，去编号后规范化、不截断；`formal_title_candidate` 列给出把连字符拆散的数字并回小数形式的正式题名候选（如 `4 0 Jails` → `4.0 Jails`），批准时仍须逐条确认，不得以工作题名直接落库。
- 未提出章／卷级提案：簇锚在旧节、只做同章内合并，本批未出现跨多旧章的同主题簇，也无“宿主章缺位”的 ≥20 行簇，故无新章／新卷证据。

## 4.1 已批准虚拟目标（严格按批准范围，不再重复提案）

- V-076：五章 36 节（`V076-<ch>.<sec>`）。**只认** `17-v076-source-inventory.tsv` 的 1,301 个`source_id`（以题面前缀 `章.节.序号` 逐行对齐 `mapping.tsv`，逐节行数与 `19` 号 plan B 相等）；实得 1301 行。清单外 991 行（246 待裁／38 法律票／707 计划外同章）已全部撤销，改走既有节／聚合／留旧树，其中法律票按 D1 归 V-063 现有节或留旧树，不入 V-076。
- D5 九节（`D5-01…D5-09`）：V66 三节（韩国 5／俄罗斯 6→V-066 C2，加拿大 3＋矩阵 1→V-066 C1）；微机 OS 谱系 7／time_t 6／US v Microsoft 5／学生组织 5（`06` 号件族标记）；证据行合计 38 行。`D5-05`（kqueue）与 `D5-08`（Hotmail）为**已批准但零证据**节：本批 0 行，不接任何行（原复用误挂的 29／9 行已撤销，回到既有目标／聚合／留旧树）；结构批是否建空节另由零证据规则裁决。
- 语言章 22 节（`L-<vol>-<sec>`，V-008／V-018／V-037／V-041／V-045／V-058）：`23` 号件证据行＋`26` 号件题命中行＋旧 017 章关键词规则，共 191 行。
V-018 的 402 题命中行按 RV-004／RV-006 三段拆分：**归 V-076 254 行**（与 1,301 重叠，占清单配额）／**归 V-018 语言节 71 行**（题面含严格语言名，逐行 `reason` 记该词）／**无行级语言证据 77 行**（`no_row_lang_evidence`，其中 2 行原在语言段、因题面与正文均无任何语言名而移出；其余 75 行为治理／流程行）。254＋71＋77＝402，自洽。
- 语言词口径（RV-006）：只认 Fortran／ALGOL／COBOL／Lisp／Smalltalk／Prolog／Pascal／Modula／C／C++／Perl／Python／Ruby／Tcl／Java／JVM／Swift／Objective-C／Haskell／Erlang／Rust 与“编程语言／脚本语言／语言生态”；节题主题词（如“主义”）、父章词、泛词一律不作证据。494 行中仅 191 行具备行级证据（题面，非 V-018 卷必要时读正文），其余 303 行按 `no_row_lang_evidence` 退回。
- 语言章无治理行：落 `L-V*` 的 191 行逐行 `reason` 均为 `virtual_approved:lang=<严格语言词>`，全部可在该行题面或正文核到；不再出现节题主题词充作行级证据。
- 23 号件证据（480 行，唯一清单）对账：**149 行落语言节**（V-018 语言段 71＋其余五卷 78，后者含 8 行以正文补证）／254 行由 V-076 清单配额占用（裁定 1）／**77 行**无行级语言证据退回（`no_row_lang_evidence`）。480＝149＋254＋77。
- 旧 017 章（语言生态）343 行：仅 **42 行**题面含严格语言词并保留于 `L-V8-*`；其余 301 行题面仅样板串或泛词，按 RV-006 裁定 3 退回（125 留旧树／175 入聚合／1 落既有节，逐行 `reason` 可核）。V-018 退回的 77 行则为 2 留旧树／75 入聚合。
- **框架节待补**：语言章 22 节中 4 节为零行框架节（`L-V18-1`／`L-V45-1`／`L-V58-2`／`L-V58-3`），本批不接行、不生成正文，批准流程须按“零证据规则”决定是否建空节或从批准面移除。
- 合计 `VIRTUAL_TARGET` 1530 行，全部为 `APPROVED_NEW_SECTION`；**已撤销**上一版的“虚拟目标优先复用”机制（1,035 行、其中 611 行零专属词），不再以题面近似把任意行塞入虚拟节。
- 域约束：允许新卷＝该旧卷当前 target 前 3 新卷 ∪ 该旧卷行所用虚拟目标所属卷；越界行一律改判（`domain_out_of_scope` 341 行），终态越界 0（含 `near_dup_anchor` 与 `chapter_pending` 落点亦逐行校核）。
- C-0099（V18 治理章）提案 67 条，均为治理／流程／共同体题；内核技术题（关键词命中而无已批宿主）留旧树待裁，C-0047（C 语言章）提案 0 条。

## 5. 逐行 reason 与待复核

- `reason` 覆盖 37,484 行（空值 0），取值为组合码“行因→簇因”，行因含 `virtual_approved`／`existing_confirm`／`existing_new`／`reassign_stronger`／`conflict_resolved`／`near_dup_anchor`／`near_dup_no_anchor`／`zero_overlap`／`weak_overlap`／`generic_only`／`weak_band`／`meta_layer`／`chapter_pending`／`chapter_pending_domain`／`domain_out_of_scope`／`sha_duplicate`，簇因含 `cluster_parent_ge2`／`cluster_ge20_no_parent`／`cluster_lt5`／`no_legal_parent`／`title_polluted`／`meta_layer`／`c0099_technical_no_host`。
- `UNMAPPED_KEEP` 22289 行全部有 reason 且可回溯到聚合簇号（`cluster_id`）或行级原因；`resolution_ref` 指向登记册 `B-*`／提案 `P-*`。
- `EXISTING_SECTION` 814 行：复核口径（含域约束与专属词门禁）下，均满足“题面与目标节链共词 ≥2、含 ≥1 个题面专属词（语料 df<100）、分 ≥0.18、且目标卷在允许集”；零交集行 0。
- 两条章级待复核：`S-002796` 无覆盖节，入聚合后因不足 5 行留旧树；`S-002339` 的裁定落点`S-000465`（V-014）越出其旧卷允许集，按“域约束优先”改入聚合并留旧树（`chapter_pending_domain`）。
- Hotmail 四行（RV-004 F-2）：`S-027252`（PENDING，原 `V71-3.3`）已**原位恢复**至 `S-003401`（`restore_original_target`，该新卷在其旧卷前 3 允许集内）；`S-011836`／`S-011838`（DISPUTED，原 `V71-3.3`）与 `S-012752`（DISPUTED，原 `V69-8.8`）原目标所属新卷不在旧卷 5 允许集内，按域约束不得原位恢复，reason 记 `original_target_out_of_domain`，终态 2 留旧树／1 入聚合。
- `S-000599`（内核治理）集中落点由复核时的 1,630 行降至 24 行（复核上限 72），且每行均有专属词共词证据（`linus`／`maintainer`／`tab` 等）；仅命中 `linux`／`内核`／`治理` 等泛词者记 `generic_only` 并移入聚合。
- `proposed_target` 非 sec 节点或非空异常：0 行（合法集＝`targets.tsv` sec 节点 ∪ 已批准虚拟节 ∪ 空）。

## 6. 只读面与越界声明

- 本批未写 `mapping.tsv`／`targets.tsv`／`outline.txt`；SHA-256：mapping `f229ebafb8de52dd`／targets `32953902672b0b67`／outline `b21eaddfeafb91ae`（与 `checkpoints/wave-*.json` 记录一致）。
- `git status` 对旧树与三件输入： M 05-卷册大纲/映射/mapping.tsv； M 旧大纲-20261023/SUMMARY.md。其中 `mapping.tsv` 的 M 标记源于 Task 2 数据前置落账（`p01_apply_prereq.py`），`旧大纲-20261023/SUMMARY.md` 为上一批遗留改动；两者均非本批写入。
- 写入范围仅 `05-卷册大纲/映射/再分配/`（含 `pipeline/`、`checkpoints/`）与 `script/_reassign_20261026/`（Task 1／2 基线与前置脚本，`/script` 由 `.gitignore` 覆盖）；未建节点、未撰写正文、未删除旧树、未做旁路备份副本。

## 7. 二跑与 checkpoint

- 每波 checkpoint：`再分配/checkpoints/wave-1..6.json`（批次号、卷号、行数、`source_id` 区间、子批、处置分布、输入 SHA-256）。
- 同一输入二跑：六波表、汇总、聚合、登记册、提案包、最终表逐字节一致（SHA-256 比对通过）。
- 产物 26 件 UTF-8 无 BOM、LF、无直角引号。
