# 79 【Linux社区】MEP定稿与workflows列表创建

> 来源：ksummit-discuss p131（50 封全读，2019-09-09/13 MEP 评审链+TAB 选举结果+MS 会后产物，夹杂 2014-05 档案信）
> 判定：48 CAND / 2 NV。主题分布：KS2014档案-单测文化 1、继承码与公司压力 1、notes工作流缘由 1、公司阻力细辨 1、patchid签名与TOFU 1、ksummit入lore 1、TAB2019选举结果 1、am标签解析诉求 1、Vyukov议题入MS 1、MEPv2改名 1、P回收补丁 1、KS2014档案-PM 1、MEP模板全文 1、libnvdimm首例 1、SCSI准则全文 1、双缩进批驳 1、Axboe声援 1、反对分文件 1、自省clangformat 1、Vyukov视频上线 1、MS2019议程V2 1、gatekeeper推演 1、clangformat无味 1、putt三阶段提案 1、多样性即恶 1、SCSI准则四问 1、vger上限论 1、W=1辩护 1、记录现实 1、workflows列表创建 1、GitGitGadget引入 1、规则清单 1、KS2014档案-时钟 1、checkpatch前缀规则 1、kerneldoc默认化 1、W=1默认支持 1、千警告现实 1、dtsW=2 1、接受度前提 1、E标签提议 1、workflows入lore 1、MauroAck 1、理想遇现实 1、正则填充提议 1、提交侧工具 1、浅克隆问 1、mediaProfile补丁 1、2010先例引用 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p131（实锚 pk 350756-350805）的逐封提取（48 CAND / 2 NV），全 48 块采用**单行摘要体例**（丙型）：每块由“## 79.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 79.1 【Linux社区】KS2014档案-单测文化

- 【Linux社区】Fleming 回 Greg：单测应人人所有（破坏者负责修）、实现者最宜写测试；维护者角色宜用于汇总结果与大规模硬件跑测（引 Fengguang/Rothwell 语）；“永不休止的修复战会让人的头爆炸”（2014-05-21） `<!-- ROW_MINE: ksummit-discuss.messages.350756 -->`

## 79.2 【Linux社区】继承码与公司压力

- 【Linux社区】Bottomley：“继承代码反而容易——推动者不执着于他人设计、重做让它更属于他；最大问题是原作者把设计当唯一可能并施加公司压力”；“解释这是维护与一致性问题确实有帮助” `<!-- ROW_MINE: ksummit-discuss.messages.350757 -->`

## 79.3 【Linux社区】notes工作流缘由

- 【Linux社区】Brown 转用 git notes 的原因：“push 成功即发 applied 邮件、即便网络慢或不稳” `<!-- ROW_MINE: ksummit-discuss.messages.350758 -->`

## 79.4 【Linux社区】公司阻力细辨

- 【Linux社区】Brown：“公司问题常是‘X 时间内完成’或‘测试投入巨大不可重复’——超出个人；开发者或乐意重做（私下谢我替他们说出了内部已说的话）但被告知推现有代码”；“这些问题更容易向管理层讲清” `<!-- ROW_MINE: ksummit-discuss.messages.350759 -->`

## 79.5 【Linux社区】patchid签名与TOFU

- 【Linux社区】Konstantin：lore API 服务（patch-id 查询）“仍须信任 kernel.org、攻击者可伪造 From 发 LKML——没人真读潜入不难”；替代=补丁密码学签名（Patch-id-sig/Patch-id-key 放 --- 下）+git-am TOFU 数据库；“安全高马上的合理未必对他人合理” `<!-- ROW_MINE: ksummit-discuss.messages.350760 -->`

## 79.6 【Linux社区】ksummit入lore

- 【Linux社区】Konstantin：“应（强烈）大众要求，ksummit-discuss 存档现可经 lore.kernel.org/ksummit-discuss 访问”（本库入 lore 时点） `<!-- ROW_MINE: ksummit-discuss.messages.350761 -->`

## 79.7 【Linux社区】TAB2019选举结果

- 【Linux社区】Laura 公布 2019 TAB 选举结果：Greg KH/Corbet/Rostedt/Ted Tso/Sasha Levin 当选；174 人投票；CIVS 只给聚合分与对抗结果不给每人全票 `<!-- ROW_MINE: ksummit-discuss.messages.350762 -->`

## 79.8 【Linux社区】am标签解析诉求

- 【Linux社区】Hellwig 回 Boyd：“git am 若能解析标签加到正确补丁帮助巨大”；“忽略封面信+允许 diff fuzz+类 rebase 的冲突解决”（取代现需手动应用的一团糟） `<!-- ROW_MINE: ksummit-discuss.messages.350763 -->`

