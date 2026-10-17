# 218 【Linux社区】netdev 中的 BSD 网络张力与 BSD 许可证落地

> 来源：netdev（1,254,852 封，2002-2026 活跃），BSD 价值打分 72,720 条命中，BSD 变体+技术+has_bsd 过滤后 1,813 封，score≥10 后 297 封，subject 去重后 100 封（top 100 by score），4 路并行读手逐封判定，32 条 outline_worthy（precision 32.0%）。
> 判定：32 CAND。主题分布：许可证 20、技术 6、BSD 谱系 6。
> 全库去重：本次 32 条与 205-217 章 474 条 ROW_MINE 十三处严格去重（0 条完全重复）。

## 218.0 【Linux社区】体例说明
本文件系 netdev 列表中 BSD 网络张力与 BSD 许可证落地的逐封提取产物。与 205-217 章互补，构成《给我自由》第 20 卷 BSD 专题的完整图景。
**独特价值**：这 32 条是 Linux 网络开发者在 netdev 列表中讨论 BSD 网络技术（netmap、KAME、LANDLOCK）被 Linux 采用/移植、BSD 许可证（BSD-2/3-Clause）在内核网络栈的落地、BSD 网络架构（jail、namespace）对 Linux 的启发。**Linux 网络开发者的一手视角**，覆盖 2006-2025 近二十年 BSD 网络技术流入 Linux 的完整链路。
**叙事主线**：2006 Linux network namespace 对标 FreeBSD jail（Serge Hallyn）→2007“Linux stealing our code”之争（Theo de Raadt、Adrian Bunk）→2007 KAME altq 去广告条款构成 GPL 同意（Jamie Lokier）→2007 ath5k 从 FreeBSD 回流被剥成 GPL-only（Jon Smirl）→2013 netmap 进 Linux staging（Stephen Hemminger，“originally developed on FreeBSD”）→2014 netmap VALE pipes（Luigi Rizzo）→2016-2019 Landlock LSM 对标 Capsicum/pledge（Mickaël Salaün）→2018 libbpf 双授权 LGPL OR BSD-2-Clause→2019 Codel/FQ/FQ-Codel BSD-3-Clause→2023 ynl GPL-2.0 OR BSD-3-Clause→2025 pcs-lynx BSD-3-Clause 争议
**ROW_MINE 格式**：`<!-- ROW_MINE: netdev.messages.<N> -->`，N 为消息 id。

## 218.1 【Linux社区】BSD 网络技术反向输出（6 条）

- 【Linux社区】2006年4月 作者 Serge E. Hallyn 在“Re: [RFC] network namespaces”中 讨论网络命名空间的完全隔离方案，“完全分离命名空间以支持 VPN 与进程组迁移”是 FreeBSD jail 隔离语义被移植为 Linux network namespace 的原始设计争辩 `<!-- ROW_MINE: netdev.messages.8341775 -->`
- 【Linux社区】2013年4月 Stephen Hemminger 在“[RFC 2/2] ixgbe: netmap support”中 将 netmap 支持直接移植进 Intel ixgbe 驱动，“originally developed on FreeBSD”是 BSD 网络技术被 Linux 驱动采纳的直接证据 `<!-- ROW_MINE: netdev.messages.8208102 -->`
- 【Linux社区】2013年3月 Stephen Hemminger 在“[RFC 1/2] netmap: infrastructure (in staging)”中 将 Luigi Rizzo 源自 FreeBSD 的 netmap 框架移植进 Linux staging，“all the BSD ugliness”是 BSD 网络技术进入 Linux 网络栈时被显式承认的技术来源 `<!-- ROW_MINE: netdev.messages.8308463 -->`
- 【Linux社区】2014年2月 作者 Luigi Rizzo 在“netmap, VALE and netmap pipes”中 公布 netmap/VALE 与 netmap pipes 的代码库与性能数据，“FreeBSD 与 Linux 上同等功能与性能运行”是 BSD 零拷贝网络加速栈向 Linux 反向移植的自证 `<!-- ROW_MINE: netdev.messages.8248700 -->`
- 【Linux社区】2014年2月 作者 Luigi Rizzo 在“Re: netmap, VALE and netmap pipes”中 回复华为工程师关于 pkt-gen 用法并解释端口分组，“按 basename 分组 NIC/VALE 端口与 netmap pipes 共享内存以实现零拷贝”是 netmap 跨双栈核心机制的说明 `<!-- ROW_MINE: netdev.messages.8423122 -->`
- 【Linux社区】2018年2月 Mickaël Salaün 在“Re: [PATCH bpf-next v8 00/11] Landlock LSM: Toward unprivileged sandboxing”中 说明 Landlock 文件操作集借鉴 BSD Capsicum 能力模型，“XNU Sandbox or OpenBSD Pledge”是 BSD 谱系沙箱设计的对标锚点 `<!-- ROW_MINE: netdev.messages.8777997 -->`

