# 82 【Linux社区】seccomp细节定调与Documentation大讨论

> 来源：ksummit-discuss p134（50 封全读，2020-05/06 seccomp 深水+KS2020 虚拟启动+Documentation 大讨论，夹杂 2014-05 档案信）
> 判定：50 CAND / 0 NV。主题分布：Bird参选史 1、Rostedt2019先例 1、KS2020虚拟启动 1、seccomp四议题 1、KS2014档案-FB 1、ViroABI怒斥 1、Kees回击 1、Viro禁新增 1、Linus细节定调 1、Kees限深提议 1、Linus认可限深 1、Brauner不透明 1、文档化请求 1、补丁在途 1、AlexeicBPF Nack 1、KS2014档案-tinification 1、KS2014档案-livepatch 1、Williams回Rafael 1、Kees位掩码辩护 1、Alexei再战 1、Sarai二阶保留 1、Brauner驳strawman 1、Brauner更多例 1、DAMON议题 1、ExtSyscalls议题 1、CorbetDoc议题 1、Carpenter检索痛点 1、Vetterkerneldoc化 1、KS2014档案-CONFIG 1、Walleij全球TODO 1、Shuah新人调研 1、Perches反问 1、Shuah澄清 1、Pinchart优先级论 1、Rapoport学而写 1、Rapoport新旧之辨 1、Brown英语门槛 1、Shuah价值论 1、Shuah新眼论 1、KS2014档案-dynamicdebug 1、JuliaCoccinelle 1、Perches已有 1、Julia承认 1、Pinchart高门槛 1、Wilcox700警告 1、Rapoport训练效应 1、Jani-none 1、Ted提交提醒 1、Rapoportcheckpatch 1、Rapoport旧指南 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p134（实锚 pk 350906-350955）的逐封提取（50 CAND / 0 NV），全 50 块采用**单行摘要体例**（丙型）：每块由“## 82.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 82.1 【Linux社区】Bird参选史

- 【Linux社区】Bird：“我 2017 布拉格当选——在场但有冲突没到场投票；ELC 同址那年大概帮了我大忙；乐见缺席投票以降低活动配对影响；提名惯例邮件已含无需到场” `<!-- ROW_MINE: ksummit-discuss.messages.350906 -->`

## 82.2 【Linux社区】Rostedt2019先例

- 【Linux社区】Rostedt：“去年我也在场但忙 Plumbers 错过选举会也当选——去年首次电子投票只需到场会议；去年还取消了演讲改书面陈述” `<!-- ROW_MINE: ksummit-discuss.messages.350907 -->`

## 82.3 【Linux社区】KS2020虚拟启动

- 【Linux社区】Ted 公告 KS/MS 2020 因 COVID 不在 Halifax、改虚拟格式（8 月末）；MS 仍邀请制 30 人、Linus 核心名单前 10+程序委员会补位；[TECH TOPIC]+LPC 站点双提交、6/15 前中题免费；半数 unconference；程序委员会五人（Greg/Axboe/Corbet/Tso/Gleixner） `<!-- ROW_MINE: ksummit-discuss.messages.350908 -->`

## 82.4 【Linux社区】seccomp四议题

- 【Linux社区】Kees [TECH TOPIC]：fd passing/深参检查/结构尺寸/syscall 位掩码；可扩展参数 syscall 需无 TOCTOU 无双拷贝检查用户内存；嵌套结构需展平进 BPF 线性缓冲；USER_NOTIF 也要处理 `<!-- ROW_MINE: ksummit-discuss.messages.350909 -->`

## 82.5 【Linux社区】KS2014档案-FB

- 【Linux社区】Rafael（2014-05-21）：“FB 模型只在所有参与者是同一家公司员工时可行——内核开发不是；我们从互联网几乎所有人收补丁、Facebook 也是吗？我不认为” `<!-- ROW_MINE: ksummit-discuss.messages.350910 -->`

## 82.6 【Linux社区】ViroABI怒斥

- 【Linux社区】Viro：“……抓住并干掉那些试图这么搞的垃圾 ABI ‘增强’。我不确定这为什么与 seccomp 相关” `<!-- ROW_MINE: ksummit-discuss.messages.350911 -->`

## 82.7 【Linux社区】Kees回击

