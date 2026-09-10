# 核查报告：第12卷-macos的bsd遗产/第242章-macosx-100-103从cheetah到panther/index.md
- 源文件：d:\librebsd\05-卷册大纲\第12卷-macos的bsd遗产\第242章-macosx-100-103从cheetah到panther\index.md
- 批次：C095；检查日期：2026-09-09；检查方式：逐文件完整阅读人工核查
- SUMMARY.md 收录：未收录（该章入口以概述.md 收录于 SUMMARY.md 第 2039 行“第 242 章 Mac OS X 10.0-10.3：从 Cheetah 到 Panther”，242.1-242.7、媒体反响与社区舆论、采访录均已收录；index.md 本身未单独收录）
- A 占位符：发现 3 处
- B 内容完整性：发现 7 处
- C 编号与标题：通过
- D 格式规范：发现 8 处
- E 学术规范：发现 1 处
- F SUMMARY 一致性：未收录（与 UNLISTED_NOT_IN_SUMMARY 旗标一致）
- 机械旗标复核：UNLISTED_NOT_IN_SUMMARY——核实成立。SUMMARY.md 经检索确认未单独收录 index.md，章以概述.md 为入口（第 2039-2048 行收录该章全部节文件与专题辅助文件）。此为章入口双文件（概述.md/index.md）并存模式，非结构缺陷
- 问题清单：
  1. 24 | （待人工回填——详见子节文件史观/辨析字段） | A 占位符 | P1 | 回填史观映射内容，或改写为明确的数据库交叉引用行格式
  2. 28 | 〔待核：原文截断，后文待回源〕 | A 占位符 | P1 | 回源补全 Jordan Hubbard 加入 Apple 时间的考据后删除待核标记，存疑处按规范改用 [存疑脚注]
  3. 30 | 〔待核：原文截断，后文待回源〕 | A 占位符 | P1 | 回源补全 Darwin 与 FreeBSD 代码同步方向的论述后删除待核标记
  4. 11 | 提交 “Reduce gratuitous whitespace difference from | B 内容完整性 | P1 | 句子在引号未闭合处截断，回源补全 commit 信息与结论
  5. 12 | KAME 是日本 WIDE 项目主持的 IPv6/IPsec | B 内容完整性 | P1 | 括号内容在“IPv6/IPsec”处截断且括号未闭合，补全 KAME 说明
  6. 13 | 延续 Robert Watson 2001 年开始的 Darwin | B 内容完整性 | P1 | 句子截断，补全 Darwin 补丁流延续性论述
  7. 14 | Windows XP（2001 年 10 月 25 | B 内容完整性 | P1 | 句子在日期处截断且括号未闭合，补全对比结论
  8. 15 | kdebug(1) man pa | B 内容完整性 | P1 | 句子在“man pa”处截断，补全手册页论述
  9. 29 | （如与 Rendezvous 的 mDN | B 内容完整性 | P1 | 句子截断且括号未闭合，补全 mDNS 适配说明
  10. 31 | 而非底层 B | B 内容完整性 | P1 | 句子在“底层 B”处截断（BSD 一词被切），补全采信结论
  11. 24 | ## 史观 下为空占位 | E 学术规范 | P1 | 史观字段未映射 25 条总纲任何条目，须回填至少 5 条相关总纲映射
  12. 11 | bsd_commits.db 查询显示 | D 格式规范 | P2 | 文件名 bsd_commits.db 须加粗
  13. 13 | bsd_commits.db 查询显示 | D 格式规范 | P2 | 文件名须加粗
  14. 28 | freebsd.db 查询显示 | D 格式规范 | P2 | 文件名须加粗
  15. 30 | bsd_commits.db 显示 | D 格式规范 | P2 | 文件名须加粗
  16. 36 | bsd_commits.db 查询结果 [EB/OL]. | D 格式规范 | P2 | 文献条目内文件名须加粗
  17. 37 | bsd_commits.db 查询 L7.5.1 结果 | D 格式规范 | P2 | 文献条目内文件名须加粗
  18. 13 | message_subject 含 “From Apple”/“From Darwin” | D 格式规范 | P2 | 查询关键词应使用行间代码包裹（`"From Apple"`）或中文引号，不宜裸 ASCII 直引号
  19. 38 | 1985-2026 年间：2,012 次提交 | D 格式规范 | P2 | DB_REF 自动增补块内部自相矛盾（起始 1985 与“时间跨度 2001-04-10 至 2026-04-13”冲突），建议回源核验 darwin.duckdb 后修正（第 39 行同）
- 结论：存在问题 19 项（P0 0、P1 11、P2 8、P3 0）
