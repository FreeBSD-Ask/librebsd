# FreeBSD 5.3-RELEASE Release Notes（i386）引文卡

- **著录（GB/T 7714-2015）**：THE FREEBSD PROJECT. FreeBSD 5.3-RELEASE Release Notes（i386）[EB/OL]. The FreeBSD Project, 2004-11-06[2026-11-25]. https://www.freebsd.org/releases/5.3R/relnotes-i386/.
- **来源 URL**：https://www.freebsd.org/releases/5.3R/relnotes-i386/
- **访问日期**：2026-11-25（WebFetch 直取官方页；页面 Last modified 2021-05-16 by Danilo G. Baio）
- **用途**：Task 8.2 G3 全责线 V27 b014（4.1.3B 调度器选择面）
- **tier 依据**：source_type=official_doc、source_tier=primary（项目官方发行说明，同时代发布）
- **披露**：官方页分平台，取 i386 分册“2.2 Kernel Changes”；引文逐字照录，弯引号按原页 straight quotes 归一为引号内直录

## 逐字引文

Q1（4.1.3B 源，ULE 为附加调度器且 4BSD 仍为 GENERIC 默认，同段连引）:
The ULE scheduler has been added as an additional scheduler. Note that the conventional one, which is called 4BSD, is still used as the default scheduler in the GENERIC kernel. For the average user, interactivity is reported to be better in many cases.

Q2（4.1.3B 源，SMP 每 CPU 运行队列与亲和性）:
On SMP machines, ULE has per-CPU run queues which allow for CPU affinity, CPU binding, and advanced HyperThreading support, as well as providing a framework for more optimizations in the future.

## b014-r3 追加引文（2026-11-25 快照复取核证）

- **追加用途**：b014-r3（4.4.3A／4.4.5B）
- **披露**：链接后空格标点归一；roadmap“5. X .”空格形与 ``Giant'' 双反引号、rel53 ``skipping'' 双反引号照录

A1（r53A）:
For the average user, interactivity is reported to be better in many cases. This means less ``skipping'' and ``jerking'' in interactive applications while the machine is very busy.
