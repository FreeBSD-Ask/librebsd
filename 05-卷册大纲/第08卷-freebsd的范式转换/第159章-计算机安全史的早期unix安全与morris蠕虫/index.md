---
chapter: 第 159 章
id: CH159
volume: 08
---

# 第159章 计算机安全史的早期unix安全与morris蠕虫

## 要点

- 还原 1988 年 11 月之前互联网的整体安全图景——1980 年代末互联网约有 6 万台主机连接，主要分布在大学、科研机构和军方；安全防御呈散兵游勇状态，各机构自行管理、缺乏协调；漏洞信息通过 Usenet 新闻组（如 comp.security.unix）口耳相传，没有统一的漏洞编号或公告体系；系统管理员的安全实践高度依赖个人经验，弱密码、开放服务、默认配置是普遍问题；Morris 蠕虫的爆发并非凭空出现，而是这一时期安全状况的集中暴露
- 梳理 1960–1980 年代 Bell Labs 与 MIT 在计算机安全领域的奠基性工作——Multics 项目（1964–1969）的安全模型（分层保护环、强制访问控制）为后续 UNIX 安全提供了思想源头；丹尼斯·里奇（Dennis Ritchie）1970 年代初发明 setuid 机制（1973 年 Bell Labs 申请专利，1979 年授权，美国专利 4,135,240 "Protection of data file contents"）；MIT 的 Project Athena（1983 年启动）在分布式系统安全方面的探索；肯·汤普森（Ken Thompson）1983 年图灵奖演讲《Reflections on Trusting Trust》揭示编译器后门的哲学问题，影响深远
- 考察 UNIX 两大核心安全机制的起源与历史演化——setuid（设置用户标识符）由 丹尼斯·里奇 发明，最早出现在 UNIX V4/V5 时代，初衷是让特定程序（如 passwd）以文件所有者权限运行，从而实现最小权限原则；chroot（改变根目录）最早出现在 Unix V7（1979 年），比尔·乔伊（Bill Joy）于 1982 年 3 月 18 日将 chroot 系统调用加入 4.2BSD（早于 4.2BSD 正式发布约一年半），最初用于构建和测试发布环境，而非安全隔离；这两大机制既是 UNIX 安全的基石，也是无数漏洞的来源——setuid 程序的编写极其困难，chroot 并非为安全设计因而存在多种逃逸方式
- 还原 1980 年代黑客文化的社会语境与安全漏洞的传播生态——1983 年电影《WarGames》公映引发公众对黑客和网络安全的关注；同年 Telenet 商用数据网络发生一系列高调入侵事件，暴露了弱密码和开放访问的普遍性；Usenet 和 BBS 成为漏洞信息交换的主要渠道，黑客社区与安全社区界限模糊；Matt Bishop 1981–1983 年撰写的 UNIX 漏洞报告描述了 21 个漏洞、分为 6 大类（setuid 问题、配置问题、密码强度、信任关系、程序错误、物理安全），其中多数问题至今仍未根本解决；这一时期的漏洞披露没有固定规范，全披露（full disclosure）文化已在地下社区萌芽
- 考证 CERT/CC 成立的精确时间线——1988 年 11 月 2 日 Morris 蠕虫爆发，11 月 8 日 NCSC 召开蠕虫事后分析会议，11 月 17 日 DARPA 正式成立 CERT/CC 于卡内基梅隆大学软件工程研究所（CMU SEI），首任主任 Richard (Rich) D. Pethia；CERT 并非 "Computer Emergency Response Team" 的缩写，而是注册商标；CERT/CC 是全球第一个 CSIRT（计算机安全事件响应团队）

## 史观

- 总纲第 14 条——哲学思潮：Morris 蠕虫之前的安全状况是一种 “自然状态”——没有规则、没有机构、没有标准，每个人各自为战。这种状态的终结标志着安全从个人技艺走向制度化学科
  - 辨析：“1988 年之前没有安全研究” 是常见误解——实际上 Bell Labs、MIT、Purdue 等机构已有扎实的安全研究，但研究成果与工程实践之间存在巨大鸿沟；漏洞是已知的，但修补的激励和协调机制不存在
- 总纲第 3 条——形式主义膨胀：setuid 和 chroot 都是用极简的形式机制（一个比特位、一个系统调用）解决复杂的安全问题，它们的简洁性既是力量的源泉，也是问题的渊薮——形式化抽象越简洁，误用和被绕过的可能性就越大
  - 辨析：chroot 常被误认为是安全隔离机制，但它的设计初衷是构建环境，安全性只是 “副产品”；这一误解导致了大量基于 chroot 的不安全部署，直到 FreeBSD
- 总纲第 22 条——开源运动：CERT/CC 的成立标志着互联网安全从个人自发应对转向制度化协作，这与开源运动从个人黑客到社区协作的演进路径同构
  - 辨析：CERT/CC 成立的精确日期存在多种说法（11 月中旬、11 月底、12 月初），经交叉验证应以 11 月 17 日 DARPA 正式批准日为准；“CERT 是缩写” 的说法是常见误解，官方明确说明 CERT 是注册商标而非首字母缩写

- 总纲第 21 条——密码学：RSA 算法的发明与专利化体现了密码学从军事机密向民用技术转变过程中的法律与经济张力，BSD 系统在这一张力中寻求技术可能性与法律合规的平衡
  - 辨析：RSA 专利的到期日（2000 年 9 月）是加密软件生态的重要转折点，先前 BSD 系统需通过 RSAREF 等受限实现绕开专利，此后 OpenSSL 等自由实现得以完整包含 RSA；但专利只是制约因素之一，出口管
