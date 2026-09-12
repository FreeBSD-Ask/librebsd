# 核查报告：第10卷-openbsd的历史/第212章-openbsd与同时期操作系统的技术比较/index.md

- 源文件：d:\librebsd\05-卷册大纲\第10卷-openbsd的历史\第212章-openbsd与同时期操作系统的技术比较\index.md
- 批次：C253；检查日期：2026-09-12；检查方式：逐文件完整阅读人工核查（辅以 openbsd.duckdb 只读实查，7 枚 commit 哈希全量核验）
- SUMMARY.md 收录：未收录（index.md 不入 SUMMARY；SUMMARY 第 1811 行章页面为概述.md，章题“第 212 章 OpenBSD 与同时期操作系统的技术比较”）
- A 占位符：发现 2 处（行 12、14“〔待核：原文截断，后文待回源〕”）
- B 内容完整性：发现 1 处（要点五条中四条截断；史观段空心）
- C 编号与标题：发现 1 处（H1“openbsd与同时期操作系统的技术比较”与 SUMMARY 章题“OpenBSD 与同时期操作系统的技术比较”大小写不一致）
- D 格式规范：发现 1 处
- E 学术规范：通过（无总纲伪标签——PODCAST 块六条史观条目名与权威表逐字相符；无禁引来源，无禁用名称）
- F SUMMARY 一致性：见 C 项
- 机械旗标复核：UNLISTED_NOT_IN_SUMMARY——惯例豁免；无 SECTION_GAP 旗标且章目录实测 212.1-212.6 六节齐备，相符
- 问题清单：
  1. P1 | 行 23 | 史观段“(待人工回填——详见子节文件史观/辨析字段)” | 章级史观空心（42/114/246/116/283/131 同款第七例） | 依 212.1-212.6 各节史观字段汇总回填
  2. P1 | 行 11-15 | 要点五条中四条截断：行 11 止于“Jails（1999 年由 Poul-Henning Kamp”、行 12 与行 14 带〔待核〕标记、行 13 止于“Security Containment 与”、行 15 止于“早于 3” | 字节截断族＋显式待核叠加 | 回源重建
  3. P2 | 行 35-80 | 六张对照表的标题行粘入文献条目尾部（“…执行日期：2026-07-27 ［A］**OpenBSD pledge/unveil vs FreeBSD MAC Framework 对比**：”等六处） | 表题与文献行粘连（300/116 章同族），表本身可渲染但结构归位失当 | 表题拆出独立行
  4. P2 | 行 108-113 | PODCAST 块史观六条前缀全部重复（“总纲9 经验优先：总纲9 经验优先：”等，单块最重一例） | 前缀重复残留（113/116/118 同族） | 去重
  5. P2 | 行 19 | chmatch_3909“匹配置信度 folder，原因：folder 第210章” | folder 匹配噪声（42 章 index 同族），置信度字段为目录名非数值 | 库侧重投影
  6. P3 | 行 55-62 | 商业 UNIX 对照表“Common Criteria EAL4+”三处 | EAL4+ 证书随版本与评估期限更新（Solaris 10 证书 ID 在案），宜注“评估时点”以免过期误读 | 注记（可选）
- 结论：存在问题 6 项（P0 0、P1 2、P2 3、P3 1）

## 补充说明（正样本与复核留痕）

- **7 枚 commit 哈希全量实查逐字命中**（openbsd.duckdb 只读，哈希＋作者＋日期＋主题四字段全符）——本会话单文件最高验证密度：df174574d401＝deraadt 2015-10-09“Rename tame() to pledge()”、8b23add8c74b＝beck 2018-07-13“Unveiling unveil(2)”、af7d239111f9＝dm 1996-12-28 arc4random、1dc0268a4106＝millert 1998-07-01 strlcpy/strlcat、bf74e864c129＝deraadt 1999-10-01 OpenSSH-1.0、148b55c022b1＝kjell 2001-06-24 pf 初始导入、345de70aec27＝deraadt 2001-05-30 移除 ipf（“Darren Reed has interpret…”与许可证争议叙事互证）。
- 六张对照表构成安全机制比较的完整矩阵：pledge/unveil vs MAC Framework（引入版本/关键 commit/技术层级/权限模型/时间差“早约 12 年”）、SELinux vs AppArmor vs pledge（NSA/Immundix/OpenBSD 社区主导、约 4000+ 类型 vs 约 30 个 promise 关键字）、商业 UNIX CC 认证对照（Solaris/AIX/HP-UX EAL4+ vs OpenBSD 从未申请）、macOS 安全机制演进（Seatbelt 基于 TrustedBSD MAC→Gatekeeper→SIP→Apple Silicon PAC 与 OpenBSD 7.6 arm64 部分支持）、pf 关键 commit 时间线、OpenBSD 安全成果扩散（arc4random/strlcpy“进入 POSIX.1-2024 标准”/OpenSSH/pledge 启发 Linux landlock）——行 87 的跨项目采纳清单与 116 章 Capsicum、282.7 许可证考据形成互证网络。
- 行 27-31 辨析的“技术层级不同”三连辨析（pledge 进程级 syscall 沙箱 vs MAC 内核级策略框架、SELinux 4000+ 类型 vs pledge 30 关键字、SIP 系统目录保护 vs unveil 文件路径访问）拒绝了等价类比的偷懒；行 31 对基准测试“配置不等价”的批评（规则数量/状态表/conntrack 未对齐）与 NetBSD NPF 取代 pf 的时点补充，防止了单维性能结论。
- PODCAST_REVIEW（EP324）六条史观条目名与权威表逐字相符（唯前缀重复）；Hammer2 紧急模式与 ZFS slop 空间对照、RAM 耗尽死机的环境变量未隔离存疑——二手转述的边界意识保持。
- 编码合规：UTF-8 无 BOM、LF；弯引号正确；表格规范。
