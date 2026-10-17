# 交接书：BSD 邮件列表线（Phase 2D 行级史料挖掘）· 2026-09-18

> 生成时间：2026-09-18 ｜ 生成者：mail2d 线当前会话 ｜ **本文件自包含**，接手方无需任何前置上下文（但强烈建议先读 CLAUDE.md 与 `00-编纂规则与格式规范/01-规则/README.md` 索引）。
> 面向 **200K 上下文窗口**适配编写：**单批规模以 200K 可容纳为上限**，优先在尽量少的会话内完成剩余清库工作。
> **上一份交接书**：`_HANDOFF_MAIL2D_20260917.md` 已退役（已被本文件取代）；权威长线任务书：`_MAIL2D_PLAN_HANDOFF.md`（**唯一权威文档**，数字实时计算，可反复重跑刷新）。

---

## §0 一句话任务

把 `03-原始史料库/11-邮件列表史料/` 下 **BSD 五个目录**的邮件列表逐封审读，把有价值的史料主张落进 `historical_claims.duckdb`，再以 ROW_MINE 块形式写进 `05-卷册大纲/` 对应章节，最后**原子提交**。

## §1 任务边界（硬性）

- **在范围内**（257 库）：`01-freebsd`(140) / `02-netbsd`(114) / `03-openbsd`(1) / `04-dragonfly`(1) / `06-other-bsd`(1)。
- **不在范围内**：`05-linux-kernel`（Linux 战线）、`07-usenet`（usenet 战线）。**不读写、不统计。**
- ⚠ **范围按目录判定，不按库名**（`rust-for-linux`、`tech-board-discuss` 在 05 目录内但不以 linux 开头）。
- **停止条件**（任务书 §13）：**仅当用户明确说“停止／停／不用继续了”时停止**；单批失败/子代理中断/门禁告警一律就地修复后继续。

## §2 当前状态（2026-09-18 集群实况，已核实）

| 指标 | 值 |
|---|---|
| 范围内库数 | 257 |
| 全库封数 | 2,945,106 |
| 实际已读封数 | **268,724（9.1%）**（按批数×500 估算的下界为 214,694＝7.3%） |
| 未完成封数 | **2,676,382** |
| 已闭环库（catalog `completed`） | **205 / 257（79.8%）** |
| 未完成库 | 49（清库 43 ＋ 巨型 6） |
| claim 库累计总数 | **65,993**（实时查库；任务书 §3 快照 65,281 略旧，差 712 系后续批次合入） |

catalog 状态（复算确认）：**completed 205 ｜ in_progress 27 ｜ pending 25**。

### 已完成批次（2026-09-18 会话，共七批）

| 批次 | 库 | 块数 | 门禁 | 提交 |
|---|---|---|---|---|
| fh_b081 | freebsd-hubs（整库收官） | 775 | PASS | fc9341996 |
| fo_b082 | freebsd-office（整库收官） | 303 | PASS | e62f0f9df |
| pa_b083 | port-arm（整库收官） | 1976 | PASS | d3cdebe44 |
| fpa_b127 | port-alpha（整库收官） | 2365 | PASS | 705fd84d4 |
| fnb_b128 | freebsd-newbies（整库收官） | 906 | PASS | 6d2e7bbc6 |
| fisp_b129 | freebsd-isp（半库，第一批） | 2194 | PASS | a82f4e220 |
| fisp_b130 | freebsd-isp（第二批，主会话直读） | 163 | PASS | b64568597 |

- **freebsd-isp**：已读 **16,648 / 31,347 封（53.1%）**，剩余 **14,699 封**＝第三批。
- 另：fis_b077（freebsd-isdn）已在此前会话收官（585 块，commit e9583c213）；today 累计 git 提交 258 次、大纲 +67,557 行。

## §3 工具链（全部在 `script/_db_row_mining/`）

### 3.1 主运行器 `_mail2d_run_batch.py`

