# 162 【Linux社区】文件系统维护门槛与stable标签

> 来源：ksummit 独有 p26（50 封全读，2021-04 至 2026-08：Chinner 提出无主文件系统最低维护门槛政策并给出 XFS v4 弃用至 2030 移除完整 EOL 时间线含 reiserfs 先例、lklfuse 沙箱特权分离方案并正面抨击 Linus Waah 嘲讽；Levin stable 标签政策量化逾 80% Fixes 提交进入 stable 与 -rc 中 85% 修旧问题；Weinberger Bugzilla 退役后报告导引工程设计含模块名栈回溯符号自动映射与 sqlite 库；stable 标签政策三封、Bugzilla 存废之争三封、AI 补丁法律风险、C 聚合传递 ABI）
> 判定：41 CAND / 9 NV。主题分布：设备直传与ISP接口 1、Rust争议与社区担忧 1、linux-next树组织实验 1、栈回溯内嵌源码行号 1、加速器驱动用户态门槛 2、静态分析指针注解 1、文件系统维护信任 3、C聚合传递ABI 2、Cc范围与lore过滤 1、峰会远程参与模式 1、Link标签工具链 1、AI补丁提示词留存 1、Bugzilla退役与报告导引 1、隐藏提交与重复哈希 1、malloc分配器API 1、社区行为准则争论 1、stable标签政策 3、Bugzilla存废之争 3、AI补丁法律风险 2、LLM信任与身份认证 1、HIGHMEM淘汰争议 2、AI依赖性争论 1、明尼苏达事件后补丁审查 1、pkeys ABI规范化 1、Rust内核对象生命周期 2、回归修复时限表述 1、安全修复影响面之争 1、Rust文档互链方案 1、LKML减负方案 1、stable邮件过载 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p26 的逐封提取（2021-04 至 2026-08，41 CAND / 9 NV），全 30 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 162.1 设备直传与ISP接口

- 【Linux社区】Figa指V4L2有状态解码器接口可保内核API通用，问DRM为何编解码用命令提交而显示用固定KMS；警告固定功能API隐藏命令缓冲会阻碍ISP用例优化。 `<!-- ROW_MINE: ksummit.messages.4018 -->`

## 162.2 Rust争议与社区担忧

- 【Linux社区】Walleij自述对Miguel与Wedson的Rust补丁初曾质疑“你能胜过50年的C”，细看后转而认可其价值；要求Rust维护者如Torvalds在Transmeta时期那样承担超越本职的长期投入，并引Kasan为侵入性技术可快速接纳的先例。 `<!-- ROW_MINE: ksummit.messages.4027 -->`

## 162.3 linux-next树组织实验

- 【Linux社区】Levin展示按类别标签脚本生成主题化*-next分支的实验仓库，称初衷是评估AI合并冲突解决并与-next团队及Linus的人工成果对比，纯AI解决结果或可供CI与机器人使用。 `<!-- ROW_MINE: ksummit.messages.4031 -->`

## 162.4 栈回溯内嵌源码行号

- 【Linux社区】引kallsyms行号方案实测：459万条目约44MiB，vmlinux自529MiB增至573MiB（增8.3%）；Babka否决做成可加载模块的提议，称罕见崩溃“要么常开、要么错失唯一机会”。 `<!-- ROW_MINE: ksummit.messages.4032 -->`

## 162.5 加速器驱动用户态门槛

- 【Linux社区】Chehab赞同新内核接口须附完整文档与自测套件（含冒烟测试），但指出新品硬件仅厂商持有，冒烟测试对审阅者意义有限，除非厂商向审阅者提供硬件。 `<!-- ROW_MINE: ksummit.messages.4033 -->`
- 【Linux社区】Pinchart回应Leon的激进主张（API须被Debian、Fedora、SUSE包使用），建议补入Android AOSP，指Linux涵盖仅存于单一数据中心的设备等长尾市场，且GitHub项目作API使用证据最不可靠。 `<!-- ROW_MINE: ksummit.messages.4206 -->`

