# Tesseract OCR 命令调用规范

## 简介

Tesseract 是开源 OCR（光学字符识别）引擎，用于将下载的 PDF 文件转换为文本。本项目通过 Tesseract 对 Anna's Archive 下载的 PDF 文献进行 OCR 后处理，输出 Markdown 文本存入对应 `ocr/` 目录。

## 调用语法

```bash
tesseract <input.pdf> <output_basename> -l eng+chi_sim+fra+deu --psm 1
```

## 参数说明

- `<input.pdf>`：输入 PDF 文件路径
- `<output_basename>`：输出文件基名（不含扩展名，Tesseract 自动追加 `.txt` 或其他扩展名）
- `-l eng+chi_sim+fra+deu`：使用英语、简体中文、法语、德语四种语言模型，覆盖 BSD 史文献常见语种
- `--psm 1`：页面分割模式 1（自动检测页面分割，含方向与旋转检测）

## 输出位置

输出 Markdown 至对应 `ocr/` 目录，文件名同原 PDF 但扩展名 `.md`。具体目录约定见 `流程规则.md` “文献下载规则” → “OCR 后处理”小节与 “存储位置规则”小节。

## 规则引用位置

- `流程规则.md` → “文献下载规则” → “OCR 后处理”小节

## OCR 校对规则

按 0 信任原则执行 OCR 校对：

- **抽样核对**：OCR 文本应与原 PDF 抽样核对，每 100 页抽 5 页比对
- **警惕重点**：技术术语、版本号、人名、命令、路径等易错讹内容应重点核对
- **manifest 字段标注**：在 manifest `ocr_status` 字段按错讹率分级标注
  - 错讹率 < 5% 标 `verified`
  - 错讹率 ≥ 5% 标 `needs_review`

## OCR 失败处理

- 若 Tesseract 未安装或执行失败，标记 `ocr_status=failed`，记录错误信息
- OCR 失败不阻塞下载流程，下载流程继续处理下一条目
- 失败条目应在后续单独排查并重试 OCR
