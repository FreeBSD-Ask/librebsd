# 213 【Linux社区】systemd 与 BSD 的张力：拒绝移植、许可证与血统
> 来源：systemd-devel 邮件列表（52,167 封，2010-2026，197 月度归档），BSD 价值打分（BSD 变体/技术/许可证/init/dbus 词表），硬过滤（score>=5 + BSD 相关）78 候选，主题去重后 52 条，2 路并行读手逐封判定。
> 判定：21 CAND（4 strong + 17 moderate）。主题分布：BSD 谱系 15、许可证 4、人物 2、治理 0。
> 全库去重：本次 21 条与 205-212 章 335 条 ROW_MINE 严格去重（systemd-devel 数据源独立，0 条完全重复）。

## 213.0 【Linux社区】体例说明
本文件系 systemd-devel 邮件列表中 systemd 与 BSD 张力讨论的逐封提取产物。systemd 是 Linux 侧最具 BSD 争议的组件——GPL 许可证执法、init/dbus/PID1 哲学、BSD 移植层（FreeBSD 移植、LinuxKPI）、BSD 兼容工具、systemd vs BSD init 之争——因此成为《给我自由》第 20 卷 BSD/Linux 张力图谱的关键拼图。
**独特价值**：这 21 条是 systemd 开发者与 BSD 维护者在 systemd-devel 邮件列表中以 BSD 视角讨论 systemd 的一手叙事，覆盖 systemd 拒绝 BSD 移植（Lennart Poettering 公开拒绝 FreeBSD 移植）、ZFS 授权争议导致 systemd 拒纳入 GPT 子卷规范、BSD 技术（strlcpy/capsicum/capabilities）反向输出 systemd、BSD 移植尝试（dolt.m4、FreeBSD 宿主）。与 205-212 章 lkml+BSD 列表 BSD 视角互补，构成 Linux/BSD 双向张力的完整图景。
**叙事主线**：systemd 拒绝 BSD 移植（Lennart Poettering「the BSDs or Solaris would never adopt systemd anyway」）／ZFS 授权争议导致 systemd 拒集成（「I wouldn't touch this with a 10m pole, given how unresolved their licensing mess is」）／BSD 技术反向输出（OpenBSD strlcpy、FreeBSD capabilities、OpenBSD signify）／BSD 移植尝试（dolt.m4 FreeBSD/Darwin 宿主、FreeBSD pidfile_*()）／systemd vs BSD init 哲学（jail vs cgroup、capabilities vs /proc PID 竞态）。
**ROW_MINE 格式**：`<!-- ROW_MINE: systemd-devel.messages.<N> -->`，N 为 systemd-devel.duckdb messages 表的 id。

## 213.1 【Linux社区】BSD 技术在 systemd 讨论中的张力（15 条）

