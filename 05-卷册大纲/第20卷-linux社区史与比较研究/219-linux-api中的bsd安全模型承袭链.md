# 219 【Linux社区】linux-api 中的 BSD 安全模型承袭链（Capsicum → O_BENEATH → CLONE_FD → Landlock → openat2）

> 来源：linux-api（64,426 封），检索 Capsicum/CLONE_FD/O_BENEATH/LOOKUP_BENEATH/RESOLVE_IN_ROOT/Landlock/openat2 八类安全模型关键词后叠加“正文显式提及 FreeBSD/OpenBSD/NetBSD/4.4BSD”双重过滤，2,521 条主题命中 → 182 条显式 BSD 提及 → 52 条主题去重候选，3 路并行读手逐封判定，25 条 outline_worthy（precision 48.1%），跨章去重后 25 条入纲。
> 判定：25 条入纲。主题分布：capsicum 10、obeneath 4、landlock 3、clone_fd 3、openat2 3、execveat 2。
> 全库去重：本批与 205-218 章已入纲 ROW_MINE 严格比对。

## 219.0 【Linux社区】体例说明
本文件系 linux-api 列表中 BSD 安全模型承袭链的提取产物。与 217 章（BSD 安全创新反向输出的跨列表证据）、216 章（linux-fsdevel BSD 文件系统张力）互补：217 章按主题横切，本章按**承袭时间轴纵切**，追踪同一批 BSD 概念在 Linux 内核中的落地轨迹。
**独特价值**：本章是全库唯一把“BSD 能力模型 → Linux 能力模型”的**谱系证据链**完整串起来的章节。2014 年 David Drysdale 提交的 11 补丁集把 FreeBSD 的 Capsicum 能力权利框架整体移植进 Linux，含权利值定义、`fgetr()`/`sockfd_lookupr()` 权利检查入口、新增 LSM 钩子、`prctl(2)` 强制 `O_BENEATH`，以及连 FreeBSD Foundation 版权头一并移植的手册页——**该移植最终未合入**。但其思想经由三条支线延续：O_BENEATH 路径约束改以 `AT_NO_JUMPS` 过渡、最终在 openat2(5.6) 中以 `RESOLVE_IN_ROOT` 形态落地；CLONE_FD 移植 FreeBSD 的 pdfork 通知机制（未合入）；Landlock(2013 年起，5.13 合入) 明列 Capsicum 为权利集设计来源，是**唯一进入主线的 Capsicum 后代**。
**叙事主线**：2014 Drysdale Capsicum v1/v2（`Adding FreeBSD's Capsicum security framework`）→ 2014 execveat 作为 Capsicum 配套 → 2014 Hellwig 反问 O_BENEATH_ONLY 在 FreeBSD 如何实现 → 2015 O_BENEATH v4 自称 Capsicum 副产物 → 2015 CLONE_FD v2 对齐 FreeBSD pdfork → 2017 AT_NO_JUMPS 引 FreeBSD 先例 → 2018 Landlock v8 权利集对标 Capsicum/XNU Sandbox/Pledge → 2019 openat2 v14/v15 明文记载 `Drysdale's O_BENEATH patchset which was a spin-off of the Capsicum` → 2020 Landlock v14 明列 FreeBSD Capsicum 为灵感 → 2020 close_range 反向流向 FreeBSD。
**合入状态判据**：Capsicum 本体 false、O_BENEATH false、CLONE_FD false、execveat true（FreeBSD 已有）、openat2 true（v5.6）、Landlock true（v5.13）、close_range true（v5.11）。
**ROW_MINE 格式**：`<!-- ROW_MINE: linux-api.messages.<N> -->`，N 为 linux-api.duckdb messages 表 id。

## 219.1 【Linux社区】Capsicum 移植尝试（2014 David Drysdale 移植 FreeBSD 能力框架，未合入）（9 条）

