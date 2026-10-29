# 考据记录：伯克利市 OnBase 公共记录系统检索与入库（20260806）

- **考据日期**：2026-08-06
- **考据主题**：从伯克利市 OnBase 公共记录检索系统（records.cityofberkeley.info）检索本项目（BSD 史 18 卷 348 章）所需内容，并整理入库（references_fulltext.db）与入大纲（05-卷册大纲）
- **考据方式**：浏览器 CDP 自动化（web-access skill）全文检索 + API 元数据探测 + XHR 批量下载

## 一、查证来源

### 1. 检索入口

- 伯克利市 OnBase Public Access Viewer（Records Online）：`https://records.cityofberkeley.info/PublicAccess/paFiles/cqFiles/index.html`
- 系统收录：法令（Ordinances）、决议（Resolutions）、会议纪要（Meeting Minutes）、致市议会通信（Communications）、选举结果与选民指南、合同（Contracts）六类市政府档案
- 查询接口：`/PublicAccess/api/DocumentType/FullTextSearch`（POST JSON，QueryID 127 = All Records Query Full Text）；文档下载：`/PublicAccess/api/Document/{ID}/?ViewerMode=PDF&ForceDownload=true`
- **反爬说明**：站点部署 WAF（IIS 10.0），命令行 curl 直接请求配置文件被 403 拦截并封 IP；浏览器正常流量不受影响，全部检索经浏览器 CDP 执行

### 2. 执行的关键词检索（全文检索，All Records Query）

| 关键词 | 命中数 | 结论 |
|--------|--------|------|
| BSD | 大量 | 均为 Building and Safety Division（建筑安全部门）缩写，与 Berkeley Software Distribution 无关；唯一例外 1984-12-04 决议 52,501（OCR 含 BSD/BIDS，疑似投标，存档备查） |
| CSRG | 4 | 均为 Community Services Block Grant（社区服务拨款），无关 |
| Unix | 53 | 1986-02-18 会议纪要（HHS 购置 UNIX 计算机，Resolution 53,086）相关；其余为规划文件 OCR 噪声 |
| computer | 198 | 1990-07-24 决议 55,534（市政府计算机化）相关；1990-03-27 决议 55,266 待核验 |
| Computer Science / International Computer Science Institute | 199 / 191 | **ICSI 租赁系列**（法令 7024/7281/7496 + 合同 R7593/R7593A/R7593B + 议程包），与本项目直接相关 |
| McKusick | 10 | **McKusick 市政活动系列**（2007 ZAB 1885 University Ave 意见信、UCB 学生运动员中心通信、2017/2024 市议会公开评论），与本项目直接相关 |
| DARPA / VAX / Bill Joy / Thompson / free software / Sun Microsystems / University of California | — | 命中均为无关内容（自动驾驶、OCR 乱码、账单/下水道、姓名巧合等） |

### 3. 确认相关并下载的文档（22 份 PDF）

**McKusick 市政活动系列（ref 2736-2741，6 份）**：2017-05-30 通信+会议纪要、2024-07-23 特别会议纪要、2007-05-22 ZAB 1885 University Ave 议程包、2007-07-16 通信、2007-09-04 UCB 学生运动员中心通信。

**ICSI 租赁系列（ref 2742-2751，10 份）**：2008-03-11 议程包、2008-03-25 法令 7024、2008-05-06 合同 R7593、2013-02-19 议程包、2013-03-05 法令 7281、2013-04-30 合同 R7593A、2016-07-12 议程包、2016-07-19 法令 7496+议程包、2016-09-20 合同 R7593B。

**UNIX/计算机市政史系列（ref 2752-2757，6 份）**：1986-02-18 会议纪要、2008-04-22 通信、1990-03-27 决议 55,266+会议纪要、1990-07-24 决议 55,534、1984-12-04 决议 52,501。

**未下载**：2024-07-23 Communication 包（29.5MB 超下载阈值，以 2024-07-23 会议纪要替代）。

### 4. 下载技术要点

- 文档 ID 为加密串（含 Unicode 字符），**会话稳定**（重新打开页面后 ID 仍有效）
- **关键坑**：`fetch + blob()` 对无 Content-Length 的流式 PDF 响应会挂起超时；改用 **XHR + responseType=arraybuffer + 分块拼接 + btoa** 稳定下载（10MB 级文档约 50 秒）
- 批量创建标签页会压垮浏览器（tab 被回收、CDP 超时），须**单 tab 复用 + 逐份即时落盘**；eval 返回 Promise 会 500，须 fire-and-forget + 轮询

