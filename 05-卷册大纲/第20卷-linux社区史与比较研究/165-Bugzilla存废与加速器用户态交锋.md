# 165 【Linux社区】Bugzilla存废与加速器用户态交锋

> 来源：ksummit 独有 p29（50 封全读，2021-04 至 2026-08：Johannes Berg 对 Linus 强推移除 Link 尾注的罕见直白批评直指仁君社会契约破裂与权力动态；Coly Li RichACL 重启提案附创业产品公测 13 个月装机超百万实测；Dave Airlie 与 Greg KH 就加速器驱动用户态政策正面交锋举一个听劝入社区的群体来与得益的是 Linux 基金会而非 Linux；2022 都柏林维护者峰会完整日程含 Linus 开心吗环节与 28 位顶级维护者名单；Bugzilla 缺陷跟踪六封、Rust 内核开发六封、AI 生成代码政策四封）
> 判定：43 CAND / 7 NV。主题分布：内核文档工具链 3、加速器驱动用户态 3、AI生成代码政策 4、Link尾注争议 1、新开发者治理 2、Bugzilla缺陷跟踪 5、安全报告流程 1、RichACL提案 1、子系统树合并规范 1、静态分析议题 1、Rust内核开发 5、维护者峰会组织 2、fwctl设备直通 2、TAB选举与延续 1、别名与代码生成 1、kernel.org账号管理 1、文件系统用户态化 1、驱动probe失败处理 1、cleanup注解 1、AI辅助评审 1、trivial补丁政策 1、回归跟踪bot 1、维护者倦怠 1、cdev生命周期 1、KTODO任务清单 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p29 的逐封提取（2021-04 至 2026-08，43 CAND / 7 NV），全 25 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 165.1 内核文档工具链

- 【Linux社区】Linus称内核历来视提交生成文件为痛苦，mkutf8data几无人重新生成，对flex/bison主张“直接写更好的代码”而非依赖生成器产物。 `<!-- ROW_MINE: ksummit.messages.4537 -->`
- 【Linux社区】Corbet用字典替换Sphinx符号查找中的部分线性搜索，使Sphinx 5.0.2全量htmldocs构建提速约20%，称其符号查找代码复杂度“令人生畏”。 `<!-- ROW_MINE: ksummit.messages.4538 -->`
- 【Linux社区】Pinchart反对盲改用户所选Python解释器，主张以提示代替；引Mauro数据称kernel-doc改用新解释器可提速55%至60%，openSUSE Leap等需python311-sphinx。 `<!-- ROW_MINE: ksummit.messages.4643 -->`

## 165.2 加速器驱动用户态

- 【Linux社区】Pinchart引GPLv2系统例外条款，认为禁止闭源用户态在许可上不可行且开危险先例；主张可拒绝合并只暴露未文档化厂商API的驱动，DMA-BUF互操作可作筛选判据。 `<!-- ROW_MINE: ksummit.messages.4541 -->`
- 【Linux社区】Triplett表态：不应强制接口的所有用户态皆开源，但要求“至少存在一个开源用户态实现”作为新增接口的前提。 `<!-- ROW_MINE: ksummit.messages.4564 -->`
- 【Linux社区】Airlie反驳Greg的niche设备论：“举一个听劝入社区的群体来”；称HabanaLabs入上游系RHEL、亚马逊等采购合同所迫，断言“得益的是Linux基金会而非Linux”。 `<!-- ROW_MINE: ksummit.messages.4645 -->`

## 165.3 AI生成代码政策

- 【Linux社区】McKenney主张现阶段将AI生成代码排除出内核，称多起诉讼进行中、法院走向未知；建议沿用DCO与SoB：“若不确定拥有提交权就不要提交”。 `<!-- ROW_MINE: ksummit.messages.4542 -->`
- 【Linux社区】Mauro认为AI带来的法律风险与现有开发无异甚至更低——大厂重金投入AI、不愿被诉，预计不会出现针对AI使用者的低成本高回报诉讼。 `<!-- ROW_MINE: ksummit.messages.4552 -->`
- 【Linux社区】Stoakes批评工具生成内容指南草案回避要害：LLM可让无知识者端到端发补丁，维护者资源不对称前所未有，建议明文允许对“slop”系列直接拒收。 `<!-- ROW_MINE: ksummit.messages.4556 -->`
- 【Linux社区】Stoakes提交增量补丁要求全自动系列受额外审视并写明“维护者不容忍slop”；Bottomley建议删该词，Stoakes称意在向媒体传达内核不接受AI垃圾的立场。 `<!-- ROW_MINE: ksummit.messages.4595 -->`

## 165.4 Link尾注争议

- 【Linux社区】Berg直指Linus强推移除Link标签违背“仁君”社会契约、破坏信任，称这已成自我与权力之争而非技术问题，并提出可将message-id编码进git提交对象。 `<!-- ROW_MINE: ksummit.messages.4543 -->`

## 165.5 新开发者治理

