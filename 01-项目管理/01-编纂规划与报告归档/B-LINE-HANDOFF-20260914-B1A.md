# B 线交接文档 · B1 方案 A 执行（COL_SCAN 块改造）

> 交接日期：2026-09-14
> 仓库：`D:\librebsd`
> 适用对象：接手的 AI 执行者（本文档**自包含**，无需前序会话上下文）
> 上游背景文档（可选读）：`B-LINE-HANDOFF-20260914.md`、`script/_outline_audit_20260906/_bline_20260914/B-LINE-REMEDIATION-PLAN.md`

---

## 0. 一句话任务

把 `05-卷册大纲/` 下 **260 个仍为旧形态的 `COL_SCAN` 机器块**，逐章改写为“**本章关联文献（人工判定）**”；
未被采纳的候选**先尝试重新映射**，实在无法映射的**存入专用 duckdb 库**，最后**再尝试映射一次（不勉强）**。

---

## 1. 背景与当前状态

### 1.1 什么是 COL_SCAN 块

`05-卷册大纲/` 各章 `概述.md` 内嵌一类自动生成的机器块，标记为：

```
<!-- COL_SCAN v20260826 -->
## 内容包复核增补（Phase 4 · 2026-08-26）
...
```

**问题**：该块由“全局关键词扫描”生成（`script/_col_scan/fix1_augment.py`），抽样实测**错配率 80%**——
取回的证据点与所在章节主题普遍无关。经 4 轮原型 + 3 种度量指标验证，
**“用全局关键词扫描生成章节级证据点”的设计前提本身不成立**，任何排序/取数调整都无法把相关性提到可用水平。

**已批准的方案 A**：改变块的性质——从“证据点扫描”改为“**关联文献目录**”，
直接消费 `references_fulltext.chapter_matches`（文献级映射），并**逐条人工判定**取舍。

### 1.2 当前进度

| 项 | 数量 |
|---|---|
| 大纲 md 总数 | 3247 |
| 含 `COL_SCAN` 块 | 283 |
| **已转换为新形态**（`v20260914-lit`） | **23**（试点 3 + 批次 01R 20） |
| **待转换**（旧形态 `v20260826`） | **260** |
| 覆盖率（报告登记） | 2925/2925 = 100% |

### 1.3 已完成的新形态章

- 试点：ch165、ch236、ch254
- 批次 01R：ch1–ch20（报告 `A16_b1a_01R.md`）
- 报告：`A16_b1a_01.md`（**已作废**，误用偏移）、`A16_b1a_01R.md`（有效）

---

## 2. ⚠️ 最关键：章号偏移（必读，弄错则整批白做）

`references_fulltext.chapter_matches.primary_chapter` **用的是旧章号**，与磁盘章号存在 **+1 偏移**。

**映射关系**：`磁盘章号 = 旧章号 + 1` ⟹ **`旧章号 = 磁盘章号 − 1`**

因此，**取磁盘 ch N 的候选，必须查 `primary_chapter = N−1`**，而不是 `N`。

### 2.1 三重证据（已核实）

**① 数据库自述**：各章 `DB_POINTS:chapter_reviews` 块头写明
> “本章（第 9 章 …，2026-08-12 重排后为磁盘第 10 章，**旧章号 +1 映射**）”
> “**映射：旧章号 +1 → 磁盘章号**”

**② 六处完美匹配**（磁盘章主题 ↔ `primary_chapter = N−1` 的候选标题）：

| 磁盘章 | 章标题 | `primary_chapter = N−1` 的候选 | 判定 |
|---|---|---|---|
| 15 | 早期编程语言与 c 语言诞生 | `The Development of the C Language` | ✅ |
| 16 | cpp-shell 家族与脚本语言生态 | `A History of C++: 1979-1991` | ✅ |
| 236 | dragonflybsd 的习俗特殊文化考据 | `DragonFly BSD customs and culture` | ✅ |
| 237 | nextstep 的起源 bsd 走进 next | `NeXTSTEP/OPENSTEP history` | ✅ |
| 253 | macos 的 bsd 哲学史观审视 | `macOS BSD philosophy: historical perspective` | ✅ |
| 254 | 失败衍生版本与开源治理批评 | `FreeBSD derivatives: failures and governance` | ✅ |

