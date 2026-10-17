# 13-deepseek-linux 路径消解报告（2026-09-13）

**裁定**：主理人指示“统一所有任务的写入路径，不再使用 13-deepseek-linux 这个路径，将其消解掉”。
**执行**：主代理一次性完成（备份→平移→引用改写→豁免规则→验证）。
**先例对齐**：沿用 `13-deepseek-cankao` 消解先例（全量备份入 `12-数据库备份/` + 消解报告入 `08-核查报告与多轮复核/`）；与 cankao 不同，本战线为**在役战线**，活跃资产并入其既有工作区而非归档。

## 一、映射表（1:1 平移，目录名不变）

| 原路径 | 新路径 | git 追踪状态 |
| --- | --- | --- |
| `13-deepseek-linux/01-战线spec/` | `script/_db_row_mining/dslinux/01-战线spec/` | 追踪（经豁免规则） |
| `13-deepseek-linux/02-遍历留痕/` | `script/_db_row_mining/dslinux/02-遍历留痕/` | 追踪（trail.duckdb 按 `*.duckdb` 全局规则仍忽略，与迁移前一致） |
| `13-deepseek-linux/03-候选/` | `script/_db_row_mining/dslinux/03-候选/` | 追踪 |
| `13-deepseek-linux/05-数据库/` | `script/_db_row_mining/dslinux/05-数据库/` | 忽略（仓库策略：duckdb不入库；原目录级忽略规则同步改写） |
| `13-deepseek-linux/06-大纲增补/` | `script/_db_row_mining/dslinux/06-大纲增补/` | 追踪 |
| `13-deepseek-linux/`（空壳） | 已删除 | — |

**统一原则**：本战线全部读写收敛于 `script/_db_row_mining/dslinux/`（与其他战线资产同居 `script/_db_row_mining/` 惯例位）；全量备份入 `12-数据库备份/`；本报告入 `08-核查报告与多轮复核/`。

## 二、备份

- `12-数据库备份/13-deepseek-linux_消解前全量备份_20260913_064135/`（141M，59 文件，含全部 duckdb 与 .mimosa 工具态）。

## 三、引用改写

- 脚本 `script/_migrate_dslinux_paths_20260913.py`（Mimosa 扫描通过版）：白名单 13 目录内文本文件字节级替换 `13-deepseek-linux/`→`script/_db_row_mining/dslinux/`（正斜杠）与反斜杠变体；冻结快照（12-数据库备份）与 .workbuddy 历史日志不改写。
- 改写涉及 gen/review/留痕/候选/大纲全链路脚本与文档；**斜杠型引用在活文档中已清零**（剩余 4 处为 Mimosa hook-state 缓存，非仓库内容）。
- 人工修复 2 处：`progress.py` 的 `os.path.join` 裸组件拼装（TRAIL_DB 改为 `HERE/02-遍历留痕/…`）；`.gitignore` 两处（297 行目录忽略改新路径；228 行 `/script` 改级联豁免——Git 规则父目录被整体排除时无法子级豁免，故用 `/script/*` + 逐级 `!` 解锁四个追踪子目录）。
- **历史性裸提及保留**：一次性法证脚本（`_dslinux_*_2026090x.py`、早期 `gen_p12-18`/`gen_smp_p01-02` 系）与文档内叙事性提及（各活文档已加解码注）；`08-核查报告与多轮复核/20260909_*复核报告.md` 与 cankao 消解归档为历史记录不改。

## 四、验证（全绿）

1. `progress.py report`：linux-smp（32 页/1590 行）与 ksummit-discuss（76 页/3800 行）均从新 TRAIL_DB 正确读出。
2. `gen_smp_p30.py` 幂等重跑：新 CAND 路径读取、判定表解析、47 src 全命中跳过、“无新增，退出”。
3. `dslinux_claims.duckdb` 新位置只读打开：claim 表 4,877 行。
4. `git add -A` 后 **42 个改名（R）全部识别**，历史保留；1 个 D 为 `dslinux_claims.duckdb.bak_p4_20260910`（原被误追踪的备份件，按仓库 duckdb 备份忽略策略转忽略，盘上与全量备份均在）。

## 五、后续写入路径基准（接管者必读）

| 用途 | 路径 |
| --- | --- |
| 战线规范/交接 | `script/_db_row_mining/dslinux/01-战线spec/` |
| 遍历留痕（唯一真相） | `script/_db_row_mining/dslinux/02-遍历留痕/traversal_trail.duckdb` |
| 候选流 | `script/_db_row_mining/dslinux/03-候选/candidates.jsonl` |
| 成果库（claim/evidence/raw_source） | `script/_db_row_mining/dslinux/05-数据库/dslinux_*.duckdb` |
| 大纲增补素材 | `script/_db_row_mining/dslinux/06-大纲增补/`（00-总览为账目入口） |
| 页管线工作区 | `script/_db_row_mining/dslinux/{pages,view,review,gen}/`（本就在此，未动） |

新文件若落在 `script/` 下默认被忽略，四个追踪子目录已由 `.gitignore` 级联豁免保住；除此之外的 script/ 新增文件如需入库须个案豁免。
