# 镜像站批量挖掘与 OCR 流水线规则

本文件汇总 FreeBSD 历史书编纂项目中**历史镜像站/档案馆批量挖掘、扫描件 OCR、全文索引入库**的流程与规范，源自 SFU PUPS（www.vector.comm.sfu.ca/pups/）完全挖掘工程（963 文件 2.5 GB、18 组入库、944 条文件级记录、830 PDF 全文覆盖）。凡涉及镜像站抓取、批量下载、OCR、全文索引的工作应逐条对照本文件执行。

## 1 镜像站挖掘流程

### 1.1 探查与规划

- **目录级探查**：先取站点根目录与各级子目录索引页（`curl -sL <dir>/` 后 grep `href=`），摸清目录树与内容类型，再规划下载批次。勿直接盲目全站爬取。
- **区分内容类型**：技术报告（CSTR）、内部备忘录（Tech Memos）、邮件存档（mbox/html）、口述史（mp3/epub/转录）、手册（Manuals）、通讯（Newsletters）、论文（Papers）、光盘索引（非 ISO）等，按类型规划存储位置与处理方式。
- **识别子目录陷阱**：索引页显示的链接可能指向子目录（如 MERT 手册的 Green/Red/White Tabs 是子目录而非文件），应递归探查；PDF 链接可能指向其他目录的重复引用，解析时应去重。
- **明确跳过清单**：用户明确要求不下载的内容（如系统 ISO/发行版镜像 Distribution/PDP-11/VAX/4BSD 等）应在规划时列出并全程避开；光盘类只取索引文件（ls/md5sums/目录清单）不取镜像本体。

### 1.2 批量下载

- **优先 curl**：历史镜像站（如 SFU）可能拒绝 Python urllib/requests 请求（脚本静默失败），**curl 带浏览器 UA 最稳**。
- **限流应对**：连续快速请求会被站点限流（循环下载到一半静默失败/返回 502/000）。对策：
  - 每文件多 try 重试（3-6 次），失败 `rm` 后重下
  - 文件间间隔 3-5 秒（`sleep` 命令不可用时用 Python `time.sleep` 或下载循环的自然间隔）
  - 大文件（>20 MB）应 `curl --max-time 300-500`，且放后台任务跑
- **断点续跑**：下载脚本应幂等——已存在且校验通过的文件跳过（`[ -s file ]` 或 `os.path.getsize` 判断）。
- **文件名含空格**：Bash 循环应引号包裹；校验时用 Python（bash 循环会把含空格文件名拆词误报）。

### 1.3 文件完整性校验

- **PDF 校验**：所有 PDF 应检查 `%PDF` 文件头（`head -c 4 file` 或 Python `read(4)`）。
- **损坏文件检测**：`fitz.open()` 后检查 `len(doc)`——**0 页但文件有大小 = 下载不完整的损坏 PDF**，应从源站重新下载；重下后的版本可能是完整且有文本层的（如 SFU 的 AUUGN-V05.4 重下后 110 页含文本层），勿直接放弃。
- **批量校验用 Python**：遍历全部文件逐个读文件头，避免 bash 空格文件名误报。
- **AppleDouble 隐藏文件**：镜像目录常含 `._` 前缀的 AppleDouble 元数据文件（macOS 产物），**不是真实文档**，下载/统计/OCR 时一律过滤（`fn.startswith("._")`），否则会浪费大量重试时间（实测过滤后 504 文件 6 分钟完成 vs 未过滤 2 小时）。

## 2 OCR 流水线规则

### 2.1 引擎选择

- **首选 Tesseract**：按流程规则“OCR 后处理”小节执行（`tesseract <input> <output> -l eng+chi_sim+fra+deu --psm 1`，输出 md 至 `ocr/` 目录）。
- **RapidOCR 替代**：当 Tesseract 无法安装（winget/choco 权限受限、静默安装被拒）时，改用 **RapidOCR**（`rapidocr_onnxruntime`，纯 Python + onnxruntime，清华镜像 `-i https://pypi.tuna.tsinghua.edu.cn/simple` 安装，模型自动下载）。识别质量对英文印刷体良好。
- **流水线参数**：pymupdf 渲染 200-250dpi → RapidOCR 识别 → 输出 `ocr/<原文件名>.md`。实测：200dpi 速度快且质量可接受；每页 5-25 秒（取决于扫描质量），110 页大文件需 1 小时+，勿因 md 产出间隔长误判卡死。

