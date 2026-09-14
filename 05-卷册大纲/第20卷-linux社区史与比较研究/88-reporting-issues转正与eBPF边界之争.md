# 88 【Linux社区】reporting-issues转正与eBPF边界之争

> 来源：ksummit-discuss p140（50 封全读，2014-05-04 至 2022-06-17，reporting-issues.rst 转正收尾、ksummit 列表迁移与 lore 归档定论、2022 峰会 CFP、2022 eBPF 边界之争、2014 档案信）
> 判定：44 CAND / 6 NV。主题分布：报告文档全文张贴 1、Greg认可分步指南 1、Greg认可文档转正 1、PM依赖机制之辩 1、TLDR重写张贴 1、Greg认可新TLDR 1、Corbet评审TLDR 1、stable报告地址定则 1、归档停滞报告 1、新归档地址澄清 1、LWN归档可回填 1、旧列表废弃定论 1、staging提速之辩 1、TAB选举催票公告 1、未初始化警告之失 1、Smatch排序提案 1、编译器分析局限论 1、cppcheck查泄漏 1、Coverity误报之弊 1、2022峰会CFP 1、eBPF边界提案 1、HID用户态之困 1、Kosina澄清立场 1、gatekeeper合并之问 1、eBPF钩子即API 1、MGLRU的BPF钩子 1、tracepoint前车之鉴 1、维护者角色提案 1、hidraw作者自省 1、taint大锤提案 1、eBPF二进制分发 1、HID eBPF视作UAPI 1、回归追踪议题书 1、rebase实践之辩 1、峰会补充场提案 1、嵌入式以修代报 1、eBPF即模块论 1、eBPF稳定性折中 1、上游bpf程序库 1、反专有模块策略 1、eBPF成稳定后门 1、eBPF树内托管 1、维护者学习负担 1、stable五线之弊 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p140（实锚 pk 351206-351255）的逐封提取（44 CAND / 6 NV），全 44 块采用**单行摘要体例**（丙型）：每块由“## 88.x 题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 88.1 报告文档全文张贴

- 【Linux社区】Leemhuis 续贴 reporting-issues.rst 后半段全文（decode_stacktrace.sh、taint 检查、回归二分、高优先级问题专节），宣布拟于下个合并窗口删除 reporting-bugs.rst `<!-- ROW_MINE: ksummit-discuss.messages.351206 -->`

## 88.2 Greg认可分步指南

- 【Linux社区】stable 维护者 Greg KH 复 [2/5] 明示 “Looks good to me, no objections from my side”，为文档转正征求异议程序的肯定回应 `<!-- ROW_MINE: ksummit-discuss.messages.351207 -->`

## 88.3 Greg认可文档转正

- 【Linux社区】Greg KH 对转正 RFC 再表态无异议，称 “a great resource”，并宽慰不必求一次涵盖全部常见错误 `<!-- ROW_MINE: ksummit-discuss.messages.351208 -->`

## 88.4 PM依赖机制之辩

- 【Linux社区】2014 KS 议题存档：Hilman 论断仅 clk_enable 不足以唤醒供时钟设备，主张以 runtime PM get/put 为中心，V4L2 已用 DT phandle 建模数据流依赖 `<!-- ROW_MINE: ksummit-discuss.messages.351211 -->`

## 88.5 TLDR重写张贴

- 【Linux社区】因他人批评 stable/longterm 回归流程过繁，Leemhuis 整体重写 TLDR 并贴全文：stable 回归径报 stable 邮件列表并附 lore 检索指引 `<!-- ROW_MINE: ksummit-discuss.messages.351212 -->`

## 88.6 Greg认可新TLDR

- 【Linux社区】Greg KH 对重写版 TLDR 表态 “looks good to me”，构成转正评审同意记录的一部分 `<!-- ROW_MINE: ksummit-discuss.messages.351213 -->`

## 88.7 Corbet评审TLDR

- 【Linux社区】Corbet 肯定 “much improved - concise is good”，并建议将报告送达地址直接写入 TLDR 免用户检索 `<!-- ROW_MINE: ksummit-discuss.messages.351214 -->`

