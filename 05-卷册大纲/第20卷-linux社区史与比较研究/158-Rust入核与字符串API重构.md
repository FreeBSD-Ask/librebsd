158 【Linux社区】Rust入核与字符串API重构

> 来源：ksummit 独有 p22（50 封全读，2021-07 至 2026-07：Wedson 详解 PL061 Rust 驱动注册/资源/一般状态三分法与自动撤销顺序；Linus 逐字节剖析 strlcpy 设计性缺陷与 strscpy 按字长拷贝语义差异含 dst[4] 溢出实例；Konstantin 一手披露 bugzilla.kernel.org 平台濒死开发停滞与紧急转 Postgres 及 bugmaster 无从设立困境；Laurent Pinchart 提出 cdev 驱动生命周期四步方案获 Greg KH 认可；设备直通之争三封、Rust 内核策略与入核早期讨论、AI 补丁政策、文件系统维护信任）
> 判定：39 CAND / 11 NV。主题分布：内核文档工具链 2、加速器驱动用户态 1、Rust内核策略 4、Rust入核早期讨论 3、疫情与线下峰会 1、AI补丁政策 2、linux-next测试 2、LLM审查与语料 1、补丁接受政策 1、字符串API重构 2、设备直通之争 3、cdev生命周期设计 1、静态分析设想 1、C内存安全模式 1、LKML列表政策 1、补丁检查工具 1、API弃用执行 1、编码风格变量声明 1、文件系统维护信任 2、Link标签之争 2、维护者压力与CoC 1、Folio合入流程 1、HIGHMEM退役 1、Bugzilla去留 1、邮件礼仪自动化 1、拒补丁透明度 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p22 的逐封提取（2021-07 至 2026-07，39 CAND / 11 NV），全 26 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 158.1 内核文档工具链

- 【Linux社区】Laurent Pinchart反对文档构建自动选用新版Python，主张构建“应直接失败”，只提示存在可用新版本，称自动选择不可取。 `<!-- ROW_MINE: ksummit.messages.3352 -->`
- 【Linux社区】Mauro给出kernel-doc在Python 3.6至3.13的实测：77.9秒降至31.8秒、提速59.2%；并提出低版本自动重跑、DOC_WARNINGS Kconfig等4项补丁计划。 `<!-- ROW_MINE: ksummit.messages.3446 -->`

## 158.2 加速器驱动用户态

- 【Linux社区】Jonathan Corbet澄清EXPORT_USERSPACE_GPL设想：使用该接口的驱动若无可用的自由用户态实现将不予合并，并非禁止专有用户态。 `<!-- ROW_MINE: ksummit.messages.3357 -->`

## 158.3 Rust内核策略

- 【Linux社区】Kent Overstreet主张test_bit/set_bit类位标志可直接导出为Rust原子类型；认为显式内存序标注比smp_mb__after_atomic更不易因默认x86而漏屏障。 `<!-- ROW_MINE: ksummit.messages.3359 -->`
- 【Linux社区】Dave Airlie反驳“Rust应推迟到2034”：Rust先用于binder、驱动等非核心，未来数年新硬件生产驱动将依赖Rust，尚无核心代码用Rust的提案。 `<!-- ROW_MINE: ksummit.messages.3396 -->`
- 【Linux社区】H. Peter Anvin称标准流程强制写出含边角情形的真正接口契约，并溯源C别名规则源于与Fortran 77在HPC自动向量化上的竞争。 `<!-- ROW_MINE: ksummit.messages.3412 -->`
- 【Linux社区】Ventura Jack承认Rust/C++等表达力语言利于抽象，但代价是编译器庞大：rustc是唯一成熟实现，gccrs未就绪；Rust以生命周期与借用检查器著称。 `<!-- ROW_MINE: ksummit.messages.3433 -->`

## 158.4 Rust入核早期讨论

- 【Linux社区】Laurent Pinchart称C++非好替代，Rust是候选但增益未必抵过开发流程扰动；转述C委员会正考虑defer与lambda，抱怨Rust语法偏离C。 `<!-- ROW_MINE: ksummit.messages.3366 -->`
- 【Linux社区】Greg KH要求Rust展示“真实”驱动：需触碰硬件并自动加载绑定总线；指出此前nvme/i2c/gpio示例不足，binder在Android之外非真实用例。 `<!-- ROW_MINE: ksummit.messages.3424 -->`
- 【Linux社区】Wedson详解PL061 Rust驱动设备状态三分法：Registrations、Resources、General，remove时先注销注册再撤销I/O内存资源，类型系统保证顺序。 `<!-- ROW_MINE: ksummit.messages.3498 -->`

