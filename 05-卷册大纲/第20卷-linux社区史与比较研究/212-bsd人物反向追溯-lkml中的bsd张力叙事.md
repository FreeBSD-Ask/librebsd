# 212 【Linux社区】BSD 人物反向追溯：BSD 维护者在 lkml 中的张力叙事
> 来源：lkml 中 from_email 含 @freebsd.org / @openbsd.org / @netbsd.org 的 BSD 人物邮件，与 205-211 章去重后 93 封候选，5 路并行读手逐封判定。
> 判定：83 CAND（剔除 10 条 subagent 标记的同补丁系列 v1/v2/RESEND 内容重复）。主题分布：BSD 谱系 70、许可证 9、人物 3、治理 1。
> 全库去重：本次 83 条与 205/206/207/208/209/210/211 章 252 条 ROW_MINE 严格去重（0 条完全重复）。

## 212.0 【Linux社区】体例说明
本文件系 lkml 中 BSD 域名（@freebsd.org / @openbsd.org / @netbsd.org）发件人邮件的 BSD 人物反向追溯产物。与 211 章（BSD 侧发展列表视角）互补，构成 BSD 人物在 Linux/BSD 两个阵营间的双向张力图谱。
**独特价值**：这 83 条是 BSD 维护者/开发者**主动以 BSD 身份在 lkml 出现**的张力叙事，覆盖 BSD 技术反向输出（mseal 派生自 OpenBSD mimmutable、getrandom 反向吸收 OpenBSD getentropy、ath 驱动移植回 FreeBSD）、GPL/BSD 许可证双许可补丁链（manu@freebsd.org DRM drm_client 系列）、BSD 领袖治理立场（Theo de Raadt mseal RFC 主导）。与 205-210 章 lkml 内部 BSD 技术承袭（tier A/B/ZFS/claims）形成第三方视角补充。
**叙事主线**：BSD 技术反向输出（Theo mseal/mimmutable、Bob Beck getrandom、Adrian Chadd ath 驱动移植回 FreeBSD）／BSD 许可证反向塑造 Linux（manu DRM drm_client 双许可补丁链、emaste jsmn MIT SPDX）／BSD 领袖治理立场（Theo de Raadt mseal RFC、Bob Beck minherit、Ed Maste Capsicum/openat）／BSD 血统工具 API 互操作（mbuf/mbuf accessor、openat 能力模式、getentropy 兼容层）。
**ROW_MINE 格式**：`<!-- ROW_MINE: lkml.messages.<N> -->`，N 为 lkml.messages 表的 id。

## 212.1 【Linux社区】BSD 技术反向输出与血统传承（70 条）

