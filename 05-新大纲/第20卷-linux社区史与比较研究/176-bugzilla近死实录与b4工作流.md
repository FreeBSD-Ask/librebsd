# 176 【Linux社区】bugzilla近死实录与b4工作流

> 来源：ksummit 独有 p40（50 封全读，2021-04 至 2026-07：Ryabitsev 详述 bugzilla 平台近死开发停滞不兼容新 MySQL 转 Postgres 苦撑与 LF 基建立场、Greg KH 明确拒绝 GitLab；Kozlowski 用 git 统计 133 个被子维护者囤积数周才进 linux-next 的提交并点名 Intel i915 与 MediaTek 实例；Linus 亲自给出 prepare-commit-msg 钩子跑 b4 dig 替代无意识 Link 标记的具体方案披露本人 lore/b4 工作流用法；Bottomley 从版权法表达与思想框架分析 AI 补丁何时须在签收链记录；bugzilla 存废六封、峰会 2021 筹备三封、linus-next 测试三封、AI 补丁标注三封）
> 判定：41 CAND / 9 NV。主题分布：LPC议题投稿 1、linus-next测试 3、stable树邮件 1、C聚合传递之争 2、设备直通生态 1、trivial补丁废除 1、回归处理流程 2、工具生成内容规范 2、THE REST列表迁移 1、KTODO任务清单 1、VLIW与OoO之辩 1、bugzilla存废 6、Link标记之争 2、加速器用户态 2、维护者树隐匿 1、AI补丁标注 3、峰会2021筹备 3、Rust进内核之辩 3、TAB选举 2、栈回溯行号 1、补丁投递礼仪 1、内核文档工具链 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p40 的逐封提取（2021-04 至 2026-07，41 CAND / 9 NV），全 22 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 176.1 LPC议题投稿

- 【Linux社区】Rostedt说明LPC微会议题15-30分钟偏讨论、不含Plumbers入场券，Track议题更长；指导YoungJun将已提交摘要改选“Kernel Memory Management MC”轨道。 `<!-- ROW_MINE: ksummit.messages.6201 -->`

## 176.2 linus-next测试

- 【Linux社区】Geert认为0-day对编译失败报告做得好、会通知作者与维护者，但维护者仍可无视报告；回应Linus要求自动化定位故障树、勿靠人肉的设想。 `<!-- ROW_MINE: ksummit.messages.6214 -->`
- 【Linux社区】Leemhuis仍倾向改进pending-fixes而非新建linus-next树，指出无-fixes分支或迟入库的子系统破坏其回归追踪；Sasha解释query.db记录commit-id变更。 `<!-- ROW_MINE: ksummit.messages.6260 -->`
- 【Linux社区】Brown认为-next实际测试者远多于stable rc，虽偶有rebase但多为小麻烦，测试超一天的树才困难；难以让stable测试群体整体转向mainline。 `<!-- ROW_MINE: ksummit.messages.6339 -->`

## 176.3 stable树邮件

- 【Linux社区】Levin称“已加入stable树”通知邮件纯属垃圾、想停发又怕有人依赖（早于lei/lore时代）；Ryabitsev建议改写入public-inbox源仅存档不投递。 `<!-- ROW_MINE: ksummit.messages.6219 -->`

## 176.4 C聚合传递之争

- 【Linux社区】Ojeda澄清内核Rust以abort模式编译panic：析构不运行、异常不可捕获、当前映射到BUG()，故无需考虑C++式异常安全，与回溯遍历是两回事。 `<!-- ROW_MINE: ksummit.messages.6225 -->`
- 【Linux社区】Ventura Jack引c2rust缺陷单反驳Gary Guo：关闭严格别名编译的C常无UB，转成unsafe Rust反有UB，因Rust别名约束更严，并引两篇技术博客佐证。 `<!-- ROW_MINE: ksummit.messages.6289 -->`

## 176.5 设备直通生态

- 【Linux社区】Kosina以hidraw作者身份回忆：当年担心raw接口冲击HID驱动生态，结果未发生，hidraw只用于一次性设备方案，通用驱动仍在内核正常实现。 `<!-- ROW_MINE: ksummit.messages.6230 -->`

## 176.6 trivial补丁废除

- 【Linux社区】Kosina决定在5.13从Documentation与MAINTAINERS删除trivial补丁条目：补丁工具已改进，错别字补丁反制造无谓冲突，trivial列表已无价值。 `<!-- ROW_MINE: ksummit.messages.6231 -->`

## 176.7 回归处理流程

