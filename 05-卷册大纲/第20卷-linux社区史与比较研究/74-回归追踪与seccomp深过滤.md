# 74 【Linux社区】回归追踪与seccomp深过滤

> 来源：ksummit-discuss p126（50 封全读，2019-07 stable 回归追踪/seccomp USER_NOTIF/CIFSD，夹杂 2014-05 档案信）
> 判定：44 CAND / 6 NV。主题分布：SUSE回归追踪资助经验 1、集中追踪不依赖单人 1、单人回归追踪不可行 1、维护者自报回归+仪表盘 1、风险分级审查策略 1、反对新审查标签规则 1、ACPI命名GPIO缺失 1、个人Ack使用惯例 1、部分审查标签语法 1、裸Ack视为噪音 1、SoB附R-b记录流程 1、Acks可拒需共识 1、反对SoB区分责任 1、提交即担责原则 1、versatile DT转换进展 1、补丁超负荷信任矩阵 1、git am保存消息ID 1、Kees钩子实用证实 1、拉近期作者审阅 1、建议收录Kees脚本 1、新维护者信任重建 1、请求补全lore列表 1、公布脚本链接出处 1、seccomp指针过滤议题 1、replace辅助二分 1、系统调用自愿过滤 1、深度过滤需eBPF 1、Landlock扩展设想 1、拒绝依赖Landlock 1、RST转换进度规划 1、同意收录维护者脚本 1、CIFSD文件通知难题 1、LSM符号亦未导出 1、确认动态订阅需求 1、notes共享不易 1、PaStA映射工具存档 1、赞成导出fsnotify 1、nfsd补丁续推 1、LSM语义定义缺失 1、请Jan表态导出 1、撤回语气研究议题 1、TAB测试投票公告 1、nfsd组销毁用法存疑 1、有条件同意导出承诺 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p126 的逐封提取（44 CAND / 6 NV），全 44 块采用**单行摘要体例**（丙型）：每块由“## 74.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 74.1 【Linux社区】SUSE回归追踪资助经验

- 【Linux社区】Jiri Kosina披露SUSE曾长期资助回归追踪（Rafael时期），此岗需“真正深入理解内核”者，更初级的尝试“立即被压垮”，且资助公司同时损失开发脑力。 `<!-- ROW_MINE: ksummit-discuss.messages.350506 -->`

## 74.2 【Linux社区】集中追踪不依赖单人

- 【Linux社区】Laura Abbott主张回归追踪分两件事——中央追踪平台与管理人，中央平台应先建，“不依赖单一人员”更可靠。 `<!-- ROW_MINE: ksummit-discuss.messages.350507 -->`

## 74.3 【Linux社区】单人回归追踪不可行

- 【Linux社区】Rafael以亲历定性：如今单人无法追踪全内核回归，信息源太多，“LKML已成fire hose”，追踪须与开发流程同规模扩展。 `<!-- ROW_MINE: ksummit-discuss.messages.350508 -->`

## 74.4 【Linux社区】维护者自报回归+仪表盘

- 【Linux社区】Takashi Iwai提案：由各子系统维护者按标准方式向中央处上报回归，仪表盘聚合各报告链接，称“比自上而下的回归经理模式更可扩展可持续”。 `<!-- ROW_MINE: ksummit-discuss.messages.350509 -->`

## 74.5 【Linux社区】风险分级审查策略

- 【Linux社区】Jonathan Cameron披露维护者三级风险评估审查法（提交者信任史/他人Reviewed-by/副作用概率），问是否应反映进标签而非“藏在signed-off-by里”。 `<!-- ROW_MINE: ksummit-discuss.messages.350510 -->`

## 74.6 【Linux社区】反对新审查标签规则

- 【Linux社区】tglx反对另立新标签规则，称只会“制造客观可量化意义的幻觉”，用法仍靠个人解释，主张接受主观性、凭常识使用。 `<!-- ROW_MINE: ksummit-discuss.messages.350511 -->`

## 74.7 【Linux社区】ACPI命名GPIO缺失

