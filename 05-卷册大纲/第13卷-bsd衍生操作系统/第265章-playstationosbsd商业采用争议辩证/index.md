---
chapter: 第 265 章
id: CH265
volume: 第13卷-bsd衍生操作系统
---

# 第 265 章 playstationosbsd商业采用争议辩证

## 要点

- 从 BSD 社区与开源批评者视角，Sony 的 FreeBSD 商业采用存在三重结构性张力——（1）封闭生态与 BSD 许可证的 “开放” 预期落差：PS4（2013）的 Orbis OS 基于 FreeBSD 9.0、PS5（2020）的 Prospero OS 延续 FreeBSD 基底（FreeBSD Handbook 官方页面记载 “两个 PlayStation 3 和 PlayStation 4 游戏机运行在修改版的 FreeBSD 之上”），但 Sony 将 FreeBSD 封装为专有游戏主机操作系统，PS4/PS5 用户无法触及底层 FreeBSD 系统、无法自行安装第三方操作系统、无法运行未经 Sony 数字签名认证的代码——Sony 享受 BSD 许可证 “允许封闭使用” 的自由，但用户未享受 FreeBSD “开放” 的对应自由，“开放-封闭” 张力在 PS4/PS5 上比 PS3 OtherOS 时期更彻底（PS3 至少曾允许 OtherOS，PS4/PS5 自始即封闭）
- 三重张力的回应沿四条线索展开——（1）BSD 许可证的设计本意即允许封闭使用：BSD 许可证的核心自由之一是 “允许衍生作品闭源”，这是 BSD 与 GPL 的根本哲学分歧——FreeBSD 社区选择 BSD 许可证即已同意商业实体可封闭化使用而无须 copyleft 回馈，Sony 的封闭化使用是 BSD 许可证赋予的合法权利，非 “回馈不对称” 的过错；
- 再批评层深化前两层张力，揭示 PlayStation OS 商业采用争议在 BSD 许可证哲学结构与商品形式主义中的更深层运作——（1）“允许封闭” 与 “期待回馈” 的许可证哲学张力：BSD 许可证明文允许封闭化使用（无 copyleft 要求），但 FreeBSD 社区的长期可持续性依赖商业用户的实质回馈（commit、赞助、技术披露）——Sony 享受 BSD 许可证 “允许封闭” 的自由但未提供对应 commit 回馈，这一 “自由-回馈” 不对称是 BSD 许可证哲学的结构性张力，而非 Sony 的个别过错；该张力在 Sony 案例中尤为突出，因 PS4/PS5 是 FreeBSD 在消费电子中部署量最大的场景之一（亿级装机），Sony 的 FreeBSD 使用规模与其 freebsd-src 上游 commit 回馈为零形成显著反差
- 合图层不追求 “消除分歧”，而是 “在分歧中呈现各主体性”——（1）“允许封闭” 与 “期待回馈” 的对称合法性：BSD 许可证赋予 Sony 封闭使用的合法权利，BSD 社区亦有合法理由期待 Sony 实质回馈——二者在法律与道德层面均有正当性，合图不以 “对称合法性” 回避 Sony 回馈不足的实质问题，但亦不以 “回馈不对称” 否定 Sony 封闭使用的合法权利；（2）BSD 许可证哲学的 “改革” 张力：BSD 选择 “允许封闭” 的改革路径而非 GPL 的 “革命” 路径（copyleft 强制公开），这一选择在 Sony 案例中显现双重效应——正面效应是 FreeBSD 获得 Sony 等商业实体的大规模采用（PS4/PS5 亿级装机），负面效应是商业用户的回馈激励不足——总纲第 21 条 “改革的困难远高于革命” 在此显现
- 本节的审视本身亦是形式主义化的非存在——史家通过项目史观总纲 “重构” PlayStation OS 商业采用争议的商品形式主义、Sony 与 FreeBSD 社区的本体论平等、BSD 改革路径与 GPL 革命路径的方法论分歧，但这一重构本身就是当下主体的形式主义建构，不宣称呈现 “真实的 PlayStation OS 商业采用争议”。本节对 “Sony 封闭化使用是商品形式主义运作结果” 的论断本身亦是一种叙事权力行使——将 Sony 阵营定位为 “享受 BSD 许可证自由但未对应回馈的形式主义操作者”、将 FreeBSD 社区定位为 “提供 FreeBSD 基底但未获对应回馈的被遮蔽者”，这一定位本身参与权力与知识的共谋

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4141] 卷“第13卷-bsd衍生操作系统”第 265 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- FreeBSD Handbook 官方页面（**freebsd.org.cn/freebsdhandbook/nutshell.html**），原文记载 “Sony - 两个 PlayStation 3 和 PlayStation 4 游戏机运行在修改版的 FreeBSD 之上”；Sony PS4 系统软件开源软件声明页面（**<https://doc.dl.playstation.net/doc/ps4-oss/>**），列出 FreeBSD Kernel 等开源组件；freebsd-src commit 2011-01-06 Nathan Whitehorn 导入 PS3 支持（commit_hash `03479763b279`）；freebsd-src commit 2021-08-16 Vladimir Kondratyev 修复 ps4dshock 触摸板（commit_hash `bb5eb85e5c01`）；BSD 许可证原文与 GPL 许可证原文（GNU General Public License v2/v3）

