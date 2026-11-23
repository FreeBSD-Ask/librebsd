# The OpenBSD Project security page

> 任务5c 路径修复占位（2026-08-04）：原路径 04-现代研究文献/03-文献下载/衍生组采集/衍生组采集-2024-The OpenBSD Project security page.md

## b011 追加引文（2026-11-21，G7 全责线 supp-V61-b011 复用，异句异锚 J84）

> 取文：openbsd.org/security.html 经 curl 直取（11 750 字节，2026-11-21）。**同 URL 三卡披露**：库内 2011／2068／2219 三 ref 同指此页（2011 为 2007 书式旧卡、2068 为无年份旧卡），本批复用 2219（最新 EB/OL 登记卡），历史重复登记不并卡不清理（append-only）。

1. [1.11.3 用] strlcpy() and strlcat() Memory protection purify W^X .rodata segment Guard pages Randomized malloc() Randomized mmap() atexit() and stdio protection Privilege separation Privilege revocation Chroot jailing New uids ProPolice ... and others
   - **裸列表拼接披露（b011）**：原页为逐项列表（加固手段罗列），引文按列表项空白归一连续形态照录（列表项间无句读，原页形态如此）。

2. [1.11.5 用] Our proactive auditing process has really paid off. Statements like "This problem was fixed in OpenBSD about 6 months ago" have become commonplace in security forums like BUGTRAQ.
   - **q 元素披露（b011）**：原 HTML "This problem was fixed..." 系 `<q>` 元素（渲染为弯引号），引文按渲染形态照录弯引号。

## b012/b013 追加引文（2026-11-21/22 快照复取核证）

- **追加用途**：b013（3.3.2A／3.4.2B／3.4.3B／3.4.5A／3.5.1A／3.5.2A／3.5.3A／3.5.5A/B／3.6.3A／3.6.5A/B／3.7.5A）
- **披露**：链接后空格标点归一；marc 帖引用层符号剥离；apnic 页为 2021-10-28 文章快照；核心句逐字照录

A1（secA）:
We have been auditing since the summer of 1996.

A2（secB）:
The process we follow to increase security is simply a comprehensive file-by-file analysis of every critical software component.

A3（secC）:
Our security auditing team typically has between six and twelve members who continue to search for and fix new security holes.

A4（secD）:
we ship the operating system in a Secure by Default mode. All non-essential services are disabled.

A5（secE）:
since OpenBSD is exported with cryptography, we are able to take cryptographic approaches towards fixing security problems

A6（secF）:
The most intense part of our security auditing happened immediately before the OpenBSD 2.0 release and during the 2.0→2.1 transition, over the last third of 1996 and first half of 1997.

A7（secG）:
Thousands (yes, thousands) of security issues were fixed rapidly over this year-long period

A8（secH）:
we believe in full disclosure of security problems. In the operating system arena, we were probably the first to embrace the concept.

A9（secI）:
The auditing process is not over yet, and as you can see we continue to find and fix new security flaws.

A10（secJ）:
Recently the security problems we find and fix tend to be significantly more obscure or complicated.

A11（secK）:
OpenBSD passed Ballista's tests with flying colours since day 1

A12（secL）:
Statements like This problem was fixed in OpenBSD about 6 months ago have become commonplace in security forums like BUGTRAQ
