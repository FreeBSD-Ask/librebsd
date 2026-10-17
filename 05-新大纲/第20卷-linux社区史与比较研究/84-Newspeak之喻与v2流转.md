# 84 【Linux社区】Newspeak之喻与v2流转

> 来源：ksummit-discuss p136（50 封全读，2020-07 包容术语论战中段，夹杂 2014-05 档案信）
> 判定：43 CAND / 7 NV。主题分布：苏联Newspeak之喻 1、补丁评审措辞意见 1、支持并求署名 1、替换词与措辞建议 1、subordinate异议答辩 1、git元数据档案信 1、slave词亲身经历 1、作者修订承诺 1、收录Shuah背书 1、弃背景文档收敛 1、回应Newspeak之喻 1、作者修订再承诺 1、seccomp先例数据 1、checkpatch补丁数据 1、Brauner署Ack 1、元数据机制论断 1、allowlist语法之争 1、非母语者语法论 1、英语语法无逻辑 1、非等价替换论 1、动作明确性原则 1、具体性优先论 1、ACPI与DT议题 1、bisect术语之察 1、设备平等之问 1、滑坡讽刺批驳 1、替换词划界质疑 1、颜色标签辨析 1、语境必要性论 1、词源内涵之辩 1、动词形式辨析 1、双动词构词解析 1、blacklist贬义确证 1、回归标签可行性 1、blacklist禁废之辩 1、行业标准先例 1、checkpatch分工 1、v2补丁流转全文 1、Ack升SoB及建议 1、承诺修checkpatch 1、Brown署Review 1、Carpenter署SoB 1、Ts'o署SoB 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p136（实锚 pk 351006-351055）的逐封提取（43 CAND / 7 NV），全 43 块采用**单行摘要体例**（丙型）：每块由“## 84.x 题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 84.1 苏联Newspeak之喻

- 【Linux社区】Rapoport 复 Mason：亲历苏联，“Newspeak was not a fiction but a reality”，担忧包容用语提案乃“a step in a wrong direction” `<!-- ROW_MINE: ksummit-discuss.messages.351006 -->`

## 84.2 补丁评审措辞意见

- 【Linux社区】Lutomirski 要求增列 whitelist、target 及 master 配对词，主张历史叙述移入 changelog，seccomp 改用描述性短语 `<!-- ROW_MINE: ksummit-discuss.messages.351007 -->`

## 84.3 支持并求署名

- 【Linux社区】Shuah Khan 肯定 allowlist/denylist“直观、基于动作且全局含义统一”，请求补加其 Signed-off-by 或 Acked-by `<!-- ROW_MINE: ksummit-discuss.messages.351008 -->`

## 84.4 替换词与措辞建议

- 【Linux社区】Mark Brown 提议增 device 为 slave 替换词，称词源论证不相干，“revelation of 2020”措辞宜更中性 `<!-- ROW_MINE: ksummit-discuss.messages.351009 -->`

## 84.5 subordinate异议答辩

- 【Linux社区】Rostedt 复 Begunkov：设备不平等则 subordinate 恰当，“We are not concerned about the inequality of devices” `<!-- ROW_MINE: ksummit-discuss.messages.351010 -->`

## 84.6 git元数据档案信

- 【Linux社区】2014 Couder 转述 Junio 方案：Fixes: 经 interpret-trailers 标准化、notes 反向映射、bisect 集成，并问可否 signed notes/replace `<!-- ROW_MINE: ksummit-discuss.messages.351011 -->`

## 84.7 slave词亲身经历

- 【Linux社区】Rostedt 忆大学时代即有人指 master/slave 措辞不妥，并谓“does one device actually enslave another device?”本就误导 `<!-- ROW_MINE: ksummit-discuss.messages.351012 -->`

## 84.8 作者修订承诺

- 【Linux社区】Williams 承诺补 whitelist、target 与 master 配对术语，同意历史段落移 changelog，拟荐 blocklist/passlist 为统一简写 `<!-- ROW_MINE: ksummit-discuss.messages.351013 -->`

## 84.9 收录Shuah背书

- 【Linux社区】Williams 谢并收录 Shuah Ack，定 blocklist/passlist 为通用简写，allowlist/denylist 听任子系统本地习惯 `<!-- ROW_MINE: ksummit-discuss.messages.351014 -->`

## 84.10 弃背景文档收敛

- 【Linux社区】Williams 拟增 device 替换词，称背景论述“live in the archives”即可，收敛为仅改 coding-style `<!-- ROW_MINE: ksummit-discuss.messages.351015 -->`

