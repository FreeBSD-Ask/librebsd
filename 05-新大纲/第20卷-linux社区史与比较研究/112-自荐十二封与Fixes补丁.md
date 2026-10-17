# 112 【Linux社区】自荐十二封与Fixes补丁

> 来源：tech-board-discuss p12（50 封全读，2007-08 至 2026-03，Williams/Greg/Shuah/Colomar/Wilk/Olof/Lutomirski/Sang/Abbott 等十二封自荐、Colomar Fixes 加日期完整补丁、xz CFLAGS 注入与 Make 插值投毒路径详列、TAB 扩容 at-large 提案、红黑树 left/right 主张、2009 银座选举流程）
> 体例说明：本页 38 块采用**速览体例**——块下仅存单行摘记（主题陈述＋史料锚），要点、史观、辨析、文献四字段另立详表承载；五字段完整体例见 00-总览 §一.2。本页卷头未登记 claim 编号区间，文献著录与史观映射待详表单独立卷时补录。
> 判定：43 CAND / 7 NV。主题分布：unwind 符号导出与树外 ABI 1、2009 TAB 选举通知 1、2022 TAB 自荐（Dan Williams） 1、TAB 自荐（Greg KH） 1、TAB 章程修改与远程投票 1、TAB 自荐（Shuah） 1、SPI 会员作投票基础之辩 1、2018 TAB 自荐（Pavel Machek） 1、CodingStyle 包容性术语 6、TAB 自荐（Alejandro Colomar） 1、2010 TAB 自荐（Konrad Rzeszutek Wilk） 1、2016 TAB 自荐（Olof Johansson） 1、2016 TAB 选举流程（草案 v2） 1、CoC 半年报反馈征集 1、2009 选举嵌入式代表动员 1、2008 选举流程补充 1、xz 事件与构建供应链 1、2015 TAB 自荐（Olof Johansson） 1、CIVS 投票 opt-in 通知 1、2020 提名截止提醒 1、2017 TAB 自荐（Greg KH） 1、Fixes 标签加日期之辩 1、2018 TAB 自荐（Andy Lutomirski） 1、unwind 符号导出之争 1、2007 选举程序批评 1、Fixes 标签加作者日期补丁 1、2016 候选人声明汇总 1、LLM 重写与 clean-room 1、2021 提名截止最后提醒 1、2018 TAB 自荐声明草稿 1、2014 TAB 自荐（hpa） 1、TAB 扩容提案 1、2020 TAB 自荐（Laura Abbott） 1、2019 提名流程状态说明 1、2017 TAB 自荐（Wolfram Sang） 1、SPI 会员作投票基础提案 1、TAB 扩容提案讨论 1、提名滥用与程序裁量 1。

## 112.1 unwind 符号导出与树外 ABI

- 【Linux社区】反驳 Rostedt“树外是优势”论：ABI 契约的上游维护本是各子系统核心难题，“让内核让路、自管 ABI”的诉求历来因回归与安全顾虑被婉拒 `<!-- ROW_MINE: tech-board-discuss.messages.9363142 -->`

## 112.2 2009 TAB 选举通知

- 【Linux社区】TAB 主席发布选举流程：银座 Gonpachi 现场投票、开放 KS/JLS 与会者参加、十名候选人名单与提名截止安排 `<!-- ROW_MINE: tech-board-discuss.messages.9363143 -->`

## 112.3 2022 TAB 自荐（Dan Williams）

- 【Linux社区】自荐声明：NVDIMM 与 CXL 维护者、上游 17 年，主张 TAB 影响力仅源于成员个人声望，愿投入开源最佳实践与维护者贡献者关系议题 `<!-- ROW_MINE: tech-board-discuss.messages.9363144 -->`

## 112.4 TAB 自荐（Greg KH）

