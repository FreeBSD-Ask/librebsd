# 52 【Linux社区】治理火线EXPORT符号与拔盘复活

> 来源：ksummit-discuss p104（50 封全读，2018-09-13 ~ 2018-09-17，夹杂 KS2014 档案信 2014-05-14/15）。
> 判定：50 CAND / 0 NV。主题分布：governance 13、communication 14、EXPORT_SYMBOL_GPL 9、Banbury 8、KS2014 4、tooling 1、safety 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p104（pk 349406-349455）的逐封提取（50 CAND / 0 NV），全 7 块采用**导语＋带锚条目体例**：每块由“## 52.x 【Linux社区】题名”＋导语段＋“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——导语段承担“要点”职能、带锚条目承担“史料”与“史料锚”职能（ROW_MINE 坐标与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 52.1 【Linux社区】治理火线第二轮：指标之辩与 tglx 退出通牒

2018-09-13/17 ksummit-discuss 治理辩论第二轮收束：指标有效性、组维护制的历史与边界、tglx “out of discussion” 通牒与 Vetter 的系统化回应。

- 【Linux社区】Ripard 为单人贡献占比指标辩护：单点故障、burn-out、守门排斥三重风险，数据中心单硬盘比喻 `<!-- ROW_MINE: ksummit-discuss.messages.349406 -->`
- 【Linux社区】Belloni 反驳指标失真：RTC 收补丁多于自写、DRM 驱动贡献同样由维护者主导、对“小核心多驱动”有系统偏差 `<!-- ROW_MINE: ksummit-discuss.messages.349407 -->`
- 【Linux社区】Ripard 再驳：DRM 不完美不等于问题不存在，指标是冗余预警不是抹黑 `<!-- ROW_MINE: ksummit-discuss.messages.349408 -->`
- 【Linux社区】Jani：Daniel 已卸任、按现行 MAINTAINERS 统计画像不同；组维护制换帅平滑、给团队找共同维护者远易于给单人找继任 `<!-- ROW_MINE: ksummit-discuss.messages.349409 -->`
- 【Linux社区】tglx 反击：tip 树 2007 年三人起步、ARM-SoC 沿用、Linus 早背书；组维护制非万灵药 `<!-- ROW_MINE: ksummit-discuss.messages.349414 -->`
- 【Linux社区】Vivi 澄清：没人自称发明组维护制，Daniel 原话是“分享经验” `<!-- ROW_MINE: ksummit-discuss.messages.349417 -->`
- 【Linux社区】Airlie：DRM 组维护制更成熟（有人进有人出）、drm-next/fixes 迁至同权工具链、十年来首次可交出访问 `<!-- ROW_MINE: ksummit-discuss.messages.349419 -->`
- 【Linux社区】Rafael 批评“对我有效所以对你也必须有效”姿态令人自卫、反生产 `<!-- ROW_MINE: ksummit-discuss.messages.349420 -->`
- 【Linux社区】tglx 长篇反驳：DRM 贡献者是企业团队、tip 侧是 drive-by 与甩栅栏；工具标准化不会变出关爱者；除非系统性分析否则退出讨论 `<!-- ROW_MINE: ksummit-discuss.messages.349426 -->`
- 【Linux社区】Vetter 压稿两日的总结陈词：drm-misc 强制交叉评审提升 bus factor、漏斗损耗、commit 权利留人、CoC 严格执行+维护者无特权 `<!-- ROW_MINE: ksummit-discuss.messages.349439 -->`

## 52.2 【Linux社区】单任维护者之殇：Brownell 案例与 GPIO sysfs 遗产

单任维护者消失的真实代价：Brownell 2011 年去世对 GPIO/SPI/MMC 子系统的长期影响与 sysfs ABI 遗产之辩。

- 【Linux社区】Walleij：Brownell 去世后 GPIO 无主、akpm 代收、湍流期合入 GPIO sysfs ABI 暴露全局 numberspace 成半 ABI `<!-- ROW_MINE: ksummit-discuss.messages.349421 -->`
- 【Linux社区】Geert 纠正时间线：GPIO sysfs 接口 commit d8f388d8dc8d4f36 作者正是 Brownell 本人 `<!-- ROW_MINE: ksummit-discuss.messages.349424 -->`
- 【Linux社区】Walleij 认错（git history never lies）；其他作者只记得“当时只是需要从用户态控制 GPIO” `<!-- ROW_MINE: ksummit-discuss.messages.349425 -->`

## 52.3 【Linux社区】EXPORT_SYMBOL_GPL 语义之辩：从 Rusty 2005 到 ABI 稳定性分界线

EXPORT_SYMBOL_GPL 议题全景：2005 年 Rusty Russell commit b6c17ea4 与 LWN 154602 的源头、政治/法律/技术三重解读、Greg 与 Ted 两种成文路线。