- 【Linux社区】2014年7月 David Drysdale 把 FreeBSD 10.x 权利值定义与结构体移植进内核，“adapted from the FreeBSD 10.x implementation of”　`移植尝试，未合入主线` <!-- ROW_MINE: linux-api.messages.14735 -->
- 【Linux社区】2014年7月 Andy Lutomirski 复审 cap_rights_get 手册页的权利位描述，“Obtain the current Capsicum capability rights for a file descriptor”　`移植尝试，未合入主线` <!-- ROW_MINE: linux-api.messages.22125 -->
- 【Linux社区】2014年7月 David Drysdale 发起第二版移植 RFC，目标是让 Capsicum 跑进内核，“getting the Capsicum framework running in the kernel”　`移植尝试，未合入主线` <!-- ROW_MINE: linux-api.messages.27373 -->
- 【Linux社区】2014年6月 David Drysdale 提交 11 补丁移植 RFC，主张 Linux 需等效能力框架，“It would be good to have equivalent functionality in Linux”　`移植尝试，未合入主线` <!-- ROW_MINE: linux-api.messages.41650 -->
- 【Linux社区】2014年7月 David Drysdale 为 Linux 移植配套编写 Capsicum 权利手册页，“Capsicum capability rights for file descriptors”　`移植尝试，未合入主线` <!-- ROW_MINE: linux-api.messages.42724 -->
- 【Linux社区】2014年6月 David Drysdale 以绕过 Capsicum 下失效的 /proc 为动机补 execveat，“Capsicum is a security framework that has been present in FreeBSD”　`移植尝试，未合入主线` <!-- ROW_MINE: linux-api.messages.46844 -->
- 【Linux社区】2014年6月 David Drysdale 移植 cap_rights_limit 手册页并保留 FreeBSD 版权头，“Copyright (c) 2012-2013 The FreeBSD Foundation”　`移植尝试，未合入主线` <!-- ROW_MINE: linux-api.messages.51226 -->
- 【Linux社区】2014年6月 David Drysdale 声明权利位掩码编码方案直接沿用 FreeBSD 实现，“The encoding scheme is taken from the FreeBSD implementation”　`移植尝试，未合入主线` <!-- ROW_MINE: linux-api.messages.54878 -->
- 【Linux社区】2014年6月 David Drysdale 提交能力权利限制与查询的两个新系统调用，“Note that in FreeBSD 10.x the function of this pair of syscalls”　`移植尝试，未合入主线` <!-- ROW_MINE: linux-api.messages.63949 -->

## 219.2 【Linux社区】O_BENEATH 与受限路径解析（FreeBSD 语义进入 openat，未以原名合入）（4 条）

- 【Linux社区】2014年7月 Christoph Hellwig 反问 O_BENEATH_ONLY 在 FreeBSD 中如何实现，“How is this implemented in FreeBSD?”　`对照讨论，未合入主线` <!-- ROW_MINE: linux-api.messages.15296 -->
- 【Linux社区】2015年8月 David Drysdale 把路径约束独立成 O_BENEATH 标志并标注来源，“of the Capsicum security framework, which is available in FreeBSD 10.x”　`移植尝试，未合入主线` <!-- ROW_MINE: linux-api.messages.72681 -->
- 【Linux社区】2017年5月 Mickaël Salaün 指出 O_BENEATH 出自 FreeBSD 为支持 Capsicum 而讨论，“discussed for FreeBSD to support Capsicum”　`对照讨论，未合入主线` <!-- ROW_MINE: linux-api.messages.53965 -->
- 【Linux社区】2019年11月 Aleksa Sarai 说明 FreeBSD 从 Capsicum 拆出 O_BENEATH 并落地 openat2，“FreeBSD spun out O_BENEATH”　`承袭落地，已合入主线` <!-- ROW_MINE: linux-api.messages.49008 -->

## 219.3 【Linux社区】CLONE_FD 进程生命周期通知（FreeBSD pdfork 移植，未合入）（3 条）

- 【Linux社区】2015年3月 Josh Triplett 对比 Linux CLONE_FD 与 FreeBSD 9.x 的 pdfork，“libqt should be able to use pdfork on FreeBSD and CLONE_FD”　`对照讨论，未合入主线` <!-- ROW_MINE: linux-api.messages.47563 -->
- 【Linux社区】2015年3月 Thiago Macieira 实测 FreeBSD 进程描述符 API 并映射到 clone4，“pdfork: can be emulated with clone4 + CLONE_FD”　`移植尝试，未合入主线` <!-- ROW_MINE: linux-api.messages.50600 -->
- 【Linux社区】2015年3月 Josh Triplett 提交 v2 版 CLONE_FD 以对齐 FreeBSD pdfork 语义，“compatibility with FreeBSD's pdfork”　`移植尝试，未合入主线` <!-- ROW_MINE: linux-api.messages.66020 -->

