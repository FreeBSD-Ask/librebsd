# 镜像站批量挖掘与 OCR 流水线规则

本文件汇总 FreeBSD 历史书编纂项目中**历史镜像站/档案馆批量挖掘、扫描件 OCR、全文索引入库**的流程与规范，源自 SFU PUPS（www.vector.comm.sfu.ca/pups/）完全挖掘工程（963 文件 2.5GB、18 组入库、944 条文件级记录、830 PDF 全文覆盖）。凡涉及镜像站抓取、批量下载、OCR、全文索引的工作须逐条对照本文件执行。

## 1 镜像站挖掘流程

### 1.1 探查与规划

- **目录级探查**：先取站点根目录与各级子目录索引页（`curl -sL <dir>/` 后 grep `href=`），摸清目录树与内容类型，再规划下载批次。勿直接盲目全站爬取。
- **区分内容类型**：技术报告（CSTR）、内部备忘录（Tech Memos）、邮件存档（mbox/html）、口述史（mp3/epub/转录）、手册（Manuals）、通讯（Newsletters）、论文（Papers）、光盘索引（非 ISO）等，按类型规划存储位置与处理方式。
- **识别子目录陷阱**：索引页显示的链接可能指向子目录（如 MERT 手册的 Green/Red/White Tabs 是子目录而非文件），须递归探查；PDF 链接可能指向其他目录的重复引用，解析时须去重。
- **明确跳过清单**：用户明确要求不下载的内容（如系统 ISO/发行版镜像 Distribution/PDP-11/VAX/4BSD 等）须在规划时列出并全程避开；光盘类只取索引文件（ls/md5sums/目录清单）不取镜像本体。

### 1.2 批量下载

- **优先 curl**：历史镜像站（如 SFU）可能拒绝 Python urllib/requests 请求（脚本静默失败），**curl 带浏览器 UA 最稳**。
- **限流应对**：连续快速请求会被站点限流（循环下载到一半静默失败/返回 502/000）。对策：
  - 每文件多 try 重试（3-6 次），失败 `rm` 后重下
  - 文件间间隔 3-5 秒（`sleep` 命令不可用时用 Python `time.sleep` 或下载循环的自然间隔）
  - 大文件（>20MB）须 `curl --max-time 300-500`，且放后台任务跑
- **断点续跑**：下载脚本须幂等——已存在且校验通过的文件跳过（`[ -s file ]` 或 `os.path.getsize` 判断）。
- **文件名含空格**：Bash 循环须引号包裹；校验时用 Python（bash 循环会把含空格文件名拆词误报）。

### 1.3 文件完整性校验

- **PDF 校验**：所有 PDF 须检查 `%PDF` 文件头（`head -c 4 file` 或 Python `read(4)`）。
- **损坏文件检测**：`fitz.open()` 后检查 `len(doc)`——**0 页但文件有大小 = 下载不完整的损坏 PDF**，须从源站重新下载；重下后的版本可能是完整且有文本层的（如 SFU 的 AUUGN-V05.4 重下后 110 页含文本层），勿直接放弃。
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
- 注意：OCR 脚本的“无文本层”判定与入库脚本须一致（均用“全页提取 > 阈值”），否则出现入库判定差异。

### 2.3 并行与断点

- **多进程并行**：单进程 OCR 浪费 CPU 核数（16 核机器单进程 7 分钟 0 产出），用 8 进程（大文件阶段降为 2-4 进程防内存竞争）。每文件在独立子进程/subprocess 中运行，崩溃不影响主流程。
- **独立 worker 文件**：worker 逻辑写入独立 `.py` 文件（`_ocr_worker_fill.py`），用 `subprocess.Popen([sys.executable, worker, pdf, ocr_dir])` 调用——**避免 Bash 内联 Python 的引号转义问题**（`\"` 破坏语法是 Bash heredoc/内联的已知坑，一律写独立 .py 文件）。
- **幂等断点**：已生成 `ocr/*.md`（>200 字节）的文件跳过；0 字节 md 视为失败，须重跑。
- **活跃度判断**：后台 OCR 任务跨会话后任务 ID 可能失效，判断是否存活看①进程列表大内存 worker（>200MB）②临时目录渲染 PNG 时间戳（每 20-40 秒一张 = 活跃）。**勿仅凭 md 数量不增长判断卡死**——大文件单 md 间隔 10-15 分钟正常。

