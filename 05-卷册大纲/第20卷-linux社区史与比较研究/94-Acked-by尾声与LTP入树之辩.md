# 94 【Linux社区】Acked-by尾声与LTP入树之辩

> 来源：ksummit-discuss p146（50 封全读，2014-05-04 至 2014-06-05，Acked-by 利害相关者语义收束、新人做 stable 回移之辩、LTP 入树之辩与 KS 邀请 Gmail 垃圾箱事件、块层大设计过程之问）
> 判定：39 CAND / 11 NV。主题分布：Acked-by利害相关者语义 1、xfstests-bld公开可复现 1、评审是维护者职责 1、staging五人成长实证 1、Intel嵌入式信誉之疑 1、stable活动不计KS邀请 1、新人回移vs老手共维 1、stable维护须专家论 1、公司环境前提自白 1、grunt work选拔论 1、逐补丁测试缺位 1、重发退避机制设想 1、基线测试减少stable债 1、为何没有大设计过程 1、演化式设计过程论 1、show me the code定则 1、大系列分阶段拆分 1、有偿评审原意澄清 1、标签歧义活例证 1、树内TODO优于网站 1、驱动能力范围论 1、btrfs为正解论 1、RAID统一失败史与架构观 1、KS邀请进Gmail垃圾箱 1、测试指针与硬件门槛 1、LF域Gmail拒信实录 1、垃圾箱与PR事故 1、LTP入树开明表态 1、彻底拒收证据 1、Olof提名Kevin 1、单一翻译点方案 1、LTP专家引荐与bisect险 1、bisect反成不入树理由 1、测试套兼容宽度之痛 1、commit-id自配置设想 1、非技术之难在维护 1、SORBS拉黑溯源 1、delisting与换主机 1、LTP维护者反对拆分 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p146（实锚 pk 351506-351555）的逐封提取（39 CAND / 11 NV），全 39 块采用**单行摘要体例**（丙型）：每块由“## 94.x 题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 94.1 Acked-by利害相关者语义

- 【Linux社区】Rostedt 反驳“+1”定性：Acked-by 真义是“与代码有利害关系者认可”，陌生人的 Acked-by 才是 +1 且自己根本不加；Approved-by＝维护者放行“可走你的树”；拿不到 Reviewed-by 时向利害相关者要 Acked-by `<!-- ROW_MINE: ksummit-discuss.messages.351506 -->`

## 94.2 xfstests-bld公开可复现

- 【Linux社区】Ted Ts'o 公开 xfstests-bld 测试环境（完全可复现）并推 ext4 开发者提交前用 kvm-xfstests，bisect 到其补丁会温和提醒；建议 MAINTAINERS 加测试指针字段为最简方案；自述环境清理到敢公开花了一阵、公开后省时极多 `<!-- ROW_MINE: ksummit-discuss.messages.351509 -->`

## 94.3 评审是维护者职责

- 【Linux社区】Greg KH：除“信任的人”外补丁必须被评审——那是子系统维护者的职责；“推回去并请求帮助——有人问能做什么帮忙，给他们事做” `<!-- ROW_MINE: ksummit-discuss.messages.351510 -->`

## 94.4 staging五人成长实证

- 【Linux社区】Greg KH：至少 5 人从 staging cleanup 起步成为各公司内核开发者（有人进公司离开但其成长本身算成功）；“怎么知道谁是那 1%？我不愿冒这个险”；曾派新人翻 bugzilla 几乎总失败——人须“invested”，报 bug 者协助修复则成功得多；staging 变干净故继续鼓励 `<!-- ROW_MINE: ksummit-discuss.messages.351511 -->`

## 94.5 Intel嵌入式信誉之疑

- 【Linux社区】Guenter 以 BMW 类比讥 Intel 营销不卖想买之物；指 Intel 再推嵌入式时上次被弃者持怀疑态度——硬件厂商市场信誉史料 `<!-- ROW_MINE: ksummit-discuss.messages.351513 -->`