## 162.6 静态分析指针注解

- 【Linux社区】与Arnd讨论指针返回值注解分类：合法指针、NULL、错误指针的组合共五类；Geert补充devm_clk_get_optional()属第五类，取决于DTB而非编译期，系可选硬件功能所致。 `<!-- ROW_MINE: ksummit.messages.4036 -->`

## 162.7 文件系统维护信任

- 【Linux社区】Hellwig支持像移除ia64那样淘汰无人维护的旧文件系统，但表态不欲顶着强烈反对硬移，只要有一名用户承诺做基本QA即可保留，并称net子系统移除策略更激进。 `<!-- ROW_MINE: ksummit.messages.4039 -->`
- 【Linux社区】Chinner提出无主文件系统至少须有可用mkfs、fsck并纳入fstests，以fstype标志标注维护与弃用状态；详述XFS v4在2020弃用、2025默认关闭、2030全面移除的时间线及reiserfs先例。 `<!-- ROW_MINE: ksummit.messages.4049 -->`
- 【Linux社区】Chinner反驳“移用户态库”是安全表演，提出lklfuse在用户态沙箱运行内核文件系统解析实现特权分离，称信任模型完善后旧文件系统更可保留；并斥Linus“Waah”式嘲讽不可接受、领导层沉默更糟。 `<!-- ROW_MINE: ksummit.messages.4081 -->`

## 162.8 C聚合传递ABI

- 【Linux社区】comex用GCC与Clang在Compiler Explorer实测：32位x86、ARM、MIPS、SPARC及32与64位POWER（power64le除外）默认将双寄存器结构经栈返回；32位x86靠-freg-struct-return规避，他架构无对应选项。 `<!-- ROW_MINE: ksummit.messages.4040 -->`
- 【Linux社区】Torvalds称内核确实按值传结构且生成更优代码，但仅限能装入两寄存器的结构，页表项为数十年的典型用例；并指C无法如Python那样多返回值解构，仅适合语义上“一件事”的类型。 `<!-- ROW_MINE: ksummit.messages.4169 -->`

## 162.9 Cc范围与lore过滤

- 【Linux社区】Herring称依赖提交者自觉抄送永不可靠，常遇DT补丁不抄DT列表；主张降低发送目标的重要性，转向lore更易用的过滤，并称该功能即将到来。 `<!-- ROW_MINE: ksummit.messages.4044 -->`

## 162.10 峰会远程参与模式

- 【Linux社区】Wilcox提议禁止听众直接提问，改由主持人从官方聊天平台遴选问题转呈讲者，称可改善秩序并让散场后的好问题惠及全体，回应该届峰会远程参与安排。 `<!-- ROW_MINE: ksummit.messages.4050 -->`

## 162.11 Link标签工具链

- 【Linux社区】Tsirkin建议文档补充git am自动生成patch.msgid.link链接的配置，并给出applypatch-msg钩子的perl替换片段，将Message-Id转为Link尾注。 `<!-- ROW_MINE: ksummit.messages.4054 -->`

## 162.12 AI补丁提示词留存

- 【Linux社区】Luck指出AI与sed或coccinelle脚本本质不同：同一提示词得不到确定性输出，留存提示词有用但效用低于传统脚本，回应Linus要求披露工具与提示的提议。 `<!-- ROW_MINE: ksummit.messages.4059 -->`

## 162.13 Bugzilla退役与报告导引

- 【Linux社区】Weinberger设计四类输入（子系统、源文件、模块名、内核报错）到邮件列表的查询方案：用DWARF5全模块构建建立模块到源文件映射，用nm建符号映射，sqlite库可由构建自动生成。 `<!-- ROW_MINE: ksummit.messages.4075 -->`

## 162.14 隐藏提交与重复哈希

- 【Linux社区】Carpenter指DRM在分支间cherry-pick产生重复提交哈希，致Fixes标签指向对象无法解析，反向回溯某提交的后续修复搜索同样被扰乱。 `<!-- ROW_MINE: ksummit.messages.4084 -->`

