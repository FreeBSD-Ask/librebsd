# 42 【Linux社区】API废弃节奏与embargo之辨

> 对应页面：ksummit-discuss p95（pk 348956-349005，2018 API 废弃/embargo/lockdown 多线程 + 2014 档案，2 封纯寒暄 NV）
> 判定：48 CAND / 2 NV
> 编号：DSLXC-5731..5778 | claim 已入库（48/48，dslinux_claims.duckdb）

## 42.1 【Linux社区】API 废弃与转换节奏（8 例）

**要点（判定表逐字）**：Kees Cook 开题 API 废弃的快（N 引入 N+1 移除、timer_setup、kmalloc_array）慢（strscpy、VLA）两法，列 strcpy 2490 处、strncpy 865、strlcpy 2361、strscpy 仅 29 的实测数字；Stephen Rothwell 以 linux-next 维护者身份指证：每次用超快法（同周期全转换并删旧接口）都会同时引入旧接口的新用户，呼吁参与讨论；Julia Lawall 建议走中等路线：采快法但不立即删旧函数（如 devm 函数起步极慢），以免无人可见便无人采用、终至永不弃用；Julia Lawall 指已有 Coccinelle 脚本针对 DRM 欲弃函数定期触发报告，既示应做何事也示不应做何事，可做成只增函数名的通用脚本；Geert Uytterhoeven 打趣不知 VLA 也算内核 API，附 Linus 名句 hacker 自谓；Kees Cook 回 Geert：VLA 只是 shorthand，涵盖一切用法模式，读者自明其意；Geert Uytterhoeven 补：加 -Werror=vla 后 VLA 问题与废弃等价，初以为差别大；Kees Cook 提两路：社会契约（各维护者议定不添废弃函数、写入 Documentation/process/deprecated.rst、责任归作者与维护链）与未来 CI（跟 linux-next 做 allmodconfig 等机械检查、可 curl kernelci 查 SHA 通过否）