### 2.4 质量分级与失败处理

- **抽样核对**：按考据规则抽样（每 100 页抽 5 页比对），错讹率 <5% 标 `verified`，≥5% 标 `needs_review`；低质量油印扫描（如 1975 年 USENIX 特刊，1 页模糊照片）识别内容几乎全错时，标记无效并**检索其他转载格式代替**（官方重印本/二手文献转录），不强行入库。
- **入库阈值**：OCR md <200 字节视为无效（可能 0 页损坏或全噪声）；有效 md 才写入 fulltext。
- **失败不阻塞**：单文件 OCR 失败（损坏 PDF、超大文件崩溃）记录后继续，不中断整个批次；后续统一补漏重跑。

## 3 索引入库规范（references_fulltext.duckdb）

### 3.1 组记录与文件级记录双轨

- **组记录**（如 `SFU_PUPS_AUUGN_125期`）：整组索引，`file_path` 指向组目录，**不写 fulltext**（设计预期，勿当作缺失）。
- **文件级记录**：每个文件独立 references + fulltext + fulltext_blocks + ocr_status，符合 `_44doc_fulltext.py` 既有范式。文件级记录是检索主体。

### 3.2 入库脚本要求

- **幂等**：以 `filename` 已存在集合防重，重跑安全（新增/已存在/无文本 三计数）。
- **文本来源优先级**：原生文本（htm/txt/mbox）→ 文本层 PDF（pymupdf_textlayer）→ OCR md（rapidocr_onnx）→ 无文本（no_text 计数，不建记录）。
- **字段**：filename/format/ocr_status + fulltext(content/char_count/extraction_method) + fulltext_blocks 段落块（para_split 按空行切块）。
- **入库存量**：无文本层且无 OCR 的文件不建记录（等 OCR 完成后重跑脚本补齐），避免大量空壳记录。

### 3.3 大纲回写

- **卷末书目述评追加**：各卷 `05-卷册大纲/<卷>/卷末书目述评.md` 追加“SFU PUPS 存档增补”小节（GB/T 7714 著录 + ref id）。
- **增量安全**：幂等判断**不得用“整个小节已存在则跳过”**（会漏掉增量记录）——改为“小节已存在则删除旧小节重建”（述评增补是脚本生成的，重建安全）。实测漏增量教训：537 条时小节已存在导致后续 13 条新增未写入。

## 4 经验教训汇总（SFU PUPS 工程）

1. **Bash 环境坑**：内联 Python heredoc 有转义 bug（`\"` 破坏语法）→ 一律独立 .py 文件；MuPDF 错误输出到 stderr 导致 Bash 误报 exit 1（实际正常）→ `fitz.TOOLS.mupdf_display_errors(False)` 抑制 + 以日志文件为准；重定向日志被缓冲看不到进度 → print 加 `flush=True`。
2. **数据库锁**：多轮入库脚本残留 python 进程会占锁（database is locked）→ 结束残留 python 进程（tasklist 确认后 Stop-Process）释放锁。
3. **后台任务跨会话**：任务 ID 失效后靠进程/文件时间戳判断；大工程分多轮，每轮完成入库+日志，最后统一收尾。
4. **先小样本验证**：批量 OCR/入库前先跑 2-3 个样本验证链路（渲染→识别→入库），确认无误再全量。
5. **统计口径**：`os.path.exists` 只查根目录会漏子目录文件（误报未落地）——统计须 `os.walk` 全盘；文件级记录数查询须排除组记录。

## 5 相关脚本（script/，以 SFU 工程为范本）

| 脚本 | 用途 |
| ---- | ---- |
| `_sfu_dl_batch*.py` / `_sfu_dl_mert_full.py` | 镜像站批量下载（多 try 重试 + 间隔 + 幂等） |
| `_sfu_ocr_parallel.py` | 8 进程并行 OCR 主流水线（pymupdf 渲染 + RapidOCR） |
| `_sfu_ocr_fill*.py` / `_ocr_worker_fill.py` | 补漏 OCR + 单文件 worker（subprocess 隔离） |
| `_sfu_file_ingest_v5.py` | 文件级入库（幂等，文本层/OCR 优先级） |
| `_sfu_outline_backfill.py` | 大纲回写（已存在则重建，增量安全） |
| `_wait_ocr_done.py` | OCR 完成轮询（幂等退出） |
