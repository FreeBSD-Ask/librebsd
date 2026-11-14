# pandoc EPUB 转 Markdown 命令调用规范

## 简介

pandoc 是通用文档转换工具，用于将下载的 EPUB 文件转换为 Markdown 文本。本项目通过 pandoc 对 Anna's Archive 下载的 EPUB 文献进行文本提取，输出 Markdown 存入对应 `ocr/` 目录。

## 调用语法

```bash
pandoc <input.epub> -t markdown_strict -o <output.md>
```

## 参数说明

- `<input.epub>`：输入 EPUB 文件路径
- `-t markdown_strict`：输出格式为 strict Markdown（严格模式，避免 pandoc 扩展语法）
- `-o <output.md>`：输出文件路径

## 输出位置

输出至对应 `ocr/` 目录，与 PDF OCR 输出共用同一目录约定。具体见 `流程规则.md` “文献下载规则” → “OCR 后处理”小节与 “存储位置规则”小节。

## 规则引用位置

- `流程规则.md` → “文献下载规则” → “OCR 后处理”小节

## 与 Tesseract 的关系

- **EPUB**：直接使用 pandoc 转换，无需 OCR。EPUB 本身为文本格式，pandoc 可直接解析其内部 XHTML 与元数据
- **PDF**：使用 Tesseract OCR 转换。PDF 为版式文档，应 OCR 识别页面文字

两工具按文献格式择一使用，互不替代。

## 校对规则

EPUB 转换后的 Markdown 仍应按 0 信任原则与原 EPUB 抽样核对：

- 抽样核对页数与内容完整性
- 警惕章节结构、脚注、表格、引文在转换中丢失或错位
- 转换结果应在 manifest `ocr_status` 字段标注，规则同 Tesseract OCR 校对规则
