# 97 【Linux社区】TAB纪要术语v3与选举资格

> 来源：tech-board-discuss p6（50 封全读，2006-10 至 2026-03，TAB 会议纪要 2018-2019、包容术语 v3 补丁与 IEEE 802 业界对照、缺席投票与 kernel.org web of trust 资格之辩、LLM 双克隆相似性研究、EXPORT_SYMBOL_GPL 与 LTTng、2013-2025 历届选举流程）
> 判定：41 CAND / 9 NV。主题分布：TAB 参选声明 1、包容性术语补丁讨论 1、TAB 选举提名状态 1、TAB 选举公告 1、贡献成熟度模型讨论 2、TAB 章程修改与选举资格 1、2025 TAB 选举投票启动 1、宣布不再竞选 TAB 1、CodingStyle 包容性术语补丁 v3 1、TAB 提名与社区原则 1、邮件列表地址迁移补丁 1、选举投票资格讨论 1、自我提名竞选 TAB 1、TAB 电话会议纪要（2018-12-06） 1、TAB 电话会议纪要（2019-04-04） 1、CoC 委员会报告发布 1、包容性术语与行业标准 1、TAB 选举投票提醒 1、技术作者岗位进展问询 1、TAB 连任提名自述 1、graylist 术语讨论 1、包容性术语补丁修订回应 1、选举资格与 kernel.org 账号 1、TAB 选举提名更正 1、TAB 选举征集提名人 1、竞选 TAB 自荐 1、LLM 改写与 clean room 讨论 1、竞选 TAB 自我提名 1、TAB 选举与提名流程公告 1、EXPORT_SYMBOL_GPL 与 LTTng 之争 1、CoC 报告透明度建议 1、TAB 选举投票方式讨论 1、维护者支持小组与 CoC 之别 1、包容性术语自动化跟进 1、Plumbers 2016 组办方征集 1、TAB 提名程序确认 1、USB gadget 术语由来 1、TAB 提名入列确认 1、TAB 选举资格与投票机制 1、TAB 选举投票资格澄清 1。

## 【Linux社区】零、体例说明

本文件系 tech-board-discuss p6（实锚 pk 9362842-9362891）的逐封提取（41 CAND / 9 NV），全 40 块采用**单行摘要体例**（丙型）：每块由“## 97.x 题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 97.1 TAB 参选声明

- 【Linux社区】Triplett 自述资历（Sparse 维护者、RCU、CodingStyle 撰写、Intel ChromeOS 架构师）并公开表态支持 Corbet、Sharp、Garrett、GregKH 四位候选人 `<!-- ROW_MINE: tech-board-discuss.messages.9362842 -->`

## 97.2 包容性术语补丁讨论

- 【Linux社区】指出“in denylist”不合语法，提议改用“foo is denylisted”或“not in the allowlist”等措辞 `<!-- ROW_MINE: tech-board-discuss.messages.9362844 -->`

## 97.3 TAB 选举提名状态

- 【Linux社区】指出仅三人竞争五席、投票资格之争失去意义，候选人不足使资格规则形同虚设 `<!-- ROW_MINE: tech-board-discuss.messages.9362845 -->`

## 97.4 TAB 选举公告

- 【Linux社区】公布 2018 温哥华选举时间地点、十名候选人名单（含现任标记）与候选人声明幻灯片链接 `<!-- ROW_MINE: tech-board-discuss.messages.9362846 -->`

## 97.5 贡献成熟度模型讨论

- 【Linux社区】反驳“提高维护者报酬抑制自动化”论点，自述 ktest.pl 等自动化实践，提议以补丁被忽略时长衡量维护者效能 `<!-- ROW_MINE: tech-board-discuss.messages.9362847 -->`
- 【Linux社区】纠正对“无人维护即删驱动”论的解读，说明过时设备问题的实质是无人关注导致的麻烦而非删除本身 `<!-- ROW_MINE: tech-board-discuss.messages.9362871 -->`

## 97.6 TAB 章程修改与选举资格

- 【Linux社区】以自身 2017 布拉格缺席当选为例支持缺席投票，赞成在章程中明示无需到场 `<!-- ROW_MINE: tech-board-discuss.messages.9362848 -->`

## 97.7 2025 TAB 选举投票启动

- 【Linux社区】公布九名候选人、CIVS 投票指引（垃圾邮件夹、opt-in 地址）与 12 月 20 日截止时间 `<!-- ROW_MINE: tech-board-discuss.messages.9362849 -->`

