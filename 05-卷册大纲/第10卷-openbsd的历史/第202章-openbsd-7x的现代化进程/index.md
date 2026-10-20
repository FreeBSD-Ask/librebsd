---
chapter: 第 202 章
id: CH202
volume: 第10卷-openbsd的历史
---

# 第 202 章 openbsd-7x的现代化进程

## 要点

- OpenBSD 7.0-7.7 的 Release Notes 与 CVS commit log 是研究此时期现代化的核心史料；特性引入时间以 Release Notes 与 commit log 交叉验证为准——Release Notes 记录用户可见变更，commit log 记录具体代码变更，二者交叉验证可确定特性引入的精确时间；统计结论印证——openbsd.duckdb openbsd-src 仓库 commit 序列的量化结论（口径见文末章级 DB_REF 总览块与辨析 L1.1.1 局限注）与方法论互证〔2026-09-12 整改：句尾截断收束——批次 C218 问题 4〕
- OpenBSD/NetBSD/FreeBSD 关于 AI 代码政策的邮件列表档案是研究 BSD 社区应对 AI 浪潮的核心史料；政策形成过程以三个项目的官方政策文档修订历史与邮件列表讨论交叉验证为准
- OpenBSD misc@、tech@ 邮件列表中关于权限授予、撤销、committer 行为规范的讨论是研究权限模型的核心史料；权限变更的具体内容与时间以邮件列表档案与 CVS access log 交叉验证为准
- OpenBSD 7.x 时期外部批评的原始发言与邮件列表档案是研究 OpenBSD 现代化滞后形象塑造的核心史料；批评的具体语境与回应以 Linux、FreeBSD、OpenBSD 多个社区邮件列表交叉验证为准
- OpenBSD 7.x 时期核心贡献者的 commit 记录与邮件列表发言是研究 OpenBSD 社区生态的核心史料；贡献的具体内容与时间以 CVS commit log、邮件列表档案、hackathons 记录交叉验证为准

## 史料

- OpenBSD 7.0-7.7 Release Notes（plus.html 用户可见变更页）与 CVS commit log（cvsweb.openbsd.org）〔一手〕
- OpenBSD misc@/tech@ 邮件列表档案（marc.info）——AI 代码政策讨论、权限授予/撤销与行为规范讨论存档
- 各 BSD 项目官方 AI 代码政策文档修订历史（CVS/Git commit log）
- [DB:references_fulltext:chapter_matches:chmatch_3901/4016/4022/4029] 库侧匹配登记（2026-09-12 整改：原机器标识串充当史料改可读著录，匹配行含“folder 第200章”跨章零信息匹配与“任务4”内部任务号，仅作检索登记不作证据——批次 C218 问题 2）

## 史观

总纲第 9 条——经验优先：7.x 现代化以 Release Notes 与 commit log 的经验记录交叉验证为准，拒绝二手概括（据要点 1）；总纲第 3 条——不存在进步，只有权力再分配：AI 代码政策、committer 权限规则与“现代化滞后”批评的演进是社区治理权力的再分配而非线性进步（据要点 2/3/4）；总纲第 10 条——动手者创造历史：7.x 各项特性由 committer 的 commit 与 hackathon 劳动逐项落地（据要点 5）；总纲第 8 条——本体论上各方平等：OpenBSD/NetBSD/FreeBSD 三项目对 AI 浪潮的不同政策取向地位平等（据要点 2）；总纲第 19 条——解释学循环是历史认识的根本条件：外部批评与社区回应的理解均受前理解制约，须以原始语境核验（据要点 4）。（2026-09-12 整改：史观字段按批次 C218 自 202.1-202.6 各节归纳回填，映射依 25 条权威表）

## 辨析

- Release Notes 的完整性以 plus.html 页面为准——该页面仅记录 “重要的和用户可见的变更”，部分内部代码重构可能未记录；commit log 中的 arm64/桌面/无线相关 commit 须通过文件路径（如 sys/arch/arm64/、sys/dev/pci/drm/）筛选方可定位；openbsd.duckdb 查询 L1.1.1 局限：L1.1.1 报告仅显示 23 仓库 572 行结果中的前 30 行（按仓库名字母序排列，前 30 行全为 dragonfly 仓库），openbsd-src 行未在截断输出中显示，须另用查询脚本直查〔2026-09-12 整改：句尾截断按已知查询口径收束——批次 C218 问题 4〕
- 邮件列表档案的完整性以 marc.info 与 mail-index.netbsd.org 存档为准——部分讨论可能在私有列表（如各项目的 Core Team 私有列表）进行，公开档案无法覆盖全部讨论；政策文档的修订历史以各项目文档仓库（CVS/Git）的 commit log 为准
- 邮件列表档案的完整性以 marc.info 存档为准——misc@ 与 tech@ 的公开讨论有完整存档，但 Core Team 私有讨论不在公开档案中；个别权限撤销事件的具体细节以邮件列表原始帖子为准，转载或二手报道可能简化或扭曲；committer 权限撤销案例考据（2026-07-30 联网核查留痕）：经 WebSearch 检索 “openbsd committer removed”相关条目，具体撤销案例的细节须以 misc@/tech@ 原始帖核实〔2026-09-12 整改：内部条目编号移除、直引号弯引号化、截断收束——批次 C218 问题 8〕
- 批评的具体语境以原始邮件列表帖子为准——转载至 OSNews/Slashdot/Hacker News 的报道可能简化或扭曲原始语境；de Raadt 回应的语义以 <misc@openbsd.org> 原始帖子为准，二手报道的解读可能与原文有差异
- commit 记录的归属以 openbsd.duckdb author_name 字段为准（2026-09-12 整改：旧合并库名改指 openbsd.duckdb——批次 C218 问题 9）——部分 patch 由多人协作但仅 committer 一人出现在 author_name 字段，实际贡献者可能在 commit message 的 “from” 或 “ok” 行中署名；邮件列表档案的完整性以 marc.info 存档为准

