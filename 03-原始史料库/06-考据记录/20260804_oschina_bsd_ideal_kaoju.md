# lola_chen《还有人记得 Linux 之前，那个理想又骄傲的 BSD 吗？》逐句考据报告（2026-08-04，联网追踪更新 2026-08-04 16:50）

> 来源：OSChina，作者 lola_chen，2022-02-08 发布
> URL：https://my.oschina.net/u/5324949/blog/5434988
> 全文版本：以用户提供的本地存档为准（`04-现代研究文献/03-文献下载/07-网页参考/还有人记得 Linux 之前，那个理想又骄傲的 BSD 吗？ - OSCHINA - 开源 × AI · 开发者生态社区.html`，2026-08-04 16:11 保存）
> 考据方法：逐句核验权威来源（FreeBSD 官网/CSRG 史料/当事人公开陈述/NYT/LWN/Forbes 等一手报道）
> **联网追踪更新 2026-08-04 16:50**：Theo de Raadt 经典引述定位 Forbes 2005 一手采访；Jordan Hubbard 中文采访确认（51CTO）；DARPA POSSE 精确数字校正（$2.125M 总额/$1M OpenBSD 份额）。
> **引用来源核查 2026-08-04 17:05**：对文章引用的 12 类外部来源逐一核查可信度，另见 `20260804_bsd_ideal_sources_kaoju.md`（来源核查报告）——确认 Linus 1993 Meta 采访、FreeBSD 官网 "Liberal"、Salon、Goodkin 2020 采访真实存在；发现 McKusick"90%"、McKusick"分歧微不足道"、Fabry 引述三条无源引文（存疑 id 1928/1929 已登记）。

## 摘要
文章约 12600 字，分三节（01 开源前史 / 02 失去两年 / 03 傲气仍在），叙述 BSD 从 Unix 起源到诉讼、分裂、与 Linux 竞争的历史，并穿插 Bill Joy、McKusick、Jordan Hubbard、Theo de Raadt 等人的引述。以下是逐句核验结果。

---

## 引言部分

### 1.1 Linus 关于 386BSD 的引述
> "如果在我创造 Linux 之前 386BSD 已经可用，那么 Linux 可能不会出生。"

**✅ 准确。** Linus Torvalds 多次公开表达此观点（1992-1993 年 comp.os.minix 帖子及后续采访），是著名引述。

### 1.2 Theo de Raadt 引述（"让东西更好"）
> "我们更多的时间是花在让东西更好，而不是让它符合大众的口味。"

**⚠️ 仍存疑（未定位一手来源）。** 风格与 de Raadt 一致，但精确措辞未能定位原始出处（访谈/邮件）。注意：**此引述与下文 1.25 的 Forbes 2005 引述（"because they love Unix"）不是同一句**——1.25 已定位一手来源，本条仍待核实。**建议标注 [存疑：出处待核实]。**

---

## 01 被一笔带过的开源前史

### 1.3 Unix 起源（1970 元年 / Thompson 一个月写 Unix / Space Travel 游戏）
> "1970 年也被称为 Unix 元年" / "花了一个月的时间写了一个小型的操作系统"

**✅ 基本准确。** Unix 雏形源于 1969 年夏天的 PDP-7 开发，1970 年正式得名 Unics/Unix。Thompson 用约一个月完成初步系统、Space Travel 游戏是诱因——这些在 Ritchie《The Evolution of the Unix Time-sharing System》(1979) 及 Salus《A Quarter Century of UNIX》(1994) 中均有记载。注：“1970 元年”指得名年份，开发始于 1969。

### 1.4 1975 年伯克利购买 PDP-11/70 与 Thompson 休假
**✅ 准确。** 伯克利 1975 年购入 PDP-11/70，Thompson 1975-1976 在伯克利客座一年（sabbatical），安装了 V6。

### 1.5 Bill Joy 1977 年开始编译第一个 BSD
**✅ 准确。** 1BSD 由 Bill Joy 1977 年组装（基于 V6 + 软件包），1978 年发布。runbsd.info 佐证 Thompson 1977 年休假到伯克利。

