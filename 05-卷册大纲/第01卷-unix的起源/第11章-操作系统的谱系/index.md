---
chapter: 第 11 章
id: CH11
volume: 第01卷-unix的起源
---

# 第 11 章 操作系统的谱系

## 要点

- 1978 年 UNIX 生态呈双强并起雏形——Bell Labs（研究源头，V6/V7 演进）、伯克利 BSD（学术路线，1BSD 发布）；商业 UNIX 尚处萌芽阶段，Onyx Systems、Whitesmiths 等小厂商开始探索，Microsoft 的 Xenix 尚未正式发布；地理分布横跨美国东岸（Murray Hill）、西岸（伯克利）与商业中心（硅谷）。1978 年 UNIX 生态三极：
- Tandy/Radio Shack 1977 年为 TRS-80 Model I 发布 TRSDOS，由 Randy Cook 编写；TRSDOS 代表消费电子路径，针对家庭与小企业市场；1977-1979 年间 CP/M、Apple DOS、VMS、TRSDOS 与 UNIX V7 形成多线并进格局，UNIX 谱系仅为此时期操作系统生态的一支
- 1973-1980s 年间 UNIX 安全机制呈现三极分野——Research UNIX（1969-1979）坚持极简安全模型（root + rwx + setuid + **crypt(3)**），以学术研究与小范围内部分时为应用场景，无审计、无 MAC、无 TCB；PWB/商用分支（1973-1980s）面向大规模运维与商业发行，引入 rsh、SCCS、RJE 账号管理、审计子系统、TCB 框
- 谱系树成为后续 UNIX 史书的标准叙事框架——Salus 1994、Kernighan 2019、McKusick 1996 均采用树状结构；但树状叙事遮蔽了横向影响（如 BSD 工具反向流入 System V）
- 1980 年代中期/usr/group（后 UniForum）与 IEEE 1003 委员会启动 POSIX 标准化；IEEE Std 1003.1-1988 为第一版 POSIX.1 标准（POSIX 名称由 Richard Stallman 建议，期望读作“pahz-icks”），IEEE Std 1003.1-1990 对 1988 版修订并成为国际标准 ISO/IEC 9945-1:1990

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3630] 卷“第01卷-unix的起源”第 11 章，匹配置信度 curated，原因：curated token rule
- [DB:historical_claims:claim] 关键词行级挖掘素材线索 11.12-关键词行级挖掘素材线索（1 条，CL-RM 段，见 11.12-关键词行级挖掘素材线索.md）

## 史观

总纲第 9 条——循环非进步，UNIX 谱系树不是线性进化史而是分离聚合的循环；总纲第 15 条——多方平等，VMS、MS-DOS、UNIX 三条路径在本体论层面平等对待，不以 UNIX 为“高级”标准；总纲第 4 条——分离与聚合，POSIX 标准化是分离后的再聚合尝试，但标准化的形式主义无法消除实现的多样性。

## 辨析

- 1978 年生态图的具体装机数字在不同来源中有出入；Xenix 于 1980 年才正式宣布，1978 年尚未形成商业第三极；是否含日本早期接触需考据
- TRSDOS 1977 年发布日期与版本号在不同来源中有出入；**统计局限性标注**——references 表 16,867 条中仅 7,493 条（44.42%）成功提取年份，55.58% 文献无年份信息，505 条累计数基于有年份记录计算，存在选择性偏差；本时期无 BSD commits 数据库 commit 数据（数据库 1993+ 起），统计结论限于文献计量学层面，不可外推至代码活跃度；
- 三极分野的“极”是否为后人建构需辨析——实际演化中 Research UNIX 与 PWB/UNIX 存在双向代码流动（如 PWB 工具回流至 Research UNIX）；BSD 在 1980 年代是否真为“独立第三极”需考据——BSD 安全扩展仍以 Research UNIX 极简模型为基础；1992 年四大 BSD 分立时 BSD 的“路径选择”是否有意识需辨析——可能是工程惯性而非主动选择
- 替代性叙事模型（如网状图）的可行性在 1990 年代后才有零星探索
- POSIX 标准化是否真正解决了碎片化——业界普遍认为效果有限，1990 年代仍存在大量不兼容；[考据脚注] 经考据确证的 POSIX/SUS 公告日期如下——IEEE Std 1003.1-1988（第一版，［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ 精确发布日期未从 IEEE 一手来源确认，POSIX FAQ 仅说“published in 1988”无具体月份）、IEEE Std 1003.1-1990、IEEE Std 1003.1b-1993、IEEE Std 1003.1c-1995、IEEE Std 1003.1-1996、SUSv1/Spec 1170（1994 年 X/Open 发布，其精确公告日期未从一手来源确认，仅知 UNIX 95 品牌自 1995-02 起授予）、SUSv2（1997-03-12 公告）、SUSv3（2002-01-30 公告）；关键发现：标准号年份 ≠ 公告年份。

