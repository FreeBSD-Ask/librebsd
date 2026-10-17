# 148 【Linux社区】THE_REST四封与AI高标论

> 来源：ksummit 独有 p13（50 封全读，2021-04 至 2026-07，THE REST 迁离 LKML 四封交锋（lei 工作流/X: drivers/net 过滤/public-inbox 镜像前提）、AI 应设高于人类的标准（计算器 1% 类比）、被拒补丁同样有训练价值论、GPL 代码作 LLM 输入违背精神之问、Linus 接受 hpa cleanup 补丁集、OpenSSF 资助项目未公开之问、umn.edu 补丁整体回退价值质疑、SCSI 大量合入琐碎补丁现实）
> 判定：42 CAND / 8 NV。主题分布：Rust for Linux 1、加速器驱动用户态要求 2、THE REST 迁离 LKML 3、替换 Link 尾注 2、稳定分支提交标签增强 1、AI 与 LLM 在内核流程的角色 3、trivial 补丁接受政策 4、AI 补丁审查工具 1、TAB 投票程序 2、设备直通之害 1、扩展安全流程 1、next 中隐藏的提交 1、LLM 相关议题 1、内核文档技术议题 2、防止回归补丁被回移 1、Bugzilla 改进计划 1、Folios 峰会议题 1、cleanup.h 变量放置规则 1、每 cgroup 交换设备控制 1、CONFIG_HIGHMEM 退场共识 1、Rust 内核政策 2、C 聚合传递与 Rust 政策 2、Web of Trust 工作 1、工具生成内容文档指南 2、cdev 与 devm 释放问题 1、实现 malloc 1、维护者倦怠 1、stable 邮件数量 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p13 的逐封提取（2021-04 至 2026-07，42 CAND / 8 NV），全 28 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 148.1 Rust for Linux

- 【Linux社区】技术议题提案，介绍内核 Rust 支持的编译模型、文档、测试、工具链与编码规范。 `<!-- ROW_MINE: ksummit.messages.1905 -->`

## 148.2 加速器驱动用户态要求

- 【Linux社区】主张文档不足以把关，要求 API 进入主流发行版包，小众设备留在树外，门槛宁高勿低。 `<!-- ROW_MINE: ksummit.messages.1908 -->`
- 【Linux社区】分析 NPU 用户态碎片化，追问 TVM、TensorFlow、PyTorch 谁将成为标准栈。 `<!-- ROW_MINE: ksummit.messages.1966 -->`

## 148.3 THE REST 迁离 LKML

