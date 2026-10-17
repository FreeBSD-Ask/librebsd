# 159 【Linux社区】Rust抽象与AI评审推进

> 来源：ksummit 独有 p23（50 封全读，2021-04 至 2026-07：Linus 系统论证 C 标准把内存访问定为不可观测是错误、单次读拆两次引入 TOCTOU 漏洞；Leemhuis 回归处理守则官方化提案全文含严重 bug 两三天一般三周时限与 FASTTRACK 标签；Mauro 对 conclave 项目延续预案逐条批评 72 小时失联兜底与 TAB 零当选最坏情况；Starovoitov 宣布 BPF AI 评审工具以纯文本邮件直接进入开发流程；Rust 抽象架构与演化稳定性、Link 标签替代与规范、Bugzilla 退役、malloc 提案争论、AI 生成内容版权与准则）
> 判定：45 CAND / 5 NV。主题分布：AI补丁评审工具 2、Rust别名模型讨论 1、Rust与C安全对比 1、AI生成内容版权 1、闭源用户态政策 1、AI标注与隐私 1、Link标签替代 2、CC列表自动化 1、Link标签规范 3、回归处理准则 1、Revocable防UAF 1、AI评审提示词 1、PGP密钥过期争论 1、TAB选举资格 1、C标准UB争论 1、CC列表实践 1、Rust文件布局争论 1、面板驱动生态 1、trivial 补丁信任 1、Rust GPIO驱动 1、AI slop条款争论 1、malloc提案争论 2、DT绑定仓库 1、linux-next测试 1、变量声明风格 1、文档构建痛点 1、Bugzilla退役 2、安全披露流程 1、维护者倦怠 1、维护者档案文档 1、HIGHMEM淘汰 1、AI生成内容准则 1、Rust演化稳定性 1、Rust抽象架构 2、Rust内核政策争论 1、文档构建性能 2、项目延续预案 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p23 的逐封提取（2021-04 至 2026-07，45 CAND / 5 NV），全 37 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 159.1 AI补丁评审工具

- 【Linux社区】Starovoitov称下一步把BPF AI评审以纯文本邮件融入正常开发流程；Chris Mason大幅降低误报，AI评审多次发现维护者未察觉的bug，个别案例AI把bug解释得比维护者更清楚。 `<!-- ROW_MINE: ksummit.messages.3522 -->`
- 【Linux社区】Lunn主张AI评审工具应面向全体开发者、在提交前自查修复，维护者只需验证开发者已运行工具，质疑Mason把降低维护者负担设为长期目标的定位。 `<!-- ROW_MINE: ksummit.messages.3595 -->`

## 159.2 Rust别名模型讨论

- 【Linux社区】与Miguel辨析“假阳性”歧义；引Ralf Jung澄清：Rust绝不绑定LLVM别名规则、参考文档非规范，拥有第二个主要编译器可防语言定义过拟合。 `<!-- ROW_MINE: ksummit.messages.3524 -->`

## 159.3 Rust与C安全对比

- 【Linux社区】引Uecker数据：C23核心约87处UB，C2Y已删17处、另有12项提案在手；Masłowski反驳Rust安全源于类型设计防误用、所有权本质是资源安全，仅加注解达不到同等安全。 `<!-- ROW_MINE: ksummit.messages.3526 -->`

## 159.4 AI生成内容版权

- 【Linux社区】Mauro区分情形：译文保留原作者版权、AI做骨架代码等机械填充无版权问题；自述实验显示AI代码如初学者水平、错误雷同，训练权重趋向复现最常见的模式。 `<!-- ROW_MINE: ksummit.messages.3527 -->`

## 159.5 闭源用户态政策

- 【Linux社区】Jani Nikula提出判据：专有栈能复现而开放栈不能的bug，其修复不会进内核；追问仅把从专有栈简化出的复现器放入测试资产是否足够，Geert主张先加测试用例。 `<!-- ROW_MINE: ksummit.messages.3537 -->`

## 159.6 AI标注与隐私

- 【Linux社区】回应McKenney对提示被记录可遭法律调取的担忧：所指“本地服务”是无网络依赖的开源工具，担心者可用分叉或在隔离VM中运行，开源生态会淘汰带遥测的版本。 `<!-- ROW_MINE: ksummit.messages.3540 -->`

