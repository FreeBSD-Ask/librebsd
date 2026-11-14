# AutoCorrect / md-padding@latest / markdown-lint2 清理工具调用规范

## 简介

本文件规范项目正文 Markdown 文本清理所用的三个外部程序命令：AutoCorrect、`md-padding@latest` 与 `markdownlint2`。三者用途如下：

- **AutoCorrect**：自动修复中英文间距、全半角标点、英文专有名词大小写等格式问题
- **md-padding@latest**：在中文字符与英文字符/数字之间自动添加空格
- **markdownlint2**：检查 Markdown 文件格式，依据项目根目录配置文件报告违规行

三工具仅作为辅助清理手段，其输出建议一律不应默认接受，应按“约束”小节逐项人工复核。

## 调用语法

### AutoCorrect

```bash
autocorrect --fix <file>
```

自动修复 `<file>` 中中英文间距、标点全半角等格式问题，原地写回。

### md-padding@latest

```bash
npx md-padding@latest <file>
```

通过 `npx` 调用最新版 `md-padding`，为 `<file>` 中中文与英文/数字之间添加空格。

### markdown-lint2

```bash
markdownlint2 <file>
```

按项目根目录配置文件对 `<file>` 进行 Markdown 格式检查，输出违规行号与规则编号。

## 参数说明

### AutoCorrect 常用参数

- `--fix`：原地修复并写回文件（默认仅打印差异）
- `--lint`：仅报告问题不修复
- `--file <path>`：指定单个文件
- `--glob <pattern>`：按 glob 模式批量处理

### md-padding@latest 常用参数

- `<file>`：待处理 Markdown 文件路径（位置参数）
- `--write`：原地写回（默认打印到标准输出）

### markdown-lint2 常用参数

- `<file>`：待检查 Markdown 文件路径（位置参数）
- `-c <config>`：指定配置文件（默认读取项目根目录 `.markdownlint.json` 或类似配置）
- `--fix`：自动修复可修复的违规项

## 规则引用位置

本文件涉及的三个工具在以下规则文件小节中被引用：

- `流程规则.md` → “AutoCorrect 调用规范”小节
- `流程规则.md` → “三轮完整执行规则”小节
- `写作规则.md` → “中文引号强制规则”小节（提到 AutoCorrect、`md-padding`、`markdown-lint` 工具建议修改行间代码时应拒绝）
- `写作规则.md` → “行间代码与代码块不可篡改规则”小节
- `主题规则.md` → “仅 FreeBSD 内容跨 BSD/UNIX/macOS 扩展规则”小节（提到不应批量接受 AutoCorrect/`md-padding`/`markdownlint2` 输出）

## 约束

- **不应批量接受**：三工具的输出建议一律不应批量接受，应逐条审阅
- **不应默认接受**：不应以工具输出为最终结果，应经人工判断
- **逐个复核**：每条建议应结合上下文综合判断，特别注意行间代码、代码块、命令、路径是否被误改
- **修改前后各复核一次**：执行工具前先复核原文，执行后逐条比对差异
- **最后总复核一次**：全部清理完成后，对整文件做一次总体复核，确保未破坏代码块、引号、标点语义
- **行间代码不可篡改**：凡工具建议修改行间代码（如 `` `path/to/file` ``）或代码块内容，一律拒绝
