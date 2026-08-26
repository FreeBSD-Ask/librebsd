---
chapter: 第 10 章
id: CH10
volume: 01
---

## 要点

- 1973 年 UNIX V4 引入多用户分时后，root（UID 0）与普通用户的二元特权模型成为系统安全的核心结构；root 拥有绕过文件权限检查、绑定特权端口、执行关键系统调用等全部特权，普通用户权限受 9 位 rwx 权限位约束；该模型将 Multics 的环形保护（ring 0-7）与可信计算基（TCB）极简化为二元判定，符合 UNIX“做一件事并做好”的工程哲学
- UNIX 密码存储历经三阶段演化——V1-V3（1971-1973）存储于 `/etc/passwd` [^oi4-fn]、V4-V6（1973-1975）尝试简单加密（ROT13 等被快速攻破）、V7（1979 年）引入基于 DES 25 轮迭代的 **crypt(3)** 与 12 位 salt 机制；1978-1979 年间 UNIX V6 密码文件被攻破事件直接触发 V7 密码散列升级；**crypt(3)** 由 Robert Morris（罗伯特·莫里斯） 与 Ken Thompson 共同设计，使相同密码因不同 salt 产生不同散列，抵御预计算字典攻击
- Morris & Thompson 1979 年 CACM 论文《Password Security: A Case History》是密码散列演化的最权威学术记录，原作于 1978-1979 年间，描述了 UNIX V1 至 V7 密码存储方案的全部演化过程；该论文后被 4.4BSD 系统管理员手册第 17 章（SMM: 17）再版，成为 BSD 谱系密码安全的权威一手史料；论文记录了多种早期方案被攻破的过程，最终在 V7 引入 DES **crypt(3)** 与 12 位 salt
- root 二元特权模型与 DES **crypt(3)** 散列机制共同构成 Research UNIX 留给 BSD 的两大安全基因——root 模型延续至 4.4BSD-Lite 与 386BSD，**crypt(3)** 直接被 FreeBSD 1.0-4.x 继承直至 1990 年代末被 MD5-based **crypt(3)** 与 bcrypt 替代；root 模型的“全有或全无”缺陷催生 BSD 后世 **jail(8)**（4.4BSD-Lite2 后 FreeBSD 引入）、**securelevel(7)**、Capsicum（Watson et al. 2010）等细粒度特权机制；**crypt(3)** 的 salt 思想影响后续 bcrypt、scrypt、argon2 等现代密码散列设计
- UNIX 哲学文本的塑造者包括 McIlroy、Pike、Kernighan、Raymond 等，但还包括 Bell Labs 内部通信参与者、USENIX 演讲者、邮件列表讨论者；多数边缘塑造者姓名未被记录

## 史观

