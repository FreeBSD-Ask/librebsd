# H 线核心驱动清单（mail2d）

本目录 7 件 `mail2d_*.py` 副本为版本化参考件；`script/_db_row_mining/` 原件在在途批次收口前继续作为运行件；路径切换另批执行（`ADR-0006` §1.2；验收判据见 `H1-H4-全链路规格.md` FR-H14）。副本按 SHA-256 **逐字节复制**，不改一个字节（含 BOM 与换行形态），`script/` 原件零改动（**一处有意识偏离**：`mail2d_build_read_ledger.py` 增 `--append`／`--selftest`；`mail2d_run_batch.py` 的“加文件头注释”偏离已随 2026-10-22 阶段二刷新废止——副本现为原件逐字节复制）。

## 运行状态（2026-10-22 声明）

本目录 7 件 `mail2d_*.py` 为**版本化参考件**，依赖（如 `_git_lsfiles.py`）未随件复制，**不得直接运行**；运行一律用 `script/_db_row_mining/` 原件。`--help` 行为**不代表原件行为**——烟测实测：`mail2d_run_batch.py --help` 因缺 `_git_lsfiles` 依赖报 `ModuleNotFoundError: No module named '_git_lsfiles'`；`mail2d_prep_batches.py --help` 空跑并打印“完成。”后 exit 0；`mail2d_batch_dump.py --help` 报 `IndexError`。**唯一例外**：`mail2d_build_read_ledger.py --selftest` 不依赖 catalog／spec／邮件库（自建临时夹具），可直接运行；其重建与追加分支仍须 catalog，故整体仍归“不得直接运行”。逐件“可直接运行”栏见下表。

## 核心驱动（7 件）

| 源路径 | 副本 | 字节 | SHA-256 | 职能 | 运行状态 | 可直接运行 |
| ------ | ---- | ---: | ------- | ---- | -------- | ---------- |
| `script/_db_row_mining/_prep_batches.py` | `mail2d_prep_batches.py` | 4778 | `4047b37136a11fe110dd36a09a1bf7160305b12de6e6a9dc7fa6a663e0705add` | 批量预建批次：建 spec → dump → 补 `pk_range` → 容器行清单 → 拆 digest，供读手到即派（FR-H01） | 原件运行；副本未启用 | 否 |
| `script/_db_row_mining/_mail2d_run_batch.py` | `mail2d_run_batch.py` | 32422 | `d74072ca5fcf320be260f817615b0725bbf0a66c99f30ce0c3ac80a072363712` | 单批运行器（`new`／`dump`／`body`／`check`／`register`／`outline`／`bookkeep` 子命令），批内编排与入库、入纲写盘（FR-H01、FR-H07–FR-H10）；**2026-10-22 阶段二刷新（含 F1–F4 复核修复）**：`outline` 子命令改调 `脚本与命令/outline_writer.py`（ADR-0010；旧模板生成链退役；任一步非零短路返回，不再吞退出码），`load_hosts()` 兼容目录化四段路径＋工作树校验＋多义键剔除＋mount 源落盘校验（悬空键 50→0） | 原件运行；副本未启用 | 否 |
| `script/_db_row_mining/_mail2d_batch_dump.py` | `mail2d_batch_dump.py` | 5354 | `9efe78538719e0e6fa0d3b7d4a4d91fb277b21ade2e3f6111455f6bda3685a94` | 通用批 dump：全文 dump／`review_logs` digest（pk\|date\|from\|subject\|正文前 420 字）／heads 头表，只读源库（FR-H01） | 原件运行；副本未启用 | 否 |
| `script/_db_row_mining/_build_read_ledger.py` | `mail2d_build_read_ledger.py` | 25142 | `5d79c545374f99c7fc466bce7926e53c5ccf413aad56a6064e308a42848221ae` | 台账单写入口：重建 `mail2d_read_ledger.json`（`records`／`read_judged`／`read_effective`／`queued_records`，预建 spec 不计已读）＋`--append` 批内追加合并（按 key 去重、只重算涉及库、原子落盘）＋`--selftest`（FR-H11） | 原件运行；副本仅 `--selftest` 自检可跑（重建／追加须 catalog） | 仅 `--selftest` |
| `script/_db_row_mining/_merge_cand.py` | `mail2d_merge_cand.py` | 6225 | `3c70664275a7ddec7fa477871c607ebd3571f5e735ab30559cf51a038187cbf5` | 候选分件合并：字段数与等级／长度／越界／重复／禁字符校验，`--srcdb` 回库验存在性剔幽灵 pk（FR-H03、FR-H04） | 原件运行；副本未启用 | 否 |
| `script/_db_row_mining/_merge_narr.py` | `mail2d_merge_narr.py` | 3481 | `b9ff2b3e989f18cb903a10e9c2b547d7cac19b778d4407c3bc830639475a15c5` | 叙述分件合并：三列 TSV 汇总，阻断集为缺文件与 CRLF，pk 集合与候选全集对齐（FR-H05） | 原件运行；副本未启用 | 否 |
| `script/_db_row_mining/_vn_narr.py` | `mail2d_vn_narr.py` | 6714 | `9763bcfb0c697fb7b3c73cb120b369a4a53f31e0f002e6c575195efae9ce3b4f` | 叙述硬门禁：存在性与 pk 全等、3 个 TAB 字段、长度 60–140、尾标点、禁字符、宿主逐 pk 一致，违规 exit 1（FR-H06） | 原件运行；副本未启用 | 否 |

