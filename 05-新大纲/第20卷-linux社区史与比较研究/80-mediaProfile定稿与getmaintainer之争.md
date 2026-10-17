# 80 【Linux社区】mediaProfile定稿与getmaintainer之争

> 来源：ksummit-discuss p132（50 封全读，2019-09-13/21 MEP 收束段+media profile v2 评审链+W=1 数据战，夹杂 2014-05 档案信）
> 判定：49 CAND / 1 NV。主题分布：应用时静默修 1、W=1数据长文 1、MauroW=0主张 1、KS2014档案-列表上限 1、KS2014档案-EFI测试 1、2010提案自引 1、gcc9无差异 1、Petersen受众论 1、全系列到列表 1、Fixes标签局限 1、Jani文档累积批评 1、checkpatch配置化 1、gitnotes折中 1、供应商大系列 1、供应商不分树 1、KS2014档案-TODO 1、ViroMUA现实 1、DougMUA回应 1、Kees单目录提议 1、Mauro存储投票 1、Kees让步赞赏 1、不特别原则 1、MauroReST方案 1、Pinchart评审 1、Mauro修订 1、mediaProfilev2 1、KS2014档案-cgit 1、+++问 1、Pinchart二轮 1、KeesReST构建 1、awk方案 1、CC与自动化 1、Helgaas细问 1、getmaintainer至上 1、分散存储 1、fixes增强 1、dimfixes演示 1、KS2014档案-gatekeeper 1、dim局限 1、接受至上 1、dim源码公开 1、HerringCI细节 1、拆分旧案 1、Brown离线标签 1、Vetter拆分提议 1、LKMLdevnull 1、LKML可发现性 1、Jani流量数据 1、KS2014档案-cgit回应 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p132（实锚 pk 350806-350855）的逐封提取（49 CAND / 1 NV），全 49 块采用**单行摘要体例**（丙型）：每块由“## 80.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 80.1 【Linux社区】应用时静默修

- 【Linux社区】Geert：“我理解 differently——以为是 sub: system: 大小写；小事我应用时就改——比抱怨再数周后验证下版更省事” `<!-- ROW_MINE: ksummit-discuss.messages.350806 -->`

## 80.2 【Linux社区】W=1数据长文

- 【Linux社区】Perches 实测：ARM W=1 dts 警告 69,164 条（“dts[i] 移 W=2 合理”）；x86-64 gcc8.3 非 kernel-doc W=1 约 300 条（missing-prototypes 163/unused-but-set 69/empty-body 16…）；kernel-doc 约 1000 条逐文件清单 `<!-- ROW_MINE: ksummit-discuss.messages.350808 -->`

## 80.3 【Linux社区】MauroW=0主张

- 【Linux社区】Mauro：“~300 条不算多（gcc-9 或更多）——可提升到 W=0；kernel-doc 警告多现于 make htmldocs——不在 W=0 使清除很难；建议 W=0 对 kernel-doc 标签文件默认开 kernel-doc -none（实测 165 警告）” `<!-- ROW_MINE: ksummit-discuss.messages.350809 -->`

## 80.4 【Linux社区】KS2014档案-列表上限

- 【Linux社区】Kerrisk 感谢 Ted 将 ksummit-discuss moderation 前抄送上限提到 50（2014-05-03） `<!-- ROW_MINE: ksummit-discuss.messages.350810 -->`

## 80.5 【Linux社区】KS2014档案-EFI测试

- 【Linux社区】Fleming：“哪些测试坏了？tools/testing/selftests 的 EFI 测试正常——我合并变更时定期跑”；“Go for it!”（为 Greg 的测试维护试验放行） `<!-- ROW_MINE: ksummit-discuss.messages.350811 -->`

## 80.6 【Linux社区】2010提案自引

- 【Linux社区】Herring：Perches 近十年前已提议 MAINTAINERS 加 subject 前缀文法（lore 链接）；“现在支持或许多些——立场从 who cares 到 good idea；本想实现但 perl 只会改 checkpatch” `<!-- ROW_MINE: ksummit-discuss.messages.350812 -->`

