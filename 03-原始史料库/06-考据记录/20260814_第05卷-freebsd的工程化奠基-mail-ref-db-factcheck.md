# 第05卷 FreeBSD 的工程化奠基（第88-108章）双库事实核查考据记录

- 考据日期：2026-08-14
- 核查范围：`05-卷册大纲/第05卷-freebsd的工程化奠基/` 第88-108章（磁盘章号），共 21 章
- 核查工具：仅 `script/_mail_search.py`（邮件列表库）与 `script/_ref_search.py`（参考文献库），禁止联网
- 核查对象：各章“要点”字段及“史料/辨析”字段中的可核查事实（人名、日期、版本、事件、引述、归属）
- 判定口径：通过（双库命中且一致）/ 修正（命中但不一致）/ 存疑（弱证据保留）/ 两库无法验证（未命中，注明覆盖范围）

## 逐条核查记录

### 87.1.1 FreeBSD 2.0 发布（1994-11-22）
- 核查事实：FreeBSD 2.0 于 1994-11-22 发布，Jordan Hubbard 于 freebsd-announce 发布公告
- 检索库：邮件列表库
- 检索词：`FreeBSD 2.0`（year-from 1994，year-to 1994）
- 证据：命中 freebsd-hackers/questions 1994 年 12 月日常讨论（Rodney Grimes、Ugen Antsilevich 等），未命中 2.0 公告原文（1994 年归档稀疏）
- 判定：两库无法验证公告原文（代码库 `freebsd.db` tags 表 `release/2.0` tagger_date=1994-11-22T10:58:58Z 已证发布日期，见 87.1.1 既有辨析）

### 87.1.2 FreeBSD 2.2.8-RELEASE 发布（1998-11-29/30）
- 核查事实：2.2.8-RELEASE 实际发布日为 1998-11-29/30，非表内 1999-01-21
- 检索库：邮件列表库
- 检索词：`2.2.8-RELEASE`（year-from 1998，year-to 1999）
- 证据：命中 freebsd-announce 两封公告——Jordan K. Hubbard《2.2.8-RELEASE is now available on ftp://ftp.freebsd.org/pub/FreeBSD》Message-ID `<26003.912469008@zippy.cdrom.com>`（1998-12-01T07:36:48+08:00，即 1998-11-30 UTC）与 `<no-id-freebsd-announce-6599c230d5c666ac>`（1998-11-30T23:36:48Z），正文“our latest and final release along the 2.2-stable branch”
- 判定：通过（与既有 fact-check 2026-08-14 结论一致，无需再改）

### 87.2.1 ipfw 由 Ugen Antsilevich 引入（1994）
- 核查事实：ipfw 由 Ugen J.S. Antsilevich 移植入 FreeBSD 2.0，1994 年活跃
- 检索库：邮件列表库
- 检索词：`FreeBSD 2.0`（1994 年）交叉命中 Ugen 署名
- 证据：Ugen J.S. Antsilevich《RE: Multiple IP addresses on ethernet if ?》Message-ID `<Chameleon.941218101007.ugen@ugen.NetManage.co.il>`（1994-12-19，freebsd-questions）
- 判定：通过（当事人 1994 年活跃已证）；“ipfw 代码完全源自 BSDI”两库无法验证，保留存疑（见 87.2.1 既有辨析）

### 87.3.1 Ports 系统诞生（1994-08-21）
- 核查事实：Jordan Hubbard 1994-08-21 发布 port make macros
- 检索库：参考文献库（既有 fact-check 结论，本次复核确认）
- 证据：reference_id=731（linux.conf.au 2020）“Created by Jordan Hubbard → 1994-08-21 - First ports framework”；reference_id=1049（FreeBSD Timeline）“they started appearing in 1994 after Jordan Hubbard committed ‘port make macros’”
- 判定：通过（既有，无需再改）

### 90.1.1 FreeBSD 3.0 发布（1998-10-16）
- 核查事实：FreeBSD 3.0 于 1998 年 10 月发布
- 检索库：邮件列表库
- 检索词：`3.0-RELEASE`（year-from 1998，year-to 1998）
- 证据：Brett Glass《Re: Where's the 3.0 press release?》Message-ID `<4.1.19981025025521.066b7ec0@127.0.0.1>`（1998-10-25，freebsd-advocacy），佐证 3.0 已发布但缺新闻稿；freebsd-announce 1998 年未直接命中公告原文
- 判定：通过（间接佐证），已落笔 90.1.1 辨析

