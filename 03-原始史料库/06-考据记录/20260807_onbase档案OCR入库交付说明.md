# 伯克利市 OnBase 档案综合入库续作交付说明（2026-08-07）

## 本次会话新增内容

### 一、OCR 方案选择（用户指定）
- 用户指令："用模型自己识别，禁止安装本地大模型"
- 采用 **PyMuPDF 渲染 PDF 页 → Read 工具视觉识别** 零本地模型方案
- 放弃 tencentcloud-ocr（无密钥）、rapidocr-onnxruntime（含本地 DL 模型）、tesseract（需装 Windows 程序）

### 二、批量预处理（拼接图生成）
- 19 份扫描件共 1688 页 → PyMuPDF 渲染 + PIL 拼接 → 251 张拼接图（每张 ~7 页，6384x1188）
- 3 份有文本层 PDF（20080311 / 20160712 / 20160719 议程包）跳过 OCR，PyMuPDF get_text() 直接提取 193K 字符

### 三、OCR 完成度
- **本会话完成 8 / 251 张拼接图**（约 56 / 1688 页 ≈ 3.3%）
- **OCR 仍是阶段性成果，剩余 243 张待续做会话完成**

### 四、已 OCR 的高价值发现
1. **ref 2754 决议 55,266**（Mayor Loni Hancock 签署）：UC Berkeley 计算机科学楼/工程楼扩建环境审查正式市评论文 ★★★
2. **ref 2752 1986 UNIX 采购**：议程项 11.A 授权为 HHS 购置 UNIX 计算机（Resolution 53,086）
3. **ref 2756 1990 Office of Information Services**：证明 1990 年市政府已设有 IT 部门
4. **ref 2751 ICSI 1947 Center Street 续约合同**：ICSI 机构持续存在的财政证据

### 五、综合入库（references_fulltext.db）
- `summaries` 表：22 条摘要
- `chapter_matches` 表：22 条关联章节（第 3 卷 44/53/54/55 + 第 4 卷 61）
- `fulltext` + `fulltext_blocks` + `fulltext_fts`：22 条（含 3 份文本层完整 + 6 份 OCR 摘要 + 13 份 pending 占位）
- `reference_update_log`：22 条日志
- `references.ocr_status`：22 条更新

### 六、卷级文献综述
- `vol-02.md`（伯克利的岁月）：追加 McKusick 市政活动 + UNIX 市政史章节
- `vol-03.md`（伯克利学术文化外溢）：追加 ICSI 租赁系列章节

## OCR 续做指引（重要）

由于 OCR 视觉识别工作量（1688 页）远超单次会话能力，本会话仅完成 3.3%。**用户可随时发指令继续**：

```
继续 OCR 下一批 [文档名/优先级]
```

或者：
```
继续 OCR 所有拼接图
```

接续流程：
1. `Read  script/_ocr_tiles/<base>/tile_NNN_pXXX-YYY.png` 视觉识别
2. 输出 OCR 文本 → `Edit` 追加到 `04-现代研究文献/03-文献下载/03-ocr/_onbase_berkeley/<base>.txt`
3. 重新运行 `python script/_tmp_onbase_ingest_v2.py` 更新 fulltext 内容

**优先级建议**：
1. 高：2007_zab1885（McKusick 2006 意见信所在附件）、1986_unix_minutes 剩余、1990_res55266 tile_002
2. 中：ICSI 三份法令（7024/7281/7496）剩余页
3. 低：ZAB 1885 的 700+ 页附件（建筑图纸等，与本项目相关性弱）

## 产出位置总览

| 产出 | 位置 |
|------|------|
| 22 份 PDF 原件 | `04-现代研究文献/03-文献下载/01-pdf/_onbase_berkeley/` |
| 3 份完整 OCR + 6 份紧凑摘要 TXT | `04-现代研究文献/03-文献下载/03-ocr/_onbase_berkeley/` |
| 251 张拼接图 | `script/_ocr_tiles/<base>/` |
| 数据库入库（summaries/chapter_matches/fulltext/blocks/fts） | `references_fulltext.db` ref 2736-2757 |
| 卷级文献综述 | `04-现代研究文献/02-卷级文献综述/vol-02.md` + `vol-03.md` |
| 考据记录（已追加 OCR 章节） | `03-原始史料库/06-考据记录/20260806_berkeley_records_kaoju.md` |
| 大纲史料增补（5 文件，08-06 已做） | 第 44/53/54/55 章 |
| OCR 进度报告 | `script/_ocr_tiles/_ocr_progress_20260807.md` |
| 可复现脚本 | `script/_tmp_onbase_*.py` |