- 【Linux社区】2009年8月 Robert Watson(rwatson@freebsd.org) 在「Re: Security: information leaks in /proc enable keystroke recovery」串中 以「the OS community has not engaged well with the concerns raised by past cache-based crypto side channels」并引 Colin Percival RSA cache side channel，是 FreeBSD 安全工程经验与 Linux procfs 加固差距在 lkml 的公开对话证据 `<!-- ROW_MINE: lkml.messages.2247844 -->`
- 【Linux社区】2009年8月 Robert N. M. Watson(rwatson@freebsd.org) 在「Re: Security: information leaks in /proc enable keystroke recovery」串中 以「The OS timing issue we're discussing meet two of the definitions of "covert channel" presented in NCSC-TG-030」引 Orange Book 反驳 David Wagner，是 BSD 血统安全专家将 procfs 时序泄露论证为隐蔽通道、对比 FreeBSD 已加固而 Linux 未加固的分析证据 `<!-- ROW_MINE: lkml.messages.2375105 -->`
- 【Linux社区】2009年8月 Robert Watson(rwatson@freebsd.org) 在「Re: Security: information leaks in /proc enable keystroke recovery」串中 驳斥称 FreeBSD 内核 "computes debug permissions between two processes from a number of factors" 而非仅依赖 procfs 文件权限，是 BSD 安全模型相对 Linux procfs 设计凌驾的具体佐证 `<!-- ROW_MINE: lkml.messages.2592069 -->`
- 【Linux社区】2021年9月 Mark Kettenis(kettenis@openbsd.org) 在「[PATCH v5 4/4] arm64: apple: Add PCIe node」串中 提交 Apple M1 (t8103) 的 PCIe 设备树节点，是 OpenBSD 主力开发者把 OpenBSD 长期维护的 Apple Silicon 硬件逆向工作在 Linux 侧落地、以 BSD 血统驱动 Linux 硬件移植的例证 `<!-- ROW_MINE: lkml.messages.2634315 -->`
- 【Linux社区】2021年9月 Mark Kettenis(kettenis@openbsd.org) 在「[PATCH v5 3/4] dt-bindings: pci: Add DT bindings for apple,pcie」串中 提交 apple,pcie 设备树绑定并采用 "SPDX-License-Identifier: (GPL-2.0-only OR BSD-2-Clause)" 双许可，是 OpenBSD 开发者把 BSD-2-Clause 作为一等公民带进 Linux DT 绑定、实现 BSD 技术血统正式纳入 Linux 内核文档体系的许可治理张力案例 `<!-- ROW_MINE: lkml.messages.2669912 -->`
- 【Linux社区】2021年9月 Mark Kettenis(kettenis@openbsd.org) 在「[PATCH v5 0/4] Apple M1 PCIe DT bindings」串中 说明苹果 M1 PCIe 绑定的跨 OS 消费模型，指出 "the primary consumer for these bindings is U-Boot"，是 OpenBSD 开发者把 Apple Silicon PCIe 硬件知识以 Linux/U-Boot 双栈方式落地、扩展 BSD 硬件知识在 Linux 生态可见度的谱系叙事案例 `<!-- ROW_MINE: lkml.messages.2694761 -->`
- 【Linux社区】2021年9月 Mark Kettenis(kettenis@openbsd.org) 在「[PATCH v5 2/4] dt-bindings: interrupt-controller: msi: Add msi-ranges property」串中 扩展 Linux MSI controller 绑定的 msi-ranges 属性，是 OpenBSD 开发者以 Apple Silicon 硬件需求推动 Linux 中断控制器绑定通用化的 BSD 血统技术迁移案例 `<!-- ROW_MINE: lkml.messages.2714948 -->`
- 【Linux社区】2021年9月 Mark Kettenis(kettenis@openbsd.org) 在「[PATCH v5 1/4] dt-bindings: interrupt-controller: Convert MSI controller to json-schema」串中 提交通用 MSI controller 绑定并将 SPDX 设为 "(GPL-2.0-only OR BSD-2-Clause)"，是 OpenBSD 开发者把 BSD-2-Clause 许可显性写进 Linux 通用中断控制器文档、与 Apple Silicon 支持绑定的 BSD 谱系张力案例 `<!-- ROW_MINE: lkml.messages.2762700 -->`
- 【Linux社区】2021年12月 Mark Kettenis(kettenis@openbsd.org) 在「[PATCH] arm64: dts: apple: t8103: Expose PCI node for the WiFi MAC address」串中 为 Apple M1 WiFi 暴露 PCI 节点并接入 m1n1 bootloader，是 OpenBSD 开发者以 BSD 世界成熟的 m1n1 bootloader 生态为 Linux Apple Silicon 移植补齐硬件地址链路的例证 `<!-- ROW_MINE: lkml.messages.2764628 -->`
- 【Linux社区】2023年10月 Theo de Raadt(deraadt@openbsd.org) 在「Re: [RFC PATCH v1 0/8] Introduce mseal() syscall」串中与 Linus Torvalds 讨论 Linux 新系统调用 mseal，指出 "our chrome fork knows how to use it" 并详述 OpenBSD 版 Chrome 使用 mimmutable 的 1280 处补丁，是 OpenBSD 创始人以 BSD 侧 Chrome 移植实战经验向 Linux 社区反向输入安全 API 设计参照的 BSD/Linux 直接张力案例 `<!-- ROW_MINE: lkml.messages.3464050 -->`
- 【Linux社区】2023年10月 Theo de Raadt(deraadt@openbsd.org) 在「Re: [RFC PATCH v1 0/8] Introduce mseal() syscall」串中 将 Linux mseal() 与 OpenBSD mimmutable(2) 直接对标，指出 "mseal() is a clone of mimmutable(2), but with an extremely over-complicated API based upon dubious arguments"，是 OpenBSD 创始人以 BSD 血统 API 反向评判 Linux 新系统调用设计的核心 BSD/Linux 谱系张力案例 `<!-- ROW_MINE: lkml.messages.3479951 -->`
- 【Linux社区】2023年10月 Theo de Raadt(deraadt@openbsd.org) 在「Re: [RFC PATCH v1 0/8] Introduce mseal() syscall」串中 与 Google 工程师 Stephen Röttger 深入讨论 OpenBSD mimmutable() 与 Linux mseal() 的安全语义差异，指出 "Partial sealing is not safe"，是 OpenBSD 创始人以 BSD 血统安全实践反向审视 Linux 内核新安全系统调用的深度 BSD/Linux 技术张力案例 `<!-- ROW_MINE: lkml.messages.3483140 -->`
- 【Linux社区】2023年10月 Theo de Raadt(deraadt@openbsd.org) 在「Re: [RFC PATCH v1 0/8] Introduce mseal() syscall」串中 向 Linux 开发者系统解释 OpenBSD mimmutable() 的 VA 层面语义，指出 "mimmutable() is not about permissions, but about locking permissions"，是 OpenBSD 创始人以 BSD 血统 API 作为教学范本反向影响 Linux 新系统调用 mseal 设计的核心谱系张力案例 `<!-- ROW_MINE: lkml.messages.3487991 -->`
- 【Linux社区】2023年10月 Theo de Raadt(deraadt@openbsd.org) 在「Re: [RFC PATCH v1 0/8] Introduce mseal() syscall」串中 以 OpenBSD mimmutable 语义反驳 Linux mseal 的位掩码设计，指出 "Don't make it an option that a program needs to set on pages"，是 OpenBSD 创始人以 BSD 侧成熟安全实践反向挑战 Linux 新 syscall 复杂度的 BSD/Linux 谱系张力案例 `<!-- ROW_MINE: lkml.messages.3542341 -->`
- 【Linux社区】2023 年 10 月 Theo de Raadt（deraadt@openbsd.org）在「Re: [RFC PATCH v1 0/8] Introduce mseal() syscall」串中批评 Linux 的 mseal()，认为 "you are building mseal for chrome, and chrome alone"，"I do not think this will work out for the rest of the application space"，理由有二："1) it is too complicated"，以及 "2) experience with mimmutable() says that applications don't do any of it themselves, it is all in execve(), libc initialization, and ld.so"，并点出提案者并非 execve、libc 或 ld.so 的开发者。`<!-- ROW_MINE: lkml.messages.3552940 -->`
- 【Linux社区】2023年12月 Theo de Raadt(deraadt@openbsd.org) 在「Re: [RFC PATCH v3 11/11] mseal:add documentation」串中 批评 Linux mseal() 的 Chrome 特定设计定位并建议放弃与 mimmutable 的类比，指出 "maybe this proposal should be using the name chromesyscall() instead"，是 OpenBSD 创始人以 BSD 侧成熟 API 实践反向评判 Linux 新系统调用定位的核心 BSD/Linux 谱系张力案例 `<!-- ROW_MINE: lkml.messages.3569904 -->`
- 【Linux社区】2023年12月13日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [RFC PATCH v3 11/11] mseal:add documentation」串中 解释 OpenBSD 默认不可变映射机制 「The OpenBSD kernel makes those regions immutable BY DEFAULT」 是 BSD 技术为 Linux mseal 提案提供设计源头的关键证据 `<!-- ROW_MINE: lkml.messages.3619216 -->`
- 【Linux社区】2023年10月20日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [RFC PATCH v1 0/8] Introduce mseal() syscall」串中 对比 OpenBSD 与 Linux 的 pkey 机制分歧 「we've ended up in a very different place than Linux」 是 BSD 维护者揭示 BSD 与 Linux 关键技术路线分歧的现场证据 `<!-- ROW_MINE: lkml.messages.3662146 -->`
- 【Linux社区】2024年3月14日 John Baldwin(jhb@freebsd.org) 在「Re: [PATCH 1/1] x86/elf: Add a new .note section containing Xfeatures information to x86 core files」串中 讨论 FreeBSD XSAVE core dump 与 Linux NT_X86_XSTATE 的兼容 「FreeBSD dumps an XSAVE register set note that matches the same layout of NT_X86_XSTATE used by Linux」 是 BSD 血统工具与 Linux ABI 互操作的关键见证 `<!-- ROW_MINE: lkml.messages.3739138 -->`
- 【Linux社区】2024年2月1日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v8 0/4] Introduce mseal」串中 以 OpenBSD 全源码实证反驳 Linus 的 PROT_SEAL 提案 「I'm grepping an entire Unix kernel and userland source tree」 是 BSD 实证主义方法论介入 Linux 内核 API 讨论的典范 `<!-- ROW_MINE: lkml.messages.3743437 -->`
- 【Linux社区】2024年5月14日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v10 0/5] Introduce mseal」串中 确认 Linux mseal 直接源自 OpenBSD mimmutable 「this version of mseal() is OpenBSD's mimmutable() with a basically unused extra flags argument」 是 BSD 技术被 Linux 采纳的直接证据 `<!-- ROW_MINE: lkml.messages.3753255 -->`
- 【Linux社区】2024年1月22日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v7 0/4] Introduce mseal()」串中 揭露 OpenBSD 已成熟部署不可变内存 「OpenBSD now uses this for a high percent of the address space」 是 BSD 系统级实践对 Linux API 设计的前瞻性指导 `<!-- ROW_MINE: lkml.messages.3762579 -->`
- 【Linux社区】2024年5月14日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v10 0/5] Introduce mseal」串中 论证 Linux mprotect 与 munmap 部分变更语义的攻击面 「The return values of mprotect and munmap are very rarely checked」 是 BSD 维护者从系统调用语义可靠性角度指认 Linux 独特风险的深度剖析 `<!-- ROW_MINE: lkml.messages.3762893 -->`
- 【Linux社区】2024年1月31日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v8 0/4] Introduce mseal」串中 系统性论证 MAP_SEALABLE 设计漏洞 「the ONLY way this could work is by adding a flag with the opposite meaning」 是 BSD 生态经验对 Linux API 复杂性的致命解构 `<!-- ROW_MINE: lkml.messages.3770240 -->`
- 【Linux社区】2024年5月14日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v10 0/5] Introduce mseal」串中 与 Linus 就 mprotect 原子性公开交锋 「The immutable memory management we have today in OpenBSD would completely impossible with such a flag」 是 BSD 维护者与 Linux 领袖就内核设计原则爆发的激烈冲突 `<!-- ROW_MINE: lkml.messages.3775406 -->`
- 【Linux社区】2024年2月1日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v8 0/4] Introduce mseal」串中 警示 mseal 使用陷阱 「you can only seal objects which you guarantee never get recycled」 是 BSD 经验主义对 Linux mseal API 语义陷阱的先知式警告 `<!-- ROW_MINE: lkml.messages.3787343 -->`
- 【Linux社区】2024年2月2日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v8 0/4] Introduce mseal」串中 揭示 OpenBSD MAP_STACK 强制机制与 mseal 的交互风险 「In OpenBSD, sigaltstack() forces MAP_STACK onto the specified region」 是 BSD 独有安全特性对 Linux mseal 设计盲区的补充警示 `<!-- ROW_MINE: lkml.messages.3790824 -->`
- 【Linux社区】2024年2月1日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v8 2/4] mseal: add mseal syscall」串中 要求 Linux 开发者用实证而非感觉论证 API 设计 「I did the same work in OpenBSD, at least 25% time over 2 years」 是 BSD 系统工程师对 Linux 内核开发方法论的正面挑战 `<!-- ROW_MINE: lkml.messages.3797643 -->`
- 【Linux社区】2024年5月14日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v10 0/5] Introduce mseal」串中 揭示 Linux m* 系统调用原子性偏离 POSIX 「I did not find the Linux behaviour anywhere else」 是 BSD 维护者从跨系统视角指认 Linux 语义异类地位 `<!-- ROW_MINE: lkml.messages.3810916 -->`
- 【Linux社区】2024年3月14日 John Baldwin(jhb@freebsd.org) 在「Re: [PATCH 1/1] x86/elf: Add a new .note section containing Xfeatures information to x86 core files」串中 倡导 FreeBSD 与 Linux 共享 XSAVE note 格式 「we would very much like to reach consensus on a shared format of the note」 是 BSD 开发者主动推动 BSD 与 Linux 内核 ABI 融合的姿态 `<!-- ROW_MINE: lkml.messages.3812255 -->`
- 【Linux社区】2024年1月20日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [RFC PATCH v3 11/11] mseal:add documentation」串中 推动 errno 语义在 OpenBSD 与 Linux 间统一 「we'll have something that is more-or-less compatible between Linux and OpenBSD」 是 BSD 维护者促成 Linux mseal 与 OpenBSD mimmutable 语义对齐的关键节点 `<!-- ROW_MINE: lkml.messages.3813346 -->`
- 【Linux社区】2024年2月1日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v8 2/4] mseal: add mseal syscall」串中 对 Linux 永久锁死 API 表达苦涩 「I should be the first person thrilled to see Linux make API/ABI mistakes they have to support forever」 是 BSD 视角对 Linux API 冻结机制的辛辣观察 `<!-- ROW_MINE: lkml.messages.3814556 -->`
- 【Linux社区】2024年2月1日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v8 0/4] Introduce mseal」串中 以简短警告预判 mseal 与 glibc 的兼容灾难 「the proposal doesn't work for glibc and all the applications」 是 BSD 维护者凭系统级经验对 Linux API 提案发出的闪电预判 `<!-- ROW_MINE: lkml.messages.3816028 -->`
- 【Linux社区】2024年1月20日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [RFC PATCH v3 11/11] mseal:add documentation」串中 论证 EPERM 优于 EACCES 并促成 BSD 与 Linux 对齐 「we'll have something that is more-or-less compatible between Linux and OpenBSD」 是 BSD 维护者主导 Linux errno 语义最终收敛的关键决策节点 `<!-- ROW_MINE: lkml.messages.3821853 -->`
- 【Linux社区】2024年1月31日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v8 0/4] Introduce mseal」串中 以反讽 O_DUPABLE 提议戳穿 Linux fd 设计脆弱 「we need protection against file descriptor desecration」 是 BSD 视角对 Linux 传统 Unix fd 语义的系统性批判 `<!-- ROW_MINE: lkml.messages.3843029 -->`
- 【Linux社区】2024年2月1日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v8 0/4] Introduce mseal」串中 以 BSD 全系统测试方法论对比 Linux 内核开发文化 「the absolutely minimal interface was written to apply to a whole operating system plus 10,000+ applications」 是 BSD 工程哲学与 Linux 迭代文化的根本分歧呈现 `<!-- ROW_MINE: lkml.messages.3851940 -->`
- 【Linux社区】2024年1月24日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v7 0/4] Introduce mseal()」串中 直陈 Linux mseal 直接派生自 OpenBSD mimmutable 「the raw idea stems directly from this」 是 BSD 技术血统被 Linux 继承的事实性宣告 `<!-- ROW_MINE: lkml.messages.3891707 -->`
- 【Linux社区】2024年2月2日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v8 0/4] Introduce mseal」串中 阐明 Unix 系统调用原子性原则 「In OpenBSD, all mimmutable() aspects were carefully studied to gaurantee this behaviour」 是 BSD 严守原子性契约对 Linux 部分变更语义的正式对比 `<!-- ROW_MINE: lkml.messages.3894039 -->`
- 【Linux社区】2024年1月23日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v7 0/4] Introduce mseal()」串中 以 OpenBSD 全量实证否定 PROT_SEAL 实用价值 「OpenBSD userland has zero places it can use mmap() MAP_IMMUTABLE」 是 BSD 系统级使用数据对 Linux 提案的实证否定 `<!-- ROW_MINE: lkml.messages.3899575 -->`
- 【Linux社区】2024年1月24日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v7 2/4] mseal: add mseal syscall」串中 论证 MAP_SEALABLE 破坏库边界通用性 「without breaking other extremely common circumstances where the allocation of memory and PERMANENT-USE-WITHOUT-RELEASE of such memory are seperated over a memory boundary」 是 BSD 系统架构视角对 Linux API 分界问题的深度剖析 `<!-- ROW_MINE: lkml.messages.3913557 -->`
- 【Linux社区】2024年4月16日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v10 2/5] mseal: add mseal syscall」串中 从跨系统视角指认 Linux m* 原子性异类 「Linux is an outlier here. Other systems do two passes over the entries in the range」 是 BSD 维护者系统学方法对 Linux 内核语义孤立的权威定性 `<!-- ROW_MINE: lkml.messages.3916725 -->`
- 【Linux社区】2024年1月20日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [RFC PATCH v3 11/11] mseal:add documentation」串中 指出 errno 差异阻塞 mimmutable 与 mseal 语义统一 「I think this remains the blocker which would prevent software from doing」 是 BSD 兼容性问题对 Linux API 定型的最后阻碍 `<!-- ROW_MINE: lkml.messages.3919387 -->`
- 【Linux社区】2024年2月1日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v8 0/4] Introduce mseal」串中 批评 Linux mseal 设计者缺乏完整操作系统经验 「you've not seen a complete operating system using it」 是 BSD 维护者对 Linux 内核开发视野局限的尖锐指认 `<!-- ROW_MINE: lkml.messages.3920765 -->`
- 【Linux社区】2024年3月14日 John Baldwin(jhb@freebsd.org) 在「Re: [PATCH 1/1] x86/elf: Add a new .note section containing Xfeatures information to x86 core files」串中 提出 XSAVE note 布局描述以解决 GDB 跨平台解析失败 「GDB fails to parse the entire note」 是 BSD 开发者以 FreeBSD 实战经验推动 Linux ABI 兼容的关键技术贡献 `<!-- ROW_MINE: lkml.messages.3922092 -->`
- 【Linux社区】2024年1月22日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v7 0/4] Introduce mseal()」串中 论证 mseal 对分配器控制的严苛要求 「mseal requires control of the whole stack between allocation and consumption」 是 BSD 系统级实现视角对 Linux mseal 语义边界的清晰界定 `<!-- ROW_MINE: lkml.messages.3941390 -->`
- 【Linux社区】2024年2月1日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v8 0/4] Introduce mseal」串中 建议 Linux 先实现与 mimmutable 最大兼容的 mseal 「add basic mseal() that is maximum compatible with mimmutable」 是 BSD 维护者主动为 Linux mseal 铺设 BSD 兼容路径的务实建议 `<!-- ROW_MINE: lkml.messages.3941535 -->`
- 【Linux社区】2024年1月24日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v7 2/4] mseal: add mseal syscall」串中 强调 mseal 编程错误属于既有 Unix 编程责任 「Programmers have complete control over the address space in a program」 是 BSD 维护者从 Unix 系统观出发的 mseal 语义辩护 `<!-- ROW_MINE: lkml.messages.3977717 -->`
- 【Linux社区】2024年10月4日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v2 1/1] mseal: update mseal.rst」串中 追问 Linux mseal 是否真正解决 madvise 破坏问题 「In OpenBSD, mimmutable() solves this problem」 是 BSD 实现对 Linux mseal 语义完备性的对照质询 `<!-- ROW_MINE: lkml.messages.4008278 -->`
- 【Linux社区】2024年10月22日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v1 1/2] mseal: Two fixes for madvise(MADV_DONTNEED) when sealed」串中 从旁观角度认可 Linux 侧 MADV_COLD 替代方案 「Comment from the sidelines: That seems clever enough」 是 BSD 外部观察对 Linux mseal madvise 交互修复方案的认可 `<!-- ROW_MINE: lkml.messages.4148588 -->`
- 【Linux社区】2024年10月4日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v2 1/1] mseal: update mseal.rst」串中 指出 mimmutable 会阻塞全部破坏性 madvise 操作 「In OpenBSD, mimmutable blocks all those madvise() operations」 是 BSD 实现对 Linux mseal madvise 语义完备性的对照质询 `<!-- ROW_MINE: lkml.messages.4196350 -->`
- 【Linux社区】2012年5月 Adrian Chadd(adrian@freebsd.org) 在「Re: [PATCH] mwl8k: Add 0x2a02 PCI device-id (Marvell 88W8361)」串中 提示 "the topdog firmware that FreeBSD ships with supports hostap mode"，是 BSD 随附固件资产反哺 Linux 驱动能力建设的旁证 `<!-- ROW_MINE: lkml.messages.5117708 -->`
- 【Linux社区】2012年3月 Adrian Chadd(adrian@freebsd.org) 在「Re: [PATCH wireless-next 2/3] ath5k: Introduce _ath5k_printk to reduce code/text」串中 以 FreeBSD HAL 将调试输出宏化使 "aren't evaluated unless the level (or debug bitmap in my case) fires" 的做法为 Linux ath5k 日志改造立论，是 BSD 编码范式渗入 Linux 无线驱动的范例 `<!-- ROW_MINE: lkml.messages.5136171 -->`
- 【Linux社区】2010年11月 Adrian Chadd(adrian@freebsd.org) 在「Re: Challenges with doing hardware bring up with Linux first」串中 预告将 "port the AR9003 hwops code over" 并先以 kite/merlin 校准代码在 FreeBSD 试跑，是 BSD 直接吸收 Linux 无线驱动硬件抽象层的实例 `<!-- ROW_MINE: lkml.messages.5183453 -->`
- 【Linux社区】2013年4月 Adrian Chadd(adrian@freebsd.org) 在「Re: Version number policy!」串中 以 FreeBSD ext2/3 分支实现维护者自述 "I'm a FreeBSD user. I know what it's like to have an alternate, out of" 的经历为例论证特性位图无法自动解决互操作性，是 BSD 文件系统经验反哺 Linux 固件版本治理的实例 `<!-- ROW_MINE: lkml.messages.5575431 -->`
- 【Linux社区】2014年7月 Bob Beck(beck@openbsd.org) 在「Re: [PATCH, RFC] random: introduce getrandom(2) system call」串中 借该讨论向内核询问 "getting MAP_INHERIT_ZERO minherit() support" 的 OpenBSD 内存继承语义，是 OpenBSD 语义向 Linux 渗透的标志性案例 `<!-- ROW_MINE: lkml.messages.5751475 -->`
- 【Linux社区】2014年7月 Bob Beck(beck@openbsd.org) 在「Re: [PATCH, RFC] random: introduce getrandom(2) system call」串中 表示 "we're going to put that in right away" 即 OpenBSD 将随待合入的 syscall 实现直接支持 getrandom(2)，是 Linux 新增系统调用被 OpenBSD 反向吸收的反例 `<!-- ROW_MINE: lkml.messages.5756685 -->`
- 【Linux社区】2014年7月 Bob Beck(beck@openbsd.org) 在「Re: [PATCH, RFC] random: introduce getrandom(2) system call」串中 针对 Linux 缺乏 minherit 提出 "maybe a FORK_ZERO for madvise? or a similar way" 方案，是 OpenBSD 语义向 Linux 内存语义协商的延续 `<!-- ROW_MINE: lkml.messages.5773726 -->`
- 【Linux社区】2013年4月 Adrian Chadd(adrian@freebsd.org) 在「Re: Version number policy!」串中 呼应开放固件规则草案 "for the community, for BSD / Linux" 的共同适用目标并以共享库版本兼容模型回应，是 BSD 与 Linux 在 802.11 开放固件治理上的协作实例 `<!-- ROW_MINE: lkml.messages.5800845 -->`
- 【Linux社区】2014年7月 Bob Beck(beck@openbsd.org) 在「Re: [PATCH, RFC] random: introduce getrandom(2) system call」串中 提议 libc 补齐 getentropy 兼容层「it would be good if there was a way to influence the various libc people to ensure they manage to provide a getentropy()」，是 OpenBSD getentropy 反向塑造 Linux getrandom 设计的关键证据 `<!-- ROW_MINE: lkml.messages.5905773 -->`
- 【Linux社区】2017年10月 Adrian Chadd(adrian@freebsd.org) 在「Re: [PATCH] ath10k: fix core PCI suspend when WoWLAN is supported but disabled」串中 以 FreeBSD 移植经验背书 ath10k 补丁「I did this on my in progress ath10k port to freebsd」，是 FreeBSD 移植 Linux ath10k 驱动反哺 Linux 主树的证据 `<!-- ROW_MINE: lkml.messages.6568798 -->`
- 【Linux社区】2017年2月 Adrian Chadd(adrian@freebsd.org) 在「Re: [PATCH 1/3] ath10k: remove ath10k_vif_to_arvif()」串中 建议 Linux skb 引入类似 FreeBSD mbuf 的访问器「If there were accessors for the skb data / len fields (like we do for mbufs)」，是 BSD mbuf 抽象成为 Linux API 可迁移性讨论参照物的证据 `<!-- ROW_MINE: lkml.messages.6629221 -->`
- 【Linux社区】2018年10月 Ed Maste(emaste@freebsd.org) 在「Re: [PATCH v2 1/3] namei: implement O_BENEATH-style AT_* flags」串中 说明 FreeBSD Capsicum O_BENEATH 起源并呼吁接口对齐「Ideally I would like to see us have the same API」，是 FreeBSD Capsicum 沙箱语义直接输入 Linux namei 补丁系列的证据 `<!-- ROW_MINE: lkml.messages.6852526 -->`
- 【Linux社区】2018年4月 Kyle Evans(kevans@freebsd.org) 在「[PATCH v3] ARM: dts: sunxi: Add sid for a83t」串中 说明 FreeBSD 已实现外部驱动「a83t-sid is not currently supported by nvmem/sunxi-sid, but it is supported in an external driver for FreeBSD」，是 FreeBSD 先行实现的 a83t SID 驱动反向推动 Linux DTS 合并的证据 `<!-- ROW_MINE: lkml.messages.6954488 -->`
- 【Linux社区】2020年6月 Kyle Evans(kevans@freebsd.org) 在「Re: [PATCH v5 1/3] open: add close_range()」串中 从 FreeBSD 视角回应 Szabolcs Nagy 的 closefrom 反例，指出 "this example seems to be innocuous on FreeBSD (and likely other *BSD)"，是 FreeBSD 维护者在 Linux 新系统调用 close_range 讨论中提供 BSD 语义对照、说明 Linux 在 fork-exec 关闭 fd 这一 BSD 风格接口的历史缺口的例证 `<!-- ROW_MINE: lkml.messages.7484293 -->`
- 【Linux社区】2020年6月 Kyle Evans(kevans@freebsd.org) 在「Re: [PATCH v5 1/3] open: add close_range()」串中 论证 Linux close_range 相较 FreeBSD closefrom 的效率与调试优势，指出 "You've absolutely not lived life until you've had to watch thousands of close() calls painfully scroll by in truss/strace"，是 FreeBSD 维护者以 BSD 传统 closefrom 接口的经验教训推动 Linux 采纳近亲 API 的 BSD 血统 API 讨论案例 `<!-- ROW_MINE: lkml.messages.7490131 -->`
- 【Linux社区】2020年6月 Jung-uk Kim(jkim@freebsd.org) 在「Re: [PATCH] ACPICA: fix UBSAN warning using __builtin_offsetof」串中 从 FreeBSD 视角建议 ACPI 头采用平台特定的 offsetof 定义，指出 "I think we should let platform-specific acfoo.h decide what to do here"，是 FreeBSD 维护者在共享 ACPICA 头中捍卫非 Linux 平台（含 BSD）与 Linux 内核共存的跨平台接口治理例证 `<!-- ROW_MINE: lkml.messages.7659740 -->`
- 【Linux社区】2020年6月 Kyle Evans(kevans@freebsd.org) 在「Re: [PATCH v5 1/3] open: add close_range()」串中 以 OpenBSD sshd 源码引用论证 closefrom 语义在 BSD 世界已是成熟实践，指出 "OpenSSH sshd will closefrom() just after argument parsing"，是 FreeBSD 维护者以 BSD 血统代码作为 Linux 新 API close_range 设计参照的 BSD 谱系叙事案例 `<!-- ROW_MINE: lkml.messages.7704537 -->`
- 【Linux社区】2021年5月 Mark Kettenis(kettenis@openbsd.org) 在「[PATCH 1/2] dt-bindings: pinctrl: Add DT bindings for apple,pinctrl」串中 提交 apple,pinctrl 绑定并采用 "(GPL-2.0-only OR BSD-2-Clause)" SPDX，是 OpenBSD 开发者把 BSD-2-Clause 双许可作为 Apple Silicon 硬件移植的一等公民策略、推动 BSD 血统进入 Linux 内核文档体系的核心张力案例 `<!-- ROW_MINE: lkml.messages.7761792 -->`
- 【Linux社区】2021年5月 Mark Kettenis(kettenis@openbsd.org) 在「[PATCH 2/2] arm64: apple: Add pinctrl nodes」串中 为 Apple Silicon Mac (t8103) 添加 pinctrl 与 GPIO 节点，是 OpenBSD 开发者把 OpenBSD 长期积累的 Apple Silicon 硬件逆向工作系统性移植进 Linux DTS 的谱系迁移案例 `<!-- ROW_MINE: lkml.messages.7842394 -->`
- 【Linux社区】2021年5月 Mark Kettenis(kettenis@openbsd.org) 在「[PATCH 0/2] Apple M1 pinctrl DT bindings」串中 说明 pinctrl 绑定的跨 OS 消费模型，指出 "the primary consumer for these bindings is U-Boot"，是 OpenBSD 开发者把 Apple Silicon pinctrl 硬件知识以 Linux/U-Boot 双栈落地、扩展示 BSD 硬件理解在 Linux 生态影响的谱系案例 `<!-- ROW_MINE: lkml.messages.7931884 -->`

