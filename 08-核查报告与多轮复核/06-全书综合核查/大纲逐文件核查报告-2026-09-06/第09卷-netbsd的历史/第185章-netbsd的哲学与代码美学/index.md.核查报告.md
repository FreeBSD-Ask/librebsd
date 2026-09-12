# 核查报告：第09卷-netbsd的历史/第185章-netbsd的哲学与代码美学/index.md

- 源文件：d:\librebsd\05-卷册大纲\第09卷-netbsd的历史\第185章-netbsd的哲学与代码美学\index.md
- 批次：C266；检查日期：2026-09-12；检查方式：逐文件完整阅读人工核查（辅以 netbsd.duckdb／freebsd.duckdb 只读实查：contributors 切片 netbsd-src 900／freebsd-src 2,647——辨析“490 人/3720 人”失准；PODCAST 四期判读）
- SUMMARY.md 收录：未收录——批次 JSON 无 summary_line（chapterfile）；SUMMARY 行 1560 收录的是同章概述.md（“第 185 章 NetBSD 的哲学与代码美学”），index.md 与概述.md 并存且仅概述在册（110/294/230/180/328 同族）
- A 占位符：通过
- B 内容完整性：发现 1 处（要点截断群）
- C 编号与标题：通过（frontmatter CH185 与 H1 一致）
- D 格式规范：通过
- E 学术规范：发现 1 处（贡献者统计口径与数值双失准）
- F SUMMARY 一致性：不一致（本文件未收录，见问题清单第 3 项）
- 机械旗标复核：无（flags 为空）
- 问题清单：
  1. P1 | 行 12、15 | 要点第 2 条“于 **2004 年 1 月 22 日** 获得美”截断（IRS 认可句中断）、要点第 5 条“evbarm 通用 port 与 pkgsr”截断 | 字节截断族 ×2 处：承重要点中断（第 2 条涉及 NetBSD Foundation 税务地位关键日期） | 依上下文回源补全（“获得美国联邦税务局 501(c)(3) 免税认定”）
  2. P2 | 行 29 | “NetBSD 提交量虽最大但贡献者仅 490 人（远少于 FreeBSD 的 3720 人）” | 统计口径与数值双失准：实测 contributors 表 netbsd-src 900 行、freebsd-src 2,647 行（全库口径 1,545/5,671；duckdb 只读实查）——490/3720 与两套口径均不符 | 按重跑 SQL 核正（写明 src 切片或全库口径）
  3. P2 | 全文 | 章级双文件并存：index.md 未收录于 SUMMARY，在册者为概述.md | 结构族（110/294/230/180/328 同族）：保留/合并/迁移须主理人裁断 | DEFERRED 登记（P2-9 结构项），不阻塞循环
  4. P3 | 行 25 | 史观字段仅一句（“自反性：NetBSD 的代码美学是对‘代码可读性’这一普遍假设的自反性检验”） | 史观字段单句过薄：与 PODCAST 段十条史观（9/3/10/22/4/8/5 全符）的厚度不匹配 | 按 346 章先例从子节与 PODCAST 汇总扩充
  5. P3 | 行 80/81/83 | PODCAST 史观“总纲9 经验优先：经验优先：”“总纲4 分离聚合是永恒规律：分离聚合是永恒规律：”“总纲10 动手者创造历史：动手者创造历史：” | 标签文本重复 ×3 处（230 index 行 88-93 同族复制残迹） | 删除重复前缀
  6. P3 | 行 13 | “#netBSD IRC 频道” | 专名大小写：频道名规范为 #netbsd | 改 #netbsd
- 结论：存在问题 6 项（P0 0、P1 1、P2 2、P3 3）

## 补充说明（正样本与复核留痕）

- **要点层文化史实核对通过**：“Of course it runs NetBSD”口号 ✓；Core Team 邀请制与 FreeBSD 2000 年直选制对照 ✓；NetBSD Foundation 特拉华州注册＋“主页与 Bylaws 均未直接给出成立日期”的诚实存疑标注 ✓（2004-01-22 IRS 认可日期句被截断前可辨）；itojun（日本）/Klaus Klein（德国）/Alistair Crooks（英国）国际贡献者列举真实 ✓；“英美中心主义叙事遮蔽”的批判视角与 194.1 反刻板印象纪律同源。
- **PODCAST 四期选题与章主题（哲学与代码美学）契合度为本章最完整组合**：EP8（Antti Kantee：anykernel vs rump kernel 概念区分、puffs 起源、数 MB/100ms 开销估计、“把发生在用户态的事留在用户态”）、EP361（Fakecracker 函数式微虚拟机、Losh 2.11BSD 复原与分区史）、EP232（Thomas Cort：Minix 微内核代价收益约一成到一成五性能损失、导入约 80 个 NetBSD 用户态工具、pkgsrc 共享）、EP368（复用块）——微内核 vs 宏内核教条之争被化为情境权衡（行 85 总纲 5 释读）正是“哲学”章应做的事。
- **转写辨析 ×7 为全会话最密集自查**：Antti Conte/auntie conty→Kantee、Ramp/ROM kernel→rump kernel、Todd McWilling 归属存疑、开销数字为估计值、微内核损失为口头估计、Minix 导入时点为回忆值——每项均给复核路径（原始音频/性能文献/Minix 版本库）。
- PODCAST 史观十条（总纲 9×2/3/10×3/22/4/8/5）条目名与权威表逐字全符（仅 3 处文本重复）。
- 文献段 4 条（BSD Now EP368/361/8＋BSDTalk EP232）著录规范、零冗余——与本卷 178.2/179.2 的堆叠段形成对照。
- 编码合规：UTF-8 无 BOM、LF；弯引号正确。