- 总纲第 25 条——终结与延续：SSL/TLS 从 Netscape 的商业产品演变为 IETF 开放标准，从早期脆弱的 SSL 2.0 发展到高度优化的 TLS 1.3，既是加密技术的延续，也是安全工程实践不断进化的结果
  - 辨析：LibreSSL fork 事件（2014 年 Heartbleed 后）是安全工程路线分歧的典型案例——OpenBSD 团队认为 OpenSSL 代码质量差、过

## 辨析

- “1988 年之前没有安全研究” 是常见误解——实际上 Bell Labs、MIT、Purdue 等机构已有扎实的安全研究，但研究成果与工程实践之间存在巨大鸿沟；漏洞是已知的，但修补的激励和协调机制不存在；Morris 蠕虫的真正历史意义不在于发现了新漏洞，而在于证明了互联系统的系统性风险
  - 文献：Bishop, M. (2009). *Reflections on UNIX Vulnera
- chroot 常被误认为是安全隔离机制，但它的设计初衷是构建环境，安全性只是 “副产品”；这一误解导致了大量基于 chroot 的不安全部署，直到 FreeBSD jail（2000 年）和 Linux namespaces 才真正从设计层面解决了隔离问题；setuid 机制则被反复证明是安全事故的重灾区，但至今仍无更优的普适替代方案
  - 文献：Chen, H., Wagner, D., &
- CERT/CC 成立的精确日期存在多种说法（11 月中旬、11 月底、12 月初），经交叉验证应以 11 月 17 日 DARPA 正式批准日为准；“CERT 是缩写” 的说法是常见误解，官方明确说明 CERT 是注册商标而非首字母缩写
  - 文献：Carnegie Mellon University. (2016, Sep 1). *CERT Director Richard Pethia R
- RSA 专利的到期日（2000 年 9 月）是加密软件生态的重要转折点，先前 BSD 系统需通过 RSAREF 等受限实现绕开专利，此后 OpenSSL 等自由实现得以完整包含 RSA；但专利只是制约因素之一，出口管制的影响更为深远
  - 文献：Rivest, R. L., Shamir, A., & Adleman, L. (1978). *A Method for Obtaining Dig
- LibreSSL fork 事件（2014 年 Heartbleed 后）是安全工程路线分歧的典型案例——OpenBSD 团队认为 OpenSSL 代码质量差、过度工程化，选择 fork 并大规模清理；FreeBSD 选择继续使用 OpenSSL 但加强本地安全加固；不同选择反映了不同项目的风险偏好和工程哲学
  - 文献：IETF. (2018). *RFC 8446 - The Transpo

## 文献

- Bishop, M. (2009). *Reflections on UNIX Vulnerabilities*. ACSAC '09; Vagts, B. K. (2024). Telenet, the 1983 Hacking Incidents, and the Construction of Network Security. IEEE Annals of the History of Computing, 46(1); Spafford, E. H. (1989). *The Internet Worm: Crisis and Aftermath*. Communications o
- Chen, H., Wagner, D., & Dean, D. (2002). *Setuid Demystified*. USENIX Security Symposium; McKusick, M. K. (2000). *Jails: Confining the Omnipotent Root*. BSDCon 2000; FreeBSD Project. **jail(8)** 手册页（4.4BSD 历史注释） ［A］

## 158.1.4 1980 年代黑客文化与安全漏洞

- 要点：还原 1980 年代黑客文化的社会语境与安全漏洞的传播生态——1983 年电影《WarGames
- Carnegie Mellon University. (2016, Sep 1). *CERT Director Richard Pethia Retires*. sei.cmu.edu; FIRST Organization. (2025). *Richard (Rich) D. Pethia - Hall of Fame*. first.org/hof/inductees; CERT/CC. *Frequently Asked Questions*. cert.org/faq[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费
- Rivest, R. L., Shamir, A., & Adleman, L. (1978). *A Method for Obtaining Digital Signatures and Public-Key Cryptosystems*. Communications of the ACM, 21(2); Diffie, W., & Hellman, M. E. (1976). *New Directions in Cryptography*. IEEE Transactions on Information Theory ［B］

## 158.3.2 PGP 1991 年与出口管制冲突

- IETF. (2018). *RFC 8446 - The Transport Layer Security (TLS) Protocol Version 1.3*; OpenBSD Project. (2014). *LibreSSL - Release of OpenBSD's fork of OpenSSL*. openbsd.org/56.html; Durumeric, Z. et al. (2014). *The Matter of Heartbleed*. IMC '14[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须
- OpenSSH Project. (2025). *OpenSSH Project History*. openssh.org/history.html; Ylönen, T. (1996). *SSH — Secure Login Connections over the Internet*. Proceedings of the 6th USENIX Security Symposium; OpenBSD Project. (1999, Oct 25). *Press Release: OpenSSH integrated into OpenBSD operating system*. o
- OpenBSD CVS Repository. *src/usr.bin/ssh/ initial import*. cvsweb.openbsd.org (Sep 26, 1999); OpenBSD Project. (1999). *OpenBSD 2.6 Release Notes*. openbsd.org/26.html; Provos, N. et al. (2000). *OpenSSH: Open Source Secure Shell*. USENIX Security Symposium ［B］

## 158.4.3 OpenSSH 的全球部署与安全审计传统

- 要点
- Puppy, R. F. (2000). *RFPolicy for vulnerability disclosure*. Bugtraq Mailing List; Cencini, A., Yu, K., & Chan, T. (2005). *Software Vulnerabilities: Full-, Responsible-, and Non-Disclosure*. University of Washington; Schneier, B. (2000). *Why We Disclose: Full Disclosure and Why It's Good for Secu

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
