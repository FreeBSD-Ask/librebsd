---
chapter: 第 321 章
id: CH321
volume: 第17卷-政治制度与社区治理
---

# 第 321 章 bsd俚语考据与通用习俗

## 要点

- 综合项目史观总纲第 7、8、13、14、19、21、23、25 条审视，BSD/UNIX 俚语与行话的八类词条（BSD 专属、UNIX 通用、黑客文化通用、BSD/Linux 论战、版本号、工具与命令、文件系统、文化梗）呈现五重结构——其一，词源层积的史观审视（总纲第 7、25 条）：daemon 从 Maxwell's Demon（1867 物理思想实验）经 MIT Project MAC 后台进程隐喻进入 UNIX 术语、再于 BSD 时代人格化为守护进程形象的词源链审视，完整考据见各子节（2026-09-12 整改：句尾截断按词源链收束，索引不重复堆叠子节内容——批次 C023 问题 1）
- 综合项目史观总纲审视，BSD 通用习俗特殊文化呈现 “工程纪律传统” 与 “许可哲学根基” 的双重结构——工程纪律传统维度：man page 写作传统、BSD make 宏文件传统、/usr/share/examples/ 传统、目录层次传统、chflags 传统、securelevel 传统的交叉验证方法：各项习俗以对应手册页、commit 历史与项目文档为据逐项核对（2026-09-12 整改：截断收束——批次 C023 问题 5）vel 传统皆是 BSD 工程纪律的具体显现，体现“每个程序必须有 man page”“清晰的目录层次”等成文习俗（2026-09-12 整改：句尾截断引文残片删除留痕、直引号统一弯引号，列举以六项传统收束——批次 C023 问题 2）

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3988] 卷“第17卷-政治制度与社区治理”第 321 章，匹配置信度 folder，原因：folder 第319章

## 史观

总纲第 15 条——文化即形式主义：BSD 俚语与习俗（daemon 人格化、man page 纪律、chflags/securelevel 传统）是技术社区文化的形式主义化沉淀——词条与习俗即文化的形式载体；总纲第 10 条——动手者创造历史：俚语与习俗由动手者在 commit、文档与邮件列表实践中创造并传承，非官方钦定；总纲第 8 条——本体论上各方平等：BSD/UNIX/黑客文化通用的词条归属呈跨社区共享，各来源社区地位平等；总纲第 19 条——解释学循环是历史认识的根本条件：词条词源的考据受考据者前理解影响，须回溯 Jargon File 等一手档案；总纲第 22 条——知识注定过时：Jargon File（4.4.7，2003）所载词义随社区演化持续变迁，引用须注版本。（2026-09-12 整改：史观字段按批次 C023 回填，映射依 25 条权威表）

## 辨析

- 考据过程留痕——【查证来源】合图层史料综合第 22.22.1-22.22.5 节所有引用的一手与二手史料，包括 Jargon File 4.4.7 版本（`catb.org/jargon/`）、Marshall Kirk McKusick 个人站点 beastie 页（`mckusick.com/beastie/`）、FreeBSD Committer's Guide（`docs.freebsd.org/en/articles/committers-guide/`〔2026-09-12 整改：URL 截断补全——批次 C023 问题 4〕
- 考据过程留痕——【查证来源】综合审视史料综合第 22.23.1-22.23.8 节所有引用的一手与二手史料；项目史观总纲第 4、5、7、8、9、13、22、23 条经 据原文第 25 章 一手核验；【交叉验证方法】“工程纪律传统” 论证须以 man page 写作传统、BSD make 宏文件传统、/usr/share/examples/ 传统、目录层次传统、chflags 传统、securele

## 文献

