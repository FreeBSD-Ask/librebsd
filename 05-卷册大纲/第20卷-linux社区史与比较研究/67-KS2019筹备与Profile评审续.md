# 67 【Linux社区】KS2019筹备与Profile评审续

> 来源：ksummit-discuss p119（50 封全读，2019-05/06 KS2019 筹备+2018-11 Profile 评审链+2014 ACPI/DT 档案）
> 判定：47 CAND / 3 NV。主题分布：补丁前缀统计脚本 2、KS2014 ACPI与DT 5、多文件提交占比数据 1、可信评审人名单存废 1、评审名单维护难题 1、Profile模板设计细节 1、IRC频道替代名单 1、正式头衔促评审 1、Profile章节取舍 1、跟进节奏字段定名 1、Profile采纳率疑虑 1、采纳率疑虑之回应 1、Profile新规质疑 1、Profile目标澄清 1、IRC频道字段局限 1、IRC频道注释提案 1、KS2019启动公告 1、MS2019首轮邀请 1、KS2019议题CIFSD 1、KS2019议题UniLinux 1、KS2019议题IMS中断 1、KS2019议题ZRAM后端 1、KS2019议题KVA分配器 1、KS2019议题内联加密 1、KS2019议题入门课 1、KS2019议题MapleTree 1、UniLinux查重质询 1、MS2019议题沟通分析 3、MS2019议题清syzbot 5、沟通分析先行研究 3、KVA议题必要性质疑 1、沟通分析验证质疑 1、入门课议题否决 2。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p119（pk 350156-350205）的逐封提取（47 CAND / 3 NV），全 33 块采用**单行摘要体例**（丙型）：每块由“## 67.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 67.1 【Linux社区】补丁前缀统计脚本

- 【Linux社区】Rob Herring 赞同以 Jani 的 git log 脚本统计 subject prefix 作填充 MAINTAINERS 的起点，称“checkpatch is getting pretty unwieldy”，并指补丁触及多路径往往提示应拆分。 `<!-- ROW_MINE: ksummit-discuss.messages.350156 -->`
- 【Linux社区】Jani 回应 Perches 多文件不适用质疑：脚本可接受多文件参数给出近似前缀，“it took me all of five minutes to write that”，自认不完美但够用。 `<!-- ROW_MINE: ksummit-discuss.messages.350169 -->`

## 67.2 【Linux社区】KS2014 ACPI与DT

- 【Linux社区】Intel Hart 通报已原型验证 DT 节点到 ACPI DEVICE 1:1 映射（含嵌套子节点属性），方针是“fill the gaps in ACPI, not replace”，并请 Olof 推荐必须同时懂两套固件接口的驱动实例。 `<!-- ROW_MINE: ksummit-discuss.messages.350157 -->`
- 【Linux社区】Hart 表态“Agreed, well said”背书 Arnd 路线：统一命名属性 API 先覆盖仅用 memory/irq 的简单驱动，再渐进扩展到字符串、布尔、整型数组及 GPIO/DMA 通道。 `<!-- ROW_MINE: ksummit-discuss.messages.350168 -->`
- 【Linux社区】Hart 引 **gpio-keys.c** 证明存在无 struct device 对应的 DT 子节点，提出属性接口增设子节点参数（device_get_property 传 dev 与 child 两级）并配子节点迭代器的设计。 `<!-- ROW_MINE: ksummit-discuss.messages.350179 -->`
- 【Linux社区】Hart 主张增量改进 ACPI 而非弃用：支持把 ACPI SSDT 作为独立于板级固件的项加载并重扫命名空间，规范修改应允许描述规范未列设备类型；以其 MinnowBoard“动态基板”路线为据，认为比改走 DT 更保平台兼容性。 `<!-- ROW_MINE: ksummit-discuss.messages.350190 -->`
- 【Linux社区】Hart 论 pinctrl：嵌入式扩展中 pinctrl 与 PCI/USB 同级、需 OS 级更强控制，MinnowBoard-Max 仅能原生/GPIO 模式切换仍嫌不足；ACPI 规范修改应允许描述规范外设备，**pinctrl-baytrail.c** 可据新属性适配。 `<!-- ROW_MINE: ksummit-discuss.messages.350201 -->`

## 67.3 【Linux社区】多文件提交占比数据

- 【Linux社区】Julia Lawall 给出数据：v4.0 至 v4.19 间“18% of commits touch multiple .c files”、35% 提交触及多文件，回应 Perches 对前缀脚本不适用多文件补丁的质疑。 `<!-- ROW_MINE: ksummit-discuss.messages.350158 -->`

## 67.4 【Linux社区】可信评审人名单存废

