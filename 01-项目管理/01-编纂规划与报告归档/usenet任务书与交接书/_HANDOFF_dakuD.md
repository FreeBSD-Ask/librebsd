# 交接书 **dakuD** ｜ usenet 单库任务：**list44 · unix.bsd.openbsd.misc**（1983–2013）

**生成**：2026-09-18 23:05 ｜ **修订**：2026-09-18 23:10（**去除跨组叙述，本文件只涉本组**）
**任务范围**：**仅 list44（`unix.bsd.openbsd.misc`）** —— 本文件**自足**（自带现状真值、判据要点、流程、工具、验收），可单独开工
**口径真值**：`_progress_audit_7groups.py`（只读，2026-09-18 实测）
**本线性质**：**大库续读**，剩余 **80 段 / 31,924 头**

> **接手第一件事**：读 `_RESUME.md` → 跑 `_progress_audit_7groups.py` 核对本组真值 → 跑 `_scope_guard.py 44`。

---

## 一、任务边界

1. **本任务只负责 list44（`unix.bsd.openbsd.misc`）**。
2. **只读本组**：claim 注册、块落盘、`_excluded_pks.tsv` 追加、状态机更新，**一律只涉本组**。
3. **共享文件**（`_excluded_pks.tsv`、`long_task_state.json`、`_RESUME.md`）**改前先读**；
   **只追加／更新本组条目，不改动任何非本组条目**。
4. **宿主文件一律按“只增不撤”处理**；撤块必须限定本批 tag 与 pk 作用域。
5. 每批动手前后各跑 `_scope_guard.py 44`；越界即停并报告。**不回滚非本批改动**。
6. **不新建／不移动／不重命名任何源文件**。
7. ⚠️ `05-卷册大纲/` 可能存在**非本批**未提交改动
   → 提交必须严格按第七节 7.2 裹挟铁律执行。

---

## 二、本组现状真值（2026-09-18 实测）

| 项 | 值 |
|---|---|
| 新闻组 | `unix.bsd.openbsd.misc`（list_id = **44**） |
| pk 区间 | **186,609 – 235,328** |
| 年代 | 1983–2013（**OpenBSD 1995 年才 fork**，1995 年前帖须从严） |
| 总量 | **48,720 头** |
| 已读 | **16,796（34.47%）** |
| 剩余 | **31,924 头 ／ 80 段**（总段 122） |
| 前沿 | 203,400 |
| 注册 claim | **1,612** |
| 入纲块 | **1,612 == 注册**（不变式成立） |
| 孤儿 / 幽灵块 / 重复落地 | **0 / 0 / 0** |
| 等级分布 | L4 **486** ／ L3 **1,126** |
| 排除登记 | 258 条 |
| 段台账 / spec | **42 / 42**，无缺段 |
| 收率区间（本组） | **8%–18%**（`_ngcfg.py` 的 `CFG[44]`） |
| **下一段** | **s43 `[203405, 203804]`** |

### 2.1 已完成段（s1–s42，**勿重做**）
- **s1–s42 全部判读并落地**（changelog 见 `changelog.duckdb` 中 `list44 s<K> 续读` 条目）。
- 最近一轮（s18–s42，25 段）：落 **890 块**；`_orphan_verify.py 44` → **PASS**；
  逐段 `_verify_outline_landing.py` → **全 PASS**；各波幂等二跑 **+0**；
  内容抽验 42 条逐字回读原文，**问题率 0%**；已提交（commit `ed6f91dcb` 等）。

### 2.2 🔴 未完成（**接手即做**）

| 段 | 窗口 | 状态 | 处置 |
|---:|---|---|---|
| **s43** | `[203405, 203804]` | 判读件**不合格，已隔离** | 见 §2.3，**须重判** |
| **s44** | `[203805, 204204]` | **未产出** | **须判读** |