**③ 数据驱动验证**：对 d ∈ {−3..+3} 逐卷计算“磁盘章标题 ↔ `primary_chapter = N+d` 候选标题”的相似度，
**d = −1 在 12/19 卷显著最优**（如第13卷 0.124 vs d=0 的 0.011，差 11 倍）。

### 2.2 两种章号形态

`primary_chapter` 有两种取值形态，**取数时必须两式都查**：

| 形态 | 例 | 含义 |
|---|---|---|
| **数字** | `'235'`、`'14'` | **旧章号** → 属磁盘 ch = 数字 + 1 |
| **`CH` 前缀** | `'CH18'`、`'CH97'` | **磁盘章号**（用现行编号，**不加偏移**） |
| `NULL` / 空白 | — | **无法映射** → 存入 duckdb 存档库（见 §4） |

> `CH` 形态已由 `CH97` → 磁盘 ch97“freebsd-foundation”↔ 候选 `616: FreeBSD Foundation Interview` 验证。

**因此取数 SQL 必须写**：
```sql
WHERE m.primary_chapter IN ('<N-1>', 'CH<N>')
```

### 2.3 反例（务必避免）

- ❌ 用 `primary_chapter = N` 取数 → 会拿到**下一章**的候选（批次 01 首轮即因此使 ch14–ch20 全部零采纳）
- ❌ 把 `match_confidence` 高低当作相关性依据 → 实测 `podcast_bsdnow_outline_mappings` 置信度 **1.0** 的 114 条播客候选
  与所在章**完全无关**，全部剔除
- ❌ 机械重跑 `fix1_augment.py` → **明令禁止**

---

## 3. 铁律（违反即返工）

1. **禁止机械重跑**：不得运行 `fix1_augment.py` 或任何批量生成脚本。必须**逐章手工判定**。
2. **只改 COL_SCAN 块区间**，块外内容一字不动。
   - 块区间定义：`<!-- COL_SCAN` 行 → 块自身首行 `## ` → **第二个 `## ` 标题** 或下一 `<!-- ` 标记 或 EOF。
   - ⚠️ 只取“第一个 `## `”会切掉块体，必错。
3. **不得改 `SUMMARY.md`**；**不得动其他机器块**（`DB_REF`/`DEEP_ANALYSIS`/`DB_POINTS`/`PODCAST_REVIEW`/`MAIL_INSIGHT`/`ROW_MINE` 等）。
4. **不得新建/移动/重命名源文件**。
5. 格式：UTF-8 **无 BOM**、**LF**、中文弯引号、**禁用直角引号 `“”“”`**；路径/文件名加粗；代码块/版本号/哈希不可篡改。
6. **写前重读做乐观并发校验**（本库有并发会话持续写入）；内容不一致则跳过并记录。
7. **不改 `references_fulltext.duckdb`**（只读）；需要落库的走 §4 的专用存档库。

---

## 4. 未被采纳候选的三段处置（用户指令，必须执行）

对每一章，凡**判定为不采纳**的候选，不得简单丢弃，须依次走完三段：

### 第 1 段 · 重新映射（必须尝试）

对每条未采纳候选，尝试重新归属到正确章节：

1. 取其 `title`（必要时加 `author`/`year`），与**全库 355 个章标题**做关键词匹配打分
   （建议：英文按词、中文按字，去停用词后算 Jaccard；章标题可从目录名 `第<N>章-<标题>` 取）。
2. **唯一高分命中**（且分数显著高于次高）→ 判定归属该章：
   - 若该章尚未处理 → 作为该章候选纳入其判定流程；
   - 若该章已处理 → 追加到该章块内“未采纳候选（留痕）”并标注 `重映射归属：第 N 章`。
3. **多义或低分** → 进入第 2 段。

### 第 2 段 · 存入专用 duckdb 存档库

无法映射的候选**必须入库**：

```
库路径：D:\librebsd\script\_outline_audit_20260906\_bline_20260914\_b1a_unmapped.duckdb
表    ：unmapped_candidates
```

**表结构（已建好，417 行初始数据已装入）**：

| 字段 | 说明 |
|---|---|
| `id` | 候选 id（源自 `chapter_matches.id`） |
| `primary_chapter_raw` | 原始 `primary_chapter`（可能为 NULL/空白） |
| `match_source` / `match_confidence` / `match_reasoning` | 原始匹配元数据 |
| `title` / `author` / `year` / `language` / `summary_md_path` | 题录 |
| `origin_disk_chapter` | 在哪一章被剔除（无归属时留空） |
| `reject_reason` | 剔除理由 |
| `remap_round1` / `remap_round1_result` | 第 1 段重映射的尝试方式与结果 |
| `remap_round2` / `remap_round2_result` | 第 3 段二次映射的尝试方式与结果 |
| `final_status` | 见下 |
| `note` | 备注 |