- 【Linux社区】给出用 lei 查询 lore 追溯补丁讨论的具体工作流与命令示例。 `<!-- ROW_MINE: ksummit.messages.1911 -->`
- 【Linux社区】反驳 LKML 无用论，要求先提供可靠的 public-inbox 整库镜像方案。 `<!-- ROW_MINE: ksummit.messages.1951 -->`
- 【Linux社区】提议在 THE REST 加 X: drivers/net/* 以减少数千封误投。 `<!-- ROW_MINE: ksummit.messages.1994 -->`

## 148.4 替换 Link 尾注

- 【Linux社区】澄清 b4 dig 需解码 Link 编码，URL 末段即转义 Message-ID。 `<!-- ROW_MINE: ksummit.messages.1914 -->`
- 【Linux社区】提议给 git log 加过滤旗标，可隐藏 Message-ID 或转换为 lore 链接。 `<!-- ROW_MINE: ksummit.messages.1929 -->`

## 148.5 稳定分支提交标签增强

- 【Linux社区】指出 Linus 与 James 对 Fixes 语义理解分歧，此即其欲解决的问题。 `<!-- ROW_MINE: ksummit.messages.1921 -->`

## 148.6 AI 与 LLM 在内核流程的角色

- 【Linux社区】认同 LLM 会产生难以察觉的错误，主张标注 LLM 参与程度便于维护者分配审查精力。 `<!-- ROW_MINE: ksummit.messages.1925 -->`
- 【Linux社区】主张对 AI 应设高于人类的标准，以计算器 1% 出错率类比不可接受。 `<!-- ROW_MINE: ksummit.messages.2056 -->`
- 【Linux社区】补充总结缺失的伦理维度，GPL 代码作 LLM 输入可能违背其精神而非条文。 `<!-- ROW_MINE: ksummit.messages.2065 -->`

## 148.7 trivial 补丁接受政策

- 【Linux社区】提出新议题“如何让提交者活得更轻松”，维护者偏好不一令提交流程痛苦。 `<!-- ROW_MINE: ksummit.messages.1937 -->`
- 【Linux社区】引用 UMN 作者澄清页并追问该研究是否违反会议的漏洞披露时限要求。 `<!-- ROW_MINE: ksummit.messages.2002 -->`
- 【Linux社区】质疑整体回退 umn.edu 补丁的价值，指出其中多为真实修复且审查才是关键。 `<!-- ROW_MINE: ksummit.messages.2045 -->`
- 【Linux社区】指出 SCSI 大量合入琐碎补丁的现实，建议把警告降到 W=2/W=3，并直言多数驱动实际无人维护。 `<!-- ROW_MINE: ksummit.messages.2073 -->`

## 148.8 AI 补丁审查工具

- 【Linux社区】指出 checkpatch 对 include/trace 应直接忽略并附此前提案的 lore 链接。 `<!-- ROW_MINE: ksummit.messages.1955 -->`

## 148.9 TAB 投票程序

- 【Linux社区】询问资格脚本输出与候选提名、投票资格的对应关系及是否适用于主席选举。 `<!-- ROW_MINE: ksummit.messages.1961 -->`
- 【Linux社区】澄清 eligible 与 ballots 两个集合的用途，确认该标准不适用于主席选举。 `<!-- ROW_MINE: ksummit.messages.1968 -->`

## 148.10 设备直通之害

- 【Linux社区】主张为固件接口划定跨子系统归属与访问控制准则，形成可指引厂商的文档。 `<!-- ROW_MINE: ksummit.messages.1964 -->`

## 148.11 扩展安全流程

- 【Linux社区】指出 linux-distros 已承担该协调职能但内核未将其纳入流程，附文档提交引用。 `<!-- ROW_MINE: ksummit.messages.1971 -->`

## 148.12 next 中隐藏的提交

- 【Linux社区】反驳强制入库 -next，指出上下层树失步会给 Stephen 造成冲突负担。 `<!-- ROW_MINE: ksummit.messages.1973 -->`

## 148.13 LLM 相关议题

- 【Linux社区】质疑训练数据只取被接受补丁，主张被拒补丁及其原因同样有训练价值。 `<!-- ROW_MINE: ksummit.messages.1983 -->`

## 148.14 内核文档技术议题

- 【Linux社区】讲述三个同名 Sphinx 项目造成的构建困惑，指帮助信息误导。 `<!-- ROW_MINE: ksummit.messages.1986 -->`
- 【Linux社区】详述 sphinx-pre-install 版本切换逻辑并以 openSUSE 打包实测论证必要性。 `<!-- ROW_MINE: ksummit.messages.2034 -->`

## 148.15 防止回归补丁被回移

- 【Linux社区】主张 Message-ID 用于被应用的补丁以便回复与追踪，Link 用于引发补丁的讨论。 `<!-- ROW_MINE: ksummit.messages.1992 -->`

## 148.16 Bugzilla 改进计划

- 【Linux社区】反驳批量批评，主张 Bugzilla 可搜索可追责、报告量低且分诊属另一议题。 `<!-- ROW_MINE: ksummit.messages.1996 -->`

## 148.17 Folios 峰会议题

- 【Linux社区】提议用共享活文档记录设计要点、剩余工作与 ack/nack 干系人，消除邮件考古。 `<!-- ROW_MINE: ksummit.messages.2006 -->`

## 148.18 cleanup.h 变量放置规则

- 【Linux社区】Linus 接受 hpa 补丁集提案，视其为改进并询问转换是否已获 ack。 `<!-- ROW_MINE: ksummit.messages.2008 -->`

## 148.19 每 cgroup 交换设备控制

- 【Linux社区】澄清议题走向并指导向 LPC MM 微会提交注册的具体步骤。 `<!-- ROW_MINE: ksummit.messages.2016 -->`

## 148.20 CONFIG_HIGHMEM 退场共识

- 【Linux社区】提供设备存量数据，OpenBlocks A7 有设计缺陷，Kirkwood NAS 仍有人在维护。 `<!-- ROW_MINE: ksummit.messages.2017 -->`

## 148.21 Rust 内核政策

- 【Linux社区】介绍 systemd 以成套 cleanup 类型注解编码清理逻辑的实践经验。 `<!-- ROW_MINE: ksummit.messages.2024 -->`
- 【Linux社区】探讨 Rice 定理与运行时检查的关系，分析 Rust 类型系统空洞与求解器缺陷。 `<!-- ROW_MINE: ksummit.messages.2069 -->`

## 148.22 C 聚合传递与 Rust 政策

- 【Linux社区】论证唯一可行别名模型是“勿假设不别名”，基于来源的规则或可扩展但不可强制。 `<!-- ROW_MINE: ksummit.messages.2033 -->`
- 【Linux社区】指出标准允许编译器向内存位置先写无关值或改写为读检写，代码须自行假设。 `<!-- ROW_MINE: ksummit.messages.2062 -->`

## 148.23 Web of Trust 工作

- 【Linux社区】追问 OpenSSF 资助项目需求与设计讨论为何未公开，批评 LF 延迟透明。 `<!-- ROW_MINE: ksummit.messages.2038 -->`

## 148.24 工具生成内容文档指南

- 【Linux社区】主张关键在工具使用方式而非工具本身，机械重命名属文档范围。 `<!-- ROW_MINE: ksummit.messages.2041 -->`
- 【Linux社区】给出 Reviewed-by，主张机械变换工具明确在文档范围内应予披露。 `<!-- ROW_MINE: ksummit.messages.2068 -->`

## 148.25 cdev 与 devm 释放问题

- 【Linux社区】介绍 GPIO 双抽象与引用计数、设备“麻木”等生命周期处理实践。 `<!-- ROW_MINE: ksummit.messages.2053 -->`

## 148.26 实现 malloc

- 【Linux社区】主张为无特殊限制的代码提供统一分配接口，以 zlib 需临时内存为例。 `<!-- ROW_MINE: ksummit.messages.2057 -->`

## 148.27 维护者倦怠

- 【Linux社区】反驳语气问题，指出真正的风险是测试噪音与无价值的 CI 邮件。 `<!-- ROW_MINE: ksummit.messages.2058 -->`

## 148.28 stable 邮件数量

- 【Linux社区】指出回移通知批次冗余令人困惑，请求伪短日志按作者排序。 `<!-- ROW_MINE: ksummit.messages.2059 -->`