## 94.6 stable活动不计KS邀请

- 【Linux社区】Li Zefan 问 stable 上的活动是否计入 KS 邀请——无法区分自动回移与人工请求回移，后者应获认可 `<!-- ROW_MINE: ksummit-discuss.messages.351514 -->`

## 94.7 新人回移vs老手共维

- 【Linux社区】Li Zefan 回 Ted：新人做 stable 回移与“给 Greg 找 co-maintainer”相似但自己建议找有经验可信者；同意 Woodhouse 的担忧、怀疑新人对 stable 回移有热情 `<!-- ROW_MINE: ksummit-discuss.messages.351515 -->`

## 94.8 stable维护须专家论

- 【Linux社区】Guenter：非热情问题而是专长问题——stable 用户宁要专家而非新人维护 `<!-- ROW_MINE: ksummit-discuss.messages.351516 -->`

## 94.9 公司环境前提自白

- 【Linux社区】Ted Ts'o 承认见过新人回移成功但皆在公司环境：隔壁桌可求助、commit 标注测试说明、过评审流程、皆过 Google 面试——邮件列表上能力未知、问责与动机不同 `<!-- ROW_MINE: ksummit-discuss.messages.351517 -->`

## 94.10 grunt work选拔论

- 【Linux社区】Ted Ts'o：stable 树仍由专家维护、新人回移仍经专家评审；首几补丁省不了时间但长期更可能育出能干程序员；维护者的 grunt work 亦多（评审/集成测试/bisect）；“发千个空白补丁的人不是我想指导的”——要培养接棒维护者该选哪种人 `<!-- ROW_MINE: ksummit-discuss.messages.351518 -->`

## 94.11 逐补丁测试缺位

- 【Linux社区】Greg KH 回 Ted：所列全是公司环境与正常 stable 回移的差异；何况没有逐补丁测试确保修复属实、回移没搞坏 `<!-- ROW_MINE: ksummit-discuss.messages.351519 -->`

## 94.12 重发退避机制设想

- 【Linux社区】Geert：大系列每被挑一小错即全量重发、版本号通胀（v29 现记录）；提议 git send-email 记忆上版发送时间、按系列大小设退避期拒绝过快重发 `<!-- ROW_MINE: ksummit-discuss.messages.351521 -->`

## 94.13 基线测试减少stable债

- 【Linux社区】Michal Simek：应在 linux-next 及入 next 前分支多测——基线少 bug 则 stable 补丁少；0day 构建覆盖好、扩展 Qemu/模拟器运行时测试是下一步——每个开发者都能收到“你的补丁弄坏了别人”的消息；统一框架自动化测试合理 `<!-- ROW_MINE: ksummit-discuss.messages.351524 -->`

## 94.14 为何没有大设计过程

- 【Linux社区】Daniel Phillips：dm/md 仍是孤岛、无可用快照块设备、fs 与卷管理器零交互——多年反复失败；抛出更大问题“为何 Linux 对大型设计议题没有设计过程”——也许这才是缺失的核心议题 `<!-- ROW_MINE: ksummit-discuss.messages.351525 -->`

## 94.15 演化式设计过程论

- 【Linux社区】Greg KH 回 Phillips：Neil 演讲讲了十年——重要性不够或无人说服公司赞助；Linux 有“演化式”设计过程——对比四五年前的内核重大变化赫然，只是身处其中不觉其大 `<!-- ROW_MINE: ksummit-discuss.messages.351527 -->`

## 94.16 show me the code定则

- 【Linux社区】NeilBrown：dm-raid.c 即桥、dm-thin.c 快照可用；Linux 设计规则简单——“show me the code”，过评审就进；跨子系统大设计需多个原型、准备丢弃重来——“演化不只是适者生存，也是弱者之死” `<!-- ROW_MINE: ksummit-discuss.messages.351528 -->`

## 94.17 大系列分阶段拆分