## 212.2 【Linux社区】BSD 开发者反向塑造 Linux 许可证（9 条）

- 【Linux社区】2002年8月 Robert Watson(rwatson@freebsd.org) 在「Re: [PATCH] Define ENOATTR in 2.5 kernels」串中 以「In general, BSD VFS's return EOPNOTSUPP when VFS or vnode operations attempted on an object are not defined」回应 Linux ENOATTR 补丁，是 FreeBSD 团队以 errno(2) 权威解释介入 Linux ABI 定义、跨内核错误码标准之争的早期证据 `<!-- ROW_MINE: lkml.messages.1903261 -->`
- 【Linux社区】2007年9月 Henning Brauer(henning@openbsd.org) 在「Re: Wasting our Freedom」串中 以「the HAL code is under a pure BSD license」附议 ath5k HAL 采用 BSD 许可，是 GPL 与 BSD 许可冲突在 ath5k 移植案上进入 lkml 公共讨论的直接证据 `<!-- ROW_MINE: lkml.messages.2275598 -->`
- 【Linux社区】2007年9月 Reyk Floeter(reyk@openbsd.org) 在「Re: request for information about the "ath5k" licensing」串中 以「I'm still waiting for an answer. Your process is taking too long.」追问 ath5k 代码许可修改进展，是 OpenBSD OpenHAL 作者以版权人身份向 lkml 施压、GPL/BSD 移植争议的直接在场证据 `<!-- ROW_MINE: lkml.messages.2368389 -->`
- 【Linux社区】2019年12月 Ed Maste(emaste@freebsd.org) 在「Re: [PATCH] perf tools: correct license on jsmn json parser」串中 澄清 jsmn 头文件许可证归属，指出 "json.h is actually part of Andi Kleen's wrapper and I suspect should be 2-clause BSD"，是 FreeBSD 维护者在 Linux perf 工具链中澄清 MIT/BSD/GPL 三者边界、守护 BSD 兼容许可链的例证 `<!-- ROW_MINE: lkml.messages.7226589 -->`
- 【Linux社区】2019 年 12 月 Ed Maste(emaste@freebsd.org) 提交 perf tools 修正 jsmn json 解析器许可证的补丁，将 jsmn.h 的 SPDX 标识符由 GPL-2.0 更正为 MIT，说明该头文件属于 jsmn json 解析器、系引入于提交 867a979a83，应将 SPDX 标签更正以表明其采用 MIT 许可，该补丁已获 Andi Kleen 认可。`<!-- ROW_MINE: lkml.messages.7319459 -->`
- 【Linux社区】2020年2月 Emmanuel Vadot(manu@freebsd.org) 在「[PATCH 1/2] drm/client: Dual licence the file in GPL-2 and MIT」串中 提交 drm_client.c 双许可补丁，明确写出 "Change the licence to a dual one with MIT so BSDs could use this file"，是 FreeBSD 贡献者以 "BSDs could use this file" 为核心理由推动 Linux DRM 代码向 BSD 兼容许可转型的张力案例 `<!-- ROW_MINE: lkml.messages.7473914 -->`
- 【Linux社区】2020年2月 Emmanuel Vadot(manu@freebsd.org) 在「[PATCH 0/2] Dual licence some files in GPL-2.0 and MIT」串中 说明 Linux DRM 源文件对 BSD 系统的许可障碍，指出 "Those files are a problem with BSDs as we cannot include them"，是 FreeBSD 贡献者把 Linux DRM 代码无法被 BSD 树包含的许可冲突显性化、并推动 Noralf Trønnes 等原作者同意双许可的许可治理叙事 `<!-- ROW_MINE: lkml.messages.7475731 -->`
- 【Linux社区】2020年2月 Emmanuel Vadot(manu@freebsd.org) 在「[PATCH 2/2] drm/format_helper: Dual licence the file in GPL 2 and MIT」串中 提交 drm_format_helper.c 双许可补丁，明确写出 "Change the licence to a dual one with MIT so BSDs could use this file"，是 FreeBSD 贡献者以 BSD 包含 Linux DRM 代码为理由推动 Linux 向 BSD 兼容许可转型的直接张力案例 `<!-- ROW_MINE: lkml.messages.7650031 -->`
- 【Linux社区】2020年3月 Emmanuel Vadot(manu@freebsd.org) 在「[PATCH 2/2] drm/format_helper: Dual licence the header in GPL-2 and MIT」串中 提交 drm_format_helper.h 从 GPL-2.0-or-later 改为 GPL-2.0-or-later or MIT 的补丁，是 FreeBSD 贡献者延续同一许可冲突把 Linux DRM 头文件推向 BSD 兼容许可的直接动作 `<!-- ROW_MINE: lkml.messages.7722314 -->`

