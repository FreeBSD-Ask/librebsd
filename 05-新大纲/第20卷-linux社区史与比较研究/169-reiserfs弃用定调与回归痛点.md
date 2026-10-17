# 169 【Linux社区】reiserfs弃用定调与回归痛点

> 来源：ksummit 独有 p33（50 封全读，2021-04 至 2026-07：Torvalds 一手定调 buffer_head 老不等于坏并直言 reiserfs 被弃用非因技术流程而是 Hans Reiser 杀妻；Leemhuis 系统列举回归追踪痛点清单含 -next 滞留 bugzilla 无人处理 Link 标签缺失与 CI 回归属；Chamberlain 给出 AI 训练语料许可比例估计约 60% 宽松 25% GPL 15% 不明与个人风险评估、McKenney 以 copyleft 追责先例正面交锋；Pinchart 剖析 Sashiko AI 评审 bot 对 DMA 字段误报 TOCTOU 高危根源系硬件不应预设恶意原则未进提示词；Link 标签规范之辩五封、Rust 与 C 语义之辩三封、设备直通之辩三封）
> 判定：45 CAND / 5 NV。主题分布：回归追踪与regzbot 3、特性纳入与剔除之辩 2、隐藏提交与next滞后 2、Link标签规范之辩 5、旧内核构建Werror补丁 1、文件系统弃用之争 2、编译器警告与UB取舍 3、NVMe拷贝卸载议题 1、HIGHMEM淘汰之辩 1、SCSI栈用户态化之辩 1、内核文档构建优化 2、设备直通之辩 2、琐碎补丁政策之辩 2、内核malloc接口之争 1、diff审阅工具推荐 1、Rust与C语义之辩 3、邮件工具与工作流 3、驱动资源与生命周期 1、AI辅助代码标注 2、安全公告与stable基线 1、Rust驱动引入之辩 2、linus-next测试二分 1、AI评审bot误报 1、DAMON内存监测议题 1、stable标签政策矛盾 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p33 的逐封提取（2021-04 至 2026-07，45 CAND / 5 NV），全 25 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 169.1 回归追踪与regzbot

- 【Linux社区】Leemhuis详述regzbot设计：#regzb邮件标签追踪人工回归报告，Link:标签自动闭环，与KernelCI及KCIDB分工避免重复，项目获NGI pointer资助一年 `<!-- ROW_MINE: ksummit.messages.5111 -->`
- 【Linux社区】Leemhuis为峰会拟议题：简单回归修复在-next滞留数周、bugzilla大量报告无人处理、开发者漏加Link:标签、CI回归归属及低质量厂商内核报告等待议 `<!-- ROW_MINE: ksummit.messages.5246 -->`
- 【Linux社区】Leemhuis基于三年回归追踪经验提交LPC议题：剖析致回归高发与修复迟缓的工作流模式，解释各子系统快慢悬殊，并汇报regzbot实践与路线 `<!-- ROW_MINE: ksummit.messages.5268 -->`

## 169.2 特性纳入与剔除之辩

- 【Linux社区】Chehab主张维护者离开不应立即剔除特性，宜给一两个周期等人接手、实验特性先进staging；赞同Rostedt建立维护者导师培训制 `<!-- ROW_MINE: ksummit.messages.5112 -->`
- 【Linux社区】Chehab介绍媒体子系统惯例：争议特性先进staging（如有状态与无状态编解码器），并认同Ts'o反对以投票或核心团队裁决取代维护者层级判断 `<!-- ROW_MINE: ksummit.messages.5161 -->`

## 169.3 隐藏提交与next滞后

- 【Linux社区】Kozlowski证实补丁滞留维护者树曾致其漏掉DT绑定集成问题，指rebase丢失签名标签信任链，引其统计约133个提交迟至近两周才入linux-next `<!-- ROW_MINE: ksummit.messages.5115 -->`
- 【Linux社区】Bottomley针对不进-next子树的修复滞后，提议修复应视同bug修复快速上行，或需为此类树补充规则与鼓励条款 `<!-- ROW_MINE: ksummit.messages.5157 -->`

## 169.4 Link标签规范之辩

- 【Linux社区】Ryabitsev宣布b4 0.14新增-i选项可插入Message-ID: trailer替代Link:，另可用gitconfig的linktrailermask沿用-l输出 `<!-- ROW_MINE: ksummit.messages.5120 -->`
- 【Linux社区】Anderson发现b4 dig仍需Message-Id作输入且尚未落地，质疑弃用Link:标签的论证自相矛盾，引Sasha的RFC为证 `<!-- ROW_MINE: ksummit.messages.5146 -->`
- 【Linux社区】Williams提议约定子系统在拉取请求中更新notes，由pr-tracker-bot维护中央notes树向下游传递元数据，不改Linus工作流与主线提交 `<!-- ROW_MINE: ksummit.messages.5192 -->`
- 【Linux社区】Iwai向Torvalds解释：其git钩子本自动把Message-Id转为Link，迁移工作站后失效致近几次PR残留Message-Id，已在最近PR修复 `<!-- ROW_MINE: ksummit.messages.5213 -->`
- 【Linux社区】Ellerman质疑散文脚注式链接套用Link:前缀的必要，举Arnd的TEE合并提交为例，主张标准markdown引用式链接即可，脚本无法解读此类链接 `<!-- ROW_MINE: ksummit.messages.5271 -->`