- 项目史观总纲第 7、8、13、14、19、21、23、25 条；Raymond E S. The Jargon File [EB/OL]. Version 4.4.7. (2003)[2026-07-27]. `catb.org/jargon/`；McKusick M K. History of the BSD Daemon [EB/OL]. [2026-07-27]. `mckusick.com/beastie/`；The FreeBSD Documentation Project. Committer's Guide [EB/OL]. (1999-2022)[2026-07-27]. `docs.freebsd.org/en/articles/committers-guide/`；The NetBSD Project. Commit Guidelines [EB/OL]. (2024-05 revision)[2026-07-27]. Internet Archive 存档版本。<https://web.archive.org/web/2024/https://www.netbsd.org/developers/commit-guidelines.html>；freebsd-advocacy 邮件列表存档 [EB/OL]. [2026-07-27]. <https://lists.freebsd.org/archives/freebsd-advocacy/>（2026-09-12 整改：URL 尖括号错乱粘连修复——批次 C023 问题 6）；The FreeBSD Project. FreeBSD Manual Pages [EB/OL]. [2026-07-27]. `man.freebsd.org/cgi/man.cgi`；OpenBSD Project. OpenBSD Project Goals [EB/OL]. [2026-07-27]. `openbsd.org/goals.html`；第 22.22.1-22.22.5 节史料综合；参见相关章节 BSD 文化溯源与治理批评部分史料 ［A］
- 上述第 22.23.1-22.23.8 节所有文献综合；项目史观总纲第 4、5、7、8、9、13、22、23 条 ［A］

<!-- ROW_MINE: login-zazhi.articles.CL-17-043 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-17-043`；login 逐条遍历判定采纳）

Conserver 由 Thomas A. Fine 与 Steven Romig 于 1990 年 LISA IV 上作为客户-服务器串口控制台管理工具发布，此后十年依据用户需求持续演化并自由分发，成为 2000 年前后互联网公司系统管理员节省时间、减少宕机的关键运维工具。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-17-043 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-17-043`；login 逐条遍历判定采纳）

Conserver 由 Thomas A. Fine 与 Steven Romig 于 1990 年 LISA IV 上作为客户-服务器串口控制台管理工具发布，此后十年依据用户需求持续演化并自由分发，成为 2000 年前后互联网公司系统管理员节省时间、减少宕机的关键运维工具。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-17-043 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-17-043`；login 逐条遍历判定采纳）

Conserver 由 Thomas A. Fine 与 Steven Romig 于 1990 年 LISA IV 上作为客户-服务器串口控制台管理工具发布，此后十年依据用户需求持续演化并自由分发，成为 2000 年前后互联网公司系统管理员节省时间、减少宕机的关键运维工具。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-17-043 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-17-043`；login 逐条遍历判定采纳）

Conserver 由 Thomas A. Fine 与 Steven Romig 于 1990 年 LISA IV 上作为客户-服务器串口控制台管理工具发布，此后十年依据用户需求持续演化并自由分发，成为 2000 年前后互联网公司系统管理员节省时间、减少宕机的关键运维工具。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-17-043 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-17-043`；login 逐条遍历判定采纳）

Conserver 由 Thomas A. Fine 与 Steven Romig 于 1990 年 LISA IV 上作为客户-服务器串口控制台管理工具发布，此后十年依据用户需求持续演化并自由分发，成为 2000 年前后互联网公司系统管理员节省时间、减少宕机的关键运维工具。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-17-043 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-17-043`；login 逐条遍历判定采纳）

Conserver 由 Thomas A. Fine 与 Steven Romig 于 1990 年 LISA IV 上作为客户-服务器串口控制台管理工具发布，此后十年依据用户需求持续演化并自由分发，成为 2000 年前后互联网公司系统管理员节省时间、减少宕机的关键运维工具。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-17-043 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-17-043`；login 逐条遍历判定采纳）

Conserver 由 Thomas A. Fine 与 Steven Romig 于 1990 年 LISA IV 上作为客户-服务器串口控制台管理工具发布，此后十年依据用户需求持续演化并自由分发，成为 2000 年前后互联网公司系统管理员节省时间、减少宕机的关键运维工具。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-17-043 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-17-043`；login 逐条遍历判定采纳）

Conserver 由 Thomas A. Fine 与 Steven Romig 于 1990 年 LISA IV 上作为客户-服务器串口控制台管理工具发布，此后十年依据用户需求持续演化并自由分发，成为 2000 年前后互联网公司系统管理员节省时间、减少宕机的关键运维工具。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