## 文献

- OpenBSD Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>；OpenBSD CVS 仓库 [EB/OL]. <https://cvsweb.openbsd.org/>；man pages [EB/OL]. <https://man.openbsd.org/>
- 统计分析报告：推断性统计.md（Pettitt + BUISHAND 变点检测），存于 **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/**（2026-09-12 整改：原条目混入的“原材料/”断链路径、Python 脚本名与执行日期等非文献要素移除留痕——批次 C218 问题 10）

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库（2026-09-12 整改：原六连 DB_REF 块〔2020-2026/2023-2026/2013-2026/1995-2026×2/2020-2026 六种窗口〕去重合并为章级总览块并补闭合；各块后交错文献条目已归位“## 文献”——批次 C218 问题 3/12/13）。
> 窗口切片：2020-2026 年 115,626 次；2023-2026 年 63,828 次；2013-2026 年 248,174 次；1995-2026 年（全库）491,195 次。

<!-- /DB_REF:openbsd.duckdb -->

## 文献

- 各 BSD 项目邮件列表档案 [EB/OL]. <https://marc.info/>、<https://mail-index.netbsd.org/>；各项目政策文档；BSD 社区讨论档案
- OpenBSD 邮件列表档案 [EB/OL]. <https://marc.info/?l=openbsd-misc>；CVS access log；OpenBSD hackathons 记录（2026-09-12 整改：URL 参数 ?lacc → ?l= 修正，批次 C218 问题 7）
- 各 BSD/Linux 邮件列表档案 [EB/OL]. <https://lists.freebsd.org/>；技术媒体文章；de Raadt 公开发言（2026-09-12 整改：分号与中文移出尖括号，批次 C218 问题 6）
- OpenBSD 7.0-7.7 Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>；**pledge(2)** 手册页 <https://man.openbsd.org/pledge.2>；**unveil(2)** 手册页 <https://man.openbsd.org/unveil.2>；tech@ 邮件列表档案 [EB/OL]. <https://marc.info/?l=openbsd-tech>

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2020-2026 年间：115,626 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP368、BSD Now EP626（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->
<!-- 主题限定注（2026-09-12 整改补，批次 C218 问题 14）：EP626 主体为 FreeBSD Journal/NetBSD 11/Foundation 内容，与本章 OpenBSD 7.x 主题直接相关者仅 USB 摄像头测试（7.8 征集）与 OpenSSH refuse connection 两条，引用时以该段落范围为限 -->

**要点**：

- Frederick Cambus 的文章梳理 OpenBSD 控制台从 80×25 文本模式到帧缓冲的演进，提及 wscons 控制台框架继承自 NetBSD。（BSD Now EP368，[82.09-313.37]，L2）
- John Carmack 于 2020 年 6 月为 OpenBSD 控制台贡献快速条件滚动与 32 位字符渲染优化，体现其对 OpenBSD 开发环境的偏好。（BSD Now EP368，[319.03-357.67]，L2）
- Ruben 反思操作系统角色变化：Mac 转向商务软件、Linux 转向游戏与仿真、FreeBSD 承担其余，OS 逐渐成为向应用提供服务的后台平台。（BSD Now EP368，[373.44-634.26]，L2）
- Zero Day Initiative 披露 FreeBSD Compat32 子系统 sendmsg 的 TOCTOU 竞态漏洞，可致堆溢出并进一步提权。（BSD Now EP368，[1612.45-2034.16]，L2）
- FreeBSD Journal 2025 夏季刊以网络为主题，收录 Tom Jones 的 Wi-Fi 开发入门、Randall Stewart 与 Michael Tüxen 的 TCP 静态 pacing 以及 Christopher R. Bowman 的嵌入式 FreeBSD 等文章。（BSD Now EP626，[141.82-762.54]，L2）
- FreeBSD Foundation 的《Java hiding in plain sight》指出 OpenJDK 仍是 Elasticsearch、Tomcat、LibreOffice 与 Minecraft 等系统的基础，维护者的工作使 FreeBSD 上的 OpenJDK 保持最新。（BSD Now EP626，[762.54-946.78]，L2）
- Chuck Tuffley 的 BSDCan 2025 报告记录基金会社区调查与笔记本支持、Core 团队章程修订、AI 政策讨论以及 Verisign 与 NVIDIA 的产业报告。（BSD Now EP626，[948.80-1427.06]，L1）
- OpenBSD 7.8 征集 USB 摄像头测试，开发者 Kirill 为 uvideo 增加 H.264 流支持并优化 CPU 占用以支持 4K 60fps 原始流。（BSD Now EP626，[1437.62-1538.58]，L2）
- OpenSSH 新增 refuse connection 配置指令与 PKCS#11 ED25519 密钥支持，由 Damien Miller 提交。（BSD Now EP626，[1541.90-1621.92]，L2）
- NetBSD 11 分支进入发布流程，包括 32 位兼容集拆分、CD 安装镜像、x86 PVH 启动支持、RISC-V 新端口与工具链更新。（BSD Now EP626，[1636.36-1806.82]，L2）
- Nico Cartron 自述 2000 年在巴黎计算机学校初识 NetBSD 机房，后以 FreeBSD 为主，日常通过 WireGuard 与 SSH 使用家中的 FreeBSD 笔记本。（BSD Now EP626，[1950.18-2571.94]，L1）

**史料**：

- Frederick Cambus 的 OpenBSD 控制台现代化文章及 spleen 字体说明链接。（BSD Now EP368，[82.09-313.37]，L2）
- Zero Day Initiative 关于 MoonBSD 漏洞的研究者撰写，含 FreeBSD Compat32 子系统的背景说明。（BSD Now EP368，[1612.45-2034.16]，L2）
- FreeBSD Journal 2025 年夏季刊及其收录文章。（BSD Now EP626，[141.82-762.54]，L2）
- Mark Phillips 撰写的 FreeBSD Foundation 博客 Java hiding in plain sight。（BSD Now EP626，[762.54-946.78]，L2）
- Chuck Tuffley 的 BSDCan 2025 Trip Report。（BSD Now EP626，[948.80-1427.06]，L1）
- Undeadly.org 的 USB webcam 测试征集与 OpenSSH 新特性报道。（BSD Now EP626，[1437.62-1621.92]，L2）
- Martin Husemann 的 NetBSD 11 release process 博客。（BSD Now EP626，[1636.36-1806.82]，L2）
- Nico Cartron 访谈。（BSD Now EP626，[1950.18-3345.10]，L1）

**史观**：

- 总纲9 经验优先：OpenBSD 控制台改进源自对文本模式与帧缓冲显示带宽差异的实际测量，而非抽象设计。（BSD Now EP368，[169.94-214.16]，L2）
- 总纲3 不存在进步，只有权力再分配：操作系统角色变化的叙事揭示各系统在不同场景中的功能再分配，而非单向的线性进步。（BSD Now EP368，[373.44-634.26]，L2）
- 总纲10 动手者创造历史：Chuck Tuffley 报告中 Google Summer of Code 学生与 Kyle Evans 接力推进 squashfs 驱动，体现未完成工作由后来者接续。（BSD Now EP626，[1232.26-1271.62]，L1）
- 总纲22 知识注定过时：NetBSD 11 将 32 位兼容、CD 安装集等旧有默认拆分为可选集，反映旧硬件假设随时代过时。（BSD Now EP626，[1647.40-1682.94]，L2）
- 总纲20 历史地理塑造思想土壤：Nico Cartron 的法国计算机学校以 NetBSD 教学机房塑造其 BSD 使用路径，体现机构地理对技术选择的塑造。（BSD Now EP626，[1973.62-2103.06]，L1）

**辨析**：

- 新转写清晰读出：OpenBSD 帧缓冲的 rasops（RasterOps）系 2001 年自 NetBSD 引入，i386/AMD64 帧缓冲控制台于 2013 年随 Intel DRM 与 Radeon DRM 启用，细节仍宜对照 Cambus 原文。 [存疑脚注] 平台与时间细节待原文核对（BSD Now EP368，[203.20-240.50]，L4）[订正：原 引入时间与平台细节存在 ASR 转写噪声且 [215.94-251.96]，2026-09-30 SenseAudio 重转核对]
- 转录将 Martin Husemann 记作 Martin Hussman，且节目开场将 NetBSD 11 与 FreeBSD 11 混写，须以 NetBSD 官方博客核验。 [存疑脚注] 人名与版本号存在转写歧义，未与 NetBSD 官方公告核验（BSD Now EP626，[1636.36-1806.82]，L4）
- OpenJDK 维护者姓名在转录中作 Harold 或 Harald，具体拼写须以 FreeBSD Foundation 原文核验。 [存疑脚注] 维护者姓名存在转写歧义（BSD Now EP626，[867.98-873.02]，L4）

**文献**：

- [BSD Now EP368] Pennington J. BSD Now: 368: Changing OS roles[EB/OL]. (2020-09-17)[2026-08-15]. <https://www.bsdnow.tv/368>.
- [BSD Now EP626] Pennington J. BSD Now: 626: USB webcam testing[EB/OL]. (2025-08-28)[2026-08-15]. <https://www.bsdnow.tv/626>.

<!-- /PODCAST_REVIEW -->

> （2026-09-12 整改：原 dangan-20260908 消解回写块（“IT. 之家 2024-05-17 报道”条，含内部工单标记 DKC-0046→fulltext:5461、[EB/OL] 重复、URL 系腾讯云开发者转载非一手）删除留痕；如该报道确有史料价值须另行按规范著录后归档——批次 C218 问题 5。）

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-283 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-283`；w172 YouTube 章节路由采纳）

据〔The OpenBSD Hypervisor in the wild 演讲〕讲者口述：讲者称自己只提供 OpenBSD 虚拟机而非 Linux 虚拟机，且当时 OpenBSD 6.6 即将发布。（YouTube EP9TuWCR9X-wY，[445.31-454.45]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-396 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-396`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：讲者约在三年前在 OpenBSD 中实现了 VXLAN 控制器这一组件。（YouTube EPCuo0qT-lqig，[46.462-57.176]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-542 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-542`；w172 YouTube 章节路由采纳）

据〔BSDCan 2017〕讲者 Reyk Floeter 口述：OpenBSD 虚拟机守护进程的客户机支持中 FreeBSD 仍在推进，此前因未满足若干假设而受阻。（YouTube EPGEXzo6hRf3M，[983.12-996.67]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-563 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-563`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：讲者正在为 OpenBSD 处理 Hyper-V 驱动相关工作，依据是 FreeBSD 侧已经有可用的同类驱动可以移植参考。（YouTube EPGWwhgIPdKH0，[2920.599-2930.23]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-755 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-755`；w172 YouTube 章节路由采纳）

据〔EuroBSDcon 2023〕讲者 Otto Moerbeek 口述：OpenBSD 在 2008 年（距演讲时约十五年前）改用自有的 malloc 实现，在那之前 OpenBSD 与 FreeBSD 一样沿用同一套 malloc 实现。（YouTube EPMIjUsv91rXg，[76.82-90.83]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-976 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-976`；w172 YouTube 章节路由采纳）

据讲者口述：OpenBSD 4.5（转写音作 LWBV 4.5）仅收录 72 个传感器驱动，讲者预计 4.6 版将增至 76 个，仍低于原订目标。（YouTube EPTwcWU626TzI，[2030.8-2042.7]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-975 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-975`；w172 YouTube 章节路由采纳）

据讲者口述：OpenBSD 的传感器子系统于 1999 或 2000 年被引入，2003 年由 Alexander Yershov 报告并加入了 lm4 与 amp 两个传感器驱动。（YouTube EPTwcWU626TzI，[1704.1-1721.5]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-310 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-310`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Iain R. Learmonth 口述：OpenBSD 于 1995 年自 NetBSD 分叉，此后力求默认安全并重视代码质量。（YouTube EPa2ttG9bdfig，[1312.48-1324.31]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-311 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-311`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Iain R. Learmonth 口述：LibreSSL 提供了新的 libtls API。（YouTube EPa2ttG9bdfig，[2233.599-2241.109]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-611 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-611`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Laurent Bernaille 口述：迄今 AWS 对 OpenBSD 仍无官方 MI 支持（转写音作 MI；MI 指 OpenBSD 的 machine-independent，机器无关代码）。（YouTube EPicR06naQ8LI，[3077.73-3086.67]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-627 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-627`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：讲者称约五年前该技术突然以内核驱动形式出现在 OpenBSD（转写音作 open V on openbsd）上，且当时实现相当简陋。（YouTube EPipbPcNXeDj4，[371.08-379.27]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-679 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-679`；w172 YouTube 章节路由采纳）

据〔NYC*BUG 2023〕讲者 Ori Bernstein 口述：GEFS 快照代计数机制借鉴自 ZFS；Matt Ahrens 于 2019 年 BSDCan 曾演讲详解该机制（YouTube EPjuFndFy72gI，[1149.2-1172.6]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-738 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-738`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Massimiliano Stucchi 口述：他通过 pfctl 填写 table，把现场看到正在攻击目标的 IP 地址加进去。（YouTube EPlty1aqNgqkU，[6737.28-6748.07]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-801 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-801`；w172 YouTube 章节路由采纳）

据〔Modernizing relayd & the road to HTTP/2 报告（来源不详）〕讲者 Reyk Floeter 口述：libtls（转写音作 Lib tlf）是不错的 TLS 库，构建在 libssl 之上。（YouTube EPo4T41IQFhMg，[965.36-978.31]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-842 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-842`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：当时显而易见的选择是采用 FreeBSD 或 NetBSD 的 rc.d 与 rc.order。（YouTube EPpjHDvO_haQY，[598.24-606.43]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-841 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-841`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：他们曾快速考察过 Solaris 与 Illumos 的 SMF（转写音作 SMH SMF）以及 launch（转写音作 launchd）方案。（YouTube EPpjHDvO_haQY，[476.36-481.75]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-877 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-877`；w172 YouTube 章节路由采纳）

据〔EuroBSDCon〕讲者 Dave Voutila 口述：NetBSD 与 OpenBSD 在 UVM 上已大量分化，而 FreeBSD 如今使用的是一套完全不同的虚拟内存框架。（YouTube EPqKrxVzS96BM，[1710.72-1723.07]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-885 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-885`；w172 YouTube 章节路由采纳）

据〔Why rewrite fw_update(8)? 报告（来源不详）〕讲者 Andrew Hewus Fresh 口述：fw_update 的 FTP 组件虽已 pledge 与 unveil，仍属旧实现。（YouTube EPqsGBjXzI9OU，[1782.76-1789.83]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-987 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-987`；w172 YouTube 章节路由采纳）

据〔BSDCan 2018〕讲者 Ayaka Koshibe 口述：Mininet 的 OpenBSD 端口自 2017 年 8 月起合入 ports 树，讲者另维护一个也支持 FreeBSD 的 Mininet（转写音作 mignonette）GitHub Fork。（YouTube EPu-E8emCBGXI，[2654.859-2662.89]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-988 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-988`；w172 YouTube 章节路由采纳）

据〔BSDCan 2018〕讲者 Ayaka Koshibe 口述：Mininet Fork 在 FreeBSD 上运行于 VM 中的 jails 内（转写音作 vm h jails）。（YouTube EPu-E8emCBGXI，[2662.9-2681.22]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1119 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1119`；w172 YouTube 章节路由采纳）

据〔EuroBSDCon 2012〕讲者 Philip Guenther 口述：Solaris 9 及 FreeBSD 在相关线程实现上采用了相同方式。（YouTube EPxAJpfy_Hhy4，[152.56-164.63]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1118 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1118`；w172 YouTube 章节路由采纳）

据〔EuroBSDCon 2012〕讲者 Philip Guenther 口述：Solaris、FreeBSD、NetBSD 采用 jump table 作为线程切换的已知方法。（YouTube EPxAJpfy_Hhy4，[2698.88-2706.309]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1164 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1164`；w172 YouTube 章节路由采纳）

据〔OpenBSD 技术分享〕讲者口述：DTrace 在 Solaris 发布数年后约 2007 年进入 macOS，并延伸至 FreeBSD、NetBSD、Linux。（YouTube EPyHKx57Wv6DA，[291.7-301.68]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1165 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1165`；w172 YouTube 章节路由采纳）

据〔OpenBSD 技术分享〕讲者口述：DTrace 最初为 Solaris 开发，之后也被 FreeBSD 与 NetBSD 采用。（YouTube EPyHKx57Wv6DA，[74.61-85.49]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1746 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1746`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Ted Unangst《OpenBSD vs SMP, Threading, and Concurrency》演讲〕讲者口述：OpenBSD 内核中散布的 simple locks（自旋锁）是继承自 Berkeley 的遗留物，在 OpenBSD 中从未被使用、也不会被使用，部分原因是它们很可能本身就是错的。（YouTube EPhKpljl-kI3I，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1747 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1747`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Ted Unangst《OpenBSD vs SMP, Threading, and Concurrency》演讲〕讲者口述：巨型锁（giant）实际上把内核里其他所有互斥量都吞并了——即使专门给 TCP 栈加上七十几个新锁、实测一切看着正常，也根本没法判断改动是否真的生效，因为那些代码本身仍然在 giant 的保护之下跑。（YouTube EPhKpljl-kI3I，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1748 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1748`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Ted Unangst《OpenBSD vs SMP, Threading, and Concurrency》演讲〕讲者口述：OpenBSD 当时自带的 libpthread（转写作“the L P thread”）是一个纯用户态实现、属于 FreeBSD 的附加件，之前工作得很好，但存在一系列问题，其中之一是完全无法扩展到 SMP。（YouTube EPhKpljl-kI3I，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1749 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1749`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Ted Unangst《OpenBSD vs SMP, Threading, and Concurrency》演讲〕讲者口述：面对当场听众问“其他项目为何不直接取用（FreeBSD 的）witness”，台下指出它就是 BSD 授权的、不存在许可障碍。（YouTube EPhKpljl-kI3I，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1777 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1777`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon 2024 Rob Keizer《Global anycast using OpenBSD on a budget》演讲〕讲者口述：OpenBSD 上现有的 FUSE 版本仅支持 sshfs 与少数其他项，这是讲者最希望看到改变的一点（他同时表示 FUSE 本身很好用、自己也并未编写该实现）。（YouTube EPHiEzmIi3B24，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1778 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1778`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon 2024 Rob Keizer《Global anycast using OpenBSD on a budget》演讲〕讲者口述：讲者称 OpenBSD 的包处理大致只能有效跑满单核，需借助网卡卸载，但即便如此，在推到两三百 Gbps 量级时 CPU 侧仍是问题所在。（YouTube EPHiEzmIi3B24，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1779 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1779`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon 2024 Rob Keizer《Global anycast using OpenBSD on a budget》演讲〕讲者口述：corosync 在 OpenBSD 上需自行打补丁方能运行（耗时良久），且其默认网络栈已弃用 UDP，故讲者通常不建议拿 corosync 承担此用途。（YouTube EPHiEzmIi3B24，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1796 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1796`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Building an accessible OpenBSD laptop〕讲者口述：讲者称这台笔记本所用的基层 USB 3 控制器驱动并不支持该传输类型——既没有正确的错误处理，也没有把缓冲区正确送入送出的方式，这部分根本没做、未被实现，因此相关流式设备无法使用；他自 2017 年起着手补这块。（YouTube EPMa_Y1hVmK8o，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1797 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1797`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Building an accessible OpenBSD laptop〕讲者口述：讲者称这段 USB 相关工作并非他一人完成——他当时还在并行做别的事，恰逢合适的人在合适的时间出现并加入协作，最终由 Alexander Racha 修掉了其中大量 bug，他称之为非常难得的一件事。（YouTube EPMa_Y1hVmK8o，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1798 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1798`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Building an accessible OpenBSD laptop〕讲者口述：讲者称本机第二个扬声器无法开箱使用，这部分并非他本人完成，而是由一位贡献者（转写音作 Joshua）反向工程该音频设备的驱动，找出能启用正确扬声器的一串魔数命令序列，需要向硬件喂入一长列十六进制值。（YouTube EPMa_Y1hVmK8o，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1799 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1799`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Building an accessible OpenBSD laptop〕讲者口述：麦克风与扬声器是另一回事——虽也开箱不工作，但讲者查出问题出在某处的连接方式（转写音作 one surface wired up）上，只需改配置即可修好，不需要改动任何代码。（YouTube EPMa_Y1hVmK8o，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1978 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1978`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Klemens Nanni（字幕误作 Clements/Clements）EuroBSDcon 2023 讲座 The OpenBSD Installer〕讲者口述：OpenBSD 安装器不只是安装，也能升级；用户已有 OpenBSD 系统想取新版本时，执行升级的代码与执行安装的代码完全相同，“安装”一词在其口径中涵盖所有模式。讲者称转写中 'open business' 实为 OpenBSD。（YouTube EPr6MwG5D5r5U，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1979 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1979`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Klemens Nanni EuroBSDcon 2023 讲座 The OpenBSD Installer〕讲者口述： OpenBSD 安装器的绝大部分能装进一张小 i386 软盘，仅数兆字节，却可完成安装、升级、无人值守安装与联网交互式升级，并称在如此小的体量下做到这些颇为令人惊讶。（YouTube EPr6MwG5D5r5U，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1980 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1980`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Klemens Nanni EuroBSDcon 2023 讲座 The OpenBSD Installer〕讲者口述：OpenBSD 自多年以前就已官方支持 amd64 及其他平台的加密磁盘安装；安装器中那行看似简单、默认选否的“加密根分区”新提问，实际是多年间进入代码树的庞大改动列表的结果——若想把这一能力从 amd64 扩展到更多架构，就会发现自己触及大量此前没人考虑过的边角情形。补充口述：softcrypto（可加密磁盘与软加密）在所支持的全部架构上都能编译启用，但并非全部架构都能在引导加载器阶段就识别此类磁盘，故加密安装在 amd64 机器上可行，在 armv7 上则不可行。（YouTube EPr6MwG5D5r5U，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1997 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1997`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔D. Gwynne 的 OpenBSD active-active 防火墙集群演讲〕讲者口述：OpenBSD 的防火墙叫做 PF，它替代的是此前的 IP filter；后来对 IP filter 的许可证条款作了一次澄清，结果它因此被从源码树中移除，讲者称这对他个人来说相当令人震惊。（YouTube EPcBxDgevQpCg，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1998 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1998`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔D. Gwynne 的 OpenBSD active-active 防火墙集群演讲〕讲者口述：所幸有一位名叫 Daniel Hartmeier 的人接上来动手写了 PF；讲者称亲眼看着事情推进之快相当惊人——IP filter 在数周内（或一个月内）就从树上消失了，而 PF 随即就位，并赶在下一个版本发布时进入。（YouTube EPcBxDgevQpCg，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1999 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1999`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔D. Gwynne 的 OpenBSD active-active 防火墙集群演讲〕讲者口述：几年前出现的做法是一种叫做 pfsync 的协议，它存在的唯一目的就是在多台 PF 防火墙之间共享状态表；它是一个非常简单的协议——就是一个带 IP 头的裸 IP 包，内部没有任何声明自己是 UDP 或 TCP 之类的内容，只是内核之间的数据报。（YouTube EPcBxDgevQpCg，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2000 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2000`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔D. Gwynne 的 OpenBSD active-active 防火墙集群演讲〕讲者口述：讲者自述已投入 OpenBSD 源码树的是协议处理、状态管理与解析的整块重写，这次约四千行改动的绝大部分在数周前已提交进 open BSD 的源码库，并将进入 4.5 版本的发布。（YouTube EPcBxDgevQpCg，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2023 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2023`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔OpenBSD vmm Update -- Mike Larkin 讲题〕讲者口述：讲者称该 C BIOS 包不随 base 交付，因为它属于“强许可”（转写音作 Stockman opener），且有人不希望 base 中出现此类许可。（YouTube EPg2kJGkVxWa8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2024 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2024`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔OpenBSD vmm Update -- Mike Larkin 讲题〕讲者口述：讲者称 FreeBSD 来宾所暴露的问题需要指令译码器（instruction decoder）；vmm 开发已两年多却一直不需要它，他一直有意识地把它往后推。（YouTube EPg2kJGkVxWa8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2025 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2025`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔OpenBSD vmm Update -- Mike Larkin 讲题〕讲者口述：讲者称 Pratik 是其圣何塞州立大学硕士课程的学生，他与另外三名学生实现了 vmm 的“send and receive”即迁移；新版 vmctl/vmd（转写音作 NCTM e of d）可暂停与恢复，并可发送与接收虚拟机。（YouTube EPg2kJGkVxWa8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2026 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2026`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔OpenBSD vmm Update -- Mike Larkin 讲题〕讲者口述：讲者提出的内核隐藏（undrJV）思路是借 vmm 把现有宿主自身当作虚拟机启动，从而隐藏全部内核文本；他自认这不是新想法，Blue Pill 早已做过类似事情，也可能有人做过相近的事。（YouTube EPg2kJGkVxWa8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2103 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2103`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon 2024〕讲者口述：OpenBSD 的 IPv6 支持起于 1999 年 KAME 并入（字幕音作“K St”“K project”）；KAME 是一个日本研究项目，其内容早于讲者本人的时期，他自述并非史家；该研究项目 2006 年停止，其代码并入后仍由 OpenBSD（字幕音作“OPD”）继续维护。（YouTube EPQ4b26mqb_G8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2104 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2104`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon 2024〕讲者口述：对照 RFC 6724 逐行读 OpenBSD 的源地址选择实现，他盯着那张判定表与代码看了好几天，想弄清“是否需要替换当前最佳地址”的分支究竟会不会被触发，结论是不会——不存在任何会实际执行替换的情形，这段判定逻辑在实现中不会走到。（YouTube EPQ4b26mqb_G8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2105 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2105`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon 2024〕讲者口述：为解决旧做法的缺陷，他把 router advertisement 处理从内核整体拆出、搬到用户态，亲自写了 slaacd——他称 2018 年 BSDCan 已有一场专门的报告讲这件事，该进程特权分离并执行 pledge（字幕音作“privileg separated”“pledged”，slaacd 音作“slacky”）。（YouTube EPQ4b26mqb_G8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2106 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2106`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon 2024〕讲者口述：在 IPv6-only 场景下客户端侧用 pf 也能完成这套地址转换，但规则“极其复杂”（字幕音作“massively more comp complicated”）且有其原因——首先必须把该 IPv6 地址动态设置上去，因为 pf 没有办法表达“取该接口上的全局地址、把它填作 from”，这不是 pf 的能力。（YouTube EPQ4b26mqb_G8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2119 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2119`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔OpenBSD Network Stack Internals，Claudio Jeker〕讲者口述：socket API 是 BSD 最成功的一次输出——连 Windows 也实现了它；因此 OpenBSD 尽量不大幅改动 socket API。（YouTube EPV85It0dGUF4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2120 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2120`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔OpenBSD Network Stack Internals，Claudio Jeker〕讲者口述：mbuf“API”其实并非 API，只是一堆操纵 mbuf 与指针的函数，多数带不算太坏、部分带极坏的副作用，是网络相关故障的第一大原因；网络栈一崩溃，要么出在 mbuf，要么多半出在路由表。（YouTube EPV85It0dGUF4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2121 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2121`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔OpenBSD Network Stack Internals，Claudio Jeker〕讲者口述：PF 是 m_tag 的最大使用者，几乎所有每个数据包都挂有 m_tag；把这份元数据从 m_tag 直接移入包头后，PF 在低速机器上的性能翻了一倍。（YouTube EPV85It0dGUF4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2122 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2122`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔OpenBSD Network Stack Internals，Claudio Jeker〕讲者口述：OpenBSD 在近年扩展了路由表代码：加入路由标签（route labels）、启用多路径（multipath）路由、支持多张路由表；另两项在研工作是路由域与路由优先级。（YouTube EPV85It0dGUF4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2238 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2238`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon 2024，Alexander Bluhm 演讲“A Packet's Journey Through the OpenBSD Network Stack”〕讲者口述：OpenBSD 的网络协议栈已把诸如 X.25 之类的非 IP 协议族全部移除，如今只保留 IP 一族，其上只叠置 UDP、TCP 与 raw IP，再往上是 socket 层作为应用与协议之间的接口。（YouTube EPKn2XEW4Qre0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2239 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2239`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon 2024，Alexander Bluhm 演讲〕讲者口述：当 UDP 报文的队列丢弃计数上升时，说明系统处理速度不足；RX 恒指接收队列、TX 指发送队列，据此可判断瓶颈位于本地上游——是 UDP 或 raw IP 报文送达速度超出本机处理能力。（YouTube EPKn2XEW4Qre0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2240 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2240`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon 2024，Alexander Bluhm 演讲〕讲者口述：OpenBSD 的 PF 本质上是嵌在 IP 输入与 IP 输出路径中、调用 PF 测试函数完成全部 PF 处理；规则写作 PF in／PF out 两类，in 规则匹配报文进入方向，out 规则匹配报文离开方向。（YouTube EPKn2XEW4Qre0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2476 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2476`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔OpenBSD 网络启动工作站一讲〕讲者口述：起因是公司内 IT 部门的岗位交换项目，由此生出想法——试试看把 OpenBSD 跑到公司工作站上到底有多难。（YouTube EPkFqHXfWEB4o，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2477 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2477`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔OpenBSD 网络启动工作站一讲〕讲者口述：他们部署新机器的办法是把该机的 MAC 地址录入中心系统、再把它放到公司某处，机器随后启动、选定安装项并自动完成安装。（YouTube EPkFqHXfWEB4o，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2478 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2478`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔OpenBSD 网络启动工作站一讲〕讲者口述：他在自己研究部门的项目里把两台机器用一根网线直连成一个小型网络，结果网络启动不工作、机器卡住报错，因为始终拿不到反向 ARP 的应答（转写音作 the reverse a purpose）。（YouTube EPkFqHXfWEB4o，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2479 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2479`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔OpenBSD 网络启动工作站一讲〕讲者口述：上述失败的原因是启动时内核探测并初始化所有设备，网卡初始化使链路反复 down/up，对端链路随之抖动，服务端应答地址请求的那个守护进程（转写音作 demon）因此漏掉了客户端询问自身 IP 地址的报文。（YouTube EPkFqHXfWEB4o，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2483 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2483`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔“Bidirectional Forwarding Detection BFD implementation and support in OpenBSD”汇报〕讲者口述：讲者自名 Peter（转写音作 Hustler），正在为 OpenBSD 实现双向转发检测（BFD）协议。（YouTube EPnLq6T8zUryo，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2484 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2484`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔同上 OpenBSD BFD 汇报〕讲者口述：受 OpenBSD 内核架构的制约，其 BFD 实现极不可能支持快于每 50 毫秒一次的检测，即便 50 毫秒也已非常激进；就其当前用例而言这不成问题。（YouTube EPnLq6T8zUryo，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2485 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2485`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔同上 OpenBSD BFD 汇报〕讲者口述：截至汇报时，其实现已覆盖 RFC 5880 与 5881（BFD 基础规范与单跳 IPv4/IPv6 规范）的全部必选项，能与 Juniper 设备建起会话并完成常规健康检查。（YouTube EPnLq6T8zUryo，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2486 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2486`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔同上 OpenBSD BFD 汇报〕讲者口述：该实现完全位于内核之内，但因所用机制并未绕过协议栈，BFD 报文以普通数据包形式进出常规网络接口，故可用 PF 对其拦截或作其他操纵。（YouTube EPnLq6T8zUryo，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2487 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2487`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marko Cupać 关于 OpenBSD 高可用 WAN 的演讲〕讲者口述：其负责运维一张约 30 节点的广域网，该网完全基于 OpenBSD 路由器构建，站点侧交换机则用 Juniper。（YouTube EP2-GwlUFG6oA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2488 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2488`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marko Cupać 关于 OpenBSD 高可用 WAN 的演讲〕讲者口述：其公司自托管 DNS、Web、数据库、邮件、LDAP、即时通信等全部基础互联网服务，均以 FreeBSD jails 承载。（YouTube EP2-GwlUFG6oA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2489 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2489`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marko Cupać 关于 OpenBSD 高可用 WAN 的演讲〕讲者口述：其 WAN 采用 hub-and-spoke 拓扑，hub 侧实施 CARP 与 pf 状态同步，每个 spoke 四条 GRE 隧道并以传输模式 IPsec 保护，密钥交换机制选用 isakmpd。（YouTube EP2-GwlUFG6oA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2490 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2490`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marko Cupać 关于 OpenBSD 高可用 WAN 的演讲〕讲者口述：其明知 iked 更新、还有更新的东西，仍坚持选用 isakmpd，理由是它久经验证、成熟可靠。（YouTube EP2-GwlUFG6oA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2534 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2534`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Claudio Jeker 在 AsiaBSDCon（东京）口述 vscsi(4) 与 iscsid〕讲者口述：vscsi 是 OpenBSD 的用户态虚拟 SCSI 控制器，其目的把内核 SCSI 中间层暴露到用户态，让用户态得以实现 SCSI 控制器：内核通过 ioctl 接口把 SCSI 命令自中间层下传，用户态程序对这些调用作出回应。（YouTube EP9SPM1y-HynQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2535 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2535`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Claudio Jeker 在 AsiaBSDCon（东京）口述 vscsi(4) 与 iscsid〕讲者口述：讲者自认 OpenBSD 在 iSCSI initiator 上“fairly late in the game”并作三大 BSD 对比： FreeBSD 已有 initiator，全部在内核里实现，用一个内含全部 initiator 代码的内核模块；NetBSD 是用户态 initiator，走其 FUSE（原文 “re-fuse or whatever they call it now”）一类的用户态文件系统接口。（YouTube EP9SPM1y-HynQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2536 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2536`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Claudio Jeker 在 AsiaBSDCon（东京）口述 vscsi(4) 与 iscsid〕讲者口述：OpenBSD 自写 initiator 的理由是目标不同：要简单实现与更多安全，不愿在内核里放大量以超用户权限运行的代码，也不愿常驻一个以超用户权限运行的守护进程；同段后文称因此重视 privilege dropping 与 privilege separation，并补充说 vscsi 只需在打开设备节点时取权，故 iscsid 可用 chroot 加降权而无需完整特权分离。（YouTube EP9SPM1y-HynQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2537 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2537`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Claudio Jeker 在 AsiaBSDCon（东京）口述 vscsi(4) 与 iscsid〕讲者口述：内核侧 vscsi 实现约 600 行代码，用户态 iscsid 为数千行，因此整个工程对外看似复杂的协议实际上是个很小的程序。（YouTube EP9SPM1y-HynQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2644 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2644`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Alexandre Ratchov〕讲者口述：就音频子系统应置于内核还是用户态，讲者的结论是内核实现并无额外好处，故该项目在用户态实现，以求简单。（YouTube EPWcro3UliMZ4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2645 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2645`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Alexandre Ratchov〕讲者口述：该框架围绕一个音频服务器构建，由它完成格式转换、重采样、混音与声道映射。（YouTube EPWcro3UliMZ4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2646 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2646`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Alexandre Ratchov〕讲者口述：音量控制选择走 MIDI（转写音作 Medi／Med），因为 MIDI 是标准协议，可以直接复用现有应用。（YouTube EPWcro3UliMZ4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2647 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2647`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Alexandre Ratchov〕讲者口述：该项目的目的之一，是让若干小工具能够协同工作，而不是依赖大而单一的程序（Unix 哲学）。（YouTube EPWcro3UliMZ4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-20 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-3367 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3367`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔WIP vmm and Vagrant -- Philipp Buehler〕讲者口述：转写作 way rent 的 Vagrant 把虚拟机配置抽象成简单声明：用户只需写明两 GB 内存与网卡等需求，无需理解底层 hypervisor 或 provider 的配置，无论 provider 是 VirtualBox、转写损毁未敢补名的后端、还是转写作 Penniston cloud 的云上服务，都没有差别。（YouTube EPUI8TtQ6zowE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3368 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3368`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔WIP vmm and Vagrant -- Philipp Buehler〕讲者口述：讲者写了一个 Vagrant 插件：让 Vagrant 感知自己正运行在 OpenBSD 之下，并教会它如何与转写作 right out 的 hypervisor（vmm）及其配套组件打交道——即用转写作 we have CTL 的 vmctl 以适当选项，达到 Vagrantfile 中定义的期望状态。（YouTube EPUI8TtQ6zowE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3369 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3369`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔WIP vmm and Vagrant -- Philipp Buehler〕讲者口述：在 OpenBSD 上定义一台安装服务器：走典型 OpenBSD 安装器、大约按七次回车，再设置 FTP／HTTP 等服务即可开跑。（YouTube EPUI8TtQ6zowE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