**`final_status` 取值**：
- `UNMAPPED_NO_CHAPTER` —— 无章归属且重映射失败（**保留此标记，不勉强**）
- `REMAPPED` —— 重映射成功（已写入对应章，可移出或留档）

**追加语句示例**：
```python
import duckdb
con = duckdb.connect(r"D:\librebsd\script\_outline_audit_20260906\_bline_20260914\_b1a_unmapped.duckdb")
con.execute("INSERT INTO unmapped_candidates VALUES (" + ",".join(["?"]*18) + ")",
            [id, pc_raw, src, conf, reason, title, author, year, lang, mdpath,
             origin_ch, reject_reason, r1, r1res, r2, r2res, "UNMAPPED_NO_CHAPTER", note])
```

### 第 3 段 · 最后再尝试映射一次（不勉强）

全部批次完成后，对存档库做**最后一轮**映射尝试：

1. 放宽阈值（允许次高分命中、允许按 `summary_md_path` 路径线索、允许按作者/年份交叉）。
2. 成功者：写回对应章块 → `final_status='REMAPPED'` + `remap_round2_result` 记录依据。
3. 仍失败者：**保持 `UNMAPPED_NO_CHAPTER`，不再尝试**，并在此库中永久留档。

> **“不勉强”的含义**：宁可留档为未映射，也不要为了清空而强行归属。归属必须有可复述的依据。

---

## 5. 块模板（逐字使用）

### 5.1 有采纳项

```
<!-- COL_SCAN v20260914-lit -->
## 本章关联文献（人工判定）

> 数据源：`references_fulltext.chapter_matches`（文献级映射）。本节由**逐条人工判定**产生，不作段落级证据抽取。
> 章号映射：库内 `primary_chapter` 为旧章号，已按“旧章号 +1 → 磁盘章号”取数（本章取 `primary_chapter = {N-1}` 与 `CH{N}`）。
> 候选 {N} 条 → 采纳 {M} 条。

| # | 文献 | 作者 | 年份 | 来源 | 采纳理由 |
| --- | --- | --- | --- | --- | --- |
| 1 | *标题* | 作者 | 年份 | match_source | 与本章主题的关联（一句话） |

### 未采纳候选（留痕）

- **<分组理由>**：`标题`（作者, 年份）、… —— K 条。
```

### 5.2 零采纳

```
<!-- COL_SCAN v20260914-lit -->
## 本章关联文献（人工判定）

> 数据源：`references_fulltext.chapter_matches`（文献级映射）。本节由**逐条人工判定**产生。
> 章号映射：已按“旧章号 +1 → 磁盘章号”取数（本章取 `primary_chapter = {N-1}` 与 `CH{N}`）。
> 候选 {N} 条 → 采纳 **0** 条。

**结论：本章无可采纳的关联文献。** <一句话说明候选为何全部不相关>

### 未采纳候选（留痕）

- `标题`（作者, 年份；match_source=…, 置信度 …）—— 剔除理由…
```

### 5.3 无候选

```
<!-- COL_SCAN v20260914-lit -->
## 本章关联文献（人工判定）

> 数据源：`references_fulltext.chapter_matches`（文献级映射）。
> 本章在库内无候选记录（已按 `primary_chapter = {N-1}` 与 `CH{N}` 两式查证），故本节无可采纳项；关联文献需另行采集。
```

---

## 6. 剩余批次执行清单

