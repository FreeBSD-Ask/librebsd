# The OpenBSD Project security page

> 任务5c 路径修复占位（2026-08-04）：原路径 04-现代研究文献/03-文献下载/衍生组采集/衍生组采集-2024-The OpenBSD Project security page.md

## b011 追加引文（2026-11-21，G7 全责线 supp-V61-b011 复用，异句异锚 J84）

> 取文：openbsd.org/security.html 经 curl 直取（11 750 字节，2026-11-21）。**同 URL 三卡披露**：库内 2011／2068／2219 三 ref 同指此页（2011 为 2007 书式旧卡、2068 为无年份旧卡），本批复用 2219（最新 EB/OL 登记卡），历史重复登记不并卡不清理（append-only）。

1. [1.11.3 用] strlcpy() and strlcat() Memory protection purify W^X .rodata segment Guard pages Randomized malloc() Randomized mmap() atexit() and stdio protection Privilege separation Privilege revocation Chroot jailing New uids ProPolice ... and others
   - **裸列表拼接披露（b011）**：原页为逐项列表（加固手段罗列），引文按列表项空白归一连续形态照录（列表项间无句读，原页形态如此）。

2. [1.11.5 用] Our proactive auditing process has really paid off. Statements like "This problem was fixed in OpenBSD about 6 months ago" have become commonplace in security forums like BUGTRAQ.
   - **q 元素披露（b011）**：原 HTML "This problem was fixed..." 系 `<q>` 元素（渲染为弯引号），引文按渲染形态照录弯引号。