## 文献

- USENIX Conference Proceedings 1978；Salus 1994；McKusick & Karels 1986 CSRG 报告 ［B］
- Radio Shack"TRS-80 Reference Manual" (1977)；BYTE Magazine 1977-1978 TRS-80 评测；统计分析报告：文献计量学分析.md Task 22 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/文献计量学分析.md**；SQL 查询：`SELECT id, gbt7714 FROM "references"`. **资料数据库.duckdb** [DB/OL]. 查询日期：2026-07-27；Python 统计脚本：`script/phase6_bibliometrics.py`. Task 22 参考文献增长曲线与 Price 指数。执行日期：2026-07-27 [考据脚注：references 表 16,867 条、年份提取率 44.42%、1977-1979 年累计 505 条等统计结论经 `script/phase6_bibliometrics.py` 执行结果与 `phase6_results.json` 结构化结果交叉验证。]
- McKusick M K, Bostic K, Karels M J, Quarterman J S 1996"The Design and Implementation of the 4.4BSD Operating System" (Addison-Wesley, ISBN 0-201-54979-4)；Salus 1994；Bach 1986；freebsd.duckdb：freebsd-src commit `5b81b6b301437eb9a6df491c829475bd29ae5d6c`（1993-06-12）与 `26f9a76710a312a951848542b9ca1f44100450e2`（1994-05-25）；研究底稿 `research-unix-security-1969-1979.md`、`pwb-commercial-unix-security.md`、`4xbsd-security-1980-1991.md` ［A］
- Salus 1994；Kernighan 2019；McKusick et al. 1996；Spinellis 2006"A Repository for Unix History" ［B］
- IEEE Std 1003.1-1988；Zlotnick 1991"The POSIX.1 Standard"；COSE 1993 Common Open Software Environment 公告；POSIX FAQ Version 1.18（Andrew Josey 维护，opengroup.org/austin/papers/posix_faq.html，2025-05-25 更新）；Austin Group 主页（opengroup.org/austin/）；unix.org/version2/pr.html（SUSv2 公告新闻稿，1997-03-12）；unix.org/version3/pr.html（SUSv3 公告新闻稿，2002-01-30）；McKusick, M. K. (1999) "Twenty Years of Berkeley Unix"（O'Reilly Open Sources）［A］
- Miller 1990；Cutler & Nash"Windows NT" (1993)；McKusick et al. 1996 ［B］
- McKusick, 1999; "USL v. BSDi Settlement Agreement," 1994（Groklaw 存档）；Lawrence Rosen, "Open Source Licensing: Software Freedom and Intellectual Property Law," Prentice-Hall, 2004（对 BSDL 的法律分析） ［A］
- Spinellis 2006；Levenez UNIX History；学术批判性研究 [考据脚注：经相关权威来源交叉验证。]
- USENIX 邮件列表（minnie.tuhs.org）；口述史方法论文献 ［A］
- USL v. BSDi 1992；BSD 许可证文本；McKusick et al. 1996 第 1 章 ［B］

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP362、BSD Now EP351（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取。EP351 的 chown 语义考据与 2.11BSD 磁带谱系叙述与本章谱系主题相关，予以保留 -->

**要点**：