#### §2.3 s43 隔离件详情
隔离路径：`_rejudge_ng44_s43_20260917.tsv.BAD-20260918`（**勿直接使用、勿改后缀回用**）。
不合格项（`_verify_tsv.py` 实测 15 项）：
- **C1 含 UTF-8 BOM**
- **C2 行数 396 ≠ 输入表 400**，缺 pk **203405／203497／203614／203681**
- **C4 9 条摘要 82–98 字超 80 上限**（203408／203503／203514／203549／203573／203626／203627／203651／203689）

→ **处置**：删除隔离件，按第四节标准流程**从零重判 s43**（勿在隔离件上修补）。

---

## 三、本组判据要点

**判据唯一标尺**：`_REJUDGE_RULES_ng44_20260917.md`（L4→P1–P8；L3→N1–N6；DROP→D1–D8）。
**任务书**：`TASK_NG44_unix_bsd_openbsd_misc_20260913.md`（**冲突时以任务书为准**）。

`unix.bsd.openbsd.misc` = **OpenBSD misc（1983–2013）的一手现场**：安全、平台支持、社区与发布。

**优先抓**：
1. **安全工程**：pf 防火墙演进、全代码审计、漏洞发现与响应、pledge／unveil／W^X／malloc 加固
2. **发布与版本**：6 个月发布周期、release song、errata、版本升级与迁移现场
3. **加密与固件**：OpenSSH 的 fork 与普及、IPsec、随机数与熵、无线固件与二进制 blob 政策
4. **平台支持与驱动**：sparc／macppc／i386／amd64／arm 移植、无线与网卡驱动反向工程
5. **社区与治理**：邮件列表与 IRC 文化、deraadt 个人主导、committer 权限、基金会
6. **许可证与工具链**：IPFilter 许可争议、GCC GPLv3 与 pcc／clang 替代

**🔴 收率纪律**：
- 收率＝(L4+L3)/400，须落 **8%–18%**。
- **常规运维问答一律 D8**（细则 §四）：网卡配置、X 启动、pf 规则语法求助、包管理、编译报错……
  这类帖**话题虽在 OpenBSD 上，但与版本、规模、结论无关** → 一律不收。
  仅当**同时满足**“① 涉 OpenBSD 特有机制”＋“② 提供版本间行为差异／机制限制／规模数据的边际史料价值”才升 N6。
  **校准与边界以细则 §四为准**（细则载有该界线的量化依据）。
- **严禁凑率**：严禁为贴近区间而升降级；偏离即如实回报并说明原因
  （本组 s19 实测 **7.8%**，低于下限，已如实保留）。
- **1995 年前帖从严**（细则 §五.7）：项目尚未 fork，除非确与 OpenBSD 前身
  （NetBSD core team 冲突、de Raadt 被逐）直接相关，否则一律 **D7**。

---

## 四、每段标准作业流程（**7 步，逐段执行**）

