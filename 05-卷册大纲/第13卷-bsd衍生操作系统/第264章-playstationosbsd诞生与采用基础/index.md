---
chapter: 第 264 章
id: CH264
volume: 第13卷-bsd衍生操作系统
---

# 第 264 章 PlayStation OS 诞生与 BSD 在游戏主机的采用基础，2006-2026

## 要点

- PS3（2006）的 GameOS 在 Linux 早期支持撤回后，底层含 FreeBSD 派生组件，Sony 工程师在 BSD 会议（如 BSDCan）披露 PlayStation 对 FreeBSD 的使用；具体组件范围须以 Sony 工程演讲核实。
- Sony 工程师（含日本籍与非英美成员）向 FreeBSD 回馈驱动/网络补丁，构成企业 →BSD 的代码流动案例。
- 对比 PlayStation OS（FreeBSD）与 Xbox（Windows 定制内核）、Nintendo（专有/FreeBSD 混合），分析游戏主机 OS 的 BSD 占比。
- 从用户与 BSD/Linux 阵营视角，Sony 移除 OtherOS 存在三重张力——（1）已交付功能的撤回：OtherOS 是 PS3 2006 年 11 月发售后即向用户承诺的功能，Yellow Dog Linux 5.0 于 2006 年 11 月发布官方支持 PS3，安装手册明确写道 "It was fully intended that you, a PS3 owner, could play games, watch movies, view photos, listen to music, and run a full-featured Linux operating system that transforms your PS3 into a home computer"；（2）“自愿更新”实质强制：拒绝更新将丧失 PSN、新游戏、蓝光电影等核心功能；（3）“安全理由”不透明：Sony 仅以 “due to security concerns” 为由未详述（2026-09-11 整改自本章 264.4 节回源补全）
- Sony 阵营的移除正当性论证沿四条线索展开——（1）服务条款保留修改权：PS3 用户协议（PlayStation Network User Agreement）保留 Sony 修改系统软件与服务的权利，用户在激活 PS3 与登录 PSN 时已同意此条款，固件 3.21 移除 OtherOS 是 Sony 在用户协议框架内的合法权利行使，非合同违约——Sony 在 Ventura v. SCEA 案中主张 "its terms of service allowed it to remove the Other OS feature"（2026-09-11 整改自本章 264.4 节回源补全；其余三条线索详见 264.4 节）

## 史料

- PlayStation.Blog 2010-03-28 固件 3.21 更新公告（OtherOS 功能移除的官方声明）；EU PlayStation.Blog 2010-03-29 公告
- Yellow Dog Linux 5.0 PS3 安装手册（OtherOS 与完整 Linux 环境支持的官方承诺文本）
- FreeBSD 9.0 release notes；FreeBSD PS3 移植邮件列表存档（PS3 支持于 2011 年由 Nathan Whitehorn 等社区成员导入）
- Ventura v. Sony Computer Entertainment America Inc. 案件档案（case no. 4:10-cv-01811，N.D.C.A.）及历次裁定报道存档
- Sony 工程师 BSD 会议（BSDCan 等）演讲存档（PlayStation 对 FreeBSD 使用的官方披露）

（2026-09-11 整改：原史料字段仅存的机械映射条目 [DB:references_fulltext:chapter_matches:chmatch_4140]（置信度 1.0，原因为算法工单“任务4第二批 缺口章补充”）已按核查报告建议移除，替换为上列本章实有史料清单，均转录自本文件要点与文献字段已载条目。）

## 史观

- 总纲第 13 条（法律与道德是利益分配）与总纲第 11 条（商品是形式主义）：PS3 OtherOS 移除争议呈现 Sony 商业利益（防盗版、维护游戏生态）与用户权益（已交付功能保留）的利益分配冲突，“自愿更新”是商品形式主义下形式自愿对实质强制的掩盖；总纲第 2 条（历史是形式主义化的非存在）：用户协议的形式主义文本先于实质的功能撤回；企业→BSD 的代码流动案例须与社区主导移植（FreeBSD PS3 支持由 Nathan Whitehorn 等社区成员于 2011 年导入）区分呈现（2026-09-11 整改回填，归纳自本章 264.4 节史观字段）

## 辨析

- PS3 的 “FreeBSD 成分” 范围与 Linux 支持撤回的关系须厘清［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。
> 2006-2006 年间：40,461 次提交。
> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

- freebsd.duckdb 查询 L7.2.1（衍生项目贡献者在 freebsd-src 的回馈 commit，≥5 次，前 30 名）；**research_notes.duckdb** 衍生项目与跨项目对比分析记录 §L7.2（原“原材料/研究/bsd 仓库分析/数据分析/衍生项目与跨项目对比分析.md”路径已失效，2026-09-11 整改改指）；Sony 工程存档。［A］
- 各主机厂商资料。［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:bsd-derivatives.duckdb -->
> **数据库引用（bsd-derivatives.duckdb）**：本子节对应 bsd-derivatives 代码仓库。
> 1985-2026 年间：963,557 次提交。
> 仓库总览：963,557 次提交，9,744 位贡献者（contributors 表行数，1985-06-13 至 2026-08-24）。

