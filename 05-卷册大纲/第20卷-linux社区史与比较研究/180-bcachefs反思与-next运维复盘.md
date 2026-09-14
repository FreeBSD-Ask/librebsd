# 180 【Linux社区】bcachefs反思与-next运维复盘

> 来源：ksummit 独有 p44（50 封全读，2023-11 至 2026-08：Ted Ts'o 把 bcachefs 争议定性为人事问题宜私下调解并系统反驳当初拒收即可避免与民主投票两种替代方案；Mark Brown 2026 年 -next 维护者对 Rust 构建 KASAN+KUnit kselftest 接入弃树决策的全面自述属罕见整建制运维史料；Coly Li 详述 NAS 本地 AI 相册分类权限用例与 LSM 只能拒绝不能授权设计困境；Sasha 与 Linus 论 Fixes 标签披露回传 AUTOSEL 与谷歌机器人强制 Fixes 制度由来且 Linus 拒绝新增 Improves 标签；linux-next 运维复盘与 AI 审查工具与 CI 双封、GitLab 流程迁移争论双封）
> 判定：44 CAND / 6 NV。主题分布：linux-next 运维复盘 2、AI 审查工具与 CI 2、AI 辅助补丁标注 2、峰会议程安排 1、cleanup 属性之争 2、GitLab 流程迁移争论 2、Link 标签与 lore 链接 1、fwctl 与 EDAC 之争 1、checkpatch 局限 1、buffer_head 淘汰路线 1、AI 生成内容守则 1、倦怠支持资源 1、API 弃用执行方案 1、Rust 语义争论 2、linux-next 驻留时长 1、Fixes 标签政策 2、驱动 probe 设计澄清 1、高端内存淘汰调查 1、加速器驱动开源门槛 1、AI 审查提示词工程 1、Sphinx 版本下限 1、稳定版回归修复义务 1、b4 线程回填用法 1、Rust 内核政策 1、安全 embargo 代码质量 1、引文礼仪之争 1、Werror 处置之争 1、设备直通与相机 ISP 1、AI 时代 ACL 需求 1、审查自动化减负 1、文件系统用户态化构想 1、bcachefs 事件反思 1、AI 代码质量标准 1、trivial 树兴衰 1、linus-next 测试价值 1、kernel.org 信任改造 1、Rust 寄存器访问安全 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p44 的逐封提取（2023-11 至 2026-08，44 CAND / 6 NV），全 37 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 180.1 linux-next 运维复盘

- 【Linux社区】Mark Brown 盘点 -next 现状：新增 Rust 构建、KASAN 加持的 KUnit、kselftest 子集与每周状态摘要，曾因问题移除一个子树，并征询文档构建、重复提交报告等改进方向。 `<!-- ROW_MINE: ksummit.messages.6797 -->`
- 【Linux社区】Brown 说明有意双树造成的重复提交提示邮件仍需手工发送，计划 Stephen 休假期间改进脚本，或把此类树标记为预期重复以实现自动化。 `<!-- ROW_MINE: ksummit.messages.6892 -->`

## 180.2 AI 审查工具与 CI

- 【Linux社区】Pinchart 介绍 netdev 与 media 子系统 CI：补丁经 patchwork 接口取走测试，结果以红黄绿标示，失败不自动改状态而由人工裁决；checkpatch 误报多，靠自动邮件要求修正重交。 `<!-- ROW_MINE: ksummit.messages.6799 -->`
- 【Linux社区】Chris Mason 澄清 BPF 现状：patchwork 触发的 CI 已运行 AI 审查提示词，kernel-patches/bpf 第 9962 号 PR 的评论全部来自 AI 审查产出。 `<!-- ROW_MINE: ksummit.messages.6857 -->`

## 180.3 AI 辅助补丁标注

- 【Linux社区】Sasha Levin 认为 AI 补丁与 checkpatch、syzbot 垃圾修复同属症状，根源是提交者不理解内容；Pinchart 主张把工具生成内容的政策一并写清，一石二鸟。 `<!-- ROW_MINE: ksummit.messages.6808 -->`
- 【Linux社区】Luck 提议禁止 AI 代理直接发补丁、From 行人类负全责；Sasha 回应已有签署要求与提交清单 11 项检查常被无视，问题在规则被无视而非缺失。 `<!-- ROW_MINE: ksummit.messages.6814 -->`

## 180.4 峰会议程安排