- 【Linux社区】Leon 主张整节删除 Trusted Reviewers，称名单会令落选者觉得“untrusted”；Mauro 草拟准入线（每年 25 补丁加 50 次跨驱动评审），Leon 主张改为文档化 **get_maintainers.pl**。 `<!-- ROW_MINE: ksummit-discuss.messages.350159 -->`

## 67.5 【Linux社区】评审名单维护难题

- 【Linux社区】Leon 点出要害“someone needs to maintain such lists”，且把人移出名单绝非易事；Mauro 承认 MAINTAINERS 单文件格式容不下评审准入标准等自由文本。 `<!-- ROW_MINE: ksummit-discuss.messages.350160 -->`

## 67.6 【Linux社区】Profile模板设计细节

- 【Linux社区】Mauro 主张各 profile 链回模板而非复制不变文本；media 有 DTV/V4L2/CEC/media controller/遥控器 5 套 API，get_maintainers.pl 按 F: 标签无法分辨评审人；重发同题补丁反会被排到队列后方延后处理。 `<!-- ROW_MINE: ksummit-discuss.messages.350161 -->`

## 67.7 【Linux社区】IRC频道替代名单

- 【Linux社区】Dan 承认名单易被读成“untrusted”并解释本意是新人直接求助的第二意见渠道；Mauro 提议 profile 改指 IRC 频道，“Several subsystems use them in order to provide newbies some directions”。 `<!-- ROW_MINE: ksummit-discuss.messages.350162 -->`

## 67.8 【Linux社区】正式头衔促评审

- 【Linux社区】Mauro 转述有子系统反馈“giving someone a formal credit may actually help to get more reviews”（NeilBrown：头衔让人从“someone should”变“I should”），但移除评审人“will likely require some written policy”。 `<!-- ROW_MINE: ksummit-discuss.messages.350163 -->`

## 67.9 【Linux社区】Profile章节取舍

- 【Linux社区】Dan 接受删除 Time Zone/Office Hours 节（已有按天数周计的 Resubmit Cadence），同意各 profile 链回 handbook 模板即可，且不做层级式 profile。 `<!-- ROW_MINE: ksummit-discuss.messages.350164 -->`

## 67.10 【Linux社区】跟进节奏字段定名

- 【Linux社区】Dan 更正口误并定名“Follow-up Cadence”，明确该节将记录维护者偏好：私下 ping 或整套补丁重发到列表。 `<!-- ROW_MINE: ksummit-discuss.messages.350166 -->`

## 67.11 【Linux社区】Profile采纳率疑虑

- 【Linux社区】Jani 指出 MAINTAINERS 早有 C: 聊天 URI 字段但“Alas very few subsystems have added that”，并预言极少子系统会真写 subsystem profile。 `<!-- ROW_MINE: ksummit-discuss.messages.350170 -->`

## 67.12 【Linux社区】采纳率疑虑之回应

- 【Linux社区】Dan 称不担心采纳率：“If a few subsystems pick it up and contributors find it useful then it will naturally proliferate”，否则当初关于贡献者摸索本地政策之痛的担忧本就错置。 `<!-- ROW_MINE: ksummit-discuss.messages.350171 -->`

## 67.13 【Linux社区】Profile新规质疑

- 【Linux社区】Pavel Machek 批评“Sounds like a new rules to me”，令提交简单补丁更难，主张各子系统规则应相似或相同，记录“it is okay to be different”并无帮助。 `<!-- ROW_MINE: ksummit-discuss.messages.350172 -->`

## 67.14 【Linux社区】Profile目标澄清

- 【Linux社区】Dan 回应 Pavel：并非宣布“可以不同”而是承认流程本已不同；目标是跨子系统交换经验以期长期收敛、给新维护者可复制的模板、让提交者能查到子系统本地政策。 `<!-- ROW_MINE: ksummit-discuss.messages.350173 -->`

## 67.15 【Linux社区】IRC频道字段局限

- 【Linux社区】Mauro 通报 media 在 freenode 用双频道（#linuxtv 管数字电视、#v4l 管其余），单一 C: 字段无法说明各自用途，认为现有格式不适配。 `<!-- ROW_MINE: ksummit-discuss.messages.350174 -->`

## 67.16 【Linux社区】IRC频道注释提案

- 【Linux社区】Perches 提议在 C: 条目后加注释区分用途，如 “# only for digital tv #linuxtv” 与 “# everything else”。 `<!-- ROW_MINE: ksummit-discuss.messages.350175 -->`

## 67.17 【Linux社区】KS2019启动公告