## 97.8 宣布不再竞选 TAB

- 【Linux社区】以多样性为由退出连任，主张社区职业化需要更广泛代表，呼吁选民投票时考虑此需要 `<!-- ROW_MINE: tech-board-discuss.messages.9362850 -->`

## 97.9 CodingStyle 包容性术语补丁 v3

- 【Linux社区】提交禁止新增 master/slave、blacklist/whitelist 术语的正式补丁，附替换词表、ABI/API 例外与多位维护者签名 `<!-- ROW_MINE: tech-board-discuss.messages.9362851 -->`

## 97.10 TAB 提名与社区原则

- 【Linux社区】主张除 CoC 外应强调工程原则（“说真话”“show me the code”），援引 Schulzrinne SIGCOMM 文章与 ASCE 职业伦理准则 `<!-- ROW_MINE: tech-board-discuss.messages.9362852 -->`

## 97.11 邮件列表地址迁移补丁

- 【Linux社区】因 mailman2 服务器即将关停，批量更新内核树中 lists.linuxfoundation.org 旧地址至新目的地 `<!-- ROW_MINE: tech-board-discuss.messages.9362853 -->`

## 97.12 选举投票资格讨论

- 【Linux社区】单句反驳“按 git 提交数投票”提议：git 历史仅回溯至 2.6.12 `<!-- ROW_MINE: tech-board-discuss.messages.9362854 -->`

## 97.13 自我提名竞选 TAB

- 【Linux社区】简短参选声明，提及当天 tinification 议题与跨子系统关注 `<!-- ROW_MINE: tech-board-discuss.messages.9362856 -->`

## 97.14 TAB 电话会议纪要（2018-12-06）

- 【Linux社区】公布会议公共摘要：Plumbers 2019/2020 提案、CoC 委员会人员补充、纪要发布流程重启等 `<!-- ROW_MINE: tech-board-discuss.messages.9362858 -->`

## 97.15 TAB 电话会议纪要（2019-04-04）

- 【Linux社区】记录 Community Bridge 资助计划、CoC 委员会进展、选举投票系统研究、Chris 连任主席与 Jon 任副主席 `<!-- ROW_MINE: tech-board-discuss.messages.9362859 -->`

## 97.16 CoC 委员会报告发布

- 【Linux社区】确认已将 2022-10 至 2023-03 CoC 报告更新至 kernel.org 公开页面并补充解读文档链接 `<!-- ROW_MINE: tech-board-discuss.messages.9362860 -->`

## 97.17 包容性术语与行业标准

- 【Linux社区】主张内核术语应与现行标准一致，指出 IEEE 802 已弃用相关措辞、Linux bonding 的 master/slave 用法异于业界惯例 `<!-- ROW_MINE: tech-board-discuss.messages.9362861 -->`

## 97.18 TAB 选举投票提醒

- 【Linux社区】2017 布拉格选举当日公告：时间地点、候选人文档链接、五席空缺 `<!-- ROW_MINE: tech-board-discuss.messages.9362862 -->`

## 97.19 技术作者岗位进展问询

- 【Linux社区】依据 TAB 纪要追问 OSDL 官方招聘帖发布位置，并请求将纪要或链接发布到本列表 `<!-- ROW_MINE: tech-board-discuss.messages.9362863 -->`

## 97.20 TAB 连任提名自述

- 【Linux社区】自述资历：Driver 声明、GPLv3 声明、Code of Conflict、内核执行声明、UEFI 关系协商，承诺继续弥合社区与企业鸿沟 `<!-- ROW_MINE: tech-board-discuss.messages.9362864 -->`

## 97.21 graylist 术语讨论

- 【Linux社区】梳理 greylisting 源自邮件反垃圾技术与“grey area”习语，主张其与敏感用法距离过远、不必更改 `<!-- ROW_MINE: tech-board-discuss.messages.9362865 -->`

## 97.22 包容性术语补丁修订回应

- 【Linux社区】采纳 Kees 意见：成对替换 master 与 whitelist、补 API、加入存量清理条款，并认为“Beyond just Linux”一节倡导性过强不宜进内核文档 `<!-- ROW_MINE: tech-board-discuss.messages.9362870 -->`

## 97.23 选举资格与 kernel.org 账号

- 【Linux社区】辩护以 kernel.org 账号（web of trust、团队管理九年）核验投票人身份，回应透明度与包容性质疑 `<!-- ROW_MINE: tech-board-discuss.messages.9362872 -->`