## 84.11 回应Newspeak之喻

- 【Linux社区】Williams 以赴外文化交流培训类比，称非审查而是向最广受众高效表达，且“time will tell” `<!-- ROW_MINE: ksummit-discuss.messages.351016 -->`

## 84.12 作者修订再承诺

- 【Linux社区】Williams 同意补 master 配对词与旧用语清理条款，释 ABI 例外为“don't break userspace”，称“Beyond just Linux”倡议过度 `<!-- ROW_MINE: ksummit-discuss.messages.351017 -->`

## 84.13 seccomp先例数据

- 【Linux社区】Kees Cook 指 seccomp 已用 allow-list/deny-list：man-pages 提交 462ce23（去年）、libseccomp 提交 0e76252（上月） `<!-- ROW_MINE: ksummit-discuss.messages.351018 -->`

## 84.14 checkpatch补丁数据

- 【Linux社区】SeongJae Park 署 Ack，称其自动鼓励用语补丁已并入 linux-next：提交 7d0bea01 与 95a94258 `<!-- ROW_MINE: ksummit-discuss.messages.351020 -->`

## 84.15 Brauner署Ack

- 【Linux社区】Brauner 称“这是该做的事”并署 Acked-by，附议历史段落移入 changelog `<!-- ROW_MINE: ksummit-discuss.messages.351021 -->`

## 84.16 元数据机制论断

- 【Linux社区】2014 Iwai 称不能只靠 Fixes 标签：addendum 尚可记外部链接与未修复回归，建议可信 push/pull notes 或 web API `<!-- ROW_MINE: ksummit-discuss.messages.351022 -->`

## 84.17 allowlist语法之争

- 【Linux社区】Kees Cook 复非母语者：动词前置作名词修饰可通，然“I will allow-list the syscall”令其不适，改用描述性句式 `<!-- ROW_MINE: ksummit-discuss.messages.351023 -->`

## 84.18 非母语者语法论

- 【Linux社区】Boaz Harrosh 举 running mate、cutting board 等动词作形容词之例，称 allow-list“sounds totally English” `<!-- ROW_MINE: ksummit-discuss.messages.351025 -->`

## 84.19 英语语法无逻辑

- 【Linux社区】Brown 谓在英语语法中寻逻辑“注定失望”，并认同 Kees“looks off”直觉 `<!-- ROW_MINE: ksummit-discuss.messages.351026 -->`

## 84.20 非等价替换论

- 【Linux社区】Rostedt 主张 allow-list 不作 whitelist 直换词，“I will add the syscall to the allow-list”反而更自然 `<!-- ROW_MINE: ksummit-discuss.messages.351028 -->`

## 84.21 动作明确性原则

- 【Linux社区】Tim Bird 主张宁取语法笨拙但动作具体的词：allow/deny 有清晰心智模型，yes/no 泛词无益 `<!-- ROW_MINE: ksummit-discuss.messages.351030 -->`

## 84.22 具体性优先论

- 【Linux社区】Randy Dunlap 谓 yes/no 不说明所允所拒，应更描述性“like allow/block” `<!-- ROW_MINE: ksummit-discuss.messages.351032 -->`

## 84.23 ACPI与DT议题

- 【Linux社区】2014 Marinas 自认 arm64 高度关注该 KS 议题，忧厂商自创“ACPI+DT mix”，要求 DT 式信息入 ACPI 规范 `<!-- ROW_MINE: ksummit-discuss.messages.351033 -->`

## 84.24 bisect术语之察

- 【Linux社区】Tim Bird 辨 git 中 good/bad 描述结果状态而非动作，并发现“git bisect terms”可改用 fast/slow、fixed/broken `<!-- ROW_MINE: ksummit-discuss.messages.351035 -->`

## 84.25 设备平等之问

- 【Linux社区】Begunkov 复 Rostedt：设备 slave-master 与 subordinate 无根本区别，“Can't see how it fundamentally differs” `<!-- ROW_MINE: ksummit-discuss.messages.351036 -->`

## 84.26 滑坡讽刺批驳

- 【Linux社区】Begunkov 讽 secondary/subordinate 亦含不平等、kill 亦含杀人，斥提案“ill-conceived and pretty arrogant essay” `<!-- ROW_MINE: ksummit-discuss.messages.351037 -->`

## 84.27 替换词划界质疑