## 80.7 【Linux社区】gcc9无差异

- 【Linux社区】Perches：“gcc-9.1 产生同样输出”（163/69/16 清单不变）；“总体同意大多易移除——只差时间清 missing-prototypes 与 unused-but-set 后即可默认启用” `<!-- ROW_MINE: ksummit-discuss.messages.350813 -->`

## 80.8 【Linux社区】Petersen受众论

- 【Linux社区】Petersen：“我的文档基本无 SCSI 专属内容（除分支命名）；刻意不提风格——20+ 年积尘不可能管、只要求新代码跟 coding-style.rst”；“原目标读者=硬件公司新驱动贡献者——他们不懂 merge window；这该是全球共同指南+维护者自留裁量” `<!-- ROW_MINE: ksummit-discuss.messages.350814 -->`

## 80.9 【Linux社区】全系列到列表

- 【Linux社区】Petersen：“我偏好整个系列发 linux-scsi 或 target-devel——树级变更讨论常发生在其他子系统补丁的回复里、不落到 linux-scsi”；“不引入新警告我完全支持”；“希望准则材料活在 Documentation/process” `<!-- ROW_MINE: ksummit-discuss.messages.350815 -->`

## 80.10 【Linux社区】Fixes标签局限

- 【Linux社区】Carpenter：“Fixes 标签不管用？你从没问过我们 kernel-newbies——我们也不知道答案；net 的树判定我尽力仍常搞错” `<!-- ROW_MINE: ksummit-discuss.messages.350816 -->`

## 80.11 【Linux社区】Jani文档累积批评

- 【Linux社区】Jani：“我们善累积不善清理——Documentation/process 已 11k 行；我更愿看到精简友好的贡献指南而非更多规则（还是子系统专属）；连我都没读完 process”；“profile 只对已 get it 的人有用”；MAINTAINERS 2000+ 条目若 10% 加 profile 是巨量文档；B: 19 条 C: 7 条且只有 networking 标注邮件偏好 `<!-- ROW_MINE: ksummit-discuss.messages.350817 -->`

## 80.12 【Linux社区】checkpatch配置化

- 【Linux社区】Jani：“子系统专属 checkpatch 规则完全可加进 MAINTAINERS 条目或目录配置文件——直接作为选项如 --strict --max-line-length=100 --ignore=...。SMOP ;)” `<!-- ROW_MINE: ksummit-discuss.messages.350818 -->`

## 80.13 【Linux社区】gitnotes折中

- 【Linux社区】Brauner：“我支持 Link 路线但看到让 Change-Id 工作流不干扰上游期望的可能——--- 后放 Change-Id 仍会在 git tag+request-pull 泄出；何不让 Gerrit 从 git notes 找 Change-Id——不进 merge 与 pull” `<!-- ROW_MINE: ksummit-discuss.messages.350819 -->`

## 80.14 【Linux社区】供应商大系列

- 【Linux社区】Petersen：“供应商驱动提交常 50+ 补丁/窗口；同期同驱动 fixes 树常收 10-20 补丁——判断属于哪棵树不易” `<!-- ROW_MINE: ksummit-discuss.messages.350820 -->`

## 80.15 【Linux社区】供应商不分树

- 【Linux社区】Brown：“很多供应商根本不区分、只关心上游——嵌入式世界他们本就预期给非 mainline 用户发一堆树外补丁；回溯到 stable 与供应商关系的老话题” `<!-- ROW_MINE: ksummit-discuss.messages.350821 -->`

## 80.16 【Linux社区】KS2014档案-TODO

- 【Linux社区】Carpenter（2014-05-21）发明 TODO-list 邮件标签：“TODO-list: 2014-05-21: lirc: LIRC_GET_FEATURES API 时而 ulong 时而 u32——grep ^TODO-list: inbox 自动生成清单、任何人都能添加” `<!-- ROW_MINE: ksummit-discuss.messages.350822 -->`

## 80.17 【Linux社区】ViroMUA现实