- 【Linux社区】Ts'o为新人补丁bot细化规则：若补丁基于LTS分支且缺Upstream-commit:标签应告警；无法简单回移的LTS特殊修复属高级用法，bot可忽略。 `<!-- ROW_MINE: ksummit.messages.4546 -->`
- 【Linux社区】Pinchart指维护者也难定补丁基树，b4的base-commit与prerequisite-patch-id尾注有帮助但未普及，盼新人机制顺带强制补丁携带基线信息。 `<!-- ROW_MINE: ksummit.messages.4557 -->`

## 165.6 Bugzilla缺陷跟踪

- 【Linux社区】用户Tashkinov列出最低诉求：集中收集、组件及时更新、可CC相关人；举例bug 204807两年255条评论附补丁，断言邮件无法承载此类协作。 `<!-- ROW_MINE: ksummit.messages.4548 -->`
- 【Linux社区】Ts'o称Launchpad上e2fsprogs报告多为浪费时间，Debian邮件式报告反而数据齐全可定位，质疑“流行百倍”意味着“噪音千倍”。 `<!-- ROW_MINE: ksummit.messages.4576 -->`
- 【Linux社区】Iwai指出bugzilla根本缺陷在缺初筛：报告只达组件指派人而非公共列表，既不扩展也难分流；并称内核无法判断设备是否正常，错误信息只能逐案处理。 `<!-- ROW_MINE: ksummit.messages.4581 -->`
- 【Linux社区】Tarreau反驳：邮件列表是广播式集体努力，缺陷跟踪器却给报告者“正被处理”的错觉并对个别开发者施加定向压力，参与度模型上邮件更优。 `<!-- ROW_MINE: ksummit.messages.4582 -->`
- 【Linux社区】Tarreau详陈邮件列表优越：集体浏览、无人不可或缺；以“未回复以一周计、多为LKP报告”驳“大量石沉大海”说，并斥bugzilla强制订阅近于垃圾邮件逻辑。 `<!-- ROW_MINE: ksummit.messages.4654 -->`

## 165.7 安全报告流程

- 【Linux社区】Ryabitsev警告security@kernel.org是单点故障，持0-day者可瘫痪kernel.org；提出security.txt多地址、直投地址、Signal备用通道与SecureDrop等冗余方案。 `<!-- ROW_MINE: ksummit.messages.4560 -->`

## 165.8 RichACL提案

- 【Linux社区】bcache维护者Coly Li称其AI存储创业产品公测13个月装机超百万，POSIX ACL无法承载AI任务访问控制，用户态方案性能不济，提议重启RichACL上游化讨论。 `<!-- ROW_MINE: ksummit.messages.4561 -->`

## 165.9 子系统树合并规范

- 【Linux社区】Rostedt称合并提交应像普通提交一样说明目的；其多topic分支间偶以带详细说明的合并共享补丁，Linus未抱怨，佐证Linus重质量而非数量。 `<!-- ROW_MINE: ksummit.messages.4572 -->`

## 165.10 静态分析议题

- 【Linux社区】Lawall核查ovl_lookup_inode调用上下文，指出NULL与ERR_PTR并存在两处调用点行为各异，属“可选资源”模式而非单纯编码错误。 `<!-- ROW_MINE: ksummit.messages.4573 -->`

## 165.11 Rust内核开发

- 【Linux社区】Kumar介绍Linaro Stratos用Rust编写hypervisor无关的vhost-user后端，处理I2C、GPIO、RPMB等guest请求；virtio GPIO规范推进中，Rust I2C后端已在rust-vmm评审。 `<!-- ROW_MINE: ksummit.messages.4574 -->`
- 【Linux社区】Lutomirski建议以virtio作Rust示范：virtio ring极不安全，!use_dma变体是历史错误，其设备内存用法本不该通过编译，应标注unsafe并注明“这确实是错的”。 `<!-- ROW_MINE: ksummit.messages.4599 -->`
- 【Linux社区】Elver强调安全抽象不等于无bug：Rust须集成KASAN、KCSAN、KMSAN（rustc -Zsanitizer）才能抓C与Rust边界错误，如C侧误释放与跨语言数据竞争。 `<!-- ROW_MINE: ksummit.messages.4622 -->`
- 【Linux社区】Ojeda解析try_writeb运行期检查因offset非编译期常量，介绍以持有不变量的类型复用安全知识，盼Rust支持对静态范围循环变量取编译期值。 `<!-- ROW_MINE: ksummit.messages.4635 -->`
- 【Linux社区】Ojeda梳理Rust分配器史：初用vendor的alloc crate，v6.10借Wedson方案传GFP标志（b6a006e21b82），v6.13由Danilo自建alloc模块与Allocator trait（b7a084ba4fbb）。 `<!-- ROW_MINE: ksummit.messages.4650 -->`

## 165.12 维护者峰会组织