## 88.8 stable报告地址定则

- 【Linux社区】Greg KH 明确定则：报 stable 回归用 “stable@vger.kernel.org” 即可，无需另 CC 维护者个人 `<!-- ROW_MINE: ksummit-discuss.messages.351215 -->`

## 88.9 归档停滞报告

- 【Linux社区】Geert 报告 lore.kernel.org/ksummit-discuss/ 归档停在 2021 年 3 月，pipermail 同样无更新 `<!-- ROW_MINE: ksummit-discuss.messages.351217 -->`

## 88.10 新归档地址澄清

- 【Linux社区】Konstantin 澄清旧名已废弃，新归档位于 lore.kernel.org/ksummit/ `<!-- ROW_MINE: ksummit-discuss.messages.351218 -->`

## 88.11 LWN归档可回填

- 【Linux社区】Corbet 指出 LWN 存有完整归档（archive.lwn.net:8080/ksummit-discuss/），愿供 Konstantin 回填 lore `<!-- ROW_MINE: ksummit-discuss.messages.351219 -->`

## 88.12 旧列表废弃定论

- 【Linux社区】Konstantin 定论 ksummit-discuss@lists.linuxfoundation.org 已废弃、正典地址为 ksummit@lists.linux.dev，拟对旧列表设隐藏与紧急管制加自动回复 `<!-- ROW_MINE: ksummit-discuss.messages.351220 -->`

## 88.13 staging提速之辩

- 【Linux社区】2014 存档：staging 维护者 Greg KH 论断 staging 未加快内核其他部分开发并索要数据；指出企业内核用户要数年后才用上新特性 `<!-- ROW_MINE: ksummit-discuss.messages.351222 -->`

## 88.14 TAB选举催票公告

- 【Linux社区】Abbott 通告 2021 TAB 选举 9 月 23 日 16:00（GMT-4）截止，缺票联络 tab-elections@lists.linuxfoundation.org，资格为 2020-21 年三个带 SoB 等标签的提交 `<!-- ROW_MINE: ksummit-discuss.messages.351223 -->`

## 88.15 未初始化警告之失

- 【Linux社区】Carpenter 论述 commit 78a5255ffb6a 关停 GCC 未初始化警告后缺陷全赖他与 Nathan 复审 Smatch/Clang 拦截，循环边界误报为最大痛点，盼将来重启 GCC 警告 `<!-- ROW_MINE: ksummit-discuss.messages.351224 -->`

## 88.16 Smatch排序提案

- 【Linux社区】Lawall 提议 Smatch 对结果标注可能误报，或按真阳性概率排序输出 `<!-- ROW_MINE: ksummit-discuss.messages.351225 -->`

## 88.17 编译器分析局限论

- 【Linux社区】Arnd 论断此类检测受停机问题所限无法完美：clang 可靠但止于函数边界，gcc 内联变化致误报激增，gcc-12 新静态分析选项或可入 CI `<!-- ROW_MINE: ksummit-discuss.messages.351226 -->`

## 88.18 cppcheck查泄漏

- 【Linux社区】Shuah 报告 cppcheck 有效发现 kselftest 错误路径的文件指针泄漏，修复补丁在途，并提议纳入 LPC 内核测试与可靠性小型会议讨论 `<!-- ROW_MINE: ksummit-discuss.messages.351227 -->`

## 88.19 Coverity误报之弊

- 【Linux社区】Kozlowski 指 of_device_get_match_data() 经 OF 匹配实际不会返回 NULL，Coverity 逼出的 NULL 检查属无谓修补，半数驱动加了、半数没加 `<!-- ROW_MINE: ksummit-discuss.messages.351228 -->`

## 88.20 2022峰会CFP

- 【Linux社区】Ts'o 通告：维护者峰会 9 月 15 日 Dublin 邀请制限 30 人、由 Linus 出核心名单，Kernel Summit 为 LPC 并行赛道，6 月 19 日前以 [TECH TOPIC] 双渠道交题；program 委员会为 Greg KH、Axboe、Ts'o、Arnd、Corbet `<!-- ROW_MINE: ksummit-discuss.messages.351229 -->`

