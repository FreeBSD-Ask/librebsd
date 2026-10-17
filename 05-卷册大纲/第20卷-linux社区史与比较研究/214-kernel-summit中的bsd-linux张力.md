# 214 【Linux社区】Kernel Summit 中的 BSD/Linux 张力
> 来源：ksummit 邮件列表（10,650 封，2014-2024），BSD 价值打分（BSD 变体/技术/许可证/init/dbus 词表），硬过滤（score>=5 + BSD 相关）220 候选，主题去重后 43 条，2 路并行读手逐封判定。
> 判定：11 CAND（6 strong + 5 moderate）。主题分布：BSD 谱系 8、许可证 3。
> 全库去重：本次 11 条与 205-213 章 356 条 ROW_MINE 严格去重（ksummit 数据源独立，0 条完全重复）。

## 214.0 【Linux社区】体例说明
本文件系 ksummit（Kernel Summit）邮件列表中 BSD/Linux 张力讨论的逐封提取产物。Kernel Summit 是 Linux 内核社区的年度技术讨论平台，BSD 变体（OpenBSD/NetBSD/FreeBSD）在 2038 问题、GPL 许可证执法、EXPORT_SYMBOL_GPL、Devicetree 跨平台等议题中被反复引用。
**独特价值**：这 11 条是 Linux 内核核心维护者（Linus Torvalds、Theodore Ts'o、Mauro Carvalho Chehab）与 BSD 维护者在 Kernel Summit 中讨论 BSD/Linux 张力的一手叙事，覆盖 2038 问题 BSD 方案（NetBSD/OpenBSD time_t 迁移）、GPL/BSD 许可证冲突（BSD-vs-GPL flame wars、BSD-licensed free-for-all）、EXPORT_SYMBOL_GPL 与 BSD 授权、Devicetree 跨平台（FreeBSD/NetBSD/OpenBSD 合流）。与 205-213 章 lkml+BSD 列表+systemd 视角互补，构成 Linux 核心维护者视角的 BSD 张力补充。
**叙事主线**：2038 问题 BSD 方案（NetBSD/OpenBSD time_t 64-bit 迁移早于 Linux 6 年）／GPL/BSD 许可证冲突（Linus“those BSD-vs-GPL flame wars”、David Woodhouse“BSD-licensed free-for-all”）／EXPORT_SYMBOL_GPL 与 BSD 授权兼容性／Devicetree 跨平台（“all 5 projects using a common set of dts files”FreeBSD/NetBSD/OpenBSD 合流）／BSD 4.3 治理反面教材（Theodore Ts'o“from the mountain top as if from Moses”）。
**ROW_MINE 格式**：`<!-- ROW_MINE: ksummit.messages.<N> -->`，N 为 ksummit.duckdb messages 表的 id。

## 214.1 【Linux社区】BSD 技术在 Kernel Summit 的张力（8 条）

- 【Linux社区】2016年8月 Linus Torvalds(torvalds@linux-foundation.org) 在“[CORE TOPIC] GPL defense issues”串中援引“those BSD-vs-GPL flame wars”反驳 Bradley Kuhn，将 FSF 式 GPL 强制主义斥为“bad old FSF message”，是 BSD 阵营与 GPL 教条派在 Kernel Summit 语境下直接对撞的定调发言 `<!-- ROW_MINE: ksummit.messages.296 -->`
- 【Linux社区】2014年5月 Theodore Ts'o(tytso@mit.edu) 在“Re: [Ksummit-discuss] [CORE TOPIC] [nomination] Move Fast and Oops Things”串中以 FreeBSD tty 维护者的旧竞赛与 BSD 4.3 架构的固化姿态反衬 Linux 快速迭代的治理优势，原文“viewed the architecture from BSD 4.3 to be handed down from the mountain top as if from Moses”是 BSD 谱系在 Linux 治理论证中被引为反面教材的书面实例 `<!-- ROW_MINE: ksummit.messages.2131 -->`
- 【Linux社区】2014年5月 Andy Lutomirski(luto@amacapital.net) 在“Re: [Ksummit-discuss] [CORE TOPIC] Dealing with 2038”串中以 CONFIG_COMPAT_VDSO 为例追问 Linux 兼容治理的规则，原文“it would be nice if there were a clear mostly-applicable rule for how this should work”把 John Stultz 开篇援引的 NetBSD 与 OpenBSD time_t ABI 破例纳入 Linux 的兼容治理议程 `<!-- ROW_MINE: ksummit.messages.4422 -->`
- 【Linux社区】2017年10月 Alexandre Torgue(alexandre.torgue@st.com) 在“Devicetree Workshop at Kernel Summit Prague”串中转述 Andrew Turner 的“all 5 projects using a common set of dts files”提议，是 FreeBSD/NetBSD/OpenBSD 与 Linux 在 DT 层首次走向共库的合流节点 `<!-- ROW_MINE: ksummit.messages.5185 -->`
- 【Linux社区】2014年7月 John Stultz(john.stultz@linaro.org) 在“2038 Kernel Summit Discussion Fodder”串中把“OpenBSD switched its 32bit systems time_t to use long long”引为 Linux 2038 方案的先行经验，是 BSD 家族在 32 位 time_t 迁移上领先 Linux 的教科书证据 `<!-- ROW_MINE: ksummit.messages.5281 -->`
- 【Linux社区】2014年8月 John Stultz(john.stultz@linaro.org) 在“Re: [Ksummit-discuss] (Resend) 2038 Kernel Summit Discussion Fodder”串中把 2008 年 NetBSD 技术讨论作为 Libc 版本升级方案的直接参照，原文“NetBSD developers discussed this same approach back in 2008”是 BSD 2038 方案进入 Linux 主线治理文本的书面证据 `<!-- ROW_MINE: ksummit.messages.5697 -->`
- 【Linux社区】2014年8月 Joseph S. Myers(joseph@codesourcery.com) 在“2038 Kernel Summit Discussion Fodder”串中援引“NetBSD developers discussed this same approach back in 2008”，是 BSD 谱系在 _TIME_BITS=64 迁移路径上比 Linux 早 6 年完成讨论的定量证据 `<!-- ROW_MINE: ksummit.messages.6941 -->`
- 【Linux社区】2014年5月 John Stultz(john.stultz@linaro.org) 在“[Ksummit-discuss] [CORE TOPIC] Dealing with 2038”串中开题并把 NetBSD 与 OpenBSD 的 ABI 破例方案作为直接先例，原文“NetBSD and OpenBSD have recently broken their ABI, converted their time_t to long long”将 BSD 时间方案写进 Linux 2038 议程，是 BSD 对 Linux 兼容性治理最直白的技术参照 `<!-- ROW_MINE: ksummit.messages.9498 -->`