```bash
cd /d/librebsd/script/_db_row_mining
PY="C:/Python314/python.exe"
K=<段号>; LO=<lo>; HI=<hi>

# ① 并发守卫（每波开工前）
git -C /d/librebsd log --oneline -5
$PY -c "import duckdb;c=duckdb.connect(r'D:\librebsd\04-现代研究文献\historical_claims.duckdb',read_only=True);print(c.execute(\"select count(*) from evidence where anchor='ng44_s$K'\").fetchone())"
#    返回 > 0 → 该段已被并发会话做过，跳过

# ② 输入表完整性自检（必做）
#    比对 review_logs/_rejudge_ng44_s<K>_input.txt 的 pk 集合与窗口 [LO,HI] 是否连续
#    若缺 pk → 先修 heads 再重建输入表：
$PY _fix_heads_multiline_20260918.py 44 $LO $HI ng44_s$K
$PY _rejudge_seg.py 44 --seg $K --lo $LO --hi $HI --dump     # 须“行数 400 缺 0 条”

# ③ 派子代理判读（同刻 ≤3 个；1 代理 2 段；25 分钟盒；只轮询禁 block 死等）
#    提示词须写明：读 _REJUDGE_RULES_ng44_20260917.md；大分块顺序通读 _ng44_s<K>_forread.txt
#    （Read limit=2000，约 7–9 次）；产出 _rejudge_ng44_s<K>_20260917.tsv；
#    内置 _verify_tsv.py 自检；严禁凑率；回报 ≤250 字。
#    产出格式：每行 4 列 TAB：<pk>\t<L4|L3|DROP>\t<理由类>\t<修订后一句话>
#              每段恰好 400 行、pk 升序；非 DROP 行摘要 30–80 汉字、无直角引号与星号；
#              DROP 行第 4 列留空（行尾仍须有 TAB）；UTF-8 无 BOM、LF。

# ④ 独立复核（不采信子代理自述）
$PY _verify_tsv.py 44 $K $LO $HI 8 18        # 须 C1–C5 全通过（exit 0）
#    并抽 3% 采纳行回读 forread 原文比对摘要

# ⑤ 落地
$PY _land_seg.py 44 $K $LO $HI 400 --write   # prep→register→claim_map→备份→落块→核验

# ⑥ 幂等与收尾
$PY _backfill_orphan_blocks.py ng44_s$K _groups_ng44_s$K.json _targets_ng44_s$K.json \
    review_logs/ng44_s${K}_spec.txt review_logs/ng44_s${K}_claim_map.json \
    --tag "2026-09-18 list44 unix.bsd.openbsd.misc 续读考据采纳"   # 须“总计拟插: 0 块”
$PY _closeout_batch.py 44 "$K:$LO:$HI:400"

# ⑦ 检查点（第八节）
```

### 4.1 🔴 若需对**已落地段**补判／返工
重跑 `_land_seg.py`（内含 `_prep_seg.py`）会因**容量感知重路由**既有 pk → 核验器按新宿主查而报**假 FAIL**。
**必做**：落块后立即重建映射再复验
```bash
$PY _mk_groups_from_map.py ng44_s$K _groups_ng44_s$K.json _targets_ng44_s$K.json
$PY _verify_outline_landing.py ng44_s$K
```

---

## 五、波次计划

- **粒度**：**1 代理 × 2 段**，**同刻 ≤3 个代理**（一次派 4 个会触发 API 并发数限制）。
- **每波 6 段**（3 代理 × 2 段）→ 80 段约 **14 波**。
- **窗口一律以 `review_logs/_rejudge_ng44_s<K>_input.txt` 与源库取真值**，勿沿用任何旧表
  （历史波次表与 400 网格存在偏移）。
- **素材已全部备齐**：`_ng44_s18_forread.txt` … `_ng44_s122_forread.txt`、`_ng44_s*_heads.txt`、
  `review_logs/_rejudge_ng44_s*_input.txt` **均在盘，免再 dump**
  （例外：s18／s19／s87／s88 的输入表已用修复版重建为 400 行，**s87／s88 判读前须确认其输入表为 400 行**）。

### 5.1 分段窗口真值（s43–s48，其余按输入表 `min/max` 取）

| 段 | 窗口 |
|---:|---|
| s43 | `[203405, 203804]` |
| s44 | `[203805, 204204]` |
| s45 | `[204205, 204604]` |
| s46 | `[204605, 205004]` |
| s47 | `[205005, 205404]` |
| s48 | `[205405, 205804]` |

---

## 六、验收标准（每波）

- [ ] 机械级：波内各段 `_verify_tsv.py` **C1–C5 全通过**
- [ ] 内容级：抽 3% 采纳行回读原文复核，**问题率 ≤ 5%**
- [ ] 落地：`_verify_outline_landing.py` **PASS**、幂等二跑 **+0**、逐 pk 核对 **0 缺失**
- [ ] 账目：`_orphan_verify.py 44` 报 **未落地 0／重复块 0／等级不符 0**
- [ ] 块内一致性：`_scan_level_consistency.py` 报 **D／H／M 三项本组均 0 不符**
- [ ] 范围：`_scope_guard.py 44` **硬检查通过**
- [ ] **检查点**：第八节四项**全部完成**

