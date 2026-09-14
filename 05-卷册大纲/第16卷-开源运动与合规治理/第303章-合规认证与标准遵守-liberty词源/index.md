---
chapter: 第 303 章
id: CH303
volume: 第16卷-开源运动与合规治理
---

# 第 303 章 合规认证与标准遵守-liberty词源

## 要点

- 汉语“自由”近代由严复《群己权界论》（1903，译 Mill《On Liberty》）引入并定型；“自由”同时涵盖 liberty（政治/制度自由）与 freedom（活动自由）两义；BSD 社区中文语境普遍以“自由”兼指两者。本书为消解歧义，以“自由（liberty）”标注制度化义、以“自由（freedom）”标注活动义
- 2004 年 IEEE/Open Group 授权 FreeBSD 使用 POSIX 文档材料一事经 OSNews 与 IEEE 官方公告交叉验证；“C99 and POSIX Conformance Project”的具体产出文档在邮件列表中只有零散提及，是否最终完成存疑
- FreeBSD 跟踪 C 标准切换的具体时间线需交叉验证 Makefile、release notes 与 quarterly reports，C99/C11/C17/C23 的采纳并非同步而是渐进
- KAME 项目曾与 UNH-IOL（University of New Hampshire InterOperability Laboratory）合作进行 IPv6 一致性测试，但具体测试报告与结果在公开档案中零散
- LSB 测试套件在 FreeBSD 上的运行结果公开档案稀缺，是否存在正式 LSB 认证报告需考据

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3626] 卷“第16卷-开源运动与合规治理”第 303 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3627] 卷“第16卷-开源运动与合规治理”第 303 章，匹配置信度 curated，原因：curated token rule

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 译名接受史——严复初拟“自繇”后定“自由”；“自由”是否亏损 liberty 的制度义（汉语中不显）——本书以加注方式处理该语义亏损
- 项目是否产出过正式 conformance 报告需查 FreeBSD CVS/SVN 仓库中的 standards/ 目录历史；OSNews 报道是否提及 1400 接口数需原文核对
- FreeBSD 10.0 是否默认 C99 存在不同说法，需查 share/mk/bsd.sys.mk 中的 CSTD 默认值；C23 在 FreeBSD 15 中的实际支持范围需区分 clang 与 gcc
- UNH-IOL 测试是否覆盖 FreeBSD 集成后的 KAME 代码需查测试报告具体版本；KAME 自身的测试套品 vs UNH-IOL 测试需区分
- FreeBSD 是否曾正式申请 LSB 认证需查 Linux Foundation 历史认证记录；lsb-release 命令在 FreeBSD ports 中的可用性需确认

## 文献

- 严复译本；Mill《On Liberty》；汉语词汇史研究 ［C/A］
- OSNews 2004-06-02“FreeBSD Gets POSIX License”；IEEE 1003.1 授权文本副本；FreeBSD Foundation 历年年报中的 standards 条目 ［B］
- FreeBSD 10.0 Release Notes；FreeBSD 15.0 Release Notes；ISO/IEC 9899 历版本对照表［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- UNH-IOL IPv6 conformance test specifications；IETF RFC 4294 IPv6 Node Requirements［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Linux Foundation LSB 认证档案；FreeBSD ports/misc/lsb-release［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:linux_kernel.duckdb -->
> **数据库引用（linux_kernel.duckdb）**：本子节对应 linux_kernel 代码仓库。> 2003-2026 年间：1,474,325 次提交。> 仓库总览：1,474,341 次提交，39,865 位贡献者（contributors 表行数，1970-01-01 至 2026-08-24）。
- FreeBSD Foundation Board Meeting Minutes；freebsd-advocacy 邮件列表存档 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2003-2026 年间：1,102,265 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- NIST CMVP Active Modules 数据库；CCCS CSPN 数据库［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- dangan-20260908 消解回写 -->
- Austin. Group 主页 [EB/OL]. (2026-07-23 访问). <https://www.opengroup.org/austin/>[EB/OL]. 2026. ［待核·needs_fix］［DKC-0564→fulltext:5555］
<!-- /dangan-20260908 -->
