# H5 长线任务主控（mail2d 线 · 小库收尾包）

> **自包含**：新会话／他方 AI 仅读本文件 ＋ `_h5_state.json` 即可续跑，**无须任何上下文记忆**。
> 交接书本体见 `_HANDOFF_H5.md`（范围、纪律、验收），本文件只管“**断点在哪、下一步做什么、有什么硬约束**”。

## 一、上下文预算与并发规模（**实测口径**）

| 项 | 值 | 依据 |
|---|---|---|
| 会话上下文上限 | **200K token** | 本会话实测硬上限 |
| 分件粒度 | **500 行 / 份 ≈ 60–70K token** | `review_logs/<tag>_digest_part<K>.txt` 实测 |
| 读手一次领料 | **1 份 500 行** | 读得动且留有余量（200K 上限内） |
| 每波并发 | **3–5 路子代理并行** | `Agent` 工具 + `run_in_background` |
| 单路止损 | **22 分钟** | `TaskStop` 后以 `TaskOutput` 取出的部分产出或磁盘产物为准 |
| 每波结束核验 | **磁盘条数硬核** | 不能只信子代理口头汇报；比对 `wc -l` 与 pk 端点 |
| 小批阈值 | **总行数 ≤ 320** | 只有 1 份分件时**主代理直读直判**，不派子代理 |

**小批实测例**：`freebsd-ppc` 尾批 `h5ppc_b510_3` 共 **291 行 / 1 份 ≈ 43.7K token**，
主代理一次读完即判出 **176 条候选**，省下一轮子代理调度，且更快更稳。

### 1.1 派发与止损动作

```
主代理：Agent(run_in_background=True) × 3–5 → 每路 1 份 500 行分件
主代理：TaskOutput 轮询（≤ 22 分钟 / 路）
  → 超时 → TaskStop 该路 → 以 TaskOutput 已取出的部分产出 + 磁盘产物为准，缺口下波补
每波结束：wc -l 各份候选文件 + 比对各份末条 pk 与该份区间末端（尾段覆盖校验）
  → 缺口即补读（本线曾一次并发超支漏读尾段 236 行）
```

### 1.2 明确禁用 `CreateWorkflow` / actor 编排（**硬约束**）

已三次实证：actor 无 per-ask 超时、卡死后脚本无法局部止损、`dwf.ts` 已废弃不执行。
任何情况下**不得**在 H5 长线调用 `CreateWorkflow` / `AmendWorkflow` / `ResumeWorkflowRun`
或依赖 `Agent` actor 池做长时编排。子代理编排一律走主会话的 `Agent` 工具 +
`run_in_background` + `TaskOutput` 轮询（见 §1.1）。

### 1.3 分批策略

实测 2,815 行 → `forread` 56MB、`digest` 1.5MB（约 **20MB forread / 千行**）。
故设 **MAX_ROWS_PER_BATCH = 6,000**（forread ≈120MB、digest ≈3.2MB）；
超过者按 offset 递增切多批，`_h5_init_state.py` 已切好（如 `freebsd-fs` 38,710 行 → 7 批）。

## 二、真相源与三条命令

| 文件 | 作用 |
|---|---|
| `_h5_state.json` | **唯一状态源**（27 库／104 批的状态、tag、产出） |
| `_h5_resume.py` | 断点恢复器：`--status`／`--next`／`--advance`／`--mark` |
| `_HANDOFF_H5.md` | 范围与纪律（§二 范围、§三 SOP、§四 铁律、§五 并发、§六 验收、§九 复核与台账） |

```sh
PYM=C:/Users/ykla/.workbuddy-ai/binaries/python/versions/3.13.12/python.exe   # 文本脚本
PYD=C:/Python314/python.exe                                                  # duckdb 脚本
cd /d/librebsd/script/_db_row_mining

$PYM _h5_resume.py --status     # 全表：哪个库、剩余多少、当前批 tag、状态、已产出
$PYM _h5_resume.py --next       # 只打印“下一步该执行哪条确切命令”
$PYM _h5_resume.py --advance    # 自动做完 new+dump+split，并把批次置为 split
$PYM _h5_resume.py --mark <库> <tag> <状态> [--cands N] [--claims "CL-RM-a-b"] [--commit sha] [--hosts 892,894]
```