- 【Linux社区】Ted 宣布 KS2019 在里斯本 Corinthia 酒店举行：KS 为 LPC track（9月9-11日），Maintainer's Summit 9月12日邀请制限 30 人；Linus 生成 18 人核心名单供程序委员会至少选 10 人；[TECH TOPIC] 与 [MAINTAINERS SUMMIT] 双轨投稿、5月31日前中稿免费入场；约半数 KS 时段留作 unconference；程序委员会为 Greg KH、Axboe、Corbet、Ts'o、Gleixner。 `<!-- ROW_MINE: ksummit-discuss.messages.350176 -->`

## 67.18 【Linux社区】MS2019首轮邀请

- 【Linux社区】首轮 15/30 席邀请已发出，取自 Linus 按 git 统计生成的名单；列名 16 人含 Linus Torvalds、Andrew Morton、David Miller、Ingo Molnar、Takashi Iwai、Stephen Rothwell 等，二轮改按提名产生。 `<!-- ROW_MINE: ksummit-discuss.messages.350177 -->`

## 67.19 【Linux社区】KS2019议题CIFSD

- 【Linux社区】Ted 转贴 Senozhatsky 议题：CIFSD 为树外内核态 SMB 服务器，自称极简且性能优于用户态方案，拟介绍架构与组件通信协议并探讨未来并入上游；议题截稿延至 6月3日。 `<!-- ROW_MINE: ksummit-discuss.messages.350178 -->`

## 67.20 【Linux社区】KS2019议题UniLinux

- 【Linux社区】VMware 陈铁军（Tiejun Chen）提议探索把 Linux 改造为 Unikernel 形态：内核与用户态同运行于内核态、轻量网络栈、压缩内存足迹，瞄准 IoT 与 Serverless，并称 Unikernel 较传统容器更小更快更安全。 `<!-- ROW_MINE: ksummit-discuss.messages.350180 -->`

## 67.21 【Linux社区】KS2019议题IMS中断

- 【Linux社区】Intel Megha Dey 提案 IMS：MSI/MSI-X 每设备上限 2048 向量且 probe 期一次性静态分配，SIOV 需支持超过 2048 个可分配设备接口 ADI，IMS 以设备特定存储（片上或主机内存）枚举 MSI 地址/数据对并把向量协商推迟到 probe 之后。 `<!-- ROW_MINE: ksummit-discuss.messages.350181 -->`

## 67.22 【Linux社区】KS2019议题ZRAM后端

- 【Linux社区】z3fold 作者 Vitaly Wool 提议解耦 ZRAM 与 zsmalloc、扩展 zpool API 以便按需选配后端：zbud 每页 2 对象、z3fold 每页 3 对象，低延迟但牺牲压缩比，称换用须待“a wider consensus”。 `<!-- ROW_MINE: ksummit-discuss.messages.350182 -->`

## 67.23 【Linux社区】KS2019议题KVA分配器

- 【Linux社区】Uladzislau Rezki 提交“Reworking of KVA allocator in Linux kernel”议题，正文极简仅附 ftp 站点上的 PDF 演讲稿链接，未写摘要细节。 `<!-- ROW_MINE: ksummit-discuss.messages.350183 -->`

## 67.24 【Linux社区】KS2019议题内联加密

- 【Linux社区】Google Satya Tangirala 提案：内联加密已入 UFS/eMMC 标准、Android SoC 渐普及，已发覆盖 block/UFS/f2fs/fscrypt 的 RFC 补丁集，拟议每 bio 传递密钥、device mapper 分层支持与软件回退，展望统一 fscrypt、dm-crypt、eCryptfs。 `<!-- ROW_MINE: ksummit-discuss.messages.350184 -->`

## 67.25 【Linux社区】KS2019议题入门课

- 【Linux社区】Tanish Shinde 提交“Anatomy Of The Linux Kernel”入门议题（系统调用、内存管理、VFS、网络栈等清单），自称已在 OSS+KubeCon+CloudNativeCon China 2019 讲授，附 GitHub 与个人站链接。 `<!-- ROW_MINE: ksummit-discuss.messages.350185 -->`

## 67.26 【Linux社区】KS2019议题MapleTree

- 【Linux社区】Howlett 与 Wilcox 提案 Maple Tree：红黑树需自写插入搜索且假设访存廉价、radix 树在 2 的幂对齐之外最差性能糟糕；Maple Tree 高效支持连续区间并可选追踪空闲区间，欲作页缓存基座还需搜索标记与 shadow 条目回收支持。 `<!-- ROW_MINE: ksummit-discuss.messages.350186 -->`

## 67.27 【Linux社区】UniLinux查重质询

- 【Linux社区】Ted 查问 UniLinux 提案与其 OSS NA 2017 洛杉矶演讲（sched.com/event/BDpy）有何实质差异，显示程序委员会对重复议题的把关。 `<!-- ROW_MINE: ksummit-discuss.messages.350187 -->`

## 67.28 【Linux社区】MS2019议题沟通分析

