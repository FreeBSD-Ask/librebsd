---
chapter: 第 177 章
id: CH177
volume: 第09卷-netbsd的历史
---

# 第 177 章 netbsd嵌入式市场与外部批评

## 要点

- NetBSD 嵌入式部署记录（**ports/** 目录）与硬件支持文档是研究嵌入式应用的一手史料
- 批评 NetBSD 的原始发言与邮件列表讨论是研究外部批评的一手史料
- NetBSD 缺乏商业支持体系是嵌入式市场应用的障碍；2000 年 Wasabi Systems 成立，提供 NetBSD 商业支持、定制开发、咨询与培训；Wasabi 模式借鉴 Red Hat 商业模式但规模较小，主要客户为嵌入式设备厂商；Wasabi 贡献了 NetBSD ARM 移植、嵌入式优化等代码；Wasabi 模式是 NetBSD 早期商业-社区平衡的尝试，但因规模有限未能持续
- NetBSD、FreeBSD、OpenBSD、Linux 在 1994-2004 年的发布节奏与市场份额变化
- NetBSD 1.x 时期内核权限边界缺陷在嵌入式场景下具有特殊影响——NetBSD-SA1998-005（**mmap(2)** 设备驱动权限检查缺陷，本地用户可映射设备内存访问任意物理内存）、NetBSD-SA2000-001（**procfs(5)** 权限检查缺陷，本地用户可读取其他进程内存映射）、NetBSD-SA2001-009（SUID 程序执行与 **ptrace(2)** 竞态条件

## 史料

- NetBSD 官方嵌入式移植文档（**ports/** 目录）与硬件支持列表（PLATFORMS）；NetBSD、FreeBSD、OpenBSD 与 Linux 1994-2004 年发布公告档案；NetBSD-SA1998-005、NetBSD-SA2000-001、NetBSD-SA2001-009 安全公告原文

## 史观

- 总纲第 4 条（分离聚合是永恒规律）：NetBSD 在嵌入式细分市场的深耕系从通用工作站市场分离后的再聚合——ports 架构矩阵的扩张与收缩即分合循环的物质层。
- 总纲第 3 条（不存在进步，只有权力再分配）：1994-2004 年嵌入式市场份额的升降并非线性进步叙事，Wasabi Systems（2000 年成立、借鉴 Red Hat 模式、终未能持续）的商业兴衰即权力再分配的注脚。
- 自反性声明：本章史观映射系基于项目统摄史观的具体时点释读，欢迎被超越。

## 辨析

- 部署记录的完整性需考据——部分部署可能未被完整记录；需对照多源档案核实
- Wasabi 成立的具体时间存在叙事分歧——部分资料称 2000 年，部分称 1999 年，需对照公司注册档案核验；Wasabi 衰退的具体时间与原因需考据。经 netbsd.duckdb netbsd-src 仓库 commits 表验证：Wasabi 相关 commit 最早可追溯至 2000-10-24（thorpej 性能计数器工具，署名 From Frank），2001-11-24 jhawk 提交 Wasabi 版权声明更新（commit 记录见文献），与 Wasabi 运营期吻合
- 市场份额数据的具体口径需考据——不同统计口径可能差异较大；需对照多源档案核实
- 嵌入式设备是否普遍以 root 运行单一应用须考据——Dreamcast、Zaurus 等设备的具体权限配置须对照设备文档核验；“远程 → 本地 → 内核” 攻击链在嵌入式场景下的实际案例须考据——公开攻击案例可能有限，须对照安全研究报告核验；he 的 procfs 修复 commit `a685050c3f4b3919cc804eea7792397efc311b4e` 标注 “Fix a cri…”（引文系 commit subject 截断残留，全文须以 commit 记录原文为准）

## 文献

- NetBSD-SA1998-005、NetBSD-SA2000-001、NetBSD-SA2001-009 公告原文；netbsd.duckdb netbsd-src 仓库 he procfs 修复 commit ［A］
- NetBSD 嵌入式史料分析

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1998-2004 年间：549,070 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD 外部批评史料分析

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- Wasabi Systems 公司档案；NetBSD Foundation 与 Wasabi 合作记录；Wasabi 贡献的 NetBSD commit log；thorpej. A program for reading performance counters. netbsd-src 仓库 [DB/OL]. 2000-10-24T23:54:31Z；simonb. Add a port to IBM's PPC405GP Reference Board. netbsd-src 仓库 [DB/OL]. 2001-06-13T06:01:44Z；jhawk. Wasabi copyright notice update. netbsd-src 仓库 [DB/OL]. 2001-11-24T23:53:18Z；origin/netbsd-1-5. netbsd-src 仓库 branch [DB/OL]. 2004-12-10T23:08:26Z. commit: 1c43a6ba5391；origin/netbsd-1-6. netbsd-src 仓库 branch [DB/OL]. 2006-06-01T06:03:17Z. commit: e5a9a0024746 ［A］---

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- BSD 与 Linux 市场份额史料分析

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1994-2004 年间：279,033 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。

（收录限定：本期为 BSDCan 2026 周六流多场演讲合并转写，与本章直接相关者仅 RiscBSD→acorn32 演化与 NetStation NFS 网络引导两段，其余 anyRAID、扩展错误消息、CHERI、pkg base 段落系同期演讲背景收录）

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：YouTube EPmZ-dhntnkCQ（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Allan Jude 在 BSDCan 2026 报告 OpenZFS 的 anyRAID 方案：vdev 空间被划分为 16 GiB 的 tile，经一块置于 vdev 前端固定偏移、保留四份冗余的 tile map 完成逻辑到物理的间接寻址，无需导入存储池即可读取，从而把 RAID Z 固定条带宽度改造为可随盘数动态伸缩的条带，支持镜像与 RAID Z1/2/3 混合、vdev 扩容与收缩、以及以重平衡替代整盘搬迁，并兼容快照、DDT、块克隆与收发等既有 ZFS 特性，定位于以最低每 TB 成本换取最大容量与灵活性；其约束亦被明确：tile map 容量决定单 vdev 上限 256 盘与 65000 tile，未来新盘不得超过初始最小盘的 1024 倍，收缩下限为 RAID Z 条带宽度。（YouTube EPmZ-dhntnkCQ，[1044.959-1120.639]，L1）
- 一位 NetBSD 发布工程团队成员自述三十年产品史：1994 年 RiscBSD 宣布把基于 NetBSD 的 ARM Unix 带上 32 位的 Risc PC，与主张直接采用 4.4BSD 代码、面向旧机型的 ArcBSD 项目以及南安普顿一名学生的单人 Linux 移植形成三路线竞争；同年 FreeBSD 提交者 Gary Palmer 澄清 ArcBSD 实际改用 FreeBSD，RiscBSD 则演化为 NetBSD 的 acorn32 移植并延续至今。演讲人 1996 年为 Acorn 面向 Oracle 网络计算机参考设计的 NetStation 构建经 NFS 网络引导的 NetBSD 方案并于 1997 年公开演示，1999 年在 Exemplar 被 Apple 全资收购、技术支持团队整体被裁后创办 Precedence Technologies 承接存量支持合同，其 NetManager 产品以单一 shell 风格配置文件加逐服务构建脚本实现跨 NetBSD 版本的配置迁移，并随 Citrix XenServer 8.4 弃用半虚拟化内核而被迫从惯用的奇数版本策略迁入 NetBSD 10 的 HVM 时代。（YouTube EPmZ-dhntnkCQ，[5260.96-5994.64]，L1） [订正：原“……NetBSD 方案并公开演示”承前系于 1996 年→演示实为 1997 年（转写 [5518.0-5527.4]：we demonstrated this to the public in 1997），内容复核]
- Kirk McKusick 报告 FreeBSD 内核的扩展错误消息框架，并以设计史还原开篇：Unix 的纯整数错误码根源于 PDP-11 的 16 位地址空间——64K 文本段约合一万行 C，字符串是稀缺资源，内核以数字返回、用户态再展开为可读串曾是工程必然；在 64 位地址空间下该约束失效，新框架允许系统调用返回带至多两个参数的格式化错误串，逐文件注册错误类别、可经编译选项剥离以兼顾嵌入式场景，由 C 运行时与线程库按线程预置缓冲、成功调用零开销，错误沿 BIO 与内核线程上下文逐层回传至发起进程，并可用 ktrace/kdump 检视。（YouTube EPmZ-dhntnkCQ，[13264.96-14136.88]，L1）
- Brooks Davis 阐述 CHERI 能力架构的 FreeBSD 集成路线：团队目标在 FreeBSD 16 至少交付空间安全支持、时间安全视进度而定；上游选择覆盖 RISC-V Y 标准（目标 tier 2）与 Morello 两类硬件，后者被视为终将被蒸馏的超集架构；策略上内核支持先行、纯能力模式起步并明确拒绝混合模式，再依次推进用户态库、运行时链接器与基于链接器的隔离仓， heap 时间安全列为更高风险的后续阶段；机器无关部分改动量级与一次 RISC-V 移植相当，而 CheriBSD 的先行积累被其视为 FreeBSD 及其他 BSD 相对 Linux 的先发优势。（YouTube EPmZ-dhntnkCQ，[18933.2-19045.52]，L1） [订正：原“机内相关改动量级”→“机器无关部分改动量级”（转写 [19590.1-19611.0]：the machine independent parts of Cherry support…on the order of the RISC-V support），内容复核]
- 一位自称系统管理员的讲者报告在无互联网内网环境下近两年的 pkg base 生产实践：15.0 技术预览把基本系统拆为 495 个包并提供 minimal（约 60 包）与 minimal-jail（42 包）等包集，其工作流为在联网侧构建服务器执行 buildworld、buildkernel 与 build packages，再经 nginx 向内网发布、以 ansible 配置客户端；主机侧以 boot environment 为回滚单元完成补丁级、次版本以及经 ABI 覆盖迁往 16-CURRENT 的升级；讲者表示该机制可能在未来版本取代 freebsd-update——其去年曾称 15.0 即将取代而未兑现，本轮经主持人当场确认指向 16.0——并演示了 jail 的包化创建与官方尚不支持的 14 到 15 迁移路径。（YouTube EPmZ-dhntnkCQ，[22286.958-22458.48]，L1） [订正：原“两年余”→“近两年”（转写 [22182.3-22188.7]／[22559.8-22567.4]：almost two years），内容复核]

**史料**：

- 本期为 BSDCan 2026 周六流的多场一手口述：Allan Jude 报告 anyRAID 设计并致谢 Klara 团队成员 Paul 的实现，及 Brian Behlendorf、Alexander Motin、Tony Hutter、Alec Pinchek 等评审，提及上年十月 ZFS 开发者峰会上的早期报告与 Seagate 就元件级故障盘用例的接洽；Brooks Davis 给出 CHERI 研究中心站点、IEEE 安全与隐私杂志特刊获奖综述、CHERI ISA v9 技术报告与 RISC-V Y 架构批准草案等文献线索；Kirk McKusick 以 mmap 系统调用系列用例演示扩展错误并指向第九节手册页 xerror；Warner 自述 FreeBSD 15.0 RC 阶段引导挂起的定位过程，称在晚餐前的 LLM 会话中发现引导装载器 staging 区域地址被编码进页表，移动四十行代码即修复；另有 FreeBSD Foundation 实习生报告 AMD ROCm 原生移植的 LLVM 改动上游化与 KFD 移植进展，以及一位开发者报告其树莓派公共 NTP 服务每秒 213 次请求、日均约 1800 万客户端。　[考据脚注] 本流转写为多场演讲音频交错合并，企业与项目名存在系统性音变（如 Klara、CHERI、Acorn 等拼写），人名多为转写音变形态；引用名单、数字前须与会议官方议程、OpenZFS 代码评审记录交叉核对。（YouTube EPmZ-dhntnkCQ，[3235.2-3259.52]，L3）

**史观**：

- 总纲22 知识注定过时：扩展错误演讲的论证本身就是一次历史考据：McKusick 把当代内核接口的形态还原到 PDP-11 文本空间约束的生成语境，指出 errno 的紧凑形式在 16 位机器上曾是工程必然，而约束消失后它从最优设计退化为纯粹的路径依赖——知识注定过时，形式比内容活得更久。（YouTube EPmZ-dhntnkCQ，[13264.96-13408.88]，L1）

**辨析**：

- Brooks Davis 自认 RISC-V Y 架构批准时点“我们已经说了好一阵子”，提示其 FreeBSD 16 时间表属目标性陈述而非承诺，引用时不宜当作既成事实；另据 Warner 自述，RC 阶段引导问题的 LLM 辅助调试“省下约一周、成本三美元”系个人估计，无独立记录可验。　[存疑脚注] LLM 辅助调试所省时间与成本为讲者单方估计；RISC-V Y 批准时点为目标性陈述，转写中 15.0 RC 版本号写作 150.1 RC3，精确版本待核官方发布记录。（YouTube EPmZ-dhntnkCQ，[18894.56-18907.04]，L4）

**文献**：

- [YouTube EPmZ-dhntnkCQ] BSDCan 2026. BSDCan Saturday 2026-06-20 周六场流（Allan Jude、Kirk McKusick、Brooks Davis 等多场演讲合流）[EB/OL]. (2026-06-20)[2026-08-15]. <https://www.youtube.com/watch?v=mZ-dhntnkCQ>.［著录注：原条目作者与题名误著录为"YouTube"且残留流水号"1160"、日期空括号，依核查报告按行内演讲者与流标题重著；正式逐讲题名待核会议官方议程］ [订正：原"YouTube. YouTube: BSDCan Saturday 2026-06-20: 1160[EB/OL]. ()[2026-08-15]."→重著作者、题名并补发布日期，内容复核]

<!-- /PODCAST_REVIEW -->

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

