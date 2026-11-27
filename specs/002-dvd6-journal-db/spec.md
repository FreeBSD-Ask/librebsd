# Feature Specification: dvd6 期刊四库建库 → 全文库入库 → 入大纲

**Feature Branch**: `002-dvd6-journal-db`

**Created**: 2026-10-05

**Status**: Draft

**Input**: User description: "首先阅读claude.md。遍历 D:\librebsd\dvd6\Website\source。按期刊名称分别建立若干数据库（4个，图片中的代码、文字LLM直接转，不是文字图，是艺术图的话直接base64，禁止使用本地模型转）。4个数据库（使用duckdb）放在 ddj 文件夹（自行创建）。无需记录文件的路径等无用内容，仅记录期刊时间、作者、名称等元数据和正文等有意义的内容。广告也必须存储。按规则遍历上述数据库，入放到全文数据库，然后入大纲。不计成本代价。源码包也入库（禁止二进制入库，必须解压后跟随文章在数据库单独关联文本代码）"

## 源材料实测（2026-10-05 侦察，作为规格事实基础）

`D:\librebsd\dvd6\Website\` 为 "Dr. Dobb's Developer Library DVD-ROM Release 6" 网站镜像。两棵内容树：

- **`source/`** —— 随刊源码压缩档，按期打包：
  - `CUJ/`（C/C++ Users Journal）：年份目录 1990–2006，年内按月 zip（jan90.zip…），月包内嵌**每作者 zip**（如 `saks.zip`、`plauger.zip`），两层嵌套；
  - `DDJ/`（Dr. Dobb's Journal）：年 zip（1988.zip…2009.zip），包内按期目录（9001、9002…）存放每作者 `.asc`/`.lst` 源码文件、`NNNN.htm` 说明页、`readme.txt`，并混有 `.exe`/`.scr`/`.DS_Store` 等二进制；
  - `SA/`（Sys Admin）：年份目录 1992–2006，年内按月 `.tar`；
  - `TPJ/`（The Perl Journal）：按期 `tpjNNNN_source.zip`/`.tgz`（如 tpj0302_source.tgz）；
  - `images/`：站点导航图片（bg10.gif、cover.jpg 等）。
- **`articles/`** —— 文章 HTML 页：
  - `DDJ/年份/期号/`（如 1990/9001/）：每文一目录一 HTML（如 `9001a/9001a.htm`），含 `META year`、TITLE（含月份）、`h1` 题名、`h2` 副题、`h3` 作者、作者简介、正文全文；期目录有 `NNNNtoc.htm` 目录页（栏目分节 FEATURES/…、每文含署名与摘要）；
  - `CUJ/年份/期号/`：每文一作者名目录（如 `plauger/`、`saks/`），含 `toc*.htm` 目录页与 `newprod`（新产品栏）、`letters`（读者来信）、`edforum`（编者论坛）等栏目；
  - `TPJ/年份/volN_M/`：每文一编号 HTML（如 `tpj0101-0001.html`），期目录含 `images/` 子目录（`.gif`/`.jpg` 图表、汉字字形图等）与 `ewtoc.html` 目录页；
  - `SA/vNN/iN/`：每文 `aN.htm` 加随文清单页 `aN_lN.htm`/`aN_sN.htm`，另有 `resource/` 与框架页（border/navbar/tree/main.htm）。

## User Scenarios & Testing *(mandatory)*

### User Story 1 - 按期刊建立 4 个 DuckDB（Priority: P1）

主理人需要把 DVD 上四份期刊（DDJ、CUJ、SA、TPJ）的全部有意义内容变成可检索的结构化数据：新建 `ddj` 文件夹，按期刊名称各建一个 DuckDB 数据库（共 4 个）。遍历 `dvd6/Website/source` 与 `dvd6/Website/articles` 两棵树：文章页的元数据（期刊时间、作者、题名、栏目）与正文全文、目录页、读者来信/编者论坛/新产品等栏目、广告，全部入库；随刊源码包必须解压，文本代码逐文件入库并按期、按文章关联；图片中的代码与文字由 LLM 直接读图转写入库（禁止使用本地 OCR/转录模型），纯艺术图以 base64 存库；禁止任何二进制文件入库；不记录文件路径等无意义内容。

**Why this priority**: 四库是后续全文入库与入大纲的唯一数据源，没有库则一切后续工作无从谈起。

**Independent Test**: 打开 4 个数据库，按期号/年份统计文章数、正文数、代码文件数、广告数、图片处理数，与磁盘实测期号清单对照，即可独立验收。

**Acceptance Scenarios**:

1. **Given** 四库建成，**When** 按 4 个期刊名查询库清单，**Then** 恰好 4 个 DuckDB，库名与期刊一一对应，全部位于 `ddj` 文件夹内。
2. **Given** 任一期（抽样），**When** 比对库内文章数与 `articles/` 该期目录实测文章目录数，**Then** 数量一致且无遗漏文章。
3. **Given** 任一期源码包（抽样），**When** 解压并列出文本文件，**Then** 库内存在逐文件对应的代码文本行，且与解压内容逐字一致，并关联到正确期号/文章。
4. **Given** 全库任意一行文本内容，**When** 检索二进制特征（`.exe`/`.scr`/`.DS_Store` 等二进制内容、压缩包原始字节），**Then** 不存在任何二进制内容入库。
5. **Given** 任一含代码/文字的图片（抽样），**When** 查其处理记录，**Then** 有 LLM 直转的文字/代码文本入库且未调用本地模型；任一艺术图（抽样）有 base64 入库。

---

### User Story 2 - 按 references_fulltext 规则补齐四库（Priority: P2）

四库装满后，按 references_fulltext 数据库的既有规则（概述、著录、原料层）补齐：每篇 article 一条 GB/T 7714 著录（refs 表，文献综述原料）、一条中文概述（summaries 表：3–6 句＋关键词＋原文摘引）、原子事实入 key_facts（reference_id 指向本库 refs）。**不写 references_fulltext.duckdb**——四库本身即本批内容的全文库（主理人 2026-10-05 修正）。

**Why this priority**: 概述与著录是把“装满数据的库”升格为“可支撑编纂引用的全文库”的规则要件；大纲两层依赖 refs 与 key_facts。

**Independent Test**: 每库 refs/summaries/key_facts 三表与 articles 计数闭合，ref 0 悬空；抽样概述与正文相符；幂等重跑 0 新增。

**Acceptance Scenarios**:

1. **Given** 补齐完成，**When** 按库查 refs/summaries/key_facts 行数，**Then** 三表与 articles 闭合（refs=articles；summaries 无缺行；key_facts.reference_id 全部回指本库 refs）。
2. **Given** 抽样 12 篇概述，**When** 与 body_text 人工比对，**Then** 概述内容相符且含 topic_keywords 与原文摘引。
3. **Given** 重跑补齐脚本，**When** 比对前后，**Then** 0 新增 0 重复（幂等）。

---

### User Story 3 - 入大纲（授权两层）（Priority: P3）

全文入库后，按既有授权把本批文献落入大纲两层：`key_facts` 原料层与各卷 `卷末书目述评.md` 书目述评层（bullet 体例、幂等判据按既有规则）；**成稿正文层（SUMMARY/章正文）禁止写入**。全部写盘走 write_guard（UTF-8 无 BOM、LF），写后跑大纲相关门禁。

**Why this priority**: 大纲层是内容最终可被编纂引用的落点，但依赖前两层完成。

**Independent Test**: 查 key_facts 新增行数与 `卷末书目述评.md` 新增 bullet 数，逐条核对 ref 号存在且著录非空；重跑幂等。

**Acceptance Scenarios**:

1. **Given** 入大纲完成，**When** 检索新 bullet 的 ref 号，**Then** 均在 references 全文库有非空著录（不悬空）。
2. **Given** 重跑入大纲脚本，**When** 比对前后，**Then** 0 重复追加（has_block 幂等）。
3. **Given** 写盘完成，**When** 跑大纲门禁（lint、证据等级、目录页相关件如触及），**Then** 全绿。

---

### Edge Cases

- 嵌套压缩包：CUJ 月包内嵌作者 zip；DDJ 年包内 `noland.zip` 等内嵌 zip——必须递归解压至文本层，嵌套包不作为独立记录单位，其内容随期/文章关联。
- 二进制混入：`.exe`/`.scr`/`.DS_Store`/字体等二进制一律不入库（内容与原始字节都不存）；文章正文文字里提及的可执行文件名（如 "contains the following executables: RAHNER.EXE"）属正文，随正文自然保留。
- 编码混杂：DOS 时代源码可能含 OEM/CP437/latin-1 字节、制表符、CR/LF 差异——解码后统一 UTF-8 文本入库，保留代码文本原貌（不重排、不改字），仅行结构与编码归一。
- 图片判别：图表/代码截图/含文字扫描件与 logo/装饰图/照片混在同目录——判别错误会把文字内容当艺术图（丢内容）或把艺术图当文字（编造）。判别以实际读图为准，存疑挂账不猜。
- 整页广告：可能为纯图片广告或 HTML 文字广告，也可能二者混排——图片广告按图片规则（文字转写/艺术图 base64），HTML 广告按文本入库。
- 站点壳件：框架页（forms/、tree.htm、navbar.htm、border.htm）、搜索工具（zoom/）、`readme`/`.old` 残留件（如 `tpj0101-0004.html.old`）——壳件不入文章库；`.old` 残留件不重复入库（以正身 HTML 为准）。
- SA 的随文清单页（`aN_lN.htm`）：其内容本质是清单/代码，应并入对应文章的代码或正文，不得当作独立文章重复著录。
- DDJ 部分年份无 articles 树对应（articles/DDJ 实测至 2002 年）或 source 包与文章页期号不对齐——以磁盘实测为准逐期核对，缺失侧如实记录，不臆造补齐。
- 期刊时间口径：TITLE 内月份缩写（JAN90、jan92.tar）与目录页月份并存——入库时归一为年/月/期号结构化字段，保留原文题名不改。

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: 系统 MUST 按期刊名称建立恰好 4 个 DuckDB 数据库（DDJ、CUJ、SA、TPJ 各一），不得合并、不得多建；建库期间置于本会话宿主真本地目录 `C:\ddj_stage\`（主理人 2026-10-05 令：D: 为网络映射不算本地），全部完成并核验后推送至 `dvd6/Website/ddj/`（推送后双侧字节级比对）。
- **FR-002**: 系统 MUST 遍历 `dvd6/Website/source` 全部压缩档（zip/tgz/tar，含嵌套压缩）与 `dvd6/Website/articles` 全部文章页/目录页/栏目页，无遗漏、无跳过。
- **FR-003**: 每篇文章 MUST 记录元数据：期刊名称、年、月/期号、文章题名、副题（如有）、作者、作者简介（如有）、栏目/类型（FEATURES/COLUMNS/LETTERS/NEW PRODUCTS 等与 TOC 分节一致）；MUST NOT 记录文件路径、站点框架、导航等无意义内容。
- **FR-004**: 文章正文 MUST 以文本形式全文入库（HTML 转文本保留标题层级与段落结构）；目录页、编者论坛、读者来信、新产品栏等栏目内容一并入库；正文照录不改字。
- **FR-005**: 广告 MUST 存储：文字类广告按文本入库，图片类广告按图片规则（FR-007）处理；每条广告可归属到期号。
- **FR-006**: 源码包 MUST 解压后入库：文本代码/文档逐文件以文本存储，并至少与期号关联、能关联到文章的关联到文章；**禁止二进制入库**（可执行文件、对象文件、压缩包原始字节等一律不入库）。
- **FR-007**: 图片 MUST 逐件处置：含代码/文字的图片由 LLM 直接读图转写为文本入库（**禁止使用本地 OCR/转录模型**）；纯艺术图（logo、装饰、照片、封面）以 base64 存库；每件图片的处理方式可查。
- **FR-008**: 四库 MUST 按 references_fulltext 数据库的既有规则补齐三件套（主理人 2026-10-05 修正：四库本身即全文库，**不再写入 references_fulltext.duckdb**）：①`summaries` 概述表（每 article 一条：中文概述＋topic_keywords＋important_excerpts，schema 同 references_fulltext.summaries）；②`refs` 著录表（每 article 一条 GB/T 7714 期刊著录，作为文献综述原料）；③`key_facts` 原料层表（schema 同 references_fulltext.key_facts，reference_id 指向本库 refs）。
- **FR-009**: 补齐完成后 MUST 按授权两层入大纲：各卷 `卷末书目述评.md` 书目述评层＋key_facts 的 related_chapter 归属；新增 bullet 的 ref 锚点采用 `<DB>-<refs.id>` 限定格式（如 `ref DDJ-1027`，指向四库 refs——偏离既有 `ref NNNN` 体系，已报请主理人确认）；禁止写成稿正文层；写盘统一走 write_guard（UTF-8 无 BOM、LF、幂等 has_block）。
- **FR-010**: 全链路 MUST 幂等：四库重建重跑、全文库重跑、大纲重跑均 0 新增 0 重复；写前有判据、写后有独立回读断言（不信任脚本自述）。
- **FR-011**: 成本豁免：本件按“不计成本、不计代价”最高规则执行——子代理数量、复核轮数、逐字比对面不设上限；但每步仍须遵守 0 信任原则与三次复查流程。

### Key Entities *(include if feature involves data)*

- **journal（期刊）**: DDJ / CUJ / SA / TPJ 四刊之一；属性＝刊名、全称、年份覆盖范围。
- **issue（期）**: 某刊某年某月一期；属性＝年、月、期号、目录页内容；一刊物多期，一期多文。
- **article（文章）**: 一篇文章；属性＝题名、副题、作者、作者简介、栏目、正文文本、TOC 摘要；关联期与源码文件、图片。
- **source_file（源码文件）**: 解压后的一个文本代码/文档文件；属性＝文件名（含内嵌包层级）、文本内容；关联期与文章。
- **advertisement（广告）**: 一条广告；属性＝文本内容或图片处理产物；关联期。
- **figure（图片件）**: 一件图片；属性＝判别结果（含文字/代码 → 转写文本；艺术图 → base64）、处理记录；关联期/文章。
- **fulltext 条目**: 全文库侧 references 著录 + fulltext_blocks 块 + 留痕行。
- **大纲两层落点**: key_facts 行（原料层）与 卷末书目述评 bullet（书目述评层）。

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 4 个 DuckDB 建成且全部位于 `ddj` 文件夹；每库期号覆盖与磁盘实测清单一致（DDJ 1988–2009 年包、CUJ 1990–2006、SA 1992–2006、TPJ 全部 `tpjNNNN` 包），期数零遗漏。
- **SC-002**: 抽样 ≥12 期（每刊 ≥3 期），库内文章数、正文文本、代码文件、广告、图片处理与磁盘实测逐项一致；抽样正文与源页面/解压文件逐字一致。
- **SC-003**: 全库二进制检查 0 命中（无二进制内容入库）；无文件路径类无意义字段。
- **SC-004**: 图片件 100% 有处置记录（转写文本或 base64 二选一，含处理方式标记），无“既无转写也无 base64”的悬空图片。
- **SC-005**: `references_fulltext.duckdb` 新增著录、全文块、留痕三者对应闭合；抽样块文与四库源行逐字一致；幂等重跑 0 新增。
- **SC-006**: 大纲两层落账：key_facts 新增行与书目述评新增 bullet 全部 ref 可回指全文库著录（0 悬空）；幂等重跑 0 重复；大纲门禁全绿。
- **SC-007**: 全程留痕可审计：每批操作有记录、每条目可追溯到源（期号/文章/文件级）。

## Assumptions

- `ddj` 文件夹位置＝`D:\librebsd\dvd6\Website\ddj\`（与 `source/` 同级，数据贴源存放；主理人仅指定文件夹名“ddj”并授权自行创建）。
- “二进制不入库”的口径＝二进制内容与原始字节均不入库；文中自然提及的可执行文件名（正文文字的一部分）不受此限。
- 广告的分布以实测为准（TOC 页、栏目页、图片），实施时先侦察样刊再定判别与抽取规则，不预设格式。
- SA 的 `aN_lN.htm` 清单页并入对应文章处理；框架/搜索壳件不入库。
- 全文库与大纲的既有规则、门禁、幂等机制（write_guard、WO-007、证据等级门禁等）全部适用，本件不新立与之冲突的规则。
- TPJ 的 `.old` 残留件、DDJ 的 `.DS_Store` 等站点残渣按 Edge Cases 处置，不计入内容。
