# 55 【Linux社区】CoC补丁战与官方叙事之求

> 来源：ksummit-discuss p107（50 封全读，2018-09-19/23，夹杂 KS2014 档案信 2014-05-03/15）。
> 判定：50 CAND / 0 NV。主题分布：coc 31、KS2014 6、communication 5、governance 3、security 3、memory-model 1、next-discipline 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p107（pk 349556-349605）的逐封提取（50 CAND / 0 NV），全 6 块采用**导语＋带锚条目体例**：每块由“## 55.x 【Linux社区】题名”＋导语段＋“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——导语段承担“要点”职能、带锚条目承担“史料”与“史料锚”职能（ROW_MINE 坐标与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 55.1 【Linux社区】CoC 补丁战与官方叙事之求

2018-09-19/20 CoC 补丁战全记录：Tony Luck 与 Mauro 的两版 code-of-conduct.rst 补丁全文、Airlie/Tim/Jani/Woodhouse/Vetter 的法理与流程之争、Rafael 的执行责任三问与 dri-devel 操作经验、Perches“代码/行为”二分。

- 【Linux社区】Mauro 语法分析论：逗号使“such as a physical or electronic address”成为“private information”的定义；“foo”替换实验证明系两句合并 `<!-- ROW_MINE: ksummit-discuss.messages.349557 -->`
- 【Linux社区】Tony Luck 直接给出 **code-of-conduct.rst** 补丁：地址[1]+脚注“公共邮件列表地址不属私人信息、应（事实上应当）用于致谢标签” `<!-- ROW_MINE: ksummit-discuss.messages.349558 -->`
- 【Linux社区】Mauro 给 Tony 补丁回 Reviewed-by `<!-- ROW_MINE: ksummit-discuss.messages.349561 -->`
- 【Linux社区】Tim Bird：直截了当解决歧义；CoC 修改流程之问（“由 Greg 决定”） `<!-- ROW_MINE: ksummit-discuss.messages.349562 -->`
- 【Linux社区】Mauro 驳 Airlie 并自拟大补丁：删“in good faith”罚则段、scope 收窄 kernel.org、IRC 公共渠道入脚注 `<!-- ROW_MINE: ksummit-discuss.messages.349563 -->`
- 【Linux社区】Airlie 法理反驳：社区准则集非法律文档；drm 组维护制实践（私信转公开） `<!-- ROW_MINE: ksummit-discuss.messages.349559 -->`
- 【Linux社区】Tim Bird“我家派对规则”类比；求法诉实例；建议研究其他项目采纳史 `<!-- ROW_MINE: ksummit-discuss.messages.349564 -->`
- 【Linux社区】Hemminger“请保留牛津逗号” `<!-- ROW_MINE: ksummit-discuss.messages.349565 -->`
- 【Linux社区】Jani：广泛使用胜于自改——“如 GPL 之于 copyleft”；正道是 Contributor Covenant 上游 `<!-- ROW_MINE: ksummit-discuss.messages.349566 -->`
- 【Linux社区】Josh Triplett Seconded：内核特定澄清放单独文档 `<!-- ROW_MINE: ksummit-discuss.messages.349568 -->`
- 【Linux社区】Woodhouse：“Linus 对 GPL 也不是这么干的”；前加声明方案 `<!-- ROW_MINE: ksummit-discuss.messages.349569 -->`
- 【Linux社区】Vetter：fd.o 流程细节入单独 policy；隐私政策“发邮件列表即公开、不喜欢就别发” `<!-- ROW_MINE: ksummit-discuss.messages.349570 -->`
- 【Linux社区】Pinchart：或在文档旁加 FAQ 澄清内核解释 `<!-- ROW_MINE: ksummit-discuss.messages.349576 -->`
- 【Linux社区】Rafael 选虫问：Our Responsibilities 要我做什么？何为 fair corrective action？须拒绝正确代码吗？ `<!-- ROW_MINE: ksummit-discuss.messages.349572 -->`
- 【Linux社区】Vetter 以 dri-devel 经验作答：公开回复+私聊、fd.o 只作上诉机构、“Ultimately, yes”、暂停 commit 权限冷却 `<!-- ROW_MINE: ksummit-discuss.messages.349573 -->`
- 【Linux社区】Vetter：“CoC 执行是一种技能——或值得在 kernel summit 安排培训” `<!-- ROW_MINE: ksummit-discuss.messages.349574 -->`
- 【Linux社区】Brown 极端案例：曾拒绝“commit message 全是辱骂”的 bugfix `<!-- ROW_MINE: ksummit-discuss.messages.349592 -->`
- 【Linux社区】Perches：删法律腔；“维护者负责代码，社区负责行为” `<!-- ROW_MINE: ksummit-discuss.messages.349580 -->`
- 【Linux社区】Pinchart 问“谁是社区？维护者不是一部分吗？” `<!-- ROW_MINE: ksummit-discuss.messages.349581 -->`
- 【Linux社区】Perches 答：社区不止维护者、更多人应参与行为管理 `<!-- ROW_MINE: ksummit-discuss.messages.349587 -->`
- 【Linux社区】Tim Bird：法诉风险被夸大；责任方向误解论（维护者夹在贡献者与 Linus 之间）；“无记录有人因未执行 CoC 被封” `<!-- ROW_MINE: ksummit-discuss.messages.349588 -->`
- 【Linux社区】Mauro：“期待 FAQ；若当初加顶注说明 roll-out 时序则好得多；这一份为 GitHub 而生” `<!-- ROW_MINE: ksummit-discuss.messages.349597 -->`

