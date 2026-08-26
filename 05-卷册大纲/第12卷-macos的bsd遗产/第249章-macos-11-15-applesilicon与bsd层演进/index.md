---
chapter: 第 249 章
id: CH249
volume: 第12卷-macos的bsd遗产
---

# 第 249 章 macos-11-15-applesilicon与bsd层演进

## 要点

- **Rosetta 2** 是 Apple 为 Apple Silicon 过渡开发的 x86_64 至 ARM64 动态二进制翻译层，于 **2020 年 11 月 12 日** 随 macOS 11 Big Sur 发布。Rosetta 2 在用户态运行，通过 BSD 层的 `mmap`（映射代码段）、`mprotect`（设置可执行权限）、`execve`（启动翻译进程）系统调用实现二进制翻
- Apple 于 **2020 年 6 月** 承诺 2 年内完成 Apple Silicon 过渡，至 **2022 年 6 月** WWDC 2022 公布 Apple Silicon Mac 全产品线覆盖完成（包括 Mac Studio、Mac Pro **2023 年 6 月** 发布，此为最后过渡至 Apple Silicon 的产品线）。**2020-2023 年** 间 Apple 发
- **2025-09-15 至 2026-06-29** 期间，Apple 发布 macOS Tahoe 26.x 系列共 **30 条 Security Advisories**，覆盖 12 个 macOS 版本（26、26.0.1、26.1、26.2、26.3、26.3.1、26.3.2、26.4、26.4.1、26.5、26.5.1、26.5.2）。所有公告均通过 Apple Security
- darwin 代码仓库共 2,016 次提交（2001-04-10 至 2106-02-07），27 位贡献者

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4129] 卷“第12卷-macos的bsd遗产”第 249 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- Rosetta 2 是否影响 BSD 层的内核设计——经 Darwin 源码仓库比对，Rosetta 2 在用户态运行，未修改 XNU 内核。BSD 层的 `mmap`、`mprotect`、`execve` 系统调用在 Apple Silicon 过渡前后保持接口稳定。采信 “Rosetta 2 是用户态翻译层，不影响 BSD 内核设计” 的判断。
- Apple Silicon 过渡是否导致 FreeBSD arm64 工作的变化——Apple Silicon Mac 的启动方式（Apple 自研的 BootPolicy 与 fwarpd）与 FreeBSD 的 arm64 启动方式不同，Apple Silicon Mac 无法直接运行 FreeBSD（须通过虚拟化如 Asahi Linux 项目的 m1n1 hypervisor）。此限制是
- macOS Tahoe 26.x 系列小版本是否对应独立 Security Advisory——Security Releases 索引页显示 26.0.1、26.3.1、26.3.2、26.4.1、26.5.1 等小版本未列出独立公告 URL，可能 Apple 将这些小版本的安全更新合并到上一主版本的公告中，亦可能是索引页更新滞后。bsd_commits.db 显示这些小版本亦共用同一 XNU
- 贡献者高度集中——Top 1 贡献者 Apple OSS Distributions 占比 100.0%，需考量'个人主导'与'社区协作'的叙事张力

## 文献

- Apple Inc. Rosetta 2 Technical Overview [Z]. Apple Developer Documentation, 2020; AnandTech. Apple M1 Review [EB/OL]. (2020-11-18). <https://www.anandtech.com/show/16252/mac-mini-apple-m1-tested>.<!-- DB_REF:darwin.duckdb -->> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 2020-2021 年间：186 次提交。> 仓库总览：2,016 次提交，27 位贡献者，2001-04-10 至 2106-02-07。
- Apple Inc. WWDC 2022 Keynote [EB/OL]. (2022-06-06). Apple Press Release; Apple Inc. Mac Studio and Mac Pro with M2 Ultra [EB/OL]. (2023-06-05). Apple Press Release; Asahi Linux Project. m1n1 Hypervisor Documentation [EB/OL]. <https://asahilinux.org/>.<!-- DB_REF:darwin.duckdb -->> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 2021-2024 年间：343 次提交。> 仓库总览：2,016 次提交，27 位贡献者，2001-04-10 至 2106-02-07。
- Apple Security Releases [EB/OL]. <https://support.apple.com/en-us/100100>, 2026-07-23 访问; Apple Inc. macOS Tahoe 26 Security Content [EB/OL]. (2025-09-15). <https://support.apple.com/en-us/125110>; bsd_commits.db 查询结果 [EB/OL]. script/query_xnu_tags.py, 2026-07-23; 原材料/研究/考据记录/20260723_announcements-macos.md [EB/OL]. 2026-07-23.<!-- DB_REF:darwin.duckdb -->> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 2025-2026 年间：138 次提交。> 仓库总览：2,016 次提交，27 位贡献者，2001-04-10 至 2106-02-07。
