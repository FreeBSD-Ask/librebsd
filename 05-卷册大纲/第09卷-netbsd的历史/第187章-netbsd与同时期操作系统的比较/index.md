---
chapter: 第 187 章
id: CH187
volume: 第09卷-netbsd的历史
---

# 第 187 章 netbsd与同时期操作系统的比较

## 要点

- FreeBSD 长期聚焦 i386/amd64 与 ARM64，明确放弃对冷门架构的支持；NetBSD 维护 50+ 移植端口，覆盖冷门架构（VAX、HP300、sun2/sun3 等）；两项目在 1990 年代后逐步形成 “广度 vs 深度” 的分化
- OpenBSD 自 1996 年 fork 后聚焦 “安全审计” 与 “默认安全”，NetBSD 则采取 “机制提供但不强制” 的安全哲学；OpenBSD 的主动审计文化（如 strlcpy/strlcat 提出）反向影响 NetBSD
- Linux 凭借 GPLv2 强制回馈机制与企业投入（Red Hat、IBM、Intel 等）在 2000 年代快速扩张生态；NetBSD 的 BSDL 允许商业闭源 fork 但缺乏企业回馈机制，生态扩张缓慢；从学术文献计量视角看，本章涉及 NetBSD 与同时期操作系统的比较叙事，其参考文献基础来自资料数据库.duckdb references 表——该表收录 16,867 条参考文献，其中年份字段提
- Apple Darwin/XNU 用户空间大量复用 FreeBSD 代码但内核为混合内核；Solaris、AIX、HP-UX 等商业 UNIX 在 2000 年代逐步衰退，NetBSD 在嵌入式与教学场景填补部分空缺
- NetBSD 在嵌入式市场（路由器、NAS、消费电子）的定位介于 VxWorks/QNX 等商业 RTOS 与嵌入式 Linux 之间；Wind River VxWorks 长期主导硬实时市场，嵌入式 Linux 在 2000 年代后快速扩张，NetBSD 占据小众但稳定的 “可移植 BSD” 位置

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4001] 卷“第09卷-netbsd的历史”第 187 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- FreeBSD 实际支持的平台数量需考据，部分叙事夸大了 FreeBSD 的 “单一平台” 程度。L1.1.2 查询的占比基于四大 BSD src 仓库合计 commit 量，dragonflybsd-src 在 2003 年后才加入，故 1993-2002 年占比实为 freebsd-src+netbsd-src+openbsd-src 三仓库合计；1995 年占比骤降（58.88%）与 Ope
- OpenBSD 与 NetBSD 的安全漏洞统计比较需对照 CVE 数据库核验，不得仅依项目自述
- “Linux 击败 BSD” 的叙事需考据，避免事后叙事化，需呈现 1990-2000 年代的具体历史语境。L7.3.1 查询的 BSD commit 量为 freebsd-src+netbsd-src+openbsd-src+dragonflybsd-src 四仓库合计，Linux commit 量为 linux-stable 单仓库，二者口径不完全对等（Linux 单仓库涵盖全部子系统，BSD
- Darwin 与 FreeBSD 的代码共享程度需考据，部分叙事夸大了共享程度
- 许可证与生态扩张的因果关系需审慎考据，避免简化为 “许可证决定论”

## 文献