## 218.2 【Linux社区】BSD 许可证在 Linux 网络栈的落地（20 条）

- 【Linux社区】2007年9月 Adrian Bunk 在“Linux 窃取我们代码之争”讨论中 反驳 Jason Dixon 关于 BSD 许可证被随意删除的指控，“Once the grantor (Reyk) releases his code under that license, it must remain”成为 BSD 派生代码权利的核心表述 `<!-- ROW_MINE: netdev.messages.8167541 -->`
- 【Linux社区】2007年9月 Constantine Murenin 在“Re: Fwd: That whole "Linux stealing our code" thing”中 就 Theo de Raadt 对 ath(4) 代码改为 GPL-only 的指控与 Adrian Bunk 辩论，“accusations of people breaking the law”是 BSD 阵营指控 Linux 违反 BSD 许可证的标志性现场 `<!-- ROW_MINE: netdev.messages.8191922 -->`
- 【Linux社区】2017年 Jie Deng 在“[PATCH net-next 1/2] net: dwc-xlgmac: declaration of dual license in headers”中 将 Synopsys dwc-xlgmac 驱动头文件声明改为 GPL 或 BSD 双授权，“dual-licensed ... GPL or BSD license”是 BSD 许可证在商用以太网驱动中的落地 `<!-- ROW_MINE: netdev.messages.8015345 -->`
- 【Linux社区】2018年 Alexei Starovoitov 在“[PATCH bpf-next] libbpf: relicense libbpf as LGPL-2.1 OR BSD-2-Clause”中 将 libbpf 由 LGPL-2.1 单一授权改为 LGPL-2.1 或 BSD-2-Clause 双授权，“BSD-2 is compatible with Apache2”是 BSD 许可证打通 Apache2 生态的动因 `<!-- ROW_MINE: netdev.messages.8579990 -->`
- 【Linux社区】2018年 Leon Romanovsky 在“mlx5 SRQ 许可证对齐”补丁中将 OpenIB BSD 声明压缩为 SPDX 标签，“GPL-2.0 OR Linux-OpenIB”是 RDMA/InfiniBand 进入 Linux 的历史授权入口 `<!-- ROW_MINE: netdev.messages.8649013 -->`
- 【Linux社区】2018年 Jakub Kicinski 在“[PATCH bpf-next 3/3] tools: bpftool: dual license all files”中 将 bpftool 全部文件统一为 GPL-2.0-only 或 BSD-2-Clause 双授权，“dual licensed under GPLv2 and BSD-2-Clause”是 BSD 许可证在 Linux 网络工具链的规模化落地 `<!-- ROW_MINE: netdev.messages.8787984 -->`
- 【Linux社区】2019年8月 Daniel Borkmann 在“libbpf bpf_helpers.h 重新授权”邮件中 回应为何不用 Apache-2.0，“The Apache-2.0 is not GPL2 compatible”是 libbpf 在 LGPL-2.1 OR BSD-2-Clause 之间选择 BSD 的根本理由 `<!-- ROW_MINE: netdev.messages.8717333 -->`
- 【Linux社区】2019年8月 Thomas Gleixner 在“bpftool 许可证混乱清理”补丁中指出 bpftool 从 iproute2 引入时误留 GPL boilerplate 与 BSD-2-Clause SPDX 冲突，“json_writer: add SPDX Identifier (GPL-2/BSD-2)”是 iproute2 的原始授权意图 `<!-- ROW_MINE: netdev.messages.8720547 -->`
- 【Linux社区】2020年 Alexander Lobakin 在“[PATCH net-next 1/6] net: qed: correct existing SPDX tags”中 将 QED 驱动 SPDX 标签修正为 GPL-2.0-only 或 BSD-3-Clause，“dual licensed under GPL-2.0/BSD-3-Clause”确认 BSD-3-Clause 在 Marvell 网驱动中的正式落地 `<!-- ROW_MINE: netdev.messages.8677256 -->`
- 【Linux社区】2021年11月 Quentin Monnet 在“bpftool Makefile 与 .gitignore SPDX 修正”补丁中 指出 bpftool 在 commit 907b22365115 已被全量改为“GPLv2 and BSD-2-Clause”双授权，“skipped at the time”的 Makefile 需要补上 BSD-2-Clause 标签 `<!-- ROW_MINE: netdev.messages.8913859 -->`
- 【Linux社区】2023年 Stefan Wahren 在“qca_7k 驱动 BSD 样板替换”补丁中将 BSD-2-Clause 声明替换为 SPDX 标签，“GPL-2.0 OR BSD-2-Clause”是 Qualcomm 网卡驱动进入 Linux 的双授权标准 `<!-- ROW_MINE: netdev.messages.8827397 -->`
- 【Linux社区】2023年3月 Chuck Lever III 在“net/handshake NETLINK 服务补丁”中 指出 GPL 规范派生的代码不能贴 BSD-3 标签，“code and spec licenses have to match”是 Netlink YAML 规范体系的授权底线 `<!-- ROW_MINE: netdev.messages.8835969 -->`
- 【Linux社区】2023年 Stephen Hemminger 在“iproute2 tc codel/fq SPDX 替换”补丁中将 Codel 与 FQ 算法整段 BSD-3-Clause 样板压缩为“GPL-2.0 OR BSD-3-Clause”SPDX 标签，“These algorithms are dual licensed”是 BSD 在网络 QoS 算法中落地的标杆 `<!-- ROW_MINE: netdev.messages.8845122 -->`
- 【Linux社区】2023年5月 作者 Richard Fontana 在“Re: [PATCH v2 09/10] udf: Replace license notice with SPDX identifier”中 反对把 ecma_167.h 标为 BSD-2-Clause，“这既不是 BSD-2-Clause，最接近的 SPDX 可能是 BSD-Source-Code”是 BSD 系许可证 SPDX 标签精确性的典型纠错 `<!-- ROW_MINE: netdev.messages.8900043 -->`
- 【Linux社区】2023年4月 Jakub Kicinski 在“[PATCH net 2/3] ynl: broaden the license even more”中 将 ynl 全部规范与生成代码的 SPDX 标签统一为 GPL-2.0（含 Linux-syscall-note）或 BSD-3-Clause，“license match everywhere”是 BSD-3-Clause 在 netlink 规范层落地一致化的标志 `<!-- ROW_MINE: netdev.messages.8909812 -->`
- 【Linux社区】2023年3月 Jakub Kicinski 在“[PATCH net] ynl: re-license uniformly under GPL-2.0 OR BSD-3-Clause”中 将 ynl 全部规范统一重授权为 GPL-2.0 OR BSD-3-Clause，“full BSD freedom while fulfilling ... GPL expectations”是 BSD 许可证在内核规范层落地的代表性表述 `<!-- ROW_MINE: netdev.messages.8952279 -->`
- 【Linux社区】2023年3月 作者 Jakub Kicinski 在“[PATCH net 3/3] ynl: make the tooling check the license”中 让 YNL 生成器读取并校验 spec 的 SPDX 标签，“GPL-2.0 WITH Linux-syscall-note OR BSD-3-Clause”是 BSD 双重许可在 net-next 工具链中被机器强制执行的形态 `<!-- ROW_MINE: netdev.messages.8990578 -->`
- 【Linux社区】2025年5月 作者 Vladimir Oltean 在“Re: [net-next PATCH v3 05/11] net: pcs: lynx”中 质疑 Sean Anderson 把 pcs-lynx 从 (GPL-2.0+ OR BSD-3-Clause) 改为 GPL-2.0+，“不允许他人选择 BSD-3-Clause 分支”是 BSD 双重许可下贡献者单方收窄许可范围的争议 `<!-- ROW_MINE: netdev.messages.9097259 -->`
- 【Linux社区】2025年7月 Kuniyuki Iwashima 在“Re: [PATCH net-next v12 14/15] net: homa: create homa_plumbing.c”中 指出 HOMAOPL 模块以 BSD-2-Clause + GPL-2.0 双许可证声明入树，“homa_plumbing.c”是 John Ousterhout 从斯坦福带入 Linux 网络的 BSD-2-Clause 落点 `<!-- ROW_MINE: netdev.messages.9193855 -->`
- 【Linux社区】2026年 Tim Bird 在“RE: [PATCH] tipc: Add SPDX id lines to source files”中 反驳 TIPC 原许可仅为 GPL-2.0 的说法，“Per Lindon”2006 年 1 月以 BSD-3-Clause 引入代码并在 commit 9ea1fd3c1a15 追加 GPL 备选条款 `<!-- ROW_MINE: netdev.messages.9231558 -->`

