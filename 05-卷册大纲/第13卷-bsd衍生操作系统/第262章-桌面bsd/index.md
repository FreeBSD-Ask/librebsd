---
chapter: 第 262 章
id: CH262
volume: 第13卷-bsd衍生操作系统
---

# 第 262 章 桌面bsd

## 要点

- BSD 衍生项目 Top 5：ghostbsd-src(616346)、hardenedbsd-src(167144)、midnightbsd-mports(68177)、truenas-middleware(59959)、opnsense-core(30850)。GhostBSD 提交量最大，反映桌面 BSD 的活跃尝试

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4139] 卷“第13卷-bsd衍生操作系统”第 262 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

- [DB:code_repos:bsd-derivatives.duckdb] BSD 衍生项目 Top 5：ghostbsd-src(616346)、hardenedbsd-src(167144)、midnightbsd-mports(68177)、truenas-middleware(59959)、opnsense-core(30850)。GhostBSD 提交量最大，反映桌面 BSD 的活跃尝试

## 史观

- 动手者创造历史：桌面 BSD 的反复尝试（GhostBSD/MidnightBSD/NomadBSD/helloSystem）是无数动手者的默默努力

## 辨析

- GhostBSD 版本对应的 FreeBSD 基底须以项目 Release Notes 核实；openbsd.db 查询 L7.1.1.ghostbsd-src 的 commit 量须警惕 fork 分歧识别局限——ghostbsd-src 仓库 1993 年起的 commit 是 fork 自 FreeBSD 继承的上游历史，非 GhostBSD 项目本地 commit，识别 GhostBSD 
- 须纠正原文中 “helloSystem 由 GhostBSD 衍生思想启发” 的表述——经联网考据，helloSystem 由 Simon Peter 独立发起，其设计灵感明确来源于早期 MacOS（System 1），与 GhostBSD 无直接衍生关系，二者仅同属 “FreeBSD 桌面化” 大类；helloSystem “无密码/无用户账户” 的设计在多用户场景与远程管理中存在结构性局限，须
- 桌面 BSD 与 Linux 桌面在硬件支持、应用生态、许可证三维度存在结构性差异——(1) 硬件支持：桌面 BSD 在 amdgpu 驱动支持上滞后于 Linux（参照 120.19.1 节已考据内容，FreeBSD amdgpu 驱动由 AMD 在 Linux 内核维护，FreeBSD 须通过 drm-kmod 移植，存在版本滞后），Wayland 支持不完整（FreeBSD Wayland 
- ghostbsd-src 的 592 个去重 CVE 须区分 “继承自 FreeBSD 上游” 与 “GhostBSD 本地特有”——fork 仓库的 commit 历史包含上游继承部分，识别本地特有 commit 须通过 parent_hashes 交叉验证；2022 年 merge commit 比例降至 1.1% 的原因须与 Eric Turgeon 的 GhostBSD 公告、FreeBS
- midnightbsd-src 的 152 个去重 CVE 数量低于 ghostbsd-src 不必然意味着 MidnightBSD 更安全，更可能反映其 commit 追踪不完整或上游同步滞后——fork 自 FreeBSD 6.x 的代码库可能存在未被 commit message 显式标注 CVE 的已知漏洞；FreeBSD 6.x 停止支持（2013 年）后 MidnightBSD 是否独

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 bsd-derivatives.duckdb
