---
chapter: 第 28 章
id: CH28
volume: 第02卷-伯克利的岁月
---

# 第 28 章 vi与cshell的诞生

## 要点

- **vi** 命名起源的通行说法是 “vi 代表 visual（可视模式）”，此说法有 2BSD 一手发布说明支持——1979 年 2BSD 发布说明（TUHS 归档 2bsd_announcement.pdf）将 vi 描述为 ex 编辑器的 "screen editing facilities"（屏幕编辑功能），且 2BSD 随附文档标题为 "An Introduction to Displa
- csh 的历史替换与作业控制功能影响了后续 shell 设计——tcsh（Ken Greer **1981 年 12 月** 将 TENEX 风格文件名补全合并入 csh）延续 csh 谱系（Arch Linux man **tcsh(1)** 原文 "Ken Greer, HP Labs, 1981. File name completion."），bash（Brian Fox **1989 年
- 2BSD 是 PDP-11 平台上最后的主要 BSD 版本，1980 年代 BSD 主力转向 VAX，PDP-11 上的 2BSD 进入维护模式，但 2BSD 的代码与工具持续影响后续版本
- vi 的模态设计影响了后续编辑器——vim（Bram Moolenaar **1988 年** 在 Amiga 上开始开发，**1991 年 11 月** 首次公开发布 Vim 1.14 于 Fred Fish Disk #591，最初名为 "Vi IMitation"，**1992 年** Vim 1.22 移植到 UNIX/MS-DOS 后更名为 "Vi IMproved"）、nvi（Keit
- **csh 手册页**首次出现于 **2BSD**（man page 内部日期 **1979-02-24**），由 Bill Joy 编写，对应 csh 1.0 版本；**1BSD**（1978.3.9，TUHS 归档 1BSD/man1/ 目录确认）不含 csh man page，1BSD/man1/ 仅含 cd.1、lib.1、login.1、sh.1（Bourne Shell）、su.8、w

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3811] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 folder，原因：folder 第28章
- [DB:references_fulltext:chapter_matches:chmatch_3812] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 folder，原因：folder 第28章
- [DB:references_fulltext:chapter_matches:chmatch_3890] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 folder，原因：folder 第28章
- [DB:references_fulltext:chapter_matches:chmatch_3891] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 folder，原因：folder 第28章
- [DB:references_fulltext:chapter_matches:chmatch_3914] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 folder，原因：folder 第28章
- [DB:references_fulltext:chapter_matches:chmatch_3919] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 folder，原因：folder 第28章
- [DB:references_fulltext:chapter_matches:chmatch_3934] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 folder，原因：folder 第28章
- [DB:references_fulltext:chapter_matches:chmatch_3958] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 folder，原因：folder 第28章
- [DB:references_fulltext:chapter_matches:chmatch_1551] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- [考据完成：2026-07-28 该处辨析所涉存疑点经穷尽联网考据，属史料缺口，详见上下文分析] vi 命名起源在三个一手访谈来源中的具体陈述差异本节未能完整比对，原因如下：(1) Joy 2011 CHM 口述史 PDF 共 27 页，本节仅获取到前 6 页（至 BSD 与 VAX 引入部分），尚未触及 vi 命名讨论的具体段落，需后续获取完整 PDF 查阅 vi 命名相关段落；(2) McKu
- bash 对 csh 功能的吸收程度在不同 GNU 文档中表述不一，需核对 bash 源代码注释；Ken Greer 1981 年合并 tcsh 至 csh 工作的所属机构在不同来源中表述存在分歧——Arch Linux man tcsh 原文标注 "HP Labs, 1981"（机构为 HP Labs），codearchaeology.dev 与 linux.fandom 等二手来源表述为 "C
- PDP-11 上 2BSD 的最后维护版本号在不同史料中不一致，需核对伯克利发布记录
- vim 与 vi 的兼容性程度在不同版本中存在差异，需核对 vim 兼容性文档；vim 首次公开发布时间为 1991 年 11 月（Fred Fish Disk #591），1988 年仅为 Moolenaar 在 Amiga 上的个人开发起点；nvi 为 4.4BSD-Lite（1994 年春发布）而开发，~~先前叙述 “nvi（Keith Bostic 1992 年）” 系年份错误~~（修正：
- [考据完成：2026-07-29 经 TUHS utree 各版本 csh man page 直接访问核查，原 “具体版本号对照需后续从 TUHS 归档 tar.gz 包中提取比对” 的存疑标注现予以撤销并改为确证] csh man page 各版本 TH 行与内部日期已通过 TUHS utree 直接访问逐一核查确认：(1) **2BSD csh.u**（1979-02-24，TH 行 `.TH

## 文献

- Joy, W. (1979) "2BSD Release Announcement"（TUHS 归档 2bsd_announcement.pdf，<https://www.tuhs.org/Archive/Distributions/UCB/Documentation/2bsd_announcement.pdf>）；Joy, W. (1978) "An Introduction to Display Editing with vi"（2BSD 随附手册）；Joy, Bill. Oral History [EB/OL]. Computer History Museum, 2011-03-30. Catalog Number 102743073. <https://www.computerhistory.org/collections/catalog/102743073/>；BSD Now. Episode 278: The Real McCoy [audio podcast]. 2018-12-27. <https://www.bsdnow.tv/278> ［A］
- Arch Linux man **tcsh(1)** "AUTHORS" 节（HP Labs 1981 标注）；Fox, B. (1989) "Bash Reference Manual"；Loukides, M. (1990) "Programming with GNU Software"；Falstad, P. (1990) zsh 0.1 发布公告，comp.sources.misc 新闻组（zsh.sourceforge.io 项目历史存档） ［A］
- DEC (1990) "PDP-11 End of Life Announcement"；伯克利 CSRG 维护日志[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- Moolenaar, B. (1991) Vim 1.14 首次公开发布（Fred Fish Disk #591）；Moolenaar, B. (1992) Vim 1.22 移植到 UNIX 并更名 "Vi IMproved"；Bostic, K. (1994) nvi for 4.4BSD-Lite；Joy, W. (1978) "vi User's Manual"；Kirkendall, S. (1990) elvis editor[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- Joy, W. (1978) "An Introduction to the C Shell"（2BSD 随附手册，TUHS 归档 2bsd.tar.gz）；**TUHS utree 各版本 csh man page 直接链接**（2026-07-29 联网核查确认均可访问）：2BSD csh.u（<https://www.tuhs.org/cgi-bin/utree.pl?file=2BSD/man/csh.u>）；3BSD csh.1（<https://www.tuhs.org/cgi-bin/utree.pl?file=3BSD/usr/man/man1/csh.1>）；4BSD csh.1（<https://www.tuhs.org/cgi-bin/utree.pl?file=4BSD/usr/man/man1/csh.1>）；4.1cBSD csh.1（<https://www.tuhs.org/cgi-bin/utree.pl?file=4.1cBSD/usr/man/man1/csh.1>）；4.2BSD csh.1（<https://www.tuhs.org/cgi-bin/utree.pl?file=4.2BSD/usr/man/man1/csh.1>）；4.3BSD csh.1（<https://www.tuhs.org/cgi-bin/utree.pl?file=4.3BSD/usr/man/man1/csh.1>）；4.3BSD-Reno csh.1（<https://www.tuhs.org/cgi-bin/utree.pl?file=4.3BSD-Reno/src/bin/csh/csh.1>）；4.4BSD csh.1（<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/src/bin/csh/csh.1>）；1BSD/man1/ 目录（<https://www.tuhs.org/cgi-bin/utree.pl?file=1BSD/man1>，确认 1BSD 不含 csh man page）；2BSD/man/ 目录（<https://www.tuhs.org/cgi-bin/utree.pl?file=2BSD/man>，确认 2BSD man page 均使用 `.u` 后缀）；TUHS 归档 tar.gz 包：2bsd.tar.gz（<https://www.tuhs.org/Archive/Distributions/UCB/2bsd.tar.gz>）、3bsd.tar.gz（<https://www.tuhs.org/Archive/Distributions/UCB/3bsd.tar.gz>）、4.2BSD/（<<https://www.tuhs.org/Archive/Distributions/UCB/4.2BSD/）；项目本地> `03-原始史料库/02-man源与posix仓库/01-repos/openbsd-src/bin/csh/csh.1`（OpenBSD 现代 csh man page） ［A］