---

## 七、🔴 硬约束与已知坑

### 7.1 硬约束
1. **块头证据等级必须从 DB 真值读**，严禁写死字面（门禁 `audit_evidence_level_labels.py`）。
2. **ROW_MINE 块 = 恰好 5 行**：标记 ＋ `**当事人自述**（证据等级：Lx，来源：…）` ＋ 空 ＋ 正文 ＋ 空；
   抬头用词与纪律串中段须按等级匹配（见 `_DRAFT_ROW_MINE_FORMAT_SPEC.md` 第四节）。
3. **机器块**（`_DRAFT_ROW_MINE_FORMAT_SPEC.md` 定义的各类非 `ROW_MINE` 机器块）
   **不得修改**，只能登记／DEFERRED。
4. 替换须**完整锚点 ＋ `count == 1` 断言**；禁止全字串替换；先 dry-run 再 write。
5. **禁止新建／移动／重命名源文件**；**不得**在 `08-核查报告与多轮复核/` 下新增 .md。
6. 格式：**UTF-8 无 BOM、LF、中文弯引号、禁直角引号**；路径／文件名加粗；手册页 `xx(N)` 加粗。
7. 撤块按 **pk 作用域**；**整文件覆盖前必先 diff 备份与现值、逐 pk 取并集**。

### 7.2 提交铁律（**裹挟核验**）
- `git commit -- <paths>` 提交的是这些路径的**工作区状态**（宿主 .md 内容不限于本批块）。
- **提交前逐文件核验**：① 删除行 == 0；② 新增 ROW_MINE 标记 pk 全属本批；
  ③ 每个非空新增行均为本批块抬头或本批摘要。**三条全过方可提交**。
- **判裹挟禁看暂存索引**，以写前备份（`script/_backup_ng44_s*_20260917/`）为基线。
- `git add` 与 `git commit` 必须**同一次调用内**；提交后 `git show --numstat` 复核**全部 `+N −0`**。
- Windows：`git add` 清单路径须**正斜杠**，清单以 `newline="\n"` 写。
- 工具：`_seg_commit_guard2_20260918.py`（产出 `_commit_safe_20260918.txt`）。

### 7.3 已知坑（实测）

| # | 坑 | 对策 |
|---:|---|---|
| 1 | **重跑 `_land_seg.py` 会重路由既有 pk** → 核验假 FAIL | 落块后必跑 `_mk_groups_from_map.py` 再复验 |
| 2 | `_closeout_batch.py` 重跑已收尾段曾**清空该段排除登记** | **已修**（按窗口保留 ＋ 按 (list,pk) 去重）；仍须核对本组条目数只增不减 |
| 3 | `_seg_dump.py` 的 `_hdr()` 换行未净化 → **pk 静默漏判** | **已修**；历史 heads 用 `_fix_heads_multiline_20260918.py` 重建 |
| 4 | 块插入行数**不是** `5×块数`（实测每块 7 行：标记／抬头／空／摘要＋纪律串／空／空／空） | 裹挟核验**不得**用“行数 == 5×块数”；用逐行归属核验 |
| 5 | register 二跑幂等 → MAPJSON 空 | claim_map 一律从 DB 四表 join 重建 |
| 6 | 跨会话 `claim_id` 抢号（`MAX(id)+1`） | 注册后立刻查 `claim_id`／`evidence_id` 是否重复 |
| 7 | `python -c` 内含**反引号** → bash 命令替换吞掉内容 | 含反引号／复杂 Markdown 的文本**一律写成脚本文件**执行 |
| 8 | 校验命令**接管道后再 `&&`** → 管道退出码覆盖 | 禁接管道 `&&` |
| 9 | `%`-格式化串裸 `%` | 写 `%%` |
| 10 | 子代理回报的“段号 ↔ pk”标注可能出错 | **以磁盘 TSV 与窗口真值为准** |
| 11 | 子代理产出常见缺陷：**含 BOM**、**漏 pk**、**摘要超 80 字**（s43 实测 15 项） | 独立复核 `_verify_tsv.py` 是**唯一判据**，不采信自述 |
| 12 | 子代理派发可能遇 **502／并发限制** | 重试；超时 `TaskStop`；保留已 PASS 段，按缺段补派 |
| 13 | `_progress_audit_7groups.py` 的“已读”按**连续前沿**计算 | 乱序落地会虚增；`long_task_state.json` 的 `read` 须按 `read = total − (pk_hi − frontier)` 校正 |