## 218.3 【Linux社区】BSD 网络谱系与 Linux 张力（6 条）

- 【Linux社区】2004年6月 Jamie Lokier 在“Re: [PATCH]: altq HFSC port”中 论证作者放弃广告条款即构成同意纳入 GPL 作品，“altq_hfsc.c”是 KAME 优先级队列调度器入 Linux 的许可依据 `<!-- ROW_MINE: netdev.messages.8146127 -->`
- 【Linux社区】2006年6月 Brian F. G. Bidulock 在“Re: [RFC/PATCH 1/2] in-kernel sockets API”中 论证 EXPORT_SYMBOL_GPL 不应作为一般政策强加于非衍生作品，“Linux NET4”被点名为源自 BSD 4.4-Lite 老 BSD 许可证的疑似衍生作品 `<!-- ROW_MINE: netdev.messages.8291125 -->`
- 【Linux社区】2007年8月 作者 Constantine A. Murenin 在“Fwd: That whole "Linux stealing our code" thing”中 转发 Theo de Raadt 对 Linux 社区删改 BSD 许可草案的法律意见，“双重许可文件永远保持双重许可”是 BSD 阵营对 Linux 单方剥离 BSD 许可证分支的正面反击 `<!-- ROW_MINE: netdev.messages.8240632 -->`
- 【Linux社区】2007年8月 Jon Smirl 在“Re: [PATCH 4/5] Net: ath5k, license is GPLv2”中 追问 ath5k 从 BSD 导入后被剥离 BSD 许可再回流的合法性，“Ath5K code”是 BSD 与 GPL 双向流动争议的现场 `<!-- ROW_MINE: netdev.messages.8374213 -->`
- 【Linux社区】2016年 Mickaël Salaün 在“Landlock LSM v4 RFC”中将 Landlock 定位为“allow any process including unprivileged ones to create powerful security sandboxes comparable to the OpenBSD Pledge”，是 BSD 沙箱思想进入 Linux LSM 的起点 `<!-- ROW_MINE: netdev.messages.8058206 -->`
- 【Linux社区】2019年 Mickaël Salaün 在“Landlock LSM v13”补丁说明中 将 Landlock 的安全沙箱目标明确对标“FreeBSD Capsicum or OpenBSD Pledge”，“could be implemented with Landlock”是 BSD 能力机制在 Linux LSM 中的移植承诺 `<!-- ROW_MINE: netdev.messages.8760614 -->`

