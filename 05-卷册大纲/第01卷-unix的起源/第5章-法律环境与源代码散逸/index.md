---
chapter: 第 5 章
id: CH5
volume: 第01卷-unix的起源
---

# 第 5 章 法律环境与源代码散逸

## 要点

- 1960 年代末分时系统路线分化为——研究型（UNIX、Multics）、商业型（TSS/8、TOPS-10）、批处理扩展型（OS/360 TSO）；UNIX 选择极简研究路线，与商业系统目标不同
- IBM unbundle 催生的软件工业为 UNIX 商业化提供市场；但 IBM 案也警示其他厂商——UNIX 商业化面临反垄断风险；1982 年里根政府撤销 IBM 案，标志反垄断态度转变
- UNIX Heritage Society（TUHS）由 Warren Toomey 等人于 1995 年创立，宗旨为"preserve, maintain and restore historical and non-mainstream UNIX systems"；TUHS 早期档案建设面临 SCO（1995 年自 Novell 收购 UNIX 源码）法律不确定性，多数成员仅持 AT&T/US

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3617] 卷“第01卷-unix的起源”第 5 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3618] 卷“第01卷-unix的起源”第 5 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3639] 卷“第01卷-unix的起源”第 5 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3645] 卷“第01卷-unix的起源”第 5 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3646] 卷“第01卷-unix的起源”第 5 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_20] 卷“第01卷-unix的起源”第 5 章，匹配置信度 0.6，原因：路径启发：McKusick FFS 1984
- [DB:references_fulltext:chapter_matches:chmatch_27] 卷“第01卷-unix的起源”第 5 章，匹配置信度 0.6，原因：路径启发：GFS
- [DB:references_fulltext:chapter_matches:chmatch_53] 卷“第01卷-unix的起源”第 5 章，匹配置信度 0.6，原因：关键词重合 1 项
- [DB:references_fulltext:chapter_matches:chmatch_858] 卷“第01卷-unix的起源”第 5 章，匹配置信度 0.6，原因：关键词重合 1 项
- [DB:references_fulltext:chapter_matches:chmatch_1137] 卷“第01卷-unix的起源”第 05 章，匹配置信度 0.98，原因：McKusick、Bostic、Karels、Quarterman 合著的 4.4 BSD 操作系统设计与实现是 BSD 史上最重要的技术文献之一，由 CSRG 核心成员亲笔撰写，全面记录 4.4 BSD 的内核设计、文件系统（FFS/UFS）、虚拟内存、网络栈等核心子系统。与第5章 Bell Labs 黄金时代、第26B章 FreeBSD 诞生、第35B章 FreeBSD Ports 系统直接相关，是 FreeBSD 直接祖先的权威技术记录。

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 路线分化是否为必然——技术约束与市场需求的共同作用；**统计局限性标注**——references 表 16,867 条中仅 7,493 条（44.42%）成功提取年份，55.58% 文献无年份信息，5.03% 占比基于有年份记录计算，存在选择性偏差；本时期无 BSD commits 数据库 commit 数据（数据库 1993+ 起），统计结论限于文献计量学层面，不可外推至代码活跃度；统计显著
- [考据脚注] Caldera 2002 年许可证日期存在“1 月 23 日”（Bill Broderick 信件签署日，Groklaw、O'Reilly Darwin 文章、Spinellis FOSDEM 2016 幻灯片三项独立来源印证）与“1 月 24 日”（Warren Toomey TUHS 博客记载的公开发布日）两种说法，经多来源交叉印证，二者非矛盾而是不同事件节点——23 日为信件签

## 文献

