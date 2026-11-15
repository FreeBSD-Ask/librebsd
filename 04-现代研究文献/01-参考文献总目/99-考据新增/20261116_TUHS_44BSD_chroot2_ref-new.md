# 4.4BSD chroot(2) 手册页（TUHS 收录）（新 ref）引用卡

- **性质**：UNIX Heritage Society（TUHS）源码树浏览器收录的 4.4BSD `usr/src/lib/libc/sys/chroot.2`（mroff 源文，版权页署 1983、1991、1993 加州大学董事会）；本机 Chrome UA urllib 直取，`<pre>` 块 3,578 字符
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b001；source_url 四键查重：库内 tuhs.org 条目为 pipermail 邮件页（ref2006）与 Wiki 语料，`utree.pl?file=4.4BSD` 无重合）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/lib/libc/sys/chroot.2>
- **quote（逐字，两处；均为 mroff 渲染后的句子，宏标记不入引文）**：
  1. It should be noted that chroot has no effect on the process's current directory.
  2. In order for a directory to become the root directory a process must have execute (search) access for that directory.
- **考据注**：第 1 句给**语义边界**（改根不改进程当前目录——“不做什么”先写清，越界可能才可讨论）；第 2 句给**前提**（要使目录成为根，进程须对该目录有执行／搜索权限）。**自纠（本卡已更正）**：初稿曾另引“仅限超级用户”与“起于 4.2BSD”两句，与 5.2.3（超级用户约束的用意）／5.2.2（引入时点）**重题**，已撤出本节：495653 改为第 2 句的语义前提条、495654 整条删除；两句留待 5.2.2／5.2.3 补证时按各自题旨重取。**载体说明**：TUHS 为 4.4BSD 源码树的公开转录，按 mroff 原文核对；页面附带“相似文件”列表与正文无关，未引。**版本说明**：这是 4.4BSD 版手册页，非 4.2BSD 原始页。**未取**：ERRORS 节的 errno 清单，留待 5.3 节复核
- **本批落点**：V31.5.2.1 第 1 块（第 1 句）、第 2 块（第 2 句）
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b001；official_doc／L3）
