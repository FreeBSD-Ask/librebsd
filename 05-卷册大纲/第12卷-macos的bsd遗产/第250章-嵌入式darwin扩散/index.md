---
chapter: 第 250 章
id: CH250
volume: 第12卷-macos的bsd遗产
---

# 第 250 章 嵌入式 Darwin 的扩散

## 要点

- iPhone OS 于 **2010 年 6 月 21 日** 随 iOS 4.0（iPhone OS 4）更名，iOS 之名正式启用。**iOS 4** 引入多任务（伪多任务，限定 API 后台执行）、FaceTime（基于 SIP 协议，底层 BSD socket）；**iOS 5**（**2011 年 10 月 12 日** 发布）引入 Siri 语音助手、通知中心与 iCloud 云服务，嵌入式 Darwin 的设备覆盖随 iPhone 4S 与 iPad 系列持续扩大。
- 嵌入式 Darwin 的开源部分仍经 **APSL 2.0** 接受外部贡献，但 iOS、iPadOS、watchOS、tvOS、visionOS 的完整内核源码不公开——Apple 仅公开 macOS 端的 Darwin 源码（通过 opensource.apple.com），嵌入式端的 XNU 源码以 macOS 版本为基础间接公开。Apple 于 **2020 年** 推出 Apple Security Research Device Program（安全研究设备计划，向安全研究者提供专用研究设备），间接承认封闭生态对安全研究的制约。
- **2007-2024 年** iOS 系（含 iPadOS/watchOS/tvOS/visionOS）对比 Android（Linux 2.6/3.x/4.x/5.x 内核 + ART 虚拟机）、嵌入式 FreeBSD（如 PlayStation 4/5 系统软件分别以 FreeBSD 9.x/11.x 为基底、NetBSD 的路由器固件）、Windows Phone（Windows NT 内核，Windows Phone 8 于 2012 年起改用）。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4130] 卷“第12卷-macos的bsd遗产”第 250 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

<!-- 整改留痕 2026-09-13：按核查报告 P1 回填史观占位，映射 25 条总纲权威表（依据本章要点与辨析字段）。 -->
- 总纲 4“分离聚合是永恒规律”——Darwin/XNU 自 macOS 向 iOS/iPadOS/watchOS/tvOS/visionOS 的扩散是同一内核谱系的多路分离；嵌入式端完整源码不公开又使各分支与 macOS 主线之间只剩单向的源码参照（以 macOS 版为基底），分离之后的再聚合通道实际收窄。
- 总纲 8“本体论上各方平等”——iOS（XNU）、Android（Linux）、PlayStation（FreeBSD 基底）、NetBSD 路由器固件等嵌入式系统在本体论上地位相等；市场份额与装机规模差异是商品化结果，不构成技术优劣序列。
- 总纲 11“商品是形式主义”——iOS 的“小份额大规模”（全球份额约 28% 而部署达 18 亿台）表明 BSD 谱系在消费市场的最大部署经由商品形式实现，而非以开源社区名义实现；商品形式遮蔽了其 BSD 渊源。

## 辨析

- iOS 的多任务实现与桌面 BSD 的多任务实现存在根本差异——iOS 4 的 “多任务” 是 API 限制的伪多任务（仅音频、VoIP、定位等特定 API 可后台执行），非 BSD 进程调度的完整多任务。此差异是 Apple 的工程选择（省电与安全），非 BSD 层的技术限制——BSD 层的 `fork`、`exec`、`sched_*` 系统调用本身支持完整多任务，iOS 在其上施加了策略限制
- iOS 内核 “开源” 与 “闭源” 的边界须明确——Darwin 的 macOS 版本开源（APSL 2.0），iOS 版本基于 macOS Darwin 但附加闭源的移动框架（UIKit 移动版、SpringBoard 等）。因此 iOS 内核可追溯至公开的 XNU 源码，但其完整构建不可复现，考据上须以 macOS 端 Darwin 源码为间接参照并标注此局限。
- iOS 的市场份额与 Android 的市场份额对比须分开论述——2024 年 iOS 全球市场份额约 28%、Android 约 70%（StatCounter 数据），但 iOS 的 BSD 层部署规模（18 亿台）仍远超任何其他 BSD 派生系统（FreeBSD 服务器装机量约 400 万台、macOS 约 1 亿台）。此 “小份额大规模” 现象是 iOS 作为 BSD 谱系成员的独特定位——BSD 谱系在消费市场的最大部署经由商品形式实现，而非以开源社区的名义实现。

## 文献

- Apple Inc. iOS 4 Software Update [EB/OL]. (2010-06-21). Apple Press Release; Apple Inc. iOS Application Programming Guide [Z]. Apple Developer Documentation, 2010-2013; Apple Inc. iPhone 5s Technical Specifications [EB/OL]. (2013-09-10). Apple Press Release.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 2007-2010 年间：294 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。
- Apple Inc. Apple Security Research Device Program [EB/OL]. (2020-07-15). Apple Security Blog; Apple Open Source. Darwin Source Releases [EB/OL]. <https://opensource.apple.com/releases/>; GitHub. apple-oss-distributions/xnu [EB/OL]. <https://github.com/apple-oss-distributions/xnu>.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 2010-2010 年间：53 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。
- Apple Inc. Q1 FY2024 Financial Results [EB/OL]. (2024-02-01). Apple Investor Relations; Google. Android Platform Distribution Statistics [EB/OL]. <https://developer.android.com/about/dashboards>; StatCounter. Global Mobile Operating System Market Share [EB/OL]. <https://gs.statcounter.com/os-market-share/mobile/worldwide>.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1985-2026 年间：2,012 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。