## 162.15 malloc分配器API

- 【Linux社区】Pinchart称大量开发者以有害方式滥用devm_*分配器，并转述Kees拟将对象分配API扩展至devm_*，延续kzalloc_obj语义信息讨论。 `<!-- ROW_MINE: ksummit.messages.4093 -->`

## 162.16 社区行为准则争论

- 【Linux社区】Bottomley以Chinner回其提议的粗口拒绝为例，主张其与Linus嘲讽同等致压，称对己与对人的标准必须一致；Chinner坚称议题是机器人与第三方基础设施伤害社区时的伦理对策而非AI。 `<!-- ROW_MINE: ksummit.messages.4095 -->`

## 162.17 stable标签政策

- 【Linux社区】Carpenter让步认可Fixes应针对bug而非仅回归，称审过千余拼写修复无人要求加Fixes，多数维护者认为无害的静态检查修复不够格，Fixes多指向“新增某功能”提交。 `<!-- ROW_MINE: ksummit.messages.4109 -->`
- 【Linux社区】Kroah-Hartman澄清stable参与完全自愿、不强加负担，但愿参与者应按文档用Cc: stable以获失败通知；称当周有资深核心开发者仍混淆Fixes与Cc: stable，未标注者stable组只能猜测回移。 `<!-- ROW_MINE: ksummit.messages.4139 -->`
- 【Linux社区】Levin给出数据：逾80%带Fixes提交最终进入stable，约70%仅带stable标签的提交修旧版问题，-rc中近85%提交针对合并窗口前问题；引ext4无标签示例，与Bottomley提议对照v6.8核验。 `<!-- ROW_MINE: ksummit.messages.4177 -->`

## 162.18 Bugzilla存废之争

- 【Linux社区】Leemhuis引证Red Hat将在RHEL 9后迁往issues.redhat.com，Fedora负责人Miller主张三年内弃用Bugzilla且仅两人苦撑；其LWN评论主张先导引至求助论坛再提bug。 `<!-- ROW_MINE: ksummit.messages.4113 -->`
- 【Linux社区】Tashkinov反驳Geert以v5.19以来2928个Fixes提交推算日均46修的口径，坚称bugzilla每周仅约二十余份报告并给出七日新建bug查询链接，质疑对方统计有误。 `<!-- ROW_MINE: ksummit.messages.4167 -->`
- 【Linux社区】Tashkinov称邮件列表报告互不连通，bugzilla可集中检索去重；驳斥转发行版建议，称其Fedora内核报告多年无果；自荐任分诊联络人但LF无此职位。 `<!-- ROW_MINE: ksummit.messages.4199 -->`

## 162.19 AI补丁法律风险

- 【Linux社区】Chehab分析两种情形：开源语料训练的AI输出难含实质原始代码；闭源开发若未退出训练条款，向ChatGPT提交受保护代码者须担责，OpenAI条款默认授予可再许可的使用权。 `<!-- ROW_MINE: ksummit.messages.4114 -->`
- 【Linux社区】Bottomley区分维护者依DCO(c)条无责与内核整体风险：若法院裁定AI代码属模型衍生作品，已合入代码或须大规模回退，需集体确定风险容忍度；其个人判断风险小到可接受。 `<!-- ROW_MINE: ksummit.messages.4125 -->`

## 162.20 LLM信任与身份认证

- 【Linux社区】Torvalds称不相信自动化信任系统，因其必被博弈而失却信任本义；真正的信任是对子维护者的人身信任，git签名与kernel.org密钥属身份证明，并提及Greg参与的“去中心化信任”项目。 `<!-- ROW_MINE: ksummit.messages.4118 -->`

## 162.21 HIGHMEM淘汰争议

