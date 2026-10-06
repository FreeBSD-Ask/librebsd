---
chapter: 第 42 章
id: CH42
volume: 第02卷-伯克利的岁月
---

# 第 42 章 AT&T 同意令与诉讼的深远影响

## 要点

- 法律环境对操作系统生态的影响：USL v. BSDi 加速 BSD 完全自由化与 Linux 崛起、SCO v. IBM 诉讼迟滞 Linux 发展、Apple v. Microsoft 使 Microsoft Windows 主导 GUI 市场，三案显示法律环境对操作系统生态的长期影响
- 将 USL v. BSDi（1992-1994）与两起微软反垄断案对照，可见三案结局分化的多维因素——USL 案以和解收场（3 删 70 改 + 4.4BSD-Lite 发布 + 不起诉承诺，见本卷 40.3/42 章）、US v. Microsoft 以行为和解收场（放弃拆分）、EU v. Microsoft 以维持罚款收场（4.97 亿欧元），三案均未走向“被告被拆解”的最极端救济；关键差异在于案件性质与救济形式：USL 案属版权诉讼，以和解与代码清洁收场，微软两案属反垄断诉讼，分别以行为救济与维持罚款收场
- 微软反垄断诉讼谱系（US v. Microsoft 1998-2001、EU v. Microsoft 2004-2007、Caldera v. Microsoft 1996-2000、Novell v. Microsoft 2005-2012）与 USL v. BSDi（1992-1994）共同构成 1990-2010 年代操作系统/软件产业法律战的完整图景：微软案以“反垄断+捆绑”为核心，USL 案以“版权+商业秘密”为核心，Caldera 与 Novell 案以反垄断为核心
- **1985-1988 年** AT&T UNIX 源代码许可费从教育机构免费/200 美元飙升到商业高价（具体年份价格数字无一手来源确证，完整考据与存疑脚注见 42.4 节）
- 版权登记瑕疵的影响：使 USL 初步禁令被驳回、削弱 USL 版权主张、为 BSDi 与伯克利赢得诉讼时间、为 1994 年和解创造有利条件、显示版权登记形式要求对软件版权的重要性，1992-1994 年诉讼中版权瑕疵成为关键论点

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3864] 卷“第02卷-伯克利的岁月”第 42 章，匹配置信度 folder，原因：folder 第180章
- [DB:references_fulltext:chapter_matches:chmatch_3882] 卷“第02卷-伯克利的岁月”第 42 章，匹配置信度 folder，原因：folder 第180章
- [DB:references_fulltext:chapter_matches:chmatch_3915] 卷“第02卷-伯克利的岁月”第 42 章，匹配置信度 folder，原因：folder 第180章
- [DB:references_fulltext:chapter_matches:chmatch_3937] 卷“第02卷-伯克利的岁月”第 42 章，匹配置信度 folder，原因：folder 第180章

## 史观

- 第 5 条没有必然性只有偶然性——1956 年同意令、1978 年版权登记疏忽、1992-1994 年诉讼窗口与各案结局分化均系偶然事件，却塑造了 UNIX 分发、BSD 诞生与 BSD/Linux 长期竞争格局（42.4-42.6、42.10-42.12）
- 第 2 条历史是形式主义化的非存在——AT&T 的商业化形式逻辑（最大化许可费）与事后补登记的形式补救，难以逆转 1978-1992 年版权实质瑕疵，法律形式决定实体结局（42.4、42.5、42.7）
- 第 6 条和解优于斗争——USL v. BSDi（1994 年和解＋4.4BSD-Lite）、US v. Microsoft（行为和解）、Apple v. Microsoft（和解）均以妥协收场，SCO 系列坚持诉讼则走向破产与再诉被驳，软件业大型法律战极少走到终局判决（42.10-42.12）
- 第 10 条动手者创造历史——律师团队与被忽视的证人在 BSD 叙事中被边缘化，但其版权瑕疵抗辩与和解谈判对 BSD 路线命运至关重要，须主动恢复其历史可见性（42.8、42.9）

## 辨析