## 169.5 旧内核构建Werror补丁

- 【Linux社区】Carpenter称新编译器拒建旧内核致Smatch无法分析古董内核，清理-Werror未果，拟GCC补丁以IGNORE_WERROR环境变量忽略-Werror `<!-- ROW_MINE: ksummit.messages.5123 -->`

## 169.6 文件系统弃用之争

- 【Linux社区】Roeck举提交eb103a51640e（弃用reiserfs）为文件系统弃用流程的完美范例，反驳准废弃文件系统转只读无助于减轻维护负担 `<!-- ROW_MINE: ksummit.messages.5126 -->`
- 【Linux社区】Torvalds称buffer_head虽老旧简陋但胜任遗留场景，“老不等于坏”；驳斥以reiserfs弃用为范例：无人愿碰只因Hans Reiser杀妻，绝非流程典范 `<!-- ROW_MINE: ksummit.messages.5250 -->`

## 169.7 编译器警告与UB取舍

- 【Linux社区】Uecker回应Carpenter：GCC可仿Smatch在宏内关闭unsigned比较警告且已有类似启发式，指瓶颈在沟通与资源投入而非技术障碍 `<!-- ROW_MINE: ksummit.messages.5140 -->`
- 【Linux社区】NeilBrown提议修复者在提交信息加入type system段落说明更强类型系统能否预防该bug，自动收集分析以实证Rust类型安全论点 `<!-- ROW_MINE: ksummit.messages.5202 -->`
- 【Linux社区】Rostedt解释内核禁用pragma因其令Sparse失效；静态调用依赖gcc未定义行为（void函数冒充带参调用）避开间接调用，运行期UB捕获需保留已知UB `<!-- ROW_MINE: ksummit.messages.5219 -->`

## 169.8 NVMe拷贝卸载议题

- 【Linux社区】Van Assche为NVMe SCC拷贝卸载议题补充关联的Storage: Copy Offload讨论与其GitHub实现笔记，议题涵盖ioctl、io_uring、copy_file_range接口选择 `<!-- ROW_MINE: ksummit.messages.5147 -->`

## 169.9 HIGHMEM淘汰之辩

- 【Linux社区】Torvalds称x86 1GB内存机型通常896MB低端内存加约120MB高端内存，可用2G:2G划分，老机器宜留旧内核；Anvin认同2:2分法合宜 `<!-- ROW_MINE: ksummit.messages.5149 -->`

## 169.10 SCSI栈用户态化之辩

- 【Linux社区】Van Assche反驳将SCSI栈移入用户态：数十亿Android手机使用基于SCSI的UFS存储，已有30万IOPS设备，迁移将严重拖累Android性能 `<!-- ROW_MINE: ksummit.messages.5153 -->`

## 169.11 内核文档构建优化

- 【Linux社区】Chehab拆解文档构建三处Python依赖：sphinx-pre-install、Makefile内Sphinx逻辑在Python3.7以下失败、kernel-doc慢约60%，建议自动择优并提示所用版本 `<!-- ROW_MINE: ksummit.messages.5155 -->`
- 【Linux社区】Nossum实测约40%构建耗时在C域resolve_xref、PyPy提速22%；Corbet自述曾砍20%耗时，GCC文档同病，议以conf.py开关禁用C域 `<!-- ROW_MINE: ksummit.messages.5217 -->`

## 169.12 设备直通之辩

- 【Linux社区】Ribalda称ISP渐成可编程设备，厂商因专利雷区与产品差异化拒公开用户态与ISP间算法交互，以此论证厂商受限直通的必要性 `<!-- ROW_MINE: ksummit.messages.5156 -->`
- 【Linux社区】Gunthorpe称DPDK承载大量互联网与移动流量及ORAN实时射频处理，用户态与内核取舍应凭技术优劣而非教条，Mellanox双轨支持，非5-10倍提升勿用DPDK `<!-- ROW_MINE: ksummit.messages.5235 -->`

## 169.13 琐碎补丁政策之辩

- 【Linux社区】Brown回应Leon批评精挑收件人做法：全量抄送会使补丁系列迅速嘈杂，反而无人细读，属琐碎补丁政策讨论中的立场交锋 `<!-- ROW_MINE: ksummit.messages.5162 -->`
- 【Linux社区】Bottomley提议无Fixes:标签不收bug修复并要求说明缺陷来历以剔除伪修复，指出增进信任与改进缺陷流程是两条不同路径 `<!-- ROW_MINE: ksummit.messages.5214 -->`

## 169.14 内核malloc接口之争

- 【Linux社区】Torvalds强烈反对自动选GFP标志的“魔法malloc”：自旋锁内分配必须自知用GFP_ATOMIC，kzmalloc_obj只是类型安全便利而非掩盖内核分配规则 `<!-- ROW_MINE: ksummit.messages.5172 -->`