- 【Linux社区】2014年ACPI/DT议题旧信：Rafael指出ACPI无机制把名字关联到GPIO引脚，acpi_find_gpio忽略con_id且“ATM别无他法”，赞rfkill-gpio.c为先例。 `<!-- ROW_MINE: ksummit-discuss.messages.350512 -->`

## 74.8 【Linux社区】个人Ack使用惯例

- 【Linux社区】Mauro自述惯例：跨树合并未全面审查时给Acked-by、全面审查给Reviewed-by，引Documentation/process/5.Posting.rst定义称现有描述已足够。 `<!-- ROW_MINE: ksummit-discuss.messages.350514 -->`

## 74.9 【Linux社区】部分审查标签语法

- 【Linux社区】Mauro提议部分审查/ack的注释语法“Acked-by: me <my@email> # driver_foo”，可被脚本解析并写入5.Posting.rst。 `<!-- ROW_MINE: ksummit-discuss.messages.350515 -->`

## 74.10 【Linux社区】裸Ack视为噪音

- 【Linux社区】Ted建议Acked-by定义改为“maintainer or reviewer”；披露因宣布忽略来源不明的裸Acked-by而被指责“未遵循文档流程”，称数十个外行Ack只是噪音。 `<!-- ROW_MINE: ksummit-discuss.messages.350516 -->`

## 74.11 【Linux社区】SoB附R-b记录流程

- 【Linux社区】Wolfram接受“新tag无用”论，但坚持真实全量审查时把Rev-by加进自己的SoB，以“完整记录补丁流程”。 `<!-- ROW_MINE: ksummit-discuss.messages.350518 -->`

## 74.12 【Linux社区】Acks可拒需共识

- 【Linux社区】Wolfram认为Ted新措辞“a tad too strict”但不愿纠缠愿让步，重申发起该线是为求共识，并提高“Acks与Revs可被拒绝”的意识。 `<!-- ROW_MINE: ksummit-discuss.messages.350519 -->`

## 74.13 【Linux社区】反对SoB区分责任

- 【Linux社区】Olof反对SoB附R-b：接补丁不看细节结局相同，唯一区别是“不是我的错”式开脱，“名字在上面就还是你的责任”，对项目无价值。 `<!-- ROW_MINE: ksummit-discuss.messages.350520 -->`

## 74.14 【Linux社区】提交即担责原则

- 【Linux社区】tglx裁定“提交即负责”：无论亲自审查还是依赖他人审查，责任无差别。 `<!-- ROW_MINE: ksummit-discuss.messages.350521 -->`

## 74.15 【Linux社区】versatile DT转换进展

- 【Linux社区】2014年旧信：Rob Herring列versatile全DT化三大阻塞——common clock、irq控制器DT初始化、PCI转DT/平台驱动，卡在通用DT PCI代码与个人时间。 `<!-- ROW_MINE: ksummit-discuss.messages.350523 -->`

## 74.16 【Linux社区】补丁超负荷信任矩阵

- 【Linux社区】Wolfram澄清：补丁量超个人负荷，靠“分而治之”发展单驱动维护者，“无意推卸责任”，只签确信可上游的补丁，愿换用其他追踪方式。 `<!-- ROW_MINE: ksummit-discuss.messages.350524 -->`

## 74.17 【Linux社区】git am保存消息ID

- 【Linux社区】Dan Carpenter建议给git am加自动保存Message-ID的选项，以缩短Takashi提议的Link引用。 `<!-- ROW_MINE: ksummit-discuss.messages.350525 -->`

## 74.18 【Linux社区】Kees钩子实用证实

- 【Linux社区】Greg KH证实Kees已发布git am钩子（自动加Message-ID），自己已用约一周“works wonderfully”。 `<!-- ROW_MINE: ksummit-discuss.messages.350527 -->`

## 74.19 【Linux社区】拉近期作者审阅

- 【Linux社区】Linus Walleij分享工作流：git log找近期改动人CC求审、凭直觉判断其在测试硬件、劝其登记MAINTAINERS；称get_maintainer难自动化需“real intelligence”。 `<!-- ROW_MINE: ksummit-discuss.messages.350528 -->`