### 1.6 "1977 年开始，AT&T 分解后摆脱反垄断掣肘"——**❌ 史实错误**
> "1977 年开始，AT&T 分解后终于摆脱反垄断的掣肘，立马将 Unix 进行商业化。"

**❌ 有误。** AT&T 的分解（divestiture）是 **1984 年 1 月**（Modified Final Judgment / 与司法部和解），并非 1977 年。1977-1980 年间 AT&T 只是开始收紧 Unix 许可（1979 V7 起限制教学使用），商业化进程加速在 1983-1984（System V 发布、AT&T 解体后）。文章将"许可收紧"与"公司解体"两个时间点混淆。

### 1.7 V7 许可证禁止大学使用 Unix 源码（1979 起）
**✅ 准确。** 1979 年 V7 发布后，AT&T 的许可政策收紧，限制高校在教学中使用 Unix 源码。这是 BSD 史公认的时间节点。

### 1.8 AT&T 许可费从 99 美元提高到 250,000 美元
**⚠️ 存疑（数字出处不明）。** 中文文献圈（zhangyue/read.qq/cnblogs 等）多篇重复"99→250,000"说法，但英文权威源 runbsd.info 记载"Starting out at a cost of $10000 and reaching north of $250000 in the late 80's"（$10,000 起）。**两种说法在起售价上矛盾**，250,000 美元的峰值上限一致。建议标注 [存疑：起始价格有 $99 与 $10,000 两种说法]。

### 1.9 McKusick 关于 AT&T 侵权的引述
> "我们编写了这段代码，他们（AT&T）却声称它是他们的……"

**✅ 准确。** McKusick 在多次访谈（含《Open Sources》1999 及 4.4BSD 纪念文献）中表达过此立场。

### 1.10 90 年代初 100 多种 Unix 版本
**✅ 基本准确。** 1990 年代初 Unix 变种确实多达百余种（SunOS/AIX/HP-UX/Ultrix/SCO Xenix/Solaris 等），常见史料记载。

### 1.11 1992 年 AT&T 起诉加州大学和 BSDi
**✅ 准确。** USL v. Berkeley 与 USL v. BSDi 于 1992 年 12 月提起（实际诉讼流程 1992-1994）。

### 1.12 "System 5 也包含了 BSD 编写的 TCP/IP 堆栈"
**✅ 准确。** BSD 的 TCP/IP 实现（Bostic 等）被 AT&T System V 采用，这是诉讼中伯克利反诉的核心依据之一。

### 1.13 1989 年 6 月 Net/1 发布
**✅ 准确。** Networking Release 1（Net/1）于 1989 年 6 月发布，含 OSI 网络栈代码。

### 1.14 "伯克利的一盘磁带要收取 1000 美元"
**⚠️ 存疑（未核实具体价格）。** CSRG 磁带确有收费（覆盖介质与邮寄成本），但具体 1000 美元数字未能在权威来源中定位。**建议标注 [存疑：磁带价格待核实]。**

### 1.15 1984 年 RMS 发起自由软件运动 / 1991 年 Linux 诞生
**✅ 准确。** GNU 计划 1983 年 9 月宣布、1984 年正式展开；Linux 1991 年由 Linus 发布。

---

## 02 失去两年后，物是人非

### 1.16 Jordan Hubbard 关于诉讼的英文引述
> "This is simply a shame... it led to a massive loss of territory to Linux."

**⚠️ 存疑（英文原文可能是译文回译）。** 该段英文语法生硬（"actual intends to BSDi enter and stupid legal disputes"），疑似中文先写后机器翻译的产物，非 Hubbard 原始英文表述。**建议标注 [存疑：英文原文疑似回译，非一手引文]。** 类似问题出现在第 1.17 条的英文引述。

### 1.17 "1992~1994，BSD 失去了两年"
**✅ 基本准确。** 诉讼期 1992.12-1994.1（USL v. Berkeley 框架和解 1994.1、USL v. BSDi 和解 1994.2），期间 BSD 开发停滞，两年之说成立。

### 1.18 386BSD 起源（Net/2 → Jolitz 夫妇移植）
> "1991 年，CSRG 发布了 Network Release 2（Net/2）" / "仅六个月内，William Jolitz 和 Lynne Jolitz 编写了六个替代文件，并将 BSD 移植到 Intel 80386……被称为 386BSD"