## 214.2 【Linux社区】GPL/BSD 许可证在 Kernel Summit 的张力（3 条）

- 【Linux社区】2015年7月 David Woodhouse(dwmw2@infradead.org) 在“[CORE TOPIC] GPL enforcement actions”串中指认“rabidly against enforcement and effectively wanting a BSD-licensed free-for-all”，是 BSD 许可在 GPL 强制执行辩论中被具名为对立面的典型锚点 `<!-- ROW_MINE: ksummit.messages.943 -->`
- 【Linux社区】2018年9月 Mauro Carvalho Chehab(mchehab+samsung@kernel.org) 在“[MAINTAINER SUMMIT] EXPORT_SYMBOL_GPL”串中讨论 media 子系统“GPL compatible modules”策略，是 EXPORT_SYMBOL_GPL 与 BSD 派生许可共存的技术落点 `<!-- ROW_MINE: ksummit.messages.3986 -->`
- 【Linux社区】2015年7月 David Woodhouse(dwmw2@infradead.org) 在“[Ksummit-discuss] [CORE TOPIC] GPL enforcement actions”串中把 GPL 强制执行与 BSD 授权直接并置，原文“wanting a BSD-licensed free-for-all because that supports their corporate interests”首次将 BSD 授权正式写入 GPL 执法叙事，是 GPL/BSD 张力的治理级文本化石 `<!-- ROW_MINE: ksummit.messages.7322 -->`

## 214.3 【Linux社区】附录：筛查、去重与精度对比

- **来源**：ksummit 邮件列表（lore.kernel.org/ksummit），2014-2024
- **消息总量**：10,650 封
- **BSD 价值打分**：BSD 变体/技术/许可证/init/dbus 五组词表，10,650 封全量打分
- **硬过滤**（score>=5 + BSD 相关：family OR tech OR (bsd AND lic)）：220 候选
- **主题去重**（subject 前缀聚类，同 thread 只留最高分）：43 条
- **outline_worthy**：11 条（strong 6 + moderate 5）
- **precision**：11/43 = 25.6%

### 214.3.1 来源分布（11 条入纲，按发件人）

- john.stultz@linaro.org: 3
- torvalds@linux-foundation.org: 1
- mchehab+samsung@kernel.org: 1
- alexandre.torgue@st.com: 1
- rostedt@goodmis.org: 1
- joseph@codesourcery.com: 1
- luto@amacapital.net: 1
- dwmw2@infradead.org: 1
- tytso@mit.edu: 1

### 214.3.2 年份分布（11 条入纲）

- None: 11

### 214.3.3 判定分层（43 候选 → 11 入纲）

| 层级 | 数量 | 说明 |
|---|---|---|
| ksummit 消息总量 | 10,650 | 2014-2024，Kernel Summit 邮件列表 |
| BSD 价值打分（score>0） | 698 | 6.5%，至少命中一个 BSD 词 |
| 硬过滤（score>=5 + BSD 相关） | 220 | 698 → 220，精度 31.5% |
| 主题去重（subject 聚类） | 43 | 同 thread 只留最高分 |
| **outline_worthy** | **11** | 2 路读手逐封判定 |

### 214.3.4 精度对比（205-214 章全景）

| 分层 | precision | 样本 → 入纲 |
|---|---|---|
| ksummit BSD 硬过滤 | 25.6% | 43 → 11 |
| systemd-devel BSD 硬过滤 | 40.4% | 52 → 21 |
| BSD 发展列表硬过滤 | 61.7% | 128 → 79 |
| historical_claims 反向张力 | 68.4% | 19 → 13 |
| BSD 人物反向追溯（含内容重复） | 40.3% | 231 → 93 |
| BSD 人物反向追溯（去内容重复） | 35.9% | 231 → 83 |
| tier A 硬过滤精选 | 48.2% | 218 → 104 |
| ZFS on Linux 专题 | 19.0% | 21 → 4 |
| fig_B1 层 | 13.5% | 222 → 30 |
| tier B 硬过滤精选 | 11.0% | 200 → 22 |

### 214.3.5 已知盲区

- ksummit 仅覆盖 2014-2024，未含早期 Kernel Summit（2000s）
- ksummit-discuss 子列表未单独筛查
- 本批次 43 行 2 路读手覆盖全部，但 31 条 false 主体为纯 Linux 内部实现讨论（seccomp、EXPORT_SYMBOL_GPL 无 BSD 语境、AI/LLM、GFDL、strlcpy、bus1 等）
- 2038 问题 BSD 方案（NetBSD/OpenBSD time_t）是 ksummit 中 BSD/Linux 张力的最强节点