**史料**：`348961`、`348963`、`348967`、`348969`、`348975`、`348986`、`348987`、`348988`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348961 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348963 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348967 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348969 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348975 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348986 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348987 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348988 -->` 

**史观**：知识注定过时（总纲第 22 条——知识注定过时：API 废弃之议正是接口知识新陈代谢的节律，快法（N 引入 N+1 移除）与慢法（strscpy、VLA）各承其代价）；经验优先（总纲第 9 条——经验优先：以 Kees Cook 实测的 strcpy 2490 处、strncpy 865、strlcpy 2361、strscpy 仅 29 为判据）
**辨析**：Stephen Rothwell 以 linux-next 维护者身份指证的“每次用超快法都会同时引入旧接口的新用户”为可核之实况；Julia Lawall 的“采快法但不立即删旧函数，以免无人可见便无人采用、终至永不弃用”为路径主张；Kees Cook 的“社会契约（写入 Documentation/process/deprecated.rst）与未来 CI（跟 linux-next 做 allmodconfig 等机械检查）两路并行”为提案；Geert Uytterhoeven 的“加 -Werror=vla 后 VLA 问题与废弃等价”为其实测之得。本页未见决议。
**文献**：DSLXC-5736、DSLXC-5738、DSLXC-5742、DSLXC-5744、DSLXC-5750、DSLXC-5761、DSLXC-5762、DSLXC-5763（`ksummit-discuss.messages.348961`、`ksummit-discuss.messages.348963`、`ksummit-discuss.messages.348967`、`ksummit-discuss.messages.348969`、`ksummit-discuss.messages.348975`、`ksummit-discuss.messages.348986`、`ksummit-discuss.messages.348987`、`ksummit-discuss.messages.348988`，2018-09-05、2018-09-05、2018-09-06、2018-09-06、2018-09-06、2018-09-06、2018-09-06、2018-09-06），全文见 `raw_source.raw_json`

## 42.2 【Linux社区】embargo 开发与上游优先（14 例）

**要点（判定表逐字）**：Rodrigo Vivi 披露 Intel 显卡 embargo 开发四点痛点：基于 LTS 变基将致未来重写、需持续备妥上游补丁、上游导向挤占复查质量、内部已带 Reviewed-by 上公共列表引发新问题；Linus Walleij 述 SoC embargo 经验：组件分 embargo/非 embargo、管理层给定解除 embargo 截止日、用高上游经验者内部复查、最小化与主线的汉明距离（宁变基 -rcN 或 linux-next）；Jani Nikula 赞 Linus Walleij 的 embargo 要点，指出既要求内部复查又频繁变基的矛盾：变基十余次后已非当初被复查之版本，质询内部补丁应要求多精；Arnd Bergmann 补反向截止日：面向具体软件产品集成时，代码公开的最迟时点亦须有 deadline（依发行版或硬件日程），以便估是否赶得上；Mark Brown 指 i915 这类划分不清的驱动更难做 embargo 分类，而独立芯片或 SoC 因驱动各自分离较易切分上游；Linus Walleij 述采购流程：曾要求第三方硬件商提供上游支持策略并先发初版补丁方予采购，谓 firm 胜于 hard，Jon Masters 与 Chromebook 亦持上游优先；Mark Brown 自组件商角度印证上游优先好处：与社区协作集成问题多在对方，长期支持与升级更稳，客户虽不自带上游也受益；Thomas Gleixner 补澄清：KABI 乱局本由发行版自引、成营收大头，预警者被忽视；若不影响上游、不逼垮维护者则不在乎，但无人可补偿濒临倦怠的工程师；Sean Paul 证 Chromebook 显示栈必走 drm/kms、补丁先上游再落地，4.14 分支多标 UPSTREAM/BACKPORT/FROMGIT/FROMLIST，下游工作分支定期变基；Leon Romanovsky 述 RDMA 早决基于 Linus 最新 -rc、设专人负责制上游发送并鼓励原开发者回评，借内部重组消解 Rodrigo 四点痛点，弃 staging 以免 lustre 噩梦；Jiri Kosina 论 embargo 安全事件处理：Meltdown/Spectre/L1TF 暴露我们尚无 sane 流程，提议如何适配流程、如何向不负责任 embargo 的公司施压；Jon Masters 要求 Arm 服务器厂商先发上游补丁并启用方能进 RHEL，已从贴出放宽到须入 linux-next，下一步须入 linux-next 或合入并落 Fedora，逼其如 Intel Xeon 般守规矩；Rodrigo Vivi 原发 Plumbers 提案“Unveiling Intel Graphics Internal Development”，欲谈 embargo 对上游开发的工具挑战与流程，觅走廊 track 或 BOF；Rodrigo Vivi 谢 Linus Walleij 并深论：常变基比偶变基更便宜、BOT 禁用一周即后悔；关键在 CI（drm-tip 每补丁预/后合并 CI、内部分支每变基点 CI）

**史料**：`348960`、`348971`、`348976`、`348978`、`348980`、`348981`、`348982`、`348983`、`348984`、`348985`、`348991`、`348993`、`348994`、`349003`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348960 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348971 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348976 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348978 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348980 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348981 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348982 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348983 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348984 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348985 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348991 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348993 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348994 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349003 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Rodrigo Vivi 披露的 Intel 显卡 embargo 四点痛点、Linus Walleij 的 SoC embargo 经验、Mark Brown 的组件商视角并置，未替任一方定论）；经验优先（总纲第 9 条——经验优先：以 Linus Walleij 的“最小化与主线的汉明距离（宁变基 -rcN 或 linux-next）”、Sean Paul 的“4.14 分支多标 UPSTREAM/BACKPORT/FROMGIT/FROMLIST”等实践为判据）
**辨析**：Jani Nikula 的“既要求内部复查又频繁变基的矛盾：变基十余次后已非当初被复查之版本”为机制性质问；Arnd Bergmann 的“反向截止日（代码公开的最迟时点亦须有 deadline）”为对 Linus Walleij 单一截止日的补全；Jon Masters 的“已从贴出放宽到须入 linux-next”为其采购门槛之自陈；Thomas Gleixner 的“KABI 乱局本由发行版自引、成营收大头，预警者被忽视”为其归因，与其自陈的“若不影响上游、不逼垮维护者则不在乎”并置。各说未作单方裁断。
**文献**：DSLXC-5735、DSLXC-5746、DSLXC-5751、DSLXC-5753、DSLXC-5755、DSLXC-5756、DSLXC-5757、DSLXC-5758、DSLXC-5759、DSLXC-5760、DSLXC-5766、DSLXC-5768、DSLXC-5769、DSLXC-5777（`ksummit-discuss.messages.348960`、`ksummit-discuss.messages.348971`、`ksummit-discuss.messages.348976`、`ksummit-discuss.messages.348978`、`ksummit-discuss.messages.348980`、`ksummit-discuss.messages.348981`、`ksummit-discuss.messages.348982`、`ksummit-discuss.messages.348983`、`ksummit-discuss.messages.348984`、`ksummit-discuss.messages.348985`、`ksummit-discuss.messages.348991`、`ksummit-discuss.messages.348993`、`ksummit-discuss.messages.348994`、`ksummit-discuss.messages.349003`，2018-09-05、2018-09-06、2018-09-06、2018-09-06、2018-09-06、2018-09-06、2018-09-06、2018-09-06、2018-09-06、2018-09-06、2018-09-06、2018-09-06、2018-09-04、2018-09-06），全文见 `raw_source.raw_json`

## 42.3 【Linux社区】稳定树节奏、维护者信任与峰会改址（6 例）

**要点（判定表逐字）**：Jiri Kosina 辨析纳入主线所需信任（专注开发）与纳入稳定树所需信任（专注稳定）是维护者两种不等同的素质，回应 Sasha Levin 关于稳定树标记的争论；Justin Forbes 应 Greg KH 谈稳定树节奏：今年因 spectre/meltdown 等安全乱局发布翻倍成常态，倾向每周一版（严重安全例外），反对固定星期几以免泄露带外信息；Eduardo Valentin 论稳定树固定节奏：同意每周一版但须保留 meltdown/spectre/L1TF 类带外发布；建议每周多个 stable-rc 末了一版定稿，仿 Linus 节奏；Benjamin Gilbert 列 CoreOS Container Linux 今年 11 个 4.14.x 中 5 个有用户级回归：vxlan panic、xen-netfront 设 MTU 失败、hv_netvsc 起不来、TCP 接收窗口整数溢出、CIFS 坏、ext4 大于 3TB 挂载失败；Thomas Gleixner 驳 Steven Rostedt 的 Stable Kernel ABI 必须付费神话：斥为 decades old distro fairy tale，谓老内核虽是营收来源，但依赖此的厂商已近死核之态；Ted Ts'o 公告维护者峰会改址爱丁堡（10-22 下午、约 30 人邀约制、谈流程非技术），因 Linus 误记档期并已排家庭假期；Kernel Summit 技术场仍在温哥华随 Plumbers

**史料**：`348958`、`348959`、`348964`、`348966`、`348970`、`348989`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348958 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348959 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348964 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348966 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348970 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348989 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Jiri Kosina 的“纳入主线所需信任（专注开发）与纳入稳定树所需信任（专注稳定）是两种不等同素质”与 Justin Forbes、Eduardo Valentin 的节奏主张并置）；经验优先（总纲第 9 条——经验优先：以 Benjamin Gilbert 列出的 CoreOS Container Linux 今年 11 个 4.14.x 中 5 个有用户级回归（vxlan panic、xen-netfront 设 MTU 失败、hv_netvsc 起不来、TCP 接收窗口整数溢出、CIFS 坏、ext4 大于 3TB 挂载失败）为判据）
**辨析**：Thomas Gleixner 的“驳 Steven Rostedt 的 Stable Kernel ABI 必须付费神话，斥为 decades old distro fairy tale”“谓老内核虽是营收来源，但依赖此的厂商已近死核之态”为其顶层判词；Eduardo Valentin 的“每周多个 stable-rc 末了一版定稿，仿 Linus 节奏”为流程主张；Ted Ts'o 的“峰会改址爱丁堡，因 Linus 误记档期并已排家庭假期”为可核之事由陈述，未涉评价。
**文献**：DSLXC-5733、DSLXC-5734、DSLXC-5739、DSLXC-5741、DSLXC-5745、DSLXC-5764（`ksummit-discuss.messages.348958`、`ksummit-discuss.messages.348959`、`ksummit-discuss.messages.348964`、`ksummit-discuss.messages.348966`、`ksummit-discuss.messages.348970`、`ksummit-discuss.messages.348989`，2018-09-05、2018-09-05、2018-09-06、2018-09-06、2018-09-06、2018-09-06），全文见 `raw_source.raw_json`

## 42.4 【Linux社区】lockdown 与设备错误处理（8 例）

**要点（判定表逐字）**：Justin Forbes 述 Fedora 在 4.17 rawhide 跑 CONFIG_LOCK_DOWN_KERNEL 竟无人察觉安全启动关闭，列 CONFIG_LOCK_DOWN_MANDATORY 与 CONFIG_LOCK_DOWN_IN_EFI_SECURE_BOOT；认同 Andy Lutomirski 拆分精简补丁集（先并入单一切换点再逐个加用户）的路线；Benjamin Herrenschmidt 谈设备错误处理：Power 测 EEH 时驱动错误路径极少测，硬件隔离后 MMIO 回 0xff 致超时循环拉长，建议加错误注入把 MMIO 重映射为回 0xff 以查找修复；Jani Nikula 以调试直连 PCI bar 的 -EPERM 为例，问 lockdown 是否考虑对拦截的访问记审计日志，忧其悄然改变行为难排查；David Howells 答 Jani：lockdown 拦截会在 dmesg 记一行说明拒绝原因；Jani Nikula 回应 David Howells：看来 dmesg 日志是后来加的，该用户当时跑的 lockdown 尚缺此功能；Benjamin Herrenschmidt 谈 Power 为非虚拟化系统走 IOMMU bypass 以省性能开销，主张应有通用（而非各 IOMMU 自搞）的按适配器配置策略；Benjamin Herrenschmidt 答 Roland Dreier：无驱动设备在 pci_enable_device 前不开 PCI 命令位故不能作主；认同 VT-d 现状令发行版默认不用可惜；joeyli 提 lockdown 细粒度解锁：以可信密钥环（内核内置或 MOK）验签的授权函数清单 blob 解锁单项，加时间戳防重放；认同 Andy 先简起步入主线

**史料**：`348956`、`348968`、`348972`、`348974`、`348977`、`348979`、`348990`、`348992`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348956 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348968 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348972 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348974 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348977 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348979 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348990 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348992 -->` 