上表字节数与 SHA-256 为 2026-10-22 实测；7 件均无 BOM、无 CRLF（纯 LF）。**复制件保持逐字节一致**，两处为**有意识偏离**：① `mail2d_run_batch.py`：2026-10-22 初版副本加过文件头注释（27,001 字节／`2718e42b…`）；**阶段二刷新（含 F1–F4 修复）后副本＝原件逐字节 32,422 字节／`d74072ca…`**（注释口径已并入原件 docstring；运行件同步改动：`outline` 改调 `outline_writer.py`、退出码短路传播、`load_hosts` 四段路径＋落盘校验＋多义键剔除）；② `mail2d_build_read_ledger.py` 增 `--append`／`--selftest`（TD-013 台账单入口收敛，本目录为权威实现），原件与复制时副本同为 `b71a431dd3fcd6d5ace7ad5b55ab6b464ca22d7d1ad448f65d587f5b1a75c7bd`（6185 字节），改造后副本为 `5d79c545374f99c7fc466bce7926e53c5ccf413aad56a6064e308a42848221ae`（25142 字节）；其余 5 件副本哈希仍与原件逐字节相等。复核方式：`script/_p2_mail2d_promote.py`（复制与比对一次完成）、`Get-FileHash -Algorithm SHA256`。

## 配套件（非 `mail2d_` 前缀，2026-10-22 阶段二新增）

| 原件 | 副本 | 字节 | SHA-256 | 职能 | 运行状态 |
| ---- | ---- | ---: | ------- | ---- | -------- |
| `script/_db_row_mining/_outline_common.py` | `_outline_common.py` | 5747 | `e09bd3e5e37550dadf11423aa6d770b0658eea93348e4b0b8fe6f4567f3bf5c9` | H 线宿主键空间层：`host_index()`（递归现行四段布局、**保点键**）、`whitelist()`、`frozen_sections()`／`section_refs()`（承重参考） | 随 `_mail2d_run_batch.py` 运行件加载（禁写前置于 `outline`）；副本为逐字节参考件 |

> 阶段二后 runner 与批内脚本的键空间／冻结判据均出自本件（ADR-0010 生成链切换）；与 7 件核心驱动同纪律：**逐字节复制、运行用原件**。

## 未入库的批内一次性脚本

以下类别**不迁入本目录**，留在 `script/_db_row_mining/`（`ADR-0006` §1.2 末句“批内一次性脚本留 `script/`，不迁”）。件数为 2026-10-22 实测（该目录 `.py` 合计 9793 件）。