- 法律环境的 “决定性” 需核对，避免将法律因素等同于唯一因素，技术与市场因素亦重要
- 三案对照的史料基础须说明——微软两案均为反垄断（不是版权案），与 USL 案的“版权+商业秘密”性质不同，比较时须限定在“软件业大型法律战”层面，避免类比过度；EU v. Microsoft 的互操作披露救济在 2010 年代后被互操作标准与开源替代所部分消解，其历史意义更多在反垄断法教义层面 ［A］
- 对照须限定在“操作系统/UNIX 谱系软件法律战”层面——Caldera/Novell 案是反垄断（非版权），USL 案是版权（非反垄断），微软政府案是反垄断，法律性质各异；但五案共享的“软件业巨头+政府/竞争者+巨额和解”结构使其具备比较价值；另须说明 Caldera 案的 2.8 亿美元为估计值（WSJ 报道 2.75 亿、Groklaw 披露 2.8 亿），以 Groklaw 披露的和解协议
- 许可费飙升的 “具体数字” 需按 0 信任原则核对——区分 “教育折扣” 与 “商业价格”，避免将单一价格表等同于普遍价格；“200,000-400,000 美元” 区间无独立一手史料确认，1983 年商业约 $43k/CPU、1989-1990 年 SVR4 商业 \$100,000、McKusick 回忆 “约 $250,000”等数字各有来源但无法拼出“1985 年 200,000 美元起、1987 年 400,000 美元”的连续涨价序列，具体年份数字应作存疑处理
- 版权瑕疵影响的 “决定性” 需核对，诉讼结果是多重因素叠加，版权瑕疵是关键但非唯一因素

## 文献

- 1990-2010 年操作系统市场份额报告；DiBona, C. (1999) “Open Sources”；Moody, G. (2001) “Rebel Code”［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

---

## 文献增补与辩证校准（2026-08-08 追加）

> 41.4-41.5 AT&T 同意令与版权瑕疵：
>
> - **文献增补（ref 3778）**：McKusick 记载 1974 年 UNIX 以低价磁带进入伯克利——41.4 ‘AT&T 禁止销售软件使 UNIX 以极低成本分发’的直接依据
> - **文献增补（ref 3780）**：4.4BSD 设计书历史章（History and Goals）覆盖 AT&T→BSD 版权演变
> - **辩证校准（专题语，不设总纲条号）**：‘劣币驱逐良币’命题——AT&T 的法律约束（非技术优劣）塑造了 UNIX 分发史，本章分析应聚焦形式主义权力运作