```bash
PY=C:/Python314/python.exe        # 需要系统 Python（duckdb 装这里）
cd /d/librebsd/script/_db_row_mining
$PY _mail2d_run_batch.py new      --db <库> --offset N --n 2000 --tag <批号> --hosts <节号逗号分隔，如 881,911,921>
$PY _mail2d_run_batch.py dump     --tag <批号>
$PY _mail2d_run_batch.py check    --tag <批号>
$PY _mail2d_run_batch.py register --tag <批号> --apply
$PY _mail2d_run_batch.py body     --tag <批号>
$PY _mail2d_run_batch.py outline  --tag <批号> --write
$PY _mail2d_run_batch.py bookkeep --tag <批号> --write
$PY _mail2d_run_batch.py commit   --tag <批号> --apply
$PY _mail2d_run_batch.py status   --tag <批号>
```

- `new` **校验批号不撞**（查 claim 库 anchor 全集）。批号约定：库名缩写 + `_b` + 三位序号。
- `outline` 的宿主路径由 Python 直写；宿主 key = 节号去点（`172.2`→`1722`）。
- `commit` 内置**原子提交**：同一调用内核对 numstat + `git commit -- <paths>`。
- `dump` **不回写 `pk_range`** → 随后 `check` 可能报“先跑 dump”。**dump 后须手工把 `pk_range` 补进 `_batch_<tag>.json`**。

### 3.2 辅助脚本

| 脚本 | 用途 |
|---|---|
| `_report_today_total.py` | 今日 + 总进度（内置范围过滤；今日日期字段为硬编码，勿当实时） |
| `_split_digest.py / _split_narr.py` | 拆份（参数化，`<tag> <N>`） |
| `_merge_cand.py` / `_merge_narr.py` | 合并各份候选/叙述（剥 BOM + 升序 + 交集 0 校验） |
| `_gen_cand_*.py` / `_narr_*.py` | 主会话直读时的候选/叙述装配脚本 |
| `_dup_scan.py` / `_dup_prune.py` | 同文模板帖去重（`fnb_b128` 实证 932→906） |
| `_verify_blocks.py` | 块体级核验（块存在/claim_id/等级/叙述） |
| `_host.py` / `_host_index.txt` | 节号→精确宿主路径（禁手写） |

## §4 单批标准流程（6 步）

1. **判主题定宿主**：`dump` 后**先读 digest 前 5–10 行**判断该库主题与年代；按**主题**选章（年代仅细分），**勿沿用他库模板宿主**；改 spec 的 `hosts` 后用 `load_hosts()` 验证 4 key 可解析。
2. **拆份派读手**：digest 拆每份 ≤500 行，**并行**派子代理（见 §7）。
3. **合并候选** → `register --apply` → `body` → 按候选数拆份派**叙述**子代理（并行）。
4. **合并叙述** → `outline --write`（幂等二跑，二跑须 +0）。
5. **`bookkeep --write`**：落地核验（缺块/claim_id/重复三项全 0）＋ 格式校验 ＋ progress ＋ catalog 升格。
6. **`commit --apply`**：按宿主核块数（权威）＋ 行数容差校验 → 提交。

## §5 铁律（违反即返工）

1. **块格式**：ROW_MINE 块 = **恰好 5 行**（标记 ＋ `**当事人自述**（证据等级：Lx…）` ＋ 空 ＋ 正文 ＋ 空）；块头等级**从 DB 真值读**，严禁写死字面。
2. **机器块不可改**：`DB_REF/DEEP_ANALYSIS/COL_SCAN/DB_POINTS/PODCAST_REVIEW/MAIL_INSIGHT/ROW_MINE` 只登记，不修改。
3. **替换须完整锚点 + `count==1`**，先 dry-run 再 write；写盘前 grep 确认旧值 0 残留。**禁止全字串替换、禁止新建/移动/重命名源文件。**
4. **格式**：UTF-8 无 BOM、LF、中文弯引号、**禁用直角引号（U+300C/U+300D）**、路径/文件名加粗、手册页 `xx(N)` 加粗。
5. **catalog 状态只升不降**（只做 `pending/deferred → in_progress`；`completed` 由专门流程判定）。**绝不可用“批数 × 500”反推状态**（曾误降 95 个 completed）。
6. **不 commit 他人改动**：`git commit -- <paths>` 提交**工作区状态**；宿主常被多会话共用；提交前按宿主核块数。**不 commit 时绝不 `git add` 全树。**
7. **收/不收纪律**（提示词必须逐条写清）：
   - **不收**：pkg-fallout、portscout、tinderbox、bugzilla/GNATS 转发、提交通知、例行升版、纯求助/问答/联络/对骂、空正文或 <40 字符。
   - **要收**：当事人一手 L4；可查事实 L3；里程碑（新建/退役 port、破坏性变更、CVE、架构改动）。