- 【Linux社区】Ted Ts'o 将 ChromeOS 议题从性能 MC 的 20 分钟档改排内核峰会轨道 45 分钟，理由是议题实为开发流程可扩展性而非硬件扩展性，另设周五 BOF 与不直播的黑客房。 `<!-- ROW_MINE: ksummit.messages.6816 -->`

## 180.5 cleanup 属性之争

- 【Linux社区】Linus 认为 kmalloc_type() 宏若兼做 sizeof 与 __alignof__ 即可支撑 auto __free 简洁写法；特例应拆行或写包装分配函数，反对把复杂分配摊成三行。 `<!-- ROW_MINE: ksummit.messages.6826 -->`
- 【Linux社区】Petersen 指内核已有 include/linux/cleanup.h，赞成清理属性用于部分错误处理，但需在 kfree 之外做更多时声明语法凌乱，反不如传统 goto 收尾可读。 `<!-- ROW_MINE: ksummit.messages.6888 -->`

## 180.6 GitLab 流程迁移争论

- 【Linux社区】Pinchart 归纳邮件流程真正价值：单客户端完成全部审查、可自由定制；设想一种人类可读、可被 mutt 与编辑器解析的类邮件结构化格式，作为渐进过渡路径。 `<!-- ROW_MINE: ksummit.messages.6827 -->`
- 【Linux社区】Pinchart 指出 GitLab 无法对提交说明行内评论，恐拉低提交信息质量；询问 Red Hat 审查数据入口是否仅限网页，并重申以邮件列表为传输层、结构化服务订阅的两全构想。 `<!-- ROW_MINE: ksummit.messages.6870 -->`

## 180.7 Link 标签与 lore 链接

- 【Linux社区】Geert 列举每日点击 lore 链接的场景：报 bug 找线程、查新增 Rb 标签、追溯同补丁早期提交；反对以 patchwork URL 充当 Link:，称多一步跳转且担心 freedesktop 域名消失。 `<!-- ROW_MINE: ksummit.messages.6828 -->`

## 180.8 fwctl 与 EDAC 之争

- 【Linux社区】Borislav 澄清建议把新 RAS 接口并入 EDAC 只是复用既有设施而非另立新框架；Cameron 仍担忧 fwctl 内先落地的窄功能日后如何泛化。 `<!-- ROW_MINE: ksummit.messages.6829 -->`

## 180.9 checkpatch 局限

- 【Linux社区】Brown 补充 checkpatch.pl 在 include/trace 的复杂宏上几乎全军覆没，架构代码与内联汇编同样易触发误报，宏自成一体的语言不宜套用内核惯例。 `<!-- ROW_MINE: ksummit.messages.6832 -->`

## 180.10 buffer_head 淘汰路线

- 【Linux社区】Wilcox 实测 Debian 上 buffer_head 每块 104 字节；逐 BH 置位判定在数十个 BH 后不扩展，提出仿 iomap 用状态位图拆分 BH，但大量代码假设同 folio 内 b_size 一致。 `<!-- ROW_MINE: ksummit.messages.6837 -->`

## 180.11 AI 生成内容守则

- 【Linux社区】Stoakes 给出工具生成内容文档修正案定稿：审查强度与生成比例成正比，作者须理解并能辩护全部提交，否则维护者可不经详审拒收；Rostedt 表示认可。 `<!-- ROW_MINE: ksummit.messages.6840 -->`

## 180.12 倦怠支持资源

- 【Linux社区】Bottomley 指社区几乎没有可调用的倦怠支持资源；Williams 分享请 Dr. Chance 跟进咨询、以线下协作减压；Shuah 计划 2026 导师系列纳入 Linux 职业导航并索取咨询使用数据。 `<!-- ROW_MINE: ksummit.messages.6843 -->`

## 180.13 API 弃用执行方案

- 【Linux社区】Biederman 提议在头文件用专用宏隐藏旧 API，新调用须显式定义方可编译，grep 宏名或改宏全量重编即可清点残留使用者，为大规模迁移铺路。 `<!-- ROW_MINE: ksummit.messages.6844 -->`

## 180.14 Rust 语义争论

- 【Linux社区】Overstreet 以 bcachefs 文件系统选项对象为例：C 中各选项无依赖可无同步裸读，转 Rust 须经 UnsafeCell 包装的 getter 表达内部可变性，访问规则显式化必然引入访问器。 `<!-- ROW_MINE: ksummit.messages.6847 -->`
- 【Linux社区】Ventura Jack 指出 Rust 尚无完整官方别名规范，stacked borrows 与 tree borrows 皆属实验模型，MIRI 无法全查且自认规则未定，rustc 独大经 LLVM 后端，gccrs 仍在开发。 `<!-- ROW_MINE: ksummit.messages.6930 -->`