## 79.9 【Linux社区】Vyukov议题入MS

- 【Linux社区】Ted：Greg 建议把 Vyukov Reflections 谈列为 MS 首题——“进一步标准化工具与流程的标准与程序、让开发流程更成熟、提升开发者生产力与幸福” `<!-- ROW_MINE: ksummit-discuss.messages.350764 -->`

## 79.10 【Linux社区】MEPv2改名

- 【Linux社区】Dan Williams [PATCH v2 0/3]：Subsystem Profile→Maintainer Entry Profile（“不是每个条目都是完整子系统”）、删旧 P:；引 Plumbers2018 开场“内核维护的第一条规则是没有硬性规则——既是祝福也是诅咒” `<!-- ROW_MINE: ksummit-discuss.messages.350765 -->`

## 79.11 【Linux社区】P回收补丁

- 【Linux社区】[v2 1/3] MAINTAINERS P: 条目修为 M: 或删除（Perches 建议）——P: 将指向 Profile 文档 `<!-- ROW_MINE: ksummit-discuss.messages.350766 -->`

## 79.12 【Linux社区】KS2014档案-PM

- 【Linux社区】Ulf Hansson（2014-05-21）：runtime PM centric 方法的复杂问题——PM core 在 system suspend 期间阻止 runtime suspend（pm_runtime_get_noresume）；pm_runtime_force_suspend `<!-- ROW_MINE: ksummit-discuss.messages.350767 -->`

## 79.13 【Linux社区】MEP模板全文

- 【Linux社区】[v2 2/3] 模板 99 行全文六节：Overview/Submit Checklist Addendum/Key Cycle Dates（新特性 -rc5 前投稿惯例）/Coding Style Addendum/Review Cadence/Style Cleanup Patches `<!-- ROW_MINE: ksummit-discuss.messages.350768 -->`

## 79.14 【Linux社区】libnvdimm首例

- 【Linux社区】[v2 3/3] libnvdimm Profile 64 行全文：patchwork 反馈/libnvdimm-fixes 与 for-next 双分支/ndctl 单测/-rc4 前投稿 rc6 稳定/双缩进风格/一周 ping 私有提醒/风格清理欢迎 `<!-- ROW_MINE: ksummit-discuss.messages.350769 -->`

## 79.15 【Linux社区】SCSI准则全文

- 【Linux社区】Petersen：“去年 Plumbers 后我为 SCSI 写过（Christoph 早期版本）——会更新以匹配你的模板”+SCSI 提交准则全文（8 周窗口/双树/两正面评审/A Tested-by worth a thousand reviews/公司外评审一项/5 工作日响应/patchwork 状态机） `<!-- ROW_MINE: ksummit-discuss.messages.350770 -->`

## 79.16 【Linux社区】双缩进批驳

- 【Linux社区】Carpenter：“那看起来 horrible 且触发 checkpatch 警告——用大家的写法”；“我讨厌这些额外文档——人人都会发明新 hoops”；BPF 树标签“约半数标错——凡自标的人都会标糟” `<!-- ROW_MINE: ksummit-discuss.messages.350772 -->`

## 79.17 【Linux社区】Axboe声援

- 【Linux社区】Axboe：“完全同意 Dan(Carpenter)：绝对不喜欢这类文件与子系统强加怪异风格（yuck）”；“更合理的是标准化代码何时到维护者手里的规则——不应每子系统详列” `<!-- ROW_MINE: ksummit-discuss.messages.350773 -->`

## 79.18 【Linux社区】反对分文件

- 【Linux社区】Perches：“多行语句双缩进找不到好理由”；“指向单独文件的间接层不是好事；子系统单独风格非我愿鼓励” `<!-- ROW_MINE: ksummit-discuss.messages.350774 -->`

## 79.19 【Linux社区】自省clangformat

- 【Linux社区】Williams：“这就是本 exercise 的要点”；CodingStyle 定了 clang-format——“比手写可解释风格更好的答案、我会转 libnvdimm”；“若标准化所有变异处 MEP 可被共同指南取代——否则 MEP 是贡献者导航现状的可悲注解，但那是需要面对的现实” `<!-- ROW_MINE: ksummit-discuss.messages.350775 -->`

## 79.20 【Linux社区】Vyukov视频上线

- 【Linux社区】Ted 上传“hot wash”未剪辑视频（YouTube）——“在 Linux 视频编辑工具界面我的 saving throw 失败了直接传” `<!-- ROW_MINE: ksummit-discuss.messages.350776 -->`

## 79.21 【Linux社区】MS2019议程V2

