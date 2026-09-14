# 66 【Linux社区】SubsystemProfile评审与可信名单之争

> 来源：ksummit-discuss p118（50 封全读，2018-11-14/17 Dan Williams RFC 全评审链，夹杂 2014 档案与 XArray 追踪）
> 判定：48 CAND / 2 NV。主题分布：P:标签回收提案 1、Profile模板提案 1、首个样例Profile 1、P:条目清理与Ack 1、补丁主题行规则 1、media子维护者模式 1、ACPI属性机制 1、Profile工具联动 1、主题行经验之谈 1、样例Profile评审 1、文档受众分立 1、子系统句法红线 1、评审名单去重 1、样例受众批评 1、受众顺位共识 1、媒体样例Profile 1、属性接口设计 1、信任名单异议 1、社会接口辩护 1、名单改名折中 1、删除名单主张 1、名单定位之辩 1、P:条目去留考证 1、XArray报道动向 1、模板逐节评审 1、模板定位澄清 1、XArray适用边界 1、属性模式统一 1、XArray演讲定位 1、R:标签收编论 1、名单入选门槛 1、分文件评审名录 1、名单质疑交锋 1、工作流细节问答 1、主题行统计脚本 1、前缀方案反驳 1、作者逐点回应 1、API增长考证 1、quirk弊端辨析 1、v2改进承诺 1、受众改写承诺 1、名单扩展性质疑 1、media样例校对 1、名单辩护陈述 1、新人措辞建议 1、时区命名规范 1、挂名激励效应 1、media样例补正 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p118（pk 350106-350155）的逐封提取（48 CAND / 2 NV），全 48 块采用**单行摘要体例**（丙型）：每块由“## 66.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 66.1 【Linux社区】P:标签回收提案

- 【Linux社区】Dan Williams 的 RFC 补丁把废弃的 P:（Person）条目改 M: 或 E:（Entity），腾出 P: 指向 Subsystem Profile。 `<!-- ROW_MINE: ksummit-discuss.messages.350106 -->`

## 66.2 【Linux社区】Profile模板提案

- 【Linux社区】Dan 依 LPC2018 报告（event/2/59）提出 14 项维护政策模板，新增 **Documentation/maintainer/subsystem-profile.rst**。 `<!-- ROW_MINE: ksummit-discuss.messages.350107 -->`

## 66.3 【Linux社区】首个样例Profile

- 【Linux社区】Dan 以 libnvdimm 作首例：仅收邮件补丁、新特性 -rc5 前、重发周期 8 个工作日，Trusted Reviewers 列 Thumshirn/Kani/Moyer/Elliott。 `<!-- ROW_MINE: ksummit-discuss.messages.350108 -->`

## 66.4 【Linux社区】P:条目清理与Ack

- 【Linux社区】Mauro 主张直接删除旧 P: 条目而非改名，同意移除 LinuxTV 条目并给出 Acked-by。 `<!-- ROW_MINE: ksummit-discuss.messages.350109 -->`

## 66.5 【Linux社区】补丁主题行规则

- 【Linux社区】Julia Lawall 质询模板漏了补丁主题行规则，文件名到前缀的转换无公式可循。 `<!-- ROW_MINE: ksummit-discuss.messages.350110 -->`

## 66.6 【Linux社区】media子维护者模式

- 【Linux社区】Mauro 介绍媒体子系统子维护者制（V4L2/传感器/遥控/CEC/DVB/媒体控制器），子维护者兼任评审与提交，多数补丁有两个非作者 SOB。 `<!-- ROW_MINE: ksummit-discuss.messages.350111 -->`

## 66.7 【Linux社区】ACPI属性机制

- 【Linux社区】2014 年档案信：Darren Hart 指 _DSM 与命名对象碎片化，主张 ACPI 标准化属性机制统一解析（ELC/KS 原型经验）。 `<!-- ROW_MINE: ksummit-discuss.messages.350112 -->`

## 66.8 【Linux社区】Profile工具联动