- Warner Losh 自述 2.11BSD 复原工程：因原始磁带由 Usenix 分发且早期母带重制，现仅存 patch level 195（约发布 18 个月后），他通过 2.10.1BSD、4.3BSD 等来源拼合出 patch level 0。（BSD Now EP362，[774.42-1103.02]，L1）
- 2.11BSD 的 patch 以 shell 脚本、uuencode 压缩 tar 等格式发布，部分指令破坏信息，无法简单用 patch -R 逆向。（BSD Now EP362，[884.78-912.34]，L1）
- Warner 自述曾因疫情失眠而以复原工程为消遣，最终重建出可启动的原始系统磁带，并计划把每个 patch 转为 git commit。（BSD Now EP362，[964.58-1472.50]，L1）
- 关于 sync：早期 Unix 没有 reboot 命令，靠 sync 后断电；连续三次 sync 是人为延时的误传，各 BSD 内核的 sync 只调度写盘而不等待完成。（BSD Now EP362，[2597.68-2885.24]，L1）
- OpenBSD 6.7 于 2020 年 5 月 19 日如期发布，延续其固定发布周期；本期逐项梳理 FFS2 默认、软 RAID 加密、PowerPC 默认编译器切换等改动。（BSD Now EP351，[426.2-433.64]，L2）
- 安全方面，OpenBSD 6.7 将 unveil 用于 82 个用户态程序，把 dig、host、nslookup 从 BIND 源码中剥离并以 pledge 收紧，体现 6.x 安全机制的持续扩散。（BSD Now EP351，[729.32-749.88]，L2）
- Chris Siebenmann 的文章考据 chown 语义的 Unix 分野：V7 与 4.2BSD 限制普通用户转让文件所有权，System III/System V 放开，POSIX 允许两种行为并存，现代系统多采 BSD 一侧。（BSD Now EP351，[1344.98-1550.98]，L2）

**史料**：

- Warner Losh 本人口述及博客、Twitter 记录，涉及 Usenix 磁带分发、TUHS 档案与 patch 链。（BSD Now EP362，[774.42-1826.06]，L1）
- Unix Heritage Society（TUHS）由 William Toomey 创立，保存代码、二进制、论文扫描件与早期商业发行的私有档案。（BSD Now EP362，[2022.96-2260.64]，L1）
- OpenBSD 6.7 变更日志与发布公告，含 FFS2、softraid 加密、PowerPC Clang、SMP 与硬件驱动改进。（BSD Now EP351，[476.52-480.64]，L2）
- V7 与 4.2BSD 的 chown 手册页及源码，以及 POSIX chown 规范的 rationale 章节（节目引述）。（BSD Now EP351，[1373.9-1542.98]，L2）
- LibreSSL 3.1.1 与 OpenSSH 8.3 随 6.7 更新，OpenSSH 移除 SHA-1 证书签名算法支持。（BSD Now EP351，[816.68-855.76]，L2）

**史观**：

- 总纲第 19 条——解释学循环是历史认识的根本条件：复原工程通过现存 patch 链与早期二进制格式博客互相印证，构成解释学循环的认识过程。（BSD Now EP362，[1076.58-1268.54]，L2）
- 总纲第 22 条——知识注定过时：早期二进制格式与工具链需借助旧模拟器与二进制工件才能重建，说明工具知识会随代际过时。（BSD Now EP362，[678.42-758.62]，L1）
- 总纲第 13 条——法律与道德是利益分配：chown 与配额语义的分野最终服务于磁盘空间这一稀缺资源的分配与控制，POSIX 以允许差异化的方式调和各方。（BSD Now EP351，[1505.46-1542.98]，L2）
- 总纲第 4 条——分离聚合是永恒规律：BSD 与 System V 从共同 V7 祖先分离出相反的 chown 语义，再由 POSIX 规范聚合为可共存的行为。（BSD Now EP351，[1344.98-1550.98]，L2）

**辨析**：

- 2BSD 系列早期版本号（2.8 至 2.11）与缺失版本（如 2.6/2.7）的编号逻辑，Warner 亦无法确证，仅推测与磁带编号相关。[存疑脚注] 版本号缺口原因待原始档案确认（BSD Now EP362，[802.42-826.70]，L4）
- 转写对‘软件 RAID 加密卷’等术语有拼写漂移（如‘software aid crypto volumes’），引用时须回查 OpenBSD 6.7 官方变更日志。[存疑脚注] 转写术语拼写漂移（BSD Now EP351，[514.16-524.0]，L4）

**文献**：

- [BSD Now EP362] Pennington J. BSD Now: 362: 2.11-BSD restoration[EB/OL]. (2020-08-06)[2026-08-15]. <https://www.bsdnow.tv/362>.
- [BSD Now EP351] Pennington J. BSD Now: 351: Heaven: OpenBSD 6.7[EB/OL]. (2020-05-21)[2026-08-15]. <https://www.bsdnow.tv/351>.

<!-- /PODCAST_REVIEW -->