**批次状态机**（`--mark` 只能取这些值）：
`pending → dumped → split → cand → registered → narrated → outlined → committed`

## 三、单批八步 SOP

`new → dump → check → register → body → outline → bookkeep → commit`。
配套切分/合并助手：`_split_digest.py`（候选侧切分）／`_merge_cand.py`（候选合并）／
`_split_narr.py`（叙述侧切分）／`_merge_narr.py`（叙述合并）。命令以 `--next` 输出为准。

| 步 | 状态 | 动作 |
|---|---|---|
| 0 | — | **四源交叉核对起点**（见 §五 硬约束 1），不符则改 `_h5_state.json` 的 offset 后再开工 |
| 1 | pending | `new` ＋ `dump` ＋ `_split_digest.py <tag> <份数>`（三合一：`--advance`） |
| 2 | split | 派读手（**每波 3–5 路，每读手 1 份 500 行**，见 §1.1）→ `review_logs/<tag>_candidates_p<K>.txt` |
| 3 | cand | `_merge_cand.py <tag> <N> <LO> <HI>` 合并 → `check`（违规须 0）→ `--mark ... cand --cands N` |
| 4 | registered | `register --apply`（先 dry）→ `--mark ... registered --claims "CL-RM-a-b"` |
| 5 | narrated | `body` → `_split_narr.py <tag> <N>` → 派叙述手（同上并发口径）→ `_merge_narr.py <tag> <N> <host1,host2,...>` → `check` |
| 6 | outlined | `outline --write` ＋**幂等二跑须 +0** |
| 7 | committed | `bookkeep --write` → 证据等级门禁 → `commit --apply` → `--mark ... committed --commit <sha>` |
| 8 | — | 更新台账 `_h5_ledger_update.py <lib> <lo> <hi> <tag> [--complete]`（只改己库条目） |

**每批提交一次**（缩短在途窗口）；**每库最后一批完成**时加 `--complete` 置台账闭环。

## 四、读手与叙述手任务书模板要点

任务书由 `_h5_gen_read_task.py <tag>` 从 `_batch_<tag>.json` ＋ digest 画像自动生成到
`_READ_TASK_<tag>.md`。要点（模板须与之一致）：

- **上下文**：任务书写明“**200K 上下文**，每读手 1 份 500 行 ≈ 60–70K token”，禁止"1M 上下文"或
  “领多份逐份读完”等旧口径。
- **分件路径**：`review_logs/<tag>_digest_part<K>.txt`（K 由派发指令给定）。
- **产出**：
  - 读手：`review_logs/<tag>_candidates_p<K>.txt`，格式 `pk|等级|摘要`。
  - 叙述手：`review_logs/<tag>_mount_narr_p<K>.tsv`，**无表头**，`pk\t<host>\t<叙述>`。
