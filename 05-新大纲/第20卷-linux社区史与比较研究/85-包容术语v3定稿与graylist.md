# 85 【Linux社区】包容术语v3定稿与graylist

> 来源：ksummit-discuss p137（50 封全读，2020-07 术语补丁 v3 流转+blacklist 语言学讨论，夹杂 2014-05 档案信）
> 判定：31 CAND / 19 NV。主题分布：PM依赖框架设计 1、术语替换词修订 1、术语文档去留 1、术语补丁质疑 1、术语补丁背书 1、术语补丁v3定稿 1、ARM旧板DT转制 1、术语替换泛滥忧 1、文档检查归属 3、术语全球社区论 1、graylist语义界定 1、graylist去留定调 1、0-day文档检查 1、门控机制风险论 1、文档检查替代案 1、文档检查收敛 1、术语文化引证 1、seccomp用语批评 1、Fixes标签机制 1、blacklist存废议 1、SoundWire换词 1、术语动词形式 1、术语语法商榷 1、allowlist语义辨 1、git签名注记设想 1、全量替换之害论 1、换词分权定调 1、术语动词方案 1、sed替换可行性 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p137（实锚 pk 351056-351104）的逐封提取（31 CAND / 19 NV），全 29 块采用**单行摘要体例**（丙型）：每块由“## 85.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 85.1 【Linux社区】PM依赖框架设计

- 【Linux社区】Mark Brown 主张设备依赖引用应放进抽象该关系的 API，ACPI _DEP“此设备依赖彼设备”怪例则“baked into however ACPI is hooked in” `<!-- ROW_MINE: ksummit-discuss.messages.351056 -->`

## 85.2 【Linux社区】术语替换词修订

- 【Linux社区】Kees Cook 将 Ack 升格为 Signed-off-by；商定合并 primary/main、拆 leader/performer 为 leader/follower 与 director/performer、增 controller/worker，Williams 全盘采纳 `<!-- ROW_MINE: ksummit-discuss.messages.351057 -->`

## 85.3 【Linux社区】术语文档去留

- 【Linux社区】Dan Williams 澄清弃 inclusive-terminology.rst 系 James 提议、Linus 同意；SeongJae Park 将改其检查器指向 coding-style；老驱动子系统可如常抵触搅动 `<!-- ROW_MINE: ksummit-discuss.messages.351058 -->`

## 85.4 【Linux社区】术语补丁质疑

- 【Linux社区】Joe Perches 追问“Linus 在何处公开说过无必要”，建议引 SeongJae 的 scripts/deprecated_terms.txt，并主张存量代码应一律不动 `<!-- ROW_MINE: ksummit-discuss.messages.351059 -->`

## 85.5 【Linux社区】术语补丁背书

- 【Linux社区】James Bottomley 补 Acked-by 并给出 Linus 表态出处链接 tech-board-discuss 2020-July/000412.html，正面回应 Perches 质询 `<!-- ROW_MINE: ksummit-discuss.messages.351060 -->`

## 85.6 【Linux社区】术语补丁v3定稿

- 【Linux社区】v3 全文含 5 Ack+1 Review+9 Sign-off 名单（Ted Ts'o、Shuah、Corbet、Greg KH 等）与 coding-style.rst 20 行替换词表及 ABI/既有规范例外条款 `<!-- ROW_MINE: ksummit-discuss.messages.351063 -->`

## 85.7 【Linux社区】ARM旧板DT转制

- 【Linux社区】Rob Herring 称经 Linus Walleij 清 plat 头文件后 versatile 多平台化已趋直接，公开 versatile-multiplatform 分支，剩 PCI 与 LED，瓶颈为通用 DT PCI 代码 `<!-- ROW_MINE: ksummit-discuss.messages.351067 -->`

## 85.8 【Linux社区】术语替换泛滥忧

- 【Linux社区】Mauro 预警合并后“邮件列表将被替换补丁淹没”，media 术语多源自 I2C master/slave 与 DiSEqC 规范，应先改规范再改代码 `<!-- ROW_MINE: ksummit-discuss.messages.351068 -->`

## 85.9 【Linux社区】文档检查归属

- 【Linux社区】Mike Rapoport 点破症结：开发者通常只跑 checkpatch 而不跑 kernel-doc，故有把文档检查塞进 checkpatch 的动议 `<!-- ROW_MINE: ksummit-discuss.messages.351069 -->`
- 【Linux社区】Joe Perches 明确拒绝在 checkpatch 内跑 kernel-doc -none：“checkpatch 只跑补丁，该用为此设计的工具” `<!-- ROW_MINE: ksummit-discuss.messages.351070 -->`
- 【Linux社区】Rapoport 质疑 Perches 偏好的 patch 1260408“看不出如何减少 kernel-doc 告警、如何让人自查新告警” `<!-- ROW_MINE: ksummit-discuss.messages.351075 -->`

## 85.10 【Linux社区】术语全球社区论

- 【Linux社区】Shuah Khan 以“社区是全球的，英语并非处处相同”支持统一词汇，并追问 graylist 含义引出后续讨论 `<!-- ROW_MINE: ksummit-discuss.messages.351071 -->`

## 85.11 【Linux社区】graylist语义界定

- 【Linux社区】Mark Brown 释 graylist 为介于 allow/deny 之间“不想拒绝但可加查”的中间态 `<!-- ROW_MINE: ksummit-discuss.messages.351072 -->`

## 85.12 【Linux社区】graylist去留定调

