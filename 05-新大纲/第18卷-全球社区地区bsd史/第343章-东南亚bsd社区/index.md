---
chapter: 第 343 章
id: CH343
volume: 第18卷-全球社区地区bsd史
---

# 第343章 东南亚bsd社区

## 要点

- 新加坡国立大学（NUS）与南洋理工大学（NTU）在 1990 年代开设 UNIX/BSD 相关课程，NUS 计算机学院（School of Computing）在 BSD 网络栈与操作系统研究方面有传统。新加坡高校的 BSD 教育培养了一批新加坡 BSD 贡献者，新加坡学生通过 编程之夏 参与 BSD 项目
- 新加坡作为亚洲互联网枢纽（SGIX 新加坡互联网交换中心），其 ISP（Singtel、StarHub、M1）与数据中心在 1990-2000 年代大量使用 FreeBSD 作为网络服务器。新加坡的国家宽带网络（Next Gen NBN）基础设施中也有 BSD 部署
- Singapore BSD Users Group（SBUG）是新加坡 BSD 社区的核心组织，定期举办技术讲座与安装会。新加坡 BSD 社区参与 AsiaBSDCon（2007 年起），新加坡 BSD 用户也参与 FOSSASIA 等东南亚开源会议中的 BSD 相关活动
- 新加坡 BSD 部署记录是评估新加坡 BSD 采用的关键史料，新加坡作为英语国家，其 BSD 记录在亚洲 BSD 社区中保存最为完整
- 马来西亚 BSD 社区以吉隆坡（Kuala Lumpur）与槟城（Penang）为中心，马来西亚 IT 产业（如 MSC Malaysia 多媒体超级走廊计划，1996 年启动）为 BSD 在马来西亚的采用提供了政策环境。马来西亚早期 ISP（如 TMnet、Jaring）在 1990 年代使用 FreeBSD

## 史观

- 总纲第 20 条——历史地理塑造思想土壤，新加坡高校 BSD 教育是 BSD 在东南亚学术扩散的核心节点
  - 辨析：NUS/NTU BSD 课程的具体内容需考据；新加坡 BSD 教育的影响力需评估
  - 文献：NUS School of Computing 课程档案；NTU CS 课程大纲［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

**编排说明（2026-09-11 整改按磁盘实况 343.1-343.9 重排）**：原文件主体为生成期残损堆叠（多处子节标题残留旧章号 342.x 或无号残标、多个子节重复出现、多处要点与史料条目截断为空壳），现按磁盘实况 343.1-343.9 重排为章级导航；残损子节块的完整版本保存在同章各子节文件中，本文件不再重复堆叠。

## 本章节索引

1. [343.1 新加坡：亚洲 BSD 的技术枢纽](343.1-新加坡-亚洲-BSD-的技术枢纽.md)
2. [343.2 马来西亚的 BSD 社区与教育](343.2-马来西亚的-BSD-社区与教育.md)
3. [343.3 印度尼西亚的 BSD 采用](343.3-印度尼西亚的-BSD-采用.md)
4. [343.4 泰国的 BSD 社区](343.4-泰国的-BSD-社区.md)
5. [343.5 越南与菲律宾的 BSD 使用](343.5-越南与菲律宾的-BSD-使用.md)
6. [343.6 东南亚 BSD 社区与东南亚国家的 FreeBSD 部署案例](343.6-东南亚bsd社区与东南亚国家的freebsd部署案例.md)
7. [343.7 重要贡献者与边缘者](343.7-重要贡献者与边缘者.md)
8. [343.8 多元群体贡献](343.8-多元群体贡献.md)
9. [343.9 东南亚与同时期操作系统的比较](343.9-东南亚与同时期操作系统的比较.md)

## 史料考据补充

- 新加坡小型 ISP 历史记录；新加坡早期系统管理员口述历史［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；openbsd.duckdb 查询 L3.3.1（committer_date 时区偏移分布前 30，22 仓库合计，30 行结果）、L3.3.2（author_email 域名 TLD 分布，22 仓库合计，16 行结果），见 `原材料/研究/bsd仓库分析/数据分析/深层信息挖掘.md` §L3.3.1、§L3.3.2

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- ROW_MINE: login-zazhi.articles.CL-18-067 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-18-067`；login 逐条遍历判定采纳）

2000年前后，家用用户已可用NetBSD在旧PC上构建低成本、免维护的NAT防火墙；作者主张该配置安全性优于部分商业防火墙，并因BSD/Linux在旧硬件上表现良好而被选为家用网关平台。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-18-067 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-18-067`；login 逐条遍历判定采纳）

2000年前后，家用用户已可用NetBSD在旧PC上构建低成本、免维护的NAT防火墙；作者主张该配置安全性优于部分商业防火墙，并因BSD/Linux在旧硬件上表现良好而被选为家用网关平台。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1256 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1256`；w172 YouTube 章节路由采纳）

据 meetBSD 2010 讲者口述：2007 年 Google 开设办公室（原文“and then 2007 Google opens their offices”）。（YouTube EPbj24jHtRkZs，[823.38-824.93]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1254 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1254`；w172 YouTube 章节路由采纳）

据 meetBSD 2010 讲者口述：到 2004 年，波兰加入（原文“so fast forward to 2004 Poland joins the”，其后加入的对象在转写中缺失，无据可断）。（YouTube EPbj24jHtRkZs，[763.139-766.61]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1255 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1255`；w172 YouTube 章节路由采纳）

据 meetBSD 2010 讲者口述：讲者提到 2005 年时 IBM 随之加入（原文讹字、断句不全）。（YouTube EPbj24jHtRkZs，[793.38-796.009]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->
