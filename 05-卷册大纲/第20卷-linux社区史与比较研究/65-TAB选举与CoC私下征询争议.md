# 65 【Linux社区】TAB选举与CoC私下征询争议

> 来源：ksummit-discuss p117（50 封全读，2018-11-10/15 TAB 选举全流程+XArray 议题，夹杂 2014-05 档案信）
> 判定：42 CAND / 8 NV。主题分布：CoC流程交锋 1、提速与维护者瓶颈 1、TAB竞选声明 5、CoC咨询名单争议 1、CoC私下讨论 1、贡献度度量争议 2、CoC补丁流转 2、CoC社区界定 1、CoC流程之争 1、CoC效果归因 1、ARM旧平台清理 3、CoC冻结之争 1、TAB不参选声明 1、TAB选举流程 4、TAB选举公告 1、非技术列表提案 2、XArray议题 1、KS2018议程 2、TAB选举结果 1、TAB选举门槛争议 3、CoC咨询机制 1、DAX面谈安排 1、ZUFS议程安排 2、ACPI/DT议题 1、XArray多阶缓存 1、维护者手册提案 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p117（pk 350056-350105）的逐封提取（42 CAND / 8 NV），全 26 块采用**单行摘要体例**（丙型）：每块由“## 65.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 65.1 【Linux社区】CoC流程交锋

- 【Linux社区】Mason 反驳 Cooper“受邀讨论内容皆可公开”的假设，回以“you lost me right here”，坚持私密征询路线 `<!-- ROW_MINE: ksummit-discuss.messages.350056 -->`

## 65.2 【Linux社区】提速与维护者瓶颈

- 【Linux社区】转 Mason 对 Facebook 模式定性：集中评审工具、无维护者层级、维护者是最大瓶颈，fb.com 每日发布两次；Dunlap 认同评审者不该查编码风格 `<!-- ROW_MINE: ksummit-discuss.messages.350057 -->`

## 65.3 【Linux社区】TAB竞选声明

- 【Linux社区】Williams 自荐：2015 落选、2016 当选，签署 CoC，称 TAB 的 TA 更近“Trusted Adviser” `<!-- ROW_MINE: ksummit-discuss.messages.350058 -->`
- 【Linux社区】Pinchart 自荐：治理与维护层级有缺陷、社区弥漫无力感，主张给开发者更多权力 `<!-- ROW_MINE: ksummit-discuss.messages.350071 -->`
- 【Linux社区】Mauro 自荐：media 子系统由每版约 30 补丁增至每窗口 400-500，从未缺席合并窗口，强调南美代表意义 `<!-- ROW_MINE: ksummit-discuss.messages.350074 -->`
- 【Linux社区】Mason 自荐连任 TAB 主席：2000 年起全职内核、主攻 Btrfs、Facebook 内核团队五年 `<!-- ROW_MINE: ksummit-discuss.messages.350078 -->`
- 【Linux社区】Lutomirski 自荐：security@ 适合小议题，Meltdown 级跨厂商协调需 LF 改进；CoC 重规则轻文化 `<!-- ROW_MINE: ksummit-discuss.messages.350081 -->`

## 65.4 【Linux社区】CoC咨询名单争议

- 【Linux社区】Tso 以 Signed-off/Ack/Reviewed 计数复核 Perches 约#240 不在前 200，承认 git 统计客观但可被钻营（game） `<!-- ROW_MINE: ksummit-discuss.messages.350059 -->`

## 65.5 【Linux社区】CoC私下讨论

- 【Linux社区】Cooper 转而认同 Mason“给反对者自由发言场所”的理由，称此前不知此为私密讨论主因 `<!-- ROW_MINE: ksummit-discuss.messages.350060 -->`

## 65.6 【Linux社区】贡献度度量争议

- 【Linux社区】Perches：Ack 几乎无用、非主 Sign-off 次之，按作者的“git shortlog -n -s”更有用 `<!-- ROW_MINE: ksummit-discuss.messages.350062 -->`
- 【Linux社区】Morris 提醒：子树合并维护者常不加 Signed-off-by，git 统计会漏计 `<!-- ROW_MINE: ksummit-discuss.messages.350070 -->`