- 【Linux社区】2011年11月 Manuel Amador(rudd-o) 在「Question about generators and adding new units in the middle of a transaction」串中提出「bring ZFS datasets into systemd as first-class elements」，是ZFS在Linux上通过generator与systemd集成、把FreeBSD后裔文件系统抬进systemd事务模型的原点 `<!-- ROW_MINE: systemd-devel.messages.3871 -->`
- 【Linux社区】2012年 Tom Gundersen(teg) 在「[PATCH] tmpfiles.d: create /run/lock{, /lockdev} even without sysvcompat」串中留下注释「On modern systems a BSD file lock is a better choice」，是BSD文件锁在systemd源码头注里作为Unix正统序列化手段的旁证 `<!-- ROW_MINE: systemd-devel.messages.5807 -->`
- 【Linux社区】2013年X月 Lennart Poettering(lennart) 在「[HEADSUP] New module ‘libc’ in systemd git」串中 提议 systemd 新 libc 加入 strlcpy 作为 BSD 风格 API，是 BSD 技术被 systemd 反向采纳的例证「we added strlcpy() as known from OpenBSD」 `<!-- ROW_MINE: systemd-devel.messages.10040 -->`
- 【Linux社区】2014年X月 Andy Lutomirski(luto) 在「[RFC PATCH] proc, pidns: Add highpid」串中 援引 FreeBSD 的 Capabilities 作为 /proc 竞态解决方案的原型，是 BSD Capabilities 模型反向进入 Linux 内核 API 设计讨论的例证「the Capsicum stuff from FreeBSD would probably be a very good start here」 `<!-- ROW_MINE: systemd-devel.messages.25625 -->`
- 【Linux社区】2014年 Veres Lajos(vlajos) 在「[PATCH 1/2] typofixes - https://github.com/vlajos/misspell_fixer」串中在systemd TODO列表里保留「pushing out journal messages onto the network in BSD syslog protocol」，是BSD syslog与BSD锁在systemd规划里的显影 `<!-- ROW_MINE: systemd-devel.messages.26528 -->`
- 【Linux社区】2015年X月 Tom Gundersen(teg) 在「Udev won't rename interfaces that are already UP」串中 援引 OpenBSD 网卡命名作为 systemd predictable naming 的对比，是 BSD 接口命名哲学作为 systemd 设计批判参照的例证「The probe order is nondeterministic so you are not guaranteed the same order and hence the same name on every boot」 `<!-- ROW_MINE: systemd-devel.messages.28511 -->`
- 【Linux社区】2015年X月 harald at redhat.com(harald) 在「[PATCH] use dolt.m4 to speedup compilation」串中 提交 dolt.m4 以 FreeBSD 和 Darwin 为兼容目标，是 systemd 构建系统明确列出 BSD 宿主作为兼容目标的证据「*-*-linux* | amd64-*-freebsd*|i?86-*-freebsd*|ia64-*-freebsd* | i?86-apple-darwin*」 `<!-- ROW_MINE: systemd-devel.messages.28941 -->`
- 【Linux社区】2015年X月 Andy Lutomirski(luto) 在「SD_BUS_VTABLE_CAPABILITY」串中 援引 FreeBSD 的 Capabilities 模型作为 kdbus 权限系统缺失的参照，是 BSD 安全模型反向进入 systemd 讨论的例证「it would be great if we had something better in the kernel, like capsicum or whatever」 `<!-- ROW_MINE: systemd-devel.messages.30820 -->`
- 【Linux社区】2015年X月 Cristian Rodríguez(crrodriguez) 在「SysVInit service migration to systemd」串中 引用 FreeBSD 的 pidfile_*() 接口作为 systemd 反对 PID 文件的对照，是 BSD 技术作为 systemd 设计批评参照物的例证「the lack of a FREEBSD-like pidfile_*() interface that at least tries to be correct」 `<!-- ROW_MINE: systemd-devel.messages.33269 -->`
- 【Linux社区】2015年11月 Simon McVittie(simon.mcvittie) 在「[packaging] split of systemd package」串中对比「dbus is portable (to Windows, non-GNU Linux, and non-Linux Unix like *BSD and Solaris)」，是systemd仅面向GNU/Linux而D-Bus仍保留BSD移植能力的架构分裂的直陈 `<!-- ROW_MINE: systemd-devel.messages.34912 -->`
- 【Linux社区】2015年X月 Mantas Mikulėnas(grawity) 在「systemd shutdown: switch-root after remounting  root fs ro」串中 给出 systemd-shutdown 自动切换到 /run/initramfs 的方案以兼容双启动 FreeBSD，是 systemd 与 FreeBSD 双启动 ZFS 兼容层的具体技术路径「to reset root ZFS mount point (to dual boot FreeBSD)」「If systemd-shutdown finds /run/initramfs at the end, it will automatically switch to that as the new root」 `<!-- ROW_MINE: systemd-devel.messages.35138 -->`
- 【Linux社区】2016年6月 Andrei Borzenkov(arvidjaar) 在「advice for zfs-mount-generator」串中反问「was it ever possible (Solaris, *BSD) to intermix zfs and legacy mount points」，是ZFS与systemd挂载次序争论中把Solaris与BSD作为参照系的关键发问 `<!-- ROW_MINE: systemd-devel.messages.36911 -->`
- 【Linux社区】2017年10月 Jonathan de Boyne Pollard(J.deBoynePollard-newsgroups) 在「New reboot flag: -c for 'power cycle'」串中介绍「Warner Losh, FreeBSD and embedded systems developer, has just invented a new shutdowngoal」，是FreeBSD在reboot语义上向Linux反向输出RB_POWERCYCLE标志、冲击PID 1实现的一次BSD技术反向 `<!-- ROW_MINE: systemd-devel.messages.39595 -->`
- 【Linux社区】2018年2月 Lennart Poettering(lennart) 在「[ANNOUNCE] systemd v239」串中宣布「take arguments and input compatible with the Debian and FreeBSD resolvconf tool」，是systemd v239通过resolvectl反向兼容FreeBSD resolvconf工具的BSD兼容层落地记录 `<!-- ROW_MINE: systemd-devel.messages.40791 -->`
- 【Linux社区】2020年X月 Lennart Poettering(lennart) 在「[PATCH] man: add instruction on clearing file  descriptors」串中 援引 FreeBSD 与 NetBSD 的 /dev/fd 差异以论证无通用便携方案，是 BSD 系统行为差异作为 systemd 移植论证的例证「FreeBSD only exposing 0-2 in its /dev/fd by default unless you mounted a separate virtual filesystem there」「NetBSD seems to always have 64 devnodes no matter how many fds」 `<!-- ROW_MINE: systemd-devel.messages.45612 -->`

