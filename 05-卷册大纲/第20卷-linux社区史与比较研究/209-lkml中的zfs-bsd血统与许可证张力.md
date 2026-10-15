# 209 【Linux社区】LKML 中的 ZFS：BSD 血统与许可证张力（专题）
> 来源：lkml 2016-2024 年 ZFS 相关讨论全量筛查（ZFS + FreeBSD/OpenBSD/NetBSD/illumos/GEOM/OpenZFS/Solaris/SunOS 关键字），命中 21 封，1 路并行读手判定，4 条 outline_worthy（precision 19%）。
> 判定：4 CAND。主题分布：BSD 谱系 2、许可证 2。
> 全库去重：本次 4 条与 historical_claims 已入库 19 条 lkml、dslinux_keywords.hits 8141 lkml 基座、205/206/207/208 章 156 条 ROW_MINE 四处严格去重（0 条完全重复）。

## 209.0 【Linux社区】体例说明
本文件系 lkml ZFS on Linux BSD 血统专题筛查产物。ZFS on Linux 是 BSD 与 Linux 最大工程融合事件之一，但 lkml 讨论中 BSD 血统线索稀疏（21 封候选仅 4 封 outline-worthy），主要因 ZFS on Linux 讨论聚焦于 Solaris/illumos 血统而非 BSD 血统。
**与 208 章互补**：208 章是 tier B BSD 技术承袭续篇（dtrace/capsicum/KAME/strlcpy 等），本章是 ZFS on Linux BSD 血统专题（GPL 张力、BSD 交叉验证、NFSv4 ACL 参照）。
**已知盲区**：ZFS on Linux 主要讨论在 zfsonlinux/zfs-linux GitHub 与 illumos 邮件列表，不在 lkml；FreeBSD ZFS 移植讨论在 freebsd-fs 列表；OpenZFS 开发讨论在 openzfshackers 列表。

## 209.1 【Linux社区】BSD 谱系（ZFS 交叉验证与 NFSv4 ACL 参照）

- 【Linux社区】2019年2月 Martin Cracauer(cracauer@cons.org) 在「Possibe NFS mm problem: client page-in errors with ZFS Linux server」串中报告 ZFS on Linux NFS 客户端页错误问题，「cross-checked with a FreeBSD server with very similar ZFS code」，是 FreeBSD 作为 ZFS on Linux 调试对照基准的具体用例。 `<!-- ROW_MINE: lkml.messages.6803041 -->`
- 【Linux社区】2023年5月 Ondrej Valousek(ondrej.valousek.xm@renesas.com) 在「RE: A pass-through support for NFSv4 style ACL」串中列举 FreeBSD、OmniOS、Solaris 作为 NFSv4 ACL 参照，「a clean NFSv4 acls implemented - just like Netapp, OmniOS, Solaris or FreeBSD」，是 BSD 血统系统作为 ZFS ACL 方案参照的具象化。 `<!-- ROW_MINE: lkml.messages.3534781 -->`

## 209.2 【Linux社区】许可证张力（GPL-only 阻碍与 FreeBSD 转向）

- 【Linux社区】2017年12月 Boris Lukashev(blukashev@sempervictus.com) 在「Re: [kernel-hardening] [PATCH 5/5] docs: add dmesg encryption doc」串中质疑 GPL-only 设施对非 GPL 模块的阻碍，「Tom Caputi of Datto had to port over a ton of Illumos crypto code for ZFS」，是 GPL 与 BSD 血统冲突在 ZFS on Linux 上的具体印证。 `<!-- ROW_MINE: lkml.messages.6734892 -->`
- 【Linux社区】2019年1月 Rene Schickbauer(cavac@cavac.at) 在「Re: x86/fpu: Don't export __kernel_fpu_{begin,end}()」串中反驳 GPL-only 立场并表态宁可转向 FreeBSD 也不换文件系统，「i'm more inclined to switching to FreeBSD than to switch to another filesystem」，是 GPL 与 BSD 血统冲突在 ZFS 问题上最直白的表态。 `<!-- ROW_MINE: lkml.messages.6975317 -->`

## 209.3 【Linux社区】附录：筛查与去重情况

- **筛查范围**：lkml 2016-2024 年 ZFS 相关讨论
- **总命中**：21 封（ZFS + BSD/Solaris/illumos 关键字）
- **outline_worthy**：4 条（strong 2 + moderate 2）
- **剔除**：17 条（util-linux release notes 7 + Linux 内部讨论 6 + Getting a new fs 串 3 + NVMe 崩溃 1）
- **precision**：4/21 = 19.0%

### 209.3.1 ZFS 关键字分布（21 条候选）

- has_freebsd: 13
- has_geom: 3
- has_illumos: 1
- has_openzfs: 1

### 209.3.2 年份分布（4 条入纲）

- 2017: 1
- 2019: 2
- 2023: 1

### 209.3.3 已知盲区

- ZFS on Linux 主要讨论在 zfsonlinux/zfs-linux GitHub（2016-2024 合并入 Linux 6.12 主线）
- FreeBSD ZFS 移植讨论在 freebsd-fs 邮件列表
- OpenZFS 开发讨论在 openzfshackers 邮件列表
- illumos 邮件列表讨论 ZFS 内核移植
- Solaris/SunOS ZFS 起源讨论在 Sun Developer Network（已归档）

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1245 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1245`；w172 YouTube 章节路由采纳）

据 OpenZFS Dev Summit 2014 讲者口述：ZFS on Linux 当时的当前版本为 0.6.3（原文口述讹字 on links、063）。（YouTube EP_MVOpMNV7LY，[19.359-26.91]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->
