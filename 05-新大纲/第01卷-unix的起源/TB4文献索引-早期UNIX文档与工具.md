# TB4 文献索引——早期 UNIX 文档与工具（重 OCR 转录）

> **转录批次**：TB4（GLM 视觉重 OCR，2026-09-29）
> **覆盖范围**：ref 3719–3744（共 24 件，1310 页）
> **转录方法**：GLM-4.6V 视觉逐页转录，替代原 rapidocr_onnx
> **数据库状态**：全部入库，`extraction_method='glm_vision_20260924'`，`ocr_status='glm_vision_reocr_20260929'`
> **key_facts**：398 条（technology + person 分类）

## 文献清单

### 用户通讯与会议资料

| Ref | 标题 | 页数 | 年代 | 说明 |
|-----|------|------|------|------|
| 3719 | AUUGN-V03.4 | 126 | 1979 | AUUG（澳大利亚 UNIX 用户组）通讯第 3.4 期，含 Bell Labs 资料 |
| 3720 | AUUGN-V03.5 | 50 | 1980 | AUUG 通讯第 3.5 期 |
| 3721 | AUUGN-V03.6 | 52 | 1981 | AUUG 通讯第 3.6 期，Kevin Hill 编辑 |
| 3722 | UNIX Reference Card | 23 | — | L. L. Cherry 编写，UNIX 命令速查卡 |
| 3723 | UNIX System Quick Guide | 11 | 1982 | UNIX 系统快速指南 |
| 3725 | Unix Users Talk Notes | 7 | 1973 | 1973 年 1 月 UNIX 用户座谈会纪要 |

### 杂志与技术资讯

| Ref | 标题 | 页数 | 年代 | 说明 |
|-----|------|------|------|------|
| 3726 | UNIX REVIEW 1984-12 | 112 | 1984 | UNIX REVIEW 杂志 1984 年 12 月刊 |
| 3743 | UNIX Technology Advisor 1989-03 | 24 | 1989 | UNIX 技术顾问杂志 1989 年 3 月刊 |
| 3744 | UNIX REVIEW 1985-01 | 142 | 1985 | UNIX REVIEW 杂志 1985 年 1 月刊 |

### 工具与系统软件文档

| Ref | 标题 | 页数 | 年代 | 说明 |
|-----|------|------|------|------|
| 3724 | Tuning Unix Lex | 2 | 1987 | Vint Cerf 撰，USENIX 冬会论文，LEX 编译器调优 |
| 3727 | PLOT/CHRGEN 绘图例程 | 59 | 1977 | Bell Labs 文档，GPLOT/CHRGEN 绘图工具 |
| 3728 | DUMP 备份工具 | 1 | 1978 | Bell Labs 文档，DUMP 磁盘备份工具 |
| 3729 | FSNAP 文件备份 | 2 | 1979 | Bell Labs 文档，FSNAP 新文件特性 |
| 3736 | Adb 调试器 | 27 | — | Bell Labs 文档，Maranzano & Bourne 编写 |
| 3737 | Yacc 解析器 | 33 | — | Bell Labs 文档，Stephen C. Johnson 编写 |

### 手册与参考指南

| Ref | 标题 | 页数 | 年代 | 说明 |
|-----|------|------|------|------|
| 3730 | man1 用户命令手册 | 186 | — | Bell Labs 文档，第一节用户命令 |
| 3731 | man2 系统调用手册 | 56 | — | Bell Labs 文档，第二节系统调用 |
| 3732 | man5 文件格式手册 | 24 | — | Bell Labs 文档，第五节文件格式 |
| 3733 | NROFF/TROFF 用户手册 | 37 | — | Bell Labs 文档，Joseph F. Ossanna 编写 |
| 3734 | Memorandum Macros | 73 | 1980 | Bell Labs 文档，MM 宏包（Smith/Mashey/Pariser/Smith） |
| 3735 | Eqn 用户指南 | 11 | — | Bell Labs 文档，Kernighan & Cherry 编写 |
| 3740 | UNIX Reference Guide R4.0 | 66 | 1981 | Bell Labs 文档，Release 4.0 参考指南 |

### C 语言编译器文档

| Ref | 标题 | 页数 | 年代 | 说明 |
|-----|------|------|------|------|
| 3741 | Four Generations of Portable C Compiler | 9 | 1986 | Kristol 撰，PCC 四代演进 |
| 3742 | Lions PCC pass 2 | 177 | 1979 | PCC 第二遍编译器实现详解 |

## 章节关联

本批文献主要关联以下章节：

- **第 4 章 贝尔实验室的文化土壤**：Bell Labs 文档（3727–3740）
- **第 6 章 C 语言的诞生**：编译器与工具文档（3724, 3736, 3737, 3741, 3742）
- **第 7 章 UNIX 的传播**：用户通讯与杂志（3719–3721, 3725, 3726, 3743, 3744）
- **第 8 章 贝尔实验室的黄金时代**：Bell Labs 工具文档（3730–3737）
- **第 11 章 操作系统的谱系**：系统调用与文件格式手册（3731, 3732）
- **第 16 章 CPP-Shell 家族与脚本语言生态**：文本处理工具（3733–3735）

## 转录质量说明

- 全部 1310 页经 GLM-4.6V 视觉逐页转录
- 替换原 rapidocr_onnx 结果，`extraction_method` 更新为 `glm_vision_20260924`
- `references.ocr_status` 更新为 `glm_vision_reocr_20260929`
- 398 条 key_facts 已入库（technology 381 条 + person 17 条）
- 102 个关键词已添加到 `chapter_keywords.json`（涉及 6 个章节）

## 数据库留痕

- `fulltext`：24 件全部更新
- `fulltext_blocks`：1310 块
- `key_facts`：398 条
- `references`：`ocr_status='glm_vision_reocr_20260929'`
- `reference_update_log`：24 条留痕记录

---

**生成日期**：2026-09-29  
**转录批次**：TB4（任务书 4）  
**总页数**：1310  
**总件数**：24