## 159.7 Link标签替代

- 【Linux社区】Greg KH反对用git notes承载Link元数据：发行版、stable与triage人员处理整棵树，须跨全部子系统翻找notes，除非合并为统一notes树否则不可行。 `<!-- ROW_MINE: ksummit.messages.3541 -->`
- 【Linux社区】Bottomley发起议题：Link trailer消失后工具链与分诊受冲击，Konstantin正开发补救工具，提议讨论让Link或替代标签成为人人可用的指针。 `<!-- ROW_MINE: ksummit.messages.3610 -->`

## 159.8 CC列表自动化

- 【Linux社区】公布其cc脚本：封面信若抄送全部维护者使头部超512字符则只发邮件列表；并展示remove_undesirable_emails.sh用grep过滤Ingo Molnar地址。 `<!-- ROW_MINE: ksummit.messages.3545 -->`

## 159.9 Link标签规范

- 【Linux社区】回应Ellerman“Message-Id难点击”之抱怨：查看原始提交通常无用，仍推荐msgid.link链接；但真正的难题是可靠地把commit映射到补丁提交以支撑评审自动化。 `<!-- ROW_MINE: ksummit.messages.3551 -->`
- 【Linux社区】不建议在patch.msgid.link链接中嵌列表名：列表会迁移或改名；整体趋势是弱化“发往哪个列表”的意义，已支持lei查询并将桥接forge提交接口。 `<!-- ROW_MINE: ksummit.messages.3609 -->`
- 【Linux社区】Leemhuis的RFC补丁在5.Posting.rst补写Fixes:与Link:标签说明，并注明维护者常用b4或git钩子自动补Link指向最新公开评审帖。 `<!-- ROW_MINE: ksummit.messages.3659 -->`

## 159.10 回归处理准则

- 【Linux社区】Leemhuis提议将回归处理守则官方化并请Linus背书；细则含严重bug两三天内、一般三周内合入修复，称最大拖延是修复滞留子系统树数周，拟议[FASTTRACK]类标签。 `<!-- ROW_MINE: ksummit.messages.3553 -->`

## 159.11 Revocable防UAF

- 【Linux社区】依Kosina与Greg反馈修订摘要：revocable与devres分工在访问失效而非生命周期清理，devm_可建构其上如Rust版devm_*；已用于ChromeOS EC驱动修复真实UAF。 `<!-- ROW_MINE: ksummit.messages.3562 -->`

## 159.12 AI评审提示词

- 【Linux社区】Gushchin披露正试验Sashiko依邮件中人工反馈自动生成评审提示词且初步见效；Mauro建议新提示生效前应向子系统维护者展示应用前后的评审差异并征得同意。 `<!-- ROW_MINE: ksummit.messages.3572 -->`

## 159.13 PGP密钥过期争论

- 【Linux社区】反驳Linus废止主张：过期日促使密钥更新扩散并作失联者开关；手工验证2014年签名gpg返回0而git显示红色，指系git显示缺陷；Sequoia已分离导入与信任，将推动内核钥匙环采用过期日。 `<!-- ROW_MINE: ksummit.messages.3576 -->`

## 159.14 TAB选举资格

- 【Linux社区】反映2021年TAB选举投票资格混乱：Abbott向超50提交者寄发通知后，选民不确定自己是否在名单、是否须在自动寄发选票前主动申请。 `<!-- ROW_MINE: ksummit.messages.3581 -->`

## 159.15 C标准UB争论

- 【Linux社区】Linus指C标准把内存访问定为不可观测是错误的：源码单次读被编译成两次读会引入TOCTOU安全问题，单次写成两次写更是bug；要求编译器对UB告警或按朴素语义定义。 `<!-- ROW_MINE: ksummit.messages.3601 -->`

## 159.16 CC列表实践

- 【Linux社区】Carpenter自述精简抄送习惯：无线补丁不必抄netdev、amd gpu补丁不必抄drm，bug报告只抄一个lore列表；并知悉tracing经linux-trace-kernel进patchwork而讨论留在LKML。 `<!-- ROW_MINE: ksummit.messages.3605 -->`