- 【Linux社区】Dan Williams 提出新议题：文档仅一句模糊表述；两问——客观判据与符号改判考量清单 `<!-- ROW_MINE: ksummit-discuss.messages.349411 -->`
- 【Linux社区】Roeck：希望有手段声明“本代码只许 GPL 代码使用”，自认完全非技术 `<!-- ROW_MINE: ksummit-discuss.messages.349413 -->`
- 【Linux社区】Greg KH 自称第一个使用 _GPL 的人、愿牵头正式成文；“文档化以免维护者夹在中间” `<!-- ROW_MINE: ksummit-discuss.messages.349415 -->`
- 【Linux社区】Pinchart：_GPL 是政治手段多于技术、法律灰色；“internal implementation”句出自 Rusty Russell 2005-09-09 commit b6c17ea4 且无解释 `<!-- ROW_MINE: ksummit-discuss.messages.349416 -->`
- 【Linux社区】Airlie 引 LWN 154602 原始法律建议；认为已被滥用稀释、refcounts 案例纯属政治 `<!-- ROW_MINE: ksummit-discuss.messages.349418 -->`
- 【Linux社区】Pinchart：派生作品论未证伪、政治论点也可以是法律论点；_GPL 表明意图但非内部性判据 `<!-- ROW_MINE: ksummit-discuss.messages.349422 -->`
- 【Linux社区】Wolfram Sang 全盘认同 Pinchart `<!-- ROW_MINE: ksummit-discuss.messages.349431 -->`
- 【Linux社区】Ted：程序员辩论法律解释无价值且有害；2005 建议只要求“存在差异并显式表达”；个人分界线是 ABI 稳定性——_GPL 更不稳定 `<!-- ROW_MINE: ksummit-discuss.messages.349437 -->`
- 【Linux社区】Mauro：media 强烈偏好 kAPI 用 _GPL；现存 EXPORT_SYMBOL 是历史遗留；重写顺手改 _GPL、小改不动 `<!-- ROW_MINE: ksummit-discuss.messages.349440 -->`

## 52.4 【Linux社区】Project Banbury：拔盘复活之辩

Project Banbury 热插拔回写复活议题：Wilcox 提案、Linus 可行性质疑（NFS intr 先例）、Bottomley 缓存谎言论与 Ted 的 device-mapper 重传缓冲设计。

- 【Linux社区】Wilcox 提出新议题：拔错盘/过早拔 USB 致回写丢失，能否“插回去就能用”；**banbury.html** 架构草图、未写一行代码 `<!-- ROW_MINE: ksummit-discuss.messages.349427 -->`
- 【Linux社区】Reinecke 支持、建议爱丁堡当面深聊 `<!-- ROW_MINE: ksummit-discuss.messages.349428 -->`
- 【Linux社区】Wilcox：不去爱丁堡，tech topics 归 Plumbers、用户态组件更合适 `<!-- ROW_MINE: ksummit-discuss.messages.349430 -->`
- 【Linux社区】Pinchart：因 DDoS 致 CPU-存储链路断而丢过服务器，认为是了不起的改进 `<!-- ROW_MINE: ksummit-discuss.messages.349432 -->`
- 【Linux社区】Linus：“amazing”是字面惊叹但不现实：暂停 IO 等于挂机、内存耗尽；NFS intr 三前提与 USB 串号不可靠 `<!-- ROW_MINE: ksummit-discuss.messages.349433 -->`
- 【Linux社区】Bottomley：外置存储内部回写缓存、SATA 可能说谎 USB 必说谎；barrier 型缓存需从最后 barrier 起按序重放 IO `<!-- ROW_MINE: ksummit-discuss.messages.349435 -->`
- 【Linux社区】Ted 方案：device-mapper 设备 + TCP 式重传缓冲保留已写块副本、可配上限、CACHE FLUSH 释放、用户态重连重放 `<!-- ROW_MINE: ksummit-discuss.messages.349436 -->`
- 【Linux社区】Howells 问 fscache 能否帮忙 `<!-- ROW_MINE: ksummit-discuss.messages.349438 -->`

## 52.5 【Linux社区】通信系统之辩：邮件强制性与 GitHub 账户墙

通信系统之辩全景：Mauro 的“为何强制邮件”挑战、hch 的账户墙底线与 Pinchart 的推送式/可脚本化/离线三需求，221 条 moderated 列表等价论之驳。

