# xen(4) 手册页（复用卡，ref10972）

- **性质**：复用本线 ref10972（2026-11-18 b025 建，`man.freebsd.org/cgi/man.cgi?query=xen&sektion=4`），本卡只登记本批新取的引文段
- **source_url**：<https://man.freebsd.org/cgi/man.cgi?query=xen&sektion=4>
- **本批取句（逐字，一处；"virtu-\nalizable" 为排版软连字符断词，还原为 virtualizable）**：

  > When first released, Xen required that i386 kernels be compiled "para-virtualized" as the x86 instruction set was not fully virtualizable.

- **与前批的关系**：ref10972 原卡（b025）引 guest/host 接入模式句；本批取 **DESCRIPTION 历史段首句**——初代 Xen 因 x86 指令集不可完全虚拟化而要求内核半虚拟化编译：这正是**半虚拟化与硬件辅助的分界原点**（硬件辅助 VT-x／AMD-V 的出现即为了消除此要求），同段后文“para-virtualization modifies the virtual memory system to use hypervisor calls (hypercalls)…”本批未整句引。
- **通道披露**：`format=ascii` 变体；行内多空格归一；**软连字符还原披露**（"virtu-"＋换行＋"alizable"→"virtualizable"，属排版断词非词汇连字符，逐字还原后连读）；引号符 "para-virtualized" 照录原文直引号。
- **限度**：①本句证历史分界的成因，不证两类模式的具体性能数值；②“性能与兼容分界”的展开属编纂论旨。
- **本批落点**：V37.3.4.4
- **考据日期**：2026-11-18（Task 8.2 G4-P2 批 b026；复用 ref10972，official_doc／L3）

## b027 追加引文（2026-11-18，第三段）

- **本批取句（逐字，一处；行内多空格归一，词界换行无断词）**：

  > although para-virtualized device drivers were also required to access resources such as virtual network interfaces and disk devices.

- **考据注**：用于 **DomU 内核适配面覆盖驱动栈**（V37.3.4.2）——半虚拟化设备驱动为访问虚拟网络接口与磁盘设备等资源所必需，与 b025 的接入模式句、b026 的分界成因句同页三面互补（接入模式／分界成因／驱动适配）。
- **限度**：①事件通道（event channel）机制本句未展开，另有出处面；②“适配面覆盖驱动栈”的清单化属编纂论旨。
- **落点**：V37.3.4.2（复用 ref10972，official_doc／L3）