- 【Linux社区】Ts'o宣布2024维护者峰会9月17日维也纳举行、限30名受邀者，程序委员会为Brauner、Corbet、Greg KH、Levin、Ts'o、Wysocki六人，KS议题截止延至6月23日。 `<!-- ROW_MINE: ksummit.messages.4575 -->`
- 【Linux社区】Ts'o公布2022都柏林维护者峰会日程：回归追踪（Leemhuis）、Rust下一步（Ojeda）、eBPF边界（Kosina）及“Linus开心吗”环节，附28位维护者参会名单。 `<!-- ROW_MINE: ksummit.messages.4637 -->`

## 165.13 fwctl设备直通

- 【Linux社区】Gunthorpe预言GPU同样需要fwctl（固件调试追踪成难题），强调fwctl不得排他：固件接口必须可共享或被阻断，不能因此放弃功能性子系统接口。 `<!-- ROW_MINE: ksummit.messages.4578 -->`
- 【Linux社区】Gunthorpe称fwctl历经三年会议讨论已成多方驱动维护者共识并在netdev会议报告；预判RDMA要开放共享固件接口、netdev要拒绝的分歧不会因再讨论而改变。 `<!-- ROW_MINE: ksummit.messages.4628 -->`

## 165.14 TAB选举与延续

- 【Linux社区】Ojeda澄清TAB选举通常随KS或LPC举行但非硬性要求，若某年未办峰会或改期将照常选举，社区曾简略讨论调整此事。 `<!-- ROW_MINE: ksummit.messages.4579 -->`

## 165.15 别名与代码生成

- 【Linux社区】Overstreet与Linus激辩：Kent主张Rust若解决别名可消除spill并使VLIW可行，Linus称别名极少要紧、OoO根本优于VLIW，并同批C未定义行为泛滥。 `<!-- ROW_MINE: ksummit.messages.4588 -->`

## 165.16 kernel.org账号管理

- 【Linux社区】Ryabitsev说明kernel.org已有MIA处置机制：SSH密钥一年未用即自动停用，仅保留邮件别名，以此回应Uwe关于失联账号的质疑。 `<!-- ROW_MINE: ksummit.messages.4596 -->`

## 165.17 文件系统用户态化

- 【Linux社区】Disseldorp详解lklfuse运行完整内核VFS到文件系统路径、LKL为non-mmu架构、仅依赖non-mmu xfs_buf一处下游改动，并问Chinner是否重审XFS non-mmu提案。 `<!-- ROW_MINE: ksummit.messages.4602 -->`

## 165.18 驱动probe失败处理

- 【Linux社区】Pinchart辨析probe失败未必是驱动之过、可能设备故障致同型号多实例皆废；并称驱动并非defunct而是已加载未绑定，sysfs残留问题待解。 `<!-- ROW_MINE: ksummit.messages.4603 -->`

## 165.19 cleanup注解

- 【Linux社区】Rostedt证实tracing子系统已转向_cleanup_注解简化错误分支，给出两个lore系列链接，并计划将之加入自己的tracing库。 `<!-- ROW_MINE: ksummit.messages.4605 -->`

## 165.20 AI辅助评审

- 【Linux社区】Brown举反例：有人一周末与Sashiko迭代15版简单quirk后仍被人评“方向不对”，对照Roeck的350行驱动9问题案例，主张需找中间道路。 `<!-- ROW_MINE: ksummit.messages.4606 -->`

## 165.21 trivial补丁政策

- 【Linux社区】Khan查证UMN补丁8e949363f017（mlx5 idr_find检查）绝非trivial；Kosina自认trivial.git荒废多年且umn.edu补丁无一经该树进入；结论唯靠评审。 `<!-- ROW_MINE: ksummit.messages.4611 -->`

## 165.22 回归跟踪bot

- 【Linux社区】Leemhuis详述regzbot构想：#regzb标签、初期靠人工补标、恳请把regressions@列入回复CC，长远每周rc前后向Linus与LKML发报告；Greg KH愿提供stable工具。 `<!-- ROW_MINE: ksummit.messages.4614 -->`

## 165.23 维护者倦怠

- 【Linux社区】Pinchart称评审满负荷时效率骤降；互换评审对企业贡献者仅限业务相关，求评无关驱动即遭“没空”；建议大厂商按比例承担业务外评审义务。 `<!-- ROW_MINE: ksummit.messages.4633 -->`

## 165.24 cdev生命周期

- 【Linux社区】Williams介绍CXL驱动做法：remove时把devm数据从cdev断开、ioctl全部失败直至用户态关闭；提出推广debugfs的FULL_PROXY_FUNC代理机制到驱动ioctl关停同步。 `<!-- ROW_MINE: ksummit.messages.4647 -->`

## 165.25 KTODO任务清单

- 【Linux社区】Howlett建议KTODO工具在缺Closes:标签时反查受影响函数的潜在git提交以列出未决问题，类比stable补丁失败邮件的关联提示。 `<!-- ROW_MINE: ksummit.messages.4662 -->`
