# 208 【Linux社区】LKML 中的 BSD：技术承袭续篇（tier B 精选）
> 来源：lkml tier B 19,038 封候选，硬过滤（body BSD 关键字 total >= 3 且 family >= 1 或 tech >= 1 + 非 relay/dup + 非 bitkeeper 噪声 + 非纯 GPL）后 367 封，二次复核（排除 patch_low_fam/family_lt2/bot）后 338 封，主题去重（subject 前缀只留 1 条）后 226 封，top 200 by total_bsd 分 10 路并行读手，22 条 outline_worthy（precision 11%）。
> 判定：22 CAND。主题分布：BSD 技术承袭 18（入本章）、许可证 2、治理 2。
> 全库去重：本次 22 条与 historical_claims 已入库 19 条 lkml、dslinux_keywords.hits 8141 lkml 基座、205/206/207 章 134 条 ROW_MINE 四处严格去重（0 条 205.x/206.x/207.x 完全重复）。

## 208.0 【Linux社区】体例说明
本文件系 lkml tier B 精选 200 封中 BSD 技术承袭主线的 22 封逐封提取，采用**单行摘要体例**（丙型）。与 206 章（tier A BSD 技术承袭 80 条）互补，与 207 章（许可证/人物/治理 24 条）互补。
**主题分组依据**：按 body 中 BSD 技术名（strlcpy / kqueue / dtrace / Capsicum / disklabel / softupdates / ath / EtherIP / libata / DTS 等）自动单桶归类（每条只归一个主题，按 dtrace > capsicum > KAME > strlcpy > kqueue > arc4random > close_range > 守护进程 > IP_PORTRANGE > 其他的优先级）。
**与 206 章互补**：206 章是 tier A 精选（precision 48.2%）的 BSD 技术承袭 80 条，涵盖 ath9k/kqueue/epoll/EtherIP/i8042/strlcpy/Capsicum 等；本章是 tier B 精选（precision 11%）的 22 条，补充 dtrace 系列（6 条）、capsicum 系列（3 条）、KAME 系列（2 条）等 206 章未深度覆盖的 BSD 技术脉络。
**已知盲区**：tier B 之外 tier C 未启动；BSD 家族名直接命中（bsd_variant_core）子集尚未纳入；bsdisdying 梗在 comp.unix.bsd.misc 而非 lkml。

## 208.1 【Linux社区】dtrace 与内核追踪

- 【Linux社区】2014年7月 Alexei Starovoitov(ast@plumgrid.com) 在「Re: [PATCH RFC v3 net-next 3/3] samples: bpf: eBPF dropmon example in C」串中 追问「I thought dtrace printf are also happening from the kernel」以厘清 eBPF 与 dtrace 的内核态/用户态分工，是 Linux eBPF 生态主动向 BSD dtrace 谱系寻求技术参照的实例 `<!-- ROW_MINE: lkml.messages.5612946 -->`
- 【Linux社区】2014年4月 Masami Hiramatsu(masami.hiramatsu.pt@hitachi.com) 在「Re: [PATCH 14/28] ktap: add runtime/kp_events.[c|h]」串中 以「On the performance overhead of dynamic tracing tools(ktap/stap/dtrace)」把 ktap/stap/dtrace 并列作为动态追踪工具对比集，是 Linux 追踪工具生态把 BSD dtrace 作为合法性与基准参照的实例 `<!-- ROW_MINE: lkml.messages.5898684 -->`
- 【Linux社区】2005年7月 Tom Zanussi(zanussi@us.ibm.com) 在「Re: Merging relayfs?」串中援引「DTrace takes this to the extreme and does everything in the kernel」反驳 relayfs 内核聚合策略，是 Linux relayfs 设计讨论中以 BSD DTrace 为参照系的第一手技术对照 `<!-- ROW_MINE: lkml.messages.1638913 -->`
- 【Linux社区】2008年7月 James Bottomley(james.bottomley@hansenpartnership.com) 在「[RFC] simple dprobe like markers for the kernel」串中提出 dprobe 补丁并论证现有 marker 因「the way they drop stubbable calling points」比 dtrace 笨重，是 Linux 轻量内核探针 RFC 明确以 BSD dtrace 为设计动机 `<!-- ROW_MINE: lkml.messages.2213916 -->`
- 【Linux社区】2021年9月 Kees Cook(keescook@chromium.org) 在「[PATCH v5] kallsyms: new /proc/kallmodsyms with builtin modules」串中认可「We have a long-term consumer in DTrace」的诉求，是 DTrace 作为长期消费者被写入 Linux 内核 kallmodsyms 新 API 的设计依据 `<!-- ROW_MINE: lkml.messages.2693116 -->`
- 【Linux社区】2023年7月 Kris Van Hees(kris.van.hees@oracle.com) 在「[PATCH v2] scripts/link-vmlinux.sh: Add alias to duplicate symbols for kallsyms」串中说明「DTrace supports arbitrary address probing based on an offset from a symbol」，是 DTrace 探测能力对 Linux kallsyms 符号别名补丁的直接技术论证 `<!-- ROW_MINE: lkml.messages.3653601 -->`

