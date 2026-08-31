---
chapter: 第 349 章
id: CH349
volume: 18
---

# 第349章 商业unix与开源运动人物传记

## 要点

- （待从数据库提取）
- （待从数据库提取）
- （待从数据库提取）

## 史观

- 动手者创造历史：记录默默做事的人，而非只写站在台前的大佬
  - 辨析：（待从数据库考据记录提取）
  - 文献：[DB:historical_claims] 历史主张数据库（853 条主张，26,898 条证据）

## 辨析

- （待从数据库考据记录提取）
  - 文献：[DB:historical_claims] 历史主张数据库（853 条主张，26,898 条证据）

## 文献

- 见 22.8。
- - Schwartz J. Sun Microsystems blog archive [EB/OL]. Mountain View: Sun Microsystems, 2006-2010.
    - OpenSolaris Project. OpenSolaris history and governance [EB/OL]. 2005-2010.

11. **个人生活（2026-08-08 考据增补）**：政治观点——无公开党籍记录；公开立场偏“技术即社会公用事业”；在国会倡导保护个人隐私/言论自由/知识产权权利；2005 认为 GPL 被用作“美国企业掠夺发展中国家知识产权的工具”；

- - Oracle Corporation. Oracle database history and annual reports [EB/OL]. Redwood City: Oracle, 1979-2026.
    - Symonds M. Softwar: an intimate portrait of Larry Ellison and Oracle [M]. New York: Simon & Schuster, 2003.

11. **个人生活（2026-08-08 考据增补）**：政治观点——自称‘中间派’；长期两党通捐（1991 以来逾 1000 万美元）；共和党受助者：Li

- - Stallman R M. The GNU manifesto [EB/OL]. Cambridge: Free Software Foundation, 1985.
    - Stallman R M. Free software, free society: selected essays [M]. Boston: GNU Press, 2002.
    - Free Software Foundation. GNU project history [EB/OL]. Boston: FSF, 1983-2026.

11. **个人生活（2026-08-08 考据增补）**：政治观点

- - Torvalds L. Just for fun: the story of an accidental revolutionary [M]. New York: HarperCollins, 2001.
    - Linux Kernel Organization. Linux kernel source repository and mailing lists [EB/OL]. 1991-2026.

11. **个人生活（2026-08-08 考据增补）**：政治观点——自称“从不热衷政治”；2010 入籍美国并登记投票，未加入任何政党（“我有太多个人自尊，不愿与任何一个政党扯上关系

- - Young R. Under the radar: how Red Hat changed the software business and took Microsoft by surprise [M]. Scotts Valley: Coriolis, 1999.
    - Red Hat. Annual reports 1999-2025 [R]. Raleigh: Red Hat, 1999-2025.
- [DB:historical_claims] 历史主张数据库（853 条主张，26,898 条证据）
- - FreeBSD Project. FreeBSD core team elections 2022, 2024 [EB/OL]. Santa Clara: FreeBSD Project.
    - FreeBSD Foundation. Annual report 2025 [R]. Boulder: FreeBSD Foundation, 2025.

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP149（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Michael Dexter 回顾 bhyve 的 GSoC Vagrant 支持、UEFI GOP 与磁盘镜像格式，认为虚拟化最终归结为块设备、内存与少量网络配置，hypervisor 本身的复杂度极高，能维护者稀少。（BSD Now EP149，[3615.00-3745.00]，L1）
- Dexter 介绍 diskctl 构想：以机器可读输出替代 smartctl 难以解析的输出，由长期从事磁盘恢复的 Rod Grimes 提供 ATA 底层知识，目标是将该工具纳入 FreeBSD base。（BSD Now EP149，[3782.00-4225.00]，L1）
- Dexter 认为 ZFS 的关键优点是可移植性：其设计使字节序无关，能跨 x86 与 SPARC；他同时指出空间映射重建与更宽松的 zpool import 只读恢复是值得期待的改进方向。（BSD Now EP149，[4443.00-4662.00]，L1）
- FreeBSD Foundation 2016 年 6 月更新披露，Peter Holm 十多年内核压力测试发现约 1400 个问题，Konstantin Belousov 已调查 910 个，并谈及 VM 对象的 copy-on-write 缺陷与修复。（BSD Now EP149，[6530.00-6643.00]，L2）
- Roger Faulkner 去世，主持人转述其作为 Solaris 人物在 /proc 与线程模型方面的贡献，以及 Hacker News 上关于其辅导后辈的追忆。（BSD Now EP149，[7091.00-7190.00]，L2）

**史料**：

- Michael Dexter 提交 AsiaBSDCon 与 BSDCan 的 diskctl/SMART 论文，作为工具构想的原始方案。（BSD Now EP149，[3962.00-3974.00]，L1）
- FreeBSD Foundation June 2016 update 的发布内容，含 Peter Holm 压力测试数据与 BSDCan 募捐记录。（BSD Now EP149，[6477.00-6761.00]，L2）
- POSIX 标准邮件列表上的 Roger Faulkner 讣告，记录其 20 世纪 70 年代至 2000 年代的工作脉络。（BSD Now EP149，[7183.00-7190.00]，L2）

**史观**：

- 总纲10 动手者创造历史：Rod Grimes 长期做底层磁盘恢复，其不可替代的经验构成 diskctl 的实质知识来源，是动手者知识沉淀推动工具的典型。（BSD Now EP149，[3985.00-4024.00]，L1）
- 总纲9 经验优先：Dexter 从 FreeNAS 支持中观察用户真实误用与数据丢失模式，把一线经验反哺到工具设计，体现经验优先于抽象设计。（BSD Now EP149，[4349.00-4412.00]，L1）
- 总纲4 分离聚合是永恒规律：Dexter 对 fork 与社区的讨论表明商业 fork 若脱离上游会失去 SMP、64 位与新硬件支持，分离之后仍需重新聚合到社区主线，呈现分离聚合的循环。（BSD Now EP149，[5711.00-5796.00]，L1）

**辨析**：

- smartctl 输出难解析且 GPL 许可无法进入 base，是催生 BSD 许可磁盘工具的动因，但该构想仍处志愿者业余阶段，尚无公司投入，能否落地存疑。　[存疑脚注] 项目仍为“蓝天空闲”的志愿者努力，未有公司承诺资源（BSD Now EP149，[3895.00-4225.00]，L1）
- Dexter 指出 ZFS 对损坏数据“过于严格”，用户无法取回剩余数据，恢复工具生态不足；这与 ZFS 不常失效的特点形成张力，是否值得建立官方恢复工具存在分歧。（BSD Now EP149，[4707.00-4774.00]，L1）

**文献**：

- [BSD Now EP149] Pennington J. BSD Now: 149: The bhyve has been disturbed, and a wild Dexter appears![EB/OL]. (2016-07-06)[2026-08-15]. https://www.bsdnow.tv/149.

<!-- /PODCAST_REVIEW -->