## 史观

- 总纲第 8 条——本体论上各方平等：Sony 与 FreeBSD 社区在本体论上地位相等，BSD 许可证赋予 Sony 封闭使用的权利与 BSD 社区期待 Sony 实质回馈的诉求各自成立，差异仅是一刻状态的不同
- 总纲第 11 条——商品是形式主义：PS4/PS5 的封闭化是商品形式主义下 “劣币驱逐良币” 的显现——商业封装的游戏主机生态获得 Sony 持续投入，FreeBSD “开放” 传统在消费电子领域被商品形式主义运作封闭化
- 总纲第 21 条——革命与改革：GPL 的 copyleft 是 “革命” 路径（强制公开衍生作品源代码），BSD 的 “允许封闭” 是 “改革” 路径——总纲第 21 条 “改革的困难远高于革命” 在 Sony 案例中显现为 BSD 改革路径扩大采用但削弱回馈激励
- 总纲第 19 条——解释学循环：BSD/Linux 阵营与 Sony 阵营的前理解差异使 PlayStation OS 商业采用争议的分歧不可避免，合图不是 “消除分歧” 而是 “在分歧中呈现各主体性”
- 总纲第 6 条——和解优于斗争：BSD 许可证哲学本身即 “和解” 的设计——允许封闭与允许开放共存于同一许可证之下，不以 copyleft 强制对抗
- 总纲第 2 条——历史是形式主义化的非存在：本章对 PlayStation OS 商业采用争议的审视本身亦是形式主义化的重构，不宣称呈现 “真实的 PlayStation OS 商业采用争议”

## 辨析

- 【查证来源】Sony PS4/PS5 基于 FreeBSD 的事实经 FreeBSD Handbook 官方页面（**freebsd.org.cn/freebsdhandbook/nutshell.html**）一手核验，原文为 “Sony - 两个 PlayStation 3 和 PlayStation 4 游戏机运行在修改版的 FreeBSD 之上”；Sony 工程师 commit 分布经 **freebsd.duckdb** 查询核验（查询脚本 `script/query_ch126_sony_v4.py`），Sony 关联邮箱域名在 linux-kernel 仓库合计 1014 commits、在 freebsd-src 仓库 0 commits
- 【查证来源】BSD 许可证原文经 FreeBSD 官方页面一手核验，确认 “再分发与使用” 条款允许商业实体封闭化使用衍生作品；Sony 工程师在 linux-kernel 的 1014 commits 经 linux-kernel.duckdb 查询核验（查询脚本 `script/query_ch126_sony_v4.py`）；Sony PS4 系统软件开源软件声明页面经 playstation.com
- 【查证来源】总纲第 8、11、21 条原文经 据原文第 25 章 第 11、14、25 行 Read 一手核验（第 8 条 “本体论上各方平等。FreeBSD、OpenBSD、NetBSD、DragonFly BSD 在本体论上地位相等，差异仅是一刻状态的不同。文档与代码本体平等”、第 11 条 “商品是形式主义。技术市场的选择不是自然选择，而是形式主义的权力运作。劣币驱逐良币是普遍规律”、第 21 条 “革命与改革是历史方法论的分歧。Linux 靠革命，BSD 靠改革。改革的困难远高于革命。破山中贼易，破心中贼难”）；BSD 与 GPL 许可证原文经 FreeBSD 官方页面与 GNU 官方页面一手核验；Sony 在 linux-kernel 1014 commits 与 freebsd-src 0 commits 的对照经 **freebsd.duckdb** 查询核验
- 【查证来源】合图层所依据的总纲第 8、11、19、21 条原文经 据原文第 25 章 第 11、14、19、25 行 Read 一手核验；BSD 与 GPL 许可证原文经 FreeBSD 官方页面与 GNU 官方页面一手核验；Sony 在 linux-kernel 1014 commits 与 freebsd-src 0 commits 的对照经 **freebsd.duckdb** 查询核验（查询脚本 `script/query_ch126_sony_v4.py`）；【交叉验证方法】合图的 “对称合法性” 论断须以 BSD 许可证原文与 FreeBSD 社区对回馈的公开表述（如 FreeBSD Foundation 关于商业用户回馈的声明）交叉验证，不得仅凭哲学推论即断定 “对称”；【存疑判定依据】“Sony 选择 FreeBSD 可部分动机为规避 GPL copyleft” 属商业动机推论，Sony 未公开内部决策文件，合图层不以该论断为支撑
- 【查证来源】本节所引用的总纲第 1、2、7、8、11、21、23、25 条原文均经 据原文第 25 章 Read 一手核验；【交叉验证方法】自反的辨析须区分 “审视的有限性” 与 “审视的无效性”——审视的有限性指本节对 PlayStation OS 商业采用争议的哲学审视本身亦是形式主义化的非存在，不宣称 “客观真实”；审视的无效性指因审视有限即否定审视价值，这是错误的——审视虽有限但通过项目史