- 【Linux社区】Mauro 提醒按 LPC 讨论需补丁教 **get_maintainers.pl** 打印子系统规则（Profile）标签。 `<!-- ROW_MINE: ksummit-discuss.messages.350113 -->`

## 66.9 【Linux社区】主题行经验之谈

- 【Linux社区】Geert 称自动化困难，自述惯用“git log --oneline”推导补丁主题前缀。 `<!-- ROW_MINE: ksummit-discuss.messages.350115 -->`

## 66.10 【Linux社区】样例Profile评审

- 【Linux社区】Geert 建议补 Trusted Reviewers 邮箱（仅一人列于 MAINTAINERS），并以 UTC 表示时区。 `<!-- ROW_MINE: ksummit-discuss.messages.350116 -->`

## 66.11 【Linux社区】文档受众分立

- 【Linux社区】Jani Nikula 主张贡献者与维护者文档分开，Documentation/maintainer 应严格面向维护者。 `<!-- ROW_MINE: ksummit-discuss.messages.350117 -->`

## 66.12 【Linux社区】子系统句法红线

- 【Linux社区】Julia 主张 Profile 记录用哪个树、是否抄送 stable 等会因句法被秒拒的各子系统规则。 `<!-- ROW_MINE: ksummit-discuss.messages.350118 -->`

## 66.13 【Linux社区】评审名单去重

- 【Linux社区】Mauro 主张评审者或用 R: 标签或入 Profile，重复维护会痛苦，且名单需可被 get_maintainers.pl 解析。 `<!-- ROW_MINE: ksummit-discuss.messages.350119 -->`

## 66.14 【Linux社区】样例受众批评

- 【Linux社区】Mauro 指 nvdimm 样例开头即面向维护者会吓退开发者，建议文末单列维护者专节并在 **index.rst** 加指针。 `<!-- ROW_MINE: ksummit-discuss.messages.350120 -->`

## 66.15 【Linux社区】受众顺位共识

- 【Linux社区】Julia 赞成开发者优先阅读，称新维护者多由老维护者引导而来、自带上下文。 `<!-- ROW_MINE: ksummit-discuss.messages.350121 -->`

## 66.16 【Linux社区】媒体样例Profile

- 【Linux社区】Mauro 发媒体子系统 Profile RFC：HTML 邮件被服务器自动拒收、patchwork.linuxtv.org 流程、子维护者列 Sakari/Hans/Laurent/Sean/Krufky。 `<!-- ROW_MINE: ksummit-discuss.messages.350122 -->`

## 66.17 【Linux社区】属性接口设计

- 【Linux社区】2014 年档案信：Darren Hart 展示 ASL Package 属性样例，主张 dev_get_property() 统一入口、反对再造中间格式。 `<!-- ROW_MINE: ksummit-discuss.messages.350123 -->`

## 66.18 【Linux社区】信任名单异议

- 【Linux社区】Leon Romanovsky 断言“trusted reviewers”名单弊大于利，未入选者会自感“untrusted”。 `<!-- ROW_MINE: ksummit-discuss.messages.350124 -->`

## 66.19 【Linux社区】社会接口辩护

- 【Linux社区】Tim Bird 反对按受众拆分，称文档记录群体间“social API”，两处维护易失同步且不利贡献者成长为维护者。 `<!-- ROW_MINE: ksummit-discuss.messages.350125 -->`

## 66.20 【Linux社区】名单改名折中

- 【Linux社区】Mauro 提议把“trusted reviewers”改称“most active reviewers”以缓和情绪。 `<!-- ROW_MINE: ksummit-discuss.messages.350126 -->`

## 66.21 【Linux社区】删除名单主张

- 【Linux社区】Leon 建议整节删除，称新维护者出自社区、自会判断该信任谁。 `<!-- ROW_MINE: ksummit-discuss.messages.350127 -->`

## 66.22 【Linux社区】名单定位之辩

- 【Linux社区】Tony Luck 定位该名单是给贡献者的提示，应被 **scripts/get_maintainer.pl** 采集以组织 Cc: 列表。 `<!-- ROW_MINE: ksummit-discuss.messages.350128 -->`