- 【Linux社区】James Bottomley 考证 greylisting 源自邮件反垃圾与“grey area”习语，结论“与问题性用法关联太远，留着不动” `<!-- ROW_MINE: ksummit-discuss.messages.351073 -->`

## 85.13 【Linux社区】0-day文档检查

- 【Linux社区】Andrew Lunn 主张 0-day 类系统更合适：会套用补丁、对整棵源码树跑工具、能从旧告警中分辨新增告警 `<!-- ROW_MINE: ksummit-discuss.messages.351076 -->`

## 85.14 【Linux社区】门控机制风险论

- 【Linux社区】Ted Ts'o 论 2014“Move Fast and Oops Things”：xfs/ext4 及 SuSE btrfs 已用门控分级启用，但涉 ABI/文件系统格式须先定型；Google/Facebook 单树优势不可平移上游 `<!-- ROW_MINE: ksummit-discuss.messages.351078 -->`

## 85.15 【Linux社区】文档检查替代案

- 【Linux社区】Joe Perches 表态更偏好 patchwork 1260408 补丁（下文证为 Masahiro Yamada 的 W=d 方案） `<!-- ROW_MINE: ksummit-discuss.messages.351080 -->`

## 85.16 【Linux社区】文档检查收敛

- 【Linux社区】Valdis 录明认可 Masahiro Yamada 在 W=123 外加 W=d 选项“比我原补丁更好”，Perches 亦表同意，此线争论收束 `<!-- ROW_MINE: ksummit-discuss.messages.351081 -->`

## 85.17 【Linux社区】术语文化引证

- 【Linux社区】Linus Walleij 附 Signed-off-by 并荐 Hofstadter 1985 讽文“A Person Paper on Purity in Language”，称其使自己确信职业语言之要 `<!-- ROW_MINE: ksummit-discuss.messages.351082 -->`

## 85.18 【Linux社区】seccomp用语批评

- 【Linux社区】Andy Lutomirski 指 v3 新措辞“并不比旧的好多少”并称“I'll send a patch”，举 seccomp 手页已用 allow-list/deny-list `<!-- ROW_MINE: ksummit-discuss.messages.351084 -->`

## 85.19 【Linux社区】Fixes标签机制

- 【Linux社区】2014 档案：Herland 答 Iwai——漏打 Fixes: 则反向映射尽失，除非事后以 git-notes 补注，但复陷 notes 共享难题；并录 Junio 的 Fixes: 标准化与 bisect 摘樱桃设想 `<!-- ROW_MINE: ksummit-discuss.messages.351089 -->`

## 85.20 【Linux社区】blacklist存废议

- 【Linux社区】Pavel Machek 质疑 blacklist/whitelist“何来不包容”，称 blocklist/denylist 并不适合内核现有用法，要求先 grep 实际用例 `<!-- ROW_MINE: ksummit-discuss.messages.351090 -->`

## 85.21 【Linux社区】SoundWire换词

- 【Linux社区】Vinod Koul 称该子系统因 MIPI 规范定义 Master/Slave 而有逾千处 slave，“计划直接替换、不等 MIPI 改规范”，倡与利益相关方商定后批量换 `<!-- ROW_MINE: ksummit-discuss.messages.351093 -->`

## 85.22 【Linux社区】术语动词形式

- 【Linux社区】Takashi Iwai 实查树内大量 whitelisted/blacklisted 被动式两例，正以“Foo is in denylist”替换但不确定“非白名单可加载”句式，附条件 Acked-by `<!-- ROW_MINE: ksummit-discuss.messages.351095 -->`

## 85.23 【Linux社区】术语语法商榷

- 【Linux社区】Julia Lawall 指“in denylist”不合语法须加冠词，试拟“foo is denylisted”“not in the allowList”等可行形式 `<!-- ROW_MINE: ksummit-discuss.messages.351098 -->`

## 85.24 【Linux社区】allowlist语义辨

- 【Linux社区】Iwai 澄清两例分属不同驱动，并点出关键语义：“不在 allowlist 不意味着在 denylist，只是未知” `<!-- ROW_MINE: ksummit-discuss.messages.351099 -->`

## 85.25 【Linux社区】git签名注记设想

- 【Linux社区】2014 档案：Herland 答 Couder“签名 notes/replace”之问——可用指向相应 ref 的签名 tag，但 notes 能否穿透 tag 取对象、replace 语义如何处理均存疑 `<!-- ROW_MINE: ksummit-discuss.messages.351100 -->`

## 85.26 【Linux社区】全量替换之害论

- 【Linux社区】James Bottomley 定调：建议只面向增量非强制翻旧账，树内相关词逾 10 万处，全改将大规模搅动妨害开发，“弊远大于利” `<!-- ROW_MINE: ksummit-discuss.messages.351101 -->`

## 85.27 【Linux社区】换词分权定调

- 【Linux社区】Dan Williams 确认落地节奏交子系统自决：“与其他 coding-style 清理一样，按你维护的子系统最合理方式分期” `<!-- ROW_MINE: ksummit-discuss.messages.351102 -->`

## 85.28 【Linux社区】术语动词方案

- 【Linux社区】Josh Triplett 献 blocklist 动词化用法“foo is blocklisted”“block foo”“deny foo”，第二例拟“allow loading cards not on the passlist” `<!-- ROW_MINE: ksummit-discuss.messages.351103 -->`

## 85.29 【Linux社区】sed替换可行性

- 【Linux社区】Iwai 收束小线：本望 sed 一键替换，“看来还是得改写文本”，机械替换不可行 `<!-- ROW_MINE: ksummit-discuss.messages.351104 -->`
