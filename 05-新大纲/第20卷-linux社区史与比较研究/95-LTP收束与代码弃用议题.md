# 95 【Linux社区】LTP收束与代码弃用议题

> 来源：ksummit-discuss p147（23 封全读，2014-05-05 至 2014-06-11，库尾页，LTP 收束与 QA 沟通、KS 邀请流程与黑名单经济、代码弃用议题（PVH 与最小兼容层）、Christoph Lameter mm 层重设计六大议题）
> 判定：21 CAND / 2 NV。主题分布：LTP清理期高修复率 1、phandle翻译核心难题 1、tests repo聚合构想 1、黑名单经济批判 1、commit-id作feature flag 1、聚合repo入树之问 1、无线工作坊提案 1、SORBS条目之驳 1、QA与内核沟通论 1、API无人测过证言 1、弃用ad hoc之叹 1、第三固件接口之忧 1、PVH弃用议题全文 1、最小兼容层弃用论 1、硬件弃用之限 1、X版编译不过可删则 1、mm层重设计六大议题 1、uio已足之问 1、不依赖犯错的弃用方案 1、古老文件系统入FUSE设想 1、低端mm开销之问 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p147（实锚 pk 351556-351578）的逐封提取（21 CAND / 2 NV），全 21 块采用**单行摘要体例**（丙型）：每块由“## 95.x 题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 95.1 LTP清理期高修复率

- 【Linux社区】Cyril Hrubis：LTP 正清理审查遗留代码、每版覆盖与修复量大增——对老内核亦应跑最新版 `<!-- ROW_MINE: ksummit-discuss.messages.351556 -->`

## 95.2 phandle翻译核心难题

- 【Linux社区】Rafael 澄清 Pantelis：动态 PCI DT 节点创建≠DT overlay on ACPI——那是 PCI 的 DT 支持；核心难题是 phandle 与 ACPI 设备对象指针（路径）的双向翻译 `<!-- ROW_MINE: ksummit-discuss.messages.351557 -->`

## 95.3 tests repo聚合构想

- 【Linux社区】Bottomley：bisect 应支持排除路径（现排除 test 顶层目录繁琐）；须对每个内核（含 stable）跑最新 LTP——或需一个从各分散测试拉取的 tests repo、一处取最新 `<!-- ROW_MINE: ksummit-discuss.messages.351558 -->`

## 95.4 黑名单经济批判

- 【Linux社区】Bottomley：自己的 pull request 曾进 Linus 的 Gmail 垃圾箱直至 Linus 加白名单；Novell 曾用的付费反垃圾把 hansenpartnership.com 网段标垃圾且移除流程全无效——“只对收钱感兴趣”；私有黑名单难查难除 `<!-- ROW_MINE: ksummit-discuss.messages.351559 -->`

## 95.5 commit-id作feature flag

- 【Linux社区】Hiramatsu：可用 git commit-id 作其他子系统的 feature flag——stable 树补丁描述带“[ Upstream commit <commit-id> ]”标签可查哪些修复已合入 `<!-- ROW_MINE: ksummit-discuss.messages.351561 -->`

## 95.6 聚合repo入树之问

- 【Linux社区】Hiramatsu 附议 tests repo 构想（脚本/chef 类拉取构建）并问“那为何不放内核树里？” `<!-- ROW_MINE: ksummit-discuss.messages.351562 -->`

## 95.7 无线工作坊提案

- 【Linux社区】Linville 提议 KS 期间设无线网络工作坊（较 LPC miniconf 更内核向）：固件 dump 处理框架、nl80211 vendor 命令回顾、WFDS 与 HotSpot 2.0、无线监管代码（“谁懂它”） `<!-- ROW_MINE: ksummit-discuss.messages.351563 -->`

## 95.8 SORBS条目之驳

- 【Linux社区】Woodhouse：SORBS 记录是 2011 历史条目、当前未激活不应相关；请 Ted 若 Gmail 有回应解释 Randy 信被拒之因 `<!-- ROW_MINE: ksummit-discuss.messages.351564 -->`

## 95.9 QA与内核沟通论

- 【Linux社区】Cyril Hrubis：拉取运行脚本容易、配置与“谁需跑哪部分”难——主因是沟通与信息散落；建议 wiki 总结各维护中测试套件（目的/结构）；linux-api 列表与 API 变更 CC（谢 Kerrisk）是大进步；仍忧内核开发者已写的测试未流转 LTP、重复造轮子 `<!-- ROW_MINE: ksummit-discuss.messages.351565 -->`

