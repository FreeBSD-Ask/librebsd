# 179 【Linux社区】加速器uAPI原则与PGP过期驳斥

> 来源：ksummit 独有 p43（50 封全读，2021-04 至 2026-08：Airlie 加速器驱动开源用户态要求原则性陈述含 uAPI 复杂度论证靠说不建社区与跨子系统维护者联盟起草通用文档计划；Linus 对 PGP 密钥自动过期最完整驳斥无人续期旧签名反显不可信应撤销而非过期；Levin 2025 年 AI 审查工具落地状态浓缩记录 AUTOSEL 获 Linus 好评 b4 AI 扩展 semcode 调用图 token 44 万降至 2.5 万；Overstreet 对 syzbot 与模糊测试文化系统性批评及覆盖率分析替代方案；Bugzilla 改革争论四封、AI 版权与 DCO 三封、设备直通与 fwctl 三封）
> 判定：41 CAND / 9 NV。主题分布：DRM分支管理争论 1、AI补丁审查工具 2、设备直通与fwctl 3、CI与维护者负担 1、AI标注标签争论 2、Bugzilla改革争论 4、静态分析提案 2、维护者治理规则 1、Link标签与消息溯源 3、Rust政策讨论 2、AI补丁文档规范 2、AI版权与DCO 3、linux-next测试 1、文件系统维护信任 2、2021峰会筹备 1、MAINTAINERS清理 1、回归跟踪regzbot 1、加速器用户态要求 1、Werror编译争论 1、MAINTAINERS分流 1、混合会议远程参与 1、补丁发送脚本 1、贡献者信任评分 1、DRM面板API 1、PGP密钥过期争论 1、Bugzilla替代方案 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p43 的逐封提取（2021-04 至 2026-08，41 CAND / 9 NV），全 26 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 179.1 DRM分支管理争论

- 【Linux社区】Airlie反驳Kozlowski：AMD与Intel各有50-100人多团队上游化未上市GPU、速度优先，难要求人人吃透上游周期；Qualcomm经Android或ChromeOS交付、回归压力不同，不可类比。 `<!-- ROW_MINE: ksummit.messages.6653 -->`

## 179.2 AI补丁审查工具

- 【Linux社区】Levin支持Mason的AI审查设想：AUTOSEL已是大规模AI审查流程且获Linus好评；正为b4扩展“b4 ai review”等本地工具；semcode使btrfs调用图查询token由44万降至2.5万。 `<!-- ROW_MINE: ksummit.messages.6655 -->`
- 【Linux社区】Arnaldo表态信服AI审查：团队实测Mason审查提示反馈良好；BPF CI证明AI能发现维护者漏掉的bug、有时解释更清楚；下一步把审查以纯文本邮件融入开发流程。 `<!-- ROW_MINE: ksummit.messages.6690 -->`

## 179.3 设备直通与fwctl

- 【Linux社区】Hellwig认为直通有用但协议未为此设计：SCSI与NVMe须屏蔽大量影响全局状态的命令，他并在NVMe技术工作组持续抵制会破坏既有访问控制的新命令。 `<!-- ROW_MINE: ksummit.messages.6657 -->`
- 【Linux社区】Williams说明CXL吸取NVDIMM教训，移除全局状态机（如scrub）的直通能力，scrub改走EDAC而非fwctl；“立即配置变更”类命令至少需CAP_SYS_RAWIO、可能加taint。 `<!-- ROW_MINE: ksummit.messages.6708 -->`
- 【Linux社区】Vetter认为GPU迟早需要fwctl、固件调试追踪已是痛点；呼吁明确各能力应归edac、netdev/gpu等还是专用子系统；强调fwctl不得排挤功能接口，将去fwctl文档给出ack。 `<!-- ROW_MINE: ksummit.messages.6755 -->`

## 179.4 CI与维护者负担

- 【Linux社区】Rostedt主张RFC补丁可免测试门槛，但修复类补丁若连自动测试都过不了，应由自动化拒绝、无需维护者介入，以此减轻维护负担。 `<!-- ROW_MINE: ksummit.messages.6659 -->`

## 179.5 AI标注标签争论

- 【Linux社区】Rostedt以K&R教材代码被广泛复用为例谈版权先例：作者鼓励使用、无从追责，但担心对AI过于宽松的人终会“被烧到”。 `<!-- ROW_MINE: ksummit.messages.6663 -->`
- 【Linux社区】Howlett认为LLM普及后Assisted-by标签信息量趋零，MM代码已被sashiko全量AI巡检、再加标注只是噪音；反问是否预期某AI日后被判侵权而需审计历史提交。 `<!-- ROW_MINE: ksummit.messages.6734 -->`

## 179.6 Bugzilla改革争论