- PlayStation.Blog 2010.3.28 公告 ［EB/OL］. <https://blog.us.playstation.com/2010/03/28/ps3-firmware-v3-21-update/>；EU PlayStation.Blog 2010.3.29 公告 ［EB/OL］. <https://blog.eu.playstation.com/2010/03/29/ps3-firmware-3-21-coming-april-1st/>；Ars Technica 2010.4 报道“Linux on the console? Sony sued for removing PS3 support”［EB/OL］. <https://arstechnica.com/gaming/2010/04/ps3-linux-support-removal-begets-class-actin-lawsuit/>；Ars Technica 2016.6.22 David Kravets 报道"Sony agrees to pay millions to gamers to settle PS3 Linux debacle"［EB/OL］. <https://arstechnica.com/tech-policy/2016/06/if-you-used-to-run-linux-on-your-ps3-you-could-get-55-from-sony/>；Ventura v. Sony Computer Entertainment America Inc. 案件档案（case no. 4:10-cv-01811，N.D.C.A.）；Yellow Dog Linux 5.0 PS3 安装手册；美国空军研究实验室 PS3 Condor Cluster 公开报道；FreeBSD 9.0 release notes；FreeBSD PS3 移植邮件列表存档 ［A］
- PlayStation Network User Agreement；Ars Technica 2016.6.22 报道；Ventura v. SCEA 案 2011 撤销裁定与 2014 上诉法院推翻裁定；Ars Technica 2017.2.2 报道“Game over for PS3 Linux settlement”［EB/OL］. <https://arstechnica.com/tech-policy/2017/02/game-over-for-ps3-linux-settlement-judge-concerned-gamers-wont-get-paid/>；Law360 2017.9.5 报道“Sony Asks For Approval Of Revised $3.75M PS3 Settlement”；Gearnuke 2018.11.14 报道“Sony sending \$10 settlement checks for PS3 Other OS lawsuit”；Hotz 2010.1 PS3 hypervisor 漏洞博客 ［EB/OL］. <https://geohotps3.blogspot.com/>；fail0verflow 27C3 演讲档案；Sony v. Hotz 案件档案；PS3 Slim 2009.9 发布新闻稿 ［A］
- **sacred_sources.duckdb** 项目统摄史观相关章（原“原材料/哲学/项目统摄史观/第 25 章.md”路径已失效，2026-09-11 整改改指）；Ventura v. SCEA 案全部法律历程档案；Ars Technica 2016.6.22 报道；Gearnuke 2018.11.14 报道；第 6 卷 PlayStation OtherOS 诉讼相关节记录（原“126.4.1-126.4.3 节记录”旧章号引用，2026-09-11 整改改为不依赖节号表述）；PlayStation.Blog 2010.3.28 公告；Hotz 2010.1 漏洞公布博客；Sony v. Hotz 案件档案；PS3 用户协议；Yellow Dog Linux 5.0 安装手册 ［A］

<!-- NEWREF:2632 --><!-- NEWREF:2633 --><!-- NEWREF:2634 --><!-- NEWREF:2635 --><!-- NEWREF:2636 --><!-- NEWREF:2637 --><!-- NEWREF:2647 --><!-- 2026-08-05 补：PS3 OtherOS 集体诉讼一手原件（与第6卷123.11共享） -->

<!-- DB_REF:bsd-derivatives.duckdb -->
> **数据库引用（bsd-derivatives.duckdb）**：本子节对应 bsd-derivatives 代码仓库。
> 2010-2018 年间：370,282 次提交。
> 仓库总览：963,557 次提交，9,744 位贡献者（contributors 表行数，1985-06-13 至 2026-08-24）。

- **sacred_sources.duckdb** 项目统摄史观相关章（原“原材料/哲学/项目统摄史观/第 25 章.md 总纲第 1、2、7、11、13、19、23、25 条”引证，条号集合未经逐一核验，2026-09-11 整改登记待核）；PlayStation.Blog 2010.3.28 公告 ［EB/OL］. <https://blog.us.playstation.com/2010/03/28/ps3-firmware-v3-21-update/>；Ventura v. SCEA 案法律档案（case no. 4:10-cv-01811，N.D.C.A.）；Hotz 2010.1 漏洞公布博客 ［EB/OL］. <https://geohotps3.blogspot.com/>；fail0verflow 27C3 演讲档案；Sony v. Hotz 案件档案（2011.1）；Ars Technica、Courthouse News Service、Law360、Gearnuke 媒体报道；第 6 卷 PlayStation OtherOS 诉讼相关节审视文本（原“126.5.1-126.5.3 节审视文本”旧章号引用，2026-09-11 整改改为不依赖节号表述）［A］

（2026-09-11 整改说明：本字段原夹带的“## 263.4.2 反批评”“## 263.4.3 再批评”他章标题残留已清除，相关内容实属本章 264.4 节；原与文献条目同行的 DB_REF 块已拆分独立成行；粘连的“史料考据补充”标题残片已清除；重复的 bsd-derivatives.duckdb 总览块已去重。）
