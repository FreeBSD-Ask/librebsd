# ref-anoncvs-paper 登记卡（V46 b003 新登记：Cranor／de Raadt USENIX 1999 匿名 CVS 论文）

- **来源**：Cranor C D, de Raadt T. Opening the Source Repository with Anonymous CVS[EB/OL]. (1999-06-06)[2026-11-18]. https://www.openbsd.org/papers/anoncvs-paper.pdf.
- **性质**：当事人双作者（Cranor／de Raadt）USENIX 年会论文（academic_work，1999-06-06 Monterey；slides 页自署 10-Jun-99），当事人一手陈述其建制过程。
- **取文途径**：openbsd.org 本机直连不通，经 exa 通道实取论文正文，2026-11-18 04:0x；引文逐字取自正文。
- **四键查重**：source_url（openbsd.org/papers/anoncvs-paper.pdf，库内无命中）；三元组（题名＋作者 Cranor＋1999，库内无命中）——新登记。
- **tier 依据**：source_tier=primary（当事人一手论文）；块内 claim 取 L4（当事人一手记载）。
- **用途**：V46 b003（1.2.2 建制动因／1.2.4 渠道初建——同 ref 异段）。

## 逐字引文池（供本批取用，均取自上述论文正文）

1. "In the Fall of 1995 when we started our own open source operating system project called OpenBSD, we decided to use CVS to manage the OpenBSD source tree."

2. "To resolve this conflict we created Anonymous CVS — a mechanism that lets anonymous Internet users access a source repository without compromising its security."

3. "We will present the design and implementation of the first Anonymous CVS server (used to distribute the OpenBSD operating system)."

4. "CTM ("Current Through e-Mail") is another software distribution mechanism that transfers only the changes made to a collection of files rather than entire files"

## 备注
slides 页另记 “Fall 1995: first anonymous CVS server (wistl.edu)”（wustl.edu 首服）；论文正文并记 SUP／匿名 FTP 等机制比较；本批取 1—4 条，第 4 条只作机制图景比较（CTM 系 FreeBSD 阵营机制，claim 不作“OpenBSD 以 CTM 分发自家源码”断言）。

## b012/b013 追加引文（2026-11-21/22 快照复取核证）

- **追加用途**：b013（3.4.4A）
- **披露**：链接后空格标点归一；marc 帖引用层符号剥离；apnic 页为 2021-10-28 文章快照；核心句逐字照录

A1（anA）:
Anonymous CVS is an advanced source file distribution mechanism we created to allow open source software projects to distribute source code and information about code to Internet users.

A2（anB）:
Built on top of the Concurrent Versions System (CVS) revision control system, Anonymous CVS safely allows
