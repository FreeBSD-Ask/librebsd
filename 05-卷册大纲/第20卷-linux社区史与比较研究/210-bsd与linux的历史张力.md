# 210 【Linux社区】BSD 与 Linux 的历史张力：historical_claims 19 封深挖
> 来源：historical_claims 已入库 lkml claim 19 封（BSD/Linux 张力史料预筛选），3 路并行读手深读逐封判定，13 条 outline_worthy（precision 68%）。
> 判定：13 CAND。主题分布：BSD 谱系 10、许可证 3。
> 全库去重：本次 13 条与 205/206/207/208/209 章 160 条 ROW_MINE 五处严格去重（0 条完全重复）。

## 210.0 【Linux社区】体例说明
本文件系 historical_claims 已入库 19 封 BSD/Linux 张力史料的逐封深挖产物。与 205-209 章（基于 tier A/B 分层与 ZFS 专题的 BSD 技术承袭）互补，与它们共同构成《给我自由》第 20 卷 lkml BSD 专题。
**独特价值**：这 19 封是 historical_claims 早期（2020-2024）人工筛选入库的 BSD/Linux 张力史料，覆盖 1998-2024 年 26 年跨度，与 tier A/B pipeline 的算法筛选形成方法论互补。
**叙事主线**：BSD 血统技术被 Linux 采用（SGI gprof、IBM TCP Splice、Acorn RISCiX、McKusick union mount、IPv4 multicast 4.3BSD 兼容、unifdef 4-clause BSD 许可）、BSD 血统 syscall 缺席 Linux（revoke()）、GPL 与 BSD 许可证冲突（SCO Buyout *BSD variant、unifdef 许可重构）。

## 210.1 【Linux社区】BSD 血统技术被 Linux 采用（10 条）

- 【Linux社区】1999年1月 lk(lk@winux.com) 在「TCP Splice alleviates proxy bottleneck」串中 推介 IBM TCP Splice 研究成果，遗憾「The paper says that this is all running on BSDI」，是 BSD 平台承接 BSD 血统关键技术而 Linux 社区错位的张力例证 `<!-- ROW_MINE: lkml.messages.1682177 -->`
- 【Linux社区】2002年10月 Phillip Lougher(phillip@lougher.demon.co.uk) 在「Re: ANNOUNCEMENT: Squashfs released」串中 以前 Acorn 员工身份回忆 RISCiX 压缩文件系统「the underlying filesystem was a fairly vanilla BSD FFS」，是 BSD 文件系统血统被 Linux Squashfs 作者引作技术参照的物证 `<!-- ROW_MINE: lkml.messages.1868978 -->`
- 【Linux社区】2003年9月 Jamie Lokier(jamie@shareable.org) 在「Virtual alias cache coherency results」串中 汇总跨 OS 缓存一致性测试数据，包含 NetBSD、OpenBSD、FreeBSD 结果，是 BSD 作为 Linux 内核 SHMLBA API 语义验证参照出现的例证 `<!-- ROW_MINE: lkml.messages.1625369 -->`
- 【Linux社区】2003年12月 Matthew Wilcox(willy@debian.org) 在「Re: partially encrypted filesystem」串中 复述 Acorn RISCiX 压缩页技术，指出其为「4.3BSD based」并以之论证 Linux page cache 需支持更大 chunk，是 BSD 血统技术经验被 Linux 内核作者直接借用的例证 `<!-- ROW_MINE: lkml.messages.1763181 -->`
- 【Linux社区】2004年8月 Albert Cahalan(albert@users.sf.net) 在「Re: dynamic /dev security hole?」串中 批评 Linux PAM 权限模型，指出「Linux still doesn't have this system call. It's been in BSD since 4.3BSD-Reno」，是 BSD 血统 revoke() 系统调用缺席 Linux 内核、被 lkml 明确点名为安全缺陷的张力例证 `<!-- ROW_MINE: lkml.messages.1724762 -->`
- 【Linux社区】2004年9月 Jan Blunck(j.blunck@tu-harburg.de) 在「Re: [PATCH 1/3] copyfile: generic_sendpage」串中 说明自己的 union-mount 内核实现以 McKusick 论文为设计蓝本，「The focus is on the basic functionality explained by McKusick」，是 BSD 血统文件系统技术被 Linux VFS 层直接借用的例证 `<!-- ROW_MINE: lkml.messages.1914560 -->`
- 【Linux社区】2004年8月 Helge Hafting(helge.hafting@hist.no) 在「Re: PATCH: cdrecord: avoiding scsi device numbering for ide devices」串中 回应 Joerg Schilling 关于 libscg 跨平台稳定性，指认 FreeBSD 与 OpenBSD 皆运行于 libscg 的 CAM 抽象之上，「the vast majority does not allow the adressing method the people on LKML seem to prefer recently」，是 BSD 血统 libscg SCSI 抽象层以 FreeBSD CAM 承载其跨 OS 成熟度、与 Linux 内核 /dev 偏好形成张力的一例 `<!-- ROW_MINE: lkml.messages.2107554 -->`
- 【Linux社区】2006年9月 David Stevens(dlstevens@us.ibm.com) 在「Re: [PATCH] make ipv4 multicast packets only get delivered to sockets that are joined to group」串中以 'for compatibility with everything else since' 与 'about ~4.3BSD' 为据确认 Linux IPv4 组播投递语义沿袭 BSD，是 Linux 网络 API 直接对标 4.3BSD 的显性证据 `<!-- ROW_MINE: lkml.messages.2033405 -->`
- 【Linux社区】2008年10月 Michael Kerrisk(mtk.manpages@googlemail.com) 在「Re: [patch 0/3] [RFC] kernel/glibc mismatch of readlink syscall?」串中考据 'It looks like the Linux man page came from BSD' 并沿 '4.3BSD'、'FreeBSD 6.2' 双向对照，是 Linux 手册页层直接继承 BSD 血统的显性证据 `<!-- ROW_MINE: lkml.messages.2234563 -->`
- 【Linux社区】2015年3月 Taesoo Kim(tsgatesv@gmail.com) 在「[PATCH 1/1] ufs: return correct errno for write_inode()」串中以 'similar/consistant to the rest of filesystems' 为由提交 Linux 内核内 BSD 血统 UFS 文件系统的错误码补齐 patch，是 Linux 长期移植并维护 BSD 派生文件系统的例证 `<!-- ROW_MINE: lkml.messages.6322811 -->`