8. **密度基准逐库给定**（见任务书 §9 表）：同批大小下收率可差 35 倍（elastic 0.9% vs www 31.9%）。**基准跨库套用必然系统性多收或少收**。
9. **🔴 提示词须并列两套尺度**：候选摘要 **20–80 字**（宜写 60–75）；叙述 **60–140 字**。禁直角引号、`*`、`\`、`|`、制表符；末尾不加标点。
10. **一个 host 文件末尾无换行时，追加块后 git 记 `+N/−1`** → 允许，但须 `git diff` 确认仅行尾差异。

## §6 已知坑（全部踩过，必看）

| # | 坑 | 规避 |
|---|---|---|
| 1 | 单份文件子代理读 >10 次触发循环检测中断 | 份 ≤500 行，每份 ≤5 次 Read |
| 2 | digest >500 行必须拆份否则读手重读超限 | 2000 行拆 4 份 |
| 3 | 个别库 subject 几乎全空（port-alpha 6900+ 封仅 7 封有） | dump 内置正文 Subj 回退；开批前先查 subject 非空率 |
| 4 | 个别行正文为空 → 引文空串落库中止 | 运行器已内置：正文空则以主题作引文 |
| 5 | 宿主映射缺节 | `load_hosts()` 双源合并（mount 文件＋遍历大纲），覆盖约 2000 节 |
| 6 | 残留检查误判同名库 | 已修：仅当 lib/anchor 与模板不同才计残留 |
| 7 | `%` 格式化串裸 `%` 报错 | 写 `%%` |
| 8 | 子代理 504/网络中断 | **原样重试**，勿改路径 |
| 9 | 校验命令**禁接管道后再 `&&`**（管道退出码覆盖） | 分开执行 |
| 10 | `local_pk` 是 VARCHAR | 比较须 `CAST(... AS BIGINT)` |
| 11 | TSV **带 UTF-8 BOM** 首行解析失败静默丢行 | 合并前必须剥 BOM |
| 12 | 子代理配额（约 200/会话）耗尽 | 见 §8（主会话直读法兜底） |
| 13 | 年份空档可能是 id 分段所致（freebsd-isp 1999–2001） | 先查候选年月分布，勿误改宿主规则 |
| 14 | `new --db` 收库名而非路径 | 传库名（脚本内部 glob 两种模式） |
| 15 | 节号还原 key 不能用末位加小数点（100.18 → 10018 不是 1001.8） | 按 `^(\d+)\.(\d+)-` 拆两段拼接 |

## §7 子代理派发与监控（若配额可用）

- **一条消息内多个 `Agent` 调用**才能真正并行；提示词须自包含（读哪个文件、写哪个文件、格式、收/不收清单、该库密度基准、禁反复读文件）。
- **逐份核验**（不可只看口头汇报）：候选行数/pk 区间/升序/L4·L3 合法/摘要长度/无禁用字符；叙述行数 == 候选数、pk 集合一致、host_key ∈ spec 的 hosts、长度 60–140。
- 合并后：各份交集必须为 0，并集 == 总数。
- 落库后：写后反查 == 候选数；回写后幂等二跑 +0；提交前按宿主核块数（权威）。

## §8 🔴 子代理配额耗尽的“主会话直读”作业法（200K 适配）

若 `Agent` 报 `Subagent spawn limit reached`，读手与叙述手都须由主会话承担。要点：

1. **单批规模以 200K 上下文为限**：Read 单次上限 20,000 token、474 行 digest ≈58k token（1 份需 3–4 次 Read）。**200K 下建议单批 3–6 份（约 1,500–3,000 封）**，读完即刻落盘候选分件脚本，避免上下文丢失。
2. 判读结果**逐份写 `_cand_<tag>_pK.py`**（含 ROWS 列表 + 升序/去重/长度/禁字符自检 + 写盘）。
3. **摘要一次写足 60–75 字**（实测三轮收敛：21→7→0 越限）；写成后立即用脚本打印越限全文再改。
4. 短摘要（<60 字）叙述扩写 2–3 轮，`_narr_<tag>.py` 内用 `FIX`/`FIX2` 链式覆盖。
5. 该作业法比子代理慢约 5–10 倍，仅在配额耗尽时使用。

## §9 下一恢复入口（接手后照做）

### freebsd-isp 第三批（推进 `freebsd-isp` 至全库收官）

- 状态：已读 16,648 / 31,347（53.1%），剩余 **14,699 封**。
- 建议批次（200K 上下文适配，每批以 3–6 份 digest 为限）：

```bash
cd /d/librebsd/script/_db_row_mining
PY=C:/Python314/python.exe
# 批次 c/b131（offset 16648, n 3000）——先小批试密度与宿主
$PY _mail2d_run_batch.py new --db freebsd-isp --offset 16648 --n 3000 --tag fisp_b131 --hosts 881,911,921,925,10017,1011
$PY _mail2d_run_batch.py dump     --tag fisp_b131
# → 补 pk_range 到 _batch_fisp_b131.json
# 读 digest 前 5 行判主题/年代；必要时调整 hosts；然后拆份读/装箱
$PY _mail2d_run_batch.py register --tag fisp_b131 --apply
$PY _mail2d_run_batch.py body     --tag fisp_b131
# 叙述（候选≤83 拆份；或主会话装配）
$PY _mail2d_run_batch.py outline  --tag fisp_b131 --write
$PY _mail2d_run_batch.py bookkeep --tag fisp_b131 --write
$PY _mail2d_run_batch.py commit   --tag fisp_b131 --apply
```

- 随后按任务书 §11.1 顺序推进剩余库（`freebsd-alpha`(9 窗)、`freebsd-scsi`(10 窗)、`freebsd-amd64`(10 窗)、`freebsd-java`(11 窗)、`freebsd-hardware`(12 窗)、`freebsd-arch`(18 窗)、…）——**低自动化库优先**。
- 巨型库（freebsd-questions/current/hackers/bugs/ports、openbsd_mail）列为长尾：各需数百批，**速率低优先级**。

## §10 相关路径与文档

- 权威任务书：`script/_db_row_mining/_MAIL2D_PLAN_HANDOFF.md`（**唯一权威**，数字实时更新）。
- 进度复算：`C:/Python314/python.exe _report_today_total.py`。
- 技能手册：`~/.workbuddy-ai/skills/mail2d-batch-mining/SKILL.md`（含全部踩坑与修法，17 节）。
- 每日日志：`D:\librebsd\.workbuddy-ai\memory\YYYY-MM-DD.md`（追加式）。
- 长期记忆：`D:\librebsd\.workbuddy-ai\memory\MEMORY.md`。
- 宿主路径：`script/_db_row_mining/_host_index.txt`（节号→路径，**禁手写**）。
- 邮件库源：`03-原始史料库/11-邮件列表史料/<01-freebsd|02-netbsd|03-openbsd|04-dragonfly|06-other-bsd>/db/<库>.duckdb`。

---

## 附：本线已完成工作的规模（供接手方校准）

- claim 库累计 **65,993** 条；本线已闭环 **205 / 257（79.8%）**。
- 单批典型产出：**9–341 条**（视自动化占比）；2000 行批典型 150–450 条。
- 单批典型工具调用：**10–14 次**（含 2–4 子代理）；200K 直读法每批约 **20–40 次**（3–6 份 digest）。
- 语言/口径：现代汉语、学术化表达；标题/档案引用按任务书格式；不在对话里堆砌过程枚举。