- 【Linux社区】Kees：“已有 syscall 传含指针到更多结构的结构——你是说那些该被禁止？（个人很乐意但不符合那些 syscall 的设计现实）” `<!-- ROW_MINE: ksummit-discuss.messages.350912 -->`

## 82.8 【Linux社区】Viro禁新增

- 【Linux社区】Viro：“现有杀不掉但可以不再接受新的；iovec 数组作参数可豁免（数据不透明）；pselect6 类 kludge 令人作呕但或不可避免——须作者给出极好解释，‘我想要 18 个参数’不是” `<!-- ROW_MINE: ksummit-discuss.messages.350913 -->`

## 82.9 【Linux社区】Linus细节定调

- 【Linux社区】Linus：“举出安全上真正相关的真实例子；clone3/ioctl/iovec 都存在但没一个 seccomp 该关心；沙箱要么完全禁用要么逐案论证；更 fancy 就在 ptracer 里完全模拟避免竞态；‘有些计算机科学家认为一切该泛型化——那些人错了。真正重要的是细节。所以，细节请。’” `<!-- ROW_MINE: ksummit-discuss.messages.350914 -->`

## 82.10 【Linux社区】Kees限深提议

- 【Linux社区】Kees：“不打算抽象化（只针对 clone3 与 openat2）；也一直抵制把 seccomp BPF 扩成 eBPF”；clone_args.set_tid 是动态数组指针例；“或许问题是 seccomp 要看多深——只看顶层结构、其中指针全不透明？大大简化设计” `<!-- ROW_MINE: ksummit-discuss.messages.350915 -->`

## 82.11 【Linux社区】Linus认可限深

- 【Linux社区】Linus：“Exactly。绝大多数情况如此。谁真的需要深层、为什么？” `<!-- ROW_MINE: ksummit-discuss.messages.350916 -->`

## 82.12 【Linux社区】Brauner不透明

- 【Linux社区】Brauner：“我们大多不需要、二阶指针全不透明 imho 可接受；不需要嵌套结构（有 netlink）；二阶特征可放一阶 flag 下、flag 可过滤即可；clone3 的 set_tid 非零 size 即可拒绝；需要成文共识——我会提交” `<!-- ROW_MINE: ksummit-discuss.messages.350917 -->`

## 82.13 【Linux社区】文档化请求

- 【Linux社区】Kees 问 Sarai：“有文字版设计文档吗？最好更新 Documentation/process/adding-syscalls.rst 并加入 no nested flags 要求” `<!-- ROW_MINE: ksummit-discuss.messages.350918 -->`

## 82.14 【Linux社区】补丁在途

- 【Linux社区】Brauner：“去年已发 adding-syscalls 补丁草拟扩展 syscall 规范、本周重发；会加：寄存器 flag 参数一律 unsigned int、no nested flags；Aleksa 与我原计划 Plumbers/KS 联合场次” `<!-- ROW_MINE: ksummit-discuss.messages.350919 -->`

## 82.15 【Linux社区】AlexeicBPF Nack

- 【Linux社区】Alexei：“**Nack to cBPF extensions**：给 cBPF 大数组=seccomp_data 变长或巨页——变长则受 Spectre v1 之害；eBPF 验证器已能识别推测模式；巨页需清零更慢；seccomp‘现在就慢且生产数据中心不可用’；syscall bitmask=又造轮子” `<!-- ROW_MINE: ksummit-discuss.messages.350920 -->`

## 82.16 【Linux社区】KS2014档案-tinification

- 【Linux社区】Roeck（2014-05-02）：支持 CONFIG_SECURE_ROUTER/CONFIG_REDUCED_ATTACK_SURFACE——“公司路由器甚至家里服务器都想开” `<!-- ROW_MINE: ksummit-discuss.messages.350921 -->`

## 82.17 【Linux社区】KS2014档案-livepatch

- 【Linux社区】Li Zefan（华为，2014-05-04）：“感谢做 KGraft！华为想用 live patching 但保守——真的想看到 mainline 方案”（kpatch/kgraft/criu/ksplice 并行时代） `<!-- ROW_MINE: ksummit-discuss.messages.350922 -->`

## 82.18 【Linux社区】Williams回Rafael

- 【Linux社区】Williams：“难以看出这如何回应 libsas 例子；终端用户会覆盖 gatekeeper 测试仍在辩论的功能——我提议把鼓励树内实验机制化；我关心的是扩展维护者降险选项” `<!-- ROW_MINE: ksummit-discuss.messages.350923 -->`