## 88.21 eBPF边界提案

- 【Linux社区】Kosina 提会划定 eBPF 可为边界：整驱动 eBPF 化将损可维护性、发行版恐失控于内核上下文，并类比已证明不可行的 UDI 概念 `<!-- ROW_MINE: ksummit-discuss.messages.351230 -->`

## 88.22 HID用户态之困

- 【Linux社区】Walleij 爆料其 2018 Razer 键盘驱动被推给用户态项目 razer_test 而 Fedora 都未打包，自述 libmtp 经验，称今日会改做内核驱动并明言站 Hellwig 一边 `<!-- ROW_MINE: ksummit-discuss.messages.351231 -->`

## 88.23 Kosina澄清立场

- 【Linux社区】Kosina 澄清不反对 HID-BPF 本身、只求跨子系统抽象边界；直言“更倾向把驱动收进内核”，且不会要求 Walleij 把 Razer 驱动改写成 eBPF `<!-- ROW_MINE: ksummit-discuss.messages.351232 -->`

## 88.24 gatekeeper合并之问

- 【Linux社区】2014 存档：Williams 将“速度”定义为交付用户的价值与测试量，追问合并摩擦能否用 gatekeeper 释放阀——滞留过久即回退——来降低合并延迟 `<!-- ROW_MINE: ksummit-discuss.messages.351233 -->`

## 88.25 eBPF钩子即API

- 【Linux社区】Jan Kara 论断 eBPF 钩子已成事实 API：内省/监控可容忍偶尔破坏，硬件启用则用户期待开箱即用，须区别对待 `<!-- ROW_MINE: ksummit-discuss.messages.351234 -->`

## 88.26 MGLRU的BPF钩子

- 【Linux社区】Corbet 援引 LSFMM MGLRU 讨论（LWN 894859）：拟以 BPF 钩子管理 LRU 代间页迁移，因“无人能给出通用最优解”；警惕以 BPF 逃避内核自身优化义务 `<!-- ROW_MINE: ksummit-discuss.messages.351235 -->`

## 88.27 tracepoint前车之鉴

- 【Linux社区】Kosina 论断“只承诺子集稳定”在 tracepoints 已被证伪——部分子系统为免被稳定性约束而系统性拒加 tracepoint `<!-- ROW_MINE: ksummit-discuss.messages.351236 -->`

## 88.28 维护者角色提案

- 【Linux社区】Bacik 提案：技术分歧激烈时由维护者或技术领袖介入定向以免关系破裂，并以自动化卸载合并复审等机械事务缓解维护者倦怠 `<!-- ROW_MINE: ksummit-discuss.messages.351238 -->`

## 88.29 hidraw作者自省

- 【Linux社区】Kosina 以 hidraw 原作者身份称其“本意为调试与微调，未料用户态驱动爆发依赖”，libusb 同病；赞成 eBPF 走 perf 式树内同轨发布模式 `<!-- ROW_MINE: ksummit-discuss.messages.351239 -->`

## 88.30 taint大锤提案

- 【Linux社区】Walleij 提议加载非 in-tree eBPF 程序即 taint 内核，迫使其上游化，称此为“阻止碎片化的大锤” `<!-- ROW_MINE: ksummit-discuss.messages.351240 -->`

## 88.31 eBPF二进制分发

- 【Linux社区】Tissoires 方案：向用户同时提供源码与二进制 blob，可校验二进制出自该源码、维护者可签名；支持 taint 主张，最终留待 Alexei 定夺加载路径区分 `<!-- ROW_MINE: ksummit-discuss.messages.351241 -->`

## 88.32 HID eBPF视作UAPI

- 【Linux社区】Tissoires 表态“HID 中几乎所有 eBPF 都视作 UAPI、从第一天起文档化”，并克制不逐版改动参数，回应 Hellwig “UDI 式稳定驱动 ABI” 的质疑 `<!-- ROW_MINE: ksummit-discuss.messages.351242 -->`

## 88.33 回归追踪议题书