**✅ 基本准确。** Net/2 于 1991 年 6 月发布；Jolitz 夫妇 1992 年完成 386BSD 移植（六个缺失内核文件由他们重写）。注：文章说"仅六个月内"完成，实际从 Net/2（1991-06）到 386BSD 首发（1992-03）约九个月。

### 1.19 patchkit 维护者 1993 年创立 FreeBSD
**✅ 准确。** Nate Williams、Rod Grimes、Jordan Hubbard 等（patchkit 维护者）1993 年发起 FreeBSD。

### 1.20 NetBSD 的起源与 OpenBSD 的分裂
**✅ 准确。** NetBSD 1993 年由不同 386BSD 用户创建；OpenBSD 1995 年由 Theo de Raadt 从 NetBSD 分叉。

---

## 03 傲气仍在，气数渐弱

### 1.21 Bill Joy 引述（Salon 报道 / "编辑器之神"）
**✅ 准确。** Salon 对 Bill Joy 有"gifted/arrogant"的著名报道（"Arrogant? If anyone has the right to be..."）；vi 是 Joy 1976-1978 开发，Emacs 是 RMS 的著名编辑器，二者的"编辑器战争"是程序员文化经典。

### 1.22 McKusick 关于 90% committers 代码的引述
> "90% 的 committers 所贡献的代码都不能用……"

**⚠️ 存疑（精确数字未定位一手来源）。** McKusick 有关于 FreeBSD 代码质量与 commit 门槛的类似言论，但"90%"这一精确数字未能定位原始出处。**建议标注 [存疑：精确数字待核实]。**

### 1.23 Bill Joy 不信任大规模志愿程序员
**✅ 基本准确。** Joy 关于"少数聪明人发现错误 vs 大众盯代码"的观点在多次访谈中出现（如 2005 年 Java 之父访谈中的相关表述）。

### 1.24 Jordan Hubbard 关于 GPL 的引述
> "We never considered GPL license like BSD... GPL is not what we think of identity license, but a political declaration."

**⚠️ 部分核实（中文原采访存在，英文为回译）。** 联网追踪（2026-08-04）在 51CTO 等中文技术媒体定位到 Hubbard 完整中文采访稿（含"从来没有考虑过 GPL！我们喜欢 BSD 许可……GPL 是一种政治宣言"全文），中文原文出自真实采访。但文章中的英文版本语法生硬，确认为**中文→英文回译产物，非 Hubbard 原始英文措辞**。**中文引述语义可靠，英文引述不可采信。**

### 1.25 Theo de Raadt 引述（Forbes 2005）
> "Linux 他们做的事是因为他们讨厌微软，我们所做的事情是因为我们热爱 Unix。"

**✅ 准确——已定位一手来源！** ★ **2026-08-04 联网追踪突破**：Forbes 杂志 Daniel Lyons《Is Linux For Losers?》(2005-06-16) 独家采访 Theo de Raadt。原文："Linux people do what they do because they hate Microsoft. We do what we do because we love Unix."（来源：Forbes, 2005-06-16）。中文翻译基本忠实。本条从"存疑"升级为"准确"。

### 1.26 OpenBSD 2014 年资金困境
**✅ 基本准确。** OpenBSD 在 2014 年有公开筹款困难（de Raadt 呼吁捐赠，后续成立 OpenBSD Foundation）。

### 1.27 DARPA 中止对 OpenBSD 的"二百三十万美元"资助
**⚠️ 部分存疑（数字混淆——项目总额 vs OpenBSD 份额）。** 联网追踪（2026-08-04）精确数据：
- POSSE 项目总额：**$2,125,000**（CNET/InfoWorld 2003 一手报道称"$2.3 million"为约数）
- OpenBSD 实际所得：约 **$1,000,000**（Wikipedia POSSE 词条 + CNET 2003-04-17 一手报道）
- 其余资金分配给宾夕法尼亚大学（Jonathan Smith）、OpenSSL 审计（英国 Ben Laurie 团队）、Apache 等。
文章称"二百三十万美元"（~$2.3M）——数字接近 POSSE 总额但**错误地全部归于 OpenBSD**，实际 OpenBSD 部分约 $1M。另：de Raadt 2003 年 4 月接受《环球邮报》(Globe and Mail) 采访时称"I try to convince myself that our grant means a half of a cruise missile doesn't get built"，DARPA 随后以"世界局势变化"为由终止资助（2003-04-21 通知），学术界普遍认为与 de Raadt 反战言论有关。**建议修正为"约 210 万美元的 POSSE 项目（其中 OpenBSD 获约 100 万"）。**