| 类别 | 件数 | 职能 | 留 `script/` 的理由 |
| ---- | ---: | ---- | ------------------- |
| `_register_*` | 1173 | 单批落库（claim 四表写入）的按批生成件 | 一批一件、批号与 claim 号段写死在文件名与常量内，无复用面；落库契约由 `_mail2d_run_batch.py register` 与 `claimdb_guard.py`／`register_waterlock.py` 承载 |
| `_outline_*` | 631 | 单批大纲回写与宿主块改写 | 同上，`TARGET_REL` 与块头逐批不同；入纲契约由 `outline_writer.py`（ADR-0010）与 `_mail2d_run_batch.py outline` 承载 |
| `_bookkeep_*` | 97 | 单批“三零”对账与遗留项清理 | 一次性对账，依赖当批宿主与库内行；常设对账口径在 `_mail2d_run_batch.py bookkeep` |
| `_ledger_*` | 162 | 批内台账追加（仅追加件） | **待退役旧实现**：追加统一走 `mail2d_build_read_ledger.py --append`（本目录权威实现），现存件留档备查、不再新写；台账 key 结构不迁、不改契约（`ADR-0006` §1.3） |

## 一次性写盘件退役登记（TD-016 D1／D4，2026-10-22）

对象为 `script/_db_row_mining/` 下**写入目标硬编码、无路径覆盖**的批内写盘件；样本取 H3 线 `fhk_b084` 族五件（TD-016 D1 结构性失配、D4 无路径覆盖）。判据取 `script/_pilot_20261022/drill_h/H-drill.md` §1 判定表（一）、§2.1、§4 缺陷表。**结论一律“不重建、留原件备查”**：写入能力已由 `outline_writer.py`／`mail2d_run_batch.py`／`mail2d_build_read_ledger.py` 承担，重建即复活硬编码常量缺陷。

| 脚本（字节） | 写入目标（硬编码位置） | 路径覆盖 | 落盘方式 | 是否已被通用件取代 | 结论 |
| ------------ | ---------------------- | -------- | -------- | ------------------ | ---- |
| `_outline_fhk_b084.py`（6988） | `ROOT`(L22)＋`TARGET_REL['885']`(L29–31，旧路径 `第88章-…/88.5-….md`)；另读 `MAILDB`(L23)、`HC`(L81) | 无 `--dry-run`／`--host`／`--root`，仅 `--write` | 直接 `io.open(fp,"w")`，无临时件；库外 prebak | 是：`outline_writer.py`（宿主解析＋块级幂等＋路径覆盖＋原子写）；`mail2d_run_batch.py outline` | 不重建、留原件备查；**已对现网结构性失效**——宿主已由单文件拆为 `097.5-…/` 目录（1287 件），`TARGET_REL` 指向的旧文件不存在，只读运行即“目标不存在”exit 1 |
| `_bookkeep_wave_fhk_b084.py`（9417） | `ROOT`(L29)／`RL`(L30)／`PROG`(L31)／`CLDB`(L32)／`CLAIMS`(L33) 全常量 | 无，仅 `--write` | 追加 `progress.jsonl`＋`changelog.duckdb` INSERT，无临时件 | 是：`mail2d_run_batch.py bookkeep` | 不重建、留原件备查；三零判据已入常设子命令 |
| `_merge_narr_fhk_b084.py`（5840） | `TAG`(L26)／`RL`(L25)／`CAND,OUT`(L29–30) 常量 | 无，仅 `--write` | 临时件＋`fsync`＋`os.replace`＋回读断言（本族唯一原子件） | 是：`mail2d_merge_narr.py`（通用合并）＋`mail2d_vn_narr.py`（硬门禁） | 不重建、留原件备查；其 G1–G7 判据已由 `mail2d_vn_narr.py` 与 `audit_mail2d_batch.py` B3 承接 |
| `_register_fhk_b084.py`（7723） | `HC`(L28)／`MAILDB`(L29)／`CAND`(L27)／`ANCHOR`(L30) 常量 | 无 `--host`／路径覆盖；`--apply`／默认 `--dry-run` | duckdb 单事务 `BEGIN/COMMIT`，无落盘即验 | 是：`mail2d_run_batch.py register` | 不重建、留原件备查；写库前置仍走 `claimdb_guard.py`＋`register_waterlock.py` |
| `_ledger_fhk_b084.py`（5890） | `P`(L22) 台账绝对路径＋`KEY`／`OLD`／`NEW`／`TAG_OLD`／`TAG_NEW` 常量 | 无，仅 `--write` | 直接 `io.open(P,"w")`，写前 `shutil.copyfile` 备份；字符串感知切 span 替换 | 是：`mail2d_build_read_ledger.py --append` | 不重建、留原件备查；追加契约见“写者清单” |