- 【Linux社区】Leemhuis 提 KS 议题：regzbot 现状、简单回归修复滞留 -next 数周、bugzilla 报告无人转发（引 Konstantin 让开发者负责 bugzilla 之议）、Link: 标签靠自觉并提议 checkpatch 警告 `<!-- ROW_MINE: ksummit-discuss.messages.351243 -->`

## 88.34 rebase实践之辩

- 【Linux社区】2014 存档：Bottomley 称其树基本线性“实践中确实会 rebase”——git 树测试出问题即弃整系列，迟到的修复合入原提交并注记，不迷信保留历史 `<!-- ROW_MINE: ksummit-discuss.messages.351244 -->`

## 88.35 峰会补充场提案

- 【Linux社区】Leemhuis 为回归追踪另提 MAINTAINERS SUMMIT 补充场，聚焦 -next 滞留、bugzilla、CI 回归等核心维护者议题，称 2017 年同模式行之有效 `<!-- ROW_MINE: ksummit-discuss.messages.351245 -->`

## 88.36 嵌入式以修代报

- 【Linux社区】Mark Brown 论断嵌入式界大量回归以修复补丁形式直接到达、没有独立报告，解释 Leemhuis 漏见众多回归修复之因 `<!-- ROW_MINE: ksummit-discuss.messages.351246 -->`

## 88.37 eBPF即模块论

- 【Linux社区】Rostedt 主张颁令“eBPF 即花哨模块、无 ABI”；披露 sched_switch tracepoint 加参数曾被迫为 eBPF 用户重排但“不得成先例”，忧 eBPF 过度侵入 `<!-- ROW_MINE: ksummit-discuss.messages.351247 -->`

## 88.38 eBPF稳定性折中

- 【Linux社区】Bottomley 引 Sysdig 等弃专有模块转 eBPF 之例，称“完全不稳定”立场站不住且将瓦解反专有模块论据，主张讨论“略不稳定的稳定” `<!-- ROW_MINE: ksummit-discuss.messages.351248 -->`

## 88.39 上游bpf程序库

- 【Linux社区】Rostedt 提议在 tools/bpf 收容“上游 bpf 程序”并视 bpf 同模块对待；警告一旦承诺部分稳定性即成“永远的枷锁” `<!-- ROW_MINE: ksummit-discuss.messages.351249 -->`

## 88.40 反专有模块策略

- 【Linux社区】Bottomley 陈述反专有模块“胡萝卜加大棒”长期策略（大棒即 API 不稳定常破坏），称兼容负担或被高估，树内托管全 eBPF 生态“不可扩展” `<!-- ROW_MINE: ksummit-discuss.messages.351250 -->`

## 88.41 eBPF成稳定后门

- 【Linux社区】Rostedt 断言 eBPF 正成为专有模块获取稳定 API 的新途径，已钩住所有未标 notrace 的函数，预言无边界将引发绵延的“破坏我的 bpf 程序请回退”之争 `<!-- ROW_MINE: ksummit-discuss.messages.351251 -->`

## 88.42 eBPF树内托管

- 【Linux社区】Kosina 坚持树内按子系统托管 eBPF 程序为“最好且唯一选项”：镜像常规维护者结构、由子系统维护者自担同步之责，即“perf 模式的放大版”，否则程序散落全网致用户怨怼 `<!-- ROW_MINE: ksummit-discuss.messages.351253 -->`

## 88.43 维护者学习负担

- 【Linux社区】Walleij 以 DT 绑定 YAML 化类比支持按子系统托管 eBPF 程序，但警告维护者刚学会 YAML 又要学 eBPF 语法，Rust 亦已在路上 `<!-- ROW_MINE: ksummit-discuss.messages.351254 -->`

## 88.44 stable五线之弊

- 【Linux社区】2014 存档：Li Zefan 列 LTS 五线并行之弊（2.6.32 Willy Tarreau、3.2 Ben Hutchings、3.4/3.10 Greg、3.12 Jiri Slaby），DaveM 须备 5 线补丁，3.4.x 较 3.2.x 缺数百修复，提议 known_issues.txt 与 stable 专项测试 `<!-- ROW_MINE: ksummit-discuss.messages.351255 -->`