## 55.2 【Linux社区】Biederman 坏补丁论与 Mauro 攻击剧本

CoC 之战的两个极端文本：Biederman 的补丁审查视角全面检视（rc4 时点/无讨论/领导力空转/GPL 疑虑）与 Mauro 的“假账号自演控告”攻击剧本及镜像档案不可编辑论。

- 【Linux社区】Biederman 长文：评 8a104f8b5867“我们刚合入了一个坏补丁”；rc4 不宜合入；事前无讨论、TAB 补救未变；“维护者唯一实权是收不收代码”；若系法律文档则近于 GPL 违反；“kernel.org 只是 HPA 搭的基础设施、LF 不是内核项目”；PS：最常见滥用“无限提交不听反馈”从未被处理 `<!-- ROW_MINE: ksummit-discuss.messages.349584 -->`
- 【Linux社区】Jani 驳 Mauro：“大多是 FUD”；维护者不能视而不见；drm 可向 fd.o 升级封禁 `<!-- ROW_MINE: ksummit-discuss.messages.349585 -->`
- 【Linux社区】Mauro 回击：解析强制链（不作为→TAB→维护者受罚、无一字罚违规者）；“邮件被镜像后如何 remove/edit？只封人不改档案就没按 CoC 字面执行” `<!-- ROW_MINE: ksummit-discuss.messages.349586 -->`
- 【Linux社区】Mauro 驳“广泛采用”论：Contributor Covenant 为 GitHub 而生；LKML 无法 moderate；伪造账号自演控告即可搞掉任意维护者的攻击剧本；三选项（revert/换 CoC/打补丁）；“或等到 Maintainer's Summit 再发 PR” `<!-- ROW_MINE: ksummit-discuss.messages.349577 -->`

## 55.3 【Linux社区】官方叙事之求：沉默震耳欲聋与 Corbet 回应

2018-09-20 CoC 变更后的社区心理实录：Pinchart 的“Bastille”隐喻与官方叙事之求、Corbet 的断头台否认与图景之诺、Torokhov 的“凭空冒出”指控。

- 【Linux社区】Pinchart：“列表上的沉默震耳欲聋——私谈横行、公开言说有顾虑”；“Bastille 倒下后聪明人不急着表态”；求绿灯的官方论坛；求官方叙事——“数位 TAB 成员签署但绝非社区压倒性多数；流言四起” `<!-- ROW_MINE: ksummit-discuss.messages.349594 -->`
- 【Linux社区】Corbet（仅代表自己）：“人们有理由担心这种变更方式；不信有人在架断头台；没人该指望 TAB 提出所有对的问题——别复制网上的非理性讨论”；“几乎无人有完整图景——包括我——我会试着促成” `<!-- ROW_MINE: ksummit-discuss.messages.349596 -->`
- 【Linux社区】Torokhov：“旧的 Code of Conflict 至少在维护者间流传过，这个凭空冒出” `<!-- ROW_MINE: ksummit-discuss.messages.349595 -->`
- 【Linux社区】Pinchart 求公开论坛：FAQ 同样方式再扔会再现同样感受；“能被听见的中道即可” `<!-- ROW_MINE: ksummit-discuss.messages.349591 -->`
- 【Linux社区】Tim Bird：Maintainer's Summit 前有可讨论之物；FAQ 避免无尽缠斗；开放其他场 `<!-- ROW_MINE: ksummit-discuss.messages.349593 -->`

## 55.4 【Linux社区】治理续论：维护者特权词汇之争与 RTC 数据再辩

