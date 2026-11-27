# Research: dvd6 期刊四库建库 → 全文库入库 → 入大纲

**Feature**: specs/002-dvd6-journal-db | **Date**: 2026-10-05

规格阶段无遗留 [NEEDS CLARIFICATION]；本文件固化实施层决策（Decision / Rationale / Alternatives），并汇总本项目已验证的工程纪律，供后续任务直接引用。

## R1. 库位置与推送（2026-10-05 主理人两度修正后）

- **Decision**: 四库建在会话宿主真本地目录 `C:\ddj_stage\`（库名 ddj/cuj/sa/tpj.duckdb）；全部完成并核验后整体推送到 `\\DESKTOP-M5P610N\d\librebsd\dvd6\Website\ddj\`（推送后双侧字节级比对）。**本会话宿主的 D: 是指向远端共享的网络映射，不是本地盘**——已实测并据此把先建的 `D:\ddj_stage`（实为远端）迁回 C 盘并删除。
- **Rationale**: DuckDB 建库写入要吃本地盘速度与稳定性；UNC/映射路径的读缓存幽灵（listdir 假象、Write 静默失败）在万人级文件写入场景不可接受；“最后推送”把 SMB 风险压缩到一次可校验的复制。
- **Alternatives**: 直接写 D:\librebsd\dvd6\Website\ddj（过 SMB，弃）；写 UNC（同，弃）。

## R2. 文章 HTML → 文本转换

- **Decision**: 自写 stdlib `html.parser` 剥取器：`h1/h2/h3/h4` 转 Markdown 级标题（`#`…），`<p>`/`<br>`/`<hr>` 保段落边界，`<i>/<b>/<pre>/<code>` 去壳保字，实体（`&quot;` 等）解码；`META`（year 等）、`TITLE`、TOC 链接结构单独解析进元数据；`<img>` 记占位符交给图片处置流。
- **Rationale**: 四刊页面各自形态固定（DDJ 每文一目录、CUJ 作者目录、TPJ 编号 html、SA `aN.htm`+`aN_lN.htm`），规则可枚举；照录不改字（不重排、不改字、不合并段落）。
- **Alternatives**:BeautifulSoup/lxml（非 stdlib，UNC 环境尽量少依赖，弃）；整页正则替换（跨期形态漂移时脆，弃）。

## R3. 嵌套压缩档解压

- **Decision**: stdlib `zipfile`/`tarfile` 递归解压到 `%TEMP%` 工作区（从 `os.environ["TEMP"]` 派生，bash `$TEMP` 是 `/tmp` 不用）：外层包（年 zip / 月 zip / 期 tar / 期 zip-tgz）→ 内层作者 zip → 文本文件层。解压链路层级记入 `source_files.archive_layer`（如 `CUJ/1990/jan90.zip + saks.zip`），完整磁盘路径不入库。`.exe`/`.scr`/`.com`/`.obj`/`.lib`/`.dll`/图像/字体/`.DS_Store` 等按扩展名＋magic 头双判为二进制，不入库（连字节都不存）。
- **Rationale**: 实测 DDJ 年包内嵌作者 zip、CUJ 月包内每作者 zip；“解压后跟随文章关联文本代码”要求展开到文本叶子；层级标签是溯源所需的最小元数据（非文件路径）。
- **Alternatives**: 原地解压到 dvd6（污染只读输入树，弃）；入库存压缩包字节（用户明令禁止二进制，弃）。

## R4. 文本编码

- **Decision**: 解码顺序 `utf-8 → utf-8-sig → cp437（DOS 源码）→ latin-1`（latin-1 永不失败作兜底），检出编码记入 `source_files.encoding`；入库统一 UTF-8。行尾统一 LF（注意 bash 重定向会带 CR——写文件用 Write 工具或脚本）。
- **Rationale**: DOS 时代 `.asc/.lst` 源码多为 ASCII＋偶尔 CP437 图形字符；latin-1 兜底保证零崩溃；不引第三方检测库。
- **Alternatives**: chardet（第三方且误判率不优于显式序，弃）。

## R5. 图片处置（核心纪律）

- **Decision**: 三分处置，逐件留痕于 `figures` 表：
  1. **含代码/文字的图**（图表、代码截图、含文字扫描件、表格图）→ 会话内子代理 LLM 用 Read 工具直读图片转写为文本入库（`disposition='transcribed'`）；**禁止本地 OCR/转录模型**；
  2. **纯艺术图**（logo、装饰、照片、封面、图标）→ `disposition='base64'`，base64 正文入库（`base64_data`）；
  3. **导航壳图**（bg10.gif、open/closed.gif 等站点 chrome）→ `disposition='skipped'`，理由＝站点壳件非内容（记名不留内容，便于审计零悬空）。
  判别以实读为准；判别存疑者挂账 `disposition='uncertain'` 待复核，不猜。
- **Rationale**: 用户明令“图片中的代码、文字 LLM 直接转；艺术图 base64；禁本地模型”；壳件若全量 base64 会污染库（无意义内容）。
- **Alternatives**: 全部 base64（违背“LLM 直转文字”要求，弃）；全部转写（艺术图转写＝编造风险，弃）。

## R6. 广告识别与存储

