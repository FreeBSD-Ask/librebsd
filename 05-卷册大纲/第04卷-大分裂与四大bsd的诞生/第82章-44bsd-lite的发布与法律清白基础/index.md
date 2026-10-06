---
chapter: 第 82 章
id: CH82
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 82 章 4.4BSD-Lite 的发布与法律清白基础

## 要点

- 4.4BSD-Lite 法律意义的史料辨析须区分 “和解协议条款” 与 “实际执行情况”——协议要求删除 USL 代码，但实际执行中部分代码的归属认定存在模糊；辨析须对照 USL v. BSDi 和解协议原文（1994.1）与 4.4BSD-Lite 源码 diff——经 McKusick 1999 当事人一手记载确认仅 3 个文件被完全删除、约 70 个文件添加 USL 版权声明，实际执行情况与协议条款基本一致。
- 重建的史料辨析须区分 “成功重建” 与 “代价”——前者有据可循（FreeBSD 2.0 于 1994.11.22 发布，法律洁净），后者经 **bsd_commits.duckdb** tags 表 release/2.0_cvs tagger_date 1994-11-22T10:58:58Z 量化——FreeBSD 因诉讼和解要求在 1994 年 7 月底前停止 Net/2 产品发布，实际约 5 个月完成迁移。
- 解散的史料辨析须区分 “组织解散” 与 “技术终结”——前者有据可循（CSRG **1995.6** Mike Karels 告别邮件 “Berkeley CSRG is now disbanded”），后者经三大 fork 项目继承 4.4BSD-Lite2 代码延续（FreeBSD 2.0 **1994.11.22**、NetBSD 1.0 **1994.10.26**、OpenBSD 1.0 **1995.10.18**〔存疑：OpenBSD 1995.10 自 NetBSD 1.0 分叉之初的版本号与日期史料记载不一，OpenBSD 官方视 1996.10 的 2.0 为首个正式发布〕）。
- 4.4BSD-Lite Release Notes 的文档史史料辨析须区分 “文档记录” 与 “实际状态”——前者是 Release Notes 的描述（如技术变更列表、贡献者名单），后者是代码与社区的实际状态（经 4.4BSD-Lite 源码档案与 CSRG 邮件列表核实）；辨析须对照 4.4BSD-Lite Release Notes 与 4.4BSD-Lite 源码档案、CSRG 邮件列表三类史料交叉验证。
- 和解协议要求移除信号处理、printcap、tty 三文件虽仅占极少代码行数，但影响了打印机配置与串行终端支持。

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_11069] BSD Now 第 579 期，匹配 CH82 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11299] BSD Now 第 554 期，匹配 CH82 章，关联度 1.0
- [DB:historical_claims:claim] 关键词行级挖掘素材线索 82.8-关键词行级挖掘素材线索（1 条，CL-RM 段，见 82.8-关键词行级挖掘素材线索.md）

## 史观

- 总纲 13（法律与道德是利益分配）：和解协议作为法律形式直接决定 4.4BSD-Lite 的代码组成，删除 USL 代码是利益分配的技术投影
- 总纲 3（不存在进步，只有权力再分配）：法律清白与市场窗口损失并存，USL 与 BSDi 的和解实为权力再分配而非单纯技术进步
- 总纲 4（分离聚合是永恒规律）：CSRG 组织解散而 BSD 技术经 FreeBSD、NetBSD、OpenBSD 三大 fork 分离聚合延续
- 总纲 8（本体论上各方平等）：USL、BSDi、CSRG 与各 fork 项目的叙事在本体论层面平等对待，不以胜败论英雄
- 总纲 7（理论必须自反）：文档记录（Release Notes）与代码实际状态的区分须自反审视，避免以文档描述替代史料核验

## 辨析

- 法律意义的史料在不同叙事中差异较大——部分强调 “无 USL 代码” 的彻底性（采信 4.4BSD-Lite Release Notes 1994.6 与 Novell 不起诉承诺），部分指出实际执行的模糊性（采信 McKusick 1999 当事人一手记载关于 3 个文件被完全删除、约 70 个文件添加 USL 版权声明的具体范围）——经 USL v. BSDi 和解协议原文（1994.1）与 4.4BSD-Lite 源码 diff 对照，两说并存，须以一手史料逐项核验。
- 重建的史料价值在 “成功” 维度有据可循，但在 “代价” 维度需谨慎——“18 个月窗口损失” 说法无精确日期支撑〔存疑：该说法未见精确日期史料支撑〕：诉讼从 1992.12 至 1994.1 和解约 13 个月，FreeBSD 实际重建 5 个月；NetBSD 1.0 于 1994.10.26 发布，早于 FreeBSD 2.0 近一个月，各项目迁移速度不同；**bsd_commits.duckdb** 中 NetBSD src 镜像无 tag 记录可佐证
- 解散的史料价值在 “组织解散” 维度有据可循（CSRG 1995.6 Karels 告别邮件），但在 “技术终结” 维度经 FreeBSD/NetBSD/OpenBSD 三大 fork 持续至 2026 年的客观事实可证伪——BSD 技术通过社区项目长期延续，组织解散与技术终结非同一维度
- 文档史的史料价值在 “技术描述” 维度有据可循，但在 “实际状态” 维度须谨慎——文档可能滞后或不完整，须对照 4.4BSD-Lite 源码档案与 CSRG 邮件列表交叉验证
- 本目遵循 0 信任原则，三文件的“技术影响”判定须以 4.4BSD-Lite RELNOTES 与被移除文件的实际功能为据——信号处理、printcap、tty 三文件对应信号处理、打印机配置、串行终端支持三条用户态路径，其移除使 4.4BSD-Lite 相对 4.4BSD 形成功能性缺口，而非单纯的代码行数减少；【0 信任原则】三文件的“技术影响”程度须以 RELNOTES 一手记载核验，不得仅凭代码行数推断影响程度。

## 文献

- USL v. BSDi 和解协议；4.4BSD-Lite 源码档案 ［A］
- FreeBSD 2.0 Release Announcement 1994.11.22；FreeBSD Handbook；NetBSD 1.0 Release Announcement 1994.10.26；**bsd_commits.duckdb** `tags` 表（FreeBSD release/2.0_cvs）与 `contributors` 表（<christos@NetBSD.org> 首次 commit 1994-10-26T11:58:24Z） ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。
> 1992-1995 年间：15,540 次提交。

<!-- /DB_REF -->

- CSRG 解散史料分析；BSD 技术传承研究［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- 4.4BSD-Lite Release Notes 史料分析；BSD 文档史研究［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- 和解协议；4.4BSD-Lite 文档 ［A］

## 史料考据补充（2026-08-04 任务3 联网核验）

> 主题：4.4BSD Lite 的技术完整性 vs 法律清白性取舍
- 4.4BSD-Lite 批评史料分析；BSD 历史研究方法论［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- CSRG 边缘贡献者史料分析；贡献评估方法论［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- ROW_MINE: login-zazhi.articles.CL-4-126 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-126`；login 逐条遍历判定采纳）

2000 年前后，斯坦福大学在公共集群上以 Kerberos 单点登录配合 rsh 脚本实现远程批量管理，少数管理员即可管理数百台主机、每台约 30000 活跃账户；同期系统管理实践普遍采用 OS 加固（关闭不必要服务与 setuid 程序）以降低提权风险。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