- 【Linux社区】Leemhuis承认无回归硬数据、regzbot难以获知DRM外部缺陷跟踪器中的报告；Howlett主张在Plumbers讨论工作流，因Maintainers峰会覆盖不了最需改进者。 `<!-- ROW_MINE: ksummit.messages.6233 -->`
- 【Linux社区】Bottomley观察带Fixes与cc:stable的修复在合并窗外平稳回移，问题主要出自无cc:stable的autosel批量回移；提议合并窗内推迟autosel并索要回归占比数据。 `<!-- ROW_MINE: ksummit.messages.6313 -->`

## 176.8 工具生成内容规范

- 【Linux社区】Hansen讨论工具生成内容指南v5措辞，改为“即使工具使用超出范围也应考虑披露”；示例含checkpatch --fix、Coccinelle、AI生成变更日志等。 `<!-- ROW_MINE: ksummit.messages.6234 -->`
- 【Linux社区】Rostedt支持Bottomley反对在工具生成内容指南用俚语“slop”，认为俚语会随时间失义（举rawdog、chad），文档措辞须长期稳定。 `<!-- ROW_MINE: ksummit.messages.6311 -->`

## 176.9 THE REST列表迁移

- 【Linux社区】Herring比较lore回复链接的3种方式，指出有message-id时b4好用、要mbox检索用lei；回应Bottomley关于回复未订阅列表的工具之问。 `<!-- ROW_MINE: ksummit.messages.6236 -->`

## 176.10 KTODO任务清单

- 【Linux社区】Carpenter提议评审者用“KTODO:”行记录顺手发现的小任务，学生与janitor可用lei查询lore近半年KTODO找活，兼作新人任务入口。 `<!-- ROW_MINE: ksummit.messages.6237 -->`

## 176.11 VLIW与OoO之辩

- 【Linux社区】Anvin反驳Overstreet：VLIW与OoO并非正交，OoO动态调度更强，VLIW是演化死路除非按代JIT；呼应Linus别名很少要紧、内核尽量关掉UB之论。 `<!-- ROW_MINE: ksummit.messages.6240 -->`

## 176.12 bugzilla存废

- 【Linux社区】Rostedt主张学Debian reportbug做交互式缺陷报告工具、可自动回复已知问题；Leemhuis称回归联络人价值有限，优先做引导用户写好报告的工具。 `<!-- ROW_MINE: ksummit.messages.6244 -->`
- 【Linux社区】Rostedt支持Morton设想在网页内嵌get_maintainer.pl前端，并讲述有人发现驱动缺陷却因不会报而放弃的实例，自嘲现行土办法是造随机补丁跑脚本。 `<!-- ROW_MINE: ksummit.messages.6277 -->`
- 【Linux社区】Greg KH借wdat_wdt加载失败实例示范用get_maintainer.pl定位看门狗维护者、指示发ACPI列表，回应“该CC谁”之问，展示现行求助路径。 `<!-- ROW_MINE: ksummit.messages.6280 -->`
- 【Linux社区】Ryabitsev驳gitlab.kernel.org方案：无人负责处理缺陷的问题换平台依旧，且集中单点易受国家级封锁与政治影响，GitLab商业开放核心模式亦有被收购风险。 `<!-- ROW_MINE: ksummit.messages.6315 -->`
- 【Linux社区】Rostedt自述用bugzilla.kernel.org管理trace-cmd/kernelshark等工具缺陷，工具类目未录入MAINTAINERS；并引Len Brown在峰会录像中称ACPI/PM依赖bugzilla。 `<!-- ROW_MINE: ksummit.messages.6330 -->`
- 【Linux社区】Ryabitsev详述bugzilla近死：开发停滞、不兼容新MySQL、只能跑mod_perl，LF IT转Postgres苦撑；Greg KH明确拒绝迁GitLab，称缺bugmaster才是症结。 `<!-- ROW_MINE: ksummit.messages.6338 -->`

## 176.13 Link标记之争

- 【Linux社区】Torvalds反对git notes（不可分发）与无意识Link标记，给出prepare-commit-msg钩子调用“b4 dig”把lore链接作注释插入提交说明的做法。 `<!-- ROW_MINE: ksummit.messages.6247 -->`
- 【Linux社区】Herring称git-am已能把message-ID写入提交信息、可用pager配置转成lore链接，不必等git新增ATOM_MESSAGEID；Bottomley正起草该git特性补丁。 `<!-- ROW_MINE: ksummit.messages.6248 -->`

## 176.14 加速器用户态

- 【Linux社区】Greg KH称难以为加速器自定义ioctl划线、拒绝替行业定标准，视其如普通字符驱动；反驳HabanaLabs“搭便车”论，指AOSP等并不接收厂商用户态代码。 `<!-- ROW_MINE: ksummit.messages.6249 -->`
- 【Linux社区】Belloni指出内核GPLv2系统调用例外使API一旦暴露给用户态即无法限制专有软件使用，Bottomley认为修改例外不明智、唯一手段是不导出接口。 `<!-- ROW_MINE: ksummit.messages.6276 -->`