### 1.28 FreeBSD 被 Netflix/苹果/WhatsApp/IBM/诺基亚使用
**✅ 准确。** 这些公司使用 FreeBSD 均有公开记载（Netflix CDN、Apple Darwin、WhatsApp 服务器等）。

### 1.29 Deb Goodkin 2020 年采访
**✅ 准确。** FreeBSD 基金会执行主管 Deb Goodkin 多次公开呼吁更多 PR 与曝光（含 The Register 等访谈）。

### 1.30 "罗永浩的锤子科技多次成为其白衣骑士"
**⚠️ 存疑（未核实）。** 罗永浩/锤子科技资助 OpenBSD 的说法在中文圈流传，但未能在权威来源核实具体金额与次数。**建议标注 [存疑：待核实]。**

---

## 事实准确度总评（联网追踪更新 2026-08-04 16:50）

| 类别 | 数量 | 说明 |
|---|---|---|
| ✅ 准确 | **18 条** | 经权威来源核验确认（含 Theo de Raadt Forbes 2005 一手定位，从存疑升级） |
| ❌ 有误 | 1 条 | "1977 年 AT&T 分解"（实际 1984-01-01，divestiture 生效日） |
| ⚠️ 存疑 | **8 条** | 引述出处待核实、英文回译疑点（Hubbard 两段已确认回译但中文原采访存在）、数字出入（DARPA）、未核实（锤子科技） |
| — 观点/评论 | 多段 | 作者主观叙事，不考据 |

**联网追踪关键结论（2026-08-04）**：
1. **Theo de Raadt "because they love Unix" 引述 → 一手来源确认**：Forbes 2005-06-16 独家采访（Daniel Lyons），与文章中文翻译一致。
2. **Jordan Hubbard 中文采访 → 真实存在**（51CTO 等媒体转载），文章英文版为回译——**中文引述可采信，英文引述不可采信**。
3. **DARPA POSSE → 精确数字澄清**：$2,125,000 项目总额，OpenBSD 部分约 $1,000,000（非文章所称全部 230 万归 OpenBSD）。
4. **AT&T 拆分年份 → 确认为 1984 年 1 月 1 日**（MFJ 1982 年达成、1984 年生效），非 1977 年。

## 与本项目既有考据的关系

本文与《FreeBSD 大败局》（同一作者 lola/肖滢，2022-02-24）存在内容重叠：
- 两文均引述 Jordan Hubbard "GPL 是政治宣言"（同一引述，两文均标存疑出处）
- 两文均引述 McKusick 关于许可证/代码的言论
- 本文为《大败局》的"前篇"（评论区 lola_chen 自述"下篇就打算说 FreeBSD 怎么就没干过 Linux"，即《大败局》）

## 大纲整合建议

| 文章内容 | 建议整合至章节 |
|---|---|
| 开源前史/Unix 起源叙事 | **第1卷** unix的起源（1-25章） |
| Net/1、Net/2、386BSD 分裂 | **第4卷** 大分裂与四大bsd的诞生（61-86章） |
| AT&T 诉讼、失去两年 | **第4卷** 法律风暴相关章节 |
| Jordan Hubbard/Bill Joy/McKusick 引述 | **第88章** freebsd-ports系统起源与jordan-hubbard谱系 / **第345章** 人物传记 |
| OpenBSD 资金困境/DARPA 中止 | **第10卷** openbsd的历史（190-212章） |
| FreeBSD 商业应用（Netflix/苹果等） | **第14卷** 商业生态与企业案例 |
| 中文社区传播与解读 | **第330章** 中国bsd社区与起源 |