- 【Linux社区】Takashi Iwai：让 git 基础工具阻止重发亦危险；大补丁集宜拆分为多个分阶段 patchset `<!-- ROW_MINE: ksummit-discuss.messages.351529 -->`

## 94.18 有偿评审原意澄清

- 【Linux社区】Wolfram Sang 澄清原议非制造动机而是回报已在自发做评审的人——障碍存在但值得；“通过权力拿钱确实更容易”附和 `<!-- ROW_MINE: ksummit-discuss.messages.351530 -->`

## 94.19 标签歧义活例证

- 【Linux社区】NeilBrown 即席质问“Acked-by: me”的歧义：你是仅表同意，还是以文档 MAINTAINER 身份确认？——恰为 Acked-by 语义论战的活例证 `<!-- ROW_MINE: ksummit-discuss.messages.351532 -->`

## 94.20 树内TODO优于网站

- 【Linux社区】Jason Cooper：staging 已有树内 TODO 文件——处理项的补丁应同时删条目；单独网站＝对已饱和者的额外流程外维护 `<!-- ROW_MINE: ksummit-discuss.messages.351534 -->`

## 94.21 驱动能力范围论

- 【Linux社区】Ben Herrenschmidt：仅标准化资源类型（mmio/中断）可由上层处理，其余绝对属驱动能力范围——“这张桌子已经够脏，别请第三者” `<!-- ROW_MINE: ksummit-discuss.messages.351535 -->`

## 94.22 btrfs为正解论

- 【Linux社区】Petersen：要么 fs 显式管理 RAID/快照（btrfs）要么 DM/MD 背后做——新接口做已有之事无意义；“给定 cookie 有无另一份拷贝”调用有 merit 但无人做；btrfs 是更好路径 `<!-- ROW_MINE: ksummit-discuss.messages.351536 -->`

## 94.23 RAID统一失败史与架构观

- 【Linux社区】Bottomley：曾尝试 btrfs/dm/md RAID 统一——dm/md 有进展、btrfs 用法范式太异、强做会一团糟；现看 token/descriptor API（copy offload）找到好的再 revisit；年幼爱蓝图式完美大厦、年长更喜一组勾勒轮廓的抽象、由拼合引导——留出完美架构会忽略的东西 `<!-- ROW_MINE: ksummit-discuss.messages.351537 -->`

## 94.24 KS邀请进Gmail垃圾箱

- 【Linux社区】Ted Ts'o：KS 首轮邀请发出，至少两名 Gmail 用户邀请进垃圾箱——SPF/DKIM 皆过（From=thunk.org 保证身份一致）；在 Google 内部调查；请 Gmail 用户自查垃圾箱 `<!-- ROW_MINE: ksummit-discuss.messages.351538 -->`

## 94.25 测试指针与硬件门槛

- 【Linux社区】Hiramatsu：MAINTAINERS 加测试指针至少该做、还须注明所需硬件；共享后可推进“各维护者发 PR 前+rebase 后跑自己的测试”确保无回归 `<!-- ROW_MINE: ksummit-discuss.messages.351539 -->`

## 94.26 LF域Gmail拒信实录

- 【Linux社区】Randy Dunlap：回信 Cc torvalds@/akpm@/gregkh@ linux-foundation.org 时常被 Gmail 拒——“全是误判”——内核邮件反垃圾证据链一环 `<!-- ROW_MINE: ksummit-discuss.messages.351540 -->`

## 94.27 垃圾箱与PR事故

- 【Linux社区】Ted Ts'o：区分彻底拒收与进收件人垃圾箱——自己的 PULL request 曾进 Linus 垃圾箱故设 DKIM；征集完整头样本以向反垃圾团队申诉并展示 SPF/DKIM pass 仍被拒的头部 `<!-- ROW_MINE: ksummit-discuss.messages.351541 -->`

## 94.28 LTP入树开明表态

