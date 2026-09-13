# 核查报告：第05卷-freebsd的工程化奠基/第89章-freebsd-ports系统的起源与jordan-hubbard谱系/index.md

- 源文件：d:\librebsd\05-卷册大纲\第05卷-freebsd的工程化奠基\第89章-freebsd-ports系统的起源与jordan-hubbard谱系\index.md
- 批次：C326；检查日期：2026-09-13；检查方式：逐文件完整阅读人工核查（辅以 SUMMARY/章目录实测）
- SUMMARY.md 收录：未收录（UNLISTED 实测确认：SUMMARY 第 764 行章头指向概述.md、第 765 行起收录 89.1-89.5；本 index.md 未收录；批次 JSON 记 null）
- A 占位符：通过
- B 内容完整性：发现 2 处戛然截断（辨析行 32、36）；要点区仅单条为最小骨架（PODCAST_REVIEW 六期充实，登记观察不列问题）
- C 编号与标题：发现 1 项（章级双头并存）
- D 格式规范：通过
- E 学术规范：发现 2 处（自撰史观标签；E-14 数值漂移）
- F SUMMARY 一致性：未收录（双头结构组成部分，见清单 3）
- 机械旗标复核：UNLISTED_NOT_IN_SUMMARY 实测确认（章目录含概述.md/index.md/89.1-89.5/媒体反响与社区舆论.md，概述系 SUMMARY 章头）；无 SECTION_GAP
- 问题清单：
  1. P2 | 行 32、36 | “E-14 FreeBSD ports 784,191 commits 包含 Ports 系统全生命”（断）、“freebsd-pkg 邮件列表 2011-2016 归档经 …… 覆盖 pkgn”（断） | 戛然截断两处：辨析段查证体与统计口径说明中途截断（index 类截断族） | 回源补全
  2. P2 | 全文件 | index.md 与概述.md 双头并存：概述.md 系 SUMMARY 第 764 行章头，本 index.md 未收录（289index/76index 同族第三例） | 章级结构待修（合并双头或定位 index 职责）
  3. P3 | 行 28 | “形式主义：Ports 系统是‘软件包管理’这一形式主义概念在 FreeBSD 生态中的物质化” | 自撰史观标签且无权威条号（形式主义模板族） | 去自撰标签，或按论旨挂权威条号（如总纲 11 商品是形式主义）并用全称
  4. P3 | 行 32 | “E-14 FreeBSD ports 784,191 commits” | 数值漂移：实测 freebsd-ports 788,411（E-14 系旧快照值，宜注快照日期或更新） | 更新或注明
- 结论：存在问题 4 项（P0 0、P1 0、P2 2、P3 2）

## 补充说明（正样本与复核留痕）

- PODCAST_REVIEW 六期为章题核心一手材料群：BSD Now EP13（Jordan Hubbard 自述 386BSD patchkit 三人协作、FreeBSD 命名经 David Greenman 提议、ports 约 300 个交 Satoshi Asami、2001 年入组 Apple BSD Technology Group 以 FreeBSD 3.2 为参考回灌 OS X）直击“ports 起源与 Hubbard 谱系”章题；EP499（Langille FreshPorts/BSDCan）、EP312（包管理器价值）、EP283（图形栈团队）、EP223（Rust 移植 ports 流程）均含 ports 生态一手细节。
- PODCAST 史观 13 处全对（总纲 10×4、9×2、4×2、22、15、5、13——全部权威全称逐字一致），为史观映射正确率最高的文件之一；辨析存疑脚注质量高（FreshPorts 年份口述概数、BSDCan 连续办会年数、受访者姓名 Niklas/Nicolas 拼写噪音与时间戳乱序、编译器可调试性文章的利益关联、663/664 转写文件错位自曝）。
- DB 口径正样本：三仓提交量 788,411/445,203/61,237 与实测完全吻合（合计 1,294,851）。
- 树内卫生观察：章目录存在命名异质文件 V5-Ch88-新增-Ports的伦理结构.md（Ch88 编号文件置于 89 章目录），未计入本报告问题清单，登记备修改线归位。
- 实测留痕：SUMMARY 第 764-766 行（章头＋89.1/89.2）；123.4 SUMMARY 实测第 1094 行（JSON 记 1095，偏移 +1）。
