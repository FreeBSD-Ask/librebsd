# 交接书 **dakuC** ｜ usenet 单库任务：**list40 · unix.bsd**（1982–2004）

**生成**：2026-09-18 23:05 ｜ **修订**：2026-09-18 23:2x（**去除跨组叙述，本文件只涉本组**；**第三节经复核更正：不存在漏判 pk**）
**任务范围**：**仅 list40（`unix.bsd`）** —— 本文件**自足**（自带现状真值、判据要点、流程、工具、验收），可单独开工
**口径真值**：`_progress_audit_7groups.py`（只读，2026-09-18 实测）
**本线性质**：**已 100% 全读并完成收官与终验收口**（2026-09-18 复核确认；无新增段可读、无遗留判读、无待补块）

> **接手第一件事**：读 `_RESUME.md` → 跑 `_progress_audit_7groups.py` 核对本组真值 → 跑 `_scope_guard.py 40`。

---

## 一、任务边界

1. **本任务只负责 list40（`unix.bsd`）**。
2. **只读本组**：claim 注册、块落盘、`_excluded_pks.tsv` 追加、状态机更新，**一律只涉本组**。
3. **共享文件**（`_excluded_pks.tsv`、`long_task_state.json`、`_RESUME.md`）**改前先读**；
   **只追加／更新本组条目，不改动任何非本组条目**。
4. **宿主文件一律按“只增不撤”处理**；撤块必须限定本批 tag 与 pk 作用域。
5. 每批动手前后各跑 `_scope_guard.py 40`；越界即停并报告。**不回滚非本批改动**。
6. **不新建／不移动／不重命名任何源文件**。

---

## 二、本组现状真值（2026-09-18 实测）

| 项 | 值 |
|---|---|
| 新闻组 | `unix.bsd`（list_id = **40**） |
| pk 区间 | **153,816 – 172,556** |
| 年代 | 1982–2004 |
| 总量 | **18,735 头** |
| 已读 | **18,735（100.00%）** |
| 剩余段 | **0**（总段 47） |
| 前沿 | 172,543 |
| 注册 claim | **4,503** |
| 入纲块 | **4,503 == 注册**（不变式成立） |
| 孤儿 / 幽灵块 / 重复落地 | **0 / 0 / 0** |
| 等级分布 | L4 **1,504** ／ L3 **2,999** |
| 排除登记 | 41 条 |
| 段台账 / spec | **47 / 47**，无缺段 |
| 收率区间（本组） | **11%–22%**（`_ngcfg.py` 的 `CFG[40]`） |

**结论**：本组的**判读与落地已全部完成，终验收口已全部通过**（2026-09-18）。
**原记“3 个漏判 pk”经逐库实测不成立**（三 pk 不存在于源库，属窗口整数空档）——详见第三节更正。
**本组现无任何遗留工作**；如需再动，只跑只读判据（§4），勿重跑落地链。

---

## 三、🔴 复核更正（2026-09-18 23:1x）：**不存在漏判 pk，本节原“补正”任务作废**

> **本节原判“3 个漏判 pk（s39 pk169179／s41 pk170177／s44 pk171377）”经逐库实测，判据不成立。**
> 原结论系由“输入表 399 行 vs 窗口 400 整数槽”之差反推，误把**窗口整数空档**当作**记录丢失**。
> **接手者请勿执行原 3.3 的补正步骤**（该步骤将无对象可判，且重跑 `_land_seg.py` 会因容量感知
> 重路由既有 pk 而制造核验假 FAIL）。

### 3.1 实测证据

| 段 | 窗口 | 窗口整数槽 | 源库实到 | 输入表 | TSV | 源库有而 input 无 | input 有而源库无 | 窗口空档（不属本 list） |
|---:|---|---:|---:|---:|---:|---|---|---|
| s39 | `[168986, 169385]` | 400 | **399** | 399 | 399 | **空** | **空** | 169179 |
| s41 | `[169786, 170185]` | 400 | **399** | 399 | 399 | **空** | **空** | 170177 |
| s44 | `[170986, 171385]` | 400 | **399** | 399 | 399 | **空** | **空** | 171377 |

- 三 pk **不存在于源库** `usenet_mail.duckdb.messages`（`WHERE id=?` 返回空）→ 属全局 pk 空洞。
- **全组 47 段复验**：s13–s47 共 35 段（有 TSV 者）**源库 pk 集 == 输入表 pk 集 == TSV pk 集，
  双向差集为空，0 段不一致** → **全组无漏判**。