## 65.7 【Linux社区】CoC补丁流转

- 【Linux社区】Rowand 追问：更新系“不透明封闭”完成；周六发补丁周一合并“并非正常评审” `<!-- ROW_MINE: ksummit-discuss.messages.350063 -->`
- 【Linux社区】Uytterhoeven：入库补丁与其 ack 版本全同；私下渠道下 ack/nak/求改三途皆受限；此后“别再改 CoC”再无补丁重发 `<!-- ROW_MINE: ksummit-discuss.messages.350098 -->`

## 65.8 【Linux社区】CoC社区界定

- 【Linux社区】Tso 称公开讨论样本偏激（多人近年零提交、一人 5 年仅 3-4 个提交），私下征询获未发声者反馈，Linus 愿暂不再改 CoC `<!-- ROW_MINE: ksummit-discuss.messages.350064 -->`

## 65.9 【Linux社区】CoC流程之争

- 【Linux社区】NeilBrown 反问：完美的 CoC 与开放流程何者更利社区 `<!-- ROW_MINE: ksummit-discuss.messages.350065 -->`

## 65.10 【Linux社区】CoC效果归因

- 【Linux社区】NeilBrown 斥 Linus 在其“已证无能为力之处”耍威风，且行为改变与 CoC 两变量同动、效果永无法归因 `<!-- ROW_MINE: ksummit-discuss.messages.350066 -->`

## 65.11 【Linux社区】ARM旧平台清理

- 【Linux社区】Hutchings：ixp4xx 因镜像超 NSLU2 分区被移出 Debian、iop32x 早先移除，遗留 pre-v7 仅 kirkwood/mv78xx0/orion5x/versatile `<!-- ROW_MINE: ksummit-discuss.messages.350068 -->`
- 【Linux社区】Cooper 拟以两台 NSLU2 作 tinification/IoT 平台，问 Debian mv78xx0 用户情况 `<!-- ROW_MINE: ksummit-discuss.messages.350079 -->`
- 【Linux社区】Hutchings：versatile 为 ARM 自有板且 QEMU 可模拟；mv78xx0 仅剩一台 Debian 构建机 ancina `<!-- ROW_MINE: ksummit-discuss.messages.350090 -->`

## 65.12 【Linux社区】CoC冻结之争

- 【Linux社区】Rostedt 以“代码入内核后有真 bug 再修”类比 CoC 冻结，自承不同意但愿一试 `<!-- ROW_MINE: ksummit-discuss.messages.350069 -->`

## 65.13 【Linux社区】TAB不参选声明

- 【Linux社区】hpa 宣布不再连任：TAB 不需“又一位白人男性早期爱好者”，专业化需更广代表性 `<!-- ROW_MINE: ksummit-discuss.messages.350073 -->`

## 65.14 【Linux社区】TAB选举流程

- 【Linux社区】Rostedt 已将 Mauro 加入 Google Doc，但或赶不上选举幻灯片 `<!-- ROW_MINE: ksummit-discuss.messages.350075 -->`
- 【Linux社区】Mason 确认 Mauro 已入幻灯片，若 Peter 选票未定稿尚有写票空位 `<!-- ROW_MINE: ksummit-discuss.messages.350077 -->`
- 【Linux社区】Rostedt 将 Lutomirski 加入 Google Doc，称赶不上幻灯与选票可写票补入，疑列表地址大小写致丢信 `<!-- ROW_MINE: ksummit-discuss.messages.350082 -->`
- 【Linux社区】Mason 确认 Peter 已将 Lutomirski 列入选票，正补入幻灯片 `<!-- ROW_MINE: ksummit-discuss.messages.350086 -->`

## 65.15 【Linux社区】TAB选举公告

- 【Linux社区】温哥华 11 月 13 日 17:30 投票，五席改选、候选人十名（现任四人，hpa 弃选），非改选成员 Corbet/gregkh/Rostedt/Tso/Bird `<!-- ROW_MINE: ksummit-discuss.messages.350080 -->`

