# 核查报告：第09卷-netbsd的历史/第172章-netbsd的诞生与早期版本/index.md

- 源文件：d:\librebsd\05-卷册大纲\第09卷-netbsd的历史\第172章-netbsd的诞生与早期版本\index.md
- 批次：C018；检查日期：2026-09-08；检查方式：逐文件完整阅读人工核查（无降级）
- SUMMARY.md 收录：未收录（summary_title 与 summary_line 均为 null，与旗标 UNLISTED_NOT_IN_SUMMARY 相符）
- A 占位符：无显式占位符标记（无 TODO/待补等）；但存在 3 处截断残句，属内容空缺，计入 B 项
- B 内容完整性：发现 4 处
- C 编号与标题：通过（H1“第 172 章 netbsd的诞生与早期版本”与文件名、frontmatter chapter/id: CH172 一致；无旧章号残留；无子节标题）
- D 格式规范：发现 2 处
- E 学术规范：发现 1 处
- F SUMMARY 一致性：未收录
- 机械旗标复核：UNLISTED_NOT_IN_SUMMARY——属实，SUMMARY.md 未收录本章 index，且该章 index 为章入口性质文件，未收录属既有状态，登记备案
- 问题清单：
  1. 行28 | “……与 NetBSD 1993.4 创建公告时间高度吻合，可作为” | 句子戛然而止，内容截断残缺 | B | P1 | 补全该句结论或恢复被截断文本
  2. 行31 | “经 bsd_commits.db netbsd-src 仓库 commits 表验证：deraadt 末条 commit” | 句子戛然而止，验证内容缺失 | B | P1 | 补全验证结论
  3. 行32 | “ts.db commit 时间线）；【交叉验证方法】……” | 行首残段疑为 bsd_commits.db 断裂尾部，与上行衔接断裂 | B | P1 | 修复拼接残段，恢复完整交叉验证方法表述
  4. 行15-17 | 三条 chapter_matches 的“原因：folder 第170章”挂于第 172 章 | 匹配原因章号与本章不符，疑为数据库匹配错挂 | B | P2 | 复核 references_fulltext 库中 chmatch_3695/3696/3877 匹配依据
  5. 行24 | “NetBSD 的历史是‘可移植性’这一形式主义概念……”（原文为 ASCII 单引号） | 中文语境使用 ASCII 直引号，应为弯引号 | D | P1 | 改为全角弯引号
  6. 行29、31 | history.html、openbsd-faq1.html、netbsd-history.html、formal.html、bsd_commits.db、netbsd.db 等文件名未加粗 | 文件名须加粗且不篡改 | D | P2 | 按写作规则对文件名加粗
  7. 行28、31 | 分叉动机、撤权日期等存疑史实仅在辨析字段说明 | 未见 [存疑脚注] 标注 | E | P2 | 对最终无法确证处补充 [存疑脚注]
- 结论：存在问题 7 项（P0 0、P1 4、P2 3、P3 0）