- 【Linux社区】Shuah 提议 MS2019 议题“Talking code or talking in code!”：邀 Polytechnique Montréal 博士生 Isabella Ferreira 讲 Sentimine（cregit 平台上分析开源社区沟通的插件），并做邮件语气小调查。 `<!-- ROW_MINE: ksummit-discuss.messages.350188 -->`
- 【Linux社区】Ted 质疑该议题更适合开放的 KS track：检索仅见 Ferreira 2019 OSLS 幻灯与 SEMotion_2019 论文且无录像，困惑 cregit（分析代码）与幻灯前 80% 的邮件文本分析有何关系。 `<!-- ROW_MINE: ksummit-discuss.messages.350191 -->`
- 【Linux社区】Shuah 详释动机：Ferreira 已投 LPC BOF 求真数据验证；流程为概览、2-3 封邮件正/负/中性语气调查、再比对工具结果；她观察工具“missing a subjective and context component”，社区邮件是养料数据，盼引导研究关注沟通清晰度。 `<!-- ROW_MINE: ksummit-discuss.messages.350196 -->`

## 67.29 【Linux社区】MS2019议题清syzbot

- 【Linux社区】Shuah 提议“Squashing bugs!”议题：syzbot 当时已修 1276、moderation 86、fix pending 62、未决 523 且最老开放 537 天；已把 syzbot 分析列为内核导师计划申请必做项并见效，拟把清理工作结构化。 `<!-- ROW_MINE: ksummit-discuss.messages.350189 -->`
- 【Linux社区】Laura Abbott 扩展议题范围：Fedora 恒量 bug 流由三名正式内核维护者轮看仍会遗漏，kernel.org bugzilla 报告亦常丢失，盼形成适用 syzbot 及其他高流量跟踪器的通用流程。 `<!-- ROW_MINE: ksummit-discuss.messages.350194 -->`
- 【Linux社区】Shuah 认可扩展范围：“I am hoping we can look at all bugs as well”，syzbot 只是讨论切入点。 `<!-- ROW_MINE: ksummit-discuss.messages.350198 -->`
- 【Linux社区】Kees Cook 指出看板仅以出现频次“turns red”、缺严重度（栈破坏/UAF 甚于 crash/WARN）与可达性（如“only reachable via CAP_NET_ADMIN”）分级；企业不愿资助持续抓虫，只想让开发者“focused on new things”；盼跟踪器间自动去重互引。 `<!-- ROW_MINE: ksummit-discuss.messages.350202 -->`
- 【Linux社区】5月29日首发版：仅述拟议 syzbot 议题与导师计划纳入 syzbot 分析之成效，无 5月30日详版的 1276/523 等统计，系同一提案的早期稿。 `<!-- ROW_MINE: ksummit-discuss.messages.350203 -->`

## 67.30 【Linux社区】沟通分析先行研究

- 【Linux社区】Wilcox 问 Sentimine 与去年 Dawn Foster 的内核邮件列表协作研究（OSSNA18 场次 FAON）相比如何，点出先行工作。 `<!-- ROW_MINE: ksummit-discuss.messages.350192 -->`
- 【Linux社区】Abbott 回忆 Foster 研究侧重影响沟通的属性（公司、时区等）而非沟通风格，邮件背后的情感基本未被涉及。 `<!-- ROW_MINE: ksummit-discuss.messages.350195 -->`
- 【Linux社区】Shuah 透露曾协助 Foster 早期研究，确认其聚焦跨公司跨时区协作，未涉及沟通情感分析。 `<!-- ROW_MINE: ksummit-discuss.messages.350197 -->`

## 67.31 【Linux社区】KVA议题必要性质疑

- 【Linux社区】Wilcox 直问 Rezki：“I was under the impression this work was complete. Are there any remaining issues to discuss?”质疑该提案已无可议之处。 `<!-- ROW_MINE: ksummit-discuss.messages.350193 -->`

## 67.32 【Linux社区】沟通分析验证质疑

- 【Linux社区】Perches 讥问“What does it mean to social her research?”，并以该短语为例断言“I expect validation will always be a difficult proposition”。 `<!-- ROW_MINE: ksummit-discuss.messages.350200 -->`

## 67.33 【Linux社区】入门课议题否决

- 【Linux社区】Leon Romanovsky 对“Anatomy Of The Linux Kernel”议题定性：“far too beginner topic for LPC and definitely for KS too”。 `<!-- ROW_MINE: ksummit-discuss.messages.350204 -->`
- 【Linux社区】Greg KH 附议：“this really is too much of a beginner-oriented talk for this conference”，与 Leon 一致否决该入门议题。 `<!-- ROW_MINE: ksummit-discuss.messages.350205 -->`