**史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：lockdown 的细粒度解锁与审计日志之争，实为发行版合规义务与用户可诊断性的利益划分）；分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：Andy Lutomirski 与 Justin Forbes 的“先并入单一切换点再逐个加用户”与 joeyli 的“可信密钥环验签解锁单项”同向，正是补丁集分合的相位）
**辨析**：Justin Forbes 的“Fedora 在 4.17 rawhide 跑 CONFIG_LOCK_DOWN_KERNEL 竟无人察觉安全启动关闭”为其实测经验；Jani Nikula 的“以调试直连 PCI bar 的 -EPERM 为例，问 lockdown 是否考虑对拦截的访问记审计日志”与 David Howells 的“lockdown 拦截会在 dmesg 记一行说明拒绝原因”相对，Jani 复以“该用户当时跑的 lockdown 尚缺此功能”澄清时点差异，属事实层往复；Benjamin Herrenschmidt 的“主张应有通用（而非各 IOMMU 自搞）的按适配器配置策略”为设计主张，本页未见决议。
**文献**：DSLXC-5731、DSLXC-5743、DSLXC-5747、DSLXC-5749、DSLXC-5752、DSLXC-5754、DSLXC-5765、DSLXC-5767（`ksummit-discuss.messages.348956`、`ksummit-discuss.messages.348968`、`ksummit-discuss.messages.348972`、`ksummit-discuss.messages.348974`、`ksummit-discuss.messages.348977`、`ksummit-discuss.messages.348979`、`ksummit-discuss.messages.348990`、`ksummit-discuss.messages.348992`，2018-09-05、2014-05-14、2018-09-06、2018-09-06、2018-09-06、2014-05-14、2014-05-14、2018-09-06），全文见 `raw_source.raw_json`