### 2.2 文本层优先原则（关键）

**先检测文本层，有则直接用，无才 OCR**：

- 矢量 PDF（MERT man 页、PWB 手册、部分重下文件等）**自带文本层**，用 pymupdf 提取（`doc[i].get_text()`，全页合计 >100 字符判定有文本层），质量远高于 OCR，且 `ocr_status=verified`。
- 纯扫描件（AUUGN、USENIX 早期通讯、516-TSS、32V 等）才需 OCR，`ocr_status=needs_review`。
- 实测 SFU_PUPS 830 个 PDF 中约一半有文本层无需 OCR；**入库时文本层优先，OCR 结果作复核材料**。
- 注意：OCR 脚本的“无文本层”判定与入库脚本应一致（均用“全页提取 > 阈值”），否则出现入库判定差异。

### 2.3 并行与断点

- **多进程并行**：单进程 OCR 浪费 CPU 核数（16 核机器单进程 7 分钟 0 产出），用 8 进程（大文件阶段降为 2-4 进程防内存竞争）。每文件在独立子进程/subprocess 中运行，崩溃不影响主流程。
- **独立 worker 文件**：worker 逻辑写入独立 `.py` 文件（`_ocr_worker_fill.py`），用 `subprocess.Popen([sys.executable, worker, pdf, ocr_dir])` 调用——**避免 Bash 内联 Python 的引号转义问题**（`\"` 破坏语法是 Bash heredoc/内联的已知坑，一律写独立 .py 文件）。
- **幂等断点**：已生成 `ocr/*.md`（>200 字节）的文件跳过；0 字节 md 视为失败，应重跑。
- **活跃度判断**：后台 OCR 任务跨会话后任务 ID 可能失效，判断是否存活看①进程列表大内存 worker（>200 MB）②临时目录渲染 PNG 时间戳（每 20-40 秒一张 = 活跃）。**勿仅凭 md 数量不增长判断卡死**——大文件单 md 间隔 10-15 分钟正常。

### 2.4 质量分级与失败处理

- **抽样核对**：按考据规则抽样（每 100 页抽 5 页比对），错讹率 <5% 标 `verified`，≥5% 标 `needs_review`；低质量油印扫描（如 1975 年 USENIX 特刊，1 页模糊照片）识别内容几乎全错时，标记无效并**检索其他转载格式代替**（官方重印本/二手文献转录），不强行入库。
- **入库阈值**：OCR md <200 字节视为无效（可能 0 页损坏或全噪声）；有效 md 才写入 fulltext。
- **失败不阻塞**：单文件 OCR 失败（损坏 PDF、超大文件崩溃）记录后继续，不中断整个批次；后续统一补漏重跑。

## 3 索引入库规范（references_fulltext.duckdb）

### 3.1 组记录与文件级记录双轨

- **组记录**（如 `SFU_PUPS_AUUGN_125期`）：整组索引，`file_path` 指向组目录，**不写 fulltext**（设计预期，勿当作缺失）。
- **文件级记录**：每个文件独立 references + fulltext + fulltext_blocks + ocr_status，符合 2026-08 `_44doc_fulltext.py` 既有范式（该脚本未留存，见 §5 留存状态）。文件级记录是检索主体。

### 3.2 入库脚本要求

- **幂等**：以 `filename` 已存在集合防重，重跑安全（新增/已存在/无文本 三计数）。
- **文本来源优先级**：原生文本（htm/txt/mbox）→ 文本层 PDF（pymupdf_textlayer）→ OCR md（rapidocr_onnx）→ 无文本（no_text 计数，不建记录）。
- **字段**：filename/format/ocr_status + fulltext(content/char_count/extraction_method) + fulltext_blocks 段落块（para_split 按空行切块）。
- **入库存量**：无文本层且无 OCR 的文件不建记录（等 OCR 完成后重跑脚本补齐），避免大量空壳记录。

### 3.3 大纲回写

- **卷末书目述评追加**：各卷卷末书目述评章目录 `05-卷册大纲/第NN卷-<slug>/第N章-卷末书目述评/`（N＝卷内章号）追加“SFU PUPS 存档增补”小节（GB/T 7714 著录 + ref id）。
- **增量安全**：幂等判断**不应使用“整个小节已存在则跳过”**（会漏掉增量记录）——改为“小节已存在则删除旧小节重建”（述评增补是脚本生成的，重建安全）。实测漏增量教训：537 条时小节已存在导致后续 13 条新增未写入。

