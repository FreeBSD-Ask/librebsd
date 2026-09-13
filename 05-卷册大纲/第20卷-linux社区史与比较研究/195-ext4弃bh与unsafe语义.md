# 195. ext4 弃 buffer_heads、Linus unsafe 语义阐述与 ISP 归属激辩（ks p59）

> 来源：ksummit 独有 p59（50 封全读，2021-04 至 2026-08：Ts'o 一手详述 ext4 弃用 buffer_heads 三大动因及 folio 迁移破坏 bh_offset 回归案例兼论全树改动对 LTS 自动回移的阻碍；Ribalda 与 Pinchart 就 ISP 归 V4L2 还是 DRM 激辩含九成以上摄像头市场依赖树外驱动关键数据；Linus 对 unsafe 语义权威阐述程序员冒险与编译器冒险之别并与反 UB 优化立场构成 Rust 政策奠基性表述；Carpenter 复盘多起 AI 参与补丁真实案例含 grep FIXME 令 AI 实现与 AI 模糊测试戳穿不完整安全修复；Rust 未定义行为与 AI 代码审查双封、malloc 提案双封）
> 判定：45 CAND / 5 NV。主题分布：列表版面治理 1、缓冲缓存与大folio 1、THE REST收件分流 1、无符号警告之争 1、C++可行性论据 1、malloc提案 2、AI代码审查 2、旧文件系统用户态化 2、内核文档工具 1、Rust静态引用语义 1、Bugzilla改革 1、linux-next流程 2、C语言安全 1、Rust弱引用语义 1、UMN假补丁事件 1、项目延续文档 1、Link尾注替换 1、Rust文件布局 1、Rust抽象层生成 1、安全代码质检门槛 1、维护者峰会存废 1、TAB选举安排 1、Rust未定义行为 2、Rust补丁测试 1、安全披露渠道 1、ISP驱动框架之争 1、信任网重建 1、Folios之争 1、Sphinx构建依赖 1、UALink驱动布局 1、设备树绑定ABI 1、AI标注标签 1、文档构建性能 1、加速器用户态要求 1、AI政策讨论 1、缓冲缓存退役 1、回归追踪 1、评审激励机制 1、设备直通之争 1、补丁发送工具 1。

## 195.1 列表版面治理

- 【Linux社区】Ryabitsev 叫停峰会筹备线程中的防疫药物争论，警告将在其可控基础设施上启用过滤屏蔽，体现新版 ksummit 列表早期的版面整顿立场。 `<!-- ROW_MINE: ksummit.messages.9186 -->`

## 195.2 缓冲缓存与大folio

- 【Linux社区】Linus 评 Wilcox 设想：缓冲缓存理论上可为 256kB 大 folio 建非均匀 buffer_head，但从未实现与测试，也缺少相应 helper 函数。 `<!-- ROW_MINE: ksummit.messages.9190 -->`

## 195.3 THE REST收件分流

- 【Linux社区】Bonzini 质疑把“THE REST”改投 patches@ 的效果：大量 LKML 流量实为 git-send-email 默认配置所致，patches@ 现仅稳定队列在用。 `<!-- ROW_MINE: ksummit.messages.9191 -->`

## 195.4 无符号警告之争

- 【Linux社区】Linus 强硬主张内核必须禁用“无符号小于 0”警告：该警告催生错误强转与删检查等真 bug，并非安全网，称此立场不可谈判。 `<!-- ROW_MINE: ksummit.messages.9193 -->`

## 195.5 C++可行性论据

- 【Linux社区】Dobriyan 以实测否定 C++ 路线：g++ 要求 C99 初始化器按声明顺序且不支持 x86 的 __seg_gs；又指与 C 不源码兼容者（含 Rust）均非选项。 `<!-- ROW_MINE: ksummit.messages.9194 -->`

## 195.6 malloc提案

- 【Linux社区】Ojeda 回击 hpa“剔除 Rust”威胁：Rust 已支持可插拔分配器，实现 malloc 类接口无障碍，是 Rust 政策之争中的事实澄清。 `<!-- ROW_MINE: ksummit.messages.9196 -->`
- 【Linux社区】Wilcox 澄清提案是实现 1970 年代标准接口而非立新标准，未来或删 kvmalloc；指出 kzalloc_obj 配 GFP_NOWAIT 时小分配仍会失败的张力。 `<!-- ROW_MINE: ksummit.messages.9311 -->`

