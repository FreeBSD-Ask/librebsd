# FreeBSD 2012 年第一季度状态报告《GNU-Free C++11 Stack》（新 ref）引用卡

- **性质**：FreeBSD 项目季度状态报告（2012 年 1—3 月，freebsd-stable 邮件列表存档转发；C++ 栈节署 David Chisnall）
- **数据库**：新建 ref（2026-11-27 G4 全责线 V37 批 b028；freebsd.org 域内无该报告条目）
- **source_url**：<https://lists.freebsd.org/pipermail/freebsd-stable/2012-May/067486.html>
- **quote（逐字，两段）**：

  > we're on track for a BSD licensed C++ stack in 10.0.

  > Removing libstdc++ from the base system and making it available through ports for backwards compatibility.

  > With clang 3.1, we now pass all of the C++11 atomics tests.

- **考据注**：用于**libc++ 以 BSD 许可栈进入基本系统**（13.2.1）与**标准库移植的线程／原子适配**（13.2.3）。首句自述目标为“10.0 交付 BSD 许可的 C++ 栈”；第二句为开放任务清单第三项，记移除基本系统内 libstdc++、改由 Ports 提供向后兼容；第三句记 clang 3.1 下通过全部 C++11 原子测试，支撑移植须适配线程／原子模型的判断。
- **限度**：①报告为项目自述，属计划与进度陈述，不构成发布事实的终局证明（10.0 实际落地须以发布说明复核）；②移除 libstdc++ 为开放任务表述，非已完成记录；③“BSD licensed”指栈的整体许可取向，具体许可证文本另见 libc++ 与 libcxxrt 各自声明。
- **本批落点**：V37.13.2.1、V37.13.2.3
- **考据日期**：2026-11-27（Task 8.2 G4 全责线 V37 批 b028；official_doc／L3）