## 97.24 TAB 选举提名更正

- 【Linux社区】指出 Dave Jones 的提名被遗漏并给出列表归档链接 `<!-- ROW_MINE: tech-board-discuss.messages.9362874 -->`

## 97.25 TAB 选举征集提名人

- 【Linux社区】2021 线上选举公告：任期安排、到期名单、参选与投票资格的提交 tag 标准、提名截止硬时限 `<!-- ROW_MINE: tech-board-discuss.messages.9362875 -->`

## 97.26 竞选 TAB 自荐

- 【Linux社区】自述 Btrfs 与 Facebook 内核团队经历，寻求连任 TAB 主席 `<!-- ROW_MINE: tech-board-discuss.messages.9362876 -->`

## 97.27 LLM 改写与 clean room 讨论

- 【Linux社区】援引从 Claude 3.7 复现《哈利·波特》96% 的研究，分析双实例 LLM 规格克隆的相似性风险与增量改写规避手段 `<!-- ROW_MINE: tech-board-discuss.messages.9362877 -->`

## 97.28 竞选 TAB 自我提名

- 【Linux社区】单句自我提名，响应 Bottomley 的征集公告 `<!-- ROW_MINE: tech-board-discuss.messages.9362878 -->`

## 97.29 TAB 选举与提名流程公告

- 【Linux社区】2013 爱丁堡选举安排、十名提名人名单、截止时间与现场举手投票方式，并说明列表队列故障已清理 `<!-- ROW_MINE: tech-board-discuss.messages.9362879 -->`

## 97.30 EXPORT_SYMBOL_GPL 与 LTTng 之争

- 【Linux社区】主张不给“朋友”例外以免破坏机制目的，直言不关心 LTTng 入主、应聚焦内核真正需要的功能 `<!-- ROW_MINE: tech-board-discuss.messages.9362880 -->`

## 97.31 CoC 报告透明度建议

- 【Linux社区】答复 Shuah：在 CoC 报告中加入 CoC 页面链接即可提升透明度 `<!-- ROW_MINE: tech-board-discuss.messages.9362881 -->`

## 97.32 TAB 选举投票方式讨论

- 【Linux社区】分析 SPI 作为投票组织的条件与局限，说明上年选举以举手计票无加权，质疑“Linux”一词是否恰当 `<!-- ROW_MINE: tech-board-discuss.messages.9362883 -->`

## 97.33 维护者支持小组与 CoC 之别

- 【Linux社区】论证支持小组与 CoC 的关键差异在于无处置权限（戒毒互助类比），可降低维护者求助顾虑、回应留痕担忧 `<!-- ROW_MINE: tech-board-discuss.messages.9362884 -->`

## 97.34 包容性术语自动化跟进

- 【Linux社区】Acked-by 之外说明已提交的 checkpatch 鼓励补丁已入 linux-next，建议合并后扩充术语表 `<!-- ROW_MINE: tech-board-discuss.messages.9362885 -->`

## 97.35 Plumbers 2016 组办方征集

- 【Linux社区】代表 TAB 发布 2016 会议组办申请：Santa Fe 与 KS 同期、时间地点、团队要求与 10 月 5 日申请截止 `<!-- ROW_MINE: tech-board-discuss.messages.9362886 -->`

## 97.36 TAB 提名程序确认

- 【Linux社区】以 TAB 主席身份要求确认 Frank Rowand 是否愿意参选 `<!-- ROW_MINE: tech-board-discuss.messages.9362887 -->`

## 97.37 USB gadget 术语由来

- 【Linux社区】解释内核自创“gadget”一词的原因：USB 规范未以可用方式描述两类设备 `<!-- ROW_MINE: tech-board-discuss.messages.9362888 -->`

## 97.38 TAB 提名入列确认

- 【Linux社区】确认已将 Pavel Machek 及其自我介绍加入提名名单，属流程记录 `<!-- ROW_MINE: tech-board-discuss.messages.9362889 -->`

## 97.39 TAB 选举资格与投票机制

- 【Linux社区】批评把投票局限于封闭小圈子、警惕 SPI 的 Debian 倾向，提议以提交数阈值（如 5）一人一票 `<!-- ROW_MINE: tech-board-discuss.messages.9362890 -->`

## 97.40 TAB 选举投票资格澄清

- 【Linux社区】答复提问：选举现场任何人均可投票 `<!-- ROW_MINE: tech-board-discuss.messages.9362891 -->`
