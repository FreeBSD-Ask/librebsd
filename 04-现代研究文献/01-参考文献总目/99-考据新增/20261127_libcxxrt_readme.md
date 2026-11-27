# libcxxrt 仓库说明（新 ref）引用卡

- **性质**：libcxxrt 项目仓库 README（C++ ABI 实现，供标准 C++ 库底层使用）
- **数据库**：新建 ref（2026-11-27 G4 全责线 V37 批 b028；库内无 libcxxrt 仓库条目）
- **source_url**：<https://github.com/libcxxrt/libcxxrt>
- **quote（逐字，两段）**：

  > It is intended to sit below an STL implementation, and provide features required by the compiler for implementation of the C++ language.

  > Exception handling requires the assistance of a stack-unwinding library implementing the low-level parts of the ABI. Either libgcc_s or libunwind should work for this purpose.

- **考据注**：用于**libcxxrt 作为 C++ ABI 运行库的层位**（13.2.2）与**异常处理在编译器与运行库之间的分工**（13.2.4）。首句自述其位于 STL 实现之下、提供编译器实现 C++ 语言所需特性；次句说明异常处理须由实现 ABI 低层部分的栈展开库协助，libgcc_s 或 libunwind 均可承担。
- **限度**：①README 为项目自述，ABI 细节以 Itanium C++ ABI 规范为准；②“位于 STL 之下”是设计定位，FreeBSD 基本系统的具体链接形态另见构建与源码记录；③仓库随上游演进，文本以访问日快照为准。
- **本批落点**：V37.13.2.2、V37.13.2.4
- **考据日期**：2026-11-27（Task 8.2 G4 全责线 V37 批 b028；official_doc／L3）