- 误判来源：`_staging_ng40_s*.md` 的“源库实到 **400 头**”为**模板套语**（s47 实到 371 亦书 400），
  不可作真值；**真值一律取源库实测**。
- s1–s12 无 TSV/输入表（旧流程，已消费），其覆盖以“注册 + 入纲 + 排除登记”闭合（见 §3.4）。

### 3.2 `_hdr()` 换行缺陷在 list40 的**真实**影响面（元数据级，非覆盖级）

全 47 个 heads 文件扫描：**5 段各 1 条**断行（s29／s32／s36／s41／s43），且**断行均位于 `SUBJ` 字段**
（续行以制表符起首），故**该 pk 仍被正则命中、从未丢失**，仅 heads 元数据 SUBJ 被截断：

| 段 | 受影响 pk | heads 截断 SUBJ | 源库真值 SUBJ（续行） | TSV 判决 |
|---:|---:|---|---|---|
| s29 | 165051 | `Interface monopolies` | `…\n\tRe: Patents: What they are…` | DROP D7 |
| s32 | 166468 | `FAS-compatible drivers` | `…\n\tRe: The evitable question -- MGR` | DROP D8 |
| s36 | 167939 | `Re: AT&T Long Distance Boycott (was: BNR2SS, Mach, and The` | `…\n Lawsuit)` | DROP D8 |
| s41 | 169881 | `Precedent... Whitesmiths` | `…\n\tRe: AT&T vs. BSDI --> …` | **L4 P5** |
| s43 | 170671 | `Designing UNIX Lite?` | `…\n\tRe: Funding 4.4BSD Development` | DROP D8 |

- `forread` 保留原换行，判读时全文可见；唯一入选件（s41 pk169881）已回读原文核验，摘要与正文相符。
- 结论：**无需补判、无需补块**。heads 元数据截断不追改（判读已完成并落地，重写 heads 无产出）。

### 3.3 原“补正作业步骤”——**已作废，勿执行**

原步骤①–⑧ 以“存在 1 个未判 pk”为前提。既然该 pk 不存在，①–③ 无对象可判；
而⑤“重跑 `_land_seg.py`”会触发**容量感知重路由**（第七节坑 1／第八节坑 4），
反而把已正确落地的 pk 指向新宿主，使 `_verify_outline_landing.py` 报**假 FAIL**。
**如需复核，只跑只读判据（§4），不要重跑落地链。**

### 3.4 验收结果（2026-09-18 已全部实测通过）

- [x] 47 段 `_verify_outline_landing.py` → **47/47 PASS**
      （首轮 6 段假 FAIL：s6／s7／s9／s10／s13／s34 —— 陈旧 `_groups_*`／`_targets_*` 映射；
      以 `_mk_groups_from_map.py` 按 claim_map ＋ 磁盘实宿主重建后转 PASS，旧映射已备份 `_backup_groups_20260918/`）
- [x] 47 段 claim_map 合计 **4,503 == DB 注册 4,503**
- [x] `_orphan_verify.py 40` → **未落地 0／重复块 0／等级不符 0**（PASS）
- [x] `_scan_level_consistency.py` → 本组 **D／H／M 均 0 不符**
      （全库 M 不符 157 条经源库溯源：list23 147／list3 7／list2 3，**无一属 list40**）
- [x] `audit_evidence_level_labels.py` → **PASS**（错标／悬空 0）
- [x] `_scope_guard.py 40` → PASS
- [x] 块体独立终检：4,503 块“标记／抬头／空／正文／空”恰 5 行；抬头用词与等级匹配；
      无制表符／直角引号／行尾空白 —— **内容类异常 0**
- [x] **块后空行（N2）规整**：按 `_crossline_blank_20260918.md` 任务书执行
      `_fix_block_blanks.py --list 40 --write` → **132 宿主 624 处**（GLUE 39／EXTRA 585），
      git 实测 **+39 −1201**、**非空行零改动**；规整后 N2 异常归零。提交见 changelog id=1952
- [x] 账目：`long_task_state.json` 的 `usenet7.progress.by_list["40"]` 已由
      `read=19167`（>total，超 432）／`remaining=−432`／`excluded=0`／`frontier=172585`
      校正为 `read=18735`／`remaining=0`／`excluded=41`／`frontier=172543`／`status=CLOSED`；
      聚合同步为 已读 137131／剩余 31924／注册 31982／剩余段 80／81.12%

---