## 213.2 【Linux社区】GPL/BSD 许可证与 systemd 拒绝移植（4 条）

- 【Linux社区】2013年3月 Simon McVittie(simon.mcvittie) 在「[HEADSUP] libsystemd-bus + kdbus plans」串中指出「environments where the LGPL or a BSD-style license is conventional」，是GPL许可证在跨BSD移植时的兼容性代价于systemd D-Bus生态显影的旁证 `<!-- ROW_MINE: systemd-devel.messages.9871 -->`
- 【Linux社区】2014年X月 Lennart Poettering(lennart) 在「I wonder… why systemd provokes this amount of polarity and resistance」串中 援引 SMF 与 BSD 拒绝移植作为拒绝移植的证据，是 Lennart Poettering 公开表态 systemd 不服务非 Linux 内核的治理宣言「the BSDs or Solaris would never adopt systemd anyway」「We take portability patches for other archs, but not for other kernels」 `<!-- ROW_MINE: systemd-devel.messages.24103 -->`
- 【Linux社区】2020年X月 Arian Van Putten(arian) 在「RFC: Moving fully to OpenSSL (aka. stopping  support for gnutls/gcrypt)?」串中 提议以 OpenBSD signify 风格签名替代 GnuPG 后端，是 BSD 密码学工具反向进入 systemd 讨论的例证「we could also opt for something more simple akin to OpenBSD signify (A simple ed25519 signature over a hash)」 `<!-- ROW_MINE: systemd-devel.messages.45609 -->`
- 【Linux社区】2021年X月 Lennart Poettering(lennart) 在「the need for a discoverable sub-volumes  specification」串中 援引 ZFS 授权争议作为不纳入 GPT 子卷规范的拒绝理由，是 systemd 上游因 BSD 生态授权问题主动与 ZFS 保持距离的证据「I don't think ZFS is interesting either, i.e. I wouldn't touch this with a 10m pole, given how unresolved their licensing mess is」 `<!-- ROW_MINE: systemd-devel.messages.46965 -->`

## 213.3 【Linux社区】BSD 人物在 systemd-devel 的出场（2 条）