- 【Linux社区】Pinchart指出将git log中开发者邮箱自动订阅bugzilla通知在欧盟或涉违法，若真采纳该方向须先经法务审查，当前亦无此共识。 `<!-- ROW_MINE: ksummit.messages.6667 -->`
- 【Linux社区】Tashkinov力挺Bugzilla：公开可检索、汇聚注意力、不泄露邮箱；反驳Linus邮件通用语论，指gmx常被拦截、送达不可知、缺References易断链。 `<!-- ROW_MINE: ksummit.messages.6721 -->`
- 【Linux社区】Ryabitsev澄清Artem的真实主张是为MAINTAINERS中人自动建bugzilla账号、便于人工分诊时CC，而非设为默认受理人，也不会显著推高邮件量。 `<!-- ROW_MINE: ksummit.messages.6736 -->`
- 【Linux社区】Rapoport指出症结在缺分诊人力而非工具：bugzilla邮箱库不会比MAINTAINERS更利于选CC，强迫开发者接收报告也不会让他们更愿意处理。 `<!-- ROW_MINE: ksummit.messages.6773 -->`

## 179.7 静态分析提案

- 【Linux社区】NeilBrown剖析指针返回标注复杂性：归纳四类返回约定，另有低位复用自旋锁与fs_context字段随时序变化的隐含约束，主张默认不改、完全自愿加入的标注体系。 `<!-- ROW_MINE: ksummit.messages.6672 -->`
- 【Linux社区】Geert回忆gcc 4.2的未初始化警告每年能找出真实bug，忧心如今无人再开启；并提议为返回错误码或错误指针的函数加注解，辅助静态检查。 `<!-- ROW_MINE: ksummit.messages.6692 -->`

## 179.8 维护者治理规则

- 【Linux社区】Bottomley称bcachefs问题早有预警，反对“凭一时兴起”的激烈处置，主张为特性引入与维护者除名建立正式程序；Rostedt自述曾指导Bristot与Hiramatsu等成为维护者。 `<!-- ROW_MINE: ksummit.messages.6675 -->`

## 179.9 Link标签与消息溯源

- 【Linux社区】Brown赞同三步方案：暂维持patch.msgid.link自动Link:标签、推动git把来源信息写入提交头、留待峰会再议；并预期Debian stable到2027年才用上新版git。 `<!-- ROW_MINE: ksummit.messages.6682 -->`
- 【Linux社区】Brown指出GNOME等终端会把含@字符串识别为邮箱、点击即唤起GUI邮件客户端，而按建议需频繁剪切粘贴message-ID，误触概率远高于一般trailer。 `<!-- ROW_MINE: ksummit.messages.6709 -->`
- 【Linux社区】Carpenter认为lore线程显式链接对静态检查者有用——可回原帖并CC正确的人；若存在多个Link:标签，取最后一个指向线程即可接受。 `<!-- ROW_MINE: ksummit.messages.6787 -->`

## 179.10 Rust政策讨论

- 【Linux社区】Bottomley观察所关注子系统的bug修复多在错误分支（kfree遗漏或过早释放），建议借GCC _cleanup_注解（systemd经验）简化错误处理，回应Rust安全优势论。 `<!-- ROW_MINE: ksummit.messages.6683 -->`
- 【Linux社区】Ralf Jung澄清Rust内核panic不做unwind但通常仍打印backtrace，用户态运行良好、内核状态他不确定；回应Bottomley对缺诊断信息的担忧。 `<!-- ROW_MINE: ksummit.messages.6704 -->`

## 179.11 AI补丁文档规范

- 【Linux社区】Rostedt支持Stoakes的修订案：工具生成内容（不限AI，含checkpatch与coccinelle）一律按生成比例从严审查；自述长期如此，文档只是记录现状。 `<!-- ROW_MINE: ksummit.messages.6686 -->`
- 【Linux社区】Stoakes坚持文档须保留AI SLOP警示语气：确有“好心办坏事”且会认真读文档的人群，此前媒体失实报道也证明措辞不清有实际代价，反对稀释。 `<!-- ROW_MINE: ksummit.messages.6767 -->`

## 179.12 AI版权与DCO

- 【Linux社区】Mauro引美国版权局报告支持纯AI代码无版权、近乎公有领域，但提醒美国判例法可回溯适用且须顾及他国法域，并举巴西版权法中类似合理使用的解释。 `<!-- ROW_MINE: ksummit.messages.6701 -->`
- 【Linux社区】Mauro自述实验：AI产出如初学者代码、骨架需大量人工打磨，提示词与人工修改可主张版权；大训练集使权重重复多见模式，与检索写码无异。 `<!-- ROW_MINE: ksummit.messages.6765 -->`
- 【Linux社区】McKenney反驳Levin“AI审查没有法律问题”的说法，提醒去数一数当前在审的AI训练数据相关诉讼，暗示法律风险远未落定。 `<!-- ROW_MINE: ksummit.messages.6779 -->`

## 179.13 linux-next测试