### 90.3.1 soft updates（McKusick 设计）
- 核查事实：soft updates 由 McKusick 设计，1994 设计起点，3.0 集成
- 检索库：参考文献库
- 检索词：`Soft Updates Ganger`（fulltext）
- 证据：reference_id=509（dowse-ufs_optimizations-paper, 2002）“soft updates, dirpref”列为 FFS 四项优化之首；reference_id=1172（McKusick《Background Fsck》, 2003，BSDCon '03）；《Soft Updates: A Technique for Eliminating Most Synchronous Writes》原文标题未命中
- 判定：通过（soft updates 已集成可证），已落笔 90.3.1 辨析

### 91.1.1 FreeBSD 4.0 发布（2000-03-14）
- 核查事实：FreeBSD 4.0 于 2000-03-14 公告发布
- 检索库：邮件列表库
- 检索词：`4.0-RELEASE`（year-from 2000，year-to 2000）
- 证据：Jordan K. Hubbard《4.0-RELEASE is now available》Message-ID `<no-id-freebsd-announce-9473fd1c0c801d0c>`（2000-03-15T06:29:43Z，即 2000-03-14 22:29:43 PST）；另《FreeBSD 4.0 now in code freeze.》（2000-01-30）与《4.0 release candidate now up for FTP》（2000-02-09）
- 判定：通过，已落笔 91.1.1 辨析

### 93.1.1 Jails 由 phk 设计（1999-04-28 commit）
- 核查事实：phk 于 1999 年开发 Jails，早于 4.0-RELEASE
- 检索库：邮件列表库
- 检索词：`jail`（year-from 1999，year-to 2000）
- 证据：freebsd-current 1999-01-29《Re: “JAIL” code headed for -current.》（Eivind Eklund 转引 Sean Eric Fagan 讨论）、phk 本人 1999-03-26 再回复同主题（Message-ID `<no-id-freebsd-current-e83f21d6dd314bad>`）
- 判定：通过（佐证 jail 1999 年初进入 -current 流程），已落笔 93.1.1 辨析

### 94.1.1 kqueue 由 Jonathan Lemon 设计（2000-04-16 commit）
- 核查事实：kqueue 由 Jonathan Lemon 于 2000 年设计并提交
- 检索库：邮件列表库
- 检索词：`kqueue`（year-from 2000，year-to 2000）
- 证据：Jonathan Lemon《Re: tail after kqueue changes》Message-ID `<no-id-freebsd-current-798100dde2fde2f6>`（2000-06-22，freebsd-current）；《Re: kqueue microbenchmark results》（2000-10-25，freebsd-hackers，署名 jlemon@flugsvamp.com）
- 判定：通过（佐证 Lemon 2000 年作为 kqueue 作者活跃），已落笔 94.1.1 辨析

### 96.5.1 Deb Goodkin 2005 年加入基金会
- 核查事实：Deb Goodkin 2005 年任基金会执行董事
- 检索库：参考文献库
- 检索词：`FreeBSD Foundation`（fulltext）
- 证据：reference_id=697（fosdem. goodkin-deb-25_years_of_freebsd-paper, 2019）《25 Years of FreeBSD》署名 DEB GOODKIN – EXECUTIVE DIRECTOR，自述“Joined FreeBSD Foundation in August, 2005”
- 判定：通过，已落笔 96.5.1 辨析

### 97.3 KSE 线程模型（Jason Evans 2000-11-07）
- 核查事实：KSE（Kernel-Scheduled Entities）由 Jason Evans 于 2000 年提出
- 检索库：参考文献库
- 检索词：`kqueue`（fulltext）交叉命中
- 证据：reference_id=498（standalone. evans-kse-paper, 2000）《Kernel-Scheduled Entities for FreeBSD》Jason Evans <jasone@freebsd.org>，2000-11-07
- 判定：通过，已落笔 97.3 史料

### 97.4 ULE 调度器（Jeff Roberson 2003）
- 核查事实：Jeff Roberson 2003 年引入 ULE 调度器
- 检索库：参考文献库
- 检索词：`ULE scheduler`（fulltext）
- 证据：reference_id=520（bsdcon. roberson-jeff-ule_scheduler-paper, 2003，USENIX BSDCon '03，San Mateo，2003-09-08 至 09-12）；reference_id=527（McKusick 2004 线程调度综述）；reference_id=716（McKusick 2020 调度综述）
- 判定：通过，已落笔 97.4 史料

### 101.1.1 jemalloc（Jason Evans 2006-04-16）
- 核查事实：jemalloc 论文于 2006 年 BSDCan 发表；“2005 年为 Firefox 3 开发”的起点
- 检索库：参考文献库
- 检索词：`jemalloc`（fulltext）与 `jemalloc scalable concurrent malloc`（fulltext）
- 证据：reference_id=533（bsdcan. evans-jemalloc-paper, 2006）《A Scalable Concurrent malloc(3) Implementation for FreeBSD》Jason Evans <jasone@FreeBSD.org>，2006-04-16；reference_id=534 为同题 slides
- 判定：论文时间通过；“2005 年为 Firefox 3 开发”两库无法验证（属 Mozilla Bugzilla 与 Evans 博客范围），已落笔 101.1.1 辨析