## 212.3 【Linux社区】BSD 人物在 lkml 的张力出场（3 条）

- 【Linux社区】2007年9月 Gilles Chehade(gilles@openbsd.org) 在「Re: Wasting our Freedom」串中 以「no one seems to miss you so much in the BSD camp」回应 Tso「我16年前决定转向 Linux 而非 BSD」，是 BSD 与 Linux 阵营互相嘲讽进入 lkml 的标志性交锋 `<!-- ROW_MINE: lkml.messages.2465477 -->`
- 【Linux社区】2025年1月9日 Mark Kettenis(kettenis@openbsd.org) 在「[PATCH] arm64: dts: qcom: x1e80100: Mark usb_2 as dma-coherent」串中 为 Qualcomm x1e80100 DTS 添加 dma-coherent 属性 「Make this USB controller consistent with the others on this platform」 是 OpenBSD 维护者向 Linux 上游贡献 arm64 DTS 修复的姿态 `<!-- ROW_MINE: lkml.messages.4094772 -->`
- 【Linux社区】2016年10月 Adrian Chadd(adrian@freebsd.org) 在「Re: Question on kzalloc and GFP_DMA32」串中 以 FreeBSD 开发者身份批评 ath10k DMA 用法「the way ath10k is getting physically contig bounce-buffer style memory after a kzalloc is really designed for small, ephemeral allocations」，是 BSD 开发者以跨平台经验审视 Linux DMA 惯例的证据 `<!-- ROW_MINE: lkml.messages.6705033 -->`

