# OCR 流水线规范（S12；v1）

## 流程（文本层优先，STD-O 系列支撑）

```text
输入 PDF/图片
→ ① 文本层探测（PyMuPDF get_text；≥50 有效字符/页 ⇒ 走文本层，禁 OCR）
→ ② 预处理（300dpi 渲染（DA/T 31-2017 §9.4.2 下限 200，建议 300）；去噪/纠偏；ISO 19264-1 靶标抽检可选）
→ ③ OCR（Tesseract -l eng+chi_sim+fra+deu --psm 1；可选 PaddleOCR 对比批）
→ ④ 双产物：ALTO 4.4 XML（坐标/阅读顺序）＋ hOCR 1.2（x_wconf 置信度）＋ 纯文本 .md
→ ⑤ 质量门（见 质量指标.tsv；CER 抽样 5%/千页；失败分级 verified/needs_review/failed）
→ ⑥ 入库（references_fulltext.duckdb；blocks 带 bbox 元数据列预留）
→ ⑦ provenance（source_sha256、engine+version、params、时间、批号、操作者）
```

## 判据

- **文本层优先**：`get_text()` 非空且覆盖率 >0.5 → 禁 OCR（防 OCR 污染原生文本）。
- **双格式**：ALTO 为主（版面复核/重排），hOCR 为辅（轻量质检）；纯文本始终产出。
- **Unicode**：入库前 NFC 归一（UAX #15 rev 58）；正文保真场景禁 NFKC。
- **PDF/A**：长期保存件按 PDF/A-4（ISO 19005-4:2020）封装； veraPDF 校验列入试点。

## 与现状差距（落地即整改）

1. 现行 `tesseract-ocr-命令.md` 只产 txt/md → 补 `--alto` 与 hOCR 输出。
2. `fulltext_blocks` 无 bbox 列 → 迁移批加列（可空，向后兼容）。
3. 无 CER 抽样 → 引 NIST SCTK 方法（sclite DP 对齐），参考文本=文本层或人工双录。