- 【Linux社区】参选声明：列举驱动声明、GPLv3 声明、Code of Conflict、与 cve.org 谈成 CVE 编号机构及欧盟 CRA 专家组代表等 TAB 履历 `<!-- ROW_MINE: tech-board-discuss.messages.9363145 -->`

## 112.5 TAB 章程修改与远程投票

- 【Linux社区】为以 kernel.org 账号为投票资格的方案辩护：相比过去十年无远程投票已是改进，属“婴儿步”而非终极方案 `<!-- ROW_MINE: tech-board-discuss.messages.9363146 -->`

## 112.6 TAB 自荐（Shuah）

- 【Linux社区】参选声明：kselftest/usbip/cpupower 等维护与 nolibc/kunit 共同维护，CoC 委员会与 LPC 程序委员会经历，聚焦社区健康与新开发者桥梁 `<!-- ROW_MINE: tech-board-discuss.messages.9363147 -->`

## 112.7 SPI 会员作投票基础之辩

- 【Linux社区】撤回此前对 SPI 会员制的反对（私下沟通证实顾虑无据），仅担忧成员构成偏单一发行版会造成投票偏见 `<!-- ROW_MINE: tech-board-discuss.messages.9363148 -->`

## 112.8 2018 TAB 自荐（Pavel Machek）

- 【Linux社区】确认自荐并给出正式声明：NBD/x86-64/休眠维护经历，主张重要决策公开、诚实沟通，批评维护者沉默比不礼貌回复更糟 `<!-- ROW_MINE: tech-board-discuss.messages.9363149 -->`

## 112.9 CodingStyle 包容性术语

- 【Linux社区】认同 Bottomley：编码风格修改才是实际关键，使已部署相关政策的贡献组织知道如何与 Linux 协调互动 `<!-- ROW_MINE: tech-board-discuss.messages.9363150 -->`
- 【Linux社区】为该文档辩护三点作用（促成改动、集中答疑、第五段预防反复争论）并反驳 Linus“全删”主张，提出并入 patch 描述的折中思路 `<!-- ROW_MINE: tech-board-discuss.messages.9363154 -->`
- 【Linux社区】主张 red/black 树命名即便与种族无关也是糟糕间接层（赌场文化梗），left/right 命名更直观更易翻译，支持去色名化 `<!-- ROW_MINE: tech-board-discuss.messages.9363159 -->`
- 【Linux社区】借 Airlie 交流为例主张该文档会成为争议磁石，开发者可诚实分歧而仍支持包容语言，故此文件不应入内核树 `<!-- ROW_MINE: tech-board-discuss.messages.9363165 -->`
- 【Linux社区】主张倾听受影响社群作为术语专家，以 Black Hat 辞职事件说明代社群发言的风险，反驳滑坡式扩大化并强调社区建设即内核开发 `<!-- ROW_MINE: tech-board-discuss.messages.9363166 -->`
- 【Linux社区】以“SPI controller controller”等实例论证 controller/device 命名过于泛化将造成歧义，附荷兰语直接吸收英语术语的旁证 `<!-- ROW_MINE: tech-board-discuss.messages.9363167 -->`

## 112.10 TAB 自荐（Alejandro Colomar）

- 【Linux社区】自荐主张确保文档受重视并推动 ISO C 标准安全化，列出三枚 commit 作参选资格证明 `<!-- ROW_MINE: tech-board-discuss.messages.9363151 -->`

## 112.11 2010 TAB 自荐（Konrad Rzeszutek Wilk）

- 【Linux社区】自荐陈述 8 年经历：系统管理工具、RHEL on IBM、iSCSI/Xen、共同维护 Xen 树，强调跨大小公司协作经验与谈判辅导等软技能 `<!-- ROW_MINE: tech-board-discuss.messages.9363152 -->`

## 112.12 2016 TAB 自荐（Olof Johansson）

