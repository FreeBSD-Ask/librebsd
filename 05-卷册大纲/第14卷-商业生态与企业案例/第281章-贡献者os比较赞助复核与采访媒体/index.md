---
chapter: 第 281 章
id: CH281
volume: 第14卷-商业生态与企业案例
---

# 第281章 贡献者os比较赞助复核与采访媒体

## 要点

- **Netflix** 的 **Jonathan Looney**、**Drew Gallatin** 推动了 `sendfile`、**TLS** 与 **kTLS** 等核心特性，**Juniper** 的 **ARM64** 移植团队贡献了 **FreeBSD** **arm64** 端口基础。
- **Sony** **PS** 团队、**Apple** **Darwin** 团队中部分工程师因 **NDA** 无法公开贡献，但仍通过匿名渠道、私下交流影响 **FreeBSD** 发展，是被遗忘的边缘者。
- **Linux** 企业贡献者通过公司开源政策可公开贡献，**BSD** 企业贡献者受 **NDA** 限制更多，处境差异显著。
- 企业 `committer` 的贡献通过 `freebsd-committers` 邮件、`git` `commit` 记录、**BSDCan** 演讲等公开材料追溯。
- **SunOS 4.x**（1989-1994）基于 **4.3BSD-Reno**，是 **BSD** 谱系最重要的商业分支之一，但 **Sun Microsystems** 从未公开释放 **SunOS 4.x** 完整源码；1992 年起 **SunOS 5.x** 改名 **Solaris** 转向 **SVR4**，**SunOS 4.x** 进入维护阶段并最终于 1994 年停止开发；**SunOS 4.x** 源码在 **Sun** 内部保管，从未像 **Solaris 10** 那样在 **CDDL** 下开放，亦无 **Caldera** 式的许可证释放；**BSD/OS** 商业版的源码情况类似——**Berkeley Software Design, Inc.**（**BSDi**）的 **BSD/OS** 2.0-5.x 源码在 2000 年前后公司被 **Wind River** 收购后未公开释放；Commercial **Unix** 源码的封闭状态使 **BSD** 史学研究长期依赖 **4.4BSD-Lite** 与 **FreeBSD**/**NetBSD**/**OpenBSD** 的开放谱系反向追溯，**SunOS 4.x** 与 **BSD/OS** 的封闭源码构成 **BSD** 谱系的“暗物质”。

## 史观

- 总纲第 9 条——商业与社区协作：企业 `committer` 的回馈
  - 辨析：**Netflix** 与 **Juniper** 哪家对 **FreeBSD** 上游贡献更大
  - 文献：Netflix 技术博客；FreeBSD 源码 Juniper ARM64 commit ［A］
    FreeBSD 社区论文与演讲 [124]，[124] Matt Ahrens. Flexibl
- 总纲第 10 条与第 17 条的张力——商业版本的封闭是开源史学不可绕过的盲区，被遮蔽的源码意味着被遮蔽的叙事
  - 辨析：［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ **SunOS 4.x** 源码是否在 **Oracle** 收购 **Sun** 后仍完整保存于 **Oracle** 内部档案无公开确认；**BSD/OS** 源码在 **
- 总纲第 4 条与第 25 条的张力——分离是新的聚合的开始，**Oracle** 关闭 **OpenSolaris** 反而催生 **illumos** 这一独立的开放分支；但 **illumos** 与 **OpenSolaris** 之间的源码连续性在 2010 年 8 月后部分断裂，**Oracle** 后续 **Solaris 11.x** 的开发完全闭源，**illumos** 无法再吸
- 总纲第 10 条——边缘者的贡献被中心叙事遮蔽，商业 **Unix** 源码的封闭意味着这些系统的开发者贡献无法被史学完整记录
  - 辨析：［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ **AIX** 源码访问的“air-gapped 机器、8mm 磁带签名”流程在不同 ex-**IBM** 员工口述中细节不一致，可能为不同时期的内部政策；**
- 总纲第 24 条——许可证：**GPL** 催化商业闭环
  - 辨析：**Linux** 商业闭环的成功不能全归因于 **GPL**，也涉及商业策略
  - 文献：**Red Hat** 年报；**LWN** 内核统计 ［B］
    FreeBSD 社区论文与演讲 [124]，[124] Matt Ahrens. Flexible Disk Use in OpenZFS [C]//BSDCan

## 辨析

- **Netflix** 与 **Juniper** 哪家对 **FreeBSD** 上游贡献更大
  - 文献：Netflix 技术博客；FreeBSD 源码 Juniper ARM64 commit ［A］
    FreeBSD 社区论文与演讲 [124]，[124] Matt Ahrens. Flexible Disk Use in OpenZFS [C]//BSDCan 2018. [S.
- ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ **SunOS 4.x** 源码是否在 **Oracle** 收购 **Sun** 后仍完整保存于 **Oracle** 内部档案无公开确认；**BSD/OS** 源码在 **Wind River** 2005 年停止 **BSD/OS** 产品线后的去向无公开档案，需通过 **Wind River*
- ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ **OpenSolaris** 闭源后 **Oracle** 是否保留 **CDDL** 许可证下已发布源码的完整可访问性无公开声明；**illumos** 重新实现的闭源替代组件与 **Oracle** **Solaris 11.x** 中对应组件的功能等价性需通过 **API** 兼容性测试独立验
- ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ **AIX** 源码访问的“air-gapped 机器、8mm 磁带签名”流程在不同 ex-**IBM** 员工口述中细节不一致，可能为不同时期的内部政策；**SGI** **IRIX** 源码在 **SGI** 破产后的最终归属无公开法院文件确认，传闻 **Rackable Systems** 收购
- **Linux** 商业闭环的成功不能全归因于 **GPL**，也涉及商业策略
  - 文献：**Red Hat** 年报；**LWN** 内核统计 ［B］
    FreeBSD 社区论文与演讲 [124]，[124] Matt Ahrens. Flexible Disk Use in OpenZFS [C]//BSDCan 2018. [S.l.]: [s.n.], 2018. 获取路径：<h

## 文献

- Netflix 技术博客；FreeBSD 源码 Juniper ARM64 commit ［A］
    FreeBSD 社区论文与演讲 [124]，[124] Matt Ahrens. Flexible Disk Use in OpenZFS [C]//BSDCan 2018. [S.l.]: [s.n.], 2018. 获取路径：<https://papers.freebsd.org/2018/bsdcan/ahrens-flexible_disk_use_in_openzfs/> [访问日期 2026-07-26].

## 281.38.2 被 NDA 封锁的企业内部推广者

- 要点
- Sun Microsystems 1993 SunOS 4.1.3 Reference Manual；Wind River 2001-2005 年度报告中关于 BSD/OS 产品线的章节；Caldera 2002 年 1 月 BSD 释放公告（Groklaw 存档） ［A］

## 281.39.2 OpenSolaris 2010 年 8 月关闭与 illumos fork：闭源回归与社区自救

- 要点：**Sun Microsystems** 于 2005 年 6 月 14 日在 **CDDL** 许可证下开源 **Solaris** 形成 **OpenSolaris** 项目，2005
- Steven Stallion 2010.8.13 博客；Garrett D'Amore 2010.8.3 illumos 公告；Bryan Cantrill LISA 2011 演讲；illumos.org/about/history/；InfoQ 2010.8.29“OpenSolaris 走到尽头了吗？” ［C］

## 281.39.3 Apple Darwin 2005 年 5 月 x86 关闭：APSL 下的选择性开放

- 要点：**Apple** 于 2000 年在 **Apple Public Source License**（**APSL**）1.0 下释出 **Darwi
- IBM AIX Documentation；HP-UX Documentation；Tru64 UNIX Documentation（HP.com 存档）；SGI 破产重组法院文件（2006）；Unix 史学综述文章（如 Peter Salus“The Daemon, the GNU & the Penguin”） ［A］
- **Red Hat** 年报；**LWN** 内核统计 ［B］
    FreeBSD 社区论文与演讲 [124]，[124] Matt Ahrens. Flexible Disk Use in OpenZFS [C]//BSDCan 2018. [S.l.]: [s.n.], 2018. 获取路径：<https://papers.freebsd.org/2018/bsdcan/ahrens-flexible_disk_use_in_openzfs/> [访问日期 2026-07-26].

## 281.13.2 **Solaris** 与 **Windows** 商业模式的差异

- 要点
- **BSDL** 原文；**Foundation** 年报 ［B］

## 281.13.4 各项目商业数据与市场份额考据

- 要点：各项目的商业数据与市场份额需从多个来源收集，包括年报、市场研究报告。
- 史料：各公司年报、**IDC**/**Gartner** 市场报告 ［B］
- 史观：总纲第 16 条——经济周期：商业数据反映经济周期
- 辨析：市场份额数据的方法论差异需评估
- 文献：**IDC** 市场报告；**Gartner** 报告［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 281.41.2 利益分配法律化与 **BSDL**/`committer` 权限/企业赞助的形式主义（总纲第 13 条）

- 要点：从项目史观总纲第 13 条 “法律与道德是利益分配” 切入，**FreeB
- 项目史观总纲第 21 条（见 据原文第 25 章）；**BSD 2-Clause** 原文；**Linux** 内核 **COPYING** 文件（torvalds/linux 仓库）；**Committer‘s Big List of Rules**；**FreeBSD Committer’s Guide**；**FreeBSD Foundation** **IRS** **990** 表；openbsd.duckdb L3.2.1/L3.2.2 查询报告；**Berlin** I. “Two Concepts of Liberty”（1958）；**TrueNAS** 2025 迁移公告；上述 1

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