**共性结论**：五件均①写入目标为脚本内常量；②无路径覆盖，演练与重放只能以只读探针替代；③三件非原子写（outline／bookkeep／ledger），中途失败可残留半制品。凡新批一律不再复制此类脚本，改走上述通用件；原件不修改、不删除（`ADR-0006` §1.2）。

## 写者清单（文件 → 唯一写者，NFR-H02）

每个产物**只列一个写者**，不留“两可”；标注“待退役旧实现”者为历史件，不得再新写。

| 产物 | 唯一写者 | 模式 | 说明 |
| ---- | -------- | ---- | ---- |
| `script/_db_row_mining/mail2d_read_ledger.json`（重建） | `mail2d_build_read_ledger.py` | 无参／`--ledger` | 由现存批次 spec＋catalog 重算；`records` 为下界（spec 已删者不计），预建 spec 入 `queued_records` |
| `script/_db_row_mining/mail2d_read_ledger.json`（追加） | `mail2d_build_read_ledger.py --append <JSONL>` | 追加合并 | 按 key 去重（同 lib＋tag 已被覆盖即跳过）；只重算追加件点名的库，其余条目逐字不动；同目录临时件→`fsync`→`os.replace`；`note` 只追加一行 |
| `mail2d_read_ledger.json` 的批内追加 | 批内 `_ledger_append_*`／`_ledger_<tag>.py` | **待退役旧实现** | 现存 162 件留档备查，不再新写；其 `LO`／`HI`／`TAG` 常量即 `--append` JSONL 的字段来源 |
| `_h1_state.json` | `_h1_resume.py` | `--mark`／`--advance` | 读-改-写只改指定字段，不整文件覆盖（脚本头注第 1 条） |
| `review_logs/<tag>_claim_map.json` | `mail2d_run_batch.py register` | `--apply` 后合并 | `merge_claim_map()` 合并不是覆盖（覆盖会使 claim_map 缩水、`check` 断言崩）；批内 `_patch_claim_*` 只回改 claim 库文本，不写 claim_map |
| `12-数据库备份/waterlock/register__<db>__<tag>.lock` | `register_waterlock.py` | `acquire`／`release` | `O_CREAT`＋`O_EXCL` 原子创建；`probe`／`show` 只读不改锁；接管须 `--force`＋理由 |
| `05-卷册大纲/` 宿主 `.md` | `outline_writer.py` | `--write`（须配 `--anchor`） | 宿主权威解析＋块级锚点幂等＋路径覆盖＋原子写（`ADR-0010`）；`mail2d_run_batch.py outline` 为旧通用件 |
| `05-卷册大纲/` 宿主的批内回写 | 批内 `_outline_<tag>.py` | **待退役旧实现** | 已对现网结构性失效（见上表 D1），不再新写、不重建 |

## 边界

- 不改变在途批次的数据契约、判读产物、台账 key 结构、claim 号段与大纲块。
- 副本与原件若分叉，以 SHA-256 比对为准；同步动作由主代理在每次同步时承担（`ADR-0006` §5）。
- 原件不得移走或删除：在途批次 H1 `fq_b120`、H2 `fbug_b198`、H3 `fhk_b085`、H4 `ob_b024` 仍以 `script/_db_row_mining/` 为运行路径。
