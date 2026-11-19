# FreeBSD `sys/i386/conf/LINT`（releng/1）引用卡

- **性质**：FreeBSD 源码树 `sys/i386/conf/LINT`（i386 内核全量校验配置）纯文本，取自 FreeBSD 官方 cgit 的 plain 视图（releng/1 分支；7,116 字节；文件头注释自述“LINT -- config file for checking all the sources, tries to pull in as much of the source tree as it can. This kernel is NOT MEANT to be runnable!”；行内版本戳 `$Id: LINT,v 1.79 1994/06/16 05:31:16 jkh Exp $`＝1.x 时代修订）
- **数据库**：新建 ref（2026-11-20 V36 P2 联网补证批 b003；source_url 四键查重：库内 cgit 既有 8 行均 doc/树或他路径，无 `sys/i386/conf/LINT`；规范化 URL（去 query）查重亦无）
- **source_url**：<https://cgit.freebsd.org/src/plain/sys/i386/conf/LINT?h=releng/1>
- **quote（逐字，三处，分落三块；原文件制表符缩进，引文按行原样保留制表符）**：
  1. `machine		"i386"`＋`cpu		"I386_CPU"`＋`cpu		"I486_CPU"`＋`cpu		"I586_CPU"`＋`options		MATH_EMULATE		#Support for x87 emulation`（machine／cpu 档位行＋浮点模拟选项）
  2. `# LINT -- config file for checking all the sources, tries to pull in`＋`#	as much of the source tree as it can.`（文件头自述用途）
  3. `config		"386bsd"	root on wd0 swap on wd0 and sd0 dumps on wd0`（config 行）
- **考据注**：第 1 处是**机型档位界定**：i386 机器行固定，CPU 档位以选项并列（386／486／586=Pentium），低档机的浮点硬件缺位由 MATH_EMULATE 模拟覆盖——硬件档位决定内核取舍的配置层实态。第 2 处是**驱动纳入跨度的载体自述**：LINT 的存在意义即把源码树尽可能拉入一份配置校验，驱动清单的覆盖面由此文件界定（同目录另有 devices.i386 记 swap 设备 major 号表：wd/dk/fd/wt/sd/st/cd/mcd/scd 九类）。第 3 处是**硬件差异压缩的直证**：内核名保留 “386bsd”、root／swap／dump 设备全部写死在 config 行内——386 移植把硬件事务压进配置层的形态自证。**年代披露**：releng/1 分支为 1.x 收尾态（LINT v1.79＝1994-06-16），所引为 1.x 后期文本；386BSD 0.1（1992）时代的原句如须逐字另考（本批三题 thesis 均落在“机制形态”而非逐字年代，1.x 收尾态可证机制存在与形态）。**载体披露**：配置文件原文含制表符缩进，引文按行原样保留制表符，未做空白归一。
- **本批落点**：V36.1.3.1 第 1 块（第 1 处）、V36.1.3.2 第 1 块（第 2 处）、V36.1.3.3 第 1 块（第 3 处）
- **考据日期**：2026-11-20（Task 8.2 G4 全责线 V36 P2 批 b003；official_doc／L3）