## 四、终验收口（**2026-09-18 已全部执行并通过**）

1. **全组复验**：`_orphan_verify.py 40` → **PASS**；逐段 `_verify_outline_landing.py`（47 段）→ **47/47 PASS**。
2. **块内一致性**：`_scan_level_consistency.py` → 本组 D／H／M **均 0 不符**。
3. **等级标注门禁**：`audit_evidence_level_labels.py` → **PASS**（错标／悬空 0）。
4. **账目同步**：`_progress_audit_7groups.py` 已刷新；
   `long_task_state.json` 的 `usenet7.progress.by_list["40"]` 已按审计真值校正（见 §3.4）。
5. **检查点**：`_RESUME.md` ＋ 状态机 ＋ 段台账 ＋ changelog（id=1952）已写入。
6. **提交**：N2 规整 132 文件已原子提交（见第七节 7.1 裹挟铁律）。

> **重跑提示**：只读判据（1／2／3）可随时重跑；**切勿重跑落地链**（`_land_seg.py`／`_closeout_batch.py`），
> 前者会重路由、后者虽已修但仍属无必要写入。

---

## 五、本组判据要点

- **判据唯一标尺**：`_REJUDGE_RULES_ng40_20260917.md`（L4→P1–P8；L3→N1–N6；DROP→D1–D8）。
- **任务书**：`TASK_NG40_unix_bsd_20260913.md`（**冲突时以任务书为准**）。
- **收率区间**：**11%–22%**；**严禁凑率**，偏离即如实回报并说明原因。
- 主题：BSD 主库 —— 4.x 谱系、内核与驱动、发行与移植。

---

## 六、🔴 硬约束

1. **块头证据等级必须从 DB 真值读**，严禁写死字面（门禁 `audit_evidence_level_labels.py`）。
2. **ROW_MINE 块 = 恰好 5 行**：标记 ＋ `**当事人自述**（证据等级：Lx，来源：…）` ＋ 空 ＋ 正文 ＋ 空；
   抬头用词与纪律串中段须按等级匹配（见 `_DRAFT_ROW_MINE_FORMAT_SPEC.md` 第四节）。
3. **机器块**（`_DRAFT_ROW_MINE_FORMAT_SPEC.md` 定义的各类非 `ROW_MINE` 机器块）
   **不得修改**，只能登记／DEFERRED。
4. 替换须**完整锚点 ＋ `count == 1` 断言**；禁止全字串替换；先 dry-run 再 write。
5. **禁止新建／移动／重命名源文件**；**不得**在 `08-核查报告与多轮复核/` 下新增 .md。
6. 格式：**UTF-8 无 BOM、LF、中文弯引号、禁直角引号**；路径／文件名加粗；手册页 `xx(N)` 加粗。
7. 撤块按 **pk 作用域**；**整文件覆盖前必先 diff 备份与现值、逐 pk 取并集**。

### 6.1 提交铁律（**裹挟核验**）
- `git commit -- <paths>` 提交的是这些路径的**工作区状态**（宿主 .md 内容不限于本批块）。
- **提交前逐文件核验**：① 删除行 == 0；② 新增 ROW_MINE 标记 pk 全属本批；
  ③ 每个非空新增行均为本批块抬头或本批摘要。**三条全过方可提交**。
- **判裹挟禁看暂存索引**，以写前备份（`script/_backup_ng40_s*_20260917/`）为基线。
- `git add` 与 `git commit` 必须**同一次调用内**；提交后 `git show --numstat` 复核**全部 `+N −0`**。
- Windows：`git add` 清单路径须**正斜杠**，清单以 `newline="\n"` 写。

---

## 七、🔴 已知坑（踩过，务必遵守）

