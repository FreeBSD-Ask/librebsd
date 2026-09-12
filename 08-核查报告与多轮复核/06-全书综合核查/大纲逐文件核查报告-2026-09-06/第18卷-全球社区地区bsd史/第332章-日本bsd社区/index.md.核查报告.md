# 核查报告：第18卷-全球社区地区bsd史/第332章-日本bsd社区/index.md

- 源文件：d:\librebsd\05-卷册大纲\第18卷-全球社区地区bsd史\第332章-日本bsd社区\index.md
- 批次：C289；检查日期：2026-09-12；检查方式：逐文件完整阅读人工核查（辅以 openbsd.duckdb、freebsd.duckdb、netbsd.duckdb、dragonflybsd.duckdb、openssh.duckdb 只读实查）
- SUMMARY.md 收录：未收录——批次 JSON 无 summary_line；SUMMARY 行 2845 收录的是同章概述.md，index.md 与概述.md 并存且仅概述在册（概述题名“日本：BSD 社区与 FreeBSD 用户组的历史”与 index H1“第332章 日本bsd社区”不同名）
- A 占位符：发现 1 处（行 57“〔待核：原文截断，后文待回源〕”）
- B 内容完整性：发现 3 类（承重发布史错误 1 处；DB 数值与实测不符 1 族；标题/句段截断与残行族 ×11 处）
- C 编号与标题：发现 1 类（旧章号幽灵节 331.x ×10 处，含同名重复贴入；H1 与章目录一致）
- D 格式规范：通过（截断与空节已并入 B 计，无其他格式类）
- E 学术规范：发现 1 类（史观描述符未用规范文本 1 处；史观伪标签 0 处）
- F SUMMARY 一致性：不一致（index.md 未收录，在册者为概述.md——双文件族 DEFERRED，且两文件题名不同）
- 机械旗标复核：UNLISTED_NOT_IN_SUMMARY——已复核属实
- 问题清单：
  1. P1 | 行 72 | “Sony PlayStation 3/4/5 操作系统基于 FreeBSD 内核” | 承重发布史错误：PS3 的 CellOS 并非 FreeBSD，Sony 自 PS4（Orbis OS，2013）起方基于 FreeBSD；“自 2006 年 PS3 起即使用 FreeBSD”随之错误（该主题为 331.5.2 节核心主张，属承重） | 改为“PS4/PS5 基于 FreeBSD；PS3 CellOS 为索尼自研”，日期随之更正
  2. P1 | 行 15 | “H. Peter Anvin（日裔）…Yoshinori K. Okuji，GRUB 创始人” | 人物归属错置 ×2 处：H. Peter Anvin 并非日裔；GRUB 创始人为 Erich Boleyn，Okuji（小林良岳）系后续维护者而非创始人 | 删改 hpa 条目；Okuji 改“GRUB 维护者（日籍）”
  3. P2 | 行 25/63 | “+09:00 日本标准时 38,272 commit / 3,046 贡献者” | DB 数值与实测不符且口径错乱：文称“openbsd.duckdb 查询 L3.3.1/L3.3.2（22 仓库合计）”，实测该库仅 3 仓库（openbsd-src/ports/www）且 +09:00 时区与 .jp 邮箱提交均为 0；五库合计 12 仓库、JST 8,801 commit/281 email、.jp 223/17，与 38,272/3,046、6,471/205 均不符 | 重跑跨库统计，以实测值与真实库名重写
  4. P2 | 行 23-80 | “## 331.3.2 AsiaBSDCon（首届 2004 年于台北…” | 旧章号幽灵节 ×10 处（331.x 应为 332.x；331.3.2 重复贴入 3 次、331.10.2 重复 2 次），并伴标题/句段截断与残行（行 23“[考据完成：2”、32“TRON 项目与”、37“…非”、39“基于 commi”、47“UNIX Operat”、52“BSD 面”、62“成为”、67“- 要点：Hiroki”、73“Sony PS3/”、79“[考”、80 悬空“部署案例”） | 删除重复残片，按 332.x 重编并回源补全
  5. P2 | 行 63 | “原材料/研究/bsd仓库分析/数据分析/深层信息挖掘.md” | 原材料路径断链（D:\librebsd\原材料 全项目不存在） | 改库内实际路径或内联 DB 查询语句
  6. P2 | （SUMMARY 未收录） | index.md | 双文件族：在册者为概述.md（SUMMARY 行 2845），index.md 未收录且与概述题名不同 | DEFERRED（沿用主线程双文件裁决）
  7. P3 | 行 19 | “总纲第 20 条——日本作为 UNIX 工作站大国…” | 史观编号 20 与内容（硬件生态塑造渗透路径，即历史地理塑造思想土壤）契合，但未用规范描述符 | 回填规范语“历史地理塑造思想土壤”，编号不变
  8. P3 | 行 57/83 | “〔待核：原文截断，后文待回源〕”／“## 史料考据补充”（空节） | 待核占位 1 处＋空节残行（“史料考据补充”标题下无内容即接自反性声明） | 回源补全 KAME/SLAAC 条目；空节删除或补写
- 结论：存在问题 8 项（P0 0、P1 2、P2 4、P3 2）

## 补充说明（正样本与复核留痕）

- DB 实查（五库只读）：openbsd.duckdb 实仅 3 仓库（openbsd-src/openbsd-ports/openbsd-www）、491,195 提交、1,031 贡献者，+09:00 时区与 .jp 邮箱提交均为 0；五库（freebsd/netbsd/openbsd/dragonfly/openssh）合计 12 仓库，JST 提交 8,801 次/281 个邮箱，.jp 提交 223 次/17 个邮箱——行 25 的 38,272/3,046、6,471/205 及“22 仓库合计”均无法成立（问题 3）。
- 正样本：Sony NEWS（1987 年，NEWS-OS 基于 4.2BSD/4.3BSD）、NEC EWS-4800、IIJ 1992 年成立、BIGLOBE（NEC）/@nifty（富士通）/OCN（NTT）运营商归属、任天堂 2017 年向 FreeBSD Foundation 捐赠与 Switch NPLN 用 FreeBSD 等章级要点与通行记载相符；PODCAST 块内 Jun Ebihara（1987 年 Sony NEWS 工作站 4.2BSD 入门、1993 年创办 SOM、日本 NetBSD 邮件列表约 872 订户）与 itojun（萩野纯一郎）当事人证词线索可靠，转写讹误（Jun Ibehara 等）均已带存疑脚注。
- 行 25“总纲第 10 条”含规范语“动手者创造历史”且编号相符；PODCAST 块 5 条史观标签（总纲 10/4/6/10/4）全部与权威编号表相符——均不计缺陷。
- 东大 1991 年出版 4.3BSD 日文译本、早稻田 1995 年开课等细目外部不可核验，原文为平铺陈述，建议后续回填出处（暂不计缺陷）。
- 机械旗标复核留痕：flags=[UNLISTED_NOT_IN_SUMMARY]，经 grep SUMMARY.md 证实第 332 章条目族自概述.md 起（行 2845-2856），无 index.md 行。
- 编码合规：UTF-8 无 BOM、LF；弯引号正确。