## 66.23 【Linux社区】P:条目去留考证

- 【Linux社区】Joe Perches 主张全部删除 P:，并考证 Simtec EB110ATX 已停产、EB2410ITX 仍在售但难有销量。 `<!-- ROW_MINE: ksummit-discuss.messages.350129 -->`

## 66.24 【Linux社区】XArray报道动向

- 【Linux社区】Corbet 回应 Walleij：不拟为 Matthew 的 XArray 演讲写 LWN 文章，录播约一两周后放出。 `<!-- ROW_MINE: ksummit-discuss.messages.350130 -->`

## 66.25 【Linux社区】模板逐节评审

- 【Linux社区】Frank Rowand 质疑“Pull requests accepted”表述、-rc 截止难预测、名单角色近 ombudsman，并自报 17:00-25:00 UTC 作息。 `<!-- ROW_MINE: ksummit-discuss.messages.350131 -->`

## 66.26 【Linux社区】模板定位澄清

- 【Linux社区】Tobin Harding 向 Jani 澄清：文档是给维护者的模板，由维护者生成的实例才面向贡献者。 `<!-- ROW_MINE: ksummit-discuss.messages.350132 -->`

## 66.27 【Linux社区】XArray适用边界

- 【Linux社区】Ted Ts'o 给出 LWN 745073 与内核文档链接，并总结稀疏数组、宽键空间哈希表尚不宜用 XArray。 `<!-- ROW_MINE: ksummit-discuss.messages.350133 -->`

## 66.28 【Linux社区】属性模式统一

- 【Linux社区】2014 年档案信：Darren Hart 主张 get_of_pdata()/get_acpi_pdata() 而非 if/else 碎片化 schema，称 ACPI 用户不愿重写驱动。 `<!-- ROW_MINE: ksummit-discuss.messages.350134 -->`

## 66.29 【Linux社区】XArray演讲定位

- 【Linux社区】Wilcox 确认 Ted 总结准确，称往届演讲求反馈、本次是“已合并、该用起来”，附 Plumbers2018 幻灯片链接。 `<!-- ROW_MINE: ksummit-discuss.messages.350135 -->`

## 66.30 【Linux社区】R:标签收编论

- 【Linux社区】Joe Perches 主张 trusted reviewers 应以 R: 条目写入 MAINTAINERS，get_maintainers 不应另觅他处。 `<!-- ROW_MINE: ksummit-discuss.messages.350136 -->`

## 66.31 【Linux社区】名单入选门槛

- 【Linux社区】Mauro 主张保留名单并给出量化标准草案：年贡献逾 25 补丁且年评审逾 50 个非本职补丁。 `<!-- ROW_MINE: ksummit-discuss.messages.350137 -->`

## 66.32 【Linux社区】分文件评审名录

- 【Linux社区】Mauro 主张评审者放子系统自有文件并写明入列标准，指 MAINTAINERS 格式容不下自由文本。 `<!-- ROW_MINE: ksummit-discuss.messages.350138 -->`

## 66.33 【Linux社区】名单质疑交锋

- 【Linux社区】Jan Kara 追问名单“如何帮新人”——难道直接抄送补丁？从列表挑补丁不够吗。 `<!-- ROW_MINE: ksummit-discuss.messages.350139 -->`

## 66.34 【Linux社区】工作流细节问答

- 【Linux社区】Mauro 称“先上邮件列表”唯迁 Github/Gitlab 才可能破例、通常 -rc7 后收尾，并自述 patchwork 中同主题旧版标 obsoleted、重发反被排后。 `<!-- ROW_MINE: ksummit-discuss.messages.350140 -->`

## 66.35 【Linux社区】主题行统计脚本

- 【Linux社区】Jani Nikula 贴 shell 脚本取最近 200 次提交的 top-5 主题前缀，建议懂 Perl 者改成 checkpatch 检查。 `<!-- ROW_MINE: ksummit-discuss.messages.350141 -->`

## 66.36 【Linux社区】前缀方案反驳