---

## 八、检查点纪律（每波收尾必做）

| 序 | 动作 | 落点 |
|---:|---|---|
| 1 | 刷新 `_RESUME.md`（本组段：当前段号、下一波窗口、剩余段数、本会话已完成波次） | `script/_db_row_mining/_RESUME.md` |
| 2 | 更新状态机 `progress.by_list["44"]`（read／registered／frontier／segs_remaining） | `long_task_state.json` |
| 3 | 确认段台账（`_staging_ng44_s<K>.md`）与 changelog 已写入 | 同目录 ／ `changelog.duckdb` |
| 4 | 归档本波治理／纠正计划到 `_applied/` | 同目录 |

**验证恢复性**：新会话只读 `_RESUME.md` ＋ 本文件即可知道“下一步做什么”，无须翻对话历史。

---

## 九、工具速查（list44 参数）

| 用途 | 命令 |
|---|---|
| 范围守卫 | `_scope_guard.py 44` |
| 进度真值（只读） | `_progress_audit_7groups.py` |
| 组配置＋宿主路由 | `_ngcfg.py` 的 `CFG[44]`（收率区间 8–18） |
| 段素材导出 | `_seg_dump.py 44 <lo> <hi> ng44_s<K>` |
| 输入表重建 | `_rejudge_seg.py 44 --seg K --lo LO --hi HI --dump` |
| 判读自检 | `_rejudge_seg.py 44 --seg K --lo LO --hi HI --check`（**只查 pk 覆盖与收率**） |
| **产出强化复核** | `_verify_tsv.py 44 K LO HI 8 18`（**查 C1–C5，含摘要长度与格式**） |
| 落地驱动 | `_land_seg.py 44 K LO HI 400 --write`（模板 `_register_ng44_s17_20260914.py`） |
| **映射重建（重跑 prep 后必做）** | `_mk_groups_from_map.py ng44_s<K> _groups_ng44_s<K>.json _targets_ng44_s<K>.json` |
| 入纲复验 | `_verify_outline_landing.py ng44_s<K>` |
| 收尾驱动 | `_closeout_batch.py 44 "K:lo:hi:400"` |
| 孤儿复验 | `_orphan_verify.py 44` |
| 块内一致性 | `_scan_level_consistency.py` |
| **heads 断行修复** | `_fix_heads_multiline_20260918.py 44 <lo> <hi> ng44_s<K>` |
| **提交前裹挟核验** | `_seg_commit_guard2_20260918.py` |

---

## 十、参考文档

- 判据总纲：`_GRADING_RUBRIC_20260914.md`（**§七 为现行口径**）
- **本组判据**：`_REJUDGE_RULES_ng44_20260917.md`（**判读唯一标尺**）
- **任务书**：`TASK_NG44_unix_bsd_openbsd_misc_20260913.md`
- 流程协议：`_SINGLE_ROUND_SOP.md`、`PLAN_ONEGROUP.md`
- 断点恢复：`_RESUME.md`（**接手第一件事读它**）
- 格式规范：`_DRAFT_ROW_MINE_FORMAT_SPEC.md`（**块体格式以此为准**）

---

**接手第一件事**：读 `_RESUME.md` → `_progress_audit_7groups.py` 核对本组真值 → `_scope_guard.py 44`
→ **删除 s43 隔离件并重判 s43，再判 s44** → 按第四节逐段推进 → **每波末做第八节检查点**。