## 210.2 【Linux社区】GPL 与 BSD 许可证张力（3 条）

- 【Linux社区】1999年5月 Dimitris Michailidis(dimitris@darkside.engr.sgi.com) 在「[PATCH] kernel profiling with gprof」串中 提交 gprof 内核剖析补丁，补丁 profile.h 中嵌入 BSD 版权声明「Regents of the University of California」，是 BSD 版权技术直接被引入 Linux 内核、BSD 与 GPL 许可证共存张力最具体的物证 `<!-- ROW_MINE: lkml.messages.1605274 -->`
- 【Linux社区】2004年10月 Horst von Brand(vonbrand@inf.utfsm.cl) 在「Re: Linux v2.6.9 and GPL Buyout」串中 对 SCO 诉讼下的 GPL 集体买断方案表态，建议「start off a *BSD variant, where there is _no_ SCOX complications」，是 GPL 与 BSD 许可证冲突在 SCO 诉讼背景下由 BSD 血统替代方案承载的张力例证 `<!-- ROW_MINE: lkml.messages.2077327 -->`
- 【Linux社区】2009年11月 Tony Finch(dot@dotat.at) 在「[PATCHv2] unifdef: update to upstream revision 1.190」串中将自 Berkeley 血统的 unifdef 更新入内核，patch 明确 'carried the 4-clause BSD copyright licence' 且 'carries a more liberal licence'，是 BSD 血统工具被 Linux 采纳并伴随 4-clause BSD 许可重构的实证 `<!-- ROW_MINE: lkml.messages.2216571 -->`

## 210.3 【Linux社区】附录：筛查与去重情况

- **来源**：historical_claims.raw_source 已入库 lkml claim 19 封
- **outline_worthy**：13 条（strong 6 + moderate 7）
- **剔除**：6 条（1986257 NFS 纯 Linux 讨论 / 1721519 Linux 存档史 / 1777935 同 thread 去重 / 1944923 Kconfig 排版 / 1782000 个人轶事 / 3953680 PIE 讨论）
- **precision**：13/19 = 68.4%

### 210.3.1 年份分布（13 条入纲）

- 1999: 2
- 2002: 1
- 2003: 2
- 2004: 4
- 2006: 1
- 2008: 1
- 2009: 1
- 2015: 1

### 210.3.2 精度对比

| 分层 | precision | 样本 → 入纲 |
|---|---|---|
| historical_claims 反向张力 | 68.4% | 19 → 13 |
| tier A 硬过滤精选 | 48.2% | 218 → 104 |
| fig_B1 层 | 13.5% | 222 → 30 |
| ZFS on Linux 专题 | 19.0% | 21 → 4 |
| tier B 硬过滤精选 | 11% | 200 → 22 |

### 210.3.3 已知盲区

- 这 19 封是 historical_claims 早期（2020-2024）人工筛选入库，覆盖 1998-2024 年 26 年跨度，但仅占 lkml 6.44M 封的 0.0003%，是「精选之精选」
- 205-209 章是算法分层筛选（tier A/B）+ ZFS 专题，本章是人工反向张力深挖，两者方法论互补
- 211 章起将接入 BSD 发展列表（freebsd-*/netbsd-*/openbsd-*）与 BSD 人物反向追溯