<!-- DB_REF:linux_kernel.duckdb -->
> **数据库引用（linux_kernel.duckdb）**：本子节对应 linux_kernel 代码仓库。> 2003-2010 年间：230,969 次提交。> 仓库总览：1,474,341 次提交，39,865 位贡献者（contributors 表行数，1970-01-01 至 2026-08-24）。
- 本卷 40-42 章相关案卷；United States v. Microsoft Corp., 253 F.3d 34 (D.C. Cir. 2001)；Microsoft Corp. v. Commission, T-201/04 (2007)；European Commission IP/04/382（2004-03-24） ［A］<!-- NEWREF:2370 --><!-- NEWREF:2371 --><!-- NEWREF:2372 --><!-- NEWREF:2373 --><!-- NEWREF:2482 -->
- CALDERA v. Microsoft 案卷；NOVELL v. Microsoft 案卷；United States v. Microsoft Corp., 253 F.3d 34 (D.C. Cir. 2001)；European Commission IP/04/382；本卷 40-42 章案卷 ［A］<!-- NEWREF:2392 --><!-- NEWREF:2393 --><!-- NEWREF:2394 --><!-- NEWREF:2493 --><!-- NEWREF:2545 -->
- AT&T UNIX Software Operation (1990.3.28) 公开邮件列表（确认 SVR4 商业 $100,000）；McKusick, K. (1999) “Twenty Years of Berkeley Unix” 及 klarasystems 转引的 McKusick 1999 视频（回忆“约 \$250,000 ”）；Salus, P. (1994) “ A Quarter Century of UNIX ”；TUHS 邮件列表 1983 年 $43k/CPU 记录 ［A］
- USL v. BSDi 案卷；Novell-UC Berkeley 和解协议（1994）；McKusick, K. (1999) “Twenty Years of Berkeley Unix” ［B］
- Linux/BSD 市场份额报告（1992-2000）；Moody, G. (2001) “Rebel Code”；DiBona, C. (1999) “Open Sources”［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:linux_kernel.duckdb -->
> **数据库引用（linux_kernel.duckdb）**：本子节对应 linux_kernel 代码仓库。> 1978-1992 年间：0 次提交。> 仓库总览：1,474,341 次提交，39,865 位贡献者（contributors 表行数，1970-01-01 至 2026-08-24）。
- 和解协议全文（Groklaw 存档）; 4.4BSD-Lite 发行说明 ［A］
- BSD 社区邮件列表存档；1994-2000 年媒体报道集；伯克利校方法律顾问访谈 ［A］
- USL v. BSDi 案卷；伯克利校方法律顾问档案；McKusick, K. (1999) “Twenty Years of Berkeley Unix” ［B］

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：YouTube EPrXmWXIDsxig、YouTube EP3u8zKO8VTD0（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 两位 AI 主持开场即交代信源：依据用户提交的 FreeBSD Handbook 章节与维基条目生成对谈；其核心定性是 FreeBSD 为内核、驱动、工具与文档一体发布的完整系统，好比“到手即调校好的整车”，而其稳定性口碑被归因于数十年实战检验，以此回答“为何历史对今天的用户仍然重要”。（YouTube EPrXmWXIDsxig，[0.0-134.5]，L2）　[订正：2026-10-06 依 senseaudio 新转写（任务书3 tb2 战役）重锚 [4.64-131.8]→[0.0-134.5]，开场信源/完整系统定性段重锚，内容核符；模型 senseaudio-asr-stream-1.5-260910]
- 对功能面的转述全然承袭手册与维基的措辞：ZFS 被称作手册口中的革命性文件系统，快照被喻为数据的时间机器、逐层校验防止静默损坏；GEOM 是模块化存储框架，如积木般组合出 RAID 冗余、磁盘加密与网络后端存储；jails 被强调早于 Docker、更轻量且与操作系统耦合更紧；TrustedBSD 把强制访问控制做进系统核心以限制攻击者破坏半径；DTrace 则被喻为操作系统的 X 光透视。（YouTube EPrXmWXIDsxig，[303.3-567.3]，L2）　[订正：2026-10-06 依 senseaudio 新转写（任务书3 tb2 战役）重锚 [310.68-567.279]→[303.3-567.3]，功能面转述段重锚（ZFS/GEOM/jails/TrustedBSD/DTrace），内容核符；新转写 "GOM" 系 GEOM 之音写，条目按正确名保留；模型 senseaudio-asr-stream-1.5-260910]
- 对历史的转述集中于两处：其一，维基条目提及 Netflix 与 WhatsApp 等大规模服务依赖 FreeBSD，被引为网络能力“传奇”的佐证；其二，1990 年代 AT&T 就 Unix 代码提起的诉讼被表述为关键转折——一场法律之战“迫使 FreeBSD 重新发明自身”，重写大半代码库，并反过来巩固了其对开源原则的承诺，两位主持将其总结为韧性的故事。（YouTube EPrXmWXIDsxig，[164.5-237.9]，L2）[订正：原 [196.44-236.599] → [184.8-240.8]，内容复核]　[订正：2026-10-06 依 senseaudio 新转写（任务书3 tb2 战役）重锚 [184.8-240.8]→[164.5-237.9]，历史转述段重锚（Netflix/WhatsApp+USL 诉讼），内容核符；模型 senseaudio-asr-stream-1.5-260910]
- 该解说把 BSD 概括为伯克利学生对 AT&T Unix 的修改与增强包，最初并非独立操作系统，后成长为独立分支；其最重要的历史贡献是网络：在 1970 年代末与 1980 年代初实现 TCP/IP 协议栈，代码清洁、可靠且开放供研究者研究，互联网扩展出研究实验室后 BSD 网络代码无处不在，早期商业 Unix 与 Windows 网络实现亦大量借鉴，由此获得“构建互联网的 Unix 系统”之称号。（YouTube EP3u8zKO8VTD0，[93.4-192.96]，L2）[订正：原 [120.32-192.96] → [93.4-192.96]，内容复核]
- 1980 年代末 AT&T 开始对 Unix 主张知识产权，与加州大学陷入漫长复杂的法律纠纷；法律不确定性恰在 Linux 诞生之际拖慢了 BSD 的采用，Linux 因未直接衍生自 AT&T 代码而避开此问题，最终 BSD 以重写清除残余 AT&T 代码、纠纷了结，但 Linux 已积聚势头，BSD 生态遂分裂为各有目标、哲学与强项的数个重要分支。（YouTube EP3u8zKO8VTD0，[202.96-254.7]，L2）[订正：原 [202.96-240.16] → [202.96-254.7]，内容复核]
- 三分支定位在解说中被总结为：FreeBSD 以性能、可扩展与整体性设计见长，内核与用户态一体开发，被 Netflix Open Connect 内容分发网络、Juniper、NetApp 等采用，并较早引入 ZFS；OpenBSD 以“默认安全”为纲，坚持代码审计与正确性优先，孕育 OpenSSH、PF、LibreSSL 等安全工具；NetBSD 以极致可移植性立身，代码库刻意分离机器无关与机器相关组件，故常最先支持冷门硬件。（YouTube EP3u8zKO8VTD0，[252.7-554.48]，L2）[订正：原 [240.16-554.48] → [252.7-554.48]，内容复核]
- 在许可证哲学上，解说指出 BSD 宽松许可证允许商业专有产品在极少限制下使用与再分发，促成广泛采纳但不保证企业回馈改进；GPL 的 copyleft 模型则催生大规模共享开发生态。BSD 生态因而更小、更保守、更受核心开发者掌控，价值观上重视稳定性、清晰性与长期设计，与 Linux 的快速迭代形成对照。（YouTube EP3u8zKO8VTD0，[605.44-760.4]，L2）

