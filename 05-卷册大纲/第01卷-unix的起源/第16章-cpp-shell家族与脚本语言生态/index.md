---
chapter: 第 16 章
id: CH16
volume: 第01卷-unix的起源
---

# 第 16 章 cpp-shell家族与脚本语言生态

## 要点

- FreeBSD Ports 提供 GCC（g++）与 Clang/LLVM（clang++）两大 C++ 编译器；FreeBSD 10.0（2014 年 1 月）起 i386/amd64/arm 等平台默认使用 Clang/LLVM 3.3，GCC 4.2.1 不再默认构建（仅 pc98 等少数平台仍保留）；C++ 生态在 FreeBSD 用户态中稳定
- BSD 系统启动脚本（rc.d）、Ports 系统、大量系统工具均使用 Bourne shell 语法（sh）编写；csh 因编程特性缺陷（变量处理、语法不一致）不适合脚本编程，主要用于交互式使用；sh 作为 POSIX 标准 shell 保证脚本可移植性；FreeBSD 基础系统中的 sh 为 Almquist shell 衍生物，轻量且符合 POSIX，不包含 bash 特有扩展
- Sun 2006 年 GPL 化 Java（OpenJDK），2007 年开源；FreeBSD OpenJDK 移植由社区推动，2010 年起稳定；OpenJDK 6/7/8/11/17 均有 FreeBSD 移植；**OpenJDK BSD Port 项目**（openjdk.java.net/projects/bsd-port/，2026-07-28 WebFetch 核实）——由 OpenJ
- FreeBSD Ports 系统本身用 shell 与 Makefile 实现，但管理脚本语言包；Ports 提供分发渠道，脚本语言丰富 Ports 内容，二者相互促进

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_1534] 卷“第01卷-unix的起源”第 16 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- FreeBSD 切换至 Clang 的具体时间线——FreeBSD 9.0（2012 年 1 月）已默认安装 Clang 3.0 但默认编译器仍为 GCC 4.2.1，需设置 WITH_CLANG_IS_CC 选项方可切换；FreeBSD 10.0（2014 年 1 月）i386/amd64/arm 等平台正式以 Clang 为默认系统编译器，GCC 4.2.1 仅在 pc98 等平台保留；GCC
- csh 不适合脚本编程——这是 UNIX 社区长期共识，经典论文《Csh Programming Considered Harmful》（1995？）有详述；系统脚本坚持使用 POSIX sh 是工程与可移植性的选择
- OpenJDK FreeBSD 移植的版本覆盖——并非所有 LTS 版本均完整移植；OpenJDK BSD Port 项目覆盖 FreeBSD、OpenBSD、NetBSD、Mac OS X 四个 BSD 系平台，但各平台的版本覆盖与维护程度不一，FreeBSD 与 Mac OS X 为主要维护目标，OpenBSD 与 NetBSD 的版本更新存在滞后；[考据完成：2026-07-28 该处存疑标
- Ports 系统的 “语言中立性”——实际偏向 C 与 shell，脚本语言为被管理对象

## 文献

- FreeBSD 10.0 Release Notes（2014-01）；FreeBSD 2012 Q1 Status Report（Clang Replacing GCC 章节）；LLVM Documentation；GCC Documentation [考据脚注：经相关权威来源交叉验证。]
- FreeBSD src/etc/rc.d/ 脚本源码；POSIX 1003.1-2008 Shell Command Language；FreeBSD Porter's Handbook ［A］
- Sun 2006 Announcement；OpenJDK BSD Port Project (openjdk.java.net/projects/bsd-port/，2026-07-28 WebFetch 核实)；OpenJDK BSD Port Wiki (wiki.openjdk.org/display/BSDPort/Main，2026-07-28 WebFetch 核实，Dalibor Topic 创建，Brian Beck 2013-02-19 最后更新)；FreeBSD Ports (openjdk6: freshports.org/java/openjdk6/；openjdk7: freshports.org/java/openjdk7/)；OpenJDK Documentation；FreeBSD OpenJDK Porting Guide；wiki.freebsd.org/Java（2026-07-28 WebFetch 核实） ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1995-1995 年间：9,812 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Porter's Handbook；FreeBSD Ports Tree；FreeBSD Documentation ［B］