- **Decision**: 实施第一批次先做**广告侦察**（每刊抽 2–3 期全页通读，定位广告载体：TOC 页广告栏、newprod 类栏目、独立广告 HTML、整页图片广告），产出每刊广告判别规则后全量抽取；文字广告入 `ads.ad_text`，图片广告按 R5 处置并挂 `ads.figure_id`。侦察结论写入本期 spec 目录 `research.md` 追记。
- **Rationale**: 广告形态未实测（规格明示“以实测为准，不预设格式”）；先侦察后全量可避免以偏概全。
- **Alternatives**: 一次性正则抓 "ad" 关键字（期刊正文亦含 ad 字样，误报，弃）。

## R7. 按 references_fulltext 规则补齐四库（2026-10-05 主理人修正：替代原“全文库对接”）

- **Decision**: **不再向 references_fulltext.duckdb 写任何行**（该库当日已有他会话在写 DDJ 单篇，亦证内容另入只会重复）。四库按其既有规则补齐三件套：①`refs` 著录表——每 article 一条 GB/T 7714 期刊著录（作者. 题名[J]. 刊名, 年(期).），作文献综述原料；②`summaries` 概述表——schema 同 references_fulltext.summaries（id/reference_id/summary/topic_keywords/important_excerpts/processing_status/processed_at），每 article 一条中文概述＋原文摘引；③`key_facts` 原料层——schema 同其 12 列，reference_id 指向本库 refs，id 用 `kf-<db>-<ref>-<seq>` 体例。
- **Rationale**: 主理人明示“全文库已经在 ddj，不需要重复入 references_fulltext”；概述/著录/原料层是可编纂引用的规则要件，照搬既有 schema 使四库与项目库体系同构。
- **Alternatives**: 仍建 references/fulltext_blocks 行（用户明令删除，弃）；著录-only 写 references_fulltext（仍触碰该库且与他线碰撞，弃）。

## R8. 入大纲两层（Phase C）

- **Decision**: 只写授权两层：① `key_facts`（原料层，ref 关联、extracted_at 真实时间戳）；② 各对应卷 `卷末书目述评.md` 追加 bullet（判据匹配 `- **ref NNNN**｜` bullet 形式；宿主末节不一定是追加位置，体例跟宿主实测走）；卷归属按期刊主题（DDJ/CUJ→编程技术与工具生态相关卷、SA→系统管理、TPJ→Perl/脚本生态；归属落点在实施时对照重构2026 目录 54 卷定，并记入核查记录）。写盘统一 `write_guard()`（UTF-8 无 BOM、LF、has_block 幂等）；写后跑大纲门禁（lint、证据等级、磁盘层术语件）。
- **Rationale**: 授权层裁定（_TASKBOOK_INGEST_OUTLINE_20260929 §1.3）＝key_facts＋书目述评两层，成稿正文层禁止；bullet 形式判据是防“裸号误判已存在”的实测教训。
- **Alternatives**: 写 SUMMARY/章正文（明令禁止，弃）；新建锚点体例（REF_FULLTEXT: 未授权，弃）。

## R9. 并行与派单

- **Decision**: 40 路滚动在途常设授权（一路终态立即补位；读手与叙述手混流）；子代理只做转录/抽取类批量工作，主会话负责派单、验盘、合并、入库。**判死前必验盘**（死代理可能已落盘）；产物可信、回报不可信（第五次以上坐实），一切以磁盘回读为准；分件落盘永不重派。
- **Rationale**: 主理人 2026-09-29 常设授权＋本项目“回报叙述不可信”系列教训。
- **Alternatives**: 单线程主会话自做（万级文件不现实，弃）；CreateWorkflow 动态工作流（T1 战役授权明令禁用工作流工具，弃）。

## R10. 已验证工程纪律（本件强制引用）

1. **UNC 双身份**：Write/Edit 用 Windows 反斜杠 UNC 路径（POSIX `/d/...` 路径静默失败）；PowerShell 走 D: 映射；读缓存可能陈旧须多读法交叉；`listdir` 幽灵条目按精确路径 `os.stat` 复核；UNC 上禁内联 `python -c`/heredoc 写 UNC——一律写脚本文件再跑。
2. **DuckDB 写侧**：`at` 等保留字加引号；未显式开事务则逐条自动提交（脚本必须幂等，重跑不重复写）；写连接未关时只读连接直接 Fatal——**写与验分两个进程**。
3. **假绿防护**：对空集合的 `all()` 恒真——先断言非空；`list.count(子串)`/集合差分/difflib 配对各有系统误差；校验命令先在磁盘跑通再派单；每条判据独立成变量独立打印。
4. **落盘验证**：脚本自述≠落盘内容；写后必须独立回读断言（间隔 2 秒双读）；UNC Write 超时≠失败，验盘再定。
5. **并发**：references/claim 库会被他会话持锁——退避重试不杀进程；共享台账提交前 `git log`+逐库 diff 披露夹带；提交 pathspec 限定＋`--no-gpg-sign`（主理人授权）。
6. **编码**：Write 会把字面 BOM 归一化（检测脚本用 `chr(0xfeff)`）；Edit 可能把整文件转 CRLF；`head -c` 截断多字节显示假乱码。
7. **文本 grep 盲区**：库内 VARCHAR 文本 grep 零命中≠不存在；自增 id≠业务键。
