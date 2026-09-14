# 核查报告：05-卷册大纲/第06卷-freebsd的核心技术革新/第117章-capsicum在freebsd的集成与演进/index.md

- 源文件：D:\librebsd\05-卷册大纲\第06卷-freebsd的核心技术革新\第117章-capsicum在freebsd的集成与演进\index.md（137 行，一次完整通读）
- 批次：C389（第 3 块第 1/3）；检查日期：2026-09-13；检查方式：逐文件完整阅读人工核查（辅以 freebsd.duckdb 四枚哈希与 DB_REF 窗口实测）
- SUMMARY.md 收录：实测第 1185 行（本章索引，标题“本章索引”在档）
- 检查项速览：A 占位符——史观区“待人工回填”见条 1；B 内容完整性——章索引五段＋PODCAST 五期在位；C 编号与标题——H1 合规、行 51 旧节号残留见条 3；D 格式规范——DB_REF 重复见条 4；E 学术规范——伪消解簇见条 2、辨析 0 信任核正质量高；F SUMMARY 一致性——在档

## 问题清单

1. P2 | 行 39 史观区占位 | 史观字段为“(待人工回填——详见子节文件史观/辨析字段)”——占位符未填充（A 检查占位符缺陷） | 回填本索引对应的史观总纲映射
2. P2 | 行 64 伪消解脚注八连簇＋行 44/46 两处 | [^doubt-resolved-633]~[^doubt-resolved-640] 八个脚注定义全部“据 Mac OS X Internals A Systems Approach（Amit Singh）/Arch_Handbook/Porters_Handbook/Handbook/jude-interesting_zfs-paper/davis-asplos-cheriabi-paper-2（均未署名）消解”，与 Capsicum 主题无语义关联；行 44/46 又两处“消解^doubt-resolved-637/640：此处事实待多源交叉验证”——以消解之名行存疑之实 | 入“doubt-resolved 伪消解族”台账（553/855-864/1432 之后八连簇）；删除或还原真实消解语境
3. P3 | 行 51 末尾嵌入“## 116.4.3 从实验框架到基础系统组件的策略转变” | 旧章号 116.4.3 残留（现为 117 章），且 H2 标题误嵌在文献段落末尾——旧章号族＋结构错位 | 移除误嵌标题或改 117 章相应子节号
4. P3 | DB_REF 块重复与堆叠 | 两处“2010-2020 年间：488,947”同文案（行 59/63），全文件共 4 枚 DB_REF 块覆盖 4 个窗口（2012-2012 37,493 / 2010-2020×2 / 2010-2010 34,527）——模板冗余堆叠 | 保留一枚并注主窗口，其余合并或删
5. P3 | 首批 Capsicum 化程序名单含“hostctl(8)” | FreeBSD 无 hostctl 工具（疑笔误，或 hostname 之讹）——EP50 辨析谓首批含 tcpdump、gzip 等 | 名单按 FreeBSD 10 实际沙箱化工具核正
6. P3 | PODCAST 史观三处前缀重复 | 行 115/116/117“总纲10 动手者创造历史：总纲10 …”“总纲9 经验优先：总纲9 …”“总纲22 知识注定过时：总纲22 …”前缀双写 | 删重写前缀

- 结论：存在问题 6 项（P0 0、P1 0、P2 2、P3 4）

## 补充说明（正样本与复核留痕）

- 四枚 Capsicum/casperd commit 哈希逐字段精确：009d2032af44（Robert Watson，2011-12-29，“Add options CAPABILITY_MODE/CAPABILITIES to GENERIC”——与辨析“r219129 映射 commit 009d2032、2011-12-29T22:48:36Z”逐字吻合）、42a859525652（Dawidek 2013-12-02“Please welcome casperd daemon”首次合入）、f01f7446472b（Dawidek 2013-12-19“Make the world a bit more secure place…turn the casper”默认启用）、c501d73c7e2d（Zaborski 2016-02-25“Convert casperd to the libcasper”重构）——日期/作者/主题/哈希四全中
- DB_REF 两窗口全库口径精确：all-repo 2012=37,493、2010=34,527 双命中
- 辨析 0 信任核正质量高（全书样本级）：①“11.0 默认编译启用”辨误——FreeBSD 11.0 实为 2016-10 发布、9.0 已默认编译 CAPABILITIES，11.0 主要进展是 casperd 完善（纠正 2014 误说）；② 2015 CHERI 论文实为 IEEE S&P（Oakland）而非 SRI 技术报告；③ Google Capsicum-on-Linux 与“ANU 质疑”的检索自警；④ commit r219129 精确日期经 commits 表验证——四处纠正式考据全部成立
- PODCAST 史观总纲 9/10/6/3/4/22 全正用；Capsicum 主题内容（funlinkat TOCTOU、casperd system.dns、traceroute 沙箱化、gzip 沙箱困境、EP50 Watson 访谈）与章题高度相关
- 存疑脚注纪律：chroot 年代/jail 嵌套版本为无出处口头概括、Capsicum 沙箱缓解漏洞量化存疑——L4 标注到位
- 交办提示：条 2 的 633-640 八连簇为目前单文件最大伪消解样本，建议长改线台账单列“Capsicum/casperd 索引伪消解簇”归并处理；条 3 的 116.4.3 与 328 章“141 章”、92.1“53.14”同批扫旧章号