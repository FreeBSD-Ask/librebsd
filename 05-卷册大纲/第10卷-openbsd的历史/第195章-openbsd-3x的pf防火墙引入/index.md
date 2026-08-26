---
chapter: 第 195 章
id: CH195
volume: 第10卷-openbsd的历史
---

# 第 195 章 openbsd-3x的pf防火墙引入

## 要点

- pf 2001 年原始公告与 CVS commit log 是研究 pf 诞生的核心史料；公告由 de Raadt 与 Hartmeier 发布至 OpenBSD 邮件列表；commit log 反映 Hartmeier 等的早期开发节奏；统计结论印证——openbsd.db openbsd-src 仓库总 commit 数 245,904（统计结论 C-05），3.x 时期（2001-2004）
- OpenBSD 3.1-3.6 安全特性（W^X、SSP、privilege separation、swap encryption）的 commit 记录是研究此时期安全演进的核心史料；Provos、Etoh、de Raadt 等的 commit 反映开发节奏；考据需对照 CVS commit log 与 Release Notes；统计结论印证——openbsd.db openbsd-src 仓
- OpenBSD 提出“在默认安装中 6 年仅两个远程漏洞”口号，最初由 de Raadt 在 OpenBSD 网站上宣称；口号中的“远程漏洞”指默认安装下可被远程攻击者利用的漏洞；口号随时间演变，至 2000 年代中期改为“多年无远程漏洞”
- 批评者（如 CVE 数据库研究者、Linux 社区成员）指出 OpenBSD 口号依赖于严格定义——“默认安装”排除了 ports 与第三方软件，“远程漏洞”排除了本地漏洞与权限提升漏洞；批评者认为 OpenBSD 实际安全记录虽有改进，但口号夸大宣传
- OpenBSD 社区回应批评时强调“默认安装”的定义明确且一致——指基本系统安装后未启动第三方服务的状态；de Raadt 在邮件列表与演讲中多次反驳批评者；OpenBSD 社区认为批评者忽略了 OpenBSD 在安全文化上的贡献

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4023] 卷“第10卷-openbsd的历史”第 195 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- pf 1.0 的具体发布日期存在 2001.12.1 与 2001.12.3 两种说法——需对照 OpenBSD 官方公告核验；openbsd.db 查询 L1.1.1 局限：openbsd-src 为 GitHub 镜像，commit 量可能滞后于 OpenBSD CVS 主仓；L1.1.1 报告仅显示 23 仓库 572 行中的前 30 行（dragonfly 仓库），openbsd-src 
- 安全特性 commit 的具体作者归属需考据——部分大型 commit 由多人协作，难以单一归属；commit log 中的安全相关 tag 需考据；**统计局限性标注**——C-10 Mann-Kendall 趋势检验基于 1993-2026 年全期月度 commit 量序列，slope = −0.24/月 是全期趋势，3.x 时期（2001-2004）的局部趋势须结合时间窗口切片分析，全期下降
- “两个远程漏洞”的具体指代在不同叙事中存在差异——部分资料称是 OpenBSD 2.6 之前的两个漏洞，部分称是历史漏洞，需对照 OpenBSD 官网核验
- 批评者的代表性需考据——单一批评者不等于社区共识；“严格定义”的具体范围（如是否包括本地漏洞）需对照 OpenBSD 官网核验
- OpenBSD 社区的回应是否具有说服力在不同观察者中存在分歧——需对照多源核验

## 文献

- OpenBSD 3.0 公告；OpenBSD CVS 仓库；Hartmeier pf 历史文章；openbsd.db 查询 L1.1.1 与 L1.1.2（来源：原材料/研究/bsd 仓库分析/数据分析/宏观趋势统计.md §L1.1.1、§L1.1.2）；统计分析报告：描述性统计.md SubTask 2.1 [R/OL]. 2026-07-27. 文件路径：`c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\描述性统计.md`；SQL 查询：`SELECT COUNT(*) FROM commits WHERE repo_name='openbsd-src'`. openbsd.db [DB/OL]. 查询日期：2026-07-27[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2001-2001 年间：18,985 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- OpenBSD CVS 仓库；OpenBSD 邮件列表；统计分析报告：推断性统计.md Task 5 + Task 10 [R/OL]. 2026-07-27. 文件路径：`c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\推断性统计.md`；描述性统计.md SubTask 2.3 [R/OL]. 2026-07-27. 文件路径：`c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\描述性统计.md`；Python 统计脚本：`script/phase2_inferential.py`. Task 5 Mann-Kendall 趋势检验 + Task 10 Gini 系数 Bootstrap. 执行日期：2026-07-27 ［A］#### 194.3“默认安装仅两个远程漏洞”口号的演变——OpenBSD 提出“在默认安装中 6 年仅两个远程漏洞”的口号，该口号长期受批评，批评者认为计数依赖于严格定义
- OpenBSD 官网 Security 页面；Wayback Machine 快照；de Raadt 演讲[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- CVE 数据库；Bugtraq/Full Disclosure 邮件列表；OpenBSD Security 页面 ［A］
- OpenBSD 邮件列表；de Raadt 演讲；OpenBSD FAQ ［A］
- OpenBSD 邮件列表存档；OpenBSD 官网；Wayback Machine ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2002-2004 年间：48,812 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- OpenBSD 邮件列表；OpenBSD 官网；Wayback Machine ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1996-2004 年间：112,478 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 6 条与第 8 条原文）；OpenBSD CVS 仓库；FreeBSD CVS/Git 仓库（PF 相关）；OpenBSD 邮件列表存档 ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1996-2004 年间：112,478 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 8 条与第 13 条原文）；OpenBSD 邮件列表存档 [EB/OL]. **<https://marc.info/?l=openbsd-misc**>；FreeBSD CVS/Git 仓库（`sys/netpfil/pf/`）；OpenBSD security.html [EB/OL].** <https://www.openbsd.org/security/**>；FreeBSD TrustedBSD 项目文档；NSA SELinux 项目文档 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1995-2026 年间：1,289,123 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