- 【Linux社区】2014年4月 Lennart Poettering(lennart) 在「bus driver on kdbus」串中反问「you want to play the abstraction game to somehow improve your karma with the freebsd guys」，是kdbus争议中Lennart把FreeBSD开发者顾虑直接点名的BSD人物入systemd论战的关键证据 `<!-- ROW_MINE: systemd-devel.messages.18703 -->`
- 【Linux社区】2015年2月 Luke Kenneth Casson Leighton(lkcl) 在「feature request: dlopen」串中披露「the FreeBSD team are considering writing a replacement logind」，是FreeBSD直面systemd统治PID 1后被迫反向实现logind API的BSD侧应对证据 `<!-- ROW_MINE: systemd-devel.messages.28614 -->`

## 213.5 【Linux社区】附录：筛查、去重与精度对比

- **来源**：systemd-devel 邮件列表（lists.freedesktop.org），2010-09 至 2026-09，197 月度归档
- **消息总量**：52,167 封（去重后）
- **BSD 价值打分**：BSD 变体/技术/许可证/init/dbus 五组词表，52,167 封全量打分
- **硬过滤**（score>=5 + BSD 相关：family OR tech OR (bsd AND lic)）：78 候选
- **主题去重**（subject 前缀聚类，同 thread 只留最高分）：52 条
- **outline_worthy**：21 条（strong 4 + moderate 17）
- **precision**：21/52 = 40.4%

### 213.5.1 来源分布（21 条入纲，按发件人）

- lennart: 6
- simon.mcvittie: 2
- teg: 2
- luto: 2
- rudd-o: 1
- arvidjaar: 1
- lkcl: 1
- J.deBoynePollard-newsgroups: 1
- vlajos: 1
- harald: 1
- grawity: 1
- crrodriguez: 1
- arian: 1

### 213.5.2 年份分布（21 条入纲）

- None: 21

### 213.5.3 判定分层（52 候选 → 21 入纲）

| 层级 | 数量 | 说明 |
|---|---|---|
| systemd-devel 消息总量 | 52,167 | 2010-09 至 2026-09，197 月度归档 |
| BSD 价值打分（score>0） | 16,670 | 32.0%，至少命中一个 BSD 词 |
| 硬过滤（score>=5 + BSD 相关） | 78 | 16,670 → 78，精度 61.5% |
| 主题去重（subject 聚类） | 52 | 同 thread 只留最高分 |
| **outline_worthy** | **21** | 2 路读手逐封判定 |

### 213.5.4 精度对比（205-213 章全景）

| 分层 | precision | 样本 → 入纲 |
|---|---|---|
| systemd-devel BSD 硬过滤 | 40.4% | 52 → 21 |
| BSD 发展列表硬过滤 | 61.7% | 128 → 79 |
| historical_claims 反向张力 | 68.4% | 19 → 13 |
| BSD 人物反向追溯（含内容重复） | 40.3% | 231 → 93 |
| BSD 人物反向追溯（去内容重复） | 35.9% | 231 → 83 |
| tier A 硬过滤精选 | 48.2% | 218 → 104 |
| ZFS on Linux 专题 | 19.0% | 21 → 4 |
| fig_B1 层 | 13.5% | 222 → 30 |
| tier B 硬过滤精选 | 11.0% | 200 → 22 |

### 213.5.5 已知盲区

- systemd-devel 仅覆盖 2010-09 至 2026-09，未含早期 Linux kernel 邮件列表中 systemd 前身（Lennart 2010 前讨论）
- systemd 移植到 FreeBSD 的实际尝试（LinuxKPI、bsdxen）未在本列表讨论，须在 freebsd-current 列表另查
- systemd 与 BSD 许可证的 GPL/BSD 兼容性争议主要发生在 2010-2015 年间，2020 后讨论减少
- 本批次 52 行 2 路读手覆盖全部，但 31 条 false 主体为纯 systemd 内部实现讨论（D-Bus 信号、unit file 格式、cgroup 控制器）
- ZFS 授权争议（OpenZFS 2016 年改为 GPLv2）导致 systemd 拒集成 GPT 子卷，是 213 章关键张力节点