## 95.10 API无人测过证言

- 【Linux社区】Michael Kerrisk（man-pages 维护者）反证：多次为 API 写测试才发现最基础的测试失败——“包括内核开发者在内的任何人显然都没测过该特性” `<!-- ROW_MINE: ksummit-discuss.messages.351566 -->`

## 95.11 弃用ad hoc之叹

- 【Linux社区】hpa 附议 Konrad 议题：现在弃用全然 ad hoc——“X 版没编译过且无人注意”；受控弃用难做——“third rail 议题但让我们处境艰难” `<!-- ROW_MINE: ksummit-discuss.messages.351567 -->`

## 95.12 第三固件接口之忧

- 【Linux社区】Rafael 回 Ben：翻译放驱动会复制大量代码——须有一层自动翻译；绑定不应依赖翻译——驱动请求“fred”属性就应拿到而无论固件接口；否则每种新固件接口都要全改驱动 `<!-- ROW_MINE: ksummit-discuss.messages.351568 -->`

## 95.13 PVH弃用议题全文

- 【Linux社区】Konrad Rzeszutek Wilk 议题全文：移除用户仍在用但有更好代码的代码——Xen PVH 将使部分 pvops 与 lguest 过时（更快更少代码、需新硬件）；老硬件与低功耗者受难；迁移路径在但“一拔代码人们从四面八方出来追打我们”；X=stable+5 `<!-- ROW_MINE: ksummit-discuss.messages.351569 -->`

## 95.14 最小兼容层弃用论

- 【Linux社区】Josh Triplett：remap_file_pages 是好例子——旧用户态须“能用”但不必快、不必整合新特性；应更多以最小兼容层弃用内核部件 `<!-- ROW_MINE: ksummit-discuss.messages.351570 -->`

## 95.15 硬件弃用之限

- 【Linux社区】hpa：兼容层方案只适用于弃用的有限侧面——更多弃用与具体硬件绑定 `<!-- ROW_MINE: ksummit-discuss.messages.351571 -->`

## 95.16 X版编译不过可删则

- 【Linux社区】Guenter：与“在用但渐少”不同——在用就留；但希望有规则：X 版（两年发布量？）编译不过的文件/驱动可移除 `<!-- ROW_MINE: ksummit-discuss.messages.351572 -->`

## 95.17 mm层重设计六大议题

- 【Linux社区】Christoph Lameter [CORE TOPIC] 全文：大阶页与碎片化（hugepage 511 个无用 page struct、bootmem/CMA 多分配器）；巨量 CPU（power8 160 cpu/4 NUMA 节点、per-cpu 状态聚合贵——提议子系统绑定 PCI-E root complex 所属 NUMA 节点）；Zone 不反映设备能力、MOVABLE 页因 pin 不动；性能特征（NUMA/TLB/DIMM 缓存）未利用；Swap 无人想要（Android 保存应用状态思路更好）；页缺页滥用与 mlock 之惑（OSV 式单进程、“MS-DOS 式 monitor 让路”、dynticks 在路上）；直连硬件与抽象兼得之问 `<!-- ROW_MINE: ksummit-discuss.messages.351573 -->`

## 95.18 uio已足之问

- 【Linux社区】Greg KH 回 Lameter：要哪种设备？uio 接口已可从用户态直连硬件——还需要什么 `<!-- ROW_MINE: ksummit-discuss.messages.351575 -->`

## 95.19 不依赖犯错的弃用方案

- 【Linux社区】Bjorn Helgaas：X 年编译不过可移除（X 可协商）多数人同意；但编译坏是某处错误的后果、可由此推断没人在乎——最好有不依赖人们随机犯错的方案 `<!-- ROW_MINE: ksummit-discuss.messages.351576 -->`

## 95.20 古老文件系统入FUSE设想

- 【Linux社区】Josh Triplett：硬件支持无用户态接口那种兼容顾虑；可否弃用古老文件系统、推入用户态 FUSE（多数只为取证而非性能）——还能缓解该代码潜在漏洞 `<!-- ROW_MINE: ksummit-discuss.messages.351577 -->`

## 95.21 低端mm开销之问

- 【Linux社区】Josh Triplett：低端亦须问 Linux mm 开销多大——1MB RAM 系统上跑标准 mm 子系统是否合理 `<!-- ROW_MINE: ksummit-discuss.messages.351578 -->`