- 【Linux社区】Greg KH 回 Walleij：人人总问是否拉 LTP 进树——“当然，为什么不”；若有人抱怨就取 LTP“有用”子集——很好的起点 `<!-- ROW_MINE: ksummit-discuss.messages.351542 -->`

## 94.29 彻底拒收证据

- 【Linux社区】Randy Dunlap 提供被拒原文“this message has been blocked”确认属彻底拒收，并承诺保存样本供 Ted 申诉 `<!-- ROW_MINE: ksummit-discuss.messages.351543 -->`

## 94.30 Olof提名Kevin

- 【Linux社区】Olof 提名 Kevin Hilman：runtime PM 参与、跑 arm-soc 测试板场、Arnd 陪产期共同维护 arm-soc——KS2014 邀请流程史料 `<!-- ROW_MINE: ksummit-discuss.messages.351545 -->`

## 94.31 单一翻译点方案

- 【Linux社区】Ben Herrenschmidt：驱动用单一访问器取命名属性、必要时单一转换函数转 ACPI“东西”；单一转换点胜于散布全驱动；或 DT+ACPI 双表示达驱动、probe 时转私有结构（类旧 platform data） `<!-- ROW_MINE: ksummit-discuss.messages.351546 -->`

## 94.32 LTP专家引荐与bisect险

- 【Linux社区】Mel Gorman 引荐 LTP 专家 Cyril Hrubis（大幅清理）；指出 bisect 隐患——bisect 内核时须小心别 bisect 到 LTP；问导入 tools/testing/ 可行性 `<!-- ROW_MINE: ksummit-discuss.messages.351547 -->`

## 94.33 bisect反成不入树理由

- 【Linux社区】Geert：bisect 隐患也许正是不导入 LTP 的好理由；syscall API 本应稳定故无理由不跑最新 LTP（除非 bisect LTP） `<!-- ROW_MINE: ksummit-discuss.messages.351548 -->`

## 94.34 测试套兼容宽度之痛

- 【Linux社区】Vetter：backport 验证同理须用最新套件；代价是套件须兼容宽得多内核范围（如 reserved 字段垃圾各版本正确拒绝）；drm/i915 有限兼容几版、每版仍余 wontfix `<!-- ROW_MINE: ksummit-discuss.messages.351549 -->`

## 94.35 commit-id自配置设想

- 【Linux社区】Hiramatsu：测试套件或可经 git log 识别补丁是否已合、自配置拒绝不支持的测试 `<!-- ROW_MINE: ksummit-discuss.messages.351550 -->`

## 94.36 非技术之难在维护

- 【Linux社区】Vetter 回 Hiramatsu：feature flags 与跳过宏已有——非技术问题；难在所有情形做对测试并在新功能更新时持续维护 `<!-- ROW_MINE: ksummit-discuss.messages.351552 -->`

## 94.37 SORBS拉黑溯源

- 【Linux社区】Ted Ts'o 查明 infradead 信被拒根因：merlin.infradead.org 在 SORBS 列表（2011-11 spamtrap 记录）——Gmail 550 拒信全文展示；建议提交 delisting `<!-- ROW_MINE: ksummit-discuss.messages.351553 -->`

## 94.38 delisting与换主机

- 【Linux社区】Woodhouse：SORBS 条目系列表服务器时期旧档、列表防 spam 尚可；已提交 delisting；Randy 可用集群其他主机出站 SMTP（smtpauth 角色地址不含 merlin IP） `<!-- ROW_MINE: ksummit-discuss.messages.351554 -->`

## 94.39 LTP维护者反对拆分

- 【Linux社区】Cyril Hrubis：导入内核树不会大赢——LTP 向后兼容、老内核也该用最新版获覆盖与修复，入树有守旧版之险；拆两半致两处共享文件、维护开销与混乱；集成与文档不入树亦可做——难在决定何时何地跑哪些测试、按兴趣组维护用例清单耗时易错 `<!-- ROW_MINE: ksummit-discuss.messages.351555 -->`