## 82.19 【Linux社区】Kees位掩码辩护

- 【Linux社区】Kees：“同意 cBPF Nack；不打算变长——若设计迫使扩展过滤语言就转 eBPF”；“‘生产数据中心不可用’是以你意见作普遍断言”；“syscall 位掩码比单指令 BPF 快一个数量级——绝大多数过滤器只要 yes/no”；“seccomp 安全史远好于 eBPF 因坚持极小极简——不想放弃” `<!-- ROW_MINE: ksummit-discuss.messages.350924 -->`

## 82.20 【Linux社区】Alexei再战

- 【Linux社区】Alexei：“绕开内核存储与网络栈的数据中心当然 seccomp 开销无关——就像 kpti 与 retpoline；JITed eBPF 与内核 C 同速——说 C 位掩码快过 C 的 return 0？荒谬。eBPF 每秒千万包以纳秒计”；“seccomp‘主观上更安全’——低 bug 率因 syzbot 不看它；2020 年三个验证器 bug 全由新 kBdysch fuzzer 发现；担心 JIT bug 就别用 cBPF” `<!-- ROW_MINE: ksummit-discuss.messages.350925 -->`

## 82.21 【Linux社区】Sarai二阶保留

- 【Linux社区】Sarai：“坚持二阶指针话题是为确保首版模型可扩展到二阶——跳表提案只是例子；二阶全不透明则 clone3 的 set_tid 不可过滤——少数‘显然’syscall 之一将不完整可过滤；首版如此我也接受”；adding-syscalls 补丁去年与 Brauner 写过、Jon 觉得需更大共识 `<!-- ROW_MINE: ksummit-discuss.messages.350926 -->`

## 82.22 【Linux社区】Brauner驳strawman

- 【Linux社区】Brauner：“那不是有趣的二阶案例——开或关基于 set_tid_size 即可；要么允许足够能力者选 pid 要么拒绝——不是好稻草人；有趣的二阶指针=按不透明开关指向不同东西——看 bpf()：BPF_OBJ_GET_INFO_BY_FD 的 info 按 fd 类型是 prog/map/btf 之一、还有三阶指针” `<!-- ROW_MINE: ksummit-discuss.messages.350927 -->`

## 82.23 【Linux社区】Brauner更多例

- 【Linux社区】Brauner：“其他例子：epoll_ctl 的 epoll_event、struct iovec、{get,set}_robust_list、kexec_load 的 kexec_segment、sendmsg/recvmsg 的 msghdr 带大量子结构——多数无趣、有问题就不许” `<!-- ROW_MINE: ksummit-discuss.messages.350928 -->`

## 82.24 【Linux社区】DAMON议题

- 【Linux社区】SeongJae Park [TECH TOPIC] DAMON 全文：四要求（准确/轻量/可扩展/通用）、region-based sampling+adaptive regions、DAMOS 操作方案、25 工作负载实测（内存 -0.39%、CPU<1%、减速 0.63%；THP 方案去 69.43% 开销保 37.11% 加速；回收减 89.30% 驻留集）；三篇论文+LWN 812707 `<!-- ROW_MINE: ksummit-discuss.messages.350929 -->`

## 82.25 【Linux社区】ExtSyscalls议题

- 【Linux社区】Brauner+Sarai [TECH TOPIC]：扩展 syscall 惯例——尺寸版本化结构（openat2/sched_attr/clone3）、嵌套指针是否允许（特别是 seccomp 可过滤性）、寄存器 flag 一律 unsigned int、修订版命名、统一特性测试方法 `<!-- ROW_MINE: ksummit-discuss.messages.350930 -->`

## 82.26 【Linux社区】CorbetDoc议题

- 【Linux社区】Corbet：“RST 转换终于接近尾声……买到什么？从混乱破烂堆到略好组织的破烂堆+基建；下一步是什么？资源从哪来？构建基建改进什么有用？我带些想法但更想听” `<!-- ROW_MINE: ksummit-discuss.messages.350931 -->`

## 82.27 【Linux社区】Carpenter检索痛点

- 【Linux社区】Carpenter：“我只读函数实现前的文档+LDD；pm_request_resume 在 runtime_pm.rst 文档化——自动找到就好了；愿有 cscope 替代品按序出结果（全局实现/文档/本地实现）——struct device 是我第 995 个结果、cscope 很糟但那是我的默认搜索” `<!-- ROW_MINE: ksummit-discuss.messages.350932 -->`