## 208.2 【Linux社区】capsicum 能力模型

- 2014年7月 Andy Lutomirski(luto@amacapital.net) 在「Re: [PATCH 11/11] seccomp: Add tgid and tid into seccomp_data」串中主导 seccomp PID 限制语义设计，全邮件 capsicum 命中 2 次显示 FreeBSD Capsicum 能力模型是讨论中 BSD 侧的外部技术参照 `<!-- ROW_MINE: lkml.messages.5704369 -->`
- 【Linux社区】2014年7月 Loganaden Velvindron(loganaden@gmail.com) 在「Re: [PATCH 01/11] fs: add O_BENEATH_ONLY flag to openat(2)」串中 就 David Drysdale 移植 FreeBSD Capsicum 到 Linux 一事表态 「I would very like to see capsicum integrated into mainline」，是 BSD 派生安全沙箱向 Linux 内核治理渗透的路径证词 `<!-- ROW_MINE: lkml.messages.5817879 -->`
- 【Linux社区】2015年9月 Serge E. Hallyn(serge@hallyn.com) 在「Re: RFC: fsyscall」串中引用 Eric Biederman 的 capsicum 类比并提出『let's say capsicum-based』，是 FreeBSD Capsicum 能力机制在 Linux 系统调用设计评审中被直接援引的实例 `<!-- ROW_MINE: lkml.messages.6119678 -->`

## 208.3 【Linux社区】KAME 与 IPv6/IPsec

- 【Linux社区】2003年2月 YOSHIFUJI Hideaki / 吉藤英明 (yoshfuji@linux-ipv6.org) 在「Re: [PATCH] IPv6: Privacy Extensions for Stateless Address Autoconfiguration in IPv6」串中延续 David S. Miller 关于「USAGI itself uses KAME implementation」的说明并提交 2.4.x 隐私扩展补丁，是 Linux IPv6 (USAGI) 承袭 KAME BSD 项目的 BSD 谱系证据 `<!-- ROW_MINE: lkml.messages.1603581 -->`
- 【Linux社区】2003年3月 Derek Atkins(warlord@mit.edu) 在「Re: ipsec-tools 0.1 + kernel 2.5.64」串中回复 bert hubert 说明「I spoke to the KAME people and unfortunately, at least for now, there is no other choice but to fork」，是 BSD KAME 项目成员被 Linux 社区直接征询 Linux 版 IPSec 分叉策略的实例 `<!-- ROW_MINE: lkml.messages.1853779 -->`

## 208.4 【Linux社区】strlcpy 与 API 移植