- 【Linux社区】议程 V2：Vyukov Reflections 13:15 首题/HW Security Update 17:00/出席名单 31 人（加 Sasha Levin） `<!-- ROW_MINE: ksummit-discuss.messages.350777 -->`

## 79.22 【Linux社区】gatekeeper推演

- 【Linux社区】NeilBrown（2014-05-21）：用户用应用、应用用内核特性——“有人会为不保永久的功能写应用吗”；cgroups 例无 gatekeeper 也酿 API 变更；“内核内部选项应用不敢依赖、找问题更难——要有真实例子” `<!-- ROW_MINE: ksummit-discuss.messages.350778 -->`

## 79.23 【Linux社区】clangformat无味

- 【Linux社区】Perches：“clang-format 不能处理缺大括号/多段字符串合并/for_each 宏/列对齐——clang-format as yet has no taste；AI 而非表驱动才是真解但我不想训练它” `<!-- ROW_MINE: ksummit-discuss.messages.350779 -->`

## 79.24 【Linux社区】putt三阶段提案

- 【Linux社区】Konstantin 基金会提案大纲：Stage 1 putt 本地 patchwork（tagline 自动跟踪/interdiff）/Stage 2 CI 工作流（putt-cid）/Stage 3 邮件降为副信道（SSB p2p+Radicle 状态机自动合并——“或许多喝了点区块链酷爱饮料”） `<!-- ROW_MINE: ksummit-discuss.messages.350780 -->`

## 79.25 【Linux社区】多样性即恶

- 【Linux社区】Bart：“维护者读到可能视为鼓励自定政策；Plumbers2019 结论=太多多样性是坏的、需更多统一；望把 Vyukov 演讲摘要并入维护者手册” `<!-- ROW_MINE: ksummit-discuss.messages.350781 -->`

## 79.26 【Linux社区】SCSI准则四问

- 【Linux社区】Bart 对 Petersen 准则四问：Cc 要求适用范围/W=1 加入/qla2xxx 既有警告处置（要求不新增警告）/commit message 加 why/Superceded 拼写 `<!-- ROW_MINE: ksummit-discuss.messages.350782 -->`

## 79.27 【Linux社区】vger上限论

- 【Linux社区】Perches：“对 vger 列表不可行——最大邮件头尺寸限制、跨子系统补丁 to/cc 很长”；W=1“太依赖编译器版本”；“why 比 how 更重要应为主描述” `<!-- ROW_MINE: ksummit-discuss.messages.350783 -->`

## 79.28 【Linux社区】W=1辩护

- 【Linux社区】Bart：“从未观察到编译器版本问题——无用警告 Linus 会快压”；“kernel-doc 头格式检查只有 W=1 才开” `<!-- ROW_MINE: ksummit-discuss.messages.350784 -->`

## 79.29 【Linux社区】记录现实

- 【Linux社区】Corbet：“维护者峰会共识：虽不喜欢子系统专属规则、它们确实存在、我们只是记录现实。套用 Phillip K. Dick：现实就是你不记录它也不会消失”；“我希望这能把 local quirks 羞出存在——迹象显示可能” `<!-- ROW_MINE: ksummit-discuss.messages.350785 -->`

## 79.30 【Linux社区】workflows列表创建

- 【Linux社区】Ted：MS 上创建 workflows@vger.kernel.org（分享评审/收集/测试/提交工作流+讨论共同基建需求）；“这是需求讨论不是实现”；“Gerrit 与 patchwork 现状都不能完全满足社区需求；分散努力未必最佳” `<!-- ROW_MINE: ksummit-discuss.messages.350786 -->`

## 79.31 【Linux社区】GitGitGadget引入

- 【Linux社区】Boyd 提 GitGitGadget 先例+--base 实践；Brugger：“新人的挣扎不是技术而是流程；智能的 GitGitGadget 类服务能帮 github 背景开发者” `<!-- ROW_MINE: ksummit-discuss.messages.350787 -->`

## 79.32 【Linux社区】规则清单

- 【Linux社区】Carpenter 逐条列子系统怪规则（net 注释风格/逆圣诞树/[net] 标签/infiniband sizeof/前缀大小写/禁 I 与 we/声明块禁 kmalloc/bpf 标签猜测）；“不是 shaming 是 validating——Book of Rules 像读不完的 EULA”；“加不进 checkpatch 就说明你不够在乎” `<!-- ROW_MINE: ksummit-discuss.messages.350788 -->`

## 79.33 【Linux社区】KS2014档案-时钟

- 【Linux社区】Geert（2014-05-21）：盼 driver core 层通用处理时钟——“新 SoC 突然有可门控时钟时难道要改所有驱动？最好 DT 加时钟就 just work” `<!-- ROW_MINE: ksummit-discuss.messages.350789 -->`