- 【Linux社区】Mauro 回“Live without email”：github 小项目使用经验、web 界面对小项目增值、内核规模会乱、Gen-Y/Z 熟悉度与引新血 `<!-- ROW_MINE: ksummit-discuss.messages.349441 -->`
- 【Linux社区】Mauro“再下一层”：为何对所有开发强制邮件？单一驱动/低流量子系统可用 github、公开讨论比企业闭门好 `<!-- ROW_MINE: ksummit-discuss.messages.349442 -->`
- 【Linux社区】Geert 驳：驱动合入后开发并未停止、bug 修复应 CC lkml、合入后维护规模更大 `<!-- ROW_MINE: ksummit-discuss.messages.349443 -->`
- 【Linux社区】Mauro 再驳：CC lkml 不总发生、bugzilla 实践本来就 web 交互“次优但能用”、github 有邮件接口 `<!-- ROW_MINE: ksummit-discuss.messages.349444 -->`
- 【Linux社区】Julia Lawall：只用邮件交互 github issues；发帖者省略上下文 `<!-- ROW_MINE: ksummit-discuss.messages.349446 -->`
- 【Linux社区】hch：ACPI 维护者拒绝收补丁重定向 github 版；底线是必须接受邮件格式补丁 `<!-- ROW_MINE: ksummit-discuss.messages.349447 -->`
- 【Linux社区】hch：github 最大问题是无法不注册账户而交互 `<!-- ROW_MINE: ksummit-discuss.messages.349448 -->`
- 【Linux社区】Pinchart：不反对 git-push 替代但邮件网关必须到位；拒绝强制注册与认证、伤害 drive-by 贡献 `<!-- ROW_MINE: ksummit-discuss.messages.349449 -->`
- 【Linux社区】Mauro：moderated ML 221 条等价论；web 界面一次订阅全站通用 `<!-- ROW_MINE: ksummit-discuss.messages.349450 -->`
- 【Linux社区】Pinchart 长文驳：需求清单未强制邮件、历史必须公开可搜索可镜像不能单点存放、bug 报告成二等公民、建议看 gitlab `<!-- ROW_MINE: ksummit-discuss.messages.349451 -->`
- 【Linux社区】Mauro 升华为规则提案：拒绝非订阅者邮件补丁的开发模式必须保证妥善处理、应写进流程文档 `<!-- ROW_MINE: ksummit-discuss.messages.349452 -->`
- 【Linux社区】hch：moderated 不等于总拒非订阅者、linux-arm-kernel 延时放行 `<!-- ROW_MINE: ksummit-discuss.messages.349453 -->`
- 【Linux社区】Pinchart 驳 221 条等价论：ML 订阅一次后无需认证、web UI 每次都要认证；各起 gitlab 实例后情形就变了 `<!-- ROW_MINE: ksummit-discuss.messages.349454 -->`
- 【Linux社区】Geert：linux-arm-kernel 是通往众多维护者的网关；核心 ARM 仍须走 ARM patch system `<!-- ROW_MINE: ksummit-discuss.messages.349455 -->`

## 52.6 【Linux社区】KS2014 档案：能耗偏置与 ACPI-DT 资源查找

页内夹杂的 KS2014 档案信（2014-05-14/15）：能耗偏置接口三档旋钮、EAS workshop 筹备与 ACPI-DT 资源查找统一接口之辩。

- 【Linux社区】Lezcano：能耗 profile 收敛回三档中央旋钮；建议细粒度旋钮放 debugfs（2014-05-14） `<!-- ROW_MINE: ksummit-discuss.messages.349412 -->`
- 【Linux社区】Preeti 响应 EAS workshop：target_residency 定优、Lorenzo 解释能量盈亏平衡点（2014-05-15） `<!-- ROW_MINE: ksummit-discuss.messages.349423 -->`
- 【Linux社区】Preeti 回 Rafael：governor 不知是否节能、任务级 latency 站不住、手机/手表场景内核自行决策（2014-05-15） `<!-- ROW_MINE: ksummit-discuss.messages.349434 -->`
- 【Linux社区】Rafael 论 ACPI-DT 资源查找：acpi_find_gpio() 只用 index、主动 vs 被动固件模型、PCI host bridge 好例子（2014-05-15） `<!-- ROW_MINE: ksummit-discuss.messages.349445 -->`

## 52.7 【Linux社区】工具链与议题归位

零散两封：维护者 merge-config 工具链经验与安全关键议题的轨道归位（Maintainer Summit → Plumbers）。

- 【Linux社区】Hart 演示 pdx86-tools merge-config 工具链；olddefconfig 对被依赖隐藏 CONFIG 静默忽略的坑 `<!-- ROW_MINE: ksummit-discuss.messages.349410 -->`
- 【Linux社区】Chen 接受 Greg 建议：安全关键 Linux 议题改投 Plumbers 技术报告轨道 `<!-- ROW_MINE: ksummit-discuss.messages.349429 -->`