- 【Linux社区】Joe Perches 指统计脚本对多文件补丁失效，建议 basename(dirname) 加 MAINTAINERS 主题文法，并仿 **spdxcheck.py** 独立成脚本。 `<!-- ROW_MINE: ksummit-discuss.messages.350143 -->`

## 66.37 【Linux社区】作者逐点回应

- 【Linux社区】Dan Williams 提议增设 Review Forum 节应对 web 工具迁移，澄清 -rc5 是开始推回点，承诺剔除 should 措辞并把该节更名 Review Tags Requirement。 `<!-- ROW_MINE: ksummit-discuss.messages.350144 -->`

## 66.38 【Linux社区】API增长考证

- 【Linux社区】2014 年档案信：Kerrisk 纠正 sched_getattr/sched_setattr 系 3.14 加入，指 fallocate 新模式、cgroup、user ns 才是膨胀主因，自报 man7.org/tlpi/api_changes 追踪页。 `<!-- ROW_MINE: ksummit-discuss.messages.350145 -->`

## 66.39 【Linux社区】quirk弊端辨析

- 【Linux社区】2014 年档案信：Darren Hart 附和 BenH 对总线 quirk 机制的批评，提出 dev_get_property_gpiod(“volume_up”) 直取描述符的设想。 `<!-- ROW_MINE: ksummit-discuss.messages.350146 -->`

## 66.40 【Linux社区】v2改进承诺

- 【Linux社区】Dan Williams 承诺 v2 前先与四位 trusted reviewers 确认挂名、改用时区 UTC 表示，并说明名单定位是维护者无暇时的“第二意见”。 `<!-- ROW_MINE: ksummit-discuss.messages.350147 -->`

## 66.41 【Linux社区】受众改写承诺

- 【Linux社区】Dan Williams 承诺改写描述文本：模板面向维护者、子系统实例面向贡献者，并采纳文末维护者专节建议。 `<!-- ROW_MINE: ksummit-discuss.messages.350148 -->`

## 66.42 【Linux社区】名单扩展性质疑

- 【Linux社区】Rodrigo Vivi 附议 Leon：小圈子名单不可扩展、令人过载且难维护，评审应来自所有人、由提交者把关。 `<!-- ROW_MINE: ksummit-discuss.messages.350149 -->`

## 66.43 【Linux社区】media样例校对

- 【Linux社区】Randy Dunlap 大量勘误之余主张仅列姓名是“半个联系方式”，应补邮箱。 `<!-- ROW_MINE: ksummit-discuss.messages.350150 -->`

## 66.44 【Linux社区】名单辩护陈述

- 【Linux社区】Dan Williams 承认“未顾及不幸解读”，阐明目标：助新贡献者以“Hey, Alice, Bob seems busy”式直邮撬动更多评审。 `<!-- ROW_MINE: ksummit-discuss.messages.350151 -->`

## 66.45 【Linux社区】新人措辞建议

- 【Linux社区】富士通 y-goto 称“condolences, thankless job”易使非母语者误解，请求改为鼓励新人的正面表述。 `<!-- ROW_MINE: ksummit-discuss.messages.350152 -->`

## 66.46 【Linux社区】时区命名规范

- 【Linux社区】David Woodhouse 要求时区一律用 Olson 命名（若该节保留）。 `<!-- ROW_MINE: ksummit-discuss.messages.350153 -->`

## 66.47 【Linux社区】挂名激励效应

- 【Linux社区】NeilBrown 赞同列名或促人表态，自述被授头衔后心态由“someone should”转为“I should”，并笑称可故意插 bug 引评论。 `<!-- ROW_MINE: ksummit-discuss.messages.350154 -->`

## 66.48 【Linux社区】media样例补正

- 【Linux社区】Hans Verkuil 补充 radio/RDS/SDR、编解码器、m2m、touch、VBI 覆盖，主张 videobuf2 列为核心，新 V4L2/CEC 驱动须过 compliance 测试。 `<!-- ROW_MINE: ksummit-discuss.messages.350155 -->`