| # | 坑 | 对策 |
|---:|---|---|
| 1 | **重跑 `_land_seg.py` 会重路由既有 pk** → 核验报“未落地”假 FAIL | 落块后必跑 `_mk_groups_from_map.py` 重建映射再复验 |
| 2 | `_closeout_batch.py` 重跑已收尾段曾**清空该段排除登记** | **已修**（按窗口保留 ＋ 按 (list, pk) 去重）；仍须核对本组条目数只增不减 |
| 3 | `_seg_dump.py` 的 `_hdr()` 换行未净化 → **pk 漏判** | **已修**；历史 heads 用 `_fix_heads_multiline_20260918.py` 重建 |
| 4 | 块插入行数**不是** `5×块数`（实测每块 7 行：标记／抬头／空／摘要＋纪律串／空／空／空） | 裹挟核验**不得**用“行数 == 5×块数”；用逐行归属核验 |
| 5 | register 二跑幂等 → MAPJSON 空 | claim_map 一律从 DB 四表 join 重建 |
| 6 | 跨会话 `claim_id` 抢号（`MAX(id)+1`） | 注册后立刻查 `claim_id`／`evidence_id` 是否重复 |
| 7 | `python -c` 内含**反引号** → bash 命令替换吞掉内容 | 含反引号／复杂 Markdown 的文本**一律写成脚本文件**执行 |
| 8 | 校验命令**接管道后再 `&&`** → 管道退出码覆盖 | 禁接管道 `&&` |
| 9 | `%`-格式化串裸 `%` | 写 `%%` |
| 10 | 子代理回报的“段号 ↔ pk”标注可能出错 | **以磁盘 TSV 与窗口真值为准** |
| 11 | `_progress_audit_7groups.py` 的“已读”按**连续前沿**计算 | 乱序落地会虚增；`long_task_state.json` 的 `read` 须按 `read = total − (pk_hi − frontier)` 校正 |

---

## 八、检查点纪律（每批收尾必做）

| 序 | 动作 | 落点 |
|---:|---|---|
| 1 | 刷新 `_RESUME.md`（本组段：当前状态、剩余工作、本会话已完成） | `script/_db_row_mining/_RESUME.md` |
| 2 | 更新状态机 `progress.by_list["40"]` | `long_task_state.json` |
| 3 | 确认段台账（`_staging_ng40_s<K>.md`）与 changelog 已写入 | 同目录 ／ `changelog.duckdb` |
| 4 | 归档治理／纠正计划到 `_applied/` | 同目录 |

**验证恢复性**：新会话只读 `_RESUME.md` ＋ 本文件即可知道“下一步做什么”，无须翻对话历史。

---

## 九、工具速查（list40 参数）

| 用途 | 命令 |
|---|---|
| 范围守卫 | `_scope_guard.py 40` |
| 进度真值（只读） | `_progress_audit_7groups.py` |
| 组配置＋宿主路由 | `_ngcfg.py` 的 `CFG[40]`（收率区间 11–22） |
| 段素材导出 | `_seg_dump.py 40 <lo> <hi> ng40_s<K>` |
| 输入表重建 | `_rejudge_seg.py 40 --seg K --lo LO --hi HI --dump` |
| 判读自检 | `_rejudge_seg.py 40 --seg K --lo LO --hi HI --check`（**只查 pk 覆盖与收率**） |
| **产出强化复核** | `_verify_tsv.py 40 K LO HI 11 22`（**查 C1–C5，含摘要长度与格式**） |
| 落地驱动 | `_land_seg.py 40 K LO HI 400 --write`（模板 `_register_ng40_s9_20260914.py`） |
| **映射重建（重跑 prep 后必做）** | `_mk_groups_from_map.py ng40_s<K> _groups_ng40_s<K>.json _targets_ng40_s<K>.json` |
| 入纲复验 | `_verify_outline_landing.py ng40_s<K>` |
| 收尾驱动 | `_closeout_batch.py 40 "K:lo:hi:400"` |
| 孤儿复验 | `_orphan_verify.py 40` |
| 块内一致性 | `_scan_level_consistency.py` |
| **heads 断行修复** | `_fix_heads_multiline_20260918.py 40 <lo> <hi> ng40_s<K>` |
| **提交前裹挟核验** | `_seg_commit_guard2_20260918.py` |

---

## 十、参考文档

- 判据总纲：`_GRADING_RUBRIC_20260914.md`（**§七 为现行口径**）
- **本组判据**：`_REJUDGE_RULES_ng40_20260917.md`
- **任务书**：`TASK_NG40_unix_bsd_20260913.md`
- 流程协议：`_SINGLE_ROUND_SOP.md`、`PLAN_ONEGROUP.md`
- 断点恢复：`_RESUME.md`（**接手第一件事读它**）
- 格式规范：`_DRAFT_ROW_MINE_FORMAT_SPEC.md`（**块体格式以此为准**）

---

**接手第一件事**：读 `_RESUME.md` → `_progress_audit_7groups.py` 核对本组真值 → `_scope_guard.py 40`。
**本组已收官**：第三节的“3 个漏判 pk”经复核**不成立**（勿执行原补正步骤）；第四节终验收口**已全部通过**。
本文件自此为**只读存档**；如需再动本组，先读 §3.4 的验收基线再决定。
