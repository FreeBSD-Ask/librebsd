# 核查报告：第07卷-freebsd的工程体系重构/第136章-freebsd安全模型的unix-dac与权限机制/index.md

- 源文件：d:\librebsd\05-卷册大纲\第07卷-freebsd的工程体系重构\第136章-freebsd安全模型的unix-dac与权限机制\index.md（93 行，一次完整通读）
- 批次：C362；检查日期：2026-09-13；检查方式：逐文件完整阅读人工核查（辅以权威总纲表比对与 SUMMARY 实测）
- SUMMARY.md 收录：实测第 1362 行（本章索引条目），批次 UNLISTED 旗标失效
- A 占位符：无未填占位（两处〔待核〕为自标截断留痕，并入条目 1）
- B 内容完整性：史观/辨析/文献系统性句中截断（见清单条目 1）
- C 编号与标题：通过（章索引体例，frontmatter 三字段齐备）
- D 格式规范：通过
- E 学术规范：发现 1 处（史观伪标签，见清单条目 2）
- F SUMMARY 一致性：通过（以本章索引名义实收录）

## 问题清单

1. P2 | 行 19-22、26-29、33-37 | 正文系统性句中截断 11 处：史观 4 条全断（行 19 止于 FreeBSD 后、行 20 止于 Linux VS、行 21 自标〔待核：原文截断〕、行 22 止于 便于与现有审计）；辨析 4 条全断（行 26 止于 比其他 UNIX 变体更、行 27 自标〔待核〕、行 28 止于 LSM 200、行 29 止于 但实）；文献 4 条中 3 条截断（行 35 止于 Watson R、行 36 尾部空挂 FreeBSD Project.、行 37 止于 Implementation o）＋行 34 孤行残句 FreeBSD 社区论——仅行 21/27 两处自标待核，余 9 处无任何标记，章索引的分析性内容大半不可用 | 逐行可见 | 回源补全或删除断条
2. P3 | 行 19-22 | 史观标签四处伪标签：总纲第 1 条——项目统摄史观（两处，权威第 1 条为一切真历史都是古代史，项目统摄史观非名目）、总纲第 21 条——密码学（权威第 21 条为革命与改革是历史方法论的分歧）、总纲第 3 条——形式主义膨胀（权威第 3 条为不存在进步只有权力再分配） | 比对 remediation_zongang_canonical.md 权威表 | 去号或改挂正确名目

- 结论：存在问题 2 项（P0 0、P1 0、P2 1、P3 1）

## 补充说明（正样本与复核留痕）

- 要点 5 条完整且事实密度高，时间锚逐一与公开记录一致：12 权限位构成（9 基本位＋setuid/setgid/sticky）、jail 首现 4.0-RELEASE（2000-03-14）与 Kamp/Watson SANE 2000 论文、Capsicum USENIX Security 2010 论文、9.0-RELEASE（2012-01-12）GENERIC 集成、Dawidek 2013-04 基金会＋Google 资助工程化（casperd/libcapsicum）、CHERI 剑桥＋SRI 与 Arm Morello（2021）——无一处发现错讹。
- 行 12 securelevel 级别数误传自纠：存疑脚注指明原文误作四个级别，依 FreeBSD Handbook 更正为五级别（-1/0/1/2/3）并逐级给出语义——误传纠正范式。
- PODCAST 三期与章主题契合度极高：YouTube E04LxKiu79I（McKusick An Overview of Security in the FreeBSD Kernel）正中本章，覆盖 securelevels 结构性缺陷自承（单用户态启动脚本绕过）、不可变标志的 1980s CSRG 入侵轶事（荷兰入侵者上门探访）、Yarrow→Fortuna 随机数演进（含 RdRand 掺假无确证的自警）、POSIX 1003.1e ACL 被拖延致死的标准政治史、audit Target 泄露案例与每夜 setuid 差分实践、capsicum 与 pav（Dawidek）归属——一手访谈驱动的章内容，质量上乘。
- EP88（2015-05-06）Ed Schouten CloudABI 一手访谈（自述首次公开谈论）与 Capsicum 主题直接相关；/dev/urandom 回退弱熵的发现路径完整。
- PODCAST 块史观 7 条名目全部正确（总纲 10/13/5/10/3/8/3，其中总纲 3 用作 不存在进步只有权力再分配 与权威名目一致——与正文史观的伪标签用法形成对照）；存疑脚注 5 处（Percival 提案未落地单一来源、rc.d 移除预期未如期发生、Francois Toujour→François Tigeot 转写辨正等）处理规范。
- 行 26/28/29 三条辨析虽截断但立论正确：DAC 是叠加基座而非被替代、MAC 框架与 SELinux 的 mac_flask 模块关系、OpenBSM 系 clean-room 重实现以规避 CDDL 兼容问题——修改线补全时应保留论点。