## 212.4 【Linux社区】BSD 治理立场与 Linus 治理张力（1 条）

- 【Linux社区】2024年5月14日 Theo de Raadt(deraadt@openbsd.org) 在「Re: [PATCH v10 0/5] Introduce mseal」串中 回击 Linus 的人身攻击 「(Linus, don't be a jerk)」 是 BSD 领袖与 Linux 领袖个人冲突升级的标志性时刻 `<!-- ROW_MINE: lkml.messages.3818946 -->`

## 212.5 【Linux社区】附录：筛查、去重与精度对比

- **来源**：lkml.messages 中 from_email 含 @freebsd.org / @openbsd.org / @netbsd.org 的 BSD 人物邮件
- **BSD 人物 lkml 邮件总量**：248 封（@freebsd.org 183 + @openbsd.org 62 + @netbsd.org 3）
- **去重后候选**：231 封（vs 205-211 章 lkml ROW_MINE 去重）
- **outline_worthy**：93 条（strong 54 + moderate 29）
- **内容去重后入纲**：83 条（剔除 10 条同补丁系列 v1/v2/RESEND）
- **precision**：83/231 = 35.9%

### 212.5.1 来源分布（83 条入纲，按发件人）

- deraadt@openbsd.org: 39
- kettenis@openbsd.org: 10
- adrian@freebsd.org: 8
- rwatson@freebsd.org: 4
- beck@openbsd.org: 4
- kevans@freebsd.org: 4
- manu@freebsd.org: 4
- emaste@freebsd.org: 3
- jhb@freebsd.org: 3
- henning@openbsd.org: 1
- reyk@openbsd.org: 1
- gilles@openbsd.org: 1
- jkim@freebsd.org: 1

### 212.5.2 年份分布（83 条入纲）

- None: 83

### 212.5.3 判定分层（93 候选 → 83 入纲）

| 层级 | 数量 | 说明 |
|---|---|---|
| outline_worthy | 93 | 5 路读手逐封判定强/中张力的候选 |
| strong | 54 | BSD 身份直接构成张力（反向移植、许可证双许可、治理立场） |
| moderate | 29 | BSD 身份与内容相关但非核心（风格 API、血统工具） |
| 内容去重 | -10 | subagent 标记的同补丁系列 v1/v2/RESEND 变体，仅保留主体 |
| **最终入纲** | **83** | 212 章最终条目数 |

### 212.5.4 精度对比（205-212 章全景）

| 分层 | precision | 样本 → 入纲 |
|---|---|---|
| BSD 人物反向追溯（去内容重复） | 35.9% | 231 → 83 |
| historical_claims 反向张力 | 68.4% | 19 → 13 |
| BSD 发展列表硬过滤 | 61.7% | 128 → 79 |
| BSD 人物反向追溯（含内容重复） | 40.3% | 231 → 93 |
| tier A 硬过滤精选 | 48.2% | 218 → 104 |
| ZFS on Linux 专题 | 19.0% | 21 → 4 |
| fig_B1 层 | 13.5% | 222 → 30 |
| tier B 硬过滤精选 | 11.0% | 200 → 22 |

### 212.5.5 已知盲区

- BSD 域名仅覆盖 @freebsd.org / @openbsd.org / @netbsd.org，未含 @dragonflybsd.org / @bsdsystems.com / @warpmail.com 等 BSD 人物常用邮箱
- BSD 人物在 lkml 用非 BSD 域名（如 @gmail.com、@kernel.org）的邮件未覆盖
- 本批次 231 行 5 路读手覆盖全部，但 138 条 false 主体为 Suleiman Souhlal 的 memcg/slab v2 补丁集与 Emmanuel Vadot 的 allwinner/sunxi DTS 补丁集（BSD 身份仅存于签名行或邮箱后缀，与内容无关）
- P2（systemd-devel 接入）待确认数据源是否入库