批次清单已生成（TSV 三列：**章号 TAB 源文件相对路径(相对 `05-卷册大纲/`) TAB 章标题**），
位于 `D:\librebsd\script\_outline_audit_20260906\_bline_20260914\`：

| 批次文件 | 章数 | 章号范围 | 状态 |
|---|---|---|---|
| `_b1a_01.txt` | 20 | 1–20 | ✅ 已完成（见 `A16_b1a_01R.md`） |
| `_b1a_02.txt` | 20 | 21–41 | ⬜ **待办** |
| `_b1a_03.txt` | 20 | 42–66 | ⬜ 待办 |
| `_b1a_04.txt` | 20 | 67–90 | ⬜ 待办 |
| `_b1a_05.txt` | 20 | 91–116 | ⬜ 待办 |
| `_b1a_06.txt` | 20 | 117–137 | ⬜ 待办 |
| `_b1a_07.txt` | 20 | 138–157 | ⬜ 待办 |
| `_b1a_08.txt` | 20 | 158–182 | ⬜ 待办 |
| `_b1a_09.txt` | 20 | 183–209 | ⬜ 待办 |
| `_b1a_10.txt` | 20 | 210–242 | ⬜ 待办 |
| `_b1a_11.txt` | 20 | 243–267 | ⬜ 待办 |
| `_b1a_12.txt` | 20 | 268–293 | ⬜ 待办 |
| `_b1a_13.txt` | 20 | 294–322 | ⬜ 待办 |
| `_b1a_14.txt` | 15 | 323–350 | ⬜ 待办 |

> 注：批次按报告路径字符串排序切分，故 `第01卷` 的 ch1–20 在第 01 批。**已完成批次勿重做**。
> 每批完成后须产出报告 `A16_b1a_<批号>.md`（逐章：章号/标题/候选数/采纳数/剔除分组/块行数变化/入库条数）。

---

## 7. 工具与路径速查

### 7.1 数据源（只读）

```
references_fulltext.duckdb
  D:\librebsd\04-现代研究文献\05-参考文献全文数据库\references_fulltext.duckdb
  表 chapter_matches：id, reference_id, primary_volume, primary_chapter,
                       secondary_chapters, match_reasoning, match_confidence, match_source
  表 references     ：id, title, author, year, publisher, language, source_tier, summary_md_path
```

**必须用系统 Python**（托管 Python 无 duckdb）：
```
C:/Python314/python.exe
```

### 7.2 取候选（模板命令）

```bash
C:/Python314/python.exe -c "import duckdb;con=duckdb.connect(r'D:/librebsd/04-现代研究文献/05-参考文献全文数据库/references_fulltext.duckdb',read_only=True);[print(r) for r in con.execute(\"select m.match_source,m.match_confidence,m.match_reasoning,r.title,r.author,r.year,r.language from chapter_matches m left join \\\"references\\\" r on r.id=m.reference_id where m.primary_chapter in (?,?) order by m.match_source\").fetchall()]"
```
把两个 `?` 换成 `'<N-1>'` 与 `'CH<N>'`。

### 7.3 判据与基线（**统计/修复脚本必须 import**）

```
script/_outline_audit_20260906/_bline_20260914/_criteria.py          # 判据唯一来源（v2）
script/_outline_audit_20260906/_bline_20260914/_criteria_selftest.py # 45 断言自测
script/_outline_audit_20260906/_bline_20260914/_baseline_v2.py       # 基线（两次运行须逐字节一致）
```

关键接口：
- `_criteria.iter_scoped(path, rel)` → 逐行产出 `(rel, lineno, line, scope)`；
  `scope` ∈ `code`/`marker`/`comment`/`dbline`/`block`/`quote`/`prose`
- `_criteria.MODIFIABLE_SCOPES = ('prose',)` —— **只有 `prose` 可改**
- `_criteria.colscan_region(lines)` → COL_SCAN 块的 `(start, end)`（**务必用它，勿自实现**）

### 7.4 存档库

```
D:\librebsd\script\_outline_audit_20260906\_bline_20260914\_b1a_unmapped.duckdb
  表 unmapped_candidates（417 行初始数据）