## 195.7 AI代码审查

- 【Linux社区】Brown 赞同 Linus 对 AI 审查报告摩擦的担忧，但主张将 AI 发现集中建库，类比 Coverity 模式，并提议挖掘重复报告模式而非散落各评审。 `<!-- ROW_MINE: ksummit.messages.9198 -->`
- 【Linux社区】Carpenter 复盘 CVE 审读实例：有人 grep FIXME 后令 AI 实现即冒充溢出修复，AI 模糊测试发现安全补丁不完整，呼吁提交说明写明 AI 用法与流程。 `<!-- ROW_MINE: ksummit.messages.9230 -->`

## 195.8 旧文件系统用户态化

- 【Linux社区】Overstreet 提出以 shim 层把旧文件系统整体搬入用户态 FUSE 运行，bcachefs 已实现约九成代码量用户态化，可免内核重构破坏并收窄安全面。 `<!-- ROW_MINE: ksummit.messages.9205 -->`
- 【Linux社区】Biederman 主张以 libguestfs 为起点运行旧文件系统：其已带 FUSE 支持并随主流发行版发布，可在 qemu 中跑内核挂载，关键在做到零摩擦可用。 `<!-- ROW_MINE: ksummit.messages.9213 -->`

## 195.9 内核文档工具

- 【Linux社区】Mauro 介绍 kernel-doc 已可全树解析，实测 make mandocs 约 44 秒、报数千警告，支持 Nikula 提议的 --lint-rst 检查，媒体 CI 以 W=1 零警告为目标。 `<!-- ROW_MINE: ksummit.messages.9212 -->`

## 195.10 Rust静态引用语义

- 【Linux社区】Ventura Jack 引 Rust 2024 版文档指出全局可变 static 引用即使在 unsafe 中也被强烈劝阻，回应 Linus“读全局标志还要 unsafe”的批评。 `<!-- ROW_MINE: ksummit.messages.9217 -->`

## 195.11 Bugzilla改革

- 【Linux社区】Leemhuis 澄清改革后的报告路径为按子系统邮件维护者，承认缺一级支持组并有意日后组建，但当前优先级较低。 `<!-- ROW_MINE: ksummit.messages.9220 -->`

## 195.12 linux-next流程

- 【Linux社区】Brown 指出子树修复若未进 -next，bug 会持续暴露至 PR 合入为止，子树孵化期与 PR 处理延迟都直接拉长问题在 -next 的可见时间。 `<!-- ROW_MINE: ksummit.messages.9225 -->`
- 【Linux社区】Roeck 指出 linux-next 及其 pending-fixes 分支的构建与测试失败基本无人理会，质疑以其作为 PR 健康信号的实际价值。 `<!-- ROW_MINE: ksummit.messages.9345 -->`

## 195.13 C语言安全

- 【Linux社区】Uecker 指出 C 安全化投入被低估：他业余修 GCC 无人跟进、内核未参与 ISO C 标准化，认为 C 有大量低成本安全改进空间且可建内存安全子集。 `<!-- ROW_MINE: ksummit.messages.9235 -->`

## 195.14 Rust弱引用语义

- 【Linux社区】Ojeda 以代码示例向 Geert 解释 Weak::upgrade 返回 Option：对象不存在时调用方根本无从访问成员，展示 Rust 所有权模型的安全保证。 `<!-- ROW_MINE: ksummit.messages.9238 -->`

## 195.15 UMN假补丁事件

- 【Linux社区】Figa 赞同 Hellwig 对明尼苏达大学实验的评价，称评审量不足是多年顽疾，UMN 本应引入社区监督并负责事后清理，其否认态度更令人担忧。 `<!-- ROW_MINE: ksummit.messages.9249 -->`

## 195.16 项目延续文档

- 【Linux社区】Linus 表示将绕过文档树亲自直接提交 Dan Williams 的“项目延续”流程文档，后续修订再走常规途径，属治理事件的当事人表态。 `<!-- ROW_MINE: ksummit.messages.9267 -->`