## 180.15 linux-next 驻留时长

- 【Linux社区】Kozlowski 强调跨子系统驱动与 DTS 协作中补丁须尽早进 -next，上游维护者 rc6-rc7 即收敛树；Sasha 的 PR 驻留时长统计机器人因未获 Linus 反馈信号而停发。 `<!-- ROW_MINE: ksummit.messages.6848 -->`

## 180.16 Fixes 标签政策

- 【Linux社区】Sasha 披露 Fixes 回传与 AUTOSEL 由来：提交者不惯加 stable 标签，谷歌曾强制非新功能必带 Fixes；Linus 拒绝新增 Improves 标签，Sasha 问是否正式确立凡 Fixes 皆入 stable。 `<!-- ROW_MINE: ksummit.messages.6849 -->`
- 【Linux社区】Bottomley 引 handling-regressions.rst 现行规则：Fixes 标注元凶、跨开发周期修复另加 Cc: stable；主张先统一执行既有文档，勿再发明给更大自由度的新流程。 `<!-- ROW_MINE: ksummit.messages.6855 -->`

## 180.17 驱动 probe 设计澄清

- 【Linux社区】Greg KH 说明 probe 与驱动注册自 2.5 时代起即刻意解耦，probe 失败不应阻止模块加载，拒绝回到找不到设备即卸载的旧模型；Shuah 确认按设计去修 probe bug 即可。 `<!-- ROW_MINE: ksummit.messages.6853 -->`

## 180.18 高端内存淘汰调查

- 【Linux社区】Arnd 普查剩余 highmem 用户去留；Gunthorpe 提议移除仅 ARM 用的 kmap_high_get()；Geert 提醒 Microchip 会为新 DDR 重推旧 SoC，SAM9x7 的 256MB 上限未必恒定。 `<!-- ROW_MINE: ksummit.messages.6854 -->`

## 180.19 加速器驱动开源门槛

- 【Linux社区】Triplett 主张不强制全部用户态开源，但接口合入前须至少存在一个开源用户态使用者；Hansen 补充无开源用户态便无从有效测试调试，能提供自测是底线。 `<!-- ROW_MINE: ksummit.messages.6856 -->`

## 180.20 AI 审查提示词工程

- 【Linux社区】Kees Cook 向 Mason 请教 AI 审查提示词实践：反馈循环让模型自更新提示文件、从既有 bug 提炼模式库、按阶段丢弃非关键上下文以省 token，并关注 semcode MCP 工具。 `<!-- ROW_MINE: ksummit.messages.6858 -->`

## 180.21 Sphinx 版本下限

- 【Linux社区】Geert 佐证文档工具链困境：Ubuntu 20.04 LTS 仍只带 Sphinx 1.8.5，升级 22.04 才得 4.3.2，老发行版用户难以本地构建内核文档。 `<!-- ROW_MINE: ksummit.messages.6859 -->`

## 180.22 稳定版回归修复义务

- 【Linux社区】Leemhuis 提议主线新引入回归须随最新 stable 修复；Berg 强烈反对把稳定版责任压给维护者，称用户不能既不逐版测试又要求每版出修复。 `<!-- ROW_MINE: ksummit.messages.6861 -->`

## 180.23 b4 线程回填用法

- 【Linux社区】Ryabitsev 指导用 mutt 宏调用 b4 mbox 回填整线程，逐一澄清 maildir 自动识别、管道消息提取 message-id、mbox 与 am 命令区别，回应 Leon 的三个使用障碍。 `<!-- ROW_MINE: ksummit.messages.6862 -->`

## 180.24 Rust 内核政策

- 【Linux社区】Sakkinen 强调 Rust 内核政策必须写进内核树才具约束力，外部网页可被无视，并直言现行政策很糟糕。 `<!-- ROW_MINE: ksummit.messages.6863 -->`

## 180.25 安全 embargo 代码质量

- 【Linux社区】Sasha 发起新议题：embargo 代码直送绕过常规审查测试，硬件漏洞使其常态化；建议要求惯用方自建测试环境、组建可信测试者小组、与 KernelCI 和 OpenSSF 搭小型私有 CI。 `<!-- ROW_MINE: ksummit.messages.6873 -->`