## 219.4 【Linux社区】Landlock 权利集继承（2016-2021 合入主线，Capsicum 唯一落地后代）（3 条）

- 【Linux社区】2018年2月 Mickaël Salaün 重构文件动作集并对标 Capsicum 与 Pledge 沙箱，“security sandboxes comparable to XNU Sandbox or OpenBSD Pledge”　`承袭落地，已合入主线` <!-- ROW_MINE: linux-api.messages.47470 -->
- 【Linux社区】2018年2月 Andy Lutomirski 评述 Landlock 权利集合的设计灵感来源，“inspiration from the major Linux LSMs and some other access-controls”　`承袭落地，已合入主线` <!-- ROW_MINE: linux-api.messages.60121 -->
- 【Linux社区】2020年2月 Mickaël Salaün 明列 FreeBSD Capsicum 与 OpenBSD Pledge 为灵感，“FreeBSD Capsicum or OpenBSD Pledge/Unveil”　`承袭落地，已合入主线` <!-- ROW_MINE: linux-api.messages.19612 -->

## 219.5 【Linux社区】openat2 与 RESOLVE_IN_ROOT（FreeBSD 路径约束语义的最终落地形态）（3 条）

- 【Linux社区】2019年10月 Aleksa Sarai 在 how.resolve 字段定型 RESOLVE 路径解析标志，“RESOLVE_* path-resolution flags”　`承袭落地，已合入主线` <!-- ROW_MINE: linux-api.messages.12945 -->
- 【Linux社区】2019年11月 Aleksa Sarai 记载 O_BENEATH 补丁集是 Capsicum 的衍生分支，“Drysdale's O_BENEATH patchset[4] which was a spin-off of the Capsicum”　`承袭落地，已合入主线` <!-- ROW_MINE: linux-api.messages.15152 -->
- 【Linux社区】2019年10月 Aleksa Sarai 追溯 RESOLVE_IN_ROOT 源自 Capsicum 衍生补丁集，“O_BENEATH patchset[4] which was a spin-off of the Capsicum”　`承袭落地，已合入主线` <!-- ROW_MINE: linux-api.messages.26735 -->

## 219.6 【Linux社区】附录对照：横向引用、反向流向与词面噪声（3 条）

- 【Linux社区】2014年11月 Andy Lutomirski 把 FreeBSD Capsicum 列为 fd 化进程管理的起点，“the Capsicum stuff from FreeBSD would probably”　`学术引用，未合入主线` <!-- ROW_MINE: linux-api.messages.44615 -->
- 【Linux社区】2020年6月 Christian Brauner 说明 close_range 已由 Linux 首创、FreeBSD 反向跟进，“FreeBSD intends to add the same syscall once we merged it”　`对照讨论，已合入主线` <!-- ROW_MINE: linux-api.messages.24708 -->
- 【Linux社区】2020年6月 Michael Kerrisk 请 Brauner 补写 close_range 手册页并确认 FreeBSD 跟进，“FreeBSD intends to add the same syscall once we merged it”　`对照讨论，已合入主线` <!-- ROW_MINE: linux-api.messages.40653 -->

## 219.7 【Linux社区】附录：筛查、判定与去重情况