- 【Linux社区】Brown评估linux-next做功能测试：多数时候可用但会偶发灾难性崩溃，小众平台可能长期缺覆盖，不愿进-next的子树亦是障碍；广跨多树的场景反而省力。 `<!-- ROW_MINE: ksummit.messages.6705 -->`

## 179.14 文件系统维护信任

- 【Linux社区】Overstreet称syzbot随机投递最伤效率，主张以覆盖率分析部分替代模糊测试、按文件集中补测试；长期出路是Rust重写；自述已从见bug就修转向让代码自己暴露问题。 `<!-- ROW_MINE: ksummit.messages.6714 -->`
- 【Linux社区】Hellwig支持全局文件系统白名单/黑名单但反对放util-linux维护：应在内核struct file_system_type加标志并经/proc/filesystems暴露，新挂载API配自动挂载标志。 `<!-- ROW_MINE: ksummit.messages.6791 -->`

## 179.15 2021峰会筹备

- 【Linux社区】Bottomley通报欧洲疫苗接种加速、德国年轻人已可接种，预计9月底好转，冀欧美互开旅行；西雅图场地酒店口罩与社交距离规定使微会议难协作。 `<!-- ROW_MINE: ksummit.messages.6718 -->`

## 179.16 MAINTAINERS清理

- 【Linux社区】Bulwahn提议以lore归档核查维护者近一年有无发言来替代探测邮件，再甄别收发地址不同、无补丁可收、地址已死等情形；自述维护模式自检已两三年。 `<!-- ROW_MINE: ksummit.messages.6723 -->`

## 179.17 回归跟踪regzbot

- 【Linux社区】Leemhuis公布维护者峰会与LPC两场回归跟踪演讲的幻灯链接、regzbot入门与参考文档，以及handling-regressions.rst渲染版，供会后跟进。 `<!-- ROW_MINE: ksummit.messages.6730 -->`

## 179.18 加速器用户态要求

- 【Linux社区】Airlie详述开源用户态要求：加速器uAPI多线程多用户，文档与kselftest远不够；社区靠说“不”与跨厂商教育建立；厂商多受大厂驱动而最低限度参与；正起草通用文档组建维护者联盟。 `<!-- ROW_MINE: ksummit.messages.6745 -->`

## 179.19 Werror编译争论

- 【Linux社区】Gallager支持IGNORE_WERROR环境变量设想：复杂构建系统中用户无从知晓-Werror从何插入，“改你的代码”对非开发者无意义，环境变量更可行。 `<!-- ROW_MINE: ksummit.messages.6750 -->`

## 179.20 MAINTAINERS分流

- 【Linux社区】Rostedt澄清：他用linux-trace-kernel@喂patchwork但希望讨论留在LKML，说明MAINTAINERS中L:条目需区分收补丁与讨论两种用途。 `<!-- ROW_MINE: ksummit.messages.6753 -->`

## 179.21 混合会议远程参与

- 【Linux社区】Shuah给出混合会议主持人清单：盯聊天与Q&A、举手管理、强制轮流发言、请讲者复述现场提问、探索实时转写并配纪要；拟先在一两个工作坊试点。 `<!-- ROW_MINE: ksummit.messages.6756 -->`

## 179.22 补丁发送脚本

- 【Linux社区】Mauro提交658行send-patches.pl：2015年起自用，调get_maintainer.pl自动生成CC，支持--avoid-resend跳过未变补丁、Tk编辑、清理Change-Id。 `<!-- ROW_MINE: ksummit.messages.6778 -->`

## 179.23 贡献者信任评分

- 【Linux社区】Mauro称核查过UMN事件投媒体子系统的补丁多可合并，主张议题应超trivial范畴：维护者内部信任评分互不共享，提议get_developer_trustee_status脚本输出贡献史与黑名单指标。 `<!-- ROW_MINE: ksummit.messages.6780 -->`

## 179.24 DRM面板API

- 【Linux社区】Ripard主张承认drm_bridge已覆盖面板场景、让面板成为bridge进而移除面板API；指出面板厂商点火即忘、无动力上游化；提议通用bridge驱动加eBPF钩子安置面板quirk。 `<!-- ROW_MINE: ksummit.messages.6782 -->`

## 179.25 PGP密钥过期争论

- 【Linux社区】Torvalds痛斥PGP密钥自动过期：无人按时续期、旧签名反显不可信（git log --show-signature查15年前即见expired），失效应撤销而非坐等过期，并称PGP是UX灾难。 `<!-- ROW_MINE: ksummit.messages.6784 -->`

## 179.26 Bugzilla替代方案

- 【Linux社区】Limonciello建议由LF建GitLab实例（如gitlab.kernel.org）按子系统设项目承接bugzilla议题，并为愿试PR/MR流程的子系统留门；Jani嫌GitLab免费版弱于Bugzilla、倾向Forgejo。 `<!-- ROW_MINE: ksummit.messages.6792 -->`
