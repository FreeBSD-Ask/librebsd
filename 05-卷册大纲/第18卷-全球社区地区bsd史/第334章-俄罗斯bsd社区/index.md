---
chapter: 第 334 章
id: CH334
volume: 第18卷-全球社区地区bsd史
---

# 第334章 俄罗斯bsd社区

## 要点

- 俄罗斯 FreeBSD 使用起始于 1993-1994 年苏联解体后，早期由 RELCOM 网络时代的 Unix 工程师引入；DemOS（Democratic OS，1990-1993 年基于 4.3BSD-Reno）为俄罗斯本土 BSD 操作系统的先驱，与 FreeBSD 共享 BSD 血缘但独立发展；1995 年后 FreeBSD 逐步取代 DemOS 成为俄罗斯主流 BSD 系统
- 演变分三阶段——1990-1993 年的 DemOS 期（本土 BSD 系统）、1994-2000 年的过渡期（DemOS 与 FreeBSD 并存）、2001 年后的 FreeBSD 主导期；演变与俄罗斯互联网商业化同步
- 苏联技术传统对 BSD 采用的影响主要表现为 1980 年代 Unix 引入（通过 Demos 公司与 Elbrus 项目）、苏联解体后 Unix 社区去中心化、强数学传统塑造俄语 BSD 社区的高技术水平
- 后苏联技术文化演变分三阶段——1990 年代的去中心化期、2000-2010 年的商业化期、2011 年后的政治化期（“主权互联网” 政策）；演变与俄罗斯政治经济变迁同步
- 俄罗斯 BSD 史料来源包括 DemOS 项目档案、freebsd-russian 邮件列表、Yandex 等公司技术博客、参与者口述访谈；俄语史料与英语史料存在叙事差异；史料辨析须警惕意识形态偏差

## 史观

- 总纲第 4 条——分离是新的聚合的开始，苏联解体后的去中心化催生俄罗斯 BSD 社区的多元化发展
  - 辨析：DemOS 与 FreeBSD 的关系须经原始代码档案核查；“1993-1994 年” 的起始时间须经 RELCOM 历史文档验证；DemOS 是否完全基于 4.3BSD-Reno 需考据
  - 文献：DemOS 项目档案；RELCOM 网络历史文档；<freebsd-russian@FreeBSD.org> 邮件列表存档 ［A］
- 边缘者的贡献被中心叙事遮蔽，俄语 BSD 社区贡献者须从翻译项目档案中重建
  - 辨析：社区活跃度的量化数据须经邮件列表统计核查
  - 文献：freebsd-russian 邮件列表；FreeBSD.org.ru 镜像站档案 ［A］

## 334.1.2 从 DemOS 到 FreeBSD 的演变

- 要点：演变分三阶段——1990-1993 年的 DemOS 期（本土 BSD 系统）、1994-2000 年的过渡期（DemOS 与 FreeBSD 并存）、2001 年后的 FreeBSD 主导期；演变与俄罗斯互联网商业化同步
- 史料：DemOS 项目档案、Yandex 与 Mail.ru 早期技术栈文档、freebsd-russian 邮件列表 ［A］
- 史观：总纲第 6 条
- freebsd-russian 邮件列表；FreeBSD.org.ru 镜像站档案 ［A］

## 334.2.2 俄语技术文化的特征

- 要点：俄语技术文化的特征包括强数学传统（源于苏联数学教育体系）、与西方开源社区的意识形态张力、封闭性与高技术水平的悖论；俄语技术社区因语言壁垒与地缘政治形成相对封闭的圈子，但技术水平极高
- 史料：俄语技术社区档案、freebsd-russian 邮件列表、参与者口述访谈 ［A］
- 史观：边缘者的贡献被中心叙事遮蔽，俄语技术文化特征须结合地域文化语境
- 辨析：文化特征的描述须避免刻板印象；“封闭性” 与 “高技术水平” 的悖论描述须结合俄语技术社区的具体史料核查，不得以单一标签概括
- FreeBSD committers 列表；FreeBSD SVN/Git 仓库提交日志；FreeBSD Core Team 年度报告 ［A］；openbsd.duckdb 查询 L3.3.1（committer_date 时区偏移分布前 30，22 仓库合计，30 行结果）、L3.3.2（author_email 域名 TLD 分布，22 仓库合计，16 行结果），见 `原材料/研究/bsd仓库分析/数据分析/深层信息挖掘.md` §L3.3.1、§L3.3.2

## 334.3.2 提交者权限的演变过程

- 要点：俄罗斯 committer 权限演变分三阶段——1995-2005 年的零星授予
- 文献：Yandex 技术博客；freebsd-russian 邮件列表；Habr 公司页面 ［A］

## 334.4.2 Mail.ru 与 VK 的 BSD 基础设施

- 要点：Mail.ru 1998 年成立，邮件服务长期基于 FreeBSD；VK（VKontakte）2006 年成立，后端部分使用 FreeBSD 处理社交网络高并发；Rambler 1996 年成立，早期使用 FreeBSD
- 史料：VK 与 Mail.ru 技术博客、Habr 公司页面、freebsd-russian 邮件列表 ［A］
- 史观：总纲第 13 条——法律与道德是利益分配，VK 与 Mail.ru 等俄罗斯互联网企业对 BSD 的使用与回馈存在不对称
- Russian FreeBSD Documentation Project 仓库；freebsd-russian 邮件列表 ［A］

## 334.5.2 Habr 与俄语技术媒体中的 BSD

- 要点：Habr（原 Habrahabr，2006 年 6 月上线，Denis Kryuchkov 创建，2018 年 4 月 24 日改名 Habr）是俄语技术社区最大的内容平台，涵盖 BSD 相关技术文章；俄罗斯因 Habr 等技术媒体而使 BSD 有较高公众可见度
- 史料：Habr 历年 BSD 相关文章、freebsd-russian 邮件列表 ［A］
- 史观：边缘者的贡献被中心叙事遮蔽，俄罗斯因 Habr 等技术媒体而获得的 BSD 公众可见度须从俄语本土媒体档案中重建
- RBUG 记录； 俄罗斯政策文件 ［B］
- FreeBSD SVN/Git 仓库；FreeBSD.org.ru 镜像站档案；Russian FreeBSD Documentation Project 仓库 ［A］

## 334.7.2 被遗忘的 DemOS 时代先驱

- 要点：DemOS 时代的俄罗斯 Unix 先驱是 BSD 历史中被严重遮蔽的群体；1990 年代苏联解体后这批先驱在资源匮乏的环境中引入并推广 BSD，其贡献长期被英语中心叙事忽略
- 史料：DemOS 项目档案、参与者口述访谈、俄语技术媒体 ［B］
- 史观：边缘者的贡献被中心叙事遮蔽，DemOS 时代先驱的贡献须从俄语档案中重建
  
- freebsd-russian 邮件列表；提交日志；社区成员访谈 ［A］

## 334.8.2 俄罗斯远东与西伯利亚地区的 BSD 使用者

- 要点：俄罗斯地理广袤，远东与西伯利亚地区的 BSD 使用者因地理隔离形成独特的远程协作模式；这些地区的 BSD 使用者与莫斯科/圣彼得堡中心社区存在信息不对称
- 史料：freebsd-russian 邮件列表地域分布分析、社区成员访谈 ［A］
- 史观：总纲第 20 条——历史地理塑造思想土壤，地理广袤塑造远程协作传统
- 辨析：地域分布的具体数据须经邮件列表分析核查；“信息不对称” 的程度须量化评估
- 文献：freebsd-russian 邮件列表地域分布分析、社区成员访谈 ［A］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