## 159.17 Rust文件布局争论

- 【Linux社区】回应Lunn关于Rust封装文件移动妨碍stable回溯移植的担忧：文件每个发布周期都在移动，对stable维护者不是大事，只要求无充分理由不移动。 `<!-- ROW_MINE: ksummit.messages.3607 -->`

## 159.18 面板驱动生态

- 【Linux社区】Armstrong称面板IC厂商极少公开数据手册、从无厂商直接提交内核补丁；DDIC高级特性命令无公开文档难建通用API；高通下游以超通用驱动加复杂DT支持面板，上游碎片化严重。 `<!-- ROW_MINE: ksummit.messages.3614 -->`

## 159.19 trivial 补丁信任

- 【Linux社区】回应Mauro设想的开发者信任分脚本：警告会使新开发者处于劣势，须先想清楚再设准入门槛；背景为明尼苏达事件后关于 trivial 补丁（平凡补丁）审查的争论。 `<!-- ROW_MINE: ksummit.messages.3616 -->`

## 159.20 Rust GPIO驱动

- 【Linux社区】Wedson发布由C改写的可运行PL061 GPIO Rust驱动链接，并附C与Rust两版并排对照的HTML渲染，作为2021年Rust for Linux能力的实物演示。 `<!-- ROW_MINE: ksummit.messages.3617 -->`

## 159.21 AI slop条款争论

- 【Linux社区】Dan Williams反对在流程文档中写明可凭疑似AI slop直接拒稿：担心助长“猎杀slop”并在误指时伤害项目健康，认为“不信任提交者”等既有反馈比贴标签更可操作。 `<!-- ROW_MINE: ksummit.messages.3619 -->`

## 159.22 malloc提案争论

- 【Linux社区】Kees Cook强烈反对内核实现malloc：此类API有缺陷，如同刚移除的strncpy；分配应基于类型而非字节数，尺寸是“需要放什么”的副产品，按字节分配会丢失编译器可用元数据。 `<!-- ROW_MINE: ksummit.messages.3624 -->`
- 【Linux社区】Carpenter以XKCD 927质疑再造分配API；主张承认小分配不会失败，在km/zalloc_obj加BUILD_BUG_ON限定小对象以删除错误处理；并问KASAN能否查kmem_cache与mempool的UAF。 `<!-- ROW_MINE: ksummit.messages.3638 -->`

## 159.23 DT绑定仓库

- 【Linux社区】转述Rob Herring立场：内核拥有全球最多硬件支持故绑定不迁出内核；devicetree-rebasing独立仓库已存在且U-Boot已采用；Dooley称将出席LPC的DT BoF。 `<!-- ROW_MINE: ksummit.messages.3628 -->`

## 159.24 linux-next测试

- 【Linux社区】Bottomley称测试信号到手时-next已变且存在rebase风险，故更常测mainline并主张引导测stable群体上移main；Brown认为-next测试尚可，bisect从Linus树基线起即可。 `<!-- ROW_MINE: ksummit.messages.3630 -->`

## 159.25 变量声明风格

- 【Linux社区】Dobriyan历数C89函数首部声明之弊：扩大作用域增加笔误、膨胀行数、阻碍加const、打断思路，还衍生按长度排序等子风格，主张彻底废弃该规则。 `<!-- ROW_MINE: ksummit.messages.3631 -->`

## 159.26 文档构建痛点

- 【Linux社区】Linus列文档构建两症结：告警噪音过大使其无法用作校验手段，类比内核构建必须零告警；Fedora自带sphinx过旧、makefile给出错误的pip安装指引，正确做法是装python3-sphinx。 `<!-- ROW_MINE: ksummit.messages.3632 -->`

## 159.27 Bugzilla退役

- 【Linux社区】赞成逐步退役Bugzilla，主张LLM应在提交端辅助用户写出好报告并分流而非事后筛除；已参考Mason评审提示词着手原型，呼吁聚合散落各处的问题追踪器。 `<!-- ROW_MINE: ksummit.messages.3636 -->`
- 【Linux社区】主张面向普通用户的报告入口：按模块名与类别而非源文件，指mm有18个“MEMORY MANAGEMENT”开头条目易混淆，栈轨迹输入更佳；若无人短期实现网页界面应先更换Bugzilla欢迎页。 `<!-- ROW_MINE: ksummit.messages.3687 -->`