## 82.28 【Linux社区】Vetterkerneldoc化

- 【Linux社区】Vetter：“建议把这些移进代码作 kerneldoc、再用 include 指令拉进 .rst；Documentation/gpu/*.rst 大块只是从源文件拉注释的脚手架——.rst 里只有大图概览、连局部概览都做成源码 DOC: kerneldoc 注释” `<!-- ROW_MINE: ksummit-discuss.messages.350933 -->`

## 82.29 【Linux社区】KS2014档案-CONFIG

- 【Linux社区】Pinchart（2014-05-21）：“那不就是 CONFIG_EXPERIMENTAL 的用途？类似机制会以同样方式被滥用、最终被发行版默认开启（LWN 520867）；内核带安全含义——树内机制要考虑约束；未妥评审的实验特性可能让构建机器人在禁用时就失败——须评审实验补丁防之、反给维护者加担子” `<!-- ROW_MINE: ksummit-discuss.messages.350934 -->`

## 82.30 【Linux社区】Walleij全球TODO

- 【Linux社区】Walleij：“基础内核数据结构入门材料散落全球（Gorman/skb_data）且常略过时；技术写手会受益于全球 TODO（‘文档化基础 arch 接口’‘skb 是什么’）；现在是读代码+‘大家都懂’+网上随机来源的混合——对新人无益；附议紧绑代码——可归于 Knuth 1984 文学编程” `<!-- ROW_MINE: ksummit-discuss.messages.350935 -->`

## 82.31 【Linux社区】Shuah新人调研

- 【Linux社区】Shuah：“完全同意需要坚实 TODO 清单；新人本就怯于提问、常归结为带宽；过去 6 个版本（自 5.1）我问新贡献者‘对改进新人材料有什么建议’——反馈总是要更新的内核文档与在线资源；有兴趣可分享详细反馈” `<!-- ROW_MINE: ksummit-discuss.messages.350936 -->`

## 82.32 【Linux社区】Perches反问

- 【Linux社区】Perches：“所以你指望不甚了解子系统的人产出优秀有用的文档？” `<!-- ROW_MINE: ksummit-discuss.messages.350937 -->`

## 82.33 【Linux社区】Shuah澄清

- 【Linux社区】Shuah：“我没那个意思。只是说带宽缺乏是文档过时的原因之一。解决方案上盼一两个可行选项在讨论与峰会上冒出来” `<!-- ROW_MINE: ksummit-discuss.messages.350938 -->`

## 82.34 【Linux社区】Pinchart优先级论

- 【Linux社区】Pinchart：“更多是优先级问题而非带宽；大子系统有政策让人写文档——V4L2 用户态 API、DRM 内核 API——其他子系统若维护者视缺文档为提交阻碍也能跟上；英语不流利者更难受——需单独解决；文档质量门槛——作者从读者视角写的情形不多；内核会受益于更多技术写手参与评审——预算问题” `<!-- ROW_MINE: ksummit-discuss.messages.350939 -->`

## 82.35 【Linux社区】Rapoport学而写

- 【Linux社区】Rapoport：“写文档是学习的方式；产出好文档不必深通所有细节——写手须抓住大图并能解释它” `<!-- ROW_MINE: ksummit-discuss.messages.350940 -->`

## 82.36 【Linux社区】Rapoport新旧之辨

- 【Linux社区】Rapoport：“附议优先级——写代码通常更有回报 :)；应区分新增与更新——随代码变更小幅修订既有文档使 doc 与 code 同步并不难——要求文档更新作为变更一部分不算过分” `<!-- ROW_MINE: ksummit-discuss.messages.350941 -->`

## 82.37 【Linux社区】Brown英语门槛

- 【Linux社区】Brown：“不要低估这给英语不流利开发者设置的障碍——翻翻 changelog 吧；从能写可理解的代码到能写清晰有用的文档之间有很大一跳” `<!-- ROW_MINE: ksummit-discuss.messages.350942 -->`

## 82.38 【Linux社区】Shuah价值论

- 【Linux社区】Shuah：“优先级可能是更大原因——文档对工程师不有趣也不光鲜；media 子系统可作榜样（维护者强调并以之为优先）；文档不受代码同级重视——若集体认同就能做到；也许把‘Code talks…’改成‘Code with good documentation walks…’；文档含 commit logs/声明顶部 doc 区/API 文档” `<!-- ROW_MINE: ksummit-discuss.messages.350943 -->`

## 82.39 【Linux社区】Shuah新眼论

- 【Linux社区】Shuah：“+1 写文档是学习方式；反‘新人不能文档化’——他们可以、文档可由专家评审；新眼睛带来新视角；导师计划加文档任务有些成功；可创建文档 TODO 清单并评审、本就是开发流程一部分” `<!-- ROW_MINE: ksummit-discuss.messages.350944 -->`

## 82.40 【Linux社区】KS2014档案-dynamicdebug

- 【Linux社区】NeilBrown（2014-05-21）：“驱动特性这法可行——CONFIG 选项做增量发布笨拙；运行时启用有吸引力；控制接口可像 dynamic_debug——一个文件列出所有选项、写入消息启用；值得试试看接受度” `<!-- ROW_MINE: ksummit-discuss.messages.350945 -->`

## 82.41 【Linux社区】JuliaCoccinelle

- 【Linux社区】Julia：“用 Coccinelle 收集缺失或格式错误的函数文档——fman.c 示例输出（extra names/missing name/return comment but no return value…）；假定所有 EXPORT_SYMBOL 都该有文档——似乎很多没有” `<!-- ROW_MINE: ksummit-discuss.messages.350946 -->`

## 82.42 【Linux社区】Perches已有

- 【Linux社区】Perches：“just fyi：scripts/kernel-doc 已经做了——同样输出示例” `<!-- ROW_MINE: ksummit-discuss.messages.350947 -->`

## 82.43 【Linux社区】Julia承认

- 【Linux社区】Julia：“OK 差不多一样。我在一些例子上能提些建议但不多” `<!-- ROW_MINE: ksummit-discuss.messages.350948 -->`

## 82.44 【Linux社区】Pinchart高门槛

- 【Linux社区】Pinchart：“只部分同意‘写文档是学习’——我开始 DRM 文档工作是因为要写驱动而没文档；门槛真的高、比写新驱动难；需要极高动机与大量时间；新眼睛能指出不一致、但文档写作一般不是好的学习曲线任务”；问导师计划文档任务是提议/进行/已完成 `<!-- ROW_MINE: ksummit-discuss.messages.350949 -->`

## 82.45 【Linux社区】Wilcox700警告

- 【Linux社区】Wilcox：“W=1 会开文档警告——想让人认真对待文档可移到默认；上次试加了约 700 条警告、我没那把勺子去修；也许那才是好的新手任务——不需要任何特定子系统的深度知识” `<!-- ROW_MINE: ksummit-discuss.messages.350950 -->`

## 82.46 【Linux社区】Rapoport训练效应

- 【Linux社区】Rapoport：“没错但除非更注意让 API 变更补丁带上 kerneldoc 变更、否则会这样训练出许多新手 ;-)” `<!-- ROW_MINE: ksummit-discuss.messages.350951 -->`

## 82.47 【Linux社区】Jani-none

- 【Linux社区】Jani：“kernel-doc 有 -none 选项：不输出任何文档只出警告——比重定向 stdout 到 /dev/null 略高效” `<!-- ROW_MINE: ksummit-discuss.messages.350952 -->`

## 82.48 【Linux社区】Ted提交提醒

- 【Linux社区】Ted：“KS 收到 5 份技术议题；MS 至今零提交——不清楚是疫情分心还是流程顺利还是不愿虚拟讨论；若提交不足须考虑今年是否办 MS” `<!-- ROW_MINE: ksummit-discuss.messages.350953 -->`

## 82.49 【Linux社区】Rapoportcheckpatch

- 【Linux社区】Rapoport：“这能否由 checkpatch.pl 报告？若补丁破坏代码与 kerneldoc 同步能否检出？” `<!-- ROW_MINE: ksummit-discuss.messages.350954 -->`

## 82.50 【Linux社区】Rapoport旧指南

- 【Linux社区】Rapoport：“好但旧的指南怎么办？user_mode_linux.rst 讲 gdb 调试但代码引用大多过时；‘不可靠指南’写得很棒但太过时” `<!-- ROW_MINE: ksummit-discuss.messages.350955 -->`