**史料**：

- 本期不含任何一手当事人陈述：全部内容为对 FreeBSD Handbook 章节与维基条目的转述，所涉社区论（人人可贡献文档、测试与论坛答疑）与 FreeBSD Foundation 职能（基础设施与资源、开发与差旅资助）亦同属二手复述；其价值仅在于记录 FreeBSD 官方叙事在 AI 生成媒体中的再生产形态。（YouTube EPrXmWXIDsxig，[238.1-303.1]，L2）[订正：原 [645.279-659.0] → [629.3-659.0]，内容复核]　[订正：2026-10-06 依 senseaudio 新转写（任务书3 tb2 战役）重锚 [629.3-659.0]→[238.1-303.1]，社区论/Foundation 转述段重锚，内容核符；模型 senseaudio-asr-stream-1.5-260910]

**史观**：

- 总纲23 一切历史写作都是基于哲学设定的历史小说：解说以“安静的坚持是其力量的一部分”“重视工艺而非炒作”为 BSD 写传，把三个分支塑造成不追逐潮流、沉默守护互联网的人格化角色，这类叙事本身即是一种带价值预设的历史建构，将技术格局的分化转写为品味与德性的对比，读者应将其视为叙事而非中立事实。（YouTube EP3u8zKO8VTD0，[757.76-790.48]，L2）

**辨析**：

- AI 转述的诉讼叙事存在明显压缩与失真：USL 诉讼的被告是 BSDi 与加州大学伯克利方面，FreeBSD 项目本身并非被告；“重写大半代码库”混合了诉讼前 CSRG 清除 AT&T 代码的 Net/2 工程、和解后改以 4.4BSD-Lite 为基底两条不同线索，被压平为“从零重写”的韧性故事。本期可作 AI 生成媒体（自称 Deep Dive，形态与 NotebookLM 一类文档对谈工具一致）再生产 BSD 史的当代标本，但其任何历史断言不得直接引用，引用前必须回查 Handbook 原文与一手文献。[存疑脚注] 全部历史表述均为二手转述的再转述，且存在事实压缩。　[存疑脚注] 本期诉讼叙事与功能描述均系 AI 对手册与维基的转述再转述，未经任何一手来源核验，仅具媒体接受史标本价值。（YouTube EPrXmWXIDsxig，[213.6-237.9]，L4）[订正：原 [204.799-226.519] → [204.799-240.8]，内容复核]　[订正：2026-10-06 依 senseaudio 新转写（任务书3 tb2 战役）重锚 [204.799-240.8]→[213.6-237.9]，存疑脚注（诉讼叙事失真）重锚，内容核符；模型 senseaudio-asr-stream-1.5-260910]
- 解说称早期 Windows 网络栈“借鉴了 BSD 的思想与代码”，又称 Linux 是受 Unix 启发的净室重实现，两者均为流传甚广的流行说法；前者与 Windows TCP/IP 栈实际授权移植来源的考据结论需核对，后者的“净室”定性亦系标签化表述，均不可直接采信。　[存疑脚注] Windows TCP/IP 栈来源与 Linux 净室定性均须回到一手文献核验；另该期转写为双轨时间戳交错的解说词，无出镜当事人，全部陈述仅可作研究线索。（YouTube EP3u8zKO8VTD0，[222.64-233.12]、[578.6-588.3]，L4）[订正：原 [222.64-233.12] → [222.64-233.12]、[578.6-588.3]，内容复核]

**文献**：

- [YouTube EPrXmWXIDsxig] YouTube. YouTube: 🔍 The Untold History of FreeBSD: From Berkeley to the Modern Internet’s Backbone 🔍[EB/OL]. ()[2026-08-15]. <https://www.youtube.com/watch?v=rXmWXIDsxig>.
- [YouTube EP3u8zKO8VTD0] YouTube. YouTube: BSD Explained: How FreeBSD, OpenBSD & NetBSD Built the Internet[EB/OL]. ()[2026-08-15]. <https://www.youtube.com/watch?v=3u8zKO8VTD0>.

<!-- /PODCAST_REVIEW -->

<!-- dangan-20260908 消解回写 -->
- Dees. M. A stale Unix case haunts IBM: Xinuos demands a new hearing[N/OL]. Techzine, 2026-08-24. <https://www.techzine.eu/news/privacy-compliance/143772/a-stale-unix-case-haunts-ibm-xinuos-demands-a-new-hearing/> [2026-08-25]. ［DKC-1298→fulltext:5858］
<!-- /dangan-20260908 -->