## 79.34 【Linux社区】checkpatch前缀规则

- 【Linux社区】Williams：“有更好 perl 技能者写 checkpatch 规则抓前缀大小写、否则同意维护者应用时静默修正勿费时指出琐事——Linus 喜欢 - 不喜欢 *、我忘了他就静默修” `<!-- ROW_MINE: ksummit-discuss.messages.350790 -->`

## 79.35 【Linux社区】kerneldoc默认化

- 【Linux社区】Wilcox：“把 kernel-doc 警告从 W=1 移出很容易——我只是怕新警告淹没；若大体已修就默认检查” `<!-- ROW_MINE: ksummit-discuss.messages.350791 -->`

## 79.36 【Linux社区】W=1默认支持

- 【Linux社区】Mauro：“media 的 CI 实例默认用 W=1；EDAC 几个警告易修；我完全支持 W=1 默认” `<!-- ROW_MINE: ksummit-discuss.messages.350792 -->`

## 79.37 【Linux社区】千警告现实

- 【Linux社区】Perches：“x86-64 defconfig 有 1000+ 条 kernel-doc 警告——支持该想法但眼下太多无法普遍开启” `<!-- ROW_MINE: ksummit-discuss.messages.350793 -->`

## 79.38 【Linux社区】dtsW=2

- 【Linux社区】Herring：“ARM 上数千条——W=1 开了 dts 构建更多检查且多为 include 重复；可把 dts 检查移 W=2；为何不把无假警告的从 W=1 提为默认？” `<!-- ROW_MINE: ksummit-discuss.messages.350794 -->`

## 79.39 【Linux社区】接受度前提

- 【Linux社区】Roeck：“我默认 W=1 过但放弃——通用内核 include 大量警告；W=1 修复补丁被拒后就不再做”；“默认化需要共同约定：维护者应接受 W=1 问题修复” `<!-- ROW_MINE: ksummit-discuss.messages.350795 -->`

## 79.40 【Linux社区】E标签提议

- 【Linux社区】Dunlap：“子系统若要求主题拼写/大小写应加进 MAINTAINERS，如 E: NuBus” `<!-- ROW_MINE: ksummit-discuss.messages.350796 -->`

## 79.41 【Linux社区】workflows入lore

- 【Linux社区】Greg：“已经在：lore.kernel.org/workflows”（MS 产物列表上线 lore） `<!-- ROW_MINE: ksummit-discuss.messages.350798 -->`

## 79.42 【Linux社区】MauroAck

- 【Linux社区】Mauro Acked P: 回收补丁（LinuxTV 条目删除确认） `<!-- ROW_MINE: ksummit-discuss.messages.350799 -->`

## 79.43 【Linux社区】理想遇现实

- 【Linux社区】Greg KH（2014-05-21）：“理想世界遇现实——今天内核内测试是坏的、没人站出来弄清是内核问题还是测试问题；buy-in 早已存在、我求了多年终于有人能分配资源——机会很好不想搞砸” `<!-- ROW_MINE: ksummit-discuss.messages.350800 -->`

## 79.44 【Linux社区】正则填充提议

- 【Linux社区】Herring：“+1 做成正则应对 (net|net-next)” `<!-- ROW_MINE: ksummit-discuss.messages.350801 -->`

## 79.45 【Linux社区】提交侧工具

- 【Linux社区】Herring：“提交侧 free-for-all 会让维护者工具更复杂更不可靠——提交者工具也该包含”；“常见问题=提交者后续版本不加标签——工具应查旧版补加或自动回复；有 interdiff 就能区分忘记与需重审” `<!-- ROW_MINE: ksummit-discuss.messages.350802 -->`

## 79.46 【Linux社区】浅克隆问

- 【Linux社区】Pinchart：“工具支持浅克隆吗？有些列表流量巨大存在多年——只关心近 N 月的人不想克隆全部” `<!-- ROW_MINE: ksummit-discuss.messages.350803 -->`

## 79.47 【Linux社区】mediaProfile补丁

- 【Linux社区】Mauro 发 media subsystem profile（140 行全文）：纯文本邮件否则服务器自动拒/patchwork.linuxtv.org 工作流/子维护者六领域/v4l-utils compliance/W=1+C=1+smatch+sparse/--strict/-rc5 前投稿/高流量两周一 ping/风格清理按目录分组 `<!-- ROW_MINE: ksummit-discuss.messages.350804 -->`

## 79.48 【Linux社区】2010先例引用

- 【Linux社区】Perches 引 2010 年 lore LKML 旧帖（Linus 论 patch subject prefix）作前缀约定先例 `<!-- ROW_MINE: ksummit-discuss.messages.350805 -->`