- 【Linux社区】Begunkov 追问 subordinate 剥夺权利何以可容而 slave 不容“Where is the line?”，主张以术语清晰为准绳 `<!-- ROW_MINE: ksummit-discuss.messages.351038 -->`

## 84.28 颜色标签辨析

- 【Linux社区】Arvind Sankar 谓 red-black tree 纯任意标签不排斥盲人，而 blacklist/whitelist 颜色实带褒贬内涵 `<!-- ROW_MINE: ksummit-discuss.messages.351039 -->`

## 84.29 语境必要性论

- 【Linux社区】Raschko 斥改词为“smoke and mirrors”：blacklist/whitelist 人尽可解，内核阅读本需领域语境 `<!-- ROW_MINE: ksummit-discuss.messages.351040 -->`

## 84.30 词源内涵之辩

- 【Linux社区】Raschko 谓 CS 语境中这些词无负面内涵，专家从不迁就外行误解，讥动机为“Looking good in the media?” `<!-- ROW_MINE: ksummit-discuss.messages.351041 -->`

## 84.31 动词形式辨析

- 【Linux社区】Kees Cook 辨 allowed（单次许可）与 whitelisted（入持久名单）语义有别，谓英语缺贴切形容词 `<!-- ROW_MINE: ksummit-discuss.messages.351042 -->`

## 84.32 双动词构词解析

- 【Linux社区】Arvind Sankar 解析 allow-list 中 list 方为实义动词、allow 修饰之，习用既久耳朵自会接受 `<!-- ROW_MINE: ksummit-discuss.messages.351043 -->`

## 84.33 blacklist贬义确证

- 【Linux社区】Arvind Sankar 反驳 Raschko：技术上 blacklist 确含贬义，所列皆“bad”设备、驱动、域名 `<!-- ROW_MINE: ksummit-discuss.messages.351044 -->`

## 84.34 回归标签可行性

- 【Linux社区】2014 Iwai 答 Geert 玩笑：给提交加 regression 标签“对维护者不算难负担” `<!-- ROW_MINE: ksummit-discuss.messages.351045 -->`

## 84.35 blacklist禁废之辩

- 【Linux社区】Raschko 表态“支持避用 master/slave、反对避用 blacklist”，谓运动“rides on emotion”，仅禁两三词无补于事 `<!-- ROW_MINE: ksummit-discuss.messages.351046 -->`

## 84.36 行业标准先例

- 【Linux社区】Hemminger 谓 IEEE 802 标准已弃此类措辞且委员会正改 inclusive language，指 bonding master/slave 系 Linux 自创、异于 Cisco/Juniper/Arista `<!-- ROW_MINE: ksummit-discuss.messages.351047 -->`

## 84.37 checkpatch分工

- 【Linux社区】Williams 谢并托 Park 于补丁合入后修 checkpatch，提示措辞“See section 4 'Naming' in coding-style” `<!-- ROW_MINE: ksummit-discuss.messages.351048 -->`

## 84.38 v2补丁流转全文

- 【Linux社区】Williams 发 v2：删 inclusive-terminology.rst（Linus、James 意见），补 master/whitelist 配对替换词，录 Dunlap、Airlie、Cook、Park 四 Ack 与 Olof/Mason/GKH 签名 `<!-- ROW_MINE: ksummit-discuss.messages.351049 -->`

## 84.39 Ack升SoB及建议

- 【Linux社区】Kees Cook 升 Ack 为 Signed-off-by，建议合并 primary/main、拆分 leader/performer，并增 controller/worker `<!-- ROW_MINE: ksummit-discuss.messages.351051 -->`

## 84.40 承诺修checkpatch

- 【Linux社区】Park 复“Agreed, I will do that”，承诺于补丁合入后接手 checkpatch 更新 `<!-- ROW_MINE: ksummit-discuss.messages.351052 -->`

## 84.41 Brown署Review

- 【Linux社区】Mark Brown 署 Reviewed-by（误拼“Reviwed-by”），并建议 controller 与 host 并列 `<!-- ROW_MINE: ksummit-discuss.messages.351053 -->`

## 84.42 Carpenter署SoB

- 【Linux社区】Dan Carpenter 单行提供 Signed-off-by，计入 v2 签名征集（Williams 声明保留主动所署 SoB） `<!-- ROW_MINE: ksummit-discuss.messages.351054 -->`

## 84.43 Ts'o署SoB

- 【Linux社区】Theodore Ts'o 单行提供 Signed-off-by，计入 v2 签名征集 `<!-- ROW_MINE: ksummit-discuss.messages.351055 -->`
