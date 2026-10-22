# H 线核心驱动清单（mail2d）

本目录 7 件 `mail2d_*.py` 副本为版本化参考件；`script/_db_row_mining/` 原件在在途批次收口前继续作为运行件；路径切换另批执行（`ADR-0006` §1.2；验收判据见 `H1-H4-全链路规格.md` FR-H14）。副本按 SHA-256 **逐字节复制**，不改一个字节（含 BOM 与换行形态），`script/` 原件零改动。

## 核心驱动（7 件）

| 源路径 | 副本 | 字节 | SHA-256 | 职能 | 运行状态 |
| ------ | ---- | ---: | ------- | ---- | -------- |
| `script/_db_row_mining/_prep_batches.py` | `mail2d_prep_batches.py` | 4778 | `4047b37136a11fe110dd36a09a1bf7160305b12de6e6a9dc7fa6a663e0705add` | 批量预建批次：建 spec → dump → 补 `pk_range` → 容器行清单 → 拆 digest，供读手到即派（FR-H01） | 原件运行；副本未启用 |
| `script/_db_row_mining/_mail2d_run_batch.py` | `mail2d_run_batch.py` | 26635 | `f91f0934078e7212bf276a8429f5bf86410e063167275bdadf99486cf5d2bae1` | 单批运行器（`new`／`dump`／`body`／`check`／`register`／`outline`／`bookkeep` 子命令），批内编排与入库、入纲写盘（FR-H01、FR-H07–FR-H10） | 原件运行；副本未启用 |
| `script/_db_row_mining/_mail2d_batch_dump.py` | `mail2d_batch_dump.py` | 5354 | `9efe78538719e0e6fa0d3b7d4a4d91fb277b21ade2e3f6111455f6bda3685a94` | 通用批 dump：全文 dump／`review_logs` digest（pk\|date\|from\|subject\|正文前 420 字）／heads 头表，只读源库（FR-H01） | 原件运行；副本未启用 |
| `script/_db_row_mining/_build_read_ledger.py` | `mail2d_build_read_ledger.py` | 6185 | `b71a431dd3fcd6d5ace7ad5b55ab6b464ca22d7d1ad448f65d587f5b1a75c7bd` | 重建已读区间台账 `mail2d_read_ledger.json`：`records`／`read_judged`／`read_effective`／`queued_records`，预建 spec 不计已读（FR-H11） | 原件运行；副本未启用 |
| `script/_db_row_mining/_merge_cand.py` | `mail2d_merge_cand.py` | 6225 | `3c70664275a7ddec7fa477871c607ebd3571f5e735ab30559cf51a038187cbf5` | 候选分件合并：字段数与等级／长度／越界／重复／禁字符校验，`--srcdb` 回库验存在性剔幽灵 pk（FR-H03、FR-H04） | 原件运行；副本未启用 |
| `script/_db_row_mining/_merge_narr.py` | `mail2d_merge_narr.py` | 3481 | `b9ff2b3e989f18cb903a10e9c2b547d7cac19b778d4407c3bc830639475a15c5` | 叙述分件合并：三列 TSV 汇总，阻断集为缺文件与 CRLF，pk 集合与候选全集对齐（FR-H05） | 原件运行；副本未启用 |
| `script/_db_row_mining/_vn_narr.py` | `mail2d_vn_narr.py` | 6714 | `9763bcfb0c697fb7b3c73cb120b369a4a53f31e0f002e6c575195efae9ce3b4f` | 叙述硬门禁：存在性与 pk 全等、3 个 TAB 字段、长度 60–140、尾标点、禁字符、宿主逐 pk 一致，违规 exit 1（FR-H06） | 原件运行；副本未启用 |

上表字节数与 SHA-256 为 2026-10-22 复制时实测，复制前后逐件相等；7 件均无 BOM、无 CRLF（纯 LF）。复核方式：`script/_p2_mail2d_promote.py`（复制与比对一次完成）、`Get-FileHash -Algorithm SHA256`。

## 未入库的批内一次性脚本

以下类别**不迁入本目录**，留在 `script/_db_row_mining/`（`ADR-0006` §1.2 末句“批内一次性脚本留 `script/`，不迁”）。件数为 2026-10-22 实测（该目录 `.py` 合计 9793 件）。

| 类别 | 件数 | 职能 | 留 `script/` 的理由 |
| ---- | ---: | ---- | ------------------- |
| `_register_*` | 1173 | 单批落库（claim 四表写入）的按批生成件 | 一批一件、批号与 claim 号段写死在文件名与常量内，无复用面；落库契约由 `_mail2d_run_batch.py register` 与 `claimdb_guard.py`／`register_waterlock.py` 承载 |
| `_outline_*` | 631 | 单批大纲回写与宿主块改写 | 同上，`TARGET_REL` 与块头逐批不同；入纲契约由 `_mail2d_run_batch.py outline` 与 `wo007_idempotency.py` 承载 |
| `_bookkeep_*` | 97 | 单批“三零”对账与遗留项清理 | 一次性对账，依赖当批宿主与库内行；常设对账口径在 `_mail2d_run_batch.py bookkeep` |
| `_ledger_*` | 162 | 批内台账追加（仅追加件） | 与 `_build_read_ledger.py` 构成“重建＋追加”双入口的一侧，按批生成；台账 key 结构不迁、不改契约（`ADR-0006` §1.3） |

## 边界

- 不改变在途批次的数据契约、判读产物、台账 key 结构、claim 号段与大纲块。
- 副本与原件若分叉，以 SHA-256 比对为准；同步动作由主代理在每次同步时承担（`ADR-0006` §5）。
- 原件不得移走或删除：在途批次 H1 `fq_b120`、H2 `fbug_b198`、H3 `fhk_b085`、H4 `ob_b024` 仍以 `script/_db_row_mining/` 为运行路径。