- 【Linux社区】参选声明：arm-soc 联合维护者与 Chrome OS 内核技术负责人，推动 Nvidia/Rockchip/MediaTek 加大上游参与，愿带入嵌入式视角 `<!-- ROW_MINE: tech-board-discuss.messages.9363153 -->`

## 112.13 2016 TAB 选举流程（草案 v2）

- 【Linux社区】TAB 主席发布选举程序：KS/Plumbers 与会者皆可投票、提名可至选举现场、声明须 10 月 28 日前提交并汇编成在线文档 `<!-- ROW_MINE: tech-board-discuss.messages.9363155 -->`

## 112.14 CoC 半年报反馈征集

- 【Linux社区】转载 2022-10 至 2023-03 CoC 报告数据（6 起邮件不当行为、1 起辅导澄清与 5 起维护者拒码权澄清）并请 TAB 在公开前反馈 `<!-- ROW_MINE: tech-board-discuss.messages.9363156 -->`

## 112.15 2009 选举嵌入式代表动员

- 【Linux社区】表达治理立场：期望 TAB 有嵌入式背景委员，点名动员 Thomas Gleixner 与 David Woodhouse 参选 `<!-- ROW_MINE: tech-board-discuss.messages.9363157 -->`

## 112.16 2008 选举流程补充

- 【Linux社区】补充选举规则：缺席 KS/Plumbers 者可提交声明由他人会前代读、只接受自荐提名 `<!-- ROW_MINE: tech-board-discuss.messages.9363158 -->`

## 112.17 xz 事件与构建供应链

- 【Linux社区】详列内核构建被投毒的路径：CFLAGS 注入 prctl 后门实例、Make 环境变量插值执行、恶意包经 pkg-config 注入及 Shellshock 复发 `<!-- ROW_MINE: tech-board-discuss.messages.9363160 -->`

## 112.18 2015 TAB 自荐（Olof Johansson）

- 【Linux社区】简短正式自荐并声明将亲临首尔选举现场 `<!-- ROW_MINE: tech-board-discuss.messages.9363161 -->`

## 112.19 CIVS 投票 opt-in 通知

- 【Linux社区】选举操作记录：CIVS 新增私人投票须显式 opt-in 的变更，给出 opt-in 入口与咨询邮箱 `<!-- ROW_MINE: tech-board-discuss.messages.9363162 -->`

## 112.20 2020 提名截止提醒

- 【Linux社区】选举程序性提醒：提名截止 8 月 24 日 9:00 美东，因电子投票属硬性截止 `<!-- ROW_MINE: tech-board-discuss.messages.9363164 -->`

## 112.21 2017 TAB 自荐（Greg KH）

- 【Linux社区】参选声明：Linux Foundation 5 年企业协调经历、驱动声明/GPLv3/Code of Conflict/执法声明及 UEFI 与 ACPI 规格参与谈判 `<!-- ROW_MINE: tech-board-discuss.messages.9363169 -->`

## 112.22 Fixes 标签加日期之辩

- 【Linux社区】反驳加日期提案：哈希与主题同时碰撞的概率天文级低，并举 Linus 连 12 位缩写增至 13 位都否决的先例 `<!-- ROW_MINE: tech-board-discuss.messages.9363170 -->`

## 112.23 2018 TAB 自荐（Andy Lutomirski）

- 【Linux社区】参选声明：security@ 经历与 Meltdown 协调经验，主张 LF 改善跨厂商安全协调流程，并批评 CoC 重规则轻欢迎氛围 `<!-- ROW_MINE: tech-board-discuss.messages.9363171 -->`

## 112.24 unwind 符号导出之争

- 【Linux社区】重申核心政策：无树内用户即不导出符号，LTTng 未合并不应推翻该规则，驳斥“逼走 Mathieu”的说法 `<!-- ROW_MINE: tech-board-discuss.messages.9363172 -->`

## 112.25 2007 选举程序批评