- Ceruzzi“A History of Modern Computing” (2003)；Campbell-Kelly & Aspray“Computer” (1996)；统计分析报告：文献计量学分析.md Task 22 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/文献计量学分析.md**；SQL 查询：`SELECT id, gbt7714 FROM "references"`. 资料数据库.duckdb [DB/OL]. 查询日期：2026-07-27；Python 统计脚本：`script/phase6_bibliometrics.py`. Task 22 参考文献增长曲线与 Price 指数。执行日期：2026-07-27 ［ 据一手文献印证消解^doubt-resolved-35：路线分化是否为必然存在不同史观解释，Ceruzzi 2003 与 Campbell-Kelly & Aspray 1996 对 1960 年代末分时系统路线分化的动因分析侧重市场需求视角，须对照各系统原始技术手册与 AFIPS 会议论文核验技术约束维度；references 表 16,867 条、年份提取率 44.42%、1969-1974 年累计 5.03% 占比等统计结论经 `script/phase6_bibliometrics.py` 执行结果与 `phase6_results.json` 结构化结果交叉验证。］
- DOJ 1982 年撤销声明；“United States v. IBM”案件档案；Richard McKenzie“Trouble in the Teamster Union”对反垄断政策的分析 ［ 据一手文献印证消解^doubt-resolved-32：McKenzie 对反垄断政策的分析带有自由市场经济立场倾向，其对 IBM 案撤销的解读须与 DOJ 1982 年撤销声明原始文件及案件档案交叉印证，避免单一立场叙事。］<!-- NEWREF:2610 --><!-- NEWREF:2611 --><!-- NEWREF:2612 --><!-- NEWREF:2613 --><!-- NEWREF:2614 --><!-- NEWREF:2615 --><!-- 2026-08-05 补：US v. IBM 反垄断（1969/1977/1982）+ AT&T 1956 Consent Decree + 1982 MFJ 一手原件 -->
- Caldera International (2002.1.23) “Letter to UNIX enthusiasts”（Bill Broderick 签署，原件存 TUHS，Groklaw 2003.8.23 博客与 Spinellis FOSDEM 2016 演讲幻灯片转引全文）；Darwin, I. F. (2002.2.28) “Why Caldera Released Unix: A Brief History”O'Reilly（oreillynet.com/pub/a/linux/2002/02/28/caldera.html）；Toomey, W. (2009) “The Restoration of Early UNIX Artifacts”（Bond University）；Toomey, W. TUHS 官方博客（wiki.tuhs.org）；Spinellis, D. (2017) “A Repository of Unix History and Evolution”Empirical Software Engineering 22(3): 1372-1404（doi: 10.1007/s10664-016-9445-5）；SCO Group, Inc. v. Novell, Inc., 578 F.3d 1201 (10th Cir. 2009)；Unix Heritage Society 官方档案（tuhs.org） ［B］

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-191 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-191`；w172 YouTube 章节路由采纳）

据〔计算机历史博物馆活动（推断）〕讲者口述：多位讲述者接力介绍 Unix V4 源代码磁带的抢救：CHM 软件策展人 Al Kossow（前 Apple 二十年）说明软件保管职责——从磁带、磁盘组等原始介质恢复软件入数字仓库并配合模拟器开放；CHM 创始董事长 Len Shustek 回顾其 1970 年在布鲁克林理工学院 PL/I 编译器学生项目磁带保留五十年、2018 年花一千美元请专业数据恢复公司仍完全失败的经历，进而提出不读数字信号而直接采集磁带上模拟信息、以软件重建比特的思路，并与 Kossow 商定用标准磁带机在其模拟恢复点引出信号，以自研 Retape 程序重构数据——而原始 C 版 Unix 源码已失传，正待当日送达的磁带。（YouTube EP-xlq_MPWNKk）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-192 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-192`；w172 YouTube 章节路由采纳）

据〔计算机历史博物馆活动（推断）〕讲者口述：现场实操与多方佐证：软件策展人 Al Kossow 演示以磁带整备器（覆盖蓝宝石刮刀、以化妆品级环甲基硅酮润滑布轻拭带面）清洁与调理，再以 Saleae Pro 16 十六通道 ADC 数字化（预估 800 bpi、带速 50 英寸/秒即每秒 4 万磁通翻转、以 75 万样本/秒十倍过采样）；犹他大学博士生 Talia Archibald 转述‘Unix V4 tape found’消息（其团队即发现者，来自 Rob Pike）时的实验室沸腾，犹他大学 Flux 研究组 John Durig 讲述该带随创始人 Jay Lepreau 遗物封存二十年、由研究员整理遗物时偶然发现（标签写 V4 但内容仍待验证，众人谨慎管理预期），TUHS/Unix Heritage Society 创办人 Warren Toomey 阐述第四版作为 1973 年学术报告后首个对外发行、首个以 C 编写内核的版本的历史意义。（YouTube EP-xlq_MPWNKk）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1445 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1445`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔会议不详〕讲者口述：Mervin Kelly 自称其所创建的是“an institute of creative technology”，他向任何愿听者反复主张，真正要紧的突破无法被命令产生，只能像培育花园那样创造正确的条件而后等待。（YouTube EPdsBtMXOlANQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1446 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1446`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔会议不详〕讲者口述：1956 年同意令的第一项条款把 AT&T 限定在其受管制的业务之内，禁止其进入公用事业通信服务以外的任何经营领域，它不能把脚伸进计算机业务与消费电子等其自身研究所正忙于发明的领域。（YouTube EPdsBtMXOlANQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1447 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1447`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔会议不详〕讲者口述：同意令的第二项条款更为要紧，要求 AT&T 将其既有专利向其他美国公司免版税许可、未来专利按合理费率许可，贝尔实验室包含晶体管在内庞大的知识产权宝库因此被撬开、交给了美国工业的其余部分。（YouTube EPdsBtMXOlANQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1448 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1448`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔会议不详〕讲者口述：讲者称贝尔实验室在计算领域的关键进展包括一个操作系统与一门编程语言，它们将支撑整个软件世界；但在同意令之下 AT&T 被禁止把其中大部分变成生意，它不能出售计算机。（YouTube EPdsBtMXOlANQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