## 158.5 疫情与线下峰会

- 【Linux社区】Toke指出疫苗有效性仅33-93%，跨大西洋会议几乎必然有人暴露过病毒，且“空中桥梁”排斥低疫苗覆盖率地区，质疑社区国际性。 `<!-- ROW_MINE: ksummit.messages.3367 -->`

## 158.6 AI补丁政策

- 【Linux社区】Jiri Kosina认为AI提交的法律责任依DCO条款(a)由提交者承担，接收侧维护者按(c)条款无需担忧，回应Sasha Levin的法律风险之问。 `<!-- ROW_MINE: ksummit.messages.3375 -->`
- 【Linux社区】Paul E. McKenney转述Tony Luck规则建议（From须为真人、人类为补丁负全责），并提出“仅用兼容许可证数据训练的AI”选项，称这将排除所有主流AI。 `<!-- ROW_MINE: ksummit.messages.3505 -->`

## 158.7 linux-next测试

- 【Linux社区】Steven Rostedt解释urgent/core分支工作流：曾将urgent推入linux-next但无收益；修复只入Linus树的bug无需再进next，因next从未发现过这些bug。 `<!-- ROW_MINE: ksummit.messages.3387 -->`
- 【Linux社区】Ted Ts'o称已对fs-next分支跑xfstests自动化2-3个月覆盖ext4/xfs/f2fs/btrfs且稳定，举generic/564回归经回滚vfs溢出修复解决之例。 `<!-- ROW_MINE: ksummit.messages.3432 -->`

## 158.8 LLM审查与语料

- 【Linux社区】Ted Ts'o建议给LKML档案打“被拒/AI废稿/差评审人”标签做微调语料；称前沿模型靠全量抓取、小模型蒸馏后内核知识流失；审评论语比补丁更有价值。 `<!-- ROW_MINE: ksummit.messages.3395 -->`

## 158.9 补丁接受政策

- 【Linux社区】James Bottomley提议新邮件列表基建拒收HTML邮件，并考虑拒绝cover letter未正确抄送的系列补丁，用PATCH标签启发式识别。 `<!-- ROW_MINE: ksummit.messages.3404 -->`

## 158.10 字符串API重构

- 【Linux社区】Linus详析strlcpy设计性缺陷与strscpy两处差异：无损坏返回值、按字长拷贝可能补多个NUL；给出strscpy因字长写溢出dst[4]的实例，警告盲转换改变语义。 `<!-- ROW_MINE: ksummit.messages.3417 -->`
- 【Linux社区】Alexey Dobriyan批评链式调用因实参求值顺序未指定而致实现定义行为、调试器按行操作困难；引述Willy Tarreau长度优先字符串比较在-O3实测提速10倍。 `<!-- ROW_MINE: ksummit.messages.3514 -->`

## 158.11 设备直通之争

- 【Linux社区】Laurent Pinchart披露相机ISP厂商从V4L2跳到DRM以规避固件接口文档公开、搭载闭源二进制；主张以开源用户态实现替代文档，类比GPU驱动规则。 `<!-- ROW_MINE: ksummit.messages.3427 -->`
- 【Linux社区】Ricardo Ribalda称ISP差异化在于算法本身，定义ISP参数即泄露算法与专利风险；专利流氓令厂商不敢冒险，力挺厂商直通模式。 `<!-- ROW_MINE: ksummit.messages.3461 -->`
- 【Linux社区】Laurent Pinchart主张内核须验证DMA类命令保安全；称防厂商作弊无法技术解决只能靠信任与后果（举明尼苏达大学封禁先例），要求ISP开放近100%功能。 `<!-- ROW_MINE: ksummit.messages.3507 -->`

## 158.12 cdev生命周期设计

- 【Linux社区】Laurent Pinchart系统提出cdev驱动生命周期方案：禁用devm_kzalloc分配驱动数据、引用计数、remove时置标志拒新调用、取消I/O并等待调用归零；Greg KH认可。 `<!-- ROW_MINE: ksummit.messages.3430 -->`

## 158.13 静态分析设想

- 【Linux社区】Linus讨论三态返回（真指针、NULL、错误指针）并以get_cached_acl为例；斥gcc nonnull属性“垃圾”，认为给sparse加__nonnull/__errptr不值铺开。 `<!-- ROW_MINE: ksummit.messages.3440 -->`

## 158.14 C内存安全模式