## 195.17 Link尾注替换

- 【Linux社区】Bottomley 反对集中 git notes 树承载子系统元数据：notes 设计上不适共享、需过滤且易污染本地用途，主张全局重要信息应写入提交树。 `<!-- ROW_MINE: ksummit.messages.9269 -->`

## 195.18 Rust文件布局

- 【Linux社区】Ojeda 回应 Lunn 关于文件搬移影响稳定树回移的顾虑：可先定好路径不再搬，或宣布 Rust 支持前两三个版本不回移，给树内成熟留时间。 `<!-- ROW_MINE: ksummit.messages.9274 -->`

## 195.19 Rust抽象层生成

- 【Linux社区】Bottomley 与 Ojeda 辨析自动 bindings 与手工抽象层之别，后者在 C API 变更时需人手维护；提出扩展 sparse 校验注记、bindgen 生成抽象以降摩擦。 `<!-- ROW_MINE: ksummit.messages.9278 -->`

## 195.20 安全代码质检门槛

- 【Linux社区】Levin 为 embargo 代码提议硬性测试清单：多版本 GCC 与 Clang、x86 与 arm64 等平台、allmodconfig 等配置及近月 LTP，未过不得悄悄合入。 `<!-- ROW_MINE: ksummit.messages.9281 -->`

## 195.21 维护者峰会存废

- 【Linux社区】Bottomley 披露峰会经费困境：2024 年一家赞助、2025 年零赞助、2026 年仍无，LF 自付与会礼品；Pinchart 估算约 43 人、人均约 2500 美元。 `<!-- ROW_MINE: ksummit.messages.9282 -->`

## 195.22 TAB选举安排

- 【Linux社区】Corbet 解释 TAB 章程把投票绑在内核峰会即 LPC 期间，Babka 因会期漏看 CIVS 邮件错过投票，Corbet 称可修章程把选举移至年内平静时段。 `<!-- ROW_MINE: ksummit.messages.9287 -->`

## 195.23 Rust未定义行为

- 【Linux社区】Linus 请 Rust 社区避免 C 式 UB 优化模型：要么朴素代码生成要么明确警告，举 WG14 N3203 收紧未定义行为为例，称潜在优化不值得代价。 `<!-- ROW_MINE: ksummit.messages.9288 -->`
- 【Linux社区】Linus 阐明 unsafe 的本义是让源码有意绕过规则而非授权编译器重排访问，以分配器指针运算为例，要求编译器不能证明不别名就不要假设。 `<!-- ROW_MINE: ksummit.messages.9363 -->`

## 195.24 Rust补丁测试

- 【Linux社区】Airlie 坦言 Rust DMA 补丁两难：跨子系统完整系列无人肯审、无用户系列遭拒，故先走后者；Sakkinen 接受以含测试的 git 分支自行验证。 `<!-- ROW_MINE: ksummit.messages.9302 -->`

## 195.25 安全披露渠道

- 【Linux社区】Kosina 反驳以用户数论 Android 主导：证交所、空管、NASA 等企业级部署经由 Red Hat、SUSE 等供养内核开发，且 Fedora 与 openSUSE 并不用 LTS 基线。 `<!-- ROW_MINE: ksummit.messages.9303 -->`

## 195.26 ISP驱动框架之争

- 【Linux社区】Ribalda 力主 ISP 归 DRM：指 V4L2 路线致九成以上摄像头市场依赖树外驱动、用户仅剩 Android；Pinchart 坚持开放用户态覆盖要求，双方激辩命令缓冲与文档义务。 `<!-- ROW_MINE: ksummit.messages.9304 -->`

## 195.27 信任网重建

- 【Linux社区】Greg 证实 kernel.org 正与 OpenSSF 合作替换自研 PGP 信任网：旧方案有瓶颈与扩展性局限，新框架预计二月会议公布，工作仍在进行。 `<!-- ROW_MINE: ksummit.messages.9320 -->`

## 195.28 Folios之争

- 【Linux社区】Overstreet 评 folios 争论走偏：Willy 阐述不力、部分 MM 反对无理，澄清 folios 面向文件系统页而非 slab，与 Johannes 讨论出拆分 struct page 思路并等其撤 NACK。 `<!-- ROW_MINE: ksummit.messages.9321 -->`

