# 第 05 卷文献综述：FreeBSD 的工程化奠基（1996-2010）

> 卷级综述 vol-05｜撰写：2026-08-04｜模板：实施总方案 C1（五段式）
> 素材：`_素材/vol-05-base.md`（现有研究 97 / 存疑 80 / 考据 2）
> 章范围：第 87-107 章｜卷目录：`05-卷册大纲/第05卷-freebsd的工程化奠基/`

---

## ① 卷主题与章节范围

本卷覆盖 **1996-2010 年 FreeBSD 的工程化奠基期**：4.x 稳定时代、5.x 转型（SMPng/GEOM 架构）、6.x/7.x 工程深化，以及 FreeBSD 基金会成立、基础设施（ports/源码树管理）、安全公告体系（SA）等工程制度的建立（21 章，ch87-107）。本卷主题为"CSRG 遗志的承续"——FreeBSD 接棒 BSD UNIX 工程传统。

## ② 现有研究综述

**素材基础**：T1 素材 97 条（中等密度）——eurobsdcon/BSDCon 会议论文为主（素材样本显示 eurobsdcon 系列论文密集）。

- **会议文献**：eurobsdcon2011/2015/2017 系列（kettenis/packages/device-drivers/opensmtpd 等）——工程细节的会议级记录。
- **官方一手**：FreeBSD Handbook/发行说明（ch14 分类 0 条命中但 FreeBSD 官方文档在 overview 级存在）；FreeBSD-SA 安全公告（nvd_cve 数据 474 条 FreeBSD 在资料数据库）。
- **工程史**：FreeBSD 4.x-7.x 的架构论文（SMPng、GEOM）——references 中 FreeBSD 相关条目（素材 id 20/1137 等共享）。
- **承续叙事**：CSRG 遗志（McKusick 参与 FreeBSD 基金会）、BSD 许可证自由的传统延续。

**中文研究现状**：FreeBSD 2000 年代中文资料（ChinaUnix/FreeBSDChina 时代）丰富但零散；系统性工程史中文专著空白——本卷填补。

## ③ 一手史料来源

- **FreeBSD 官方文档**：Handbook、发行说明（4.x-7.x）、FAQ
- **会议论文**：BSDCon/Usenix BSD 专场/eurobsdcon
- **邮件列表档案**：freebsd-arch/freebsd-hackers（工程决策过程）
- **FreeBSD-SA 安全公告**：nvd_cve_metadata 474 条（资料数据库）
- **考据记录 2 条**（T1 素材）

## ④ 研究缺口

1. **承续机制研究**：CSRG 解散后到 FreeBSD 基金会成立之间的"组织真空期"（1995-2000）——公开文献少。
2. **5.x 转型争议**：SMPng 重写过程中的社区争议（Dillon 撤权、DragonFly fork 前史）——素材密度不足，需邮件列表考据。
3. **工程制度史**：SA 安全公告体系、ports 治理的早期制度化——官方文档有但学术分析缺。
4. **素材口径**：97 条中会议论文占多数，系统级学术综述少。

## ⑤ 与本书"软件自由"主线的关系

本卷是**"自由的工程化承续"**：FreeBSD 以 BSD 许可证（最自由）承续 CSRG 未竟事业——"自由"从版本史进入工程制度（基金会治理、安全公告、ports 生态）。与第 2 卷（伯克利版本史）构成"遗志→承续"的叙事闭环，也是后续核心技术卷（vol-06）的组织前提。

---

## 附：存疑联动

本卷存疑 80 条（历史已解决为主）；id 范围见 `存疑卷级聚合台账.md` 第 5 卷行。