维护者特权词汇之辩的收束与 RTC 贡献数据战的第三回合（Perches 孤立子系统论+Zummo 事实）。

- 【Linux社区】Pinchart 答 Rafael：非孤例但无精确数字；未向上反映（放弃有影响）；“压倒性多数尽力；存在滥用案例不应沉默；忽视更具破坏性；愿换词汇” `<!-- ROW_MINE: ksummit-discuss.messages.349575 -->`
- 【Linux社区】Rafael 容量论：有意义评审须熟悉代码与假设、工具更换不会凭空给人知识、保留已投入者是唯一出路 `<!-- ROW_MINE: ksummit-discuss.messages.349571 -->`
- 【Linux社区】Perches 驳 Vetter：孤立子系统论；Zummo 2015 后未签 commit；一次性贡献偏向空白与 checkpatch 更新 `<!-- ROW_MINE: ksummit-discuss.messages.349602 -->`
- 【Linux社区】sfr：linux-next 列表上可见、不必每件 CC `<!-- ROW_MINE: ksummit-discuss.messages.349560 -->`

## 55.5 【Linux社区】新议题三连与附件补丁 bot 设计

议题池扩充：Security 会话（Morris/Carpenter/Abbott）、内存一致性模型 hands-on（Parri/McKenney）、附件补丁 bot 设计（Olof）与工具链流失数据（Vetter/Pinchart）。

- 【Linux社区】James Morris 新议题：Security 讨论（2017 议程链接、2018 议程 11 月定） `<!-- ROW_MINE: ksummit-discuss.messages.349600 -->`
- 【Linux社区】Dan Carpenter 倡公开安全讨论列表：维护者“既嫌转发又不甘后知”不可兼得；“安全工作孤独”；一个整数溢出修复重修三次；“5% vs 95% 误报” `<!-- ROW_MINE: ksummit-discuss.messages.349603 -->`
- 【Linux社区】Laura Abbott：区分安全兴趣组与安全响应（security@/kernel-hardening） `<!-- ROW_MINE: ksummit-discuss.messages.349605 -->`
- 【Linux社区】Parri 与 McKenney 提 Concurrency with tools/memory-model：**memory-barriers.txt** 之弊；1c27b644c0fd 内存一致性模型 hands-on `<!-- ROW_MINE: ksummit-discuss.messages.349604 -->`
- 【Linux社区】Olof 具体化附件补丁 bot：checkpatch+apply 检查+内联 reply-all+可过滤 `<!-- ROW_MINE: ksummit-discuss.messages.349598 -->`
- 【Linux社区】Olof 答 Mauro：bot 宽容接受；bot 互相过滤 `<!-- ROW_MINE: ksummit-discuss.messages.349599 -->`
- 【Linux社区】Vetter 数据：2 人因 archaic toolchain 离开、新工程师 raving merge request `<!-- ROW_MINE: ksummit-discuss.messages.349579 -->`
- 【Linux社区】Pinchart 求离职者痛点；“gerrit 强推你会失去我” `<!-- ROW_MINE: ksummit-discuss.messages.349582 -->`
- 【Linux社区】Vetter 自嘲与 stone tablets 出处 `<!-- ROW_MINE: ksummit-discuss.messages.349583 -->`

## 55.6 【Linux社区】KS2014 档案六封

页内夹杂的 KS2014 档案信（2014-05-03/15）：QR oops 与发行版时滞、2038、tinification、议题人事名录。

- 【Linux社区】Kurusa：QR 让非技术用户报 bug；Debian 3.2（N-13）之叹 `<!-- ROW_MINE: ksummit-discuss.messages.349556 -->`
- 【Linux社区】Boyer：ABRT 带来更多报告但更不懂 bisect；Debian 最坏情形 `<!-- ROW_MINE: ksummit-discuss.messages.349567 -->`
- 【Linux社区】hpa 2038：ubiquitous upgrades 或已解决 `<!-- ROW_MINE: ksummit-discuss.messages.349578 -->`
- 【Linux社区】Brown tinification：kprobes 可行、tracepoints 溢出风险 `<!-- ROW_MINE: ksummit-discuss.messages.349589 -->`
- 【Linux社区】Ted：per topic people 提名名单全录（live patching/ACPI-DT/energy bias 人事名录） `<!-- ROW_MINE: ksummit-discuss.messages.349590 -->`
- 【Linux社区】Kosina：Joey Li 是 jlee@suse.com `<!-- ROW_MINE: ksummit-discuss.messages.349601 -->`