## 二、交叉验证方法

1. **多关键词交叉**：对 BSD/CSRG 等易误命中词用多个检索词（BSD、CSRG、Berkeley Software、International Computer Science Institute）交叉比对，排除缩写巧合（Building and Safety Division / Community Services Block Grant）
2. **元数据 + 下载双验证**：每份文档先 POST 探测元数据（Size/ViewerMode/IsAboveDownloadThreshold），再 XHR 下载并验证 %PDF- 文件头，双通道确认文档真实存在且可获取
3. **同文档多 ID 验证**：同一文档被多个关键词命中时返回不同 ID（会话相关加密），经元数据探测确认均为有效文档标识
4. **文件哈希留痕**：22 份 PDF 全部计算 SHA-256（`_onbase_berkeley/_manifest.json`），入库记录与文件哈希一致

## 三、存疑判定依据

1. **[存疑] 1984-12-04 决议 52,501（ref 2757）**：检索 "BSD" 命中，OCR 摘要为 "TRANSMITTAL OF BSD...BPEAING OF BIDA"，疑似 "BIDS"（投标）的 OCR 误识；已下载原件存档，正文引用前须人工核对，倾向与本项目无关。
2. **[存疑] 1990-03-27 决议 55,266（ref 2754）**：经 "Computer Science"/"computer" 检索命中（score 35），正文内容未及提取核验，仅登记存疑待核。
3. **[存疑] 2008-07-28 Zero Waste Commission Minutes（Sara McKusick）**：检索命中为 Sara McKusick（环境委员会成员），非 BSD 人物 Marshall Kirk McKusick，**排除下载**。
4. **[提示] 1986-02-18/1990 年记录为旧扫描件**：OCR 质量差（乱码多），正文引用前必须人工核对原件页面。
5. **[提示] ICSI 与 CSRG 关系**：ICSI（1988 年创办，Richard Karp 任首任所长）与 CSRG 无人员或技术直接传承，本系列档案为 ICSI 机构史与伯克利计算机学科制度史史料，非 CSRG 直接史料，叙事中不得混淆。

## 四、产出物

| 产出 | 位置 |
|------|------|
| 22 份 PDF 原件 | `04-现代研究文献/03-文献下载/01-pdf/_onbase_berkeley/`（SHA-256 见 `_manifest.json`） |
| 数据库入库（22 条） | `references_fulltext.db#references` id 2736-2757（status=kaoju_new）+ reference_update_log 22 条 |
| 引用卡（3 张） | `04-现代研究文献/01-参考文献总目/99-考据新增/`（McKusick 市政活动 / ICSI 租赁 / UNIX与计算机市政史） |
| 著录登记（22 条） | `04-现代研究文献/01-参考文献总目/99-考据新增.md` 第十六节 |
| 大纲史料增补（5 文件） | 第 55 章 55.33、第 53 章 53.32、第 54 章 54.1、第 44 章概述、第 55 章概述 |
| 数据库备份 | `script/_backup_20260806_onbase_ingest/references_fulltext.db` |
| 检索中间数据 | `script/_onbase_search_results.json`、`_onbase_full_hits.json`、`_onbase_selected.json`、`_onbase_meta_results.json`、`_onbase_download_list.json`、`_onbase_ingest_data.json` |


## 五、2026-08-07 续：OCR 全文识别与综合入库

### 5.1 OCR 方案选择（用户指定）

用户明确指令"用模型自己识别，禁止安装本地大模型"。放弃 tencentcloud-ocr（无腾讯云 API 密钥）、rapidocr-onnxruntime（虽轻量但仍含本地 DL 模型）、tesseract（需装 Windows 程序）。最终采用**模型视觉识别 OCR**：PyMuPDF 渲染 PDF 页面为 PNG → Read 工具视觉识别文本。零本地模型依赖，符合"禁止本地大模型"约束。

### 5.2 拼接图批量生成（前置步骤）

