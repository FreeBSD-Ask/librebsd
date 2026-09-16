# 核查报告：第01卷-unix的起源/第5章-法律环境与源代码散逸/index.md

- 源文件：d:\librebsd\05-卷册大纲\第01卷-unix的起源\第5章-法律环境与源代码散逸\index.md
- 批次：B029；检查日期：2026-09-07；检查方式：逐文件完整阅读人工核查
- SUMMARY.md 收录：未收录
- A 占位符：发现 1 处
- B 内容完整性：发现 4 处
- C 编号与标题：通过
- D 格式规范：发现 5 处
- E 学术规范：发现 1 处
- F SUMMARY 一致性：未收录
- 机械旗标复核：含两条旗标。其一 UNLISTED_NOT_IN_SUMMARY——经核对 SUMMARY.md 确无本文件条目，登记为“未收录”；章入口 index.md 与概述.md 的收录分工属项目结构策略，本报告如实登记。其二 SECTION_GAP：gaps 为 [1,2,3,4,5,6,7]，dups 为空，min 8、max 10、count 3——即机械扫描显示第 5 章磁盘节文件仅有 5.8、5.9、5.10 三个（本批已核 5.8、5.9，5.10 归其他批次），5.1 至 5.7 无独立节文件；该缺口是否成立需与概述.md 的本章节索引交叉核验（见本批概述.md 报告），本报告确认旗标描述的磁盘节文件分布与实际一致。

## 检查明细

### A 占位符

行 30 出现明确空缺标记“（待人工回填——详见子节文件史观/辨析字段）”，属待填占位符，计 1 处。史料字段的 [DB:references_fulltext:chapter_matches:...] 行（行 17-26）为数据库交叉引用行，按规则豁免；行 40 的 NEWREF 注释为数据库增补标记，豁免。

### B 内容完整性

1. 行 13：要点第 3 条在“多数成员仅持 AT&T/US”处截断，US 应为 USL 且后半句缺失，文意不完整。
2. 行 30：史观字段整体为待回填占位，字段缺失（与 A 项同源）。
3. 行 34：辨析第 1 条结尾“统计显著”戛然而止，应为“统计显著性”相关完整表述，文本截断。
4. 行 35：辨析第 2 条结尾“23 日为信件签”截断，应为“23 日为信件签署日”，文本截断。
   要点、史料（数据库引用）、文献三字段有实质内容，标题自洽；但四处截断/缺失使本文件作为章入口的可用性受损。

### C 编号与标题

frontmatter chapter 为“第 5 章”、id 为 CH5、volume 为“第01卷-unix的起源”，与文件所在目录一致；H1“第 5 章 法律环境与源代码散逸”与文件夹名“第5章-法律环境与源代码散逸”一致，无旧章号残留。

### D 格式规范

1. 行 13：英文宗旨引语 "preserve, maintain and restore historical and non-mainstream UNIX systems" 使用 ASCII 直引号，应改中文弯引号。
2. 行 39：英文书名 "A History of Modern Computing"、"Computer" 用直引号未用《》，且 Ceruzzi 与书名之间缺空格。
3. 行 40："United States v. IBM"、"Trouble in the Teamster Union" 书名用直引号未用《》。
4. 行 41："Letter to UNIX enthusiasts"、"Why Caldera Released Unix: A Brief History"、"A Repository of Unix History and Evolution" 书名用直引号未用《》。
5. 行 39：本地路径 c:\Users\ykla\Documents\hibsd\... 以行间代码呈现而未按“带 \ 的路径须加粗”规则加粗。
   其余：一段一行合规；无手册页引用与术语问题。

### E 学术规范

1. 行 39：引用的本地绝对路径指向旧项目目录（hibsd、c:\Users\ykla 用户目录）与旧库文件“资料数据库.db”——该库已于 2026-07-28 拆分并于 2026-08-25 升格为 DuckDB 主存储层，引用已陈旧失效，建议更新为现行数据库标识并复核路径可达性，计 1 处提示。
2. 存疑标注：行 39 带 doubt-resolved-35、行 40 带 doubt-resolved-32，符合规范；无禁引来源；无禁用名称。

### F SUMMARY 一致性

SUMMARY.md 未收录本文件（summary_title 与 summary_line 均为 null），与机械旗标 UNLISTED_NOT_IN_SUMMARY 相符，登记为“未收录”。

## 问题清单

- 1. P1 | 行 13 | 多数成员仅持 AT&T/US | 文本截断 | 补全为 AT&T/USL 及后续完整语句
- 2. P1 | 行 30 | (待人工回填——详见子节文件史观/辨析字段) | 占位符且史观字段缺失 | 依据子节史观字段汇总回填章级史观
- 3. P1 | 行 34 | 统计结论限于文献计量学层面，不可外推至代码活跃度；统计显著 | 文本截断 | 补全“统计显著性”相关完整表述
- 4. P1 | 行 35 | 二者非矛盾而是不同事件节点——23 日为信件签 | 文本截断 | 补全为“23 日为信件签署日，24 日为公开发布日”
- 5. P2 | 行 13 | 宗旨为"preserve, maintain and restore..." | ASCII 直引号 | 改为中文弯引号
- 6. P2 | 行 39 | Ceruzzi"A History of Modern Computing"(2003)；Campbell-Kelly & Aspray"Computer"(1996) | 书名未用《》且缺空格 | 改为《》并补空格
- 7. P2 | 行 40 | "United States v. IBM"案件档案；Richard McKenzie"Trouble in the Teamster Union" | 书名未用《》 | 改为《》
- 8. P2 | 行 41 | "Letter to UNIX enthusiasts"等三处书名直引号 | 书名未用《》 | 改为《》
- 9. P2 | 行 39 | 文件路径：c:\Users\ykla\Documents\hibsd\... 以行间代码呈现未加粗 | 路径未加粗 | 按规则对带 \ 路径加粗且不篡改
- 10. P2 | 行 39 | 引用旧项目路径 hibsd 与旧库“资料数据库.db”已陈旧失效 | 陈旧引用提示 | 更新为现行 DuckDB 库标识并复核可达性

## 结论

- 结论：存在问题 10 项（P0 0、P1 4、P2 6、P3 0）

核心问题为史观字段待回填占位与要点、辨析字段三处文本截断，建议优先修复 P1；格式与陈旧引用问题次之。