- 【Linux社区】Viro：“*blink* 你真提议更新所有人用的 MUA？或研究记录控制各家 MUA 的办法？我不知道 mutt 怎么做；还有用浏览器/evolution/pine 的可怜人” `<!-- ROW_MINE: ksummit-discuss.messages.350823 -->`

## 80.18 【Linux社区】DougMUA回应

- 【Linux社区】Doug：“多数人用 git-send-email 发补丁——可先写 Message-Id 再传；用 mutt 直发就不行；100% 采用不可能——盼足够采用率值得做工具集成”；patman 补丁（ozlabs 1157266）+Berg git hook PoC `<!-- ROW_MINE: ksummit-discuss.messages.350824 -->`

## 80.19 【Linux社区】Kees单目录提议

- 【Linux社区】Kees：“向 Dan 提议所有 profile 收进 Documentation/ 单一目录——两种读法：按条目读单个、全部通读研究；#2 靠单目录+单 index” `<!-- ROW_MINE: ksummit-discuss.messages.350825 -->`

## 80.20 【Linux社区】Mauro存储投票

- 【Linux社区】Mauro：“内容属于子系统专属文档、应与 kAPI 同 index——存 Documentation/*/<subsystem>”；MAINTAINERS 不产 html——新手可能不懂其重要性（多年前提过 ReST 化 RFC）；“核心人才研究全部——grep 就能找齐” `<!-- ROW_MINE: ksummit-discuss.messages.350826 -->`

## 80.21 【Linux社区】Kees让步赞赏

- 【Linux社区】Kees：“好点……MAINTAINERS 出 .rst 会很棒——可以是 sphinx 构建目标”；“无论如何别让我分心：捕获这些细节太棒了、让我生活轻松许多 :)” `<!-- ROW_MINE: ksummit-discuss.messages.350827 -->`

## 80.22 【Linux社区】不特别原则

- 【Linux社区】Williams 回 Gunthorpe：“只要有例外就回到‘这案像 net 一样特殊吗’的争论——宁可在 contributor 文档全部记录”；“值得写明 profile 指南：努力不搞特殊、怪规则会被质询（如 libnvdimm 续行）——但先别打标准之战、等异常者显形” `<!-- ROW_MINE: ksummit-discuss.messages.350828 -->`

## 80.23 【Linux社区】MauroReST方案

- 【Linux社区】Mauro：“不能直接改名 .rst 让 Sphinx 处理（顶部指令与条目都解析错）；最佳=脚本或 get_maintainers.pl 产 ReST”；附 [PATCH RFC] MAINTAINERS 入 ReST 输出（.. include:: :literal:） `<!-- ROW_MINE: ksummit-discuss.messages.350829 -->`

## 80.24 【Linux社区】Pinchart评审

- 【Linux社区】Pinchart 对 media profile 六处拼写纠正+四实质：CC 偏好（“流量太大我跟不过来、更喜欢被 CC”）；senior→experienced；“静态分析有价值但恐是新人高门槛”；“低容量清理应单补丁全子系统、太大才拆” `<!-- ROW_MINE: ksummit-discuss.messages.350830 -->`

## 80.25 【Linux社区】Mauro修订

- 【Linux社区】Mauro：“用 patchwork 看即可（pwclient 脚本化）；我个人 prefer 不被 CC——改为 It could be wise to also copy”；新警告条款加“without a very good reason”；附 media profile v2 diff（checkpatch 段加长行说明） `<!-- ROW_MINE: ksummit-discuss.messages.350831 -->`

## 80.26 【Linux社区】mediaProfilev2

- 【Linux社区】Mauro [PATCH v2] 157 行全文定稿（含 Pinchart 修订：experienced/CC 措辞/80 列豁免说明/风格清理单补丁优先） `<!-- ROW_MINE: ksummit-discuss.messages.350832 -->`

## 80.27 【Linux社区】KS2014档案-cgit

- 【Linux社区】Howells（2014-05-21）列 cgit 对 gitweb 缺失功能四条（tab 展开/远端粉色框/tag shortlog 按钮/作者名可点击） `<!-- ROW_MINE: ksummit-discuss.messages.350833 -->`

## 80.28 【Linux社区】+++问

- 【Linux社区】Almeida 问“用 +++ 而非 --- 的动机？”Mauro：“只是 cosmetics——子维护者制仅少数子系统用、故作 sub-chapter” `<!-- ROW_MINE: ksummit-discuss.messages.350834 -->`

## 80.29 【Linux社区】Pinchart二轮

- 【Linux社区】Pinchart 逐字校对+三实质：CC 个人偏好“能否在 MAINTAINERS 按人编码（你 opt-out、我 opt-in 我维护的驱动）”；“低容量清理单补丁应成规则”；“being prepared to justify 听着严厉 :-) 但大意好” `<!-- ROW_MINE: ksummit-discuss.messages.350835 -->`

## 80.30 【Linux社区】KeesReST构建

- 【Linux社区】Kees：“MAINTAINERS 出 .rst 可做 sphinx 构建目标；不重复指令——脚本生成整个文件更好（Joe 也建议）；我做如果你不抢先 :)” `<!-- ROW_MINE: ksummit-discuss.messages.350836 -->`

## 80.31 【Linux社区】awk方案

- 【Linux社区】Mauro：“同意重复指令不好——当年只是实验；大问题是 programoutput 扩展有些开发者不喜欢”；给出 awk 两行生成 maintainers.rst 方案+欢迎 Kees 先做 `<!-- ROW_MINE: ksummit-discuss.messages.350837 -->`

## 80.32 【Linux社区】CC与自动化

- 【Linux社区】Mauro：“个人偏好难按人编码——可在 profile 子维护者节加”；“有自动化计划（升级 patchwork 后像 pull request 那样）”；“profile 保留是提醒——补丁对静态分析也应干净” `<!-- ROW_MINE: ksummit-discuss.messages.350838 -->`

## 80.33 【Linux社区】Helgaas细问

- 【Linux社区】Helgaas LPC demo 后四问：离线预下载状态（“我的抱怨是每个小交互都等服务器——不慢但流程感觉迟钝”）；CI bits 可看吗；mbox 精简（“启动 mutt 5-10 秒”） `<!-- ROW_MINE: ksummit-discuss.messages.350839 -->`

## 80.34 【Linux社区】getmaintainer至上

- 【Linux社区】Carpenter：“文档该说‘用 get_maintainer.pl 并照做’——其他都太复杂”；staging 维护者抱怨没被 CC——“责任在你把自己加进 MAINTAINERS……别怪新人不读文档时错在你”；“我发补丁用 get_maintainer.pl+Fixes 提交作者+手动移除全树工作者” `<!-- ROW_MINE: ksummit-discuss.messages.350840 -->`

## 80.35 【Linux社区】分散存储

- 【Linux社区】Carpenter：“可为自己维护的 .c 加条目……或让 get_maintainer.pl grep .c 的特定标签而非全放中央 MAINTAINERS——把信息存在 MY BRAIN 没意义！我记不住 media 子模块谁维护” `<!-- ROW_MINE: ksummit-discuss.messages.350841 -->`

## 80.36 【Linux社区】fixes增强

- 【Linux社区】Geert：“更好：教 get_maintainer.pl 自动加 Fixes 指向提交的作者？” `<!-- ROW_MINE: ksummit-discuss.messages.350842 -->`

## 80.37 【Linux社区】dimfixes演示

- 【Linux社区】Jani：“DRM 维护者工具有——dim fixes 61f7f7c8 输出 Fixes+Cc 全链（gpiolib acpi 例九行）+Cc stable”；“可大幅改进但给出易修剪的初始列表” `<!-- ROW_MINE: ksummit-discuss.messages.350843 -->`

## 80.38 【Linux社区】KS2014档案-gatekeeper

- 【Linux社区】Williams（2014-05-21）：“驱动开发更适合 gatekeeper——对驱动内核常就是应用；libsas 例：‘这轮先 gatekeeper’——在意者开始用并报 bug、bug 报告会吸引深层评审”；NET_DMA 撤除 staging 例；“核心内核呢——是否在扼杀实验的暴露？” `<!-- ROW_MINE: ksummit-discuss.messages.350844 -->`

## 80.39 【Linux社区】dim局限

- 【Linux社区】Geert：“谢谢但那不是 scripts/get_maintainer.pl、且限于 N 个子系统之一——与 Dan 抱怨的没太大不同” `<!-- ROW_MINE: ksummit-discuss.messages.350845 -->`

## 80.40 【Linux社区】接受至上

- 【Linux社区】Mauro：“用 get_maintainer.pl 并照做——works for me”；“提交文档补丁时也需手动清长 CC 列表” `<!-- ROW_MINE: ksummit-discuss.messages.350846 -->`

## 80.41 【Linux社区】dim源码公开

- 【Linux社区】Jani：“要点是提供参考与可偷的东西——可视为 get_maintainer.pl 的 wrapper、非子系统专属（MIT）；贴 dim_cite/dim_fixes 函数全文” `<!-- ROW_MINE: ksummit-discuss.messages.350847 -->`

## 80.42 【Linux社区】HerringCI细节

- 【Linux社区】Herring：“pwclient list 存文件、离线存命令稍后跑”；pw-checks+CI job 链接；“设计目标=不过度绑 mutt——现在用 pwclient git-am 拿标签（离线不可）”；“用 maildir（mbox 搜索有问题）” `<!-- ROW_MINE: ksummit-discuss.messages.350848 -->`

## 80.43 【Linux社区】拆分旧案

- 【Linux社区】Perches：“另一选项=MAINTAINERS 拆成多个分布式文件——get_maintainer.pl 已支持（LWN 730509）”；“信息存 MY BRAIN 没意义——我也不该记” `<!-- ROW_MINE: ksummit-discuss.messages.350849 -->`

## 80.44 【Linux社区】Brown离线标签

- 【Linux社区】Brown：“我存到 mailbox、上线后脚本查 mailbox 查找；真要离线应用就手动加标签” `<!-- ROW_MINE: ksummit-discuss.messages.350850 -->`

## 80.45 【Linux社区】Vetter拆分提议

- 【Linux社区】Vetter：“完全漏了那提案。现在能在子系统推行吗？很想把所有 GPU 条目移 drivers/gpu——根下文件大到不可管理、git blame 永远；记得 Linus 打算 -rc1 后就拆（至少第一层）？” `<!-- ROW_MINE: ksummit-discuss.messages.350851 -->`

## 80.46 【Linux社区】LKMLdevnull

- 【Linux社区】Pinchart：“教 get_maintainer.pl 加 Fixes 作者是好主意；不确定有其他列表时自动加 LKML——它有点像 /dev/null（有日志；无其他列表时 CC 合理）” `<!-- ROW_MINE: ksummit-discuss.messages.350852 -->`

## 80.47 【Linux社区】LKML可发现性

- 【Linux社区】Doug：“请别这么做——补丁将无法在 LKML patchwork 实例找到；全补丁 CC LKML 便于回复发到未订阅列表的补丁；CC LKML 有什么坏处？” `<!-- ROW_MINE: ksummit-discuss.messages.350853 -->`

## 80.48 【Linux社区】Jani流量数据

- 【Linux社区】Jani：“问题变成：要把所有东西都发 LKML 吗？过去 30 天我角落的月增量约 96,904 封（notmuch count）；不过 LKML 本就是喝不动的消防水管……” `<!-- ROW_MINE: ksummit-discuss.messages.350854 -->`

## 80.49 【Linux社区】KS2014档案-cgit回应

- 【Linux社区】Konstantin（2014-05-21）：“cgit 是上游项目、只能转交功能请求（已转）”；“git.kernel.org 是 gitolite 的 mirror clone——bare 无其他 remote”；“作者名可点击可用 filter 加” `<!-- ROW_MINE: ksummit-discuss.messages.350855 -->`