- 【Linux社区】2003年5月 Adrian Bunk（bunk@fs.tum.de）在「[RFC] [2.5 patch] Change strlcpy and strlcat」串中提议修改 strlcpy 返回语义以简化调用方错误处理，原文「Your API is compatible with *BSD but I'm wondering whether something slightly different might make error handling for callers easier」，是 BSD 系 strlcpy API 进入 Linux 内核 API 设计讨论并被系统性重新审视的一手证据 `<!-- ROW_MINE: lkml.messages.1998312 -->`
- 【Linux社区】2014年4月 Alexey Dobriyan (adobriyan@gmail.com) 在「Re: + lib-stringc-strlcpy-might-read-too-far.patch added to -mm tree」串中要求 Linux 内核 strlcpy 与 OpenBSD 参考实现对齐：「it is better to not diverge from master code」，是 Linux 内核开发者以 OpenBSD 实现为规范源头的 BSD 谱系证据 `<!-- ROW_MINE: lkml.messages.5704582 -->`

## 208.5 【Linux社区】kqueue/kevent 事件机制

- 【Linux社区】2006年11月 Pavel Machek(pavel@ucw.cz) 在「Re: [take22 0/4] kevent: Generic event handling mechanism.」串中反对重写 BSD kqueue 并主张「keeping same/similar userland interface would be nice」，是 Linux kevent 起步期明确支持 BSD kqueue 用户态接口兼容的第一手立场 `<!-- ROW_MINE: lkml.messages.2037722 -->`

## 208.6 【Linux社区】arc4random 与 fork 安全

- 【Linux社区】2017年8月 Colm MacCárthaigh (colm@allcosts.net) 在「Re: [PATCH v2 0/2] mm,fork,security: introduce MADV_WIPEONFORK」串中以「here's how LibreSSL does it」及 OpenBSD arc4random 实现佐证 Linux 引入 fork 感知内存清零机制，是 Linux 内存管理子系统向 OpenBSD 借鉴的 BSD 谱系证据 `<!-- ROW_MINE: lkml.messages.6772794 -->`

## 208.7 【Linux社区】close_range 与 fd 管理

- 2020年6月 Szabolcs Nagy(nsz@port70.net) 在「Re: [PATCH v5 1/3] open: add close_range()」串中与 FreeBSD 维护者 Kyle Evans(kevans@freebsd.org) 就「closefrom bug」与 libc 内部 fd 安全性展开讨论，是 BSD 侧 FreeBSD 维护者对 Linux close_range 新 API 设计的直接技术参与 `<!-- ROW_MINE: lkml.messages.7610019 -->`

## 208.8 【Linux社区】BSD 守护进程惯例

- 【Linux社区】2009年10月 KOSAKI Motohiro(kosaki.motohiro@gmail.com) 在「Re: [PATCH] Added PR_SET_PROCTITLE_AREA option for prctl()」串中 以「Almost setproctitle() heavy user (e.g. sendmail, openssh and some bsd style daemon programs)」举证 PR_SET_PROCTITLE_AREA 提案必要性，是 Linux prctl API 设计对 BSD 用户态守护进程惯例的显式承认 `<!-- ROW_MINE: lkml.messages.2314607 -->`

## 208.9 【Linux社区】IP_PORTRANGE 与端口管理

- 【Linux社区】2011年9月 David Bein(d.bein@f5.com) 在「Re: /proc/sys/net/ipv4/ip_local_reserved_ports」串中提出把 FreeBSD 已有的 IP_PORTRANGE socket option 移植到 Linux，引「This interface was added to FreeBSD maybe 15 years ago」与「in fact faster」，是 FreeBSD 端口范围机制被明确建议移植到 Linux 内核的 BSD 视角技术参考 `<!-- ROW_MINE: lkml.messages.5456543 -->`

## 208.10 【Linux社区】BSD 许可证（续 207.1）