- 【Linux社区】Bergmann分析sparc32 LEON新SoC配16GiB内存：MMU有36位寻址但Linux未支持64位phys_addr_t，lowmem仅192MB，扩至2GB后高内存比仍7:1，并问NOEL-V rv64替代与2029年后生产需求。 `<!-- ROW_MINE: ksummit.messages.4133 -->`
- 【Linux社区】Ferre确认Microchip sam9x75支持DDR2、DDR3与DDR3L，sam9x60支持LPDDR1等，两款SoC内存上限均256MB，为ARM highmem去留评估提供关键事实。 `<!-- ROW_MINE: ksummit.messages.4156 -->`

## 162.22 AI依赖性争论

- 【Linux社区】Pinchart指Levin立场矛盾——既称不会依赖AI又力推AI工具；Levin称其重写脚本与CVE流程基建均由AI完成但随时可退回手工；Pinchart警告生成式AI日常化将加深依赖。 `<!-- ROW_MINE: ksummit.messages.4134 -->`

## 162.23 明尼苏达事件后补丁审查

- 【Linux社区】Rostedt自述经复查其收到的两处umn.edu琐碎修复均属正当，曾请Greg勿回退其一；主张真正的琐碎仅限注释与文档，无暇审查就别收补丁，仅对少数信任者免审。 `<!-- ROW_MINE: ksummit.messages.4135 -->`

## 162.24 pkeys ABI规范化

- 【Linux社区】Brodsky拟报LPC演讲：pkeys ABI对信号递送、rseq、io_uring工作线程等异步内核交互严重欠定义，各架构重置行为不一致，引Tglx语“全都坏了”，且不适合任何维护子组。 `<!-- ROW_MINE: ksummit.messages.4136 -->`

## 162.25 Rust内核对象生命周期

- 【Linux社区】Kroah-Hartman追问Rust如何处理kref需外加锁的引用计数及dentry、inode、kobject等多生命周期对象交互，称内核需有清晰生命周期规则的“基对象”，以v4l与input层为例。 `<!-- ROW_MINE: ksummit.messages.4160 -->`
- 【Linux社区】Ojeda答初始化与析构期免锁访问可用unsafe fn暴露，调用者须unsafe块并附SAFETY注释说明编译器无法验证的健全性理由，该要求为Rust for Linux强制规范。 `<!-- ROW_MINE: ksummit.messages.4182 -->`

## 162.26 回归修复时限表述

- 【Linux社区】Nikula建议回归修复时限以-rc或发布版本而非日历表述，Leemhuis说明“下个周日”只因Linus惯于周日发-rc，周五前合入可避免用户多忍受一周回归。 `<!-- ROW_MINE: ksummit.messages.4178 -->`

## 162.27 安全修复影响面之争

- 【Linux社区】Suchánek反驳Android至上的论据：真问题是设备并非真开源、无厂商更新则无法升级，大量用户滞留旧版，与stable作为无关；并指云端时代手机数据多存于企业系统。 `<!-- ROW_MINE: ksummit.messages.4181 -->`

## 162.28 Rust文档互链方案

- 【Linux社区】Ojeda回应Arnd对可grep与文档化的担忧：绑定生成不改C名称，计划为rustdoc增加外部引用映射表，使Rust文档可写“类似C的spinlock_t”并经Sphinx生成指向C文档的链接。 `<!-- ROW_MINE: ksummit.messages.4184 -->`

## 162.29 LKML减负方案

- 【Linux社区】Ryabitsev提出三步：get_maintainer.pl的THE REST兜底不再抄linux-kernel；public-inbox加新话题与热门话题RSS；在MAINTAINERS设ALWAYS CC条目指向patches@lists.linux.dev，拟提交维护者峰会。 `<!-- ROW_MINE: ksummit.messages.4187 -->`

## 162.30 stable邮件过载

- 【Linux社区】Bottomley回应Kosina的stable抄送邮件洪峰提案，主张多年所求不过是邮件头标签X-Stable-Base与X-Stable，若在内核文档中规范化即可用procmail过滤，无需进退机制。 `<!-- ROW_MINE: ksummit.messages.4191 -->`