```

### 7.5 相关脚本（参考实现，可复用）

| 脚本 | 用途 |
|---|---|
| `_b1a_batches.py` | 生成批次清单 |
| `_b1a_offset.py` | 逐卷确定章号偏移（数据驱动） |
| `_b1a_pilot.py` | 试点 3 章的实现（含块替换逻辑） |
| `_b1a_make_unmapped_db.py` | 建存档库 |
| `_b1a_archive_unmapped.py` | 导出不可映射候选为 md/tsv |
| `_verify_bline_20260914.py` | 覆盖率核查（须保持 2925/2925） |

---

## 8. 其他遗留专项（不在 B1 范围内，供参考）

接手 B1 时**不要**顺手改这些，它们各有专项：

| 专项 | 规模 | 说明 |
|---|---|---|
| 伪标签重挂 | 软件工程 228 处 / 技术路线分化 285 处 | **仅 3 文件 6 处 / 7 文件 8 处有报告处方**，其余无处方不得改 |
| 旧路径迁移 | `原材料/` 1508 次 | `哲学/项目统摄史观/第 NN 章.md` → `sacred_sources.duckdb`（`files` 表 id=NN+1）；已改 23 文件 155 处 |
| 直角引号 | 残留 2751 字符 / 171 文件 | 报告范围外 514 行需新报告覆盖 |
| 其他 6 类机器块重跑 | DEEP_ANALYSIS 23456 / ROW_MINE 24558 等 | **仅 PODCAST_REVIEW 可只读重跑**；DB_POINTS 无生成器 |
| `plan.json` 锚点 | 424 条已重定位 | 生成期缺陷（锚点文本与行号取自不同快照） |
| 块类型 | 实测 **25+ 种** | 边界判定用“任何行首 `<!--`” |
| `remove_all_deep_analysis.py` | 已修 | 原实现会误删 120,114 行 / 1,276 文件 |

---

## 9. 坑与反例（血泪）

1. **章号偏移**：见 §2。这是本次最容易踩且代价最大的坑。
2. **块区间**：COL_SCAN 的块体从标记行延伸到“**第二个** `## ` 标题”。用第一个会切掉整块内容。
3. **`match_confidence` 不可信**：1.0 也可能是机械关键词匹配产物（BSD Now 播客 114 条即为例证）。
4. **`git commit --pathspec-from-file` 遇含空格路径会按空格切分** → 必须配 `--pathspec-file-nul`，
   且清单用 `git diff --name-only -z` 生成；**不要**解析 `git diff` 的 `+++ b/…` 行。
5. **`core.autocrlf=true`** → CRLF 改动在 `git diff` 中不可见。
6. **并发写入**：本库有多个会话同时写入，工作区会在数分钟内由脏变净；判断是否落盘须以**文件内容**为准。
7. **“前后对比”类验收会被并发写入污染**：必须在**同一份内容快照**上做 A/B（见 `_isolate_criteria_v1v2.py`）。
8. **子代理报的数字必须自查**：本工程已实测 4 处子代理数字被推翻（如 `原材料/` 报 2359 实为 1508）。
9. **bash/grep 输出中文可能显示为乱码，但文件本身是合法 UTF-8**——不要据此转码。

---

## 10. 验收门（每批完成后必跑）

| 门 | 指标 |
|---|---|
| G1 | 该批全部章的 COL_SCAN 块标记已变为 `<!-- COL_SCAN v20260914-lit -->` |
| G2 | 块外内容与改前**逐行一致**（建议用 `HEAD` 版本比对） |
| G3 | 旧形态残留：`grep -rl "COL_SCAN v20260826" 05-卷册大纲/ \| wc -l` 递减 |
| G4 | 覆盖率仍为 **2925/2925 = 100%**（`_verify_bline_20260914.py`） |
| G5 | 该批未采纳候选：已尝试重映射，失败者已入 `_b1a_unmapped.duckdb` |
| G6 | UTF-8 无 BOM、LF；无直角引号；`SUMMARY.md` 与其他机器块零改动 |

**提交要求**：**路径限定**（只提交本批改动的 `概述.md`），不提交 `SUMMARY.md`、不提交无关并发改动。
建议提交信息格式：
```
B1 方案 A 批次 <NN>：COL_SCAN 块改为“本章关联文献（人工判定）”（<K> 章）
- 章号映射：primary_chapter = N-1 与 CH<N> 两式取数
- 候选 <A> 条 → 采纳 <B> 条；零采纳 <C> 章；入存档库 <D> 条
```

---

## 11. 建议执行顺序

1. **先跑一遍 `_criteria_selftest.py`**（应 45 断言全过）确认环境。
2. 按批次 02 → 14 顺序执行（**可并行派子代理，一批一代理**）。
3. 每批完成后立即：跑验收门 → 入库未采纳候选 → 路径限定提交 → 出报告。
4. **全部批次完成后**，执行 §4 第 3 段：对存档库做最后一轮映射尝试（不勉强）。
5. 最终统计：`v20260914-lit` 块数应为 283（或说明差异原因）。

> 有疑问时以本仓库既有实践为准：`script/_outline_audit_20260906/_bline_20260914/B-LINE-STATUS-20260914-r1..r6.md`
> 记录了逐轮方法与踩坑过程。