- 【Linux社区】批评仅现场读提名、无候选人声明的流程近乎人气比拼，要求说明候选人职责与投票依据，建议会前公布意向声明 `<!-- ROW_MINE: tech-board-discuss.messages.9363173 -->`

## 112.26 Fixes 标签加作者日期补丁

- 【Linux社区】完整补丁提案：陈述旧式 Fixes 缺日期易致误判的动机，附五处文档与 checkpatch.pl 的具体修改 `<!-- ROW_MINE: tech-board-discuss.messages.9363175 -->`

## 112.27 2016 候选人声明汇总

- 【Linux社区】选举操作记录：声明文档完成、八名已交声明候选人名单，迟报名者须投票前作一分钟现场陈述 `<!-- ROW_MINE: tech-board-discuss.messages.9363178 -->`

## 112.28 LLM 重写与 clean-room

- 【Linux社区】转述并明确非支持的辩方论点：clean-room 仅是手段，机器人只拿到 API 与测试，chardet 必在训练数据则被视为无关 `<!-- ROW_MINE: tech-board-discuss.messages.9363180 -->`

## 112.29 2021 提名截止最后提醒

- 【Linux社区】选举程序性提醒：提名截止 9 月 20 日 9:00 美东，随引完整选举公告、资格标准与候选声明要求 `<!-- ROW_MINE: tech-board-discuss.messages.9363181 -->`

## 112.30 2018 TAB 自荐声明草稿

- 【Linux社区】按主席要求的格式提交声明草稿：Linux 1.3 时代起步、NBD/x86-64/休眠维护，主张公共决策与诚实沟通、反对维护者沉默 `<!-- ROW_MINE: tech-board-discuss.messages.9363182 -->`

## 112.31 2014 TAB 自荐（hpa）

- 【Linux社区】单句正式自荐参选记录 `<!-- ROW_MINE: tech-board-discuss.messages.9363183 -->`

## 112.32 TAB 扩容提案

- 【Linux社区】提案允许 TAB 任命欠代表社群或特定技术需要的 at-large 成员任一年任期，限两届后须参选，并讨论落选者即时任命的防裙带规则 `<!-- ROW_MINE: tech-board-discuss.messages.9363184 -->`

## 112.33 2020 TAB 自荐（Laura Abbott）

- 【Linux社区】参选声明：两年 TAB 选举工作与 TAB 历史学习、Android 与 KSPP 经历、Plumbers 2020 线上版主席 `<!-- ROW_MINE: tech-board-discuss.messages.9363185 -->`

## 112.34 2019 提名流程状态说明

- 【Linux社区】澄清提名征集已发 ksummit/LKML 而漏发本列表，说明新投票程序与专用邮件列表创建进度并顺带提醒提名 `<!-- ROW_MINE: tech-board-discuss.messages.9363186 -->`

## 112.35 2017 TAB 自荐（Wolfram Sang）

- 【Linux社区】参选声明：I2C 维护者、个人顾问视角，源于执法声明后想推动社区参与，主张增进 TAB 信息回馈并关注评审人力不足 `<!-- ROW_MINE: tech-board-discuss.messages.9363187 -->`

## 112.36 SPI 会员作投票基础提案

- 【Linux社区】提出以 SPI 会员作为 TAB 投票人基础的替代方案：内核黑客取得会员资格不难且官僚事务由 SPI 承担 `<!-- ROW_MINE: tech-board-discuss.messages.9363189 -->`

## 112.37 TAB 扩容提案讨论

- 【Linux社区】要求举出专家任命适用的具体议题先例，并建议紧急议题改设三个月短期任命、于下次选举时归位常态 `<!-- ROW_MINE: tech-board-discuss.messages.9363190 -->`

## 112.38 提名滥用与程序裁量

- 【Linux社区】说明超大团体提名将由程序委员会裁量处理而不构成拒绝服务，历届五至十人提名与相互建议重叠即流程正常运作 `<!-- ROW_MINE: tech-board-discuss.messages.9363191 -->`