- 【Linux社区】Martin Uecker透露正于GCC前端实验C内存安全模式：按区域开关、保证无UB，聚焦有符号溢出；提议C2Y加入饱和算术，邀请内核社区参与讨论。 `<!-- ROW_MINE: ksummit.messages.3445 -->`

## 158.15 LKML列表政策

- 【Linux社区】Christoph Hellwig称自己一直读LKML并在其上发起讨论，反对限制新列表访问，反讽“若gmail坏就限制所有gmail地址”，回应LKML无讨论价值之说。 `<!-- ROW_MINE: ksummit.messages.3448 -->`

## 158.16 补丁检查工具

- 【Linux社区】Rob Herring主张对每个补丁运行checkpatch，先只启用零误报且共识的检查项再逐子系统放开；指出仅扫源码发现不了Signed-off-by与提交信息缺失。 `<!-- ROW_MINE: ksummit.messages.3450 -->`

## 158.17 API弃用执行

- 【Linux社区】Johannes Berg称弃用API转完即自然消亡，可在-next中删除以拦截新增调用；举PCI MSI弃用近十年却仍最常用为例，反对更多催促加重维护者负担。 `<!-- ROW_MINE: ksummit.messages.3462 -->`

## 158.18 编码风格变量声明

- 【Linux社区】Bart Van Assche以git grep统计“for (int ”在Documentation与tools之外已用1239处，主张编码规范应全局统一而非__free独例，回应cleanup.h变量声明之争。 `<!-- ROW_MINE: ksummit.messages.3464 -->`

## 158.19 文件系统维护信任

- 【Linux社区】Kent Overstreet称lklfuse没有VFS到fuse的层且会拖入整块层与调度器过重，bcachefs-tools用kthreads映射pthread、块层映射aio的更薄方案。 `<!-- ROW_MINE: ksummit.messages.3470 -->`
- 【Linux社区】Linus在FAT文件系统讨论中承认mmap假设未达预期，提出cache不一致的MAP_PRIVATE mmap可行，但比维持现状工作量大得多。 `<!-- ROW_MINE: ksummit.messages.3486 -->`

## 158.20 Link标签之争

- 【Linux社区】Doug Anderson提三条：改git默认隐藏Link标签、用AI帮补丁追踪器关联历史版本并摘要讨论、社区“干预”Linus接受Link标签，称支持者众多。 `<!-- ROW_MINE: ksummit.messages.3474 -->`
- 【Linux社区】Doug Anderson澄清“b4 dig”乌龙：Google搜到的全是Sasha同名工具，Konstantin补丁未进b4 v0.14.3；称git patch-id精确匹配、主题匹配兜底约95%可用。 `<!-- ROW_MINE: ksummit.messages.3483 -->`

## 158.21 维护者压力与CoC

- 【Linux社区】Shuah以CoC成员身份否认“CoC只针对维护者行为”，提出平衡公司战略与开发需求的“戴两顶帽”问题，建议合并各项维护者压力提案统筹讨论。 `<!-- ROW_MINE: ksummit.messages.3475 -->`

## 158.22 Folio合入流程

- 【Linux社区】Chris Mason区分两问：合并folio还剩多少工作、如何让folio级改动的开发过程更可预期且有回报；讨论LPC BOF与BBB基础设施等替代LSF/MM的场地。 `<!-- ROW_MINE: ksummit.messages.3477 -->`

## 158.23 HIGHMEM退役

- 【Linux社区】Christophe Leroy询问Richard所用PPC32型号（mpc85xx？）以考虑局部保留，并已提交在powerpc上完全移除CONFIG_HIGHMEM的补丁摸清影响面。 `<!-- ROW_MINE: ksummit.messages.3478 -->`

## 158.24 Bugzilla去留

- 【Linux社区】Konstantin透露Bugzilla平台濒死：开发停滞、不兼容新版MySQL、perl5/mod_perl，IT正转Postgres以撑过2022；核心难题是bugmaster人选且极易倦怠。 `<!-- ROW_MINE: ksummit.messages.3499 -->`

## 158.25 邮件礼仪自动化

- 【Linux社区】Konstantin反对自动化“引用过多”警告，称无法区分正当长引用会误伤无辜；主张线下邮件指导并附tglx网络礼仪页，愿在subspace.kernel.org加礼仪页。 `<!-- ROW_MINE: ksummit.messages.3508 -->`

## 158.26 拒补丁透明度

- 【Linux社区】Wolfram Sang澄清诉求是写明拒收理由属个人还是法务，否则他无法判断自己子系统遇同类补丁时该如何处理，并非重议补丁该不该收。 `<!-- ROW_MINE: ksummit.messages.3511 -->`