- **来源**：linux-api（64,426 封全文检索）
- **搜索词**：Capsicum / cap_rights / fgetr( / sockfd_lookupr / Landlock / O_BENEATH / LOOKUP_BENEATH / RESOLVE_IN_ROOT / CLONE_FD / openat2
- **第一层（主题命中）**：2,521 条（landlock 1304 / execveat 609 / obeneath 322 / capsicum 209 / clone_fd 77）
- **第二层（正文显式提及 BSD 家族）**：182 条——这是本章的关键闸门，剔除 landlock/execveat 常规内核工作中偶提 capsicum 的噪声
- **第三层（主题去重）**：52 条候选
- **3 路并行读手判定**：strong 28 / moderate 15 / false 9
- **outline_worthy**：25 条
- **跨章去重后入纲**：25 条

### 219.7.1 主题分布
- capsicum: 10
- obeneath: 4
- landlock: 3
- clone_fd: 3
- openat2: 3
- execveat: 2

### 219.7.2 合入状态分布
- 未合入: 16
- 已合入: 9

### 219.7.3 年份分布
- 2014: 11
- 2015: 4
- 2017: 1
- 2018: 2
- 2019: 4
- 2020: 3

### 219.7.4 承袭关系图谱

```
FreeBSD Capsicum (2008, Watson)                 FreeBSD pdfork (2008)
        |                                              |
        v                                              v
2014 Drysdale 11-patch port                2015 Triplett CLONE_FD v2
  rights defs / fgetr() / sockfd_lookupr()   pdfork 通知语义逐条映射
  LSM hooks / prctl O_BENEATH                 [未合入主线]
  man-pages 含 FreeBSD Foundation 版权头
  [未合入主线]
        |
        +---> 2014 O_BENEATH_ONLY / 2015 O_BENEATH v4 (自称 Capsicum 副产物)
                  |
                  +---> 2017 AT_NO_JUMPS (引 FreeBSD 先例，Jann Horn TOCTOU)
                  |
                  +---> 2019 openat2 v14/v15
                          |
                          v
                  RESOLVE_IN_ROOT  [已合入 v5.6]  ← FreeBSD 路径约束语义最终落地

        +---> 2016-2021 Landlock LSM (Mickaël Salaün)
                权利集明列 Capsicum / XNU Sandbox / OpenBSD Pledge 为对标
                [已合入 v5.13]  ← Capsicum 唯一进入主线的后代

        +---> 2014 execveat (动机：绕过 Capsicum 模式下不可用的 /proc)  [已合入]
```

### 219.7.5 精度对比

| 分层 | precision | 样本 → 入纲 |
|---|---|---|
| linux-api BSD 承袭链（主题+显式 BSD 双层过滤） | 48.1% | 52 → 25 |
| linux-api BSD 承袭链（仅主题命中口径） | 0.99% | 2,521 → 25 |
| freebsd-hackers GPL+BSD 许可 | 72.7% | 66 → 48 |
| historical_claims 反向张力 | 68.4% | 19 → 13 |
| BSD 发展列表硬过滤 | 61.7% | 128 → 79 |
| tier A 硬过滤精选 | 48.2% | 218 → 104 |
| systemd-devel BSD 硬过滤 | 40.4% | 52 → 21 |
| linux-fsdevel BSD 变体+技术 | 36.5% | 126 → 46 |
| BSD 人物反向追溯 | 35.9% | 184 → 66 |
| ksummit BSD 相关演讲 | 25.6% | 43 → 11 |
| ZFS on Linux 专题 | 19.0% | 21 → 4 |
| BSD 安全跨列表检索 | 9.4% | 138 → 13 |
| linux-mm/scsi/api 技术词面检索 | 0.7% | 150 → 1 |

### 219.7.6 已知盲区与反向流向

- **反向流向（Linux → BSD）**：close_range() 由 Linux 提出、FreeBSD 反向移植（`FreeBSD intends to add the same syscall once we merged it`），本章收录以说明承袭非单向。
- **词面噪声实测**：52 候选中 9 条 false，主要为 ①man page 遗留注释 `4.4BSD`（symlink.7 magic-links）②`MPI3_CONFIG_PAGETYPE_UEFI_BSD` 固件枚举 ③BSD 词面命中落在 4500 字预览截断区之外。
- **bsd_mentions 不可信**：多条候选元数据标 bsd_mentions≥1，但 4500 字预览内零命中，读手按“证据须在可见正文内”原则判 false，未虚标。
- **未覆盖**：OpenBSD pledge/unveil 的 Linux 采纳（seccomp-BPF 替代路线）待深挖；Capsicum 移植失败的具体技术原因（LSM 钩子粒度、文件描述符权利开销）未在本批材料内充分展开。
- **未合入原因**：Capsicum 本体未合入的完整论证链条（维护者具体反对意见）本批仅见 Lutomirski/Paul Moore/Kees Cook 的零散评审，需回到完整线程。