- **编码**：UTF-8 无 BOM、LF 换行（BOM 会让合并时首行被静默丢弃；CRLF 会中止合并写盘）。
- **禁字符**（候选摘要）：`“` `”` `*` `\` `|`。
- **禁读**：`<tag>_forread.txt`（体积过大），只读 digest 分件。
- **收／不收纪律、证据等级、摘要长度、密度基准、文风样例**：模板已固化，不得在派发指令里另说。

### 4.1 宿主 key 规则

宿主 key = 大纲节号**去点**（如 `131.5 → 1315`、`98.9 → 989`、`100.18 → 10018`、`149.11 → 14911`）。
宿主归属**由 digest 实判**，不能凭 batch spec 里的 `待定`。本线已多次因 spec 预判宿主与实际
年代／主题不符而实判改挂（`freebsd-i386`、`freebsd-sparc64` 各两批均发生过）。

## 五、硬校验口径

### 5.1 候选（`_candidates_p<K>.txt`）

- 格式：`pk|等级|摘要`；等级 ∈ **{L3, L4}**。
- 摘要长度 **20–80**（`len()` 口径，**ASCII 与中文各计 1**——中文写作时最容易误判）。
- pk 在 `[pklo, pkhi]` 内且**不重复**。
- 禁字符：`“` `”` `*` `\` `|`；无 BOM、无 CRLF。
- 合并：`_merge_cand.py <tag> <N> <LO> <HI>`。

### 5.2 叙述（`_mount_narr_p<K>.tsv`）

- **无表头**，格式 `pk\t<host>\t<叙述>`。
- 叙述长度 **60–140**。
- `host` 必须在**该批最终宿主集合**内（由 digest 实判产出，见 §4.1）。
- pk 与候选全集**一一对应**（不多不少）。
- 合并：`_merge_narr.py <tag> <N> <host1,host2,...>`。

### 5.3 提交门禁

- `check` 违规 0／越界 0。
- `register` 引文同串失败 0、四表 join 命中 = 候选数。
- `outline --write` 幂等二跑 **+0**。
- `bookkeep` 缺块 0／claim_id 不符 0／重复 0。
- `audit_evidence_level_labels.py` → PASS。
- `git show --numstat`：新增行数 == 块数×5，且**只含本批宿主文件**（不裹挟他人改动）。

## 六、坑与降级

1. **`check` 报“spec 无 pk_range，先跑 dump”** → 批次 spec `_batch_<tag>.json` 缺 `pk_range`，
   要**手工补 `[pklo, pkhi]`**（`check` 会硬退出，见 `_mail2d_run_batch.py:124`）。
2. **`script/` 整目录被 gitignore**（`.gitignore` 的 `/script`）→ **只有宿主 `.md` 的改动会进 git**；
   脚本与 `review_logs/` 改动只落磁盘，靠宿主 md 提交带节奏。审计时看到"脚本改了但没进 git"
   属正常，勿惊。
3. **摘要长度硬上限 80 是 `len()` 口径**，**ASCII 与中文各计 1**——中文写作最容易误判。
   务必让生成脚本自己校验并阻断写盘，而不是靠肉眼估（本线 `freebsd-elastic` 首批 89 条中
   18 条超长，脚本 `_h5e_b501_shrink.py` 可作模板）。
4. **`_merge_narr.py` 的阻断级检查**：缺文件 / CRLF / 空集 会**中止不写盘**，避免不完整的总表
   覆盖已有总表。看到中止信息先补齐分件，勿手改总表。
5. **`register` 增量重跑会覆盖 claim_map**（旧缺陷：53 条被缩到 15 条致 `check` 断言崩），
   现已加 `merge_claim_map` 合并逻辑——但仍建议**在批次内只跑一次**。若必须重跑，
   先备份 `_claim_map.json`，跑完比对条目数。
6. **并发超支尾段漏读**：本线曾一次并发超支漏读尾段 236 行。每波结束必做**尾段覆盖校验**
   （各份末条 pk 与该份区间末端比对），缺口即补读。
7. **同文件并发编辑会丢改**：本线曾 6 处并发改同一文件、5 处被静默覆盖。编辑必须串行。
8. **`outline --write` 幂等二跑须 +0**；register 报“跳过 source_id”属正常（历史已注册），
   须按 `_claim_map.json` 把候选筛齐，否则 `_merge_narr` 报缺、outline 断言失败。

### 6.1 降级路径

- **子代理卡死**：`TaskStop` 单路 → 磁盘产物为准 → 缺口下波补派；**不要**重启整波、不要切工作流。
- **子代理配额用尽**（`200/200` 之类提示）：由主会话手工撰写剩余分件的候选/叙述，
  按“读 narrpkg → 撰写 60–140 字 → Write 剥 BOM → 尾句池补足”流程收敛
  （`freebsd-sparc64` 首批 p5–p12 已按此路径闭环）。
- **小批（≤320 行）**：主代理直读直判，不派子代理（见 §1）。

## 七、收尾

`bookkeep → audit → commit → 状态回写` 的顺序不可颠倒：

1. `bookkeep --write`：把本批候选/叙述/claim/宿主写入 `_h5_state.json` 与台账。
2. `audit_evidence_level_labels.py`：证据等级门禁（L3/L4 标签一致）。
3. `commit --apply`：产出 git 提交（只含本批宿主 md，不裹挟他人改动）。
4. `_h5_resume.py --mark <lib> <tag> committed --commit <sha> [--hosts ...]`：状态回写。
5. 台账：`_h5_ledger_update.py <lib> <lo> <hi> <tag> [--complete]`。

## 八、硬约束（违反即返工）

1. **起点四源交叉**（决定性证据优先级：changelog ＞ claim anchor ＞ 台账 records ＞ 源库位次）：
   台账 `read_effective` 是**已读计数**不是**前沿**；历史 spec 遗失会低估前沿。
   已知订正：`tech-pkg` 起点 1500（非 0）、`freebsd-desktop` 起点 1000（非 0）、
   `freebsd-smp` 起点仍取 0（500–999 已读，重读由幂等兜底）。
2. **只做本文件范围**：其余 41 库属 H1–H4，库清单互不相交，不得越界。
3. **并发 3–5 路读手/波**（见 §1），每读手 1 份 500 行；单路 22 分钟止损；每波结束磁盘核验。
   **禁止**改用 `CreateWorkflow` / actor 编排（见 §1.2）。
4. **同一文件禁止并发编辑**；编辑必须串行。
5. **幂等**：见 §6 硬约束 8 与 §5.3。
6. **门禁**：见 §5.3 全项。
7. **tag**：本线已用至 b138，H5 取 `h5*`＋`b502`–`b528` 段避撞；新增批次不得复用已用 tag。

## 九、当前进度（**台账快照，实时以 `--status` 为准**）

已闭环库（截至 2026-09-21）：`freebsd-elastic`（`h5e_b501`，89 块，`6952b6c7f`）、
`freebsd-x11`（`h5x_b502_1` 364 块 `bb557680a`；`h5x_b502_2` 115 块 `a740df7d5`）、
`freebsd-ipfw`（`h5ip_b503_1` 664 块 `57f8c01e8`；`h5ip_b503_2` 228 块 `0d4fcd8d8`）、
`freebsd-desktop`（`h5dk_b506_1` 348 块 `37feb12e9`；`h5dk_b506_2` 302 块 `748e6fc66`）、
`cu`（`h5cu_b504_1` 677 块 `efead9c8a`；`h5cu_b504_2` 618 块 `729d10672`）、
`freebsd-acpi`（`h5acp_b505_1` 872 块 `e021d5180`；`h5acp_b505_2` 807 块 `aa5929763`）、
`freebsd-smp`（`h5smp_b507_1` 871 块 `c03db5694`；`h5smp_b507_2` 905 块 `f97649a98`）、
`freebsd-i386`（`h5i3_b508_1` 495 块 `a6fe3dbbb`；`h5i3_b508_2` 214 块 `b42080604`）、
`freebsd-sparc64`（`h5sp_b509_1` 948 块 `216bd35dc`；`h5sp_b509_2` 1,212 块 `69d48aa85`）。

细节、宿主分布、重判与勘误见 `_HANDOFF_H5.md` §9.3 台账。实时状态一律以
`$PYM _h5_resume.py --status` 为准，本表不随进度更新。

## 十、会话中断后的标准动作

```sh
$PYM _h5_resume.py --status      # 1 看断点
$PYM _h5_resume.py --next        # 2 拿命令
# 3 执行 → 4 立即 --mark（不要攒着）
```

若上一会话遗留未 `--mark` 的中间产物（如已合并的候选、已注册的 claim），
先按 §三 表格反推其应处状态并 `--mark` 补记，再继续。