## 74.20 【Linux社区】建议收录Kees脚本

- 【Linux社区】Linus Walleij确认Kees脚本“works like a charm”（限lore存档列表），请求收进Documentation/*。 `<!-- ROW_MINE: ksummit-discuss.messages.350529 -->`

## 74.21 【Linux社区】新维护者信任重建

- 【Linux社区】Wolfram补充也拉同公司作者审稿；已发展数名驱动维护者但“每个活跃新维护者都需考察其审稿方式”，故需“信任矩阵”追踪与审查摘要。 `<!-- ROW_MINE: ksummit-discuss.messages.350530 -->`

## 74.22 【Linux社区】请求补全lore列表

- 【Linux社区】Greg KH披露已提交开放请求把更多缺失邮件列表收入lore存档，期间已在用该链接。 `<!-- ROW_MINE: ksummit-discuss.messages.350531 -->`

## 74.23 【Linux社区】公布脚本链接出处

- 【Linux社区】Linus Walleij“应大众要求”公布Kees脚本原始帖链接（ksummit-discuss 2019-July/006608.html），存档指向。 `<!-- ROW_MINE: ksummit-discuss.messages.350532 -->`

## 74.24 【Linux社区】seccomp指针过滤议题

- 【Linux社区】Christian Brauner提KS议题：SECCOMP_RET_USER_NOTIF已实践拦截mknod/setxattr，clone3/openat2暴露指针参数过滤难题，主张seccomp不应拖累可扩展syscall设计，愿承担实现。 `<!-- ROW_MINE: ksummit-discuss.messages.350533 -->`

## 74.25 【Linux社区】replace辅助二分

- 【Linux社区】2014年旧信：Christian Couder详述git replace共享replace ref让二分自动用修复历史的流程，并建议git notes做纯增量元数据。 `<!-- ROW_MINE: ksummit-discuss.messages.350534 -->`

## 74.26 【Linux社区】系统调用自愿过滤

- 【Linux社区】Andy Lutomirski提议SYSCALL_FILTERABLE让syscall自愿加入深度过滤：拷入内核缓冲后调seccomp_deep_filter再转do_syscallname，建议自动生成桩。 `<!-- ROW_MINE: ksummit-discuss.messages.350535 -->`

## 74.27 【Linux社区】深度过滤需eBPF

- 【Linux社区】Kees Cook支持指针过滤，问“用cBPF能否可行还是终于需要eBPF”，指钩子位置似LSM并链接其seccomp/lsm旧设计。 `<!-- ROW_MINE: ksummit-discuss.messages.350536 -->`

## 74.28 【Linux社区】Landlock扩展设想

- 【Linux社区】James Morris提议考察把Landlock（同进程内seccomp+eBPF用户态访问控制）扩展为split watcher/watchee模型。 `<!-- ROW_MINE: ksummit-discuss.messages.350537 -->`

## 74.29 【Linux社区】拒绝依赖Landlock

- 【Linux社区】Brauner拒绝依赖Landlock三理由：“没人知道它何时落地”、seccomp已是用户态沙箱主流、系统调用拦截“是seccomp的地盘”，要求原生特性而非捆绑完整LSM。 `<!-- ROW_MINE: ksummit-discuss.messages.350538 -->`

## 74.30 【Linux社区】RST转换进度规划

- 【Linux社区】Mauro给出RST转换数据：约300文件待转换、约40个Documentation/*.txt待迁移改名，展示目标目录树，主张参照LDD3重构driver-api书并设想GPLv2旧书导入。 `<!-- ROW_MINE: ksummit-discuss.messages.350539 -->`

## 74.31 【Linux社区】同意收录维护者脚本

- 【Linux社区】Kees Cook同意脚本收入文档，问维护者脚本应放哪，并提及Dan Williams与maintainer's handbook。 `<!-- ROW_MINE: ksummit-discuss.messages.350540 -->`

## 74.32 【Linux社区】CIFSD文件通知难题

- 【Linux社区】Senozhatsky扩展CIFSD议题：SMB2 CHANGE_NOTIFY需fsnotify类机制但内核模块不可用，NFS曾有同样困境（Jeff Layton旧补丁），问能否导出fsnotify符号。 `<!-- ROW_MINE: ksummit-discuss.messages.350542 -->`

## 74.33 【Linux社区】LSM符号亦未导出

- 【Linux社区】Senozhatsky补充曾考察LSM hooks（creat/open/truncate/chmod/chown/unlink回调），但LSM非为此设且“LSM符号也未导出”。 `<!-- ROW_MINE: ksummit-discuss.messages.350543 -->`

## 74.34 【Linux社区】确认动态订阅需求

- 【Linux社区】Senozhatsky逐条确认Amir所列fsnotify相对裸LSM的优势为CIFSD刚需：动态订阅/退订、每SMB会话一个组的多数订户实例。 `<!-- ROW_MINE: ksummit-discuss.messages.350544 -->`

## 74.35 【Linux社区】notes共享不易

- 【Linux社区】2014年旧信：Takashi Iwai称git notes分享“不及tags便利”、独立refs需额外非标准步骤是障碍，疑git replace方案难适配多维护者合并树。 `<!-- ROW_MINE: ksummit-discuss.messages.350545 -->`

## 74.36 【Linux社区】PaStA映射工具存档

- 【Linux社区】Ralf Ramsauer介绍PaStA以高准确率把Message-ID映射到commit hash（曾量化RT项目上游率），自维护约190个列表的public inbox格式存档，望迁至LF托管。 `<!-- ROW_MINE: ksummit-discuss.messages.350546 -->`

## 74.37 【Linux社区】赞成导出fsnotify

- 【Linux社区】Amir Goldstein不反对导出fsnotify符号，称计划overlayfs也用，并指Jeff发补丁时“无活跃fsnotify维护者”。 `<!-- ROW_MINE: ksummit-discuss.messages.350547 -->`

## 74.38 【Linux社区】nfsd补丁续推

- 【Linux社区】Jeff Layton指出Trond Myklebust正推动nfsd修订补丁集、仍用fsnotify检测unlink活动（spinics链接），并cc Trond确认。 `<!-- ROW_MINE: ksummit-discuss.messages.350548 -->`

## 74.39 【Linux社区】LSM语义定义缺失

- 【Linux社区】Al Viro定性：LSM hooks“没有明确定义的语义”，覆盖面也“说得客气点……欠佳”。 `<!-- ROW_MINE: ksummit-discuss.messages.350549 -->`

## 74.40 【Linux社区】请Jan表态导出

- 【Linux社区】Senozhatsky直接请Jan Kara表态，希望fsnotify导出补丁尽早进linux-next。 `<!-- ROW_MINE: ksummit-discuss.messages.350550 -->`

## 74.41 【Linux社区】撤回语气研究议题

- 【Linux社区】Shuah Khan正式撤回Sentimine议题提案：清晰度方向研究“未产出有价值结果”、只看语气“一维且无用”，不愿再耗Maintainer/Kernel峰会时间。 `<!-- ROW_MINE: ksummit-discuss.messages.350552 -->`

## 74.42 【Linux社区】TAB测试投票公告

- 【Linux社区】Laura Abbott公告TAB测试投票：演练新投票程序、为Greg选LPC 2019 T恤（五个标语选项），8月18日报名、8月19-23日投票，任何人可参与。 `<!-- ROW_MINE: ksummit-discuss.messages.350553 -->`

## 74.43 【Linux社区】nfsd组销毁用法存疑

- 【Linux社区】Jan Kara审读nfsd文件缓存补丁：fsnotify_put_group/fsnotify_wait_marks_destroyed用法疑有bug，应先调fsnotify_destroy_group而非仅drop引用。 `<!-- ROW_MINE: ksummit-discuss.messages.350554 -->`

## 74.44 【Linux社区】有条件同意导出承诺

- 【Linux社区】Jan Kara同意导出fsnotify给模块（先例kernel/audit_tree.c亦为模块外用户），承诺系列接近可收录即推导出补丁入己树，但拒为短期不上游的树外代码导出符号。 `<!-- ROW_MINE: ksummit-discuss.messages.350555 -->`