## 159.28 安全披露流程

- 【Linux社区】回应发行版想要提前情报：认为与会的维护者无实权解决，峰会不邀请项目经理与VP；预测各国立法强制基于-stable后政府将替社区解决该问题。 `<!-- ROW_MINE: ksummit.messages.3641 -->`

## 159.29 维护者倦怠

- 【Linux社区】Pinchart以亲身经历指“交换评审”在无商业利益领域失效：大厂贡献者只愿评审其参与驱动；建议资源充足的公司贡献者划出时间评审其专长但非商业利益内代码。 `<!-- ROW_MINE: ksummit.messages.3642 -->`

## 159.30 维护者档案文档

- 【Linux社区】指Maintainer Entry Profile现仅7份、ext4即将新增；建议以符号链接把档案移入子系统目录提升可见度并激励更多子系统编写，因Sphinx不喜根外文档故用ln -rs方案。 `<!-- ROW_MINE: ksummit.messages.3649 -->`

## 159.31 HIGHMEM淘汰

- 【Linux社区】就32位时代1GB内存机器给出数字：约896MB低端内存加约120MB高端内存，或用2G:2G划分；主张博物馆级旧机留在旧内核，不确信为其维护现代内核。 `<!-- ROW_MINE: ksummit.messages.3661 -->`

## 159.32 AI生成内容准则

- 【Linux社区】Corbet认可generated-content.rst第五版实质并愿合入，同时声明今后对该文件的修改将比照coding-style.rst处理，缺乏强社区共识不轻易应用。 `<!-- ROW_MINE: ksummit.messages.3669 -->`

## 159.33 Rust演化稳定性

- 【Linux社区】引Rust 1.80破坏time crate、crater波及超5000个crate为例指Rust比C更愿破坏兼容；Jung澄清新trait solver部分用于1.84，AWS或有三百余Rust开发者。 `<!-- ROW_MINE: ksummit.messages.3672 -->`

## 159.34 Rust抽象架构

- 【Linux社区】Ojeda阐明leaf模块设计：C API经Rust抽象层供Rust模块消费，反向向C暴露子系统会损失类型系统与安全保证；曾向C委员会提[[safe]]属性未获接受，期望落地于Clang与GCC。 `<!-- ROW_MINE: ksummit.messages.3677 -->`
- 【Linux社区】Brown同意rust/集中放共享抽象的设计，但主张建立机制确保子系统维护者能知晓其子系统正在进行的Rust工作，避免在角落里无可见性地推进。 `<!-- ROW_MINE: ksummit.messages.3690 -->`

## 159.35 Rust内核政策争论

- 【Linux社区】答Hellwig质疑：仅靠C头文件注解无法达成内存安全；即便实现safe C也解决不了不稳定API向Rust侧传播的问题，故C API安全只是附赠目标而非项目主旨。 `<!-- ROW_MINE: ksummit.messages.3678 -->`

## 159.36 文档构建性能

- 【Linux社区】Nossum给出实测：用PyPy跑Sphinx提速22%；自行剖析发现约40%耗时在resolve_xref的C域代码，GCC文档同病，建议提供conf.py开关禁用C域。 `<!-- ROW_MINE: ksummit.messages.3679 -->`
- 【Linux社区】Mauro说明kernel-doc受Python GIL限制无法并行，早期并行实验更慢而放弃；待Python去GIL后一年内可恢复，解析器按文件实例化本为并行设计；Sphinx HTML构建器去GIL收益更大。 `<!-- ROW_MINE: ksummit.messages.3691 -->`

## 159.37 项目延续预案

- 【Linux社区】对conclave.rst逐条提修正：组织者72小时失联则上届峰会参与者可启动；反对TAB作后备因最坏情况可能无当选成员；15个月窗口最坏达23个月，需LF合法签署SoB。 `<!-- ROW_MINE: ksummit.messages.3680 -->`