- 【Linux社区】2026年8月 Alexey Dobriyan (adobriyan@gmail.com) 在「Re: [PATCH] selftests/exec: add missing SPDX-License-Identifier tag」串中纠正 Linux selftests 许可标注为「The license is OpenBSD, not ISC」并指向 OpenBSD CV 模板源，是 Linux 内核工具链显性识别 OpenBSD 许可的 BSD 许可证证据 `<!-- ROW_MINE: lkml.messages.4887608 -->`
- 【Linux社区】2019年10月 Jerry Hoemann (jerry.hoemann@hpe.com) 在「Re: [PATCH] uapi: Add the BSD-2-Clause license to ndctl.h」串中同意 Dan Williams 关于「Allow ndctl.h to be licensed with BSD-2-Clause」以支持 FreeBSD 用户态接口移植的建议，是 Linux uapi 层向 BSD 生态开放许可的 BSD 许可证证据 `<!-- ROW_MINE: lkml.messages.7343807 -->`

## 208.11 【Linux社区】BSD 治理智慧（续 207.3）

- 【Linux社区】2006年4月 Stephen Smalley(sds@tycho.nsa.gov) 在「Re: [RFC][PATCH 0/11] security: AppArmor - Overview」串中反问「why not just use existing jail-like or virtualization mechanisms」主张 AppArmor 应让位 VServer/OpenVZ，是 Linux 安全框架 RFC 中直接援引 BSD jail 概念的第一手立场 `<!-- ROW_MINE: lkml.messages.1652706 -->`
- 【Linux社区】2006年5月 Herbert Poetzl(herbert@13thfloor.at) 在「Re: [PATCH 0/9] namespaces: Introduction」串中援引「looking at BSD jails, I see a very simple approach (only one IP, limiting binds)」反驳网络命名空间复杂论，是 Linux namespaces 起步期直接援引 BSD jails 作简化参照 `<!-- ROW_MINE: lkml.messages.1903775 -->`

## 208.12 【Linux社区】附录：读手判定与去重情况

- **本次精选**：200 封（top 200 by total_bsd）
- **outline_worthy**：22 条（strong 5 + moderate 17）
- **入纲**：22 条（去重后）

### 208.12.1 BSD 技术承袭 22 条主题分组

| 主题 | 条数 |
|---|---|
| 208.1 dtrace 与内核追踪 | 6 |
| 208.2 capsicum 能力模型 | 3 |
| 208.3 KAME 与 IPv6/IPsec | 2 |
| 208.4 strlcpy 与 API 移植 | 2 |
| 208.5 kqueue/kevent 事件机制 | 1 |
| 208.6 arc4random 与 fork 安全 | 1 |
| 208.7 close_range 与 fd 管理 | 1 |
| 208.8 BSD 守护进程惯例 | 1 |
| 208.9 IP_PORTRANGE 与端口管理 | 1 |
| 208.10 许可证 | 2 |
| 208.11 治理 | 2 |

### 208.12.2 剔除情况

- **tier B 硬过滤**：19,038 → 367（剔除 used 134 + hc 19 + dk 8141 + relay/dup + total_bsd<3 + family<1+tech<1 + bitkeeper + pure GPL）
- **二次复核**：367 → 338（剔除 patch_low_fam / family_lt2 / bot）
- **主题去重**：338 → 226（同 subject 前缀只留 1 条）
- **精选**：226 → 200（top 200 by total_bsd）
- **读手判定**：200 → 22 outline_worthy（precision 11%）

### 208.12.3 精度对比

| 分层 | precision | 样本 → 入纲 |
|---|---|---|
| fig_B1 层 | 13.5% | 222 → 30 |
| tier A top-100 抽样 | 10% | 100 → 10 |
| tier A 硬过滤精选 | 48.2% | 218 → 104 |
| tier B 硬过滤精选 | 11% | 200 → 22 |

### 208.12.4 tier B anchor 分布（200 精选）

- bsd_tech_adoption: 140（70%）
- bsd_fig_in_lkml: 30（15%）
- (empty): 29（15%）
- GPL_BSD_lic: 1

### 208.12.5 年份分布（22 条入纲）

- 2003: 3
- 2005: 1
- 2006: 3
- 2008: 1
- 2009: 1
- 2011: 1
- 2014: 5
- 2015: 1
- 2017: 1
- 2019: 1
- 2020: 1
- 2021: 1
- 2023: 1
- 2026: 1
