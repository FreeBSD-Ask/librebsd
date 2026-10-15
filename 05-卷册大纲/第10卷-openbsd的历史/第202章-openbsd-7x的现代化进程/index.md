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

- 新转写清晰读出：OpenBSD 帧缓冲的 rasops（RasterOps）系 2001 年自 NetBSD 引入，i386/AMD64 帧缓冲控制台于 2013 年随 Intel DRM 与 Radeon DRM 启用，细节仍宜对照 Cambus 原文。　[存疑脚注] 平台与时间细节待原文核对（BSD Now EP368，[203.20-240.50]，L4）[订正：原 引入时间与平台细节存在 ASR 转写噪声且 [215.94-251.96]，2026-09-30 SenseAudio 重转核对]
- 转录将 Martin Husemann 记作 Martin Hussman，且节目开场将 NetBSD 11 与 FreeBSD 11 混写，须以 NetBSD 官方博客核验。　[存疑脚注] 人名与版本号存在转写歧义，未与 NetBSD 官方公告核验（BSD Now EP626，[1636.36-1806.82]，L4）
- OpenJDK 维护者姓名在转录中作 Harold 或 Harald，具体拼写须以 FreeBSD Foundation 原文核验。　[存疑脚注] 维护者姓名存在转写歧义（BSD Now EP626，[867.98-873.02]，L4）

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