## 42.5 【Linux社区】接班人计划与群维护之议（7 例）

**要点（判定表逐字）**：James Bottomley 以 Linus 误记峰会档期为由开接班人计划题：建议由维护者峰会与会者投票选新领袖（纯理论）；Daniel Vetter 反问为何单一领袖：小组维护制 work，倾向群维护；James Bottomley 偏好单一领袖以免 BSD 式小圈子崇拜，但承认若有避坑方案可试；指群维护似仅在 DRM 见效，他子系统多层级单领袖；Jiri Kosina 论 rebase 破 SUSE 工作流：其树按 git 拓扑序与上游 1:1 映射，rebase 毁映射，scsi 等树不得不视维护者树已够上游而绕过 Linus 合并；Linus Torvalds 笑接：正因如此才最好趁他去温哥华时（不在场）发动宫变，最合传统；Geert Uytterhoeven 补 Arm-soc 由三头目轮值发 pull request，证群维护非仅 DRM；Olof Johansson 论群维护亦可能失调但比单选错领袖更易调整，指 x86 亦由数人分担（arm-soc 初仿其模型），更高维护角色宜有产业平衡

**史料**：`348995`、`348996`、`348997`、`348998`、`348999`、`349000`、`349004`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348995 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348996 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348997 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348998 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348999 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349000 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349004 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以 James Bottomley 的“由维护者峰会与会者投票选新领袖”、Daniel Vetter 的“小组维护制 work”、Olof Johansson 的 arm-soc 三头目轮值为分析单位）；本体论上各方平等（总纲第 8 条——本体论上各方平等：Bottomley 的“偏好单一领袖以免 BSD 式小圈子崇拜”与 Vetter 的“倾向群维护”、Johansson 的“群维护亦可能失调但比单选错领袖更易调整”并置）
**辨析**：本块以宫变戏谑为外壳，Linus Torvalds 的“正因如此才最好趁他去温哥华时（不在场）发动宫变，最合传统”为当事人自嘲，非史家判断；Bottomley 的“指群维护似仅在 DRM 见效，他子系统多层级单领袖”与 Geert Uytterhoeven 的“补 Arm-soc 由三头目轮值发 pull request，证群维护非仅 DRM”相对，属反例对撞；Jiri Kosina 的“其树按 git 拓扑序与上游 1:1 映射，rebase 毁映射”为技术约束之陈。本页未见定论。
**文献**：DSLXC-5770、DSLXC-5771、DSLXC-5772、DSLXC-5773、DSLXC-5774、DSLXC-5775、DSLXC-5778（`ksummit-discuss.messages.348995`、`ksummit-discuss.messages.348996`、`ksummit-discuss.messages.348997`、`ksummit-discuss.messages.348998`、`ksummit-discuss.messages.348999`、`ksummit-discuss.messages.349000`、`ksummit-discuss.messages.349004`，2018-09-06、2018-09-06、2018-09-06、2018-09-06、2018-09-06、2018-09-06、2018-09-06），全文见 `raw_source.raw_json`