## 195.29 Sphinx构建依赖

- 【Linux社区】Yokosawa 实测发现 openSUSE Leap 15.4 的 Sphinx LaTeX 包缺 Sphinx 4.0 起必需的 tex-gyre 字体，Fedora 36 与 RHEL 9 均覆盖，拟向 openSUSE 报 bug。 `<!-- ROW_MINE: ksummit.messages.9322 -->`

## 195.30 UALink驱动布局

- 【Linux社区】Intel 的 Sinyuk 确定 UALink 驱动落位：先入 drivers/accel/ual 而非 misc，长期独立为 drivers/ual；Greg 说明 staging 不适合有活跃社区的新子系统。 `<!-- ROW_MINE: ksummit.messages.9328 -->`

## 195.31 设备树绑定ABI

- 【Linux社区】ÜNAL 主张设备树绑定文档修改不必连带驱动改动，Herring 反驳需同改两侧即已破坏 ABI 且顺序不可二分；ÜNAL 转而接受先修驱动的次序。 `<!-- ROW_MINE: ksummit.messages.9329 -->`

## 195.32 AI标注标签

- 【Linux社区】Howlett 赞同 Assisted-by 标签改记 AI 使用方式而非模型名，认为随使用普及原标签价值趋零，知名开发者更该用 RFC 标签请求重点审查。 `<!-- ROW_MINE: ksummit.messages.9339 -->`

## 195.33 文档构建性能

- 【Linux社区】Corbet 剖析 Sphinx C 域符号树约七亿次迭代调用的 O(n²) 行为，改字典查找使 htmldocs 提速约 20%，叠加 automarkup 优化合计约 27%。 `<!-- ROW_MINE: ksummit.messages.9342 -->`

## 195.34 加速器用户态要求

- 【Linux社区】Airlie 阐述 DRM 开源用户态要求：加速器 uAPI 复杂多线程绝非小测试程序可覆盖，社区靠拒绝与教育建成，正起草跨子系统通用文档分支。 `<!-- ROW_MINE: ksummit.messages.9364 -->`

## 195.35 AI政策讨论

- 【Linux社区】Stoakes 点出 AI 生成与人工审查成本严重不对称是核心矛盾，故主张 AI 辅助补丁必须自愿加入，并赋权各维护者自行决定取舍。 `<!-- ROW_MINE: ksummit.messages.9367 -->`

## 195.36 缓冲缓存退役

- 【Linux社区】Ts'o 详述 ext4 拟弃用 buffer_heads 三因：元数据缓存控制、写回失败无回调、内存开销；folio 改动破坏 bh_offset 被测试抓获属正常，全树改动还阻碍 LTS 回移。 `<!-- ROW_MINE: ksummit.messages.9370 -->`

## 195.37 回归追踪

- 【Linux社区】Leemhuis 申请在维护者峰会作约五分钟回归追踪现状报告，含优秀子系统经验与 regzbot 进展，并讨论 bugzilla+bugbot+bugspray 下 regzbot 的去留。 `<!-- ROW_MINE: ksummit.messages.9375 -->`

## 195.38 评审激励机制

- 【Linux社区】Kara 回应 Nossum 的评审激励错位分析：根本动力是共同责任感，避免劣质代码进入自己所在子系统；激励与互审只是辅助，公地悲剧需靠认同化解。 `<!-- ROW_MINE: ksummit.messages.9381 -->`

## 195.39 设备直通之争

- 【Linux社区】Bottomley 以史立论：Oracle 曾索要 SCSI 裸设备终被 direct I/O 化解，SPDK/DPDK 仍属小众，USB 令牌统一为 CTAP；够大的用例终被内核吸收，fwctl 宜定位慢速配置面。 `<!-- ROW_MINE: ksummit.messages.9383 -->`

## 195.40 补丁发送工具

- 【Linux社区】Glass 介绍 patman 可为每版补丁维护变更日志并一键发送、欢迎功能补丁；Romanovsky 自述另有包装 git format-patch 按目标树自动设收件人的脚本。 `<!-- ROW_MINE: ksummit.messages.9385 -->`