## 4 经验教训汇总（SFU PUPS 工程）

1. **Bash 环境坑**：内联 Python heredoc 有转义 bug（`\"` 破坏语法）→ 一律独立 .py 文件；MuPDF 错误输出到 stderr 导致 Bash 误报 exit 1（实际正常）→ `fitz.TOOLS.mupdf_display_errors(False)` 抑制 + 以日志文件为准；重定向日志被缓冲看不到进度 → print 加 `flush=True`。
2. **数据库锁**：多轮入库脚本残留 python 进程会占锁（database is locked）→ 结束残留 python 进程（tasklist 确认后 Stop-Process）释放锁。
3. **后台任务跨会话**：任务 ID 失效后靠进程/文件时间戳判断；大工程分多轮，每轮完成入库+日志，最后统一收尾。
4. **先小样本验证**：批量 OCR/入库前先跑 2-3 个样本验证链路（渲染→识别→入库），确认无误再全量。
5. **统计口径**：`os.path.exists` 只查根目录会漏子目录文件（误报未落地）——统计应 `os.walk` 全盘；文件级记录数查询应排除组记录。

## 5 相关脚本（script/，以 SFU 工程为范本）

**留存状态（2026-10-22 审计）**：本节脚本为 2026-08 SFU PUPS 执行期脚本，当前未在 `script/` 或 `脚本与命令/` 留存；本表保留方法叙述，不表示可直接执行。需复跑时按本规则重建，并在 `脚本与命令/README.md` 缺失脚本登记中更新。

| 脚本 | 用途 |
| ---- | ---- |
| `_sfu_dl_batch*.py` / `_sfu_dl_mert_full.py` | 镜像站批量下载（多 try 重试 + 间隔 + 幂等） |
| `_sfu_ocr_parallel.py` | 8 进程并行 OCR 主流水线（pymupdf 渲染 + RapidOCR） |
| `_sfu_ocr_fill*.py` / `_ocr_worker_fill.py` | 补漏 OCR + 单文件 worker（subprocess 隔离） |
| `_sfu_file_ingest_v5.py` | 文件级入库（幂等，文本层/OCR 优先级） |
| `_sfu_outline_backfill.py` | 大纲回写（已存在则重建，增量安全） |
| `_wait_ocr_done.py` | OCR 完成轮询（幂等退出） |

## 6 TUHS Wiki 全量抓取与独立库（2026-10-25 立）

本节登记 `wiki.tuhs.org`（Unix Heritage Wiki，DokuWiki）全量语料的抓取、归一、入库与复核口径。语料库为 `03-原始史料库/16-TUHS-Wiki史料/tuhs_wiki.duckdb`（DuckDB 2.0.0，存储 `v2.0.0+`），Schema 见 `脚本与命令/tuhs_wiki_schema.sql`。

### 6.1 范围与清单

- **页面范围**：14 个命名空间（systems／source／features／events／people／anecdotes／images／glossary／publications／misc／wiki／blog／playground／refnotes）及其子命名空间，另加顶层页 `start`、`syste`；2026-10-25 实测去重基线 **232 页**（230 命名空间页＋2 顶层页）。
- **清单真值**：以 `?do=index&idx=<ns>` 递归派生（处理 `&s=` 分页），去重后的页面 ID 集合为唯一口径；逐命名空间计数与集合 SHA-256 写入 `crawl_runs.scope_json`，不应以各命名空间计数之和充当总数。
- **外链范围**：页面直接引用的站外链接**只抓一跳**，不递归外站；同一归一 URL 只抓一次。

### 6.2 二进制禁令与 Markdown 归一

