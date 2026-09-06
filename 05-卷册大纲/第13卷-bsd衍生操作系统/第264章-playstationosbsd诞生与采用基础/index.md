---
chapter: 第 264 章
id: CH264
volume: 第13卷-bsd衍生操作系统
---

# 第 264 章 playstationosbsd诞生与采用基础

## 要点

- PS3（2006）的 GameOS 在 Linux 早期支持撤回后，底层含 FreeBSD 派生组件，Sony 工程师在 BSD 会议（如 BSDCan）披露 PlayStation 对 FreeBSD 的使用；具体组件范围须以 Sony 工程演讲核实。
- Sony 工程师（含日本籍与非英美成员）向 FreeBSD 回馈驱动/网络补丁，构成企业 →BSD 的代码流动案例。
- 对比 PlayStation OS（FreeBSD）与 Xbox（Windows 定制内核）、Nintendo（专有/FreeBSD 混合），分析游戏主机 OS 的 BSD 占比。
- 从用户与 BSD/Linux 阵营视角，Sony 移除 OtherOS 存在三重张力——（1）已交付功能的撤回：OtherOS 是 PS3 2006 年 11 月发售后即向用户承诺的功能，Yellow Dog Linux 5.0 于 2006 年 11 月发布官方支持 PS3，安装手册明确写道 "It was fully intended that you, a PS3 owner, could
- Sony 阵营的移除正当性论证沿四条线索展开——（1）服务条款保留修改权：PS3 用户协议（PlayStation Network User Agreement）保留 Sony 修改系统软件与服务的权利，用户在激活 PS3 与登录 PSN 时已同意此条款，固件 3.21 移除 OtherOS 是 Sony 在用户协议框架内的合法权利行使，非合同违约——Sony 在 Ventura v. SCEA

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4140] 卷“第13卷-bsd衍生操作系统”第 264 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- PS3 的 “FreeBSD 成分” 范围与 Linux 支持撤回的关系须厘清[考据完成：2026-07-28 经穷尽联网考据，PS3 的 FreeBSD 成分范围与 Linux 支持撤回的精确关系 Sony 未官方公开披露，多个二手来源（gamersky.com、3dmgame.com、CSDN）记载 PS4 Orbis OS 基于 FreeBSD 9.0 但 PS3 时期的 FreeBSD 成
- 具体贡献者须以 commit 记录核实；freebsd.db 查询 L7.2.1 的 “未出现 @sony.com 邮箱贡献者” 不等于 Sony 零回馈——Sony 工程师可能使用 @freebsd.org 邮箱（被查询排除条件过滤）、个人邮箱或 @playstation.com 等子域名提交，且 PlayStation OS 作为专有产品其内部 fork 不公开，Sony 可能通过内部维护而非
- 【查证来源】PlayStation.Blog 2010.3.28 PS3 Firmware v3.21 Update 公告原文经 WebFetch 核验（blog.us.playstation.com/2010/03/28/ps3-firmware-v3-21-update/），记载"disable the ‘Install Other OS’ feature"与"due to security 
- 【查证来源】PS3 用户协议（PlayStation Network User Agreement）保留 Sony 修改系统软件权利的条款经 Sony 官方页面核验；Ars Technica 2016.6.22 报道经 WebFetch 一手核验，记载"Sony argued that its terms of service allowed it to remove the Other OS f
- 【查证来源】原材料/哲学/项目统摄史观/第 25 章.md 总纲第 11、13、19 条原文经 Read 一手核验；Ventura v. SCEA 案全部法律历程档案（2010 提起、2011 撤销、2014 上诉法院部分推翻、2016 和解、2017 拒绝和解、2017 修订方案、2018 最终赔偿）经 Ars Technica 2016.6.22 报道、Ars Technica 2017.2.

## 文献

- Sony 工程演讲存档（BSD 会议）；PS3 架构文档；openbsd.db 查询 L3.2.1（商业实体 commit 占比随时间变化，含 Sony @sony.com）；openbsd.db 查询 L3.2.2（商业实体 commit 量按仓库分布）；原材料/研究/bsd 仓库分析/数据分析/深层信息挖掘.md §L3.2.1、§L3.2.2。 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2006-2006 年间：40,461 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- freebsd.db 查询 L7.2.1（衍生项目贡献者在 freebsd-src 的回馈 commit，≥5 次，前 30 名）；原材料/研究/bsd 仓库分析/数据分析/衍生项目与跨项目对比分析.md §L7.2；Sony 工程存档。 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：BSD 衍生系统
- 各主机厂商资料。[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:bsd_derivatives.duckdb -->> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 1985-2026 年间：963,557 次提交。> 仓库总览：963,557 次提交，9,744 位贡献者（contributors 表行数，1985-06-13 至 2026-08-24）。
- PlayStation.Blog 2010.3.28 公告 ［EB/OL］. <https://blog.us.playstation.com/2010/03/28/ps3-firmware-v3-21-update/>；EU PlayStation.Blog 2010.3.29 公告 ［EB/OL］. <https://blog.eu.playstation.com/2010/03/29/ps3-firmware-3-21-coming-april-1st/>；Ars Technica 2010.4 报道"Linux on the console? Sony sued for removing PS3 support"［EB/OL］. <https://arstechnica.com/gaming/2010/04/ps3-linux-support-removal-begets-class-actin-lawsuit/>；Ars Technica 2016.6.22 David Kravets 报道"Sony agrees to pay millions to gamers to settle PS3 Linux debacle"［EB/OL］. <https://arstechnica.com/tech-policy/2016/06/if-you-used-to-run-linux-on-your-ps3-you-could-get-55-from-sony/>；Ventura v. Sony Computer Entertainment America Inc. 案件档案（case no. 4:10-cv-01811，N.D.C.A.）；Yellow Dog Linux 5.0 PS3 安装手册；美国空军研究实验室 PS3 Condor Cluster 公开报道；FreeBSD 9.0 release notes；FreeBSD PS3 移植邮件列表存档 ［A］## 263.4.2 反批评——Sony 阵营的移除正当性论证
- PlayStation Network User Agreement；Ars Technica 2016.6.22 报道；Ventura v. SCEA 案 2011 撤销裁定与 2014 上诉法院推翻裁定；Ars Technica 2017.2.2 报道"Game over for PS3 Linux settlement"［EB/OL］. <https://arstechnica.com/tech-policy/2017/02/game-over-for-ps3-linux-settlement-judge-concerned-gamers-wont-get-paid/>；Law360 2017.9.5 报道"Sony Asks For Approval Of Revised $3.75M PS3 Settlement"；Gearnuke 2018.11.14 报道"Sony sending $ 10 settlement checks for PS3 Other OS lawsuit"；Hotz 2010.1 PS3 hypervisor 漏洞博客 ［EB/OL］. <https://geohotps3.blogspot.com/>；fail0verflow 27C3 演讲档案；Sony v. Hotz 案件档案；PS3 Slim 2009.9 发布新闻稿 ［A］## 263.4.3 再批评——商品形式主义与消费者权益的深化
- 原材料/哲学/项目统摄史观/第 25 章.md；Ventura v. SCEA 案全部法律历程档案；Ars Technica 2016.6.22 报道；Gearnuke 2018.11.14 报道；126.4.1-126.4.3 节记录；PlayStation.Blog 2010.3.28 公告；Hotz 2010.1 漏洞公布博客；Sony v. Hotz 案件档案；PS3 用户协议；Yellow Dog Linux 5.0 安装手册 ［A］<!-- NEWREF:2632 --><!-- NEWREF:2633 --><!-- NEWREF:2634 --><!-- NEWREF:2635 --><!-- NEWREF:2636 --><!-- NEWREF:2637 --><!-- NEWREF:2647 --><!-- 2026-08-05 补：PS3 OtherOS 集体诉讼一手原件（与第6卷123.11共享） --><!-- DB_REF:bsd_derivatives.duckdb -->> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 2010-2018 年间：370,282 次提交。> 仓库总览：963,557 次提交，9,744 位贡献者（contributors 表行数，1985-06-13 至 2026-08-24）。
- 原材料/哲学/项目统摄史观/第 25 章.md 总纲第 1、2、7、11、13、19、23、25 条；PlayStation.Blog 2010.3.28 公告 ［EB/OL］. <https://blog.us.playstation.com/2010/03/28/ps3-firmware-v3-21-update/>；Ventura v. SCEA 案法律档案（case no. 4:10-cv-01811，N.D.C.A.）；Hotz 2010.1 漏洞公布博客 ［EB/OL］. <https://geohotps3.blogspot.com/>；fail0verflow 27C3 演讲档案；Sony v. Hotz 案件档案（2011.1）；Ars Technica、Courthouse News Service、Law360、Gearnuke 媒体报道；126.5.1-126.5.3 节审视文本 ［A］<!-- DB_REF:bsd_derivatives.duckdb -->> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 1985-2026 年间：963,557 次提交。> 仓库总览：963,557 次提交，9,744 位贡献者（contributors 表行数，1985-06-13 至 2026-08-24）。