- NetBSD/doc/PLATFORMS 文件 [EB/OL]. <https://github.com/NetBSD/src/blob/trunk/doc/PLATFORMS>（原始链接失效，互联网档案馆无存档）；FreeBSD Release Notes 中 platforms supported 章节 [EB/OL]. <https://www.freebsd.org/releases/>；tech-platforms 邮件列表 [EB/OL]. <https://mail-index.netbsd.org/tech-platforms/>；netbsd.duckdb 数据分析·宏观趋势统计.md §L1.1.2（netbsd-src 占四大 BSD src 仓库合计 commit 比例 1993-2002） ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1993-2026 年间：1,294,851 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- OpenBSD 主页 “Only two remote holes in a heck of a long time!” 声明 [EB/OL]. <https://www.openbsd.org/>；strlcpy(3)/strlcat(3) 手册页 [EB/OL]. <https://man.openbsd.org/strlcpy>；NetBSD security-announce 邮件列表 [EB/OL]. <https://mail-index.netbsd.org/security-announce/> ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- Linux Foundation Annual Reports [EB/OL]. <https://www.linuxfoundation.org/reports/>；NetBSD Foundation 年度报告 [EB/OL]. <https://www.NetBSD.org/foundation/reports/>；GPLv2 文本 [EB/OL]. <https://www.gnu.org/licenses/gpl-2.0.txt>；BSD License 文本 [EB/OL]. <https://opensource.org/licenses/BSD-3-Clause>；netbsd.duckdb 数据分析·衍生项目与跨项目对比分析.md §L7.3.1（BSD 四仓库合计 vs Linux commit 量 2008/2020/2026）；netbsd.duckdb 数据分析·文献计量学分析.md Task 22（统计结论 C-41：references 表总数 16,867、统计结论 C-42：年份提取率 44.42%）、Task 23（统计结论 C-44：Top 10% 章节占 28.23%、Gini 0.3913） ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- Apple Darwin 开源档案 [EB/OL]. <https://opensource.apple.com/>；OpenSolaris 项目档案 [EB/OL]. <https://www.openindiana.org/>；IDC/Gartner 商业 UNIX 市场份额报告 [EB/OL]. <https://www.idc.com/> ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- Wind River VxWorks 产品文档 [EB/OL]. <https://www.windriver.com/products/vxworks>；QNX 产品文档 [EB/OL]. <https://blackberry.qnx.com/>；NetBSD 嵌入式部署案例 [EB/OL]. <https://www.NetBSD.org/gallery/embedded.html>（原始链接失效，互联网档案馆无存档） ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- BSD License 文本 [EB/OL]. <https://opensource.org/licenses/BSD-3-Clause>；GPLv2 文本 [EB/OL]. <https://www.gnu.org/licenses/gpl-2.0.txt>；FSF 对许可证的解读 [EB/OL]. <https://www.fsf.org/licensing/>；OSI 对许可证的解读 [EB/OL]. <https://opensource.org/licenses/>；Apple Darwin 仓库 [EB/OL]. <https://opensource.apple.com/>；Juniper Junos 文档 [EB/OL]. <https://www.juniper.net/documentation/> ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- 上述第 16.8.1-16.8.4 节所有文献综合；项目史观总纲第 4、5、7、8、13、22、23 条；第 82A 章第 82.6 节详细考据 ［A］### 史纲映射本节在项目统摄史观 29 章 191 子节中的主要承载映射：1.md 第七章 “文化历史哲学”——本节为 NetBSD 习俗特殊文化作为文化形式主义建构的核心考据，“文化即形式主义” 总纲在 “Of course it runs NetBSD” 口号、pkgsrc 季度分支、Foundation 选举、Tainted Code 政策、port naming 约定等习俗中的实例化；1.md 第二十五章 “总纲”——本节映射多条总纲（总纲 4 分离聚合、总纲 9 经验优先、总纲 13 法律与道德、总纲 22 知识注定过时、总纲 7 理论必须自反、总纲 23 一切历史写作都是基于哲学设定的历史小说），含自反性声明；1.md 第二十九章 “元哲学”——本节以 5 条 NetBSD 习俗为经验材料检验项目统摄史观，同时以项目统摄史观为分析工具释读 NetBSD 习俗，构成双向检验的方法论实验。### 核心内容#### 186.8.1 “Of course it runs NetBSD” 口号传统与 port naming 约定（i386、amd64、evbarm、sparc64、vax、pmax、hp300、mac68k、amiga、atari 等 50+ ports）#### 186.8.2 pkgsrc 季度分支传统（1997-08 启用，2003-12-02 pkgsrc-pmc 成立，扩展至 Solaris/Linux/Darwin/FreeBSD/OpenBSD/DragonFlyBSD 等 16+ 平台）#### 186.8.3 NetBSD Foundation 选举传统（1995 年注册，2 年任期，Board of Directors 由 NetBSD Developer 社区选举，IRC 召开 AGM）#### 186.8.4 Tainted Code 政策传统：AI 生成代码的伦理边界（2024-05 修订 CoC 引入 “tainted code” 概念，借鉴 Linux 内核 “tainted kernel”）---## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：NetBSD 特性
- NetBSD Project. 10 years of pkgsrc - Alistair Crooks [EB/OL]. (2007-10-17)[2026-07-24]. **<https://www.netbsd.org/gallery/10years.html#alcrooks>**; NetBSD Project. pkgsrc Guide [EB/OL]. [2026-07-27]. **<https://www.netbsd.org/docs/pkgsrc/>**; 本项目既有考据记录 `03-原始史料库/06-考据记录/20260724_alistair-crooks-netbsd-1x-growth.md`; 本项目既有考据记录 `03-原始史料库/06-考据记录/20260727_rumors-netbsd.md` ［A］### 史纲映射本节在项目统摄史观 29 章 191 子节中的主要承载映射：1.md 第七章 “文化历史哲学”——本节为 NetBSD 传言与都市传说作为文化形式主义建构的核心考据，“文化即形式主义” 总纲在 “Of course it runs NetBSD” 口号、Theo de Raadt 驱逐事件、Tainted Code 政策等传言中的实例化；1.md 第二十五章 “总纲”——本节映射 5 条总纲（总纲 9 经验优先、总纲 15 文化即形式主义、总纲 19 解释学循环、总纲 7 理论必须自反、总纲 23 一切历史写作都是基于哲学设定的历史小说），含自反性声明；1.md 第二十九章 “元哲学”——本节以 6 条 NetBSD 传言为经验材料检验项目统摄史观，同时以项目统摄史观为分析工具释读 NetBSD 传言，构成双向检验的方法论实验。### 核心内容#### 186.9.1 NetBSD 相关键传言与都市传说考据（6 条）——可移植性口号、Theo de Raadt 驱逐、Tainted Code 政策、pkgsrc 鼻祖地位、NASA 航天器应用等
- NetBSD 官方历史页面、Ports 列表、Adam Glass 1994 邮件、OpenBSD FAQ、pkgsrc Guide、本项目既有考据记录 `03-原始史料库/06-考据记录/20260727_rumors-netbsd.md`

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