## 180.26 引文礼仪之争

- 【Linux社区】Kozlowski 反驳 NeilBrown 的反讽：其客户端与 lore、patchwork 均无法跳过大段引文，只能人工翻找；并指 Rb/Ack 摆放位置不当，令后续意见难以辨认。 `<!-- ROW_MINE: ksummit.messages.6874 -->`

## 180.27 Werror 处置之争

- 【Linux社区】Boessenkool 自 2014 年起以未发布 GCC 构建内核，反对给 GCC 加环境变量忽略 -Werror，建议命令行加 -Wno-error 或统一走 CONFIG_WERROR，并指出补丁缩进与早退位置问题。 `<!-- ROW_MINE: ksummit.messages.6890 -->`

## 180.28 设备直通与相机 ISP

- 【Linux社区】Pinchart 称厂商可编程 ISP 多藏于固定管线固件之后，差异化在用户态算法，软件专利主要利好大厂；与 Leon 一致主张 UAPI 暴露的每项功能都应有开源对应实现。 `<!-- ROW_MINE: ksummit.messages.6891 -->`

## 180.29 AI 时代 ACL 需求

- 【Linux社区】Coly Li 详述 NAS 本地 AI 相册用例：用户凭人脸匹配可删公开目录中含本人影像的硬链接却无写权限，POSIX ACL 无法表达，现靠 eBPF 补丁硬凑，LSM 只能拒绝不能授权，故提峰会技术议题。 `<!-- ROW_MINE: ksummit.messages.6896 -->`

## 180.30 审查自动化减负

- 【Linux社区】Lunn 确认 Song Liu 所指即 patchwork Checks：netdevbpf 补丁到达即自动测试并亮灯，评审者可先过滤不值得看的补丁，并给出示例链接。 `<!-- ROW_MINE: ksummit.messages.6905 -->`

## 180.31 文件系统用户态化构想

- 【Linux社区】Overstreet 披露 bcachefs 垫片层已让约九成代码按行数在用户态运行以支持 fsck，设想 vfs 到 FUSE 的通用垫片让 reiserfs 等老文件系统整支转 FUSE，难点或需把 buffer_head 一并搬出。 `<!-- ROW_MINE: ksummit.messages.6910 -->`

## 180.32 bcachefs 事件反思

- 【Linux社区】Ts'o 把 bcachefs 争议比作人事问题，宜私下调解不宜公开；反对当初拒收即可避免祸端的说法，认为人际崩坏不可预判，也反对投票或核心团队准入制，预计维护者将更审慎。 `<!-- ROW_MINE: ksummit.messages.6911 -->`

## 180.33 AI 代码质量标准

- 【Linux社区】Sasha 主张对 AI 的门槛不应高于人类：LTS 树与 CVE 多为越界、UAF 等简单内存安全错误，恰是人类写 C 出错的活证据，AI 达到同等或更优水平即可接受。 `<!-- ROW_MINE: ksummit.messages.6912 -->`

## 180.34 trivial 树兴衰

- 【Linux社区】Kosina 回溯 trivial@ 树初衷是替子系统维护者消化琐碎补丁，如今他久未照料，赞成从文档删除该列表；多数补丁只是注释或 printk 的拼写修正。 `<!-- ROW_MINE: ksummit.messages.6917 -->`

## 180.35 linus-next 测试价值

- 【Linux社区】Chamberlain 论证 -next 价值：0-day 默认仅构建测试，-next 汇聚机器人与人工的运行时测试，覆盖罕见架构与配置，并能提前暴露合并冲突以便协调。 `<!-- ROW_MINE: ksummit.messages.6920 -->`

## 180.36 kernel.org 信任改造

- 【Linux社区】Greg KH 证实 kernel.org 正与 OpenSSF 合作替换自研 Web of Trust，2 月 LFMS 大会“第一人称维护者验证”场次已录视频，代码仓库链接待上传。 `<!-- ROW_MINE: ksummit.messages.6923 -->`

## 180.37 Rust 寄存器访问安全

- 【Linux社区】Ojeda 以 PL061 为例说明 Rust 封装 readb 安全在于地址由方法内部计算而非用户拼算，regmap 靠运行时检查而 Rust 编译期即查，并展示 memory_map! 宏自动生成寄存器读写与换算。 `<!-- ROW_MINE: ksummit.messages.6936 -->`