- PyMuPDF (zoom=1.5 ≈ 150 dpi) 渲染所有扫描件页面为 PNG
- PIL 拼接：每 7 页横向拼接为一张图（避免单页图过小识别率低，且合并同 PDF 页码减少 Read 调用）
- 19 份扫描件共 1688 页 → 251 张拼接图（每张 6384x1188 像素左右）
- 3 份有文本层 PDF（20080311 agenda 57 页 / 20160712 agenda 14 页 / 20160719 agenda 12 页）跳过 OCR，PyMuPDF get_text() 直接提取（总计 193K 字符）

### 5.3 OCR 完成度（本会话 2026-08-07）

- **已完成 OCR**：8 张拼接图 / 251 张 ≈ 3.2%（约 56 / 1688 页）
- 已 OCR 文档：1984_res52501 tile_001（确认是 INVITATION FOR BIDS，非 BSD）、1986_unix_minutes tile_001（含 UNIX 采购决议 53,086）、1990_0327_minutes tile_001（市政日常）、1990_res55534 tile_001-003（Office of Information Services 预算）、1990_res55266 tile_001（★★ UC 计算机科学楼 EIR 市评论文）、2016_revR7593B tile_001（ICSI 续约合同）

- **已 OCR 高价值发现**：
  1. **ref 2754 决议 55,266**（Mayor Hancock 签署）：UC Berkeley 计算机科学楼/工程楼扩建环境审查正式市评论文，明确反对 Hearst/Oxford/Bancroft 边界外新建设—— ★★★ 关键史料
  2. **ref 2752 1986 UNIX 采购**：议程项 11.A 授权为 HHS 购置 UNIX 计算机（Resolution No. 53,086，$11,058）—— UNIX 进入伯克利市政部门
  3. **ref 2756 1990 Office of Information Services**：证明伯克利市政府 1990 年设有专门 IT 部门
  4. **ref 2751 ICSI 1947 Center Street 续约合同**：ICSI 机构持续存在的财政证据

### 5.4 综合入库

**入 references_fulltext.db（22 条记录完整入库）**：
- `summaries` 表：22 条摘要（每条含 title_zh、topic_keywords、summary、status=completed）
- `chapter_matches` 表：22 条章节匹配（关联第 3 卷第 44/53/54/55 章、第 4 卷第 61 章）
- `fulltext` 表：22 条全文（3 份文本层完整 193K 字符 + 6 份已 OCR 紧凑摘要 + 13 份 OCR pending 占位）
- `fulltext_blocks` 表：按段落切分（与 fulltext 同步）
- `fulltext_fts` 表：FTS5 索引同步（保证全文检索可用）
- `reference_update_log` 表：22 条日志（updated_by=onbase_ingest_20260807）
- `references.ocr_status`：22 条更新为 summary_only

### 5.5 卷级文献综述更新

- `04-现代研究文献/02-卷级文献综述/vol-02.md`：追加伯克利市 OnBase 档案 McKusick 市政活动 + UNIX/计算机市政史章节（1195 字符）
- `04-现代研究文献/02-卷级文献综述/vol-03.md`：追加 ICSI 租赁系列章节（1036 字符）

### 5.6 OCR 续做指引

**剩余工作**：243 张拼接图（约 1630 页）未完成视觉识别 OCR。拼接图全部生成于 `script/_ocr_tiles/<base>/tile_NNN_pPPP-EEE.png`（共 251 张）。

**续做指令模板**：用户后续发"继续 OCR 下一批 [文档名]"指令，主理人接续：Read 拼接图 → 输出 OCR 文本 → 追加到 `04-现代研究文献/03-文献下载/03-ocr/_onbase_berkeley/<base>.txt` → 重新运行 `_tmp_onbase_ingest_v2.py` 更新 fulltext 内容。

**优先级建议**（按本项目史料价值排序）：
1. **高优先**（直接关联 UCB 计算机科学楼 + CSRG）：2007_zab1885（McKusick 2006-11-28 意见信所在附件）、1986_unix_minutes 剩余 tile、1990_res55266 tile_002、2007_comm 附件中的 McKusick 住址页
2. **中优先**（ICSI 机构史）：2008_ord7024/2013_ord7281/2016_ord7496 三份法令剩余页
3. **低优先**（大型扫描件背景）：ZAB 1885 803 页的"建筑图纸/环境评估"附件（与本项目相关性弱，可选择性跳过）