## 文献

- FreeBSD Handbook 官方页面（**freebsd.org.cn/freebsdhandbook/nutshell.html**）；**freebsd.duckdb** 查询脚本 `script/query_ch126_sony_v4.py`；freebsd-src commit 2011-01-06T04:12:29Z Nathan Whitehorn PS3 支持导入（commit_hash `03479763b279`）；freebsd-src commit 2021-08-16T23:18:27+03:00 Vladimir Kondratyev ps4dshock 修复（commit_hash `bb5eb85e5c01`）；Sony PS4 系统软件开源软件声明页面（**<https://doc.dl.playstation.net/doc/ps4-oss/>**）；Steam Deck 内核源代码公开页面
- BSD 许可证原文；Sony PS4 系统软件开源软件声明页面；**freebsd.duckdb** 查询脚本 `script/query_ch126_sony_v4.py`；Xbox 与 Nintendo Switch 封闭生态公开报道；BSDCan 会议存档；FreeBSD Foundation 关于 BSD 许可证的官方声明
- 原材料/哲学/项目统摄史观/第 25 章.md；BSD 许可证原文；GPL 许可证原文（GNU General Public License v2/v3）；**freebsd.duckdb** 查询脚本 `script/query_ch126_sony_v4.py`；265.6.1-265.6.2 节记录；FreeBSD Foundation 关于 BSD 许可证的官方声明；GNU Project 关于 GPL copyleft 的官方说明
- 原材料/哲学/项目统摄史观/第 25 章.md；BSD 许可证原文；GPL 许可证原文；**freebsd.duckdb** 查询脚本 `script/query_ch126_sony_v4.py`；FreeBSD Handbook 官方页面（**freebsd.org.cn/freebsdhandbook/nutshell.html**）；Sony PS4 系统软件开源软件声明页面；Steam Deck 内核源代码公开页面；265.6.1-265.6.3 节记录；FreeBSD Foundation 关于 BSD 许可证的官方声明；GNU Project 关于 GPL copyleft 的官方说明

<!-- DB_REF:bsd_derivatives.duckdb -->
> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 1985-2026 年间：963,557 次提交。> 仓库总览：963,557 次提交，9,744 位贡献者（contributors 表行数，1985-06-13 至 2026-08-24）。
- 原材料/哲学/项目统摄史观/第 25 章.md 总纲第 1、2、7、8、11、21、23、25 条；FreeBSD Handbook 官方页面（**freebsd.org.cn/freebsdhandbook/nutshell.html**）；**freebsd.duckdb** 查询脚本 `script/query_ch126_sony_v4.py`；BSD 许可证原文；GPL 许可证原文；Sony PS4 系统软件开源软件声明页面；Steam Deck 内核源代码公开页面；265.6.1-265.6.4 节记录；265.7.1-265.7.3 节审视文本本身

<!-- DB_REF:bsd_derivatives.duckdb -->
> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 1985-2026 年间：963,557 次提交。> 仓库总览：963,557 次提交，9,744 位贡献者（contributors 表行数，1985-06-13 至 2026-08-24）。