## 176.15 维护者树隐匿

- 【Linux社区】Kozlowski统计linux-next两周新增中133个提交早被子维护者囤积数周，列Intel i915、MediaTek等实例；指出缺bot覆盖、集成测试且部分树未录入MAINTAINERS。 `<!-- ROW_MINE: ksummit.messages.6261 -->`

## 176.16 AI补丁标注

- 【Linux社区】Bottomley从版权法分析：AI仅给思路则无需记录，若AI产出的表达进入提交则须在签收链注明；举AI建议快排数周后自行实现即近于复制的灰色地带。 `<!-- ROW_MINE: ksummit.messages.6262 -->`
- 【Linux社区】Bottomley称Signed-off-by仅是法律陈述、外界无从验证，造假被识破才降信任；透露会议投稿评审中已用AI检测AI生成内容并有一定成效。 `<!-- ROW_MINE: ksummit.messages.6283 -->`
- 【Linux社区】McKenney坚持开源项目暂不用AI生成产物直至争议解决，援引DCO第(a)款“有权按开源许可提交”的合规难题，并警告AI问答无隐私、版权风险或更糟。 `<!-- ROW_MINE: ksummit.messages.6343 -->`

## 176.17 峰会2021筹备

- 【Linux社区】Pinchart与Bottomley争论疫情后线下会议：后者称远程参会将成常态但不因恐惧牺牲线下价值，Pinchart提出地理分布分会场并顾虑远程者沦为二等公民。 `<!-- ROW_MINE: ksummit.messages.6265 -->`
- 【Linux社区】Bottomley介绍Plumbers多年积累的话筒礼仪协议：专人提醒对麦发言、备可抛掷软垫话筒盒；疫情酒店要求每次抛掷后消毒，反而阻碍线下办会。 `<!-- ROW_MINE: ksummit.messages.6292 -->`
- 【Linux社区】Kosina问Kernel Summit是否跟随Linux基金会把2021 OSS从都柏林迁往西雅图的决定，折射疫情期间峰会选址的不确定性。 `<!-- ROW_MINE: ksummit.messages.6306 -->`

## 176.18 Rust进内核之辩

- 【Linux社区】GPIO维护者Walleij欢迎Rust尝试并拉入Bartosz与Viresh，主张优先用于网络攻击面如Rust版ksmbd以吸取WannaCry教训，质疑从设备驱动起步的价值。 `<!-- ROW_MINE: ksummit.messages.6268 -->`
- 【Linux社区】Romanovsky反对Rust：跨子系统重构将因双语受阻，CONFIG_RUST=y/n双配置令老客户场景测试矩阵翻倍；Ojeda答Rust经抽象层调用C、默认开启仅影响一处。 `<!-- ROW_MINE: ksummit.messages.6281 -->`
- 【Linux社区】Walleij称最大威胁是有组织的远程root漏洞利用，主张把Rust“武器化”投向攻防前线而非仅防驱动崩溃，回应Ojeda“无需重写全内核”的质疑。 `<!-- ROW_MINE: ksummit.messages.6310 -->`

## 176.19 TAB选举

- 【Linux社区】Corbet公告2024 TAB选举9月20-27举行，Brauner、Cook、Hansen、Kicinski、Williams届满；资格为2023年以来3个带签收tag提交，50个以上自动获票，沿用CIVS。 `<!-- ROW_MINE: ksummit.messages.6272 -->`
- 【Linux社区】Corbet公告2022 TAB选举9月12-14投票，Abbott、Brauner、Cook、Mason、Williams届满；总结TAB一年工作含UMN假提交事件后续、企业资助与CoC指引。 `<!-- ROW_MINE: ksummit.messages.6279 -->`

## 176.20 栈回溯行号

- 【Linux社区】Sasha的kallsyms行号表实测增44MiB、vmlinux增8.3%；Geert建议压缩存放，Bottomley提出崩溃时定长缓冲流式解压加线性扫描，避免内存分配与磁盘IO。 `<!-- ROW_MINE: ksummit.messages.6295 -->`

## 176.21 补丁投递礼仪

- 【Linux社区】Hellwig认同Romanovsky对“精心筛选TO/CC”投递恶习的指摘：此类补丁完全不可审，视心情要求重发或直接无视，属维护者峰会流程议题。 `<!-- ROW_MINE: ksummit.messages.6300 -->`

## 176.22 内核文档工具链

- 【Linux社区】Mauro称kernel-doc受Python GIL所限无法并行、并行化尝试反而更慢，待去GIL后重试；Corbet认为kernel-doc非瓶颈，更盼Sphinx HTML构建器多线程。 `<!-- ROW_MINE: ksummit.messages.6322 -->`