- **不应二进制正文入库**：语料目录内除 `tuhs_wiki.duckdb` 外，文件扩展名只允许 `.md`／`.wikitext`；不落 `.html`／`.pdf`／`.epub`／压缩包等。图片为唯一潜在例外，默认只登记 URL 不下载；确需本体应用户逐批明示并落 `raw/media/`。
- **Wiki 页**：`export_raw` 取 Wikitext，按纯文本落 `.wikitext`（保真源）；`export_xhtml` 仅内存用于链接抽取与转换，**不落 HTML**；两者统一转 Markdown 落 `.md`，库内 `fulltext.content` 即 Markdown。
- **外链页**：HTML 去导航后转 Markdown；PDF 只下载到 `script/` 临时目录，pymupdf 文本层或 RapidOCR 转 Markdown 后删除 PDF 本体；`text/plain` 直通。
- **排除对象**：电子书格式、书名 PDF（>20 MB）、源码压缩包／`utree.pl`／raw 直链、图片音视频、登录／编辑／feed 等动作 URL，一律只登记 `excluded_items`，不下载、不计入抓取失败。
- **失效回退**：外链 404／410／5xx／超时先查 Wayback `available`，有快照取 `id_` 原始件并记 `fetch_mode='wayback'`。

### 6.3 入库与幂等

- 每页恰 1 条 `fulltext`（失败／延迟页写空内容行）、1 条 `conversions` 主记录；块级结构入 `fulltext_blocks`（含 `heading_path`）。
- 自然键：wiki＝`page_key`（DokuWiki 页面 ID 原样），external＝`canonical_url`；先查后写／`MERGE`，`id` 动态取 `max+1`，重复运行不产生重复行；内容变化写 `update_log`。
- 溯源字段：`pages.url`／`fetched_at`／`sha256_source`（原始响应字节）／`sha256_markdown`（落盘 md）／`conversions.converter_version`。

### 6.4 验证与复核（V1–V12）

抓取后应两套验证器各跑一遍，并做第三轮人工抽样：

| 编号 | 判据 | 执行件 |
| ---- | ---- | ------ |
| V1 | 页面清单守恒（重派生＝基线＝库内 wiki 页集合；逐命名空间计数一致） | 主验证器／SQL 复核器 |
| V2 | 双形态落盘与哈希（`.wikitext`／`.md` 存在；md 哈希一致；wiki 源哈希可重算） | 主验证器／SQL 复核器 |
| V3 | Markdown 覆盖（每页 1 条 fulltext；非空页有块；无 HTML 标签残留） | 主验证器／SQL 复核器 |
| V4 | 外链闭合（外链集合＝抓取行∪排除台账∪失败行∪延迟行） | 主验证器／SQL 复核器 |
| V5 | 键与去重（page_key／块键／外链归一 URL／转换键重复为零） | 主验证器／SQL 复核器 |
| V6 | 原文抽样（30 wiki 页源哈希一致；10 外链页变化只记 `changed_since_crawl`） | 主验证器 |
| V7 | 运行时／存储版本、表与约束、无 BLOB | 主验证器 |
| V8 | `EXPORT`→`IMPORT` 可恢复性（11 表行数相等） | 主验证器 |
| V9 | wiki 二跑幂等（数据表行数不增、页面集合不变） | 主验证器 |
| V10 | 二进制禁入（扩展名白名单＋文件头魔数扫描为零） | 主验证器／SQL 复核器 |
| V11 | 转换保真（30 页标题／链接／代码块差异为零；表格行数 wiki 为零、外链 HTML 按“绝对差 ≤ max(2, 20% 源行数)”容差；布局表折叠的标题层级丢失记 INFO；warnings 逐条披露） | 主验证器 |
| V12 | 转换台账（每页 conversions 行；版本与 md 哈希一致） | 主验证器／SQL 复核器 |

- **第一轮**：`verify_tuhs_wiki.py` 全量 V1–V12，结果写 `verification`（round `R1`）。
- **第二轮**：`verify_tuhs_wiki_sql.py` 以独立 SQL 复算 V1–V5／V10／V12（round `R2SQL`），不复用主验证器判据代码；两轮结论不一致即判 FAIL。
- **第三轮**：人工抽样 30 页（覆盖 14 个命名空间，含 ≥5 个外链页），逐字比对源站／外链源与库内 Markdown，抽样清单附报告附录。

### 6.5 执行件与登记

- 抓取器：`脚本与命令/tuhs_wiki_crawl.py`；主验证器：`脚本与命令/verify_tuhs_wiki.py`；独立复核器：`脚本与命令/verify_tuhs_wiki_sql.py`；Schema：`脚本与命令/tuhs_wiki_schema.sql`。
- 库路径登记于 `流程规则.md`“功能数据库唯一真值路径与空壳防治”；备份纳入 `backup_databases.py` SCOPE（28 库）；登记簿与看板同步 `11-元数据接口/09-文件夹数据库索引/`。
