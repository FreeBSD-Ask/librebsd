---
spec_id: S12
title: OCR／音频工具链
task_book: 01-项目管理/01-编纂规划与报告归档/工具链与数据库标准化-任务书-20261127.md
task_book_anchor: 十三、OCR／音频工具链（S12 的设计约束）
version: 1.0.0
status: draft
goals: [11]
owner: ykla
created: 2026-11-27
updated: 2026-11-27
binding_id: TB-20261127-S12
---

# S12 OCR／音频工具链

## 1. 意图确证（档 A 摘要）

- **用户原话（节录）**：把经常调用的ocr转音频等工具链形成任务书和specs。
- **目标**：把 OCR、音频转写、响度归一与字幕的经常调用链归一为可复用流水线、质量门与任务书模板，并绑定到本 spec；不在本 spec 跑生产批。
- **非目标**：
  - 不跑生产 OCR／转写批。
  - 不做 TTS（ykla 2026-11-27 裁定）。
  - 不替换现有 SenseAudio／Tesseract 而不评估。
  - 不引入未评估的本地模型。
  - 不处理版权未清的音频。
- **验收判据**：
  - OCR 流水线文本层优先，产物含 ALTO 或 hOCR＋纯文本。
  - 质量门含 CER／WER、置信度、抽样复核、失败分级。
  - 音频流程含响度归一（BS.1770／R128）、转写、字幕。
  - OCR／音频两份任务书模板可被实际批次引用并绑定 S12；TTS 不在范围。
- **手段自由度**：
  - Tesseract（现有）＋ALTO／hOCR；可选 PaddleOCR。
  - Whisper／SenseAudio 按批评估；噪声与限速。
  - DA/T 31／62／63、ISO 19005、BS.1770、R128、WebVTT／TTML2。
- **未知／[待验证]**：
  - 本地 Whisper 与 SenseAudio 的质量／成本。
  - ALTO 与 hOCR 主格式选择。

## 2. 范围

### 2.1 范围内

- OCR 流水线
- 音频转写流水线
- 响度归一
- 字幕
- 质量指标
- 并发／限速／检查点
- provenance
- 任务书模板
- 许可

### 2.2 范围外

- 生产批
- 模型训练
- 版权清理
- TTS（不做）

### 2.3 依赖

- S01 的 OCR／音频标准
- S03 的并发与检查点
- 现有 OCR 规则与 SenseAudio 任务书

## 3. 用户故事与验收场景

### US-S12-1 OCR 可复核

**Why this priority**：OCR 结果要能回到版面与坐标，不是只有纯文本。

**Independent Test**：任取一页，有 ALTO／hOCR 与纯文本，坐标可查。

**Acceptance Scenarios**：

1. Given 一页扫描件，When OCR，Then 产 ALTO／hOCR＋md。
2. Given 一个词，When 查坐标，Then 有 bbox。

### US-S12-2 音频可质检

**Why this priority**：转写质量与响度要可测。

**Independent Test**：任取一批，有 WER／CER、LUFS、时间戳误差。

**Acceptance Scenarios**：

1. Given 一段音频，When 转写，Then 有 WER／CER 与时间戳。
2. Given 母版，When 测响度，Then 有 LUFS 与 dBTP。

### US-S12-3 任务书可复用

**Why this priority**：每次 OCR／音频批不应从零写任务书。

**Independent Test**：模板含意图、输入、参数、质量门、并发、检查点、验收、绑定。

**Acceptance Scenarios**：

1. Given 一个新批，When 套模板，Then 八节齐全。
2. Given 模板，When 查绑定，Then 指向 S12。

## 4. 功能需求

| 编号 | 需求 | 验收判据 |
| ---- | ---- | -------- |
| S12-FR-01 | MUST 盘点现有 OCR／音频工具、规则、任务书与脚本。 | 清单；版本与许可。 |
| S12-FR-02 | OCR MUST 文本层优先；无文本层才 OCR。 | 流程图；判据。 |
| S12-FR-03 | OCR MUST 产 ALTO 或 hOCR＋纯文本；记录工具与参数。 | 样例产物；坐标可查。 |
| S12-FR-04 | OCR 质量门 MUST 含 CER／WER、置信度分布、抽样人工复核、失败分级。 | 指标表；阈值。 |
| S12-FR-05 | 音频 MUST 做响度分析与归一（BS.1770-5／R128），记录 LUFS／dBTP。 | 测量报告；目标值。 |
| S12-FR-06 | 音频转写 MUST 产时间戳与字幕（WebVTT／SRT），并记录 WER／CER。 | 样例；评分命令。 |
| S12-FR-07 | MUST 定义并发、限速、重试、检查点。 | 参数表；断点续跑。 |
| S12-FR-08 | MUST 记录 provenance：源、工具、版本、参数、时间、责任人。 | PROV 映射；字段。 |
| S12-FR-09 | MUST 提供 OCR／音频两份任务书模板，八节齐全并绑定 S12；不提供 TTS 模板。 | 模板；绑定 ID；TTS 零文件。 |
| S12-FR-10 | MUST 评估许可：Tesseract、Whisper、SenseAudio、模型、数据。 | 许可表；风险。 |

## 5. 非功能需求

- 可复核：坐标、时间戳、置信度。
- 可复现：工具版本、参数、输入哈希。
- 可扩展：批参数化。
- 合规：许可与版权。

## 6. 关键实体

- OCRJob（input、engine、params、output、confidence）
- AudioJob（input、loudness、transcript、subtitle）
- QualityGate（metric、threshold、result）
- TaskTemplate（sections、binding）
- Provenance（source、tool、time、actor）

## 7. 标准与方法基线

- ISO 19005-4:2020
- ISO 32000-2:2020
- ALTO XML 4.4
- hOCR 1.2
- UAX #15／#29
- DA/T 31-2017
- DA/T 62-2017
- DA/T 63-2017
- DA/T 59-2017
- GB/T 18894-2016
- ITU-R BS.1770-5
- EBU R 128-2023
- W3C WebVTT（CRD）
- W3C TTML2（2018 Rec）
- NIST SCTK 2.4.12（方法依据）
- W3C PROV-O

## 8. 交付物

- `OCR流水线规范.md`
- `音频流水线规范.md`
- `质量指标.tsv`
- `任务书模板-OCR.md`
- `任务书模板-音频.md`
- `许可评估.md`

## 9. 风险与未决

- OCR 多语言／古籍质量差；分级与人工复核。
- 音频版权与平台条款；先评估。
- 模型／工具版本漂移；记录版本与哈希。

## 10. 追溯

- **目标**：G11 OCR／音频工具链
- **任务**：T-S12-001、T-S12-002、T-S12-003、T-S12-004、T-S12-005、T-S12-006、T-S12-007、T-S12-008、T-S12-009、T-S12-010
- **验收**：C-S12-001、C-S12-002、C-S12-003、C-S12-004、C-S12-005、C-S12-006、C-S12-007、C-S12-008、C-S12-009、C-S12-010
- **依赖**：见 §2.3
- **被依赖**：见任务书 §3 追溯矩阵
- **绑定**：`BINDING.tsv` 对应行；任务书 §16