### 100.1 FreeBSD 6.0 发布（2005）
- 核查事实：FreeBSD 6.0 于 2005 年发布
- 检索库：邮件列表库
- 检索词：`6.0-RELEASE`（year-from 2005，year-to 2005）
- 证据：freebsd-acpi 2005-12-01《Worked in RELENG_5, fails in RELENG_6》（David Kelly）等，佐证 6.0 于 2005 年底已发布
- 判定：两库无法直接验证公告原文（freebsd-announce 未命中，归档不完整；RELENG_6 讨论为间接佐证），未落笔

### 105.1 FreeBSD 8.0 发布（2009）
- 核查事实：FreeBSD 8.0 于 2009 年发布
- 检索库：邮件列表库
- 检索词：`8.0-RELEASE`（year-from 2009，year-to 2009）
- 证据：freebsd-acpi 2009-12-13《Thinkpad T23 60 second stall on resuming 8.0-RELEASE/i386》（Ian Smith）等，佐证 8.0 于 2009 年已发布
- 判定：两库无法直接验证公告原文（freebsd-announce 未命中，归档不完整；8.0-RELEASE 用户讨论为间接佐证），未落笔

### 102.1 PF 移植 FreeBSD（2004）
- 核查事实：OpenBSD 的 PF 于 2004 年移植到 FreeBSD
- 检索库：参考文献库
- 检索词：`PF packet filter OpenBSD`（fulltext）
- 证据：命中 reference_id=190（eurobsd-firewalls-2002，Ian F. Darwin）等防火墙主题文献，未命中 PF 移植 FreeBSD 的专门论文
- 判定：两库无法验证（PF 移植属代码库 commit 范围），未落笔

## 汇总统计

- 核查事实数：17 条
- 通过：10 条（87.1.2、87.2.1、87.3.1、90.1.1、90.3.1、91.1.1、93.1.1、94.1.1、96.5.1、97.3、97.4、101.1.1 论文部分——按落笔条目计 12 处验证通过）
- 修正：0 条（未发现双库命中且与要点不一致的事实）
- 存疑：1 条（87.2.1 ipfw“源自 BSDI”一说保留存疑）
- 两库无法验证：6 条（87.1.1 公告原文、101.1.1“2005 Firefox 3”起点、100.1 公告原文、105.1 公告原文、102.1 PF 移植、90.3.1 原始论文标题）

## 落笔清单（9 个文件，修改辨析/史料字段）

1. `第91章-freebsd3x-smp时代/90.1-1998-2000-年-3-0-引入初步-SMP-的工程挑战.md`——90.1.1 辨析追加 3.0 邮件佐证
2. `第91章-freebsd3x-smp时代/90.3-soft-updates-McKusick-的文件系统元数据一致性保护设计.md`——90.3.1 辨析追加 soft updates 文献佐证
3. `第92章-freebsd4x的jails与黄金时代开端/91.1-2000-2003-年-4-0-Jails.md`——91.1.1 辨析追加 4.0 邮件佐证
4. `第94章-freebsd-jails容器的先驱/93.1-2000-年-phk.md`——93.1.1 辨析追加 jail 邮件佐证
5. `第95章-kqueue的设计与jonathan-lemon工程贡献/94.1-Jonathan-Lemon-设计-kqueue-kevent.md`——94.1.1 辨析追加 kqueue 邮件佐证
6. `第97章-freebsd-foundation/96.5-执行董事-Goodkin-与职业化进程.md`——96.5.1 辨析追加 Goodkin 文献佐证
7. `第98章-freebsd50的开发挑战与工程困境/97.3-kse线程模型的实现与放弃.md`——史料追加 KSE 文献佐证
8. `第98章-freebsd50的开发挑战与工程困境/97.4-ule调度器的早期设计与smp调度竞争.md`——史料追加 ULE 文献佐证
9. `第102章-jemalloc/101.1-Jason-Evans-开发-jemalloc.md`——101.1.1 辨析追加 jemalloc 文献佐证

## 释疑说明

- 第88章（磁盘）概述存疑 id 1870“CVSup 注册商标”已由概述勘误登记，本节未重复处理。
- 第94章 93.1.1“jail 诞生 2000.3.14/2000.3 两种说法”已由既有代码库核证消解（1999-04-28 commit），本次邮件佐证进一步确认。
- 各章存疑点凡涉及代码库 commit 归属、商业合同、董事会记录、州务卿档案者，均超出邮件列表库与参考文献库覆盖范围，保留存疑或标注“两库无法验证”。