## 218.4 【Linux社区】附录：筛查与去重情况

- **来源**：netdev（1,254,852 封）
- **BSD 价值打分**：72,720 条命中（has_bsd & score≥5）
- **BSD 变体+技术+has_bsd & score≥10**：1,813 封
- **subject 去重后**：297 封
- **top 100 by score**：100 封
- **outline_worthy**：32 条（strong 27 + moderate 5）
- **precision**：32/100 = 32.0%

### 218.4.1 年份分布（32 条入纲）

- 2004: 1
- 2006: 2
- 2007: 4
- 2013: 2
- 2014: 2
- 2016: 1
- 2017: 1
- 2018: 4
- 2019: 3
- 2020: 1
- 2021: 1
- 2023: 7
- 2025: 2
- 2026: 1

### 218.4.2 判定分布

- strong: 27
- moderate: 5

### 218.4.3 精度对比

| 分层 | precision | 样本 → 入纲 |
|---|---|---|
| netdev BSD 网络技术+许可证 | 32.0% | 100 → 32 |
| freebsd-hackers GPL+BSD 许可 | 72.7% | 66 → 48 |
| BSD 发展列表硬过滤 | 61.7% | 128 → 79 |
| historical_claims 反向张力 | 68.4% | 19 → 13 |
| tier A 硬过滤精选 | 48.2% | 218 → 104 |
| systemd-devel BSD 硬过滤 | 40.4% | 52 → 21 |
| linux-fsdevel BSD 变体+技术 | 36.5% | 126 → 46 |
| BSD 人物反向追溯 | 35.9% | 184 → 66 |
| ksummit BSD 相关演讲 | 25.6% | 43 → 11 |
| ZFS on Linux 专题 | 19.0% | 21 → 4 |
| BSD 安全跨列表检索 | 9.4% | 138 → 13 |
| fig_B1 层 | 13.5% | 222 → 30 |
| tier B 硬过滤精选 | 11% | 200 → 22 |

### 218.4.4 已知盲区

- netmap 后续维护（2015+）未完全覆盖
- BSD 网络协议栈（KAME IPv6）的完整移植链待深挖
- Linux 网络命名空间与 FreeBSD jail 的完整对照待扩展
- BSD 安全创新反向输出已在 217 章覆盖