- 总纲第 2 条——实践先于理论：root 模型在缺乏形式化安全规格下演化定型，工程实践先于安全理论总结；总纲第 14 条——哲学思潮：二元特权模型为 UNIX 极简化哲学在安全维度的工程转译
- 辨析：root 模型定型的精确版本（V3 vs V4）需考据——按 Ritchie 1984 BLTJ 与 Salus 1994 两方独立来源交叉印证为 V4（1973 年）多用户分时引入后；“1972 
- 总纲第 1 条——偶然性改写历史：1978-1979 年 V6 密码文件攻破事件偶然触发 V7 散列升级，重塑 UNIX 密码安全范式；总纲第 17 条——软件工程：**crypt(3)** 的设计与 salt 机制为密码安全工程提供范本
- 辨析：[考据脚注：经 Morris & Thompson 1979 CACM 论文一手表述确证，DES **crypt(3)** 引入于 1979 年 V7
- 总纲第 2 条——实践先于理论：Morris & Thompson 论文是对 V1-V7 密码演化的事后理论总结，工程实践（攻破-升级循环）先于学术记录；总纲第 10 条——边缘者贡献：Robert Morris 作为 Bell Labs 安全研究者，其贡献长期被 Ritchie/Thompson 的光环遮蔽
- 辨析：CACM 1979 论文与 4.4BSD SMM: 17 是否完全一致需对照—
- 总纲第 25 条——终结与延续：root 模型与 **crypt(3)** 在 V7 定型后延续至 BSD 长达二十余年，是 Research UNIX 主导期终结后 BSD 分支延续的核心安全遗产；总纲第 4 条——分离与聚合：root 二元特权与文件权限 rwx 分离为两层安全判定，再通过 setuid 机制聚合为可执行的特权切换
- 辨析：root 模型与 **crypt(3)** 对 BS
- 总纲第 10 条——边缘者贡献：UNIX 哲学非个人著作，而是集体讨论的结晶
- 辨析：边缘塑造者的具体贡献难以量化；0 信任原则要求不臆测贡献归属
- 文献：TUHS 邮件列表早期帖；USENIX ; login: 期刊；Kernighan 2019 ［A］

## 辨析

- root 模型定型的精确版本（V3 vs V4）需考据——按 Ritchie 1984 BLTJ 与 Salus 1994 两方独立来源交叉印证为 V4（1973 年）多用户分时引入后；“1972 年定型”的说法缺乏一手史料佐证 [考据脚注：经 Ritchie 1984 BLTJ 与 Salus 1994 两方独立来源交叉印证，root 模型定型于 V4（1973 年），“1972 年定型”的说法
- [考据脚注：经 Morris & Thompson 1979 CACM 论文一手表述确证，DES **crypt(3)** 引入于 1979 年 V7，而非 1976 年；V1-V3 明文存储的说法存在叙事分歧，部分来源指向 V4 起已有简单加密，穷尽考据后仍无法确证；salt 机制的设计灵感来源（是否受 IBM VM/370 密码机制影响）需进一步考据——已尝试：关键词"IBM VM/370 p
- CACM 1979 论文与 4.4BSD SMM: 17 是否完全一致需对照——SMM: 17 可能含 4.4BSD 时期的补充说明；Morris & Thompson 1979 论文中描述的“V6 密码文件被攻破”事件的具体细节（攻破者身份、攻破方法）需考据；论文中提及的早期方案（ROT13 等）是否真在 V4-V6 中部署存在回忆差异风险
- 文献：Morris R, Thompson K 1
- root 模型与 **crypt(3)** 对 BSD 安全基因的“史源意义”是否被夸大需辨析——BSD 安全基因亦受 Multics 间接影响（详见本章对 Multics 统一抽象路径的比较）与 4.2BSD 网络栈引入后的安全扩展影响；**crypt(3)** 被 MD5/bcrypt 替代的确切时间需考据（FreeBSD 4.x 时期引入 MD5-based，OpenBSD 率先引入 bcr
- 边缘塑造者的具体贡献难以量化；0 信任原则要求不臆测贡献归属
- 文献：TUHS 邮件列表早期帖；USENIX ; login: 期刊；Kernighan 2019 ［A］

## 文献

- Ritchie D M 1984"The Evolution of the Unix Time-sharing System" (AT&T Bell Laboratories Technical Journal 63 No. 6 Part 2 pp. 1577-1593)；4.4BSD SMM: 16《On the Security of UNIX》；Salus 1994"A Quarter Century of UNIX"；bsd_commits.db：freebsd-src commit `5b81b6b301437eb9a6df491c829475bd29ae5d6c`（1993-06-
- Morris R, Thompson K 1979 CACM"Password Security: A Case History"Vol. 22 No. 11 pp. 594-597；4.4BSD SMM: 17《Password Security: A Case History》；UNIX V7 源代码 `usr/src/lib/crypt.c`；Salus 1994 ［A］
- Morris R, Thompson K 1979 CACM"Password Security: A Case History"Vol. 22 No. 11 pp. 594-597；4.4BSD SMM: 17《Password Security: A Case History》；docs.freebsd.org/44doc/smm/17.password/ ［A］
- Watson et al. 2010"Capsicum: Practical Capabilities for UNIX" (USENIX Security)；Poul-Henning Kamp 1998 MD5-crypt；Provos & Mazières 1999 bcrypt；bsd_commits.db：freebsd-src commit `5b81b6b301437eb9a6df491c829475bd29ae5d6c`（1993-06-12）与 `26f9a76710a312a951848542b9ca1f44100450e2`（1994-05-25）［A］
- TUHS 邮件列表早期帖；USENIX ; login: 期刊；Kernighan 2019 ［A］
- 同 6.8.1；Campbell-Kelly 2007 综述 ［C］
- Salus 1994；Campbell-Kelly 2007；Raymond 2003 附录 [考据脚注：经 Salus 1994"A Quarter Century of UNIX"与 Campbell-Kelly 2007 原著交叉验证确证。]
- TUHS 邮件列表；AT&T Archives 在线目录；USENIX ; login: 期刊早期卷期 ［A］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。