## 65.16 【Linux社区】非技术列表提案

- 【Linux社区】Nikula 提议 LKML 旁设常设非技术列表：仅订阅者可发、限 MAINTAINERS 或近年若干提交者 `<!-- ROW_MINE: ksummit-discuss.messages.350084 -->`
- 【Linux社区】Pinchart：限 MAINTAINERS 会挡掉有效反馈，核心问题是“内核社区是谁” `<!-- ROW_MINE: ksummit-discuss.messages.350087 -->`

## 65.17 【Linux社区】XArray议题

- 【Linux社区】Wilcox 议题：已有树将全部 radix tree 用户转 XArray，并可替代 list_head `<!-- ROW_MINE: ksummit-discuss.messages.350085 -->`

## 65.18 【Linux社区】KS2018议程

- 【Linux社区】Tso 确认 XArray 议题排期周三 16:00 `<!-- ROW_MINE: ksummit-discuss.messages.350088 -->`
- 【Linux社区】Tso 承诺 XArray 演讲录像约次周上线 LPC YouTube 频道 `<!-- ROW_MINE: ksummit-discuss.messages.350094 -->`

## 65.19 【Linux社区】TAB选举结果

- 【Linux社区】95 张选票：Mason 67、Abbott 62、Olof 53、Dan Williams 47、Cook 45，次高 41 票 `<!-- ROW_MINE: ksummit-discuss.messages.350089 -->`

## 65.20 【Linux社区】TAB选举门槛争议

- 【Linux社区】Nikula 唱反调：投票需到场并“交给 LF 数百美元”，仅是近似的民主开放 `<!-- ROW_MINE: ksummit-discuss.messages.350093 -->`
- 【Linux社区】Mason 回应：LF 设有差旅基金助社区成员与会 `<!-- ROW_MINE: ksummit-discuss.messages.350095 -->`
- 【Linux社区】Dreier：到场投票是财务外的实质门槛，旅程负担不均，爱丁堡对苏格兰人易、对新西兰人难 `<!-- ROW_MINE: ksummit-discuss.messages.350097 -->`

## 65.21 【Linux社区】CoC咨询机制

- 【Linux社区】Brown 指出同类咨询通常公开宣布正在进行并留意见入口，此次未做 `<!-- ROW_MINE: ksummit-discuss.messages.350096 -->`

## 65.22 【Linux社区】DAX面谈安排

- 【Linux社区】Wilcox 与 Dan Williams 当日 14:00 面谈 DAX 与 XArray，自承“邮件列表上一直各说各话” `<!-- ROW_MINE: ksummit-discuss.messages.350099 -->`

## 65.23 【Linux社区】ZUFS议程安排

- 【Linux社区】Tso 因 Boaz 病缺将 ZUFS 改排周四 9 点 KS track（首句误写周五），并请 Phillips 制作标题页 `<!-- ROW_MINE: ksummit-discuss.messages.350100 -->`
- 【Linux社区】Tso 更正 ZUFS 排期为周四 9 点（前信误写周五） `<!-- ROW_MINE: ksummit-discuss.messages.350102 -->`

## 65.24 【Linux社区】ACPI/DT议题

- 【Linux社区】Hart：与 Wysocki 紧密协作，方向为 ACPI/DT 双后端统一资源 API 与三路探测；pdata 转换应留在驱动内 `<!-- ROW_MINE: ksummit-discuss.messages.350101 -->`

## 65.25 【Linux社区】XArray多阶缓存

- 【Linux社区】Wilcox：多阶补丁将出，瓶颈在页缓存侧而非 XArray，DAX 是“矿井金丝雀” `<!-- ROW_MINE: ksummit-discuss.messages.350104 -->`

## 65.26 【Linux社区】维护者手册提案

- 【Linux社区】Williams 发 RFC 0/3：Subsystem Profile 记录各子系统潜规则，回收 MAINTAINERS 的 P 标签，附 nvdimm 样例与 145 行模板 `<!-- ROW_MINE: ksummit-discuss.messages.350105 -->`