## 169.15 diff审阅工具推荐

- 【Linux社区】Belloni推荐delta分页器并给出git配置实现并排逐行diff高亮，辅助审阅重命名补丁，回应wdiff与diff-highlight讨论 `<!-- ROW_MINE: ksummit.messages.5175 -->`

## 169.16 Rust与C语义之辩

- 【Linux社区】Lossin论证对UnsafeCell取多个共享引用可同线程变更、语义等价C指针；Opaque借PhantomPinned变!Unpin以关闭noalias，树内pinned-init不依赖nightly `<!-- ROW_MINE: ksummit.messages.5178 -->`
- 【Linux社区】Tarreau以gcc-2.95汇编对照证实-freg-struct-return在i386与ARM使小结构体经寄存器返回，省去内存往返，赞成做成按函数属性 `<!-- ROW_MINE: ksummit.messages.5207 -->`
- 【Linux社区】Ventura Jack举安全Rust反更慢实例：运行期边界检查与get_unchecked取舍、rustc升级后自动向量化消失致性能回退，图像解码库仅追平Wuffs `<!-- ROW_MINE: ksummit.messages.5263 -->`

## 169.17 邮件工具与工作流

- 【Linux社区】Luck分享不订阅列表的回帖流程：b4 mbox按message-id下载整线程为mbox，再用mutt打开回复 `<!-- ROW_MINE: ksummit.messages.5180 -->`
- 【Linux社区】Perches自述已不订阅LKML也很少参与讨论，仅偶用lore关键词检索并手动下载线程消息，回应MAINTAINERS收件范围争论 `<!-- ROW_MINE: ksummit.messages.5225 -->`
- 【Linux社区】Romanovsky实测mutt加b4键绑三处障碍：Maildir迁移脚本半成、从讨论中段lore链接取全系列失败、b4只取补丁不取讨论回复 `<!-- ROW_MINE: ksummit.messages.5259 -->`

## 169.18 驱动资源与生命周期

- 【Linux社区】Gunthorpe指kobj释放与错误回滚缺陷或可被root在模块加载时利用，批评v4l2把init与register合一模式固化进子系统，另提devm与工作队列时序问题 `<!-- ROW_MINE: ksummit.messages.5184 -->`

## 169.19 AI辅助代码标注

- 【Linux社区】Kosina主张将tip手册中SOB链与Co-developed-by规范推广为全内核要求，叠加LLM辅助标注即可基本解决AI代码标注问题 `<!-- ROW_MINE: ksummit.messages.5210 -->`
- 【Linux社区】Chamberlain估算Github语料约60%宽松许可、25%GPL、15%不明，认为copyleft项目风险低值得拥抱AI；McKenney提醒已有追究copyleft先例且诉讼在审 `<!-- ROW_MINE: ksummit.messages.5211 -->`

## 169.20 安全公告与stable基线

- 【Linux社区】Kosina回应Greg批评发行版非要预知具体修复，称愿把议题转为“如何让主流发行版基于-stable内核”，指出该题已被广泛讨论 `<!-- ROW_MINE: ksummit.messages.5212 -->`

## 169.21 Rust驱动引入之辩

- 【Linux社区】Van Assche反驳Torvalds拒C++论：其经历的项目均启用-fno-exceptions与-fno-rtti，operator new可自定义绕开异常依赖，并附示例代码 `<!-- ROW_MINE: ksummit.messages.5224 -->`
- 【Linux社区】Ojeda回应Leon质疑：Rust驱动经子系统抽象层调用而非直呼C代码，CONFIG_RUST当时仅影响vsprintf一处格式符，目标架构默认启用，Rust静态禁UB强于UBSan `<!-- ROW_MINE: ksummit.messages.5247 -->`

## 169.22 linus-next测试二分

- 【Linux社区】Brown澄清其曾在帖中讲过mainline、pending-fixes与-next之间二分方法，认同应收入官方文档并承诺提交patch `<!-- ROW_MINE: ksummit.messages.5231 -->`

## 169.23 AI评审bot误报

- 【Linux社区】Pinchart指Sashiko对SCSI补丁误报DMA字段TOCTOU高危：硬件不应预设恶意（仅虚拟化来宾与USB等例外），归因于评审提示词，拟向kernel/subsystems增drivers.md `<!-- ROW_MINE: ksummit.messages.5258 -->`

## 169.24 DAMON内存监测议题

- 【Linux社区】Park提议峰会演示十分钟用DAMON与DAMOS编写访问模式感知模块：70GB生产机每5ms全量扫描仅耗1%单核，三行scheme实现感知THP与主动回收，已入Amazon Linux `<!-- ROW_MINE: ksummit.messages.5262 -->`

## 169.25 stable标签政策矛盾

- 【Linux社区】Corbet点破矛盾：Greg称stable参与完全自愿不增负担，Sasha却称文档明言stable标签必须添加并反复催促，追问内核实际政策为何 `<!-- ROW_MINE: ksummit.messages.5267 -->`