## 42.6 【Linux社区】staging 毕业、GPIO 治理、补丁元数据与严保护（5 例）

**要点（判定表逐字）**：Li Zefan 就 Takashi Iwai 的提交元数据构想补充：与其在变更日志加 Fixes 指认引入 bug 的提交，不如给原提交加元数据指向后续修复，便于向旧内核反向移植时一键查询；Joe Perches 指 staging 代码毕业至主线树时应更早拉入名义维护者评审，举 netdev 一处合并前评审不足为例；Linus Walleij 述 GPIO 描述符去全局编号（受 IRQ 去全局编号启发），谢 Arnd 删 blackfin 等怪架构与 0day kbuild 纠错加速推进，谓仍不快；Steven Rostedt 提议在 kernel.org 跑脚本或零日机器人，对新提交（及 LKML 补丁）中新增的废弃函数如 strcpy 自动发难邮件，弥补并非人人跑最新 checkpatch；Benjamin Herrenschmidt 论笔记本/桌机最廉硬件最该默认严保护模型（且易遭 ExpressCard 窃数），受控机房高端适配器则或因性能关 IOMMU

**史料**：`348957`、`348962`、`348973`、`348965`、`349001`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348957 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348962 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348973 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348965 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349001 -->` 

**史观**：知识注定过时（总纲第 22 条——知识注定过时：Li Zefan 的“给原提交加元数据指向后续修复，便于向旧内核反向移植时一键查询”与 Steven Rostedt 的“对新提交中新增的废弃函数自动发难邮件”，皆为对抗知识过时的机制设计）；分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：staging 代码毕业至主线树、GPIO 描述符去全局编号，正是暂存与子系统之间的分合相位）
**辨析**：Joe Perches 的“staging 代码毕业至主线树时应更早拉入名义维护者评审，举 netdev 一处合并前评审不足为例”为其程序主张；Linus Walleij 的“谢 Arnd 删 blackfin 等怪架构与 0day kbuild 纠错加速推进，谓仍不快”为当事人自陈；Benjamin Herrenschmidt 的“笔记本／桌机最廉硬件最该默认严保护模型（且易遭 ExpressCard 窃数），受控机房高端适配器则或因性能关 IOMMU”为其权衡之判。各说未作单方裁断。
**文献**：DSLXC-5732、DSLXC-5737、DSLXC-5748、DSLXC-5740、DSLXC-5776（`ksummit-discuss.messages.348957`、`ksummit-discuss.messages.348962`、`ksummit-discuss.messages.348973`、`ksummit-discuss.messages.348965`、`ksummit-discuss.messages.349001`，2014-05-14、2018-09-05、2018-09-06、2018-09-06、2014-05-14），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（6 块，覆盖 48